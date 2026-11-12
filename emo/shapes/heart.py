"""Heart eyes."""

from math import hypot, sqrt

from .types import Sdf


def heart(hw: float, hh: float) -> Sdf:
    """A heart fitted inside the half-size (hw, hh), point down."""
    k = min(hw / 0.62, 2.0 * hh / 1.12)

    def f(lx: float, ly: float) -> float:
        x = (lx if lx >= 0.0 else -lx) / k
        y = 0.552 - ly / k
        if x + y > 1.0:
            return (hypot(x - 0.25, y - 0.75) - 0.35355339) * k
        a = x * x + (y - 1.0) * (y - 1.0)
        m = 0.5 * (x + y) if x + y > 0.0 else 0.0
        b = (x - m) * (x - m) + (y - m) * (y - m)
        d = sqrt(min(b, a))
        return (d if x > y else -d) * k

    return f
