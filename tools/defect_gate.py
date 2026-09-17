#!/usr/bin/env python3
"""Fail unless every tracked defect has reached a terminal verified state."""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

TERMINAL = {"fixed", "not-applicable", "duplicate"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("registry", nargs="?", type=Path, default=Path("analysis/bug_registry.csv"))
    args = ap.parse_args()

    with args.registry.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    counts = Counter((row.get("status") or "").strip().lower() for row in rows)
    unresolved = [row for row in rows if (row.get("status") or "").strip().lower() not in TERMINAL]

    print(f"tracked={len(rows)} terminal={len(rows)-len(unresolved)} unresolved={len(unresolved)}")
    for status, count in sorted(counts.items()):
        print(f"  {status or '<blank>'}: {count}")

    if unresolved:
        print("\nUNRESOLVED:")
        for row in unresolved:
            print(f"  {row.get('id','?')}: {row.get('status','?')} - {row.get('name','?')}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
