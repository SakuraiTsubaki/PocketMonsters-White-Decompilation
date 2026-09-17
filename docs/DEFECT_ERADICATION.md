# Defect eradication workflow

## Goal

No known reproducible bug, glitch, crash, softlock, state corruption, invalid collision, incorrect data display, audio-state leak, or unsafe malformed-state path remains unresolved in the maintained target. Unused/dummy/placeholder data is preserved unless the data or its reachable behavior is itself defective.

## Evidence states

`candidate` -> `documented` -> `reproduced` -> `localized` -> `patched` -> `regression-passed` -> `fixed`

Only `fixed`, `not-applicable`, and `duplicate` are terminal. `tools/defect_gate.py` deliberately fails while any other state remains.

## Required evidence for `fixed`

1. Exact target build fingerprint is recorded.
2. Reproduction steps or a machine-readable fixture demonstrate the original failure.
3. Root cause is localized to code/data/script/map/asset state.
4. Patch changes only the defective behavior; intended mechanics and preserved unused data remain intact.
5. Regression test proves the failure no longer occurs.
6. Neighboring behavior is tested for regressions.
7. Black/White shared-engine fixes are checked in both versions; version/region-specific fixes remain scoped.
8. Generated ROMs are never committed. Only source, patch recipes, manifests, hashes, logs, and verification output are committed.

## Audit tools

- `tools/rom_audit.py`: hashes the image and inventories NDS header CRCs, ARM9/ARM7, FNT/FAT, NitroFS file bounds and hashes, and overlay tables.
- `tools/compare_nds.py`: compares two builds without emitting ROM bytes.
- `tools/defect_gate.py`: enforces zero unresolved registry entries.

## Current highest-risk queue

1. Triple Battle softlock.
2. Sky Drop + Gravity immobilization.
3. HP display / fainted-Pokemon state desynchronization.
4. GTS empty-result-slot freeze and related stale network state.
5. Choice-item stale move lock and Shed Shell stale switchability.
6. Triple Battle AI impossible-move selection and Ability storage.
7. Landing/collision states that can trap or displace the player.
8. Map, tile, event, UI, audio, and text defects.

## Secondary evidence index

These sources are discovery/evidence leads only; the ROM/build must still reproduce the defect before patching.

- Bulbapedia, `List of battle glitches in Generation V`: https://bulbapedia.bulbagarden.net/wiki/List_of_battle_glitches_in_Generation_V
- Bulbapedia, `List of glitches in Generation V`: https://bulbapedia.bulbagarden.net/wiki/List_of_glitches_in_Generation_V
- Bulbapedia, `List of overworld glitches in Generation V`: https://bulbapedia.bulbagarden.net/wiki/List_of_overworld_glitches_in_Generation_V
- Project Pokemon Generation 5 research forum: https://projectpokemon.org/home/forums/forum/116-generation-5/

## Scope corrections discovered during verification

Do not merge region-specific behavior into all-language entries. In particular, the Opelucid Gym Surf trap is documented for Japanese Black/White and must be tracked separately from all-language Opelucid collision/geometry defects.
