"""Where one eye sits this frame, and how big it is."""

from math import cos, pi, sin
from typing import NamedTuple

from .blinking import closed
from .pose import Pose
from .state import Face
from .tuning import VH, VW

TAU = 2.0 * pi


class EyeBox(NamedTuple):
    pcx: float  # centre, in canvas pixels
    pcy: float
    hw: float  # half size, in canvas pixels
    hh: float
    ang: float


def place_eye(face: Face, pose: Pose, i: int, s: float) -> EyeBox:
    """Work out eye ``i`` (``s`` is -1 for the left eye, +1 for the right)."""
    f = face.f.cur
    e = face.eyes[i].cur
    lx, ly = f["lx"], f["ly"]
    shut = closed(face, i)
    wob = sin(TAU * face.phase["wobble"] + s * 1.2) * f["wobble"]
    # the eye on the side being looked at narrows a little, like a turning head
    w = e["w"] * pose.scale * (1.0 - 0.10 * lx * s) * (1.0 + 0.06 * shut)
    h = (
        e["h"]
        * pose.scale
        * (1.0 - 0.04 * lx * s)
        * (1.0 - 0.05 * abs(ly))
        * (1.0 - 0.93 * shut)
        * (1.0 + wob)
        * (1.0 + 0.012 * pose.breath * f["breath"])
        * (1.0 + 0.07 * pose.talk)
    )
    w = max(2.0, w)
    h = max(1.2, h)
    x = s * f["gap"] + e["x"] + lx * 9.0
    y = e["y"] + ly * 5.5 + 1.5 * shut
    ct, st = cos(pose.tilt), sin(pose.tilt)
    cx = VW / 2.0 + pose.fx + x * ct - y * st
    cy = VH / 2.0 + pose.fy + x * st + y * ct
    face.geom[i] = (cx, cy, w / 2.0, h / 2.0)
    return EyeBox(
        pose.ox + cx * pose.S,
        pose.oy + cy * pose.S,
        max(0.6, w * pose.S / 2.0),
        max(0.6, h * pose.S / 2.0),
        pose.tilt - e["rot"] * s,
    )
