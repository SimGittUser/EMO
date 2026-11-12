"""Where the eyes look."""

from math import sin

from .actions import blink
from .state import Face


def _next_target(face: Face) -> None:
    """Pick the next place for wandering eyes to jump to."""
    rng = face.rng
    old = face.gaze_target
    if face.gaze_mode == "dart":
        face.gaze_target = (rng.uniform(-0.9, 0.9), rng.uniform(-0.5, 0.5))
        face.gaze_timer = rng.uniform(0.15, 0.5)
    elif face.gaze_mode == "down_dart":
        face.gaze_target = (rng.uniform(-0.7, 0.7), rng.uniform(0.3, 0.8))
        face.gaze_timer = rng.uniform(0.3, 0.9)
    else:
        if rng.random() < 0.45:
            face.gaze_target = (0.0, 0.0)
        else:
            face.gaze_target = (rng.uniform(-0.8, 0.8), rng.uniform(-0.45, 0.45))
        face.gaze_timer = rng.uniform(0.7, 3.0)
        # eyes often blink as they jump a long way
        far = abs(face.gaze_target[0] - old[0]) > 0.7
        if far and face.blink_every and rng.random() < 0.4:
            blink(face)


def update_gaze(face: Face, dt: float) -> None:
    if face.attn_t > 0.0 and face.gaze_mode in ("wander", "fixed", "scan"):
        face.attn_t -= dt
        target = face.attn
    elif face.gaze_mode == "fixed":
        target = face.gaze_fixed
    elif face.gaze_mode == "scan":
        target = (0.85 * sin(face.t * 1.3), 0.05)
    else:
        face.gaze_timer -= dt
        if face.gaze_timer <= 0.0:
            _next_target(face)
        target = face.gaze_target
    face.f.tgt["lx"], face.f.tgt["ly"] = target
