#!/usr/bin/env python3
"""Nintendo DS backwards executable-code decompression helpers."""

from __future__ import annotations

import struct
from dataclasses import dataclass


@dataclass(frozen=True)
class BackwardCompressionTrailer:
    tail_size: int
    header_size: int
    compressed_span: int
    extra_size: int


def find_backward_compression_trailer(data: bytes) -> BackwardCompressionTrailer | None:
    """Locate the backwards-compression trailer used by NDS executable modules."""
    for tail_size in range(0, 0x20, 4):
        if len(data) < tail_size + 8:
            continue
        word, extra_size = struct.unpack_from("<II", data, len(data) - tail_size - 8)
        header_size = word >> 24
        compressed_span = word & 0x00FFFFFF
        if header_size < 8 or compressed_span > len(data) - tail_size:
            continue
        padding_start = len(data) - tail_size - header_size
        padding_end = len(data) - tail_size - 8
        if padding_start < 0:
            continue
        if all(value == 0xFF for value in data[padding_start:padding_end]):
            return BackwardCompressionTrailer(
                tail_size=tail_size,
                header_size=header_size,
                compressed_span=compressed_span,
                extra_size=extra_size,
            )
    return None


def decompress_backward(data: bytes) -> tuple[bytes, bool]:
    """Return ``(payload, was_compressed)`` for an NDS executable module."""
    trailer = find_backward_compression_trailer(data)
    if trailer is None:
        return data, False

    tail = data[len(data) - trailer.tail_size :] if trailer.tail_size else b""
    core = data[: -trailer.tail_size] if trailer.tail_size else data

    # Raw Gen V overlay payloads can coincidentally resemble a compression
    # trailer. Observed raw entries terminate in a zero word.
    if core[-4:] == b"\0\0\0\0":
        return data, False

    compressed_span = min(trailer.compressed_span, len(core))
    prefix_size = len(core) - compressed_span
    prefix = core[:prefix_size]
    stream = core[prefix_size : len(core) - trailer.header_size]

    output = bytearray(len(core) + trailer.extra_size - prefix_size)
    output_written = 0
    input_read = 0
    mask = 0
    flags = 0

    while output_written < len(output):
        if mask == 0:
            if input_read >= len(stream):
                raise ValueError("backwards compression flag stream overrun")
            flags = stream[-1 - input_read]
            input_read += 1
            mask = 0x80

        if flags & mask:
            if input_read + 2 > len(stream):
                raise ValueError("backwards compression pair stream overrun")
            first = stream[-1 - input_read]
            second = stream[-2 - input_read]
            input_read += 2
            length = (first >> 4) + 3
            displacement = (((first & 0x0F) << 8) | second) + 3
            if displacement > output_written:
                if output_written < 2:
                    raise ValueError("invalid backwards compression back-reference")
                displacement = 2
            source = output_written - displacement
            for _ in range(length):
                if output_written >= len(output):
                    break
                output[-1 - output_written] = output[-1 - source]
                output_written += 1
                source += 1
        else:
            if input_read >= len(stream):
                raise ValueError("backwards compression literal stream overrun")
            output[-1 - output_written] = stream[-1 - input_read]
            input_read += 1
            output_written += 1

        mask >>= 1

    return bytes(prefix + output + tail), True
