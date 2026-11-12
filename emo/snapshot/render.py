"""Rendering one face to a canvas without a terminal."""

from random import Random

from .. import effects, face
from ..canvas import Canvas
from ..effects import Effects
from ..face import Face


def render(
    name: str,
    w: int = 96,
    h: int = 48,
    seconds: float = 1.5,
    seed: int = 7,
    glow: bool = True,
) -> Canvas:
    """Return a Canvas showing ``name`` after it has settled for a moment."""
    rng = Random(seed)
    emo = Face(rng)
    emo.glow = glow
    fx = Effects(rng)
    face.set_expression(emo, name)
    effects.set_effects(fx, emo.expr.get("fx", ()))
    canvas = Canvas(w, h)
    face.draw(emo, canvas)
    for _ in range(int(seconds * 30)):
        emo.blink_timer = 9.0  # keep the eyes open for the picture
        face.update(emo, 1 / 30)
        effects.update(fx, 1 / 30, emo)
    canvas.clear()
    face.draw(emo, canvas)
    effects.draw(fx, canvas, emo)
    return canvas
