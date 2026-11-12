"""Calm, attentive faces."""

from typing import Any

from .colors import AMBER

CALM: dict[str, dict[str, Any]] = {
    "neutral": {"blink": 3.6, "gaze": "wander"},
    "curious": {
        "left": {"h": 27, "top": 0.12},
        "right": {"h": 35, "w": 27, "y": -2},
        "face": {"tilt": 0.10},
        "gaze": "wander",
        "blink": 3.0,
    },
    "listening": {
        "eyes": {"h": 32, "w": 25},
        "face": {"tilt": 0.07},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 4.0,
        "fx": ["wave"],
    },
    "thinking": {
        "eyes": {"top": 0.14, "h": 29},
        "left": {"top": 0.30},
        "gaze": "fixed",
        "look": (0.6, -0.8),
        "blink": 4.5,
        "fx": ["dots"],
    },
    "confused": {
        "left": {"top": 0.30, "top_slant": 0.25, "h": 27},
        "right": {"h": 34, "w": 26, "y": -2, "r": 0.8},
        "face": {"tilt": -0.09},
        "gaze": "fixed",
        "look": (0.15, -0.2),
        "blink": 3.0,
        "fx": ["question"],
    },
    "bored": {
        "eyes": {"top": 0.5, "bot": 0.04, "y": 2},
        "anim": {"sway": (0.02, 0.18)},
        "gaze": "fixed",
        "look": (-0.65, 0.35),
        "blink": 2.8,
        "blink_dur": 0.5,
        "speed": 0.5,
    },
    "suspicious": {
        "eyes": {"top": 0.48, "bot": 0.36, "w": 26},
        "face": {"color": AMBER},
        "gaze": "scan",
        "blink": 0,
        "speed": 0.8,
    },
}
