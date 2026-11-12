"""Faces for being shaken, dropped and tipped over."""

from typing import Any

from .colors import FLUSHED, GREEN, GREY, VIOLET

KNOCKED: dict[str, dict[str, Any]] = {
    "shaken": {
        "shape": "chevron",
        "eyes": {"w": 25, "h": 25},
        "anim": {"shake": (4.5, 9.0)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "speed": 2.2,
    },
    "dizzy": {
        "shape": "spiral",
        "eyes": {"w": 28, "h": 28},
        "face": {"color": VIOLET},
        "anim": {"sway": (0.09, 0.6), "wobble": (0.06, 1.3)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["stars"],
    },
    "sick": {
        "eyes": {"top": 0.42, "top_slant": -0.18, "bot": 0.18, "h": 27, "y": 2},
        "face": {"color": GREEN},
        "anim": {"sway": (0.06, 0.4), "wobble": (0.05, 0.8)},
        "gaze": "fixed",
        "look": (0, 0.3),
        "blink": 3.0,
        "fx": ["sweat"],
        "speed": 0.6,
    },
    "ko": {
        "shape": "cross",
        "eyes": {"w": 24, "h": 24},
        "face": {"color": GREY},
        "anim": {"sway": (0.04, 0.5)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["stars"],
        "speed": 2.0,
    },
    "upside_down": {
        "eyes": {"w": 21, "h": 25, "r": 1.0, "top": 0.10, "top_slant": -0.3, "y": -7},
        "face": {"color": FLUSHED},
        "anim": {"shake": (0.7, 10.0), "sway": (0.05, 0.9)},
        "gaze": "dart",
        "blink": 0,
        "fx": ["sweat_up"],
    },
}
