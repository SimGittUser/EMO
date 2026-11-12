"""Little things that float around the face: hearts, tears, Zzz, sweat ...

All positions are on the same virtual 128 x 64 screen as the face. Sprites
are tiny pixel-art bitmaps, so they port straight to any display.
"""

from .burst import burst
from .draw import draw
from .state import Effects, set_effects
from .update import update

__all__ = ["Effects", "burst", "draw", "set_effects", "update"]
