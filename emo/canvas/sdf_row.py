"""Filling one pixel row of a shape described by a distance function."""

from ..shapes.types import Sdf
from .blend import blend, edge_alpha

type Rgb = tuple[float, float, float]


def fill_row(
    row: list[int],
    sdf: Sdf,
    py: float,
    x0: int,
    x1: int,
    rgb: Rgb,
    alpha: float,
    glow: float,
    glow_strength: float,
    exact: bool,
) -> None:
    """Fill pixels x0..x1 of ``row``, anti-aliasing the edges.

    When ``exact`` is true the distance is trusted as a real bound, which
    lets whole runs of pixels be skipped: a pixel 9px inside the shape
    guarantees the next 8 are inside too. Only the outline costs anything.
    """
    r, g, b = rgb
    packed = (int(r) << 16) | (int(g) << 8) | int(b)
    outer = 0.5 + glow
    solid = alpha >= 0.999
    x = x0
    while x < x1:
        d = sdf(x + 0.5, py)
        if d <= -0.5:
            end = min(x1, x + (int(-d - 0.5) + 1 if exact else 1))
            if solid:
                row[x:end] = [packed] * (end - x)
            else:
                for i in range(x, end):
                    row[i] = blend(row[i], r, g, b, alpha)
            x = end
        elif d >= outer:
            x += int(d - outer) + 1 if exact else 1
        else:
            a = edge_alpha(d, glow, glow_strength) * alpha
            row[x] = blend(row[x], r, g, b, a)
            x += 1
