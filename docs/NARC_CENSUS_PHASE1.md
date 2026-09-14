# NARC Census — Phase 1

- Named NitroFS files: **247** per ROM
- NARC archives: **237** per ROM
- Byte-identical named files: **242 / 247**
- Different named files: **5 / 247**
- Different NARC archives: **5 / 237**

## Version-different NARCs

| Path | Members | Different members | Indexes |
|---|---:|---:|---|
| `a/0/2/6` | 15 | 8 | `0, 1, 2, 3, 4, 6, 7, 8` |
| `a/0/8/6` | 1 | 1 | `0` |
| `a/1/2/6` | 112 | 29 | `0, 5, 6, 49, 52, 53, 58, 69, 71, 75, 77, 79, 80, 81, 82, 83, 84, 95, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109` |
| `a/1/7/8` | 649 | 26 | `10, 11, 13, 14, 197, 199, 366, 367, 428, 429, 537, 538, 545, 546, 547, 548, 573, 574, 575, 576, 577, 578, 626, 627, 628, 629` |
| `a/2/3/1` | 73 | 2 | `1, 63` |

The complete 237-archive path/member census and cross-version member deltas are stored in `manifests/narc-version-diff.csv`.

## Next

Resolve each NARC path to semantic purpose, parse member formats, and extract reversible source/assets rather than treating the archives as opaque blobs.
