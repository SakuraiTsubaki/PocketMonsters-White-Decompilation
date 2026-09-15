.syntax unified
.thumb
.section .text.overlay_0074,"ax",%progbits
.balign 4

.global Overlay074_GetRecord
.type Overlay074_GetRecord,%function
.thumb_func
Overlay074_GetRecord:
    movs r1, #20
    ldr  r2, .Ltable_ptr
    muls r1, r0
    adds r0, r2, r1
    bx   lr
    nop
.Ltable_ptr:
    .word Overlay074_Table

.balign 4
.global Overlay074_Table
.type Overlay074_Table,%object
Overlay074_Table:
    .word 13,  2, 24,  1, 1
    .word 13,  3, 25,  2, 1
    .word 13,  4, 26,  3, 1
    .word 13,  5, 27,  4, 1
    .word 13,  6, 28,  5, 1
    .word 13,  7, 29,  6, 1
    .word 13,  8, 30,  7, 1
    .word 13,  9, 31,  8, 1
    .word 13, 10, 32,  9, 1
    .word 13, 11, 33, 10, 1
    .word 13, 12, 34, 11, 1
    .word 13, 13, 35, 12, 1
    .word 13, 14, 36, 13, 1
    .word 14, 15, 37, 14, 1
    .word 14, 16, 38, 15, 1
    .word 14, 17, 39, 16, 1
    .word 14, 18, 40, 17, 1
    .word 14, 19, 41, 18, 1
    .word 16, 20, 42, 19, 2
    .word 16, 21, 43, 20, 2
    .word 15,  0,  0,  0, 0
    .word 25,  0,  0,  0, 0
    .word 23,  0,  0,  0, 0
    .word 24,  0,  0,  0, 0
    .word 21,  0,  0,  0, 0
    .word 22,  0,  0,  0, 0
.size Overlay074_Table, . - Overlay074_Table

.global Overlay074_StaticInit
Overlay074_StaticInit:
    .word 0
    .word 0
