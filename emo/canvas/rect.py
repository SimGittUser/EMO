"""Axis-aligned rectangles."""

from .blend import blend
from .canvas import Canvas
from .sdf_row import Rgb


def fill_rect(
    canvas: Canvas,
    x0: float,
    y0: float,
    x1: float,
    y1: float,
    color: Rgb,
    alpha: float = 1.0,
) -> None:
    ix0 = max(0, round(x0))
    ix1 = min(canvas.w, round(x1))
    iy0 = max(0, round(y0))
    iy1 = min(canvas.h, round(y1))
    if ix0 >= ix1 or iy0 >= iy1 or alpha <= 0.003:
        return
    canvas.touch(iy0, iy1)
    r, g, b = color
    if alpha >= 0.999:
        run = [(int(r) << 16) | (int(g) << 8) | int(b)] * (ix1 - ix0)
        for y in range(iy0, iy1):
            canvas.rows[y][ix0:ix1] = run
        return
    for y in range(iy0, iy1):
        row = canvas.rows[y]
        for x in range(ix0, ix1):
            row[x] = blend(row[x], r, g, b, alpha)
