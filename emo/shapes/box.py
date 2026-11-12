"""The resting eye: a rounded box with eyelids carved out of it."""

from collections.abc import Sequence
from math import hypot, sqrt

from .types import Disc, Line, Sdf


def lidded_box(
    hw: float,
    hh: float,
    rad: float,
    lines: Sequence[Line],
    discs: Sequence[Disc],
) -> Sdf:
    """Distance to a rounded box (half-size hw x hh) in its own coordinates."""
    bx = hw - rad
    by = hh - rad

    def box(lx: float, ly: float) -> float:
        qx = (lx if lx >= 0.0 else -lx) - bx
        qy = (ly if ly >= 0.0 else -ly) - by
        if qx > 0.0:
            d = (sqrt(qx * qx + qy * qy) if qy > 0.0 else qx) - rad
        elif qy > 0.0:
            d = qy - rad
        else:
            d = (max(qy, qx)) - rad
        for a, b, c in lines:
            k = a * lx + b * ly + c
            d = max(d, k)
        for ex, ey, er in discs:
            k = er - hypot(lx - ex, ly - ey)
            d = max(d, k)
        return d

    return box
