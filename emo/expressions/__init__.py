"""EMO's faces, as data.

The face is designed on a virtual 128 x 64 screen and scaled to whatever the
real display is. An expression only lists what differs from the resting face:

  eyes   settings for both eyes          left / right   per-eye overrides
  face   whole-face settings (colour, tilt, blush ...)
  shape  swap the eye for a special shape: heart, cross, chevron, spiral
  anim   continuous motion, each given as (amount, speed in Hz)
  gaze   how the eyes wander            look   where 'fixed' gaze points
  blink  average seconds between blinks (0 = never)
  fx     overlay effects (see emo.effects)
  speed  how fast the face moves into this expression

Eyelids: ``top`` / ``bot`` close the eye from above / below (0..1).
``*_slant`` tips the lid and ``*_curve`` bends it into an arc.
"""

from typing import Any

from .calm import CALM
from .cross import CROSS
from .defaults import ANIMS, EYE_DEFAULTS, FACE_DEFAULTS
from .gallery import AI_EMOTIONS, GALLERY
from .happy import HAPPY
from .knocked import KNOCKED
from .laughing import LAUGHING
from .moving import MOVING
from .playful import PLAYFUL
from .scared import SCARED
from .tired import TIRED
from .upset import UPSET

EXPRESSIONS: dict[str, dict[str, Any]] = {
    **CALM,
    **HAPPY,
    **LAUGHING,
    **PLAYFUL,
    **MOVING,
    **SCARED,
    **UPSET,
    **CROSS,
    **TIRED,
    **KNOCKED,
}

__all__ = ["AI_EMOTIONS", "ANIMS", "EXPRESSIONS", "EYE_DEFAULTS", "FACE_DEFAULTS", "GALLERY"]
