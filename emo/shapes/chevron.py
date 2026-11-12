"""Squeezed-shut eyes: > and <."""

from math import hypot

from .types import Sdf


def chevron(hw: float, hh: float, direction: float) -> Sdf:
    """'>' when direction is +1, '<' when it is -1."""
    a = hw * 0.62
    b = hh * 0.62
    t = min(hw, hh) * 0.2
    vx = 2.0 * a
    vy = -b
    vv = vx * vx + vy * vy

    def f(lx: float, ly: float) -> float:
        wx = lx * direction + a
        wy = (ly if ly >= 0.0 else -ly) - b
        h = (wx * vx + wy * vy) / vv
        if h < 0.0:
            h = 0.0
        elif h > 1.0:
            h = 1.0
        return hypot(wx - vx * h, wy - vy * h) - t

    return f
