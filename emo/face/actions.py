"""One-off things the face can be told to do."""

from .state import Face


def blink(face: Face, dur: float | None = None) -> None:
    d = dur or face.blink_dur
    face.blinks = [[0.0, d, 0.15], [0.0, d, 0.15]]


def wink(face: Face, eye: int = 0, dur: float = 0.55) -> None:
    """Close one eye for a moment (0 = left, 1 = right)."""
    face.blinks[eye] = [0.0, dur, 0.4]


def look_at(face: Face, x: float, y: float, hold: float = 1.5) -> None:
    """Pull the gaze to a point (-1..1 on both axes) for ``hold`` seconds."""
    face.attn = (max(-1.0, min(1.0, x)), max(-1.0, min(1.0, y)))
    face.attn_t = hold


def kick(face: Face, vx: float, vy: float) -> None:
    """Jolt the whole face; the springs bring it back."""
    face.f.vel["fx"] += vx
    face.f.vel["fy"] += vy


def pop(face: Face, v: float = 3.0) -> None:
    """Make the eyes swell for an instant."""
    face.f.vel["scale"] += v
