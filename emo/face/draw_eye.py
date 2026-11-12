"""Drawing one eye."""

from math import cos, sin
from typing import NamedTuple

from .. import shapes
from ..canvas import Canvas, fill_sdf
from ..shapes.types import Sdf
from .eye_box import place_eye
from .lids import lid_cuts
from .pose import Pose
from .state import Face


class Drawn(NamedTuple):
    sdf: Sdf
    pcx: float
    pcy: float
    hw: float
    hh: float
    ex: float  # half extent of the rotated eye on the canvas
    ey: float


def _special(face: Face, i: int, s: float, hw: float, hh: float) -> Sdf | None:
    kind = face.shape[i]
    if kind == "heart":
        return shapes.heart(hw, hh)
    if kind == "cross":
        return shapes.cross(hw, hh)
    if kind == "chevron":
        return shapes.chevron(hw, hh, -s)
    if kind == "spiral":
        return shapes.spiral(hw, hh, -face.spin * s)
    return None


def draw_eye(face: Face, canvas: Canvas, pose: Pose, i: int, s: float) -> Drawn:
    e = face.eyes[i].cur
    pcx, pcy, hw, hh, ang = place_eye(face, pose, i, s)
    rad = max(0.0, min(1.0, e["r"])) * min(hw, hh)
    lines, discs = lid_cuts(e, hw, hh, s)
    mix = max(0.0, min(1.0, e["mix"]))
    special = _special(face, i, s, hw, hh) if mix > 0.005 else None
    exact = not (special is not None and face.shape[i] == "spiral")
    sdf = shapes.eye(pcx, pcy, hw, hh, rad, ang, lines, discs, special, mix)
    ca, sa = abs(cos(ang)), abs(sin(ang))
    ex = hw * ca + hh * sa
    ey = hw * sa + hh * ca
    fill_sdf(
        canvas, sdf, pcx - ex, pcy - ey, pcx + ex, pcy + ey, pose.color,
        glow=pose.glow, glow_strength=0.27, exact=exact, shade=0.22,
    )
    return Drawn(sdf, pcx, pcy, hw, hh, ex, ey)
