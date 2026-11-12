"""The animated face: turns an expression name into moving, blinking eyes.

Nothing here snaps. Every number that describes the face (eye size, lid
position, colour, tilt ...) sits on a spring that chases its target, so any
expression flows into any other.
"""

from .actions import blink, kick, look_at, pop, wink
from .draw import draw, hit_eye
from .expression import set_expression
from .state import Face
from .tuning import VH, VW
from .update import update

__all__ = [
    "VH",
    "VW",
    "Face",
    "blink",
    "draw",
    "hit_eye",
    "kick",
    "look_at",
    "pop",
    "set_expression",
    "update",
    "wink",
]
