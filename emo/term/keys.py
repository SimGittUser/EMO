"""Decoding what the terminal sends for special keys and the mouse."""

from typing import Any

# One thing the user did: ('char', c), ('key', name), ('resize',), ('eof',) or
# ('mouse', kind, col, row, button) with kind press/release/move/drag/wheel.
type Event = tuple[Any, ...]

CSI_KEYS = {
    "A": "up",
    "B": "down",
    "C": "right",
    "D": "left",
    "H": "home",
    "F": "end",
    "Z": "backtab",
}
CTRL_KEYS = {
    "\r": "enter",
    "\n": "enter",
    "\x7f": "backspace",
    "\x08": "backspace",
    "\t": "tab",
    "\x04": "ctrl-d",
    "\x15": "ctrl-u",
    "\x17": "ctrl-w",
}


def _mouse(body: str, final: str) -> Event | None:
    try:
        b, x, y = (int(v) for v in body[1:].split(";")[:3])
    except ValueError:
        return None
    if b & 64:
        return ("mouse", "wheel", x, y, "down" if b & 1 else "up")
    if b & 32:
        return ("mouse", "move" if b & 3 == 3 else "drag", x, y, b & 3)
    return ("mouse", "press" if final == "M" else "release", x, y, b & 3)


def csi(body: str, final: str) -> Event | None:
    """Decode one escape sequence: ESC [ body final."""
    if body.startswith("<") and final in "Mm":
        return _mouse(body, final)
    if final in CSI_KEYS and (not body or body.startswith("1;")):
        return ("key", CSI_KEYS[final])
    if final == "~" and body == "3":
        return ("key", "delete")
    return None
