# BW1 `/a/0/8/6` world/Pokédex map area metadata — Phase 4

## Scope

This phase resolves the 3,294-byte single member of `/a/0/8/6` as a 61-record table aligned one-for-one with the 61 BW1 Pokédex/world-map areas. Each record is 54 bytes, parsed as 27 little-endian `u16` values.

This document deliberately separates direct invariants from semantic inference. Provisional names are analysis labels, not claims about original Game Freak symbol names.

## Confirmed joins

- Record count: **61**.
- Record size: **54 bytes = 27 × u16**.
- Record index is the same area index used by `/a/1/7/8` Pokédex Area Data.
- `u16_00` is the **representative ZoneHeader ID**. Joining it to `/a/0/1/2`, then reading the ZoneHeader map-name index at `0x1A`, resolves all 61 area names.
- Black and White share the same 61-area order. Area 14 is version-specific:
  - Black: representative ZoneHeader `0` → **Black City**
  - White: representative ZoneHeader `424` → **White Forest**

## Exact structural invariants

Across all 61 records in both supplied BW1 inputs:

- `u16_01 == 1`
- `u16_02 == u16_04 == u16_06 == u16_08`
- `u16_03 == u16_05`
- `u16_07 == u16_03 - 4`
- `u16_09 == u16_03 + 4`
- `u16_10 == 8`
- `u16_13 == 0`
- `u16_14 == 0`
- `u16_12 == 1` exactly when `u16_15 != 0xFFFF`
- `u16_15` is populated on exactly 16 areas and uses the complete value set `2480..2495`
- `u16_16` is normally `0xFFFF`; only Liberty Garden=`0xF000` and Unity Tower=`0xF001`

The repeated X/Y patterns around fields 2–9 strongly indicate map-display coordinates, but the exact renderer-side names remain untraced.

## Fly-point field inference

The 16 records with `u16_12=1` have `u16_15` values `2480..2495`. They are the settlement/League destinations expected to participate in Fly destination unlocking. This makes `u16_15` a high-confidence **fly unlock/visited flag candidate** and `u16_12` a high-confidence **has-fly-flag candidate**.

This is not yet promoted to a source-symbol fact: a direct BW1 code path that tests the field as an event flag still needs to be named. Comparative Generation IV source material also assigns the `2480+` range to `FLAG_SYS_FLYPOINT_*`, which strengthens but does not by itself prove the BW1 symbol name.

## World-map component fields

`u16_17..u16_23` form a seven-slot list of IDs with `0xFFFF` padding. They behave as world-map component/segment identifiers:

- non-`0xFFFF` IDs are unique per version across the 61-area table;
- Black and White differences land exactly on version-distinct world-map content;
- Opelucid City changes `u16_17` Black `45` ↔ White `44`;
- area 14 changes Black City component IDs `56,57` ↔ White Forest `58,59`.

The exact renderer/resource archive consumed by these IDs remains the next code-tracing target, so the label `map_component_id` is high-confidence inference rather than recovered original nomenclature.

## Remaining presentation fields

- `u16_11`: values `0..5`, clustering by settlement/route/landmark presentation. Tracked as `display_class_candidate`.
- `u16_24`: values `0..15`, apparently a shape/style/orientation selector. Exact meaning unresolved.
- `u16_25/u16_26`: coordinate-like pair, generally offset from the center coordinates. Tracked as label-anchor candidates. Anville Town uses `u16_25=0xFFFF`, so consumers must tolerate a sentinel.

See `manifests/a086-field-map.csv` for field-by-field confidence.

## Black / White parsed-field differences

Only four `u16` fields differ:

| area | field | Black | White | interpretation |
|---|---|---:|---:|---|
| Opelucid City (9) | `u16_17` | 45 | 44 | version-specific map component |
| area 14 | `u16_00` | 0 | 424 | Black City representative zone ↔ White Forest representative zone |
| area 14 | `u16_17` | 56 | 58 | version-specific component |
| area 14 | `u16_18` | 57 | 59 | version-specific component |

All other parsed `u16` fields are identical between the supplied Black and White inputs.

## Encounter/ZoneHeader closure

The companion `manifests/encounter-zone-area-map.csv` closes the join from all **112** wild-encounter members to ZoneHeaders and then to these 61 area records.

- All 112 encounter IDs have exactly one ZoneHeader.
- 110 resolve by exact map-name match.
- Two named subareas are assigned to their parent Pokédex area:
  - Trial Chamber → Victory Road
  - Guidance Chamber → Mistralton Cave
- No encounter member remains unassigned.

## Next boundary

Trace the BW1 world-map/Pokédex-map renderer that consumes `/a/0/8/6`, especially fields `11`, `15`, `16`, `17..26`, and identify the graphics/archive IDs behind `u16_17..u16_23`. Until then, source-like names remain provisional.
