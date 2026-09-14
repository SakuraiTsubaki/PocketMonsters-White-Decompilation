#!/usr/bin/env python3
"""Inventory an NDS ROM without modifying it.

Outputs header identity, FNT/FAT structure, named NitroFS files, ARM9 overlay
file IDs, and NARC member hashes. Retail ROM bytes are never written to the
repository by this tool; its intended output is reproducible metadata.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import struct
import zlib


def u16(data: bytes, offset: int) -> int:
    return struct.unpack_from("<H", data, offset)[0]


def u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def parse_fnt(rom: bytes, offset: int, size: int) -> dict[int, str]:
    fnt = rom[offset : offset + size]
    directory_count = u16(fnt, 6)
    directories = []
    for index in range(directory_count):
        base = index * 8
        directories.append((u32(fnt, base), u16(fnt, base + 4), u16(fnt, base + 6)))

    children: dict[int, list[tuple[str, int]]] = {i: [] for i in range(directory_count)}
    files: dict[int, tuple[int, str]] = {}
    for index, (subtable, first_file_id, _parent) in enumerate(directories):
        pos = subtable
        file_id = first_file_id
        while pos < len(fnt):
            control = fnt[pos]
            pos += 1
            if control == 0:
                break
            is_directory = bool(control & 0x80)
            name_length = control & 0x7F
            name = fnt[pos : pos + name_length].decode("ascii", "replace")
            pos += name_length
            if is_directory:
                directory_id = u16(fnt, pos) - 0xF000
                pos += 2
                children[index].append((name, directory_id))
            else:
                files[file_id] = (index, name)
                file_id += 1

    paths = {0: ""}
    stack = [0]
    while stack:
        parent = stack.pop()
        for name, child in children.get(parent, []):
            paths[child] = (paths[parent] + "/" + name).strip("/")
            stack.append(child)

    return {
        file_id: (paths.get(directory, "") + "/" + name).strip("/")
        for file_id, (directory, name) in files.items()
    }


def parse_narc(data: bytes) -> dict | None:
    if data[:4] != b"NARC":
        return None

    header_size = u16(data, 12)
    block_count = u16(data, 14)
    pos = header_size
    sections = []
    fat_entries = None

    for _ in range(block_count):
        magic = data[pos : pos + 4]
        section_size = u32(data, pos + 4)
        sections.append((magic, pos, section_size))
        if magic in (b"BTAF", b"FATB"):
            count = u16(data, pos + 8)
            table = pos + 12
            fat_entries = [
                (u32(data, table + i * 8), u32(data, table + i * 8 + 4))
                for i in range(count)
            ]
        pos += section_size

    image = next((section for section in sections if section[0] in (b"GMIF", b"FIMG")), None)
    members = []
    if image is not None and fat_entries is not None:
        base = image[1] + 8
        for index, (start, end) in enumerate(fat_entries):
            member = data[base + start : base + end]
            members.append(
                {
                    "index": index,
                    "size": len(member),
                    "sha1": hashlib.sha1(member).hexdigest(),
                    "magic_hex": member[:4].hex(),
                }
            )

    return {
        "header_size": header_size,
        "block_count": block_count,
        "sections": [section[0].decode("ascii", "replace") for section in sections],
        "member_count": len(members),
        "members": members,
    }


def scan(path: str) -> dict:
    with open(path, "rb") as handle:
        rom = handle.read()

    header = rom[:0x4000]
    fnt_offset = u32(header, 0x40)
    fnt_size = u32(header, 0x44)
    fat_offset = u32(header, 0x48)
    fat_size = u32(header, 0x4C)
    overlay9_offset = u32(header, 0x50)
    overlay9_size = u32(header, 0x54)

    names = parse_fnt(rom, fnt_offset, fnt_size)
    fat = [
        (u32(rom, fat_offset + i * 8), u32(rom, fat_offset + i * 8 + 4))
        for i in range(fat_size // 8)
    ]
    overlay_file_ids = {
        u32(rom, overlay9_offset + i * 32 + 24)
        for i in range(overlay9_size // 32)
    }

    files = []
    narcs = []
    for file_id, path_name in sorted(names.items()):
        start, end = fat[file_id]
        blob = rom[start:end]
        narc = parse_narc(blob)
        kind = "NARC" if narc else ("SDAT" if blob[:4] == b"SDAT" else "other")
        record = {
            "file_id": file_id,
            "path": path_name,
            "offset": start,
            "size": end - start,
            "sha1": hashlib.sha1(blob).hexdigest(),
            "kind": kind,
            "is_arm9_overlay_file": file_id in overlay_file_ids,
        }
        files.append(record)
        if narc:
            narcs.append({**record, **narc})

    return {
        "source_filename": os.path.basename(path),
        "size_bytes": len(rom),
        "crc32": f"{zlib.crc32(rom) & 0xFFFFFFFF:08X}",
        "md5": hashlib.md5(rom).hexdigest().upper(),
        "sha1": hashlib.sha1(rom).hexdigest().upper(),
        "sha256": hashlib.sha256(rom).hexdigest().upper(),
        "header": {
            "internal_title": header[:12].rstrip(b"\0").decode("ascii", "replace"),
            "game_code": header[12:16].decode("ascii", "replace"),
            "maker_code": header[16:18].decode("ascii", "replace"),
            "unit_code": header[18],
            "revision": header[30],
            "fnt_offset": fnt_offset,
            "fnt_size": fnt_size,
            "fat_offset": fat_offset,
            "fat_size": fat_size,
            "arm9_overlay_offset": overlay9_offset,
            "arm9_overlay_size": overlay9_size,
        },
        "counts": {
            "fat_entries": len(fat),
            "named_nitrofs_files": len(files),
            "arm9_overlays": overlay9_size // 32,
            "narc_archives": len(narcs),
        },
        "files": files,
        "narcs": narcs,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("rom", help="path to an NDS ROM used as read-only input")
    parser.add_argument("-o", "--output", help="output JSON path; defaults to <rom>.scan.json")
    args = parser.parse_args()
    output = args.output or (args.rom + ".scan.json")
    with open(output, "w", encoding="utf-8") as handle:
        json.dump(scan(args.rom), handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    print(output)


if __name__ == "__main__":
    main()
