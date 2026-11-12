"""Cross faces: a top lid slanted down towards the nose reads as a frown."""

from typing import Any

from .colors import AMBER, ORANGE, RED

CROSS: dict[str, dict[str, Any]] = {
    "annoyed": {
        "eyes": {"top": 0.45, "top_slant": 0.10, "bot": 0.12, "h": 28},
        "face": {"color": AMBER},
        "gaze": "fixed",
        "look": (0.6, 0),
        "blink": 5.0,
    },
    "angry": {
        "eyes": {"top": 0.38, "top_slant": 0.5, "bot": 0.08, "h": 27, "y": 1},
        "face": {"color": ORANGE},
        "anim": {"shake": (0.4, 11.0)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 6.0,
        "speed": 1.3,
    },
    "furious": {
        "eyes": {"top": 0.46, "top_slant": 0.62, "bot": 0.12, "h": 28, "w": 26, "y": 1},
        "face": {"color": RED},
        "anim": {"shake": (1.3, 14.0)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["anger"],
        "speed": 1.6,
    },
}
