# Pocket Monsters White — Decompilation

![Status](https://img.shields.io/badge/status-active_reconstruction-blue)
![Project](https://img.shields.io/badge/project-decompilation-blue)
![ROMs](https://img.shields.io/badge/ROM_binaries-not_included-success)

Decompilation and source-reconstruction project for **Pokémon White**.

## 🎯 Goals

- Reconstruct game code and data into readable, editable source form.
- Document executable structures, data formats, scripts, assets, and version differences.
- Keep analysis, tooling, metadata, and documentation reproducible.
- Build a clean foundation for long-term reverse-engineering work.

## 🚧 Status

This repository is in **active reconstruction**. The initial NDS filesystem/executable inventory is recorded, Black/White version differences are being mapped, and the first ARM9 overlay source unit now rebuilds byte-for-byte against the observed decompressed payload.

The currently supplied IRAO image is a documented underdump and is retained only as identified observational evidence. Preservation-clean full-ROM matching remains a separate target.

## 🗂️ Planned scope

- Code and executable analysis
- Game data structures
- Scripts and event data
- Graphics and asset metadata
- Audio and resource formats
- Maps and world data
- Tools, notes, manifests, and verification data

## 📌 Repository policy

ROM images and redistributed ROM binaries are **not included**. The repository is intended for reconstructed source, extracted/recreated project data, tooling, analysis, and documentation.

## 🧭 Roadmap

- [x] Establish initial baseline version/revision inventory
- [x] Begin mapping executable and data structures
- [x] Begin source reconstruction
- [ ] Classify and reconstruct remaining ARM9 overlays
- [ ] Document and reconstruct assets, scripts, and formats
- [ ] Establish preservation-clean full-ROM matching workflow

## 📚 Documentation

| Document | Purpose |
| --- | --- |
| [Decompilation bootstrap](docs/BOOTSTRAP.md) | Observed NDS layout, Black/White identity pass, and initial executable plan |
| [Matched overlay 74](docs/overlays/overlay_0074.md) | First byte-matching reconstructed executable unit |
| [Project status](docs/PROJECT_STATUS.md) | Current stage, coverage, validation level, and next milestones |
| [Roadmap](docs/ROADMAP.md) | Recommended decompilation phases and long-term progression |
| [Version coverage](docs/VERSIONS.md) | Regions, languages, revisions, updates, builds, and hashes |
| [Research guide](docs/RESEARCH_GUIDE.md) | Evidence, confidence, and research-recording workflow |
| [Verification guide](docs/VERIFICATION.md) | Standards for Observed, Reproduced, and Matched results |
| [Repository structure](docs/REPOSITORY_STRUCTURE.md) | Intended long-term source, data, asset, tooling, and manifest layout |
| [Documentation hub](docs/README.md) | Entry point for format, executable, script, asset, version, and verification notes |

## 🧱 Repository structure

Real reconstructed material is added only when evidence exists. Active areas now include `src/`, `linker/`, `tools/`, `docs/`, and `manifests/`; further `include/`, `data/`, `assets/`, and `tests/` areas will be added as verified material is reconstructed rather than as empty placeholders.

See [Repository Structure](docs/REPOSITORY_STRUCTURE.md) for the full organization policy.

## 🔬 Research and verification

Research findings identify the relevant target version or revision and clearly separate hypotheses from observed, reproduced, or matched results. A **Matched** executable unit means its reconstructed decompressed payload has been compared byte-for-byte with the identified source input; it does not imply that the full source ROM is preservation-clean.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules, evidence expectations, commit guidance, and pull-request requirements.
