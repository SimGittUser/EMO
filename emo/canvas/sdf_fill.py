"""The anti-aliased signed-distance-field rasteriser."""

from math import floor

from ..shapes.types import Sdf
from .canvas import Canvas
from .sdf_row import Rgb, fill_row


def fill_sdf(
    canvas: Canvas,
    sdf: Sdf,
    x0: float,
    y0: float,
    x1: float,
    y1: float,
    color: Rgb,
    alpha: float = 1.0,
    glow: float = 0.0,
    glow_strength: float = 0.3,
    exact: bool = True,
    shade: float = 0.0,
) -> None:
    """Fill the shape described by ``sdf`` inside the box (x0,y0)-(x1,y1).

    ``sdf(px, py)`` returns the signed distance in pixels from a point to
    the shape's edge (negative inside). ``glow`` adds a soft halo that many
    pixels wide and ``shade`` makes the top brighter than the bottom.
    """
    pad = glow + 1.0
    ix0 = max(0, floor(x0 - pad))
    ix1 = min(canvas.w, floor(x1 + pad) + 1)
    iy0 = max(0, floor(y0 - pad))
    iy1 = min(canvas.h, floor(y1 + pad) + 1)
    if ix0 >= ix1 or iy0 >= iy1 or alpha <= 0.003:
        return
    canvas.touch(iy0, iy1)
    cr, cg, cb = color
    span = max(1e-6, y1 - y0)
    rgb = (cr, cg, cb)
    for y in range(iy0, iy1):
        py = y + 0.5
        if shade:
            f = 1.0 + shade * (0.5 - (py - y0) / span)
            rgb = (min(255.0, cr * f), min(255.0, cg * f), min(255.0, cb * f))
        fill_row(canvas.rows[y], sdf, py, ix0, ix1, rgb, alpha, glow, glow_strength, exact)
