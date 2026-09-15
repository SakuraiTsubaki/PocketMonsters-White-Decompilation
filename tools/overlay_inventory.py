#!/usr/bin/env python3
"""Inventory every ARM9 overlay in a Nintendo DS ROM."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

from nds_code_compression import decompress_backward


def u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_inventory(rom: bytes) -> dict:
    overlay_table_offset = u32(rom, 0x50)
    overlay_table_size = u32(rom, 0x54)
    fat_offset = u32(rom, 0x48)
    count = overlay_table_size // 32

    entries = []
    for index in range(count):
        values = struct.unpack_from("<8I", rom, overlay_table_offset + index * 32)
        overlay_id, ram_address, ram_size, bss_size, init_start, init_end, file_id, packed = values
        start, end = struct.unpack_from("<II", rom, fat_offset + file_id * 8)
        raw = rom[start:end]
        expanded, was_compressed = decompress_backward(raw)
        if len(expanded) != ram_size:
            raise ValueError(
                f"overlay {overlay_id}: expanded size {len(expanded)} != declared RAM size {ram_size}"
            )
        entries.append(
            {
                "index": index,
                "overlay_id": overlay_id,
                "file_id": file_id,
                "ram_address": f"0x{ram_address:08X}",
                "ram_size": ram_size,
                "bss_size": bss_size,
                "static_init_start": f"0x{init_start:08X}",
                "static_init_end": f"0x{init_end:08X}",
                "file_size": len(raw),
                "compressed_size_field": packed & 0x00FFFFFF,
                "flags_byte": (packed >> 24) & 0xFF,
                "backwards_compressed": was_compressed,
                "raw_sha256": sha256(raw),
                "expanded_sha256": sha256(expanded),
                "zero_filled": bool(expanded) and not any(expanded),
            }
        )

    return {
        "schema": "gen5-arm9-overlay-inventory-v1",
        "game_title": rom[0:12].rstrip(b"\0").decode("ascii", "replace"),
        "game_code": rom[0x0C:0x10].decode("ascii", "replace"),
        "rom_version": rom[0x1E],
        "overlay_table_offset": f"0x{overlay_table_offset:08X}",
        "overlay_table_size": overlay_table_size,
        "overlay_count": count,
        "compressed_count": sum(1 for entry in entries if entry["backwards_compressed"]),
        "uncompressed_count": sum(1 for entry in entries if not entry["backwards_compressed"]),
        "zero_filled_count": sum(1 for entry in entries if entry["zero_filled"]),
        "overlays": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("rom", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()
    result = build_inventory(args.rom.read_bytes())
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
