# Regional Survey Matrix — Pokémon White

## Purpose

Track every officially released regional, territorial, language, and revision build of Pokémon White against the original Japanese release baseline.

The matrix is intentionally evidence-first. Do not fill unknown fields from memory or assumption. Use `Unknown` until a source is found.

## Baseline policy

- Baseline axis: original Japanese retail release.
- Every non-Japanese build is compared directly against the Japanese baseline.
- Non-Japanese builds are also cross-compared where necessary.
- Revisions are separate records.
- Language, territory, cartridge identity, release date, revision, and technical differences must not be conflated.
- "International" is not a valid substitute for enumerating individual official builds.

## Build inventory

| Record ID | Version | Territory / market | Language | Release date | Revision | Product / cart code | Known hashes | Evidence status | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WHITE-JP-BASE | White | Japan | Japanese | Unknown | Unknown | Unknown | Unknown | Baseline pending verification | Pending |

Add one row for every confirmed official build and every confirmed revision.

## Difference matrix

| Build ID | Category | Japanese baseline state | Regional state | Difference class | Evidence level | Source(s) | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |

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

## Comparison rule

A localized text difference is not automatically a technical ROM difference category by itself; record the text difference, then separately record any encoding, font, archive-layout, script, executable, or resource change that makes it technically distinct.

Likewise, a regional bug fix must be recorded as a regional/revision implementation difference rather than generalized as a Generation V rule unless evidence shows it applies to all builds.
