"""The resting face. An expression only lists what differs from this."""

from .colors import CYAN

EYE_DEFAULTS: dict[str, float] = {
    "x": 0.0,  # offset from the resting position
    "y": 0.0,
    "w": 24.0,  # size
    "h": 30.0,
    "r": 0.45,  # corner roundness, 0 = square .. 1 = pill
    "rot": 0.0,  # radians, mirrored between the eyes
    "top": 0.0,
    "top_slant": 0.0,
    "top_curve": 0.0,
    "bot": 0.0,
    "bot_slant": 0.0,
    "bot_curve": 0.0,
    "mix": 0.0,  # 0 = normal eye, 1 = special shape
}

FACE_DEFAULTS: dict[str, float] = {
    "cr": float(CYAN[0]),
    "cg": float(CYAN[1]),
    "cb": float(CYAN[2]),
    "bright": 1.0,
    "fx": 0.0,  # whole-face offset
    "fy": 0.0,
    "tilt": 0.0,  # whole-face rotation (radians)
    "scale": 1.0,
    "gap": 23.0,  # half the distance between eye centres
    "shine": 0.0,  # sparkly highlights in the eyes
    "blush": 0.0,
    "bridge": 0.0,  # the bar that turns the eyes into shades
    "lx": 0.0,  # gaze, -1..1
    "ly": 0.0,
    # animation amounts (the Hz half of each pair lives outside the springs)
    "bounce": 0.0,
    "shake": 0.0,
    "sway": 0.0,
    "pulse": 0.0,
    "wobble": 0.0,
    "breath": 1.0,
}

ANIMS = ("bounce", "shake", "sway", "pulse", "wobble")
