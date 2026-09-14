# Public Source Registry — Pokémon Generation V

## Purpose

This repository assumes no local retail ROM is available. The project therefore maintains an **exhaustive public-source census** before treating any subsystem survey as complete. The original Japanese release of each title is the comparison baseline; every official region, language and revision remains a first-class target.

A source category is not complete because one useful page/tool was found. Relevant child pages, files, releases, archives and historical captures must be enumerated, or the access gap must be recorded.

## States
- `Registered` — source root confirmed.
- `Enumerating` — child material is being listed/classified.
- `Enumerated` — relevant public collection itemized to the practical limit.
- `Archived/partial` — only preservation copies or partial surviving material exist.
- `Blocked` — source exists but direct automated access is restricted.
- `Candidate` — source class not yet verified.

## Mandatory source classes

### Official / first-party
- Nintendo Japan Black/White: https://www.nintendo.co.jp/ds/irbj/index.html
- Pokémon.co.jp Black/White official site and sitemap: https://www.pokemon.co.jp/series/bw/ and https://www.pokemon.co.jp/series/bw/sitemap/
- Nintendo Japan Black 2/White 2: https://www.nintendo.co.jp/ds/irej/index.html
- Pokémon.co.jp Black 2/White 2: https://www.pokemon.co.jp/ex/b2w2/
- B2W2 news/product pages: https://www.pokemon.co.jp/ex/b2w2/news/ and https://www.pokemon.co.jp/ex/b2w2/product/
- Pokémon Korea Black/White: https://pokemonkorea.co.kr/game/view/5236
- Pokémon Korea Black 2/White 2: https://pokemonkorea.co.kr/game/view/5237
- Nintendo of America DS manual index: https://en-americas-support.nintendo.com/app/answers/detail/a_id/16905/
- Nintendo Wi-Fi Connection shutdown (US/JP/EU/AU): official Nintendo support/news pages
- Pokémon Global Link/Dream World maintenance, renewal and historical service notices on pokemon.co.jp / archived Pokémon.com

State: **Enumerating**.

### Web preservation
- Internet Archive / Wayback Machine: dead official sites, PGL, Dream World, regional campaign/event pages, manuals, promo media.
- Historical screenshots/videos only with original URL/date/provenance where possible.

State: **Enumerating**.

### Project Pokémon
Enumerate the complete relevant collections, not representative samples:
- Generation 5 Event Gallery: https://projectpokemon.org/home/files/category/4-generation-5/
- Dream World: https://projectpokemon.org/home/files/category/8-dream-world/
- C-Gear skins: https://projectpokemon.org/home/files/category/48-c-gear-skins/
- Pokédex skins, Musicals and Pokémon World Tournaments from the Event Gallery category tree
- Gen 5 save tutorials: https://projectpokemon.org/home/tutorials/save-editing/gen-5/
- Generation 5 Save Tool: https://projectpokemon.org/home/files/file/649-generation-5-save-tool/
- B2W2 General ROM Info: https://projectpokemon.org/home/forums/topic/22629-b2w2-general-rom-info/
- B2W2 save-structure research: https://projectpokemon.org/home/forums/topic/65609-updating-b2w2-save-structure-documentation/
- Gen I–V event contribution/preservation threads: https://projectpokemon.org/home/forums/topic/37431-gen-i-v-event-contributions-thread/
- Project Pokémon RawDB and all Gen V ROM/save research threads discoverable through the forum/index.

State: **Enumerating**.

### Public code / technical implementations
- PPRE — https://github.com/projectpokemon/PPRE
- PKHeX — https://github.com/kwsch/PKHeX
- BW_tool — https://github.com/suloku/BW_tool
- PKMDS Save Editor — https://github.com/codemonkey85/PKMDS-Save-Editor
- TrainerTyrant — https://github.com/ThirdLemon/TrainerTyrant
- SwissArmyKnife — https://github.com/PlatinumMaster/SwissArmyKnife
- FrostsGen5Editor — https://github.com/FrostFalcon/FrostsGen5Editor
- CTRMap-CE — https://github.com/ds-pokemon-hacking/CTRMap-CE
- AnimaEngine — https://github.com/KillDaWill/AnimaEngine
- Pokémon DS Map Studio — https://github.com/Trifindo/Pokemon-DS-Map-Studio
- ANDT — https://github.com/javierhimura/ANDT
- ndspy — https://github.com/RoadrunnerWMC/ndspy
- NARC implementation — https://github.com/lhearachel/narc
- Tinke — https://github.com/pleonex/tinke
- TinkeDSi — https://github.com/R-YaTian/TinkeDSi
- DS Pokémon Hacking documentation — https://ds-pokemon-hacking.github.io/docs/

Each repository must be enumerated by relevant files/classes/commits/issues rather than treated as a single citation. Known conflicts between implementations are retained.

### Unused / prerelease / development
- The Cutting Room Floor retail and prerelease/prototype pages (direct crawling may be blocked; use indexed/archived evidence).
- Data Crystal, only where Gen V coverage actually exists.
- official prerelease screenshots, trailers, TV commercials and promotional material.
- developer interviews and contemporary official/press material.

State: **Enumerating**.

### Secondary discovery/cross-check references
- Bulbapedia
- Serebii
- Pokémon Database
- GameFAQs release/product-code records
- regional community databases/wikis where useful

Secondary sources do not override official or direct technical evidence.

### Catalog / dump identity / revisions
Enumerate public metadata without distributing ROMs:
- No-Intro / DAT-o-MATIC revision/hash metadata
- catalog/product/cart codes
- box/cart/manual scans showing revision identifiers
- trustworthy public hash lists
- GameTDB or equivalent catalog data where independently useful

Public catalog hashes are evidence records, not project `Observed`/`Matched` verification by themselves.

### Events / distributions / DLC
Enumerate every preserved item by region/language/date/method and distinguishing attributes:
- Mystery Gift / PGF
- local wireless / infrared / store / movie / tournament / magazine / campaign
- Dream World / PGL Pokémon
- C-Gear and Pokédex skins
- Musicals
- PWT downloadable tournaments
- official Wi-Fi competitions/rules
- preserved raw server-format DLC and default/empty customization data

### Online / communication history
- C-Gear, IR, local wireless
- Nintendo Wi-Fi Connection
- GTS / Global Terminal
- Game Sync / Pokémon Global Link / Dream World
- Entralink / Pass Powers / Feeling Check / Xtransceiver
- official maintenance/termination notices
- fan restoration kept strictly separate from official historical behavior

### Still-open mandatory classes
- official strategy guides / authorized guides
- physical box/cart/manual scans for every region/revision
- magazines and contemporary press
- soundtrack releases / track lists / audio documentation
- localization-specific captures
- bug/glitch reproduction and revision-fix evidence
- real-hardware vs emulator-only behavior
- academic/technical papers if relevant
- historical fan tools whose original hosting disappeared

## Census rule

Do **not** mark `all public sources surveyed` until every source class above is either enumerated or explicitly recorded as unavailable/blocked with the attempted discovery path. Unknown information remains `unknown`/`TBD`; conflicting sources remain recorded as conflicts.
