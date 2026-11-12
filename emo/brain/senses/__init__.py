"""Reactions to what the sensors notice, one module per kind of sensing.

On real hardware these same events will come from a touch pad, an IMU, a
microphone and a light sensor instead of the keyboard.
"""

from collections.abc import Callable

from ..state import Brain
from .carry import pickup, shake
from .drop import drop
from .pat import pat
from .poke import poke
from .room import charge, light, sleep
from .sound import clap, loud, music
from .stroke import stroke, tickle
from .tip import flip, level, tilt_left, tilt_right

# Every event the brain understands, except "poke" (which also says where).
HANDLERS: dict[str, Callable[[Brain], None]] = {
    "pat": pat,
    "stroke": stroke,
    "tickle": tickle,
    "pickup": pickup,
    "shake": shake,
    "tilt_left": tilt_left,
    "tilt_right": tilt_right,
    "level": level,
    "flip": flip,
    "drop": drop,
    "loud": loud,
    "clap": clap,
    "music": music,
    "light": light,
    "charge": charge,
    "sleep": sleep,
}

__all__ = ["HANDLERS", "poke"]
