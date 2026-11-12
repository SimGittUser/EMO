"""Cheeky and charming faces."""

from typing import Any

from .colors import WHITE

PLAYFUL: dict[str, dict[str, Any]] = {
    "wink": {
        "left": {"bot": 0.66, "bot_curve": 1.0, "w": 27, "y": -1},
        "right": {"h": 31},
        "face": {"tilt": 0.06},
        "anim": {"bounce": (0.8, 1.6)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
    },
    "smug": {
        "eyes": {"top": 0.34, "top_slant": 0.06, "bot": 0.28, "bot_curve": 0.55, "y": -1},
        "face": {"tilt": -0.05},
        "gaze": "fixed",
        "look": (0.4, -0.1),
        "blink": 5.0,
    },
    "mischief": {
        "eyes": {"top": 0.36, "top_slant": 0.45, "bot": 0.38, "bot_curve": 0.8},
        "gaze": "scan",
        "blink": 0,
    },
    "amazed": {
        "eyes": {"w": 29, "h": 34, "r": 1.0},
        "face": {"shine": 1.0, "scale": 1.08},
        "gaze": "fixed",
        "look": (0, -0.1),
        "blink": 0,
        "fx": ["sparkles"],
    },
    "pleading": {
        "eyes": {"w": 29, "h": 33, "r": 1.0, "top": 0.06, "top_slant": -0.22, "y": 1},
        "face": {"shine": 1.0},
        "anim": {"shake": (0.25, 6.0)},
        "gaze": "fixed",
        "look": (0, -0.25),
        "blink": 0,
    },
    "shy": {
        "eyes": {"h": 25, "w": 22, "top": 0.15, "y": 3},
        "face": {"blush": 1.0},
        "gaze": "fixed",
        "look": (-0.7, 0.55),
        "blink": 2.5,
    },
    "cool": {
        "eyes": {"w": 32, "h": 20, "r": 0.6, "top": 0.14, "y": -1},
        "face": {"color": WHITE, "bridge": 1.0, "gap": 21, "tilt": -0.04},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "glint": True,
    },
}
