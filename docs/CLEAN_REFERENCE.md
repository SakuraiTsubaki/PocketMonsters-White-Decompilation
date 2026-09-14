# Clean Reference — Pokémon White Version (USA/Europe v1.0)

This repository separates the **canonical clean reference** from the locally supplied ROM used for the first direct structural scan. The retail ROM binary itself is never committed.

## Canonical clean reference

- Region: USA/Europe
- Version: 1.0
- Mode: NDSi Enhanced
- Size: `268435456` bytes
- CRC32: `B552501C`
- MD5: `77C34BA77F8FA44E7CAF04F695DB0560`
- SHA-1: `BC696A0DFB448C7B3A8A206F0F8214411A039208`
- SHA-256: `B288BB061FD646894F5059F55CD0A1EFB13B4F0CFD3D9E06E9E42A5BD9431AC6`

This is the USA/Europe v1.0 reconstruction/verification identity used for clean-reference comparisons.

## Local raw input used for the initial direct scan

- Filename: `Pokemon.White.Version.EUR.NDS-SweeTnDs.nds`
- Internal title: `POKEMON W`
- Game code: `IRAO`
- Revision field: `0`
- Unit code: `0x02`
- CRC32: `EDCD5161`
- MD5: `8DFEF9A099E1269AF5C1FCF9D7736A11`
- SHA-1: `F94D4578956487C09FEE20809A591E858017769E`
- SHA-256: `93E4F473CE9A0543BCCF2E689ECD07AB4FCC39DD00FB4F194343CBD5E70E17ED`
- Canonical clean match: **No**

The raw input remains useful as an immutable analysis input, but observations obtained from it must not be silently promoted to canonical-clean verification. Canonical-sensitive results must be reverified against the clean reference or equivalent independently verified clean-reference evidence.

## Reference rules

1. Never commit retail `.nds` binaries.
2. Keep canonical clean identity and raw-input identity in separate manifests.
3. Preserve Black/White and region/revision differences; do not normalize them away.
4. Mark evidence as `Observed raw input`, `Canonical verified`, or `External corroboration` as appropriate.
5. Extracted/reconstructed source, tools, metadata, manifests, documentation, patches, and reviewable assets may be committed.
6. Prefer reproducible extraction/rebuild paths over opaque binary dumps.

## Initial raw-input structural observation

- FAT entries: **484**
- Named NitroFS files: **247**
- NARC archives: **237**
- ARM9 overlays: **237**

These counts were directly observed from the local raw input. The current next phase is to reverify White-specific structures against the clean reference while using Black/White paired analysis only where equivalence is demonstrated rather than assumed.
