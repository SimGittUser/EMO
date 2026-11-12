"""Startled and frightened faces."""

from typing import Any

from .colors import BRIGHT, PALE

SCARED: dict[str, dict[str, Any]] = {
    "surprised": {
        "eyes": {"w": 25, "h": 33, "r": 1.0, "y": -1},
        "face": {"scale": 1.12},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["exclaim"],
        "speed": 1.7,
    },
    "startled": {
        "eyes": {"w": 27, "h": 35, "r": 1.0, "y": -2},
        "face": {"scale": 1.2, "color": BRIGHT},
        "anim": {"shake": (1.0, 16.0)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["exclaim"],
        "speed": 2.2,
    },
    "scared": {
        "eyes": {"w": 19, "h": 22, "r": 1.0, "top": 0.12, "top_slant": -0.3},
        "face": {"color": PALE, "gap": 25},
        "anim": {"shake": (0.9, 13.0)},
        "gaze": "dart",
        "blink": 0,
        "fx": ["sweat"],
        "speed": 1.6,
    },
    "nervous": {
        "eyes": {"w": 22, "h": 26, "r": 0.7, "top": 0.10, "top_slant": -0.25},
        "face": {"color": PALE},
        "anim": {"shake": (0.35, 9.0)},
        "gaze": "down_dart",
        "blink": 2.0,
        "fx": ["sweat"],
    },
    "falling": {
        "eyes": {"w": 23, "h": 31, "r": 1.0, "y": -9},
        "face": {"color": PALE, "scale": 1.1},
        "anim": {"shake": (1.3, 18.0)},
        "gaze": "fixed",
        "look": (0, 0.8),
        "blink": 0,
        "speed": 2.2,
    },
}
