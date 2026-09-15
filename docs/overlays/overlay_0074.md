# ARM9 overlay 74

## Status

**Matched** against the decompressed overlay payload observed in the supplied IRAO revision-0 input.

This is a match for one executable unit only. The supplied full ROM remains catalogued separately as a known underdump.

## Layout

- Overlay ID: `74`
- FAT file ID: `74`
- Load address: `0x021F5500`
- Decompressed/RAM size: `0x220` (544 bytes)
- BSS size: `0`
- Static initializer range: `0x021F5718..0x021F571C`
- Compressed payload size: 240 bytes
- Source: `src/overlay/overlay_0074.s`
- Linker script: `linker/overlays/overlay_0074.ld`

## Reconstructed structure

The payload contains a short Thumb accessor followed by a table at offset `0x10`.

The accessor computes:

```text
record = table + index * 20
```

The table contains 26 records of five 32-bit values each. The final eight bytes are zero; the observed static-initializer range begins at offset `0x218`.

The semantic purpose of the records is not yet named. Structural symbol names in the assembly are therefore provisional rather than claims about game semantics.

## Black / White relationship

The Black counterpart has the same 544-byte structure and same 26 table records. Its overlay load address is `0x021F54E0`, 0x20 bytes below White. The only decompressed Black/White byte difference is the relocated table pointer literal at offset `0x0C`:

- Black: `0x021F54F0`
- White: `0x021F5510`

Both resolve to `overlay_load + 0x10`.

## Match verification

The committed assembly was assembled in Thumb mode, linked at the observed address, converted to a flat binary, and compared byte-for-byte with the decompressed retail overlay payload.

Expected/rebuilt SHA-256:

`2767b34270fa1efc66b86b92568caf6f2fde8680946bdd9f6480f5d3bbb8a366`
