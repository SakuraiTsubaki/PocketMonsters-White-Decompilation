# Documentation Hub

This directory is the central documentation portal for the decompilation project. Use it to move from target identification and public-source research through reconstruction, asset handling, manifests, and verification without losing version context or evidence.

## Quick links

| Document | Purpose |
| --- | --- |
| [Project Status](PROJECT_STATUS.md) | Current stage, target coverage, validation level, and next milestones |
| [Roadmap](ROADMAP.md) | Recommended project phases from target definition through reproducible reconstruction |
| [Version Coverage](VERSIONS.md) | Regions, languages, revisions, builds, public-reference hashes, and support status |
| [Public Source Survey](PUBLIC_SOURCE_SURVEY.md) | No-local-ROM research premise, source classes, Japanese-baseline policy, and public-source workstreams |
| [Regional Survey Matrix](REGIONAL_SURVEY_MATRIX.md) | Japanese-baseline-to-region build inventory and difference tracking |
| [NARC / NitroFS Path Catalog](NARC_PATH_CATALOG.md) | Evidence-backed internal path/role catalog and cross-game path movement |
| [Research Guide](RESEARCH_GUIDE.md) | Evidence, confidence, offsets, naming, and research-recording practices |
| [Verification Guide](VERIFICATION.md) | Standards for Unverified, Observed, Reproduced, and Matched results |
| [Repository Structure](REPOSITORY_STRUCTURE.md) | Intended long-term layout for source, data, assets, tools, tests, and manifests |
| [Project Standards](PROJECT_STANDARDS.md) | Naming, provenance, generated-data, manifest, and repository-boundary rules |
| [Asset Workflow](ASSET_WORKFLOW.md) | Extraction, reviewable assets, deduplication, manifest registration, and batch workflow |
| [Manifest Guide](../manifests/README.md) | Machine-readable inventories, hashes, target coverage, provenance, and shared assets |
| [Contributing](../CONTRIBUTING.md) | Contribution rules, evidence expectations, commits, and pull-request guidance |

## Active machine-readable inventories

- `../manifests/narc-paths.csv` — current evidence-backed NARC/NitroFS role inventory. Unknown roles and unverified target-specific counts stay explicit rather than being inferred.

## Research areas

As verified work becomes concrete, documentation may grow into areas such as `architecture/`, `formats/`, `research/`, `versions/`, and `verification/`. Create these directories when they contain real research material rather than as empty placeholders.

## Recommended documentation flow

1. Identify the exact target or unresolved target question in `VERSIONS.md` and `REGIONAL_SURVEY_MATRIX.md`.
2. Register sources and assumptions under `PUBLIC_SOURCE_SURVEY.md` and `RESEARCH_GUIDE.md`.
3. Record internal paths/formats only at the confidence level supported by evidence; preserve source conflicts.
4. Reconstruct source, data, or assets following `PROJECT_STANDARDS.md` and `REPOSITORY_STRUCTURE.md`.
5. For asset work, follow `ASSET_WORKFLOW.md` and register material in `../manifests/`.
6. Apply the validation levels defined in `VERIFICATION.md`.
7. Update `PROJECT_STATUS.md` and `ROADMAP.md` when meaningful milestones are reached.

## Documentation rules

- Distinguish confirmed findings from hypotheses and public-reference metadata from project-verified target data.
- Identify the exact target version or revision for version-specific claims whenever evidence permits.
- Record paths, symbols, offsets, hashes, commands, sources, and conflicts when practical.
- Use `TBD`, `unknown`, or `null` instead of inventing missing information.
- Preserve enough provenance for another researcher to reproduce or challenge a finding.
- Keep retail ROM images, decrypted game images, console keys, and other redistributable game binaries out of the repository.