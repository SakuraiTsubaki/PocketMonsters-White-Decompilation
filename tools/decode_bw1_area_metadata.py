#!/usr/bin/env python3
"""Decode Pokémon Black/White (BW1) /a/0/8/6 area metadata.

Input may be either the NARC archive itself or its single extracted member.
The BW1 payload is 3294 bytes: 61 records * 54 bytes, 27 little-endian u16
values per record.

Provisional field names are analysis labels. Only representative_zone_id and
the exact arithmetic/constant relations documented in Phase 4 are considered
confirmed at this stage.
"""

from __future__ import annotations
import argparse
import csv
import struct
from pathlib import Path

RECORD_COUNT = 61
RECORD_SIZE = 54
FIELD_COUNT = 27
PAYLOAD_SIZE = RECORD_COUNT * RECORD_SIZE

NAMES = [
    "representative_zone_id", "constant_1", "map_center_x_candidate",
    "map_center_y_candidate", "map_center_x_dup", "map_center_y_dup",
    "map_center_x_dup2", "map_center_y_minus4", "map_center_x_dup3",
    "map_center_y_plus4", "constant_8", "display_class_candidate",
    "has_fly_flag_candidate", "constant_0_a", "constant_0_b",
    "fly_unlock_flag_candidate", "special_condition_id_candidate",
    "map_component_id_0", "map_component_id_1", "map_component_id_2",
    "map_component_id_3", "map_component_id_4", "map_component_id_5",
    "map_component_id_6", "shape_or_style_code_candidate",
    "label_anchor_x_candidate", "label_anchor_y_candidate",
]


def u16(buf: bytes, off: int) -> int:
    return struct.unpack_from("<H", buf, off)[0]


def u32(buf: bytes, off: int) -> int:
    return struct.unpack_from("<I", buf, off)[0]


def unpack_single_member_narc(data: bytes) -> bytes:
    if data[:4] != b"NARC":
        return data
    header_size = u16(data, 0x0C)
    section_count = u16(data, 0x0E)
    pos = header_size
    fat_offsets = None
    fimg_data = None
    for _ in range(section_count):
        magic = data[pos:pos + 4]
        size = u32(data, pos + 4)
        if magic == b"BTAF":
            count = u16(data, pos + 8)
            if count != 1:
                raise ValueError(f"Expected one NARC member, got {count}")
            start = u32(data, pos + 12)
            end = u32(data, pos + 16)
            fat_offsets = (start, end)
        elif magic == b"GMIF":
            fimg_data = data[pos + 8:pos + size]
        pos += size
    if fat_offsets is None or fimg_data is None:
        raise ValueError("Incomplete NARC")
    start, end = fat_offsets
    return fimg_data[start:end]


def decode(payload: bytes):
    if len(payload) != PAYLOAD_SIZE:
        raise ValueError(f"Expected {PAYLOAD_SIZE} bytes (61*54), got {len(payload)}")
    rows = []
    for area in range(RECORD_COUNT):
        base = area * RECORD_SIZE
        values = struct.unpack_from("<27H", payload, base)
        row = {"area_index": area}
        for idx, value in enumerate(values):
            row[f"u16_{idx:02d}"] = value
            row[NAMES[idx]] = value
        rows.append(row)
    return rows


def validate(rows):
    for r in rows:
        assert r["u16_01"] == 1
        assert r["u16_02"] == r["u16_04"] == r["u16_06"] == r["u16_08"]
        assert r["u16_03"] == r["u16_05"]
        assert r["u16_07"] == r["u16_03"] - 4
        assert r["u16_09"] == r["u16_03"] + 4
        assert r["u16_10"] == 8
        assert r["u16_13"] == 0
        assert r["u16_14"] == 0
        assert (r["u16_12"] == 1) == (r["u16_15"] != 0xFFFF)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path, help="/a/0/8/6 NARC or extracted member")
    ap.add_argument("output", type=Path, help="output CSV")
    args = ap.parse_args()
    payload = unpack_single_member_narc(args.input.read_bytes())
    rows = decode(payload)
    validate(rows)
    fieldnames = ["area_index"]
    for i in range(FIELD_COUNT):
        fieldnames += [f"u16_{i:02d}", NAMES[i]]
    with args.output.open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=fieldnames)
        wr.writeheader()
        wr.writerows(rows)


if __name__ == "__main__":
    main()
