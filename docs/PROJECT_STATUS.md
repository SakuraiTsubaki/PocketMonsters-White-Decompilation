# Project Status

**Current stage:** Public-source survey and reconstruction baseline

This project currently assumes that no local retail ROM is available. Work therefore begins from publicly accessible official material, technical implementations, preservation archives, reverse-engineering research, historical web captures, and independently maintained references.

## Version inventory

| Target | Region | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Pokémon White | TBD | TBD | TBD | Public-source survey | Build authoritative release/revision inventory before claiming byte-level identity |

## Progress

- [x] Establish public-source-first research methodology
- [x] Create initial public source inventory (`docs/PUBLIC_SOURCE_SURVEY.md`)
- [ ] Establish authoritative regional/language/revision inventory
- [ ] Build source-by-source evidence ledger with provenance and confidence
- [ ] Reconstruct public NitroFS/NARC path catalog
- [ ] Document executable and overlay layout from public technical evidence
- [ ] Map symbols, functions, and major subsystems where public evidence permits
- [ ] Document game-data formats and resource containers
- [ ] Reconstruct scripts, events, flags, variables and behavior
- [ ] Reconstruct asset pipelines and metadata
- [ ] Reconstruct save, communication, online and distribution structures
- [ ] Catalog unused, dummy, debug and development material
- [ ] Add reproducible tooling that does not redistribute retail ROM binaries
- [ ] Add automated verification where practical

## Validation levels

- **Unverified** — proposed, repeated, or recorded but not independently checked.
- **Corroborated** — supported by multiple independent public sources.
- **Implemented** — represented in working public source code or tooling.
- **Preserved** — backed by surviving archival files or historical captures.
- **Observed** — directly demonstrated in trustworthy captures or published extracted data.
- **Matched** — reconstructed output is verified against an identified target; this level normally requires trustworthy byte-level reference evidence.

## Next milestones

1. Expand `PUBLIC_SOURCE_SURVEY.md` into a comprehensive source registry.
2. Build the release/region/language/revision matrix for Pokémon White.
3. Catalog all publicly documented BW NARC paths and file relationships with source provenance.
4. Separate ROM-derived facts, tool-derived facts, preservation evidence, secondary references, and unresolved claims.
5. Begin subsystem reconstruction only after each subsystem has an evidence map.

Update this file whenever the project reaches a meaningful milestone or adds a new supported target.