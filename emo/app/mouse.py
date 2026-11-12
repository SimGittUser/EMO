"""Mouse input: the pointer is a hand - it pats, pokes, strokes and tickles."""

from .. import brain
from ..face import hit_eye, look_at
from .state import App


def _gaze(vx: float, vy: float) -> tuple[float, float]:
    """A point on the virtual screen as a gaze direction."""
    return (vx - 64.0) / 46.0, (vy - 32.0) / 24.0


def _click(app: App, vx: float, vy: float) -> None:
    eye = hit_eye(app.face, vx, vy)
    if eye is None:
        brain.event(app.brain, "pat")
    else:
        brain.event(app.brain, "poke", eye=eye)


def on_mouse(app: App, kind: str, col: int, row: int, button: int | str) -> None:
    L = app.layout
    if L is None or L.small:
        return
    px = col - 1 - L.px0
    cy = row - L.py0
    inside = 0 <= px < L.pw and 0 <= cy < L.ph
    S, ox, oy = app.face.view
    vx = (px + 0.5 - ox) / S
    vy = (cy * 2 + 1.0 - oy) / S
    if kind == "release":
        if app.press and not app.press[2] and inside:
            _click(app, vx, vy)
        app.press = None
    if not inside:
        return
    if kind == "move":
        look_at(app.face, *_gaze(vx, vy), 1.2)
    elif kind == "press":
        app.o.demo = False
        if button == 2:
            brain.event(app.brain, "poke", eye=hit_eye(app.face, vx, vy))
        else:
            app.press = [col, row, False]
    elif kind == "drag" and app.press:
        moved = abs(col - app.press[0]) + abs(row - app.press[1])
        if app.press[2] or moved >= 2:
            app.press[2] = True
            brain.event(app.brain, "stroke")
            look_at(app.face, *_gaze(vx, vy), 0.5)
    elif kind == "wheel":
        brain.event(app.brain, "tickle")
