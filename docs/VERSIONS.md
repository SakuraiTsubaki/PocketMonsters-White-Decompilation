# Version Coverage

Use this document as the authoritative inventory of game versions targeted by this decompilation project.

The project has no local retail ROM baseline. Entries below therefore distinguish **release/product identity documented from public sources** from byte-level verification. A public catalogue hash is a research lead, not a project-level `Matched` result.

## Japanese baseline

| Status | Region / territory | Language | Revision / update | Product / build identifier | Release | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Planned | Japan | Japanese | Public catalogues report version 0; project verification pending | `TWL-IRAJ-JPN` / game code `IRAJ` | 2010-09-18 | Public reference: CRC32 `7ac204a5`, MD5 `ba456d106c8a2050dee88acbbd13ae49`, SHA-1 `b4cb7c99b38f79dc4e56115fd4a34a6745e55588` | **Canonical survey baseline.** Release date is confirmed by Nintendo/Pokémon official material. Hashes come from GameTDB and are not yet independently verified by this project. |

## Regional / language targets

| Status | Region / territory | Language | Revision / update | Product / build identifier | Release | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Planned | Europe | English | TBD | `TWL-IRAO-EUR` / `IRAO` | 2011-03-04 | TBD | Nintendo Europe confirms Europe-wide launch date. |
| Planned | France / Europe | French | TBD | `TWL-IRAF-FRA` / `IRAF` | 2011-03-04 | TBD | Distinct French software identifier; do not merge with English build. |
| Planned | Germany / Europe | German | TBD | `TWL-IRAD-NOE` / `IRAD` | 2011-03-04 | TBD | Distinct German software identifier. |
| Planned | Italy / Europe | Italian | TBD | `TWL-IRAI-ITA` / `IRAI` | 2011-03-04 | TBD | Distinct Italian software identifier. |
| Planned | Spain / Europe | Spanish | TBD | `TWL-IRAS-ESP` / `IRAS` | 2011-03-04 | TBD | Distinct Spanish software identifier. |
| Planned | United States | English | TBD | `TWL-IRAO-USA` / `IRAO` | 2011-03-06 | TBD | North American launch date confirmed by Nintendo of America press material preserved by third parties. Compare against EUR English despite shared game code. |
| Planned | Canada | English | TBD | `TWL-IRAO-USA` packaging/catalogue record | 2011-03-06 | TBD | Separate Canadian retail/barcode record exists; software-byte identity with US build still to verify. French-Canadian packaging/build relationship remains a research target. |
| Planned | Australia | English | TBD | `TWL-IRAO-AUS` / `IRAO` | 2011-03-10 | TBD | Separate Australian retail identifier; compare against US/EUR English. |
| Planned | South Korea | Korean | Public catalogues report version 0; project verification pending | `TWL-IRAK-KOR` / `IRAK` | 2011-04-21 | Public reference: CRC32 `24ee73ae`, MD5 `ca9d8381c6168a9663efa41720f0d391`, SHA-1 `d9b731212831016be8aa5ab1ad24e6fc0aaf1d20` | Korean release date/product identity is independently catalogued; hashes from GameTDB remain public-reference evidence only. |
| Planned | Hong Kong | Japanese / TBD | TBD | TBD | TBD | TBD | Nintendo Hong Kong later lists White among supported DS software. Determine whether retail distribution used the Japanese build unchanged and document packaging/manual differences. |
| Planned | Taiwan | Japanese / TBD | TBD | TBD | TBD | TBD | Territory/build identity requires dedicated archival research; do not assume a separate executable build. |
| Planned | New Zealand | English / TBD | TBD | TBD | TBD | TBD | Determine whether Australian or another English build was officially distributed. |
| Planned | Singapore / other officially served Asian markets | English/Japanese / TBD | TBD | TBD | TBD | TBD | Research target; require official or preservation evidence before defining a build. |

## Current source anchors

- Nintendo Japan product page: https://www.nintendo.co.jp/ds/irbj/index.html
- Pokémon official BW site: https://www.pokemon.co.jp/series/bw/
- Nintendo Europe launch notice: https://www.nintendo.com/en-gb/News/2011/Pokemon-Black-Version-and-Pokemon-White-Version-arrive-in-Europe-March-4th--253463.html
- GameFAQs release/product catalogue: https://gamefaqs.gamespot.com/ds/995081-pokemon-white-version/data
- GameTDB Japanese entry: https://www.gametdb.com/DS/IRAJ
- GameTDB Korean entry: https://www.gametdb.com/DS/IRAK
- Nintendo Hong Kong NWC service list: https://www.nintendo.com/hk/pressrelease/wifi_20140227.html

## Status vocabulary

- **Planned** — target is in scope; identity may be partly documented, but project-level build verification is not complete.
- **Verified** — exact target identity and hashes have been independently confirmed under the repository verification rules.
- **Mapped** — executable/data layout documented for that exact target.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the exact target using a defined matching criterion.
- **Reference only** — used for comparison but not a reconstruction target.

## Recording rules

1. The Japanese release is the starting comparison baseline, not an assumption that later regional revisions are inferior.
2. Record exact revision/update information whenever known; use `TBD` when it is not.
3. Prefer cryptographic hashes over filenames as identity evidence, but distinguish public-reference hashes from project-verified hashes.
4. Do not commit retail game images, decrypted game images, console keys, or ROM binaries.
5. Record regional, territory, packaging, language, and revision differences instead of assuming releases are identical.
6. If two territories appear to share a game code, byte identity still requires verification.
7. Link version-specific findings to relevant documentation, manifests, or verification records.