# ARM9 overlay reconstruction status

This directory tracks executable reconstruction for the 237 ARM9 overlays observed in the current Black/White revision-0 inputs.

## Inventory baseline

- ARM9 overlay entries: **237** in Black and **237** in White.
- ARM7 overlay entries: **0** in both observed inputs.
- Overlay FAT file IDs occupy `0..236`; named NitroFS files begin after the overlay payloads.
- All 237 observed Black overlay payloads can be expanded to the RAM size declared by their overlay-table entries.
- All 237 observed White overlay payloads can be expanded to the RAM size declared by their overlay-table entries.

## Compression state

Observed uncompressed Black overlay IDs:

`1, 2, 7, 37, 79, 80, 95, 228`

Observed uncompressed White overlay IDs:

`1, 2, 3, 7, 37, 79, 80, 95, 228`

The remaining payloads use the Nintendo DS backwards executable-code compression format handled by the current bootstrap tooling.

## Zero-filled overlay entries

The following **57** overlay IDs have byte-identical compressed payloads and byte-identical decompressed payloads in the observed Black and White inputs:

`5, 66, 84, 85, 86, 87, 89, 108, 113, 126, 130, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 169, 189, 190, 191, 192, 193, 200, 201, 202, 226, 229, 232, 233, 234, 235, 236`

Every one of these 57 entries expands to **exactly 32 zero bytes** in both observed versions. They are therefore tracked as **zero-filled structural overlay entries**, not as reconstructed common code.

Their runtime purpose is not yet established. In particular, zero-filled payloads must not be labelled “unused” until overlay-loading references and execution paths are checked. Some may be placeholders, stubs, reserved overlay slots, or entries whose meaningful behavior is supplied elsewhere.

Only five overlay-table entries are completely identical across the two observed tables: IDs `95, 139, 140, 141, 142`. Four of those (`139..142`) belong to the zero-filled set; overlay 95 is a separate uncompressed non-zero entry.

## Current matched source

- [Overlay 74](overlay_0074.md) — first reconstructed non-zero source unit; 544-byte decompressed payload matched byte-for-byte in both Black and White using the same assembly source and version-specific link address.

Overlay 74 differs only by an absolute table-pointer relocation caused by the version-specific `+0x20` load-address shift; its code and 26-record table are otherwise shared.

## Reconstruction order

1. Trace references to zero-filled overlay IDs before assigning used/unused/placeholder semantics.
2. Reconstruct small non-zero overlays and verify exact decompressed payload hashes.
3. Separate address-only relocation differences from code/data differences.
4. Promote structural labels to semantic names only after call sites, data consumers, or external evidence verify their purpose.
5. Preserve version-specific link/load data instead of forcing Black and White into one binary layout.
6. Keep full-ROM preservation-clean matching separate from per-overlay matches against the identified observational inputs.
