#!/usr/bin/env python3
"""Deterministic Nintendo DS ROM structural audit.

This tool never modifies or redistributes ROM bytes. It records hashes, header
integrity, ARM regions, NitroFS/FAT bounds, FNT paths, and overlay metadata so a
specific build can be reproduced and compared before/after fixes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import struct
from pathlib import Path

U16 = struct.Struct("<H")
U32 = struct.Struct("<I")


def u16(buf: bytes, off: int) -> int:
    return U16.unpack_from(buf, off)[0]


def u32(buf: bytes, off: int) -> int:
    return U32.unpack_from(buf, off)[0]


def crc16_nintendo(data: bytes) -> int:
    crc = 0xFFFF
    for value in data:
        crc ^= value
        for _ in range(8):
            crc = (crc >> 1) ^ (0xA001 if crc & 1 else 0)
    return crc & 0xFFFF


def stream_hashes(path: Path) -> dict[str, str]:
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(8 * 1024 * 1024)
            if not chunk:
                break
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)
    return {"md5": md5.hexdigest(), "sha1": sha1.hexdigest(), "sha256": sha256.hexdigest()}


def hash_range(f, start: int, end: int) -> str:
    h = hashlib.sha256()
    f.seek(start)
    remaining = max(0, end - start)
    while remaining:
        chunk = f.read(min(1024 * 1024, remaining))
        if not chunk:
            break
        h.update(chunk)
        remaining -= len(chunk)
    return h.hexdigest()


def parse_fnt(f, fnt_off: int, fnt_size: int) -> dict[int, str]:
    if fnt_size < 8:
        return {}
    f.seek(fnt_off)
    data = f.read(fnt_size)
    if len(data) != fnt_size:
        return {}
    dir_count = u16(data, 6)
    if not dir_count or dir_count * 8 > len(data):
        return {}

    dirs: dict[int, tuple[int, int]] = {}
    for i in range(dir_count):
        off = i * 8
        sub_off = u32(data, off)
        first_file = u16(data, off + 4)
        dirs[0xF000 + i] = (sub_off, first_file)

    paths: dict[int, str] = {}
    visited: set[int] = set()

    def walk(dir_id: int, prefix: str) -> None:
        if dir_id in visited or dir_id not in dirs:
            return
        visited.add(dir_id)
        pos, file_id = dirs[dir_id]
        if pos >= len(data):
            return
        while pos < len(data):
            n = data[pos]
            pos += 1
            if n == 0:
                return
            is_dir = bool(n & 0x80)
            name_len = n & 0x7F
            if pos + name_len > len(data):
                return
            raw = data[pos:pos + name_len]
            pos += name_len
            name = raw.decode("ascii", "replace")
            if is_dir:
                if pos + 2 > len(data):
                    return
                child = u16(data, pos)
                pos += 2
                walk(child, prefix + name + "/")
            else:
                paths[file_id] = prefix + name
                file_id += 1

    walk(0xF000, "")
    return paths


def parse_overlays(f, off: int, size: int, fat_count: int) -> list[dict]:
    out = []
    if not off or not size:
        return out
    if size % 32:
        out.append({"error": "overlay table size is not a multiple of 32", "offset": off, "size": size})
        return out
    f.seek(off)
    data = f.read(size)
    if len(data) != size:
        return [{"error": "overlay table truncated", "offset": off, "size": size}]
    for i in range(0, size, 32):
        vals = struct.unpack_from("<8I", data, i)
        packed = vals[7]
        out.append({
            "overlay_id": vals[0],
            "ram_address": vals[1],
            "ram_size": vals[2],
            "bss_size": vals[3],
            "static_init_start": vals[4],
            "static_init_end": vals[5],
            "file_id": vals[6],
            "compressed_size": packed & 0x00FFFFFF,
            "flags": packed >> 24,
            "file_id_in_range": vals[6] < fat_count,
        })
    return out


def audit(path: Path, include_file_hashes: bool = True) -> dict:
    size = path.stat().st_size
    hashes = stream_hashes(path)
    anomalies: list[str] = []

    with path.open("rb") as f:
        header = f.read(min(size, 0x1000))
        if len(header) < 0x160:
            raise ValueError("file is too small to contain a valid NDS header")

        title = header[0:12].rstrip(b"\0").decode("ascii", "replace")
        game_code = header[0x0C:0x10].decode("ascii", "replace")
        maker_code = header[0x10:0x12].decode("ascii", "replace")
        unit_code = header[0x12]
        device_capacity = header[0x14]
        game_version = header[0x1E]

        arm9_off, arm9_entry, arm9_ram, arm9_size = struct.unpack_from("<4I", header, 0x20)
        arm7_off, arm7_entry, arm7_ram, arm7_size = struct.unpack_from("<4I", header, 0x30)
        fnt_off, fnt_size, fat_off, fat_size = struct.unpack_from("<4I", header, 0x40)
        arm9_ovt_off, arm9_ovt_size, arm7_ovt_off, arm7_ovt_size = struct.unpack_from("<4I", header, 0x50)
        banner_off = u32(header, 0x68)

        logo_crc_stored = u16(header, 0x15C)
        header_crc_stored = u16(header, 0x15E)
        logo_crc_calc = crc16_nintendo(header[0xC0:0x15C])
        header_crc_calc = crc16_nintendo(header[0:0x15E])

        for label, off, length in (
            ("ARM9", arm9_off, arm9_size),
            ("ARM7", arm7_off, arm7_size),
            ("FNT", fnt_off, fnt_size),
            ("FAT", fat_off, fat_size),
            ("ARM9 overlay table", arm9_ovt_off, arm9_ovt_size),
            ("ARM7 overlay table", arm7_ovt_off, arm7_ovt_size),
        ):
            if off + length > size:
                anomalies.append(f"{label} exceeds ROM size: 0x{off:X}+0x{length:X} > 0x{size:X}")

        if fat_size % 8:
            anomalies.append("FAT size is not divisible by 8")
        fat_count = fat_size // 8
        fat_entries = []
        f.seek(fat_off)
        fat_raw = f.read(fat_size) if fat_off + fat_size <= size else b""
        if len(fat_raw) != fat_size:
            anomalies.append("FAT is truncated")
        else:
            for file_id in range(fat_count):
                start, end = struct.unpack_from("<2I", fat_raw, file_id * 8)
                valid = start <= end <= size
                if not valid:
                    anomalies.append(f"FAT file {file_id} has invalid range 0x{start:X}-0x{end:X}")
                fat_entries.append({"file_id": file_id, "start": start, "end": end, "size": max(0, end - start), "valid": valid})

        fnt_paths = parse_fnt(f, fnt_off, fnt_size) if fnt_off + fnt_size <= size else {}
        if fnt_paths and max(fnt_paths, default=-1) >= fat_count:
            anomalies.append("FNT refers to a file ID outside the FAT")

        seen_ranges: dict[tuple[int, int], int] = {}
        files = []
        for entry in fat_entries:
            key = (entry["start"], entry["end"])
            duplicate_of = seen_ranges.get(key)
            if duplicate_of is None:
                seen_ranges[key] = entry["file_id"]
            item = dict(entry)
            item["path"] = fnt_paths.get(entry["file_id"])
            item["duplicate_range_of"] = duplicate_of
            if include_file_hashes and entry["valid"]:
                item["sha256"] = hash_range(f, entry["start"], entry["end"])
            files.append(item)

        arm9_sha = hash_range(f, arm9_off, arm9_off + arm9_size) if arm9_off + arm9_size <= size else None
        arm7_sha = hash_range(f, arm7_off, arm7_off + arm7_size) if arm7_off + arm7_size <= size else None
        arm9_overlays = parse_overlays(f, arm9_ovt_off, arm9_ovt_size, fat_count)
        arm7_overlays = parse_overlays(f, arm7_ovt_off, arm7_ovt_size, fat_count)

    declared_capacity = (128 * 1024) << device_capacity if device_capacity < 32 else None
    return {
        "path": str(path),
        "size": size,
        "hashes": hashes,
        "header": {
            "title": title,
            "game_code": game_code,
            "maker_code": maker_code,
            "unit_code": unit_code,
            "device_capacity_code": device_capacity,
            "declared_capacity_bytes": declared_capacity,
            "game_version": game_version,
            "banner_offset": banner_off,
            "logo_crc": {"stored": logo_crc_stored, "calculated": logo_crc_calc, "ok": logo_crc_stored == logo_crc_calc},
            "header_crc": {"stored": header_crc_stored, "calculated": header_crc_calc, "ok": header_crc_stored == header_crc_calc},
        },
        "arm9": {"rom_offset": arm9_off, "entry": arm9_entry, "ram_address": arm9_ram, "size": arm9_size, "sha256": arm9_sha},
        "arm7": {"rom_offset": arm7_off, "entry": arm7_entry, "ram_address": arm7_ram, "size": arm7_size, "sha256": arm7_sha},
        "nitrofs": {"fnt_offset": fnt_off, "fnt_size": fnt_size, "fat_offset": fat_off, "fat_size": fat_size, "fat_count": fat_count, "named_file_count": len(fnt_paths), "files": files},
        "overlays": {"arm9_table_offset": arm9_ovt_off, "arm9_table_size": arm9_ovt_size, "arm9": arm9_overlays, "arm7_table_offset": arm7_ovt_off, "arm7_table_size": arm7_ovt_size, "arm7": arm7_overlays},
        "anomalies": anomalies,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("rom", type=Path)
    ap.add_argument("-o", "--output", type=Path)
    ap.add_argument("--no-file-hashes", action="store_true")
    args = ap.parse_args()
    report = audit(args.rom, include_file_hashes=not args.no_file_hashes)
    text = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 1 if report["anomalies"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
