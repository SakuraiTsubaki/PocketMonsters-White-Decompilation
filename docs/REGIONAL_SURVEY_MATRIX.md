# Regional Survey Matrix — Pokémon White

## Purpose

Track every officially released regional, territorial, language, packaging, and revision target of Pokémon White against the original Japanese release baseline.

The matrix is intentionally evidence-first. Do not fill unknown fields from memory or assumption. Use `Unknown` until a source is found.

## Baseline policy

- Baseline axis: original Japanese retail release.
- Every non-Japanese build is compared directly against the Japanese baseline.
- Non-Japanese builds are also cross-compared where necessary.
- Revisions are separate records.
- Language, territory, cartridge identity, release date, revision, packaging, and technical differences must not be conflated.
- "International" is not a valid substitute for enumerating individual official builds.

## Build inventory

| Record ID | Version | Territory / market | Language | Release date | Revision | Product / cart code | Known hashes | Evidence status | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WHITE-JP-BASE | White | Japan | Japanese | 2010-09-18 | Public catalogue: v0; project verification pending | `TWL-IRAJ-JPN` / `IRAJ` | Public reference: CRC32 `7ac204a5`; MD5 `ba456d106c8a2050dee88acbbd13ae49`; SHA-1 `b4cb7c99b38f79dc4e56115fd4a34a6745e55588` | Release/product identity corroborated; bytes not project-verified | Nintendo JP; GameFAQs; GameTDB |
| WHITE-EU-EN | White | Europe | English | 2011-03-04 | Unknown | `TWL-IRAO-EUR` / `IRAO` | Unknown | Product/release catalogued | Nintendo Europe; GameFAQs |
| WHITE-EU-FR | White | France / Europe | French | 2011-03-04 | Unknown | `TWL-IRAF-FRA` / `IRAF` | Unknown | Product/release corroborated | French manual/catalogue records; VGCollect |
| WHITE-EU-DE | White | Germany / Europe | German | 2011-03-04 | Unknown | `TWL-IRAD-NOE` / `IRAD` | Unknown | Product/release catalogued | Preservation/catalogue sources |
| WHITE-EU-IT | White | Italy / Europe | Italian | 2011-03-04 | Unknown | `TWL-IRAI-ITA` / `IRAI` | Unknown | Product/release corroborated | VGCollect; technical compatibility reports |
| WHITE-EU-ES | White | Spain / Europe | Spanish | 2011-03-04 | Unknown | `TWL-IRAS-ESP` / `IRAS` | Unknown | Product/release corroborated | Retail catalogue records |
| WHITE-US-EN | White | United States | English | 2011-03-06 | Unknown | `TWL-IRAO-USA` / `IRAO` | Unknown | Release corroborated; exact bytes pending | Nintendo of America press material; GameFAQs |
| WHITE-CA-EN | White | Canada | English | 2011-03-06 | Unknown | `TWL-IRAO-USA` retail record | Unknown | Packaging/catalogue record; byte identity pending | GameFAQs |
| WHITE-AU-EN | White | Australia | English | 2011-03-10 | Unknown | `TWL-IRAO-AUS` / `IRAO` | Unknown | Product/release catalogued | GameFAQs |
| WHITE-KR | White | South Korea | Korean | 2011-04-21 | Public catalogue: v0; project verification pending | `TWL-IRAK-KOR` / `IRAK` | Public reference: CRC32 `24ee73ae`; MD5 `ca9d8381c6168a9663efa41720f0d391`; SHA-1 `d9b731212831016be8aa5ab1ad24e6fc0aaf1d20` | Product/release corroborated; bytes not project-verified | Korean release coverage; GameFAQs; GameTDB |
| WHITE-HK | White | Hong Kong | Japanese / TBD | Unknown | Unknown | Unknown | Unknown | Official territory support confirmed later; retail build identity unresolved | Nintendo Hong Kong NWC service list |
| WHITE-TW | White | Taiwan | Japanese / TBD | Unknown | Unknown | Unknown | Unknown | Research target | Pending primary/preservation evidence |
| WHITE-NZ | White | New Zealand | English / TBD | Unknown | Unknown | Unknown | Unknown | Research target | Pending primary/preservation evidence |
| WHITE-SG | White | Singapore / officially served Asian markets | English/Japanese / TBD | Unknown | Unknown | Unknown | Unknown | Research target | Pending primary/preservation evidence |

### Immediate unresolved territory/build questions

- Determine whether Hong Kong and Taiwan retail distribution used the Japanese `IRAJ` build unchanged or had territory-specific packaging/manual material only.
- Determine whether New Zealand used the Australian `IRAO` build unchanged.
- Determine Canadian French packaging/manual/cart relationships; do not assume FRA cartridge identity from packaging alone.
- Enumerate any additional officially served Asian markets with primary or preservation evidence.
- Enumerate every known revision for each row before declaring a build inventory complete.

## Difference matrix

| Build ID | Category | Japanese baseline state | Regional state | Difference class | Evidence level | Source(s) | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WHITE-EU-FR / DE / IT / ES | language/build identity | Japanese `IRAJ` | Separate language-specific game codes (`IRAF`, `IRAD`, `IRAI`, `IRAS`) | text / localization / encoding; potentially other technical differences | Corroborated for product identity; technical diff pending | Independent catalogue/manual/retail records | Separate game codes establish distinct targets, but do not by themselves enumerate byte-level differences. |
| WHITE-KR | language/build identity | Japanese `IRAJ` | Korean `IRAK` | text / localization / encoding; fonts/glyphs; potentially other technical differences | Corroborated for product identity; technical diff pending | GameFAQs; GameTDB | Korean target must be analyzed independently rather than folded into an international build. |
| WHITE-US-EN / WHITE-EU-EN / WHITE-AU-EN | territory/build identity | Japanese `IRAJ` | Shared `IRAO` game-code family with different retail suffixes | unclassified until byte comparison evidence exists | Corroborated for retail identity | Nintendo/secondary catalogues | Shared game code does not prove byte identity across USA/EUR/AUS. |

### Difference classes

- executable / ARM9 / ARM7
- overlay
- filesystem / NitroFS
- NARC membership / ordering / format
- Pokémon / personal data
- moves / abilities / items
- encounters
- trainers / AI / battle rules
- maps / matrices / warps / objects
- scripts / flags / variables / events
- text / localization / encoding
- fonts / glyphs
- graphics / sprites / UI / models
- audio / music / SFX
- save structure / checksums
- wireless / infrared / Wi-Fi
- C-Gear / Entralink / Game Sync / Global Link
- Mystery Gift / external distribution
- unused / dummy / debug content
- bug / glitch / revision fix
- legal / ratings / censorship / localization adaptation
- packaging / manual / non-ROM material
- unclassified

## Evidence levels

- **Official** — official first-party material directly supports the claim.
- **Direct technical** — public code, extracted data, disassembly, or format implementation directly demonstrates the claim.
- **Corroborated** — two or more independent reliable sources agree.
- **Single-source** — one credible source exists but independent confirmation is pending.
- **Reported** — claim exists but technical verification is insufficient.
- **Unknown** — no adequate evidence yet.

## Source anchors

- https://www.nintendo.co.jp/ds/irbj/index.html
- https://www.pokemon.co.jp/series/bw/
- https://www.nintendo.com/en-gb/News/2011/Pokemon-Black-Version-and-Pokemon-White-Version-arrive-in-Europe-March-4th--253463.html
- https://gamefaqs.gamespot.com/ds/995081-pokemon-white-version/data
- https://www.gametdb.com/DS/IRAJ
- https://www.gametdb.com/DS/IRAK
- https://www.nintendo.com/hk/pressrelease/wifi_20140227.html

## Comparison rule

A localized text difference is not automatically a complete technical-ROM difference description; record the text difference, then separately record any encoding, font, archive-layout, script, executable, or resource change that makes it technically distinct.

Likewise, a regional bug fix must be recorded as a regional/revision implementation difference rather than generalized as a Generation V rule unless evidence shows it applies to all builds.