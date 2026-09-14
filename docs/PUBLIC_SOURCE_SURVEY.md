# Public Source Survey — Pokémon White

## Project premise

This reconstruction phase assumes **no local retail ROM is available**. Research must therefore be built from publicly accessible technical documentation, source code, preservation records, archival material, official material, and independently published reverse-engineering results.

No byte-level claim is treated as verified merely because it is commonly repeated. Findings that normally require direct ROM inspection must remain explicitly marked as unverified until corroborated by public evidence or multiple independent technical sources.

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

1. Release/version/revision inventory by region and language.
2. Nintendo DS / DSi cartridge structure and executable layout.
3. NitroFS file tree and NARC path catalog from public research.
4. ARM9, ARM7 and overlay symbol/function research.
5. Script command set, event structure, flags and variables.
6. Map headers, matrices, models, collision, overworld objects and warps.
7. Pokémon personal data, forms, moves, abilities, items and encounter tables.
8. Trainers, parties, AI and battle rules.
9. Text encoding, message archives, fonts and localization differences.
10. Graphics: Pokémon, trainers, overworlds, UI, tiles, models, palettes and animation.
11. Audio: SDAT structure, sequences, banks, waves, streams and dynamic-music behavior.
12. Save format, checksums, event work and communication state.
13. C-Gear, infrared, local wireless, Wi-Fi, Entralink and Game Sync.
14. Pokémon Global Link, Dream World and downloadable customization content.
15. Mystery Gifts, regional event distributions and preserved PGF data.
16. Unused, dummy, debug and development leftovers.
17. Bugs, glitches, revision fixes and localization-specific corrections.
18. Black/White versus Black 2/White 2 continuity and structural differences.

## Research rule

The goal is not to copy one wiki or one tool. Each subsystem should be reconstructed from multiple independent source classes where possible, with conflicts recorded rather than silently resolved.
