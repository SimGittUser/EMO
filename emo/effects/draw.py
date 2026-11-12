"""Drawing every overlay effect on top of the face."""

from math import pi, sin

from ..canvas import Canvas
from ..face import Face
from .anchors import anchors, draw_sprite
from .draw_icons import draw_marks, draw_stars
from .draw_meters import draw_battery, draw_wave
from .state import Effects

TAU = 2.0 * pi


def draw(fx: Effects, canvas: Canvas, face: Face) -> None:
    at = anchors(face)
    for p in fx.parts:
        u = p.age / p.life
        alpha = min(1.0, u * 8.0) * min(1.0, (1.0 - u) * 2.8)
        x = p.x + (sin(TAU * (p.wob_hz * p.age + p.seed)) * p.wob if p.wob else 0.0)
        draw_sprite(canvas, face, p.sprite, x, p.y, p.size + p.grow * p.age, p.color, alpha)
    draw_marks(fx, canvas, face, at)
    draw_stars(fx, canvas, face, at)
    draw_wave(fx, canvas, face, at)
    draw_battery(fx, canvas, face, at)
