#!/usr/bin/env python3
"""Decode Pokémon Black/White /a/1/7/8 Pokédex-area NARC.

Input is an extracted NARC file, not a retail ROM. Produces one CSV row per
National Pokédex species (001-649) with four seasonal 61-area bitmask tables.
"""
from __future__ import annotations
import argparse, csv, struct
from pathlib import Path

METHODS = {
    0x01: "grass_cave",
    0x02: "doubles_grass",
    0x04: "shaking_spots",
    0x08: "surfing",
    0x10: "surfing_spots",
    0x20: "fishing",
    0x40: "fishing_spots",
}
SEASONS = ("spring", "summer", "autumn", "winter")
BW_MEMBER_LEN = 249
BW_AREA_COUNT = 61


def read_narc(path: Path) -> list[bytes]:
    data = path.read_bytes()
    if data[:4] != b"NARC":
        raise ValueError("not a NARC archive")
    block_count = struct.unpack_from("<H", data, 0x0E)[0]
    off = struct.unpack_from("<H", data, 0x0C)[0]
    fat_entries = None
    image = None
    for _ in range(block_count):
        tag = data[off:off+4]
        size = struct.unpack_from("<I", data, off+4)[0]
        payload = data[off+8:off+size]
        if tag in (b"BTAF", b"FATB"):
            count = struct.unpack_from("<H", payload, 0)[0]
            fat_entries = [struct.unpack_from("<II", payload, 4+i*8) for i in range(count)]
        elif tag in (b"GMIF", b"FIMG"):
            image = payload
        off += size
    if fat_entries is None or image is None:
        raise ValueError("NARC lacks FAT/image blocks")
    return [image[start:end] for start, end in fat_entries]


def compact_mask_list(block: bytes) -> str:
    parts = []
    for area, mask in enumerate(block[1:], start=0):
        if mask:
            names = "+".join(name for bit, name in METHODS.items() if mask & bit)
            parts.append(f"{area}:{mask:#04x}:{names}")
    return ";".join(parts)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("narc", type=Path)
    ap.add_argument("output_csv", type=Path)
    args = ap.parse_args()

    members = read_narc(args.narc)
    if len(members) != 649:
        raise ValueError(f"expected 649 BW members, got {len(members)}")
    bad = [i for i, m in enumerate(members) if len(m) != BW_MEMBER_LEN]
    if bad:
        raise ValueError(f"members not {BW_MEMBER_LEN} bytes: {bad[:10]}")

    fields = ["species_id", "season_independent_flag"]
    for season in SEASONS:
        fields += [f"{season}_unobtainable", f"{season}_area_masks"]

    with args.output_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for species_id, member in enumerate(members, start=1):
            row = {"species_id": species_id, "season_independent_flag": member[0]}
            for s, season in enumerate(SEASONS):
                start = 1 + s * (BW_AREA_COUNT + 1)
                block = member[start:start + BW_AREA_COUNT + 1]
                row[f"{season}_unobtainable"] = block[0]
                row[f"{season}_area_masks"] = compact_mask_list(block)
            w.writerow(row)


if __name__ == "__main__":
    main()
