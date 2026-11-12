"""Saving a canvas as a PNG image, using only the standard library."""

import struct
import zlib

from .canvas import Canvas


def _chunk(tag: bytes, data: bytes) -> bytes:
    body = struct.pack(">I", len(data)) + tag + data
    return body + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)


def to_png(canvas: Canvas, path: str, scale: int = 1) -> None:
    """Write the framebuffer to ``path``, each pixel ``scale`` pixels wide."""
    raw = bytearray()
    for row in canvas.rows:
        line = bytearray()
        for p in row:
            line += bytes(((p >> 16) & 255, (p >> 8) & 255, p & 255)) * scale
        for _ in range(scale):
            raw.append(0)
            raw += line
    header = struct.pack(">IIBBBBB", canvas.w * scale, canvas.h * scale, 8, 2, 0, 0, 0)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(_chunk(b"IHDR", header))
        f.write(_chunk(b"IDAT", zlib.compress(bytes(raw), 6)))
        f.write(_chunk(b"IEND", b""))
