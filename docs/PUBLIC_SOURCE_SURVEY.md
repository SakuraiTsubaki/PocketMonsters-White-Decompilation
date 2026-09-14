# Public Source Survey — Pokémon White

## Project premise

This reconstruction phase assumes **no local retail ROM is available**. Research must therefore be built from publicly accessible technical documentation, source code, preservation records, archival material, official material, and independently published reverse-engineering results.

No byte-level claim is treated as verified merely because it is commonly repeated. Findings that normally require direct ROM inspection must remain explicitly marked as unverified until corroborated by public evidence or multiple independent technical sources.

## Canonical survey axis: Japan first, all official regions compared

The project uses the **original Japanese release as the baseline reference point** for the regional survey. This is a comparison baseline, not an assumption that the Japanese build is always technically superior or free of later fixes.

Every officially released regional, territorial, and language build discovered during research must be inventoried independently and compared back to the Japanese baseline. Regional builds must never be collapsed into a single generic "international" version.

For every difference, record the most specific applicable category:

- release / revision identity
- executable or overlay change
- filesystem / NARC structure change
- game-data value change
- script / event / flag behavior change
- map / object / encounter change
- text / encoding / font / UI localization change
- graphics / model / palette / animation change
- audio / sequence / voice / sound-effect change
- online / communication / service behavior change
- Mystery Gift / distribution / regional event difference
- censorship, legal, ratings, or localization adaptation
- bug fix / regression / revision-specific correction
- packaging or manual-only difference
- currently unclassified difference

The survey order is therefore:

1. Establish the Japanese baseline release(s) and revision identity.
2. Inventory every other official regional/language build.
3. Compare each build directly against the Japanese baseline.
4. Compare non-Japanese builds against one another when differences do not derive cleanly from Japan.
5. Record later revisions separately rather than silently merging them into their launch-region entry.

## GitHub is the authoritative project record

All research results and reproducible project outputs must be committed to this GitHub repository. Chat conversations, temporary notes, and local scratch work are not treated as the authoritative project state until the result is preserved in GitHub.

Except for retail ROM images or other excluded ROM binaries, the repository should retain all generated or collected project work that can be lawfully and appropriately preserved here, including:

- source registries and bibliographies
- regional / language / revision inventories
- comparison matrices and difference logs
- technical notes and reverse-engineering documentation
- decompilation / reconstruction source
- scripts and tooling
- manifests, metadata, hashes, checksums, and verification records
- reconstructed data tables and machine-readable datasets
- graphics, sprites, palettes, maps, audio metadata, and other extracted/reconstructed project assets when appropriate
- test results, validation logs, and reproducibility procedures
- unused / dummy / debug / bug / glitch research
- online-service, Mystery Gift, distribution, and archival research
- uncertainty records and unresolved conflicts between sources

A research item is considered integrated into the project only after its evidence, interpretation, and resulting artifact or record have been committed to GitHub.

## Evidence classes

- **Primary / official** — official manuals, websites, service notices, distribution notices, developer or publisher material.
- **Technical implementation** — source code or tools that implement a documented Generation V format or behavior.
- **Reverse engineering** — published analysis of scripts, NARC paths, save structures, file formats, executable behavior, or runtime behavior.
- **Preservation archive** — archived event files, C-Gear skins, Pokédex skins, PWT data, Dream World material, screenshots, manuals, or historical web captures.
- **Secondary reference** — maintained encyclopedias and databases used for cross-checking names, mechanics, locations, version differences, and release data.
- **Unverified report** — forum posts, videos, isolated claims, or undocumented files that still require corroboration.

## Initial source inventory

### Project Pokémon

Primary research and preservation hub for Generation V ROM/save/event work.

- BW script NARC discussion: https://projectpokemon.org/home/forums/topic/20442-pok%C3%A9mon-black-and-white-script-narc/
- BW overworld/script relationship research: https://projectpokemon.org/home/forums/topic/21641-pok%C3%A9mon-black-and-white-overworlds-and-scripts/
- Generation V Event Gallery: https://projectpokemon.org/home/files/category/4-generation-5/
- C-Gear Skin archive: https://projectpokemon.org/home/files/category/48-c-gear-skins/
- Generation V save-editing research/tutorial index: https://projectpokemon.org/home/tutorials/save-editing/gen-5/
- C-Gear save-format research: https://projectpokemon.org/home/forums/topic/21064-c-gear-skin-editing/

Known public reverse-engineering leads include BW script/event data references around `a/0/5/7`, overworld data around `a/1/2/5`, and zone/map linkage research. These must be individually corroborated and documented before being promoted to authoritative structure documentation.

### PKHeX

Repository: https://github.com/kwsch/PKHeX

High-value Generation V implementation references include:

- `PK5` Pokémon structure
- BW save block accessors and checksums
- Event work, Entralink, Global Link, GTS, Battle Box, daycare and other save substructures
- Generation V Mystery Gift / PGF format
- C-Gear and related save structures

PKHeX source is implementation evidence, not a substitute for documenting provenance and version-specific behavior.

### Nintendo DS format/tooling references

- ndspy: https://github.com/RoadrunnerWMC/ndspy
- Tinke (archived): https://github.com/pleonex/tinke
- TinkeDSi: https://github.com/R-YaTian/TinkeDSi

These projects document or implement Nintendo DS containers and resources such as ROM filesystems, NARC archives, Nitro graphics, models, palettes, animation resources, SDAT audio and common compression formats.

### Generation V graphics research

- AnimaEngine: https://github.com/KillDaWill/AnimaEngine

Public implementation for Generation V battle-sprite extraction/reconstruction, including research around the `Pokegra` archive and Nitro graphics composition. Treat all path and format claims as technical leads to cross-check against independent sources.

### Encyclopedic / cross-reference sources

- Bulbapedia Black/White overview and version differences: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Black_and_White_Versions
- Bulbapedia C-Gear: https://bulbapedia.bulbagarden.net/wiki/C-Gear
- Bulbapedia Entralink: https://bulbapedia.bulbagarden.net/wiki/Entralink

Use these primarily for release history, mechanics, version differences, localization notes, distribution context, locations, characters and cross-links to primary sources. Technical implementation claims require stronger corroboration.

### Unused / development material

- The Cutting Room Floor: https://tcrf.net/

Survey Black/White pages, subpages, prototype/debug material, unused text, graphics, items, models, music, scripts and regional differences. Every unused-data claim must be checked for actual retail use, regional use, event use, debug-only use, or genuine non-use.

## Survey workstreams

1. Japanese baseline release/version/revision inventory.
2. Full official regional/language/revision inventory.
3. Japanese-baseline-to-region difference matrix.
4. Nintendo DS / DSi cartridge structure and executable layout.
5. NitroFS file tree and NARC path catalog from public research.
6. ARM9, ARM7 and overlay symbol/function research.
7. Script command set, event structure, flags and variables.
8. Map headers, matrices, models, collision, overworld objects and warps.
9. Pokémon personal data, forms, moves, abilities, items and encounter tables.
10. Trainers, parties, AI and battle rules.
11. Text encoding, message archives, fonts and localization differences.
12. Graphics: Pokémon, trainers, overworlds, UI, tiles, models, palettes and animation.
13. Audio: SDAT structure, sequences, banks, waves, streams and dynamic-music behavior.
14. Save format, checksums, event work and communication state.
15. C-Gear, infrared, local wireless, Wi-Fi, Entralink and Game Sync.
16. Pokémon Global Link, Dream World and downloadable customization content.
17. Mystery Gifts, regional event distributions and preserved PGF data.
18. Unused, dummy, debug and development leftovers.
19. Bugs, glitches, revision fixes and localization-specific corrections.
20. Black/White versus Black 2/White 2 continuity and structural differences.

## Research rule

The goal is not to copy one wiki or one tool. Each subsystem should be reconstructed from multiple independent source classes where possible, with conflicts recorded rather than silently resolved.

The Japanese release is always the starting comparison baseline, while every other official regional/language/revision build remains a first-class research target with its own evidence, differences, and uncertainty state.
