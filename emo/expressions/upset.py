"""Sad faces: a top lid that droops at the outer corners."""

from typing import Any

from .colors import BLUE, DIM

UPSET: dict[str, dict[str, Any]] = {
    "sad": {
        "eyes": {"top": 0.32, "top_slant": -0.42, "y": 4, "h": 27},
        "face": {"color": BLUE},
        "gaze": "fixed",
        "look": (0, 0.55),
        "blink": 5.0,
        "speed": 0.6,
    },
    "cry": {
        "eyes": {"top": 0.40, "top_slant": -0.5, "bot": 0.08, "y": 4, "h": 27},
        "face": {"color": BLUE},
        "anim": {"shake": (0.5, 5.0)},
        "gaze": "fixed",
        "look": (0, 0.6),
        "blink": 0,
        "fx": ["tears"],
    },
    "hungry": {
        "eyes": {"top": 0.36, "top_slant": -0.3, "h": 26, "y": 3},
        "face": {"color": DIM, "bright": 0.8},
        "gaze": "fixed",
        "look": (0, 0.5),
        "blink": 3.0,
        "fx": ["battery"],
        "speed": 0.6,
    },
}
