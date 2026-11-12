"""A contact sheet of faces, saved as a PNG."""

from ..canvas import Canvas, to_png
from ..expressions import GALLERY
from .font import draw_label
from .render import render

DIVIDER = 0x202028


def sheet(
    path: str,
    names: list[str] | None = None,
    cols: int = 5,
    w: int = 96,
    h: int = 48,
    scale: int = 3,
) -> int:
    """Save the named faces (default: all) to ``path``; returns how many."""
    names = list(names or GALLERY)
    rows = (len(names) + cols - 1) // cols
    th = h + 9
    out = Canvas(cols * (w + 2), rows * th)
    for i, name in enumerate(names):
        tile = render(name, w, h)
        x0 = (i % cols) * (w + 2)
        y0 = (i // cols) * th
        for y in range(h):
            out.rows[y0 + y][x0 : x0 + w] = tile.rows[y]
            out.rows[y0 + y][x0 + w : x0 + w + 2] = [DIVIDER] * 2
        draw_label(out, name, x0 + 2, y0 + h + 2)
    to_png(out, path, scale)
    return len(names)
