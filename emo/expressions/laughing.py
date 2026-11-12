"""Faces for laughing out loud."""

from typing import Any

from .colors import BRIGHT

LAUGHING: dict[str, dict[str, Any]] = {
    "laugh": {
        "shape": "chevron",
        "eyes": {"w": 26, "h": 26},
        "face": {"color": BRIGHT},
        "anim": {"bounce": (2.2, 5.0)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "speed": 1.4,
    },
    "giggle": {
        "eyes": {"bot": 0.55, "bot_curve": 1.0, "w": 27, "y": -2},
        "face": {"blush": 0.45},
        "anim": {"shake": (1.5, 9.0), "bounce": (1.5, 4.5)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "speed": 1.4,
    },
}
