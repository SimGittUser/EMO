"""Turning eyelid settings into the cuts that carve an eye."""

from math import sqrt

from ..shapes.types import Disc, Line


def lid_cuts(
    e: dict[str, float],
    hw: float,
    hh: float,
    s: float,
) -> tuple[list[Line], list[Disc]]:
    """Cuts for one eye with settings ``e`` and half-size (hw, hh) pixels.

    A flat lid is a straight line; a curved lid is a big circle touching the
    lid line, which leaves an arc-shaped edge.
    """
    lines: list[Line] = []
    discs: list[Disc] = []
    top = e["top"]
    if top > 0.004:
        m = -e["top_slant"] * s
        n = sqrt(1.0 + m * m)
        y0 = -hh + min(1.0, top) * 2.0 * hh
        if e["top_curve"] > 0.03:
            R = hw * 1.05 / e["top_curve"]
            discs.append((m / n * R, y0 - R / n, R))
        else:
            lines.append((m / n, -1.0 / n, y0 / n))
    bot = e["bot"]
    if bot > 0.004:
        m = -e["bot_slant"] * s
        n = sqrt(1.0 + m * m)
        y1 = hh - min(1.0, bot) * 2.0 * hh
        if e["bot_curve"] > 0.03:
            R = hw * 1.05 / e["bot_curve"]
            discs.append((-m / n * R, y1 + R / n, R))
        else:
            lines.append((-m / n, 1.0 / n, -y1 / n))
    return lines, discs
