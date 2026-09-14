# Pokédex Area Data — BW format confirmation

## Result

`/a/1/7/8` is confirmed as the Black/White **Pokédex area data** archive. The local Black and White inputs each contain 649 fixed-size members of 249 bytes, one member per National Pokédex species #001–#649.

This identification is independently corroborated by Universal Pokémon Randomizer ZX: its Gen V configuration maps `PokedexAreaData` to `/a/1/7/8`, and its Gen V handler reconstructs this archive from `/a/1/2/6` wild encounter data.

## 249-byte member layout

Each member is:

- byte `0`: season-independence flag. `1` means all four seasonal area tables are identical; `0` means at least one area/method mask differs by season.
- bytes `1..62`: spring block.
- bytes `63..124`: summer block.
- bytes `125..186`: autumn block.
- bytes `187..248`: winter block.

Each 62-byte season block is:

- byte `0`: unobtainable sentinel (`1` when the species has no mapped wild encounter in that season).
- bytes `1..61`: 61 Pokédex area entries. Each entry is a bitmask of encounter methods.

Encounter-method bits are:

| Bit | Hex | Meaning |
| ---: | ---: | --- |
| 0 | `0x01` | Grass / Cave |
| 1 | `0x02` | Doubles Grass |
| 2 | `0x04` | Shaking Spots |
| 3 | `0x08` | Surfing |
| 4 | `0x10` | Surfing Spots |
| 5 | `0x20` | Fishing |
| 6 | `0x40` | Fishing Spots |

The 232-byte per-season wild encounter record in `/a/1/2/6` is correspondingly organized as seven encounter types with slot counts `12,12,12,5,5,5,5`, after an 8-byte rate header.

## Direct validation

The mask semantics reproduce observed data cleanly. For example, regular + doubles grass produces `0x03`; shaking grass produces `0x04`; Surfing + Surfing Spots produces combinations of `0x08` and `0x10`. Stunfisk records include `0x79`, a combination of multiple land/water/fishing method bits rather than an opaque scalar.

Exactly 15 species in both local Black and White inputs have byte 0 = `0`, and exactly those 15 have different seasonal blocks. They are recorded in `season-dependent-species.csv`.

Black and White differ in 26 of the 649 Pokédex-area members. The exact species IDs and member hashes are in `black-white-pokedex-area-diff.csv`.

## `/a/0/8/6` relationship

The single member of `/a/0/8/6` is exactly 3,294 bytes, which divides into **61 fixed records × 54 bytes**. This count exactly matches BW's 61 Pokédex encounter areas. The records contain plausible map/coordinate/subarea metadata and only records 9 and 14 differ between the local Black and White inputs.

This is strong structural evidence that `/a/0/8/6` is associated with the same 61-area world-map/Pokédex-area indexing system, but the meaning of its 27 `u16` fields is not yet fully named. Therefore the repository records the 61×54 structure as confirmed and the exact field semantics as pending. Raw field tables are preserved in the manifests.

## Evidence hierarchy

1. Direct parsing of the supplied Black/White ROM inputs.
2. Direct reconstruction logic in UPR-ZX `Gen5RomHandler.updatePokedexAreaData`.
3. UPR-ZX `gen5_offsets.ini`, which explicitly identifies `/a/1/7/8` as `PokedexAreaData` for Black/White.
4. UPR-ZX `Gen5Constants`, which defines BW member length 249, encounter area count 61, encounter slot counts, and the seven encounter-type names.

## Source anchors

- https://github.com/browniechoi/universal-pokemon-randomizer-zx/blob/master/src/com/dabomstew/pkrandom/config/gen5_offsets.ini
- https://github.com/browniechoi/universal-pokemon-randomizer-zx/blob/master/src/com/dabomstew/pkrandom/romhandlers/Gen5RomHandler.java
- https://github.com/browniechoi/universal-pokemon-randomizer-zx/blob/master/src/com/dabomstew/pkrandom/constants/Gen5Constants.java

## Next

Resolve the 61 area indices to canonical location names/map headers, then fully name the 27 `u16` fields of `/a/0/8/6`.
