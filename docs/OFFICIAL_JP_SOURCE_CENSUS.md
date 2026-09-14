# Japanese Official Source Census — Generation V

## Purpose

This census tracks surviving Japanese first-party/official web material for Pokémon Black, White, Black 2, and White 2. Japanese releases are the comparison baselines, but this file is only one branch of the larger public-source census.

The full page-level inventory is machine-readable in `../manifests/official-jp-sources.csv`.

## Current census status

### Pokémon.co.jp — Black / White

- Root: `https://www.pokemon.co.jp/series/bw/`
- Site map: `https://www.pokemon.co.jp/series/bw/sitemap/`
- Core Pokémon, story, character, communication, system and PGL/Dream World HTML branches: **Enumerated-core**.
- Registered communication subjects include C-Gear, wireless, Entralink, Xtransceiver, Pass-by Survey, Wi-Fi/Game Sync/Dream World, infrared, Feeling Check and Random Match.
- Registered system subjects include kanji mode, Poké Transfer, double wild encounters, Rotation Battle, Wonder Launcher/Miracle Shooter, Battle Subway and Pokémon Musical.
- Registered PGL subjects include PGL overview, Dream World, new/hidden abilities, additional Dream World features and Global Battle.
- Embedded media, externally linked campaigns, historical news/service notices and downloadable assets remain **Enumerating**.

### Nintendo Japan — Black / White

Registered roots include:

- `https://www.nintendo.co.jp/ds/irbj/index.html`
- `https://www.nintendo.co.jp/ds/irbj/about/index.html`
- `https://www.nintendo.co.jp/ds/irbj/information/index2.html`
- `https://www.nintendo.co.jp/ds/irbj/information/index3.html`

Nintendo's `topics/file/vol_xx/fileyy.html` feature series is **Enumerating**. Confirmed examples through at least `file27.html` are recorded in the manifest, but examples are not treated as the whole series.

`社長が訊く『ポケットモンスターブラック・ホワイト』` is registered as a five-section developer-primary interview branch:

1. `.../irbj/vol1/index.html`
2. `.../index2.html`
3. `.../index3.html`
4. `.../index4.html`
5. `.../index5.html`

### Pokémon.co.jp — Black 2 / White 2

- Root: `https://www.pokemon.co.jp/ex/b2w2/`
- Core story branch and three child pages: **Enumerated-core**.
- Character branch: protagonists plus `character01.html` through `character14.html`: **Enumerated-core**.
- Pokémon branch: root plus `pokemon01.html` through `pokemon08.html`: **Enumerated-core**.
- System branch: root plus `system01.html` through `system10.html`: **Enumerated-core**.
- Download-software page, Pokémon Dream Radar/AR Searcher site and Pokédex 3D Pro site: registered.
- Product page registered.
- `https://www.pokemon.co.jp/ex/b2w2/news/`: news index registered, but individual notices/campaign destinations remain **Enumerating**.

### Nintendo Japan — Black 2 / White 2

Registered roots:

- `https://www.nintendo.co.jp/ds/irej/index.html`
- `https://www.nintendo.co.jp/ds/irej/story/index.html`
- `https://www.nintendo.co.jp/ds/irej/adventure/index.html`
- `https://www.nintendo.co.jp/ds/irej/communication/index.html`

`社長が訊く『ポケットモンスターブラック２・ホワイト２』` is registered as six sections (`index.html` through `index6.html`) covering the sequel/two-years-later concept, 100-person play, Key System design, starting-town Pokémon Center, Pokémon design values, and “three sacred treasures”.

## Still-open Japanese official branches

The Japanese official census is **not complete**. Mandatory follow-up remains:

1. Full Nintendo BW `topics/file` sequence.
2. Every B2W2 news child notice and external campaign destination.
3. BW historical announcements not represented by the surviving site map.
4. PGL/Dream World maintenance, renewal, campaigns, competitions and shutdown-related notices.
5. Japanese Mystery Gift, movie, store, tournament, magazine and campaign distribution announcements.
6. Official promotional videos, TV commercials, downloadable media and image assets with provenance.
7. Official guidebook, soundtrack and related product pages.
8. Nintendo/Pokémon support notices for communication compatibility, maintenance and termination.
9. Internet Archive captures of Japanese official pages no longer live.
10. Japanese physical box/cart/manual scans by revision where provenance is adequate.

## Completion rule

Do not mark Japanese official material `Enumerated` as a whole until every open branch is itemized to the practical public limit or explicitly documented as unavailable/blocked with the discovery route recorded.
