"""An X - the classic knocked-out eye."""

from math import hypot

from .types import Sdf


def cross(hw: float, hh: float) -> Sdf:
    a = min(hw, hh) * 0.8
    t = a * 0.27

    def f(lx: float, ly: float) -> float:
        x = lx if lx >= 0.0 else -lx
        y = ly if ly >= 0.0 else -ly
        h = (x + y) / (2.0 * a)
        h = min(h, 1.0)
        return hypot(x - a * h, y - a * h) - t

    return f
