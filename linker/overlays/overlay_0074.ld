ENTRY(Overlay074_GetRecord)
SECTIONS
{
  . = 0x021F5500;
  .text : { *(.text.overlay_0074) }
  /DISCARD/ : { *(.ARM.attributes) *(.comment) *(.note*) }
}
