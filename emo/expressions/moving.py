"""Faces that go with movement: dancing, and sliding when tipped."""

from typing import Any

MOVING: dict[str, dict[str, Any]] = {
    "dance": {
        "eyes": {"bot": 0.45, "bot_curve": 0.9, "w": 26, "y": -1},
        "anim": {"bounce": (2.6, 2.0), "sway": (0.08, 1.0)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["notes"],
        "rainbow": True,
    },
    "tilt_left": {
        "left": {"w": 21, "h": 32},
        "right": {"w": 25, "h": 29},
        "face": {"fx": -15, "tilt": -0.2},
        "gaze": "fixed",
        "look": (-0.7, 0.3),
        "blink": 3.5,
    },
    "tilt_right": {
        "left": {"w": 25, "h": 29},
        "right": {"w": 21, "h": 32},
        "face": {"fx": 15, "tilt": 0.2},
        "gaze": "fixed",
        "look": (0.7, 0.3),
        "blink": 3.5,
    },
}
