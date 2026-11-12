"""The whole-face numbers for one frame: offset, tilt, scale, colour."""

from math import cos, pi, sin
from typing import NamedTuple

from ..canvas import Canvas
from .state import Face
from .tuning import VH, VW

TAU = 2.0 * pi


class Pose(NamedTuple):
    S: float  # canvas pixels per virtual pixel
    ox: float  # where the virtual screen starts on the canvas
    oy: float
    fx: float  # face offset on the virtual screen
    fy: float
    tilt: float
    scale: float
    breath: float
    talk: float
    color: tuple[float, float, float]
    glow: float


def face_pose(face: Face, canvas: Canvas) -> Pose:
    S = min(canvas.w / VW, canvas.h / VH)
    ox = (canvas.w - VW * S) / 2.0
    oy = (canvas.h - VH * S) / 2.0
    face.view = (S, ox, oy)
    f = face.f.cur
    ph = face.phase
    t = face.t

    shake = f["shake"]
    sway = sin(TAU * ph["sway"]) * f["sway"]
    breath = sin(TAU * 0.22 * t)
    talk = face.talk * (0.5 + 0.5 * sin(TAU * 5.3 * t)) * (0.6 + 0.4 * sin(TAU * 1.7 * t))
    fx = f["fx"] + sin(TAU * ph["shake"]) * shake + sway * 22.0
    fy = (
        f["fy"]
        - abs(sin(pi * ph["bounce"])) * f["bounce"]
        + cos(TAU * ph["shake"] * 1.31) * shake * 0.35
        + breath * 0.35 * f["breath"]
        - talk * 0.8
    )
    beat = max(0.0, sin(TAU * ph["pulse"])) ** 2
    scale = max(0.2, f["scale"] * (1.0 + beat * f["pulse"]))
    bright = max(0.0, f["bright"])
    color = (
        max(0.0, min(255.0, f["cr"] * bright)),
        max(0.0, min(255.0, f["cg"] * bright)),
        max(0.0, min(255.0, f["cb"] * bright)),
    )
    glow = max(1.5, 3.2 * S) if face.glow else 0.0
    return Pose(S, ox, oy, fx, fy, f["tilt"] + sway, scale, breath, talk, color, glow)
