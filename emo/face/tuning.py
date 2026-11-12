"""How springy each part of the face is.

Each entry is (stiffness, damping ratio). A ratio below 1 overshoots a
little, which is what makes the eyes feel squishy; 1 settles without bounce.
"""

VW, VH = 128.0, 64.0  # the virtual screen every face is designed on

EYE_SPRING: dict[str, tuple[float, float]] = {
    "x": (240, 0.6),
    "y": (240, 0.6),
    "w": (240, 0.55),
    "h": (240, 0.55),
    "r": (200, 1.0),
    "rot": (200, 0.7),
    "top": (300, 0.85),
    "top_slant": (260, 0.85),
    "top_curve": (260, 1.0),
    "bot": (300, 0.85),
    "bot_slant": (260, 0.85),
    "bot_curve": (260, 1.0),
    "mix": (230, 1.0),
}

FACE_SPRING: dict[str, tuple[float, float]] = {
    "cr": (110, 1.0),
    "cg": (110, 1.0),
    "cb": (110, 1.0),
    "bright": (110, 1.0),
    "fx": (200, 0.5),
    "fy": (200, 0.5),
    "tilt": (150, 0.55),
    "scale": (260, 0.5),
    "gap": (220, 0.7),
    "shine": (150, 1.0),
    "blush": (90, 1.0),
    "bridge": (200, 1.0),
    "lx": (420, 0.8),
    "ly": (420, 0.8),
    "bounce": (120, 1.0),
    "shake": (160, 1.0),
    "sway": (90, 1.0),
    "pulse": (120, 1.0),
    "wobble": (120, 1.0),
    "breath": (60, 1.0),
}

DEFAULT_HZ = {"bounce": 1.6, "shake": 10.0, "sway": 0.5, "pulse": 1.3, "wobble": 1.0}
