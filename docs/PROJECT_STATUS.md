# Project Status

**Current stage:** Public-source survey and reconstruction baseline

This project assumes no local retail ROM is available. Work therefore begins from publicly accessible official material, technical implementations, preservation archives, reverse-engineering research, historical web captures, and independently maintained references.

## Baseline policy

- Japanese retail release is the canonical starting comparison point.
- Every official regional/language/territory/revision target remains independent until evidence proves identity.
- Black archive counts are not copied into White by assumption.
- Public-reference hashes are not project-level `Matched` evidence.
- Unknown values remain `TBD`/`Unknown`.
- GitHub is the authoritative project record; retail ROM binaries remain excluded.

## Progress

- [x] Establish public-source-first research methodology.
- [x] Create initial public source inventory (`docs/PUBLIC_SOURCE_SURVEY.md`).
- [x] Seed Japanese baseline and major regional/language targets in `docs/VERSIONS.md`.
- [x] Create Japanese-baseline regional comparison ledger (`docs/REGIONAL_SURVEY_MATRIX.md`).
- [x] Seed evidence-backed NitroFS/NARC path catalog (`docs/NARC_PATH_CATALOG.md`).
- [x] Add machine-readable NARC path inventory (`manifests/narc-paths.csv`).
- [x] Record first BW ↔ B2W2 path-movement findings and public-source conflicts.
- [ ] Complete every official territory, packaging, language, and revision target.
- [ ] Find White-specific archive/file-tree census preservation evidence.
- [ ] Establish which exact White region/revision each public tool/research source tested.
- [ ] Document executable and overlay layout from public technical evidence.
- [ ] Map symbols, functions, and major subsystems where public evidence permits.
- [ ] Document game-data formats and resource containers at record/field level.
- [ ] Reconstruct scripts, events, flags, variables, and behavior.
- [ ] Reconstruct asset pipelines and metadata.
- [ ] Reconstruct save, communication, online, and distribution structures.
- [ ] Catalog unused, dummy, debug, and development material.
- [ ] Add reproducible tooling that does not redistribute retail ROM binaries.
- [ ] Add automated verification where practical.

## Current technical baseline

Public implementations and B/W research currently support White path leads for text, personal data, learnsets, evolutions, moves, items, scripts, trainers, overworld/event data, and encounters. Unlike Black, the public Project Pokémon Raw DB index does not expose a White tree, so White-specific archive member counts remain `TBD` instead of inheriting Black's counts.

The first structural comparison already establishes that scripts, trainer metadata/parties, overworld events, and encounters move to different archive paths in B2W2.

## Validation handling

Repository-standard verification remains `Unverified` → `Observed` → `Reproduced` → `Matched`. Research documents may additionally describe public evidence as corroborated, direct technical, single-source, preserved, or conflicted, but these labels do not replace project-level target verification.

## Next milestones

1. Locate White-specific file-tree/archive census evidence.
2. Expand each known NARC from path-level identity into file/record format documentation.
3. Start with high-value data families: personal data, moves, evolutions/learnsets, trainers, encounters, text, and scripts.
4. Continue regional comparison from product identity into actual localization/technical differences.
5. Keep `VERSIONS.md`, regional matrix, NARC catalog, manifests, and this status synchronized.