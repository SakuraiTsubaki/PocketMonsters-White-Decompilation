# Clean Reference — Pokémon White Version EUR

This repository treats the exact analyzed ROM identified below as the **project clean reference** for EUR White work. The ROM binary itself is never committed. All decompilation, extraction, comparison, reconstruction, and verification artifacts must remain traceable to this exact reference.

## Identity

- Internal title: `POKEMON W`
- Game code: `IRAO`
- Revision: `0`
- Unit code: `0x02`
- Size: `268435456` bytes
- CRC32: `EDCD5161`
- MD5: `8DFEF9A099E1269AF5C1FCF9D7736A11`
- SHA-1: `F94D4578956487C09FEE20809A591E858017769E`
- SHA-256: `93E4F473CE9A0543BCCF2E689ECD07AB4FCC39DD00FB4F194343CBD5E70E17ED`

## Reference rules

1. The retail `.nds` binary is read-only input and is not committed to GitHub.
2. Extracted/reconstructed source, metadata, manifests, conversion tools, documentation, and reviewable assets may be committed.
3. Derived files should remain reproducible from this exact reference whenever practical.
4. Any later regional/revision ROM is a separate reference, not a replacement for this one.
5. “Clean reference” here means the project's immutable binary baseline; it does not independently certify archival dump provenance.
6. Black/White differences are preserved rather than normalized away.

## Structural baseline

- FAT entries: **484**
- Named NitroFS files: **247**
- NARC archives: **237**
- ARM9 overlays: **237**

The next layer is the complete NitroFS/NARC census and member-level Black/White comparison.
