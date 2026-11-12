"""The terminal as a display and as a set of fake sensors.

Display: every character cell shows two stacked pixels using the half-block
character, so an 80 x 20 patch of terminal is an 80 x 40 pixel screen.
Input: raw key presses and mouse reports, decoded into simple events.

This package is the only part of EMO that knows it is running in a
terminal; an OLED build replaces it with a display driver and real sensors.
"""

from .color import detect_color
from .keys import Event
from .parse import parse
from .pixels import Pixels
from .rows import pixel_row
from .session import session
from .styled import Part, styled
from .terminal import Terminal
from .text import clip, text_width, wrap

__all__ = [
    "Event",
    "Part",
    "Pixels",
    "Terminal",
    "clip",
    "detect_color",
    "parse",
    "pixel_row",
    "session",
    "styled",
    "text_width",
    "wrap",
]
