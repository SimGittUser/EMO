"""Advancing the face by one frame."""

import colorsys

from ..expressions import ANIMS
from .blinking import update_blinks
from .gaze import update_gaze
from .state import Face


def _update_morph(face: Face) -> None:
    """Move to / from special shapes, fading the old one out before swapping."""
    for i in (0, 1):
        eye = face.eyes[i]
        if face.shape[i] != face.want_shape[i]:
            if face.shape[i] is None or eye.cur["mix"] < 0.06:
                face.shape[i] = face.want_shape[i]
                eye.cur["mix"] = max(0.0, min(eye.cur["mix"], 0.06))
            else:
                eye.tgt["mix"] = 0.0
                continue
        eye.tgt["mix"] = 1.0 if face.shape[i] else 0.0


def update(face: Face, dt: float) -> None:
    face.t += dt
    update_gaze(face, dt)
    update_blinks(face, dt)
    _update_morph(face)
    if face.expr.get("rainbow"):
        r, g, b = colorsys.hsv_to_rgb((face.t * 0.45) % 1.0, 0.75, 1.0)
        face.f.tgt["cr"], face.f.tgt["cg"], face.f.tgt["cb"] = r * 255, g * 255, b * 255

    # springs, in small sub-steps so a slow frame can't blow them up
    n = int(dt / 0.012) + 1
    h = dt / n
    for _ in range(n):
        face.eyes[0].step(h, face.speed)
        face.eyes[1].step(h, face.speed)
        face.f.step(h, face.speed)

    for a in ANIMS:
        face.phase[a] += face.hz[a] * dt
    face.spin += dt * 5.5
    face.talk += ((1.0 if face.talking else 0.0) - face.talk) * min(1.0, dt * 10.0)
    if face.glitch > 0.0:
        face.glitch = max(0.0, face.glitch - dt * 2.2)
