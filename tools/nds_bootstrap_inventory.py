#!/usr/bin/env python3
"""Generate a reproducible Nintendo DS bootstrap inventory without redistributing ROM data."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import zlib
from pathlib import Path


def u16(data: bytes, offset: int) -> int:
    return struct.unpack_from("<H", data, offset)[0]


def u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def digest(data: bytes) -> dict[str, str]:
    return {
        "crc32": f"{zlib.crc32(data) & 0xFFFFFFFF:08X}",
        "md5": hashlib.md5(data).hexdigest(),
        "sha1": hashlib.sha1(data).hexdigest(),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def parse_fat(data: bytes, offset: int, size: int) -> list[dict]:
    files = []
    for file_id in range(size // 8):
        start, end = struct.unpack_from("<II", data, offset + file_id * 8)
        blob = data[start:end]
        files.append(
            {
                "file_id": file_id,
                "start": start,
                "end": end,
                "size": end - start,
                "sha256": hashlib.sha256(blob).hexdigest(),
            }
        )
    return files


def parse_fnt(data: bytes, offset: int, size: int, file_count: int) -> dict[int, str]:
    fnt = data[offset : offset + size]
    if len(fnt) < 8:
        return {}

    _, _, directory_count = struct.unpack_from("<IHH", fnt, 0)
    directories = []
    for index in range(directory_count):
        sub_offset, first_file_id, parent_id = struct.unpack_from("<IHH", fnt, index * 8)
        directories.append((0xF000 + index, sub_offset, first_file_id, parent_id))

    children: dict[int, list[tuple[str, str, int]]] = {entry[0]: [] for entry in directories}
    for directory_id, sub_offset, first_file_id, _ in directories:
        cursor = sub_offset
        file_id = first_file_id
        while cursor < len(fnt):
            descriptor = fnt[cursor]
            cursor += 1
            if descriptor == 0:
                break
            is_directory = bool(descriptor & 0x80)
            name_length = descriptor & 0x7F
            name = fnt[cursor : cursor + name_length].decode("ascii", "replace")
            cursor += name_length
            if is_directory:
                child_id = u16(fnt, cursor)
                cursor += 2
                children.setdefault(directory_id, []).append(("dir", name, child_id))
            else:
                if file_id < file_count:
                    children.setdefault(directory_id, []).append(("file", name, file_id))
                file_id += 1

    paths: dict[int, str] = {}

    def walk(directory_id: int, prefix: str = "") -> None:
        for kind, name, identifier in children.get(directory_id, []):
            path = f"{prefix}/{name}" if prefix else name
            if kind == "file":
                paths[identifier] = path
            else:
                walk(identifier, path)

    walk(0xF000)
    return paths


def parse_overlays(data: bytes, offset: int, size: int, fat: list[dict]) -> list[dict]:
    overlays = []
    if not offset or not size:
        return overlays
    for index in range(size // 32):
        values = struct.unpack_from("<8I", data, offset + index * 32)
        overlay_id, ram_address, ram_size, bss_size, init_start, init_end, file_id, packed = values
        row = {
            "index": index,
            "overlay_id": overlay_id,
            "ram_address": ram_address,
            "ram_size": ram_size,
            "bss_size": bss_size,
            "static_init_start": init_start,
            "static_init_end": init_end,
            "file_id": file_id,
            "compressed_size": packed & 0x00FFFFFF,
            "flags_byte": (packed >> 24) & 0xFF,
        }
        if file_id < len(fat):
            row["file_size"] = fat[file_id]["size"]
            row["file_sha256"] = fat[file_id]["sha256"]
        overlays.append(row)
    return overlays


def parse_narc_count(blob: bytes) -> int | None:
    if len(blob) < 0x1C or blob[:4] != b"NARC":
        return None
    header_size = u16(blob, 0x0C)
    if blob[header_size : header_size + 4] not in (b"BTAF", b"FATB"):
        return None
    return u16(blob, header_size + 8)


def inventory(path: Path) -> dict:
    data = path.read_bytes()
    header = {
        "game_title": data[0:12].rstrip(b"\0").decode("ascii", "replace"),
        "game_code": data[0x0C:0x10].decode("ascii", "replace"),
        "maker_code": data[0x10:0x12].decode("ascii", "replace"),
        "unit_code": data[0x12],
        "device_capacity_code": data[0x14],
        "rom_version": data[0x1E],
        "arm9": {
            "rom_offset": u32(data, 0x20),
            "entry_address": u32(data, 0x24),
            "ram_address": u32(data, 0x28),
            "size": u32(data, 0x2C),
        },
        "arm7": {
            "rom_offset": u32(data, 0x30),
            "entry_address": u32(data, 0x34),
            "ram_address": u32(data, 0x38),
            "size": u32(data, 0x3C),
        },
        "fnt": {"offset": u32(data, 0x40), "size": u32(data, 0x44)},
        "fat": {"offset": u32(data, 0x48), "size": u32(data, 0x4C)},
        "arm9_overlay": {"offset": u32(data, 0x50), "size": u32(data, 0x54)},
        "arm7_overlay": {"offset": u32(data, 0x58), "size": u32(data, 0x5C)},
        "banner_offset": u32(data, 0x68),
        "rom_size_field": u32(data, 0x80),
        "header_size": u32(data, 0x84),
    }

    fat = parse_fat(data, header["fat"]["offset"], header["fat"]["size"])
    paths = parse_fnt(data, header["fnt"]["offset"], header["fnt"]["size"], len(fat))
    for row in fat:
        row["path"] = paths.get(row["file_id"])

    for key in ("arm9", "arm7"):
        start = header[key]["rom_offset"]
        size = header[key]["size"]
        header[key]["sha256"] = hashlib.sha256(data[start : start + size]).hexdigest()

    narcs = []
    for row in fat:
        if row["path"] is None:
            continue
        member_count = parse_narc_count(data[row["start"] : row["end"]])
        if member_count is not None:
            narcs.append(
                {
                    "file_id": row["file_id"],
                    "path": row["path"],
                    "size": row["size"],
                    "sha256": row["sha256"],
                    "member_count": member_count,
                }
            )

    return {
        "schema": "gen5-nds-bootstrap-inventory-v1",
        "rom_identity": {"size": len(data), **digest(data)},
        "header": header,
        "filesystem": {
            "file_count": len(fat),
            "named_file_count": len(paths),
            "files": fat,
        },
        "overlays": {
            "arm9": parse_overlays(data, header["arm9_overlay"]["offset"], header["arm9_overlay"]["size"], fat),
            "arm7": parse_overlays(data, header["arm7_overlay"]["offset"], header["arm7_overlay"]["size"], fat),
        },
        "narc_archives": narcs,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("rom", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()
    result = inventory(args.rom)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
