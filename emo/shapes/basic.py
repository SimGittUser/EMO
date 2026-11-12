"""Simple shapes placed directly on the canvas, and how to combine them."""

from math import hypot, sqrt

from .types import Sdf


def disc(cx: float, cy: float, r: float) -> Sdf:
    def f(px: float, py: float) -> float:
        return hypot(px - cx, py - cy) - r

    return f


def pill(cx: float, cy: float, hw: float, hh: float) -> Sdf:
    """A fully rounded horizontal capsule."""
    r = min(hw, hh)
    bx = hw - r
    by = hh - r

    def f(px: float, py: float) -> float:
        qx = abs(px - cx) - bx
        qy = abs(py - cy) - by
        if qx > 0.0:
            return (sqrt(qx * qx + qy * qy) if qy > 0.0 else qx) - r
        if qy > 0.0:
            return qy - r
        return (max(qy, qx)) - r

    return f


def both(f: Sdf, g: Sdf) -> Sdf:
    """Intersection of two shapes."""

    def h(px: float, py: float) -> float:
        a = f(px, py)
        b = g(px, py)
        return max(b, a)

    return h


def band(cx: float, cy: float, nx: float, ny: float, half: float) -> Sdf:
    """A diagonal stripe through (cx, cy) with unit normal (nx, ny)."""

    def f(px: float, py: float) -> float:
        return abs((px - cx) * nx + (py - cy) * ny) - half

    return f
