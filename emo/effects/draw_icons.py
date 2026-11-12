"""Symbols beside the eyes: anger mark, ?, !, thinking dots, circling stars."""

from math import cos, pi, sin

from ..canvas import Canvas
from ..face import VW, Face
from .anchors import Anchors, draw_sprite
from .sprites import ANGER, DOT, EXCLAIM, QUESTION, SPARK, STAR, YELLOW
from .state import Effects

TAU = 2.0 * pi


def _pop(fx: Effects, name: str) -> float:
    """Fade-in factor for an icon that just appeared."""
    return min(1.0, fx.active[name] * 7.0)


def draw_marks(fx: Effects, canvas: Canvas, face: Face, at: Anchors) -> None:
    act = fx.active
    t = fx.t
    cx, cy = at.corner_x, at.corner_y
    if "anger" in act:
        big = 2 if sin(TAU * 3.0 * t) > 0 else 1
        draw_sprite(canvas, face, ANGER, cx, cy + 2, big, (255, 60, 50), _pop(fx, "anger"))
    if "question" in act:
        x = cx + sin(t * 3.0) * 1.2
        draw_sprite(canvas, face, QUESTION, x, cy + 3, 2, YELLOW, _pop(fx, "question"))
    if "exclaim" in act:
        a = _pop(fx, "exclaim")
        draw_sprite(canvas, face, EXCLAIM, cx, cy + 4 - (1.0 - a) * 4, 2, YELLOW, a)
    if "dots" in act:
        n = int(act["dots"] * 2.6) % 4
        base = min(cx - 6.0, VW - 18.0)
        for i in range(n):
            draw_sprite(canvas, face, DOT, base + i * 6, cy + 1, 2, (150, 225, 255))


def draw_stars(fx: Effects, canvas: Canvas, face: Face, at: Anchors) -> None:
    """Three stars circling the head, for dizzy and knocked-out faces."""
    if "stars" not in fx.active:
        return
    a = _pop(fx, "stars")
    for i in range(3):
        ang = fx.t * 3.2 + i * TAU / 3.0
        depth = sin(ang)
        front = depth > 0
        x = at.mx + cos(ang) * 30.0
        y = max(5.0, at.top - 5.0) + depth * 3.0
        draw_sprite(canvas, face, STAR if front else SPARK, x, y, 1, YELLOW, a * (1.0 if front else 0.6))
