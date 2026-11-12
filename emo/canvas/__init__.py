"""A small RGB framebuffer and the drawing operations that work on it.

Everything EMO shows is drawn here first, as plain pixels, and only then
handed to a display backend (the terminal today, an OLED/TFT later).
"""

from .blit import blit
from .canvas import Canvas
from .glitch import glitch
from .png import to_png
from .rect import fill_rect
from .sdf_fill import fill_sdf

__all__ = ["Canvas", "blit", "fill_rect", "fill_sdf", "glitch", "to_png"]
