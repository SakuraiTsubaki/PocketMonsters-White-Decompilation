#!/usr/bin/env python3
"""Build one reconstructed ARM9 overlay and byte-compare it with a supplied ROM."""

from __future__ import annotations

import argparse
import hashlib
import struct
import subprocess
import tempfile
from pathlib import Path

from nds_code_compression import decompress_backward


def u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def extract_arm9_overlay(rom: bytes, overlay_id: int) -> tuple[bytes, dict[str, int]]:
    overlay_table_offset = u32(rom, 0x50)
    overlay_table_size = u32(rom, 0x54)
    fat_offset = u32(rom, 0x48)
    entry_count = overlay_table_size // 32
    if not 0 <= overlay_id < entry_count:
        raise ValueError(f"overlay {overlay_id} outside 0..{entry_count - 1}")

    entry = struct.unpack_from("<8I", rom, overlay_table_offset + overlay_id * 32)
    actual_id, ram_address, ram_size, bss_size, init_start, init_end, file_id, packed = entry
    if actual_id != overlay_id:
        raise ValueError(f"overlay-table index {overlay_id} contains ID {actual_id}")

    start, end = struct.unpack_from("<II", rom, fat_offset + file_id * 8)
    raw = rom[start:end]
    expanded, compressed = decompress_backward(raw)
    if len(expanded) != ram_size:
        raise ValueError(f"expanded size {len(expanded)} != table RAM size {ram_size}")

    return expanded, {
        "file_id": file_id,
        "ram_address": ram_address,
        "ram_size": ram_size,
        "bss_size": bss_size,
        "init_start": init_start,
        "init_end": init_end,
        "compressed": int(compressed),
        "raw_size": len(raw),
        "packed_field": packed,
    }


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("rom", type=Path)
    parser.add_argument("overlay_id", type=int)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--linker", type=Path, required=True)
    parser.add_argument("--clang", default="clang")
    parser.add_argument("--lld", default="ld.lld")
    parser.add_argument("--objcopy", default="llvm-objcopy")
    args = parser.parse_args()

    rom = args.rom.read_bytes()
    expected, metadata = extract_arm9_overlay(rom, args.overlay_id)

    with tempfile.TemporaryDirectory(prefix=f"overlay_{args.overlay_id:04d}_") as temporary:
        directory = Path(temporary)
        obj = directory / "overlay.o"
        elf = directory / "overlay.elf"
        binary = directory / "overlay.bin"

        subprocess.run(
            [args.clang, "--target=armv5te-none-eabi", "-mthumb", "-c", str(args.source), "-o", str(obj)],
            check=True,
        )
        subprocess.run([args.lld, "-T", str(args.linker), str(obj), "-o", str(elf)], check=True)
        subprocess.run([args.objcopy, "-O", "binary", str(elf), str(binary)], check=True)
        rebuilt = binary.read_bytes()

    print(f"overlay_id={args.overlay_id}")
    print(f"game_code={rom[0x0C:0x10].decode('ascii', 'replace')}")
    print(f"load_address=0x{metadata['ram_address']:08X}")
    print(f"expected_size={len(expected)} rebuilt_size={len(rebuilt)}")
    print(f"expected_sha256={sha256(expected)}")
    print(f"rebuilt_sha256={sha256(rebuilt)}")
    matched = rebuilt == expected
    print(f"byte_match={'true' if matched else 'false'}")
    return 0 if matched else 1


if __name__ == "__main__":
    raise SystemExit(main())
