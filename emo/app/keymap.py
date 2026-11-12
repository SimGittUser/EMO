"""Keyboard stand-ins for the real sensors, and the on-screen key list."""

KEYS = {
    "p": "pat",
    " ": "pat",
    "s": "stroke",
    "o": "poke",
    "t": "tickle",
    "u": "pickup",
    "k": "shake",
    "f": "flip",
    "d": "drop",
    "l": "loud",
    "c": "clap",
    "m": "music",
    "n": "light",
    "b": "charge",
    "z": "sleep",
}
ARROWS = {"left": "tilt_left", "right": "tilt_right", "up": "level", "down": "level"}

# group name, then (key, what it does)
HELP = [
    ("touch", [("p", "pat"), ("s", "stroke (hold)"), ("o", "poke"), ("t", "tickle (hold)")]),
    (
        "motion",
        [
            ("u", "pick up / put down"),
            ("k", "shake"),
            ("← →", "tilt"),
            ("↓", "level"),
            ("f", "flip over"),
            ("d", "drop"),
        ],
    ),
    ("sound", [("l", "loud bang"), ("c", "clap (twice = dance)"), ("m", "music")]),
    ("light", [("n", "lights off / on")]),
    ("power", [("b", "charge"), ("z", "sleep / wake")]),
    (
        "mouse",
        [
            ("move", "look"),
            ("click", "pat"),
            ("click eye", "poke"),
            ("drag", "stroke"),
            ("wheel", "tickle"),
        ],
    ),
    ("other", [("Enter", "talk"), ("[ ]", "browse faces"), ("h", "hide keys"), ("q", "quit")]),
]
