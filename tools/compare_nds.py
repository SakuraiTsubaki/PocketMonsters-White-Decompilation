#!/usr/bin/env python3
"""Compare two Nintendo DS ROMs without emitting ROM bytes."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from rom_audit import audit


def index_files(report: dict) -> dict[int, dict]:
    return {int(x["file_id"]): x for x in report["nitrofs"]["files"]}


def overlay_index(report: dict, cpu: str) -> dict[int, dict]:
    return {int(x["overlay_id"]): x for x in report["overlays"][cpu] if "overlay_id" in x}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("left", type=Path)
    ap.add_argument("right", type=Path)
    ap.add_argument("-o", "--output", type=Path)
    args = ap.parse_args()

    left = audit(args.left, include_file_hashes=True)
    right = audit(args.right, include_file_hashes=True)
    lf, rf = index_files(left), index_files(right)
    ids = sorted(set(lf) | set(rf))

    changed_files = []
    same_files = []
    for file_id in ids:
        a, b = lf.get(file_id), rf.get(file_id)
        if a is None or b is None:
            changed_files.append({"file_id": file_id, "left": a, "right": b, "reason": "missing-on-one-side"})
            continue
        if a.get("sha256") == b.get("sha256"):
            same_files.append(file_id)
        else:
            changed_files.append({
                "file_id": file_id,
                "left_path": a.get("path"),
                "right_path": b.get("path"),
                "left_size": a.get("size"),
                "right_size": b.get("size"),
                "left_sha256": a.get("sha256"),
                "right_sha256": b.get("sha256"),
            })

    overlay_diff = {}
    for cpu in ("arm9", "arm7"):
        la, ra = overlay_index(left, cpu), overlay_index(right, cpu)
        diff = []
        for overlay_id in sorted(set(la) | set(ra)):
            if la.get(overlay_id) != ra.get(overlay_id):
                diff.append({"overlay_id": overlay_id, "left": la.get(overlay_id), "right": ra.get(overlay_id)})
        overlay_diff[cpu] = diff

    report = {
        "left": {"path": str(args.left), "hashes": left["hashes"], "header": left["header"], "arm9_sha256": left["arm9"]["sha256"], "arm7_sha256": left["arm7"]["sha256"]},
        "right": {"path": str(args.right), "hashes": right["hashes"], "header": right["header"], "arm9_sha256": right["arm9"]["sha256"], "arm7_sha256": right["arm7"]["sha256"]},
        "summary": {
            "fat_count_left": left["nitrofs"]["fat_count"],
            "fat_count_right": right["nitrofs"]["fat_count"],
            "identical_file_payloads": len(same_files),
            "different_or_missing_file_payloads": len(changed_files),
            "arm9_identical": left["arm9"]["sha256"] == right["arm9"]["sha256"],
            "arm7_identical": left["arm7"]["sha256"] == right["arm7"]["sha256"],
            "arm9_overlay_metadata_differences": len(overlay_diff["arm9"]),
            "arm7_overlay_metadata_differences": len(overlay_diff["arm7"]),
        },
        "same_file_ids": same_files,
        "changed_files": changed_files,
        "overlay_metadata_differences": overlay_diff,
        "left_anomalies": left["anomalies"],
        "right_anomalies": right["anomalies"],
    }

    text = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
