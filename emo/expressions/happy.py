"""Happy faces. A curved bottom lid is what turns a block into a smiling eye."""

from typing import Any

from .colors import BRIGHT, PINK

HAPPY: dict[str, dict[str, Any]] = {
    "happy": {
        "eyes": {"bot": 0.42, "bot_curve": 0.85, "w": 26, "y": -1.5},
        "anim": {"bounce": (1.2, 1.6)},
        "gaze": "wander",
        "blink": 4.5,
    },
    "joy": {
        "eyes": {"bot": 0.5, "bot_curve": 1.0, "w": 28, "h": 32, "y": -3},
        "face": {"color": BRIGHT},
        "anim": {"bounce": (2.6, 2.6)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["sparkles"],
        "speed": 1.3,
    },
    "content": {
        "eyes": {"bot": 0.68, "bot_curve": 1.0, "w": 28, "y": -1},
        "face": {"blush": 0.55},
        "anim": {"sway": (0.03, 0.5)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["hearts_few"],
    },
    "love": {
        "shape": "heart",
        "eyes": {"w": 30, "h": 30},
        "face": {"color": PINK, "blush": 0.6},
        "anim": {"pulse": (0.11, 1.3)},
        "gaze": "fixed",
        "look": (0, 0),
        "blink": 0,
        "fx": ["hearts"],
    },
}
