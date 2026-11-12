"""Placing an eye shape on the canvas: position, rotation and morphing."""

from collections.abc import Sequence
from math import cos, sin

from .box import lidded_box
from .types import Disc, Line, Sdf


def eye(
    cx: float,
    cy: float,
    hw: float,
    hh: float,
    rad: float,
    ang: float,
    lines: Sequence[Line] = (),
    discs: Sequence[Disc] = (),
    special: Sdf | None = None,
    mix: float = 0.0,
) -> Sdf:
    """Build the distance function for one eye.

    The base shape is a lidded rounded box centred on (cx, cy) and rotated
    by ``ang``. ``special`` is an alternative shape (heart, cross, ...) in
    the eye's own coordinates; ``mix`` (0..1) cross-fades from the box to it.
    """
    ca = cos(ang)
    sa = sin(ang)

    if special is not None and mix >= 0.995:

        def only_special(px: float, py: float) -> float:
            dx = px - cx
            dy = py - cy
            return special(dx * ca + dy * sa, dy * ca - dx * sa)

        return only_special

    box = lidded_box(hw, hh, rad, lines, discs)

    if special is None or mix <= 0.005:

        def plain(px: float, py: float) -> float:
            dx = px - cx
            dy = py - cy
            return box(dx * ca + dy * sa, dy * ca - dx * sa)

        return plain

    def morph(px: float, py: float) -> float:
        dx = px - cx
        dy = py - cy
        lx = dx * ca + dy * sa
        ly = dy * ca - dx * sa
        d = box(lx, ly)
        return d + (special(lx, ly) - d) * mix

    return morph
