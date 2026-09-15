# Decompilation bootstrap — Black / White

## Source state

The first executable/data inventory was generated from the user-supplied SweeTnDs-era USA/Europe English Black/White images.

These inputs are useful for NDS-mode code and data analysis, but the supplied images are known underdumps rather than preservation-clean DSi-enhanced dumps. The current results are therefore recorded as **Observed** source evidence, not as the final canonical rebuild identity.

No retail ROM image is committed to this repository.

## Observed NDS layout

| Property | Black (IRBO) | White (IRAO) |
| --- | ---: | ---: |
| ROM size | 268,435,456 | 268,435,456 |
| ARM9 size | 456,856 | 456,868 |
| ARM7 size | 167,812 | 167,812 |
| FAT entries | 484 | 484 |
| Named FNT files | 247 | 247 |
| ARM9 overlays | 237 | 237 |
| ARM7 overlays | 0 | 0 |
| Named NARC archives | 237 | 237 |

The ARM7 binary is byte-identical between the two observed inputs. ARM9 differs.

## Black ↔ White identity pass

Across all 484 FAT entries:

- **299** entries are byte-identical.
- **185** entries differ.
- Most differing entries are ARM9 overlay payloads.
- Only **five named filesystem entries** differ:
  - `a/0/2/6`
  - `a/0/8/6`
  - `a/1/2/6`
  - `a/1/7/8`
  - `a/2/3/1`

`a/1/2/6` is independently documented by the PPRE project as Black/White encounter data. The remaining paths stay unnamed until their semantics are verified; no guessed names are being introduced.

## Changed NARC members

The five named version-different archives retain the same member counts between these observed Black and White inputs. The current changed-member counts are:

| Path | Members | Changed members |
| --- | ---: | ---: |
| `a/0/2/6` | 15 | 8 |
| `a/0/8/6` | 1 | 1 |
| `a/1/2/6` | 112 | 29 |
| `a/1/7/8` | 649 | 26 |
| `a/2/3/1` | 73 | 2 |

Exact payload bytes are not committed. Hash inventories and reconstruction tooling are the repository-facing evidence.

## Verification levels

- **Observed** — parsed directly from a hash-identified input image.
- **Reproduced** — committed tooling independently regenerates the same structure and hashes.
- **Matched** — reconstructed output is verified against the canonical clean target.

The bootstrap currently begins at **Observed**. Clean-dump matching remains separate from the underdump observations.

## Next executable work

1. Expand the overlay map with load address, RAM size, BSS size, static initializer range, file ID, and payload identity.
2. Locate SDK/runtime boundaries and executable-module signatures in ARM9 and ARM7.
3. Classify the 237 named NARC archives, attaching semantic names only when verified.
4. Start source reconstruction from the common Black/White executable substrate while keeping version-specific units explicit.
5. Add preservation-clean IRBO/IRAO verification when clean inputs are available, without discarding the underdump observations.

## External verification references

- TASVideos game-version records list preservation-clean Black/White hashes and identify bad-dump variants.
- Project Pokémon PPRE documents `a/1/2/6` as Black/White encounter data.
