"""Sleepy faces, and the power-related ones."""

from typing import Any

from .colors import CHARGE_GREEN, DIM

TIRED: dict[str, dict[str, Any]] = {
    "sleepy": {
        "eyes": {"top": 0.52, "top_slant": -0.08, "bot": 0.06, "y": 3},
        "face": {"color": DIM},
        "anim": {"sway": (0.035, 0.22)},
        "gaze": "fixed",
        "look": (0, 0.3),
        "blink": 2.2,
        "blink_dur": 0.6,
        "speed": 0.45,
    },
    "yawn": {
        "eyes": {"h": 7, "w": 27, "r": 1.0, "y": 1, "rot": -0.16},
        "face": {"color": DIM, "scale": 1.06},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["tear1"],
        "speed": 0.7,
    },
    "sleeping": {
        "eyes": {"h": 9, "w": 26, "r": 1.0, "top": 0.62, "top_curve": 1.0, "y": 7},
        "face": {"color": DIM, "bright": 0.7, "breath": 4.0},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["zzz"],
        "speed": 0.5,
    },
    "relieved": {
        "eyes": {"h": 10, "w": 26, "r": 1.0, "top": 0.6, "top_curve": 1.0, "y": 3},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["puff"],
        "speed": 0.8,
    },
    "dazzled": {
        "eyes": {"top": 0.42, "bot": 0.40, "w": 27},
        "left": {"top": 0.52},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
    },
    "charging": {
        "eyes": {"bot": 0.6, "bot_curve": 1.0, "w": 27, "y": 1},
        "face": {"color": CHARGE_GREEN},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["battery_fill"],
    },
}
