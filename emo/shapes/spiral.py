"""A spinning swirl for dizzy eyes."""

from math import atan2, floor, hypot, pi

from .types import Sdf

TAU = 2.0 * pi


def spiral(hw: float, hh: float, phase: float) -> Sdf:
    """A swirl turned by ``phase`` radians. Only an approximate distance."""
    big = min(hw, hh)
    b = big / 2.3
    t = b * 0.27

    def f(lx: float, ly: float) -> float:
        r = hypot(lx, ly)
        u = r / b - (atan2(ly, lx) + phase) / TAU
        d = abs(u - floor(u + 0.5)) * b - t
        e = r - big
        return max(d, e)

    return f
