"""Blinking: when it happens, and how shut an eye is right now."""

from .actions import blink
from .state import Face


def _ease(u: float) -> float:
    return u * u * (3.0 - 2.0 * u)


def update_blinks(face: Face, dt: float) -> None:
    rng = face.rng
    if face.blink_every:
        face.blink_timer -= dt
        if face.blink_timer <= 0.0:
            blink(face)
            face.blink_timer = face.blink_every * rng.uniform(0.5, 1.5)
            if rng.random() < 0.18:
                face.blink_again = face.blink_dur + 0.06
    if face.blink_again > 0.0:
        face.blink_again -= dt
        if face.blink_again <= 0.0:
            blink(face)
    for b in face.blinks:
        if b is not None:
            b[0] += dt
    face.blinks = [None if (b is None or b[0] >= b[1]) else b for b in face.blinks]


def closed(face: Face, i: int) -> float:
    """How shut eye ``i`` is, from 0 (open) to 1 (closed)."""
    b = face.blinks[i]
    if b is None:
        return 0.0
    u = b[0] / b[1]
    close = (1.0 - b[2]) * 0.35
    if u < close:
        return _ease(u / close)
    if u < close + b[2]:
        return 1.0
    return 1.0 - _ease(min(1.0, (u - close - b[2]) / max(1e-6, 1.0 - close - b[2])))
