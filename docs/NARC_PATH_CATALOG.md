# NARC / NitroFS Path Catalog — Pokémon White

## Purpose

This document records publicly documented NitroFS/NARC paths for Pokémon White under the project's no-local-ROM policy. Black data is not copied into White merely because the paired versions are closely related; White-specific counts and byte identity remain `TBD` until supported by White evidence.

The machine-readable companion is `../manifests/narc-paths.csv`.

## Evidence rule

Public tools such as PPRE explicitly map several paths to both Black and White, and TrainerTyrant documents shared B/W trainer paths. These are valid technical leads but do not constitute project-level `Observed` evidence for a specific Japanese, US, EUR, Korean, or other White build.

## Initial path catalog

| Path | Reported role | White member count | Evidence | Notes |
| --- | --- | ---: | --- | --- |
| `/a/0/0/2` | Main/system text | TBD | Corroborated path role | PPRE targets White; the Gen V translation/tooling ecosystem uses this as main text. White-specific member count still needs evidence. |
| `/a/0/0/3` | Story text | TBD | Corroborated path role | PPRE targets White; role is independently documented for BW. |
| `/a/0/0/8` | Map resources | TBD | Single-source for White applicability | Paired-BW public ROM-content documentation identifies this role; dedicated White file-tree evidence pending. |
| `/a/0/1/6` | Pokémon personal data | TBD | Direct technical | PPRE maps White personal data to this path. |
| `/a/0/1/7` | Experience/growth table | TBD | Direct technical | PPRE maps White/BW generation data here. |
| `/a/0/1/8` | Level-up learnsets | TBD | Direct technical | PPRE maps White/BW learnsets here. |
| `/a/0/1/9` | Evolution data | TBD | Direct technical | PPRE maps White evolution data here. |
| `/a/0/2/0` | Base-evolution / baby-Pokémon lookup (PPRE terminology) | TBD | Direct technical | Exact semantic format still needs dedicated research. |
| `/a/0/2/1` | Move data | TBD | Direct technical | PPRE maps White move data here. |
| `/a/0/2/3` | Font set | TBD | Reported / paired-version technical evidence | Japanese BW text/font reconstruction identifies this path; White-specific extraction evidence should be added before raising confidence. |
| `/a/0/2/4` | Item data | TBD | Direct technical | PPRE maps White/Gen V item data to this location in the shared implementation. |
| `/a/0/4/9` | Overworld sprites | TBD | Reported | Public BW ROM-content documentation identifies the path; White-specific confirmation pending. |
| `/a/0/5/7` | In-game scripts | TBD | Corroborated for BW pair | Public B/W script research treats this as the script NARC. |
| `/a/0/9/2` | Trainer metadata (`trdata`) | TBD | Corroborated | B/W Trainer Editor and TrainerTyrant explicitly apply this mapping to both Black and White. |
| `/a/0/9/3` | Trainer parties (`trpoke`) | TBD | Corroborated | B/W Trainer Editor and TrainerTyrant explicitly apply this mapping to both Black and White. |
| `/a/1/2/5` | Overworld/map-event data | TBD | Corroborated for BW pair | Project Pokémon B/W overworld/script research documents the path. |
| `/a/1/2/6` | Wild encounter tables | TBD | Direct technical / paired-version | PPRE maps BW encounter data here; public B/W encounter tooling supports the same family. |

## Why counts are `TBD`

Project Pokémon Raw DB exposes a detailed Pokémon **Black** file tree, but its public Raw DB index does not currently expose a corresponding White tree. This repository therefore does not inherit Black's member counts by assumption. Establishing whether each White regional build is byte-identical or structurally identical at a given NARC is a separate survey task.

## Cross-game structural differences already established

| Subsystem | Black / White | Black 2 / White 2 |
| --- | --- | --- |
| In-game scripts | `/a/0/5/7` | `/a/0/5/6` |
| Trainer metadata | `/a/0/9/2` | `/a/0/9/1` |
| Trainer parties | `/a/0/9/3` | `/a/0/9/2` |
| Overworld/events | `/a/1/2/5` | `/a/1/2/6` |
| Wild encounters | `/a/1/2/6` | `/a/1/2/7` |

## Known source conflict

PPRE's legacy B2W2 trainer/encounter mapping is inconsistent with later B2W2 research. That conflict does not affect the documented BW trainer mapping, which is independently corroborated by dedicated B/W tools.

## Source anchors

- PPRE `nds/files.py`: https://github.com/projectpokemon/PPRE/blob/master/nds/files.py
- PPRE `pokeversion.py`: https://github.com/projectpokemon/PPRE/blob/master/pokeversion.py
- B/W Trainer Editor: https://projectpokemon.org/home/forums/topic/12078-bw-trainer-editor/
- B/W overworld/script research: https://projectpokemon.org/home/forums/topic/21641-pok%C3%A9mon-black-and-white-overworlds-and-scripts/
- TrainerTyrant: https://github.com/ThirdLemon/TrainerTyrant
- BW translation project: https://projectpokemon.org/home/forums/topic/10741-pok%C3%A9mon-black-and-white-translation-project-v3-project-is-complete/
- Japanese BW text/font reconstruction: https://github.com/WD8844/Project-PMBW-TEXT-experiment
- Project Pokémon Raw DB index: https://projectpokemon.org/rawdb/
- B2W2 General ROM Info (comparison source): https://projectpokemon.org/home/forums/topic/22629-b2w2-general-rom-info/

## Next work

1. Find White-specific file-tree/archive census preservation data.
2. Identify which White region/revision each public technical source actually tested.
3. Compare White versus Black path-by-path rather than inheriting Black counts.
4. Add record-format documents only after concrete format evidence is collected.
5. Feed every confirmed region-specific difference into `REGIONAL_SURVEY_MATRIX.md`.