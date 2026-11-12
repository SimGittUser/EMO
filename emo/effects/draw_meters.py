"""Read-outs: the listening sound wave and the battery."""

from math import pi, sin

from ..canvas import Canvas, fill_rect
from ..face import VH, Face
from .anchors import Anchors, draw_sprite
from .sprites import BATTERY
from .state import Effects

TAU = 2.0 * pi


def draw_wave(fx: Effects, canvas: Canvas, face: Face, at: Anchors) -> None:
    """A row of bouncing bars under the eyes while EMO listens."""
    if "wave" not in fx.active:
        return
    t = fx.t
    S, ox, oy = face.view
    a = min(1.0, fx.active["wave"] * 7.0)
    for i in range(-4, 5):
        amp = abs(sin(t * 6.0 + i * 0.9)) * (0.5 + 0.5 * sin(t * 2.3 + i * 1.7) ** 2)
        hh = (0.9 + 4.6 * amp * (1.0 - abs(i) / 6.0)) * S
        bx = ox + (at.mx + i * 5.0) * S
        by = oy + (VH - 6.5) * S
        half = max(0.5, 1.2 * S)
        fill_rect(canvas, bx - half, by - hh, bx + half, by + hh, (110, 215, 255), 0.9 * a)


def draw_battery(fx: Effects, canvas: Canvas, face: Face, at: Anchors) -> None:
    """A blinking red battery when low, or a green one filling up."""
    act = fx.active
    if "battery" not in act and "battery_fill" not in act:
        return
    fill = "battery_fill" in act
    age = act["battery_fill"] if fill else act["battery"]
    a = min(1.0, age * 7.0)
    color = (110, 240, 120) if fill else (255, 80, 65)
    if not (fill or sin(TAU * 1.4 * fx.t) > -0.3):
        return
    S, ox, oy = face.view
    draw_sprite(canvas, face, BATTERY, at.mx, 6.5, 1, color, a)
    bars = min(3, int(age * 2.2) + 1) if fill else 1
    px = max(1, int(S + 0.5))
    x0 = ox + at.mx * S - 6.5 * px
    y0 = oy + 6.5 * S - 3.5 * px
    for b in range(bars):
        fill_rect(
            canvas, x0 + (2 + b * 3) * px, y0 + 2 * px, x0 + (4 + b * 3) * px, y0 + 5 * px, color, a
        )
