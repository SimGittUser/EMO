"""Everything the face remembers from one frame to the next."""

from random import Random
from typing import Any

from ..expressions import ANIMS, EXPRESSIONS, EYE_DEFAULTS, FACE_DEFAULTS
from .springs import Springs
from .tuning import DEFAULT_HZ, EYE_SPRING, FACE_SPRING

# One blink in progress: [seconds elapsed, total seconds, fraction held shut].
type Blink = list[float] | None

# Where an eye was last drawn on the virtual screen: centre x, y, half w, h.
type EyeGeom = tuple[float, float, float, float]


class Face:
    """A neutral face. The functions in this package animate and draw it."""

    def __init__(self, rng: Random | None = None) -> None:
        self.rng = rng or Random()
        self.t = 0.0
        self.eyes = [Springs(EYE_DEFAULTS, EYE_SPRING), Springs(EYE_DEFAULTS, EYE_SPRING)]
        self.f = Springs(FACE_DEFAULTS, FACE_SPRING)
        self.name = "neutral"
        self.expr: dict[str, Any] = EXPRESSIONS["neutral"]
        self.speed = 1.0
        self.shape: list[str | None] = [None, None]  # special shape showing now
        self.want_shape: list[str | None] = [None, None]
        self.hz = dict(DEFAULT_HZ)
        self.phase = dict.fromkeys(ANIMS, 0.0)
        self.spin = 0.0
        self.gaze_mode = "wander"
        self.gaze_fixed: tuple[float, float] = (0.0, 0.0)
        self.gaze_target: tuple[float, float] = (0.0, 0.0)
        self.gaze_timer = 0.0
        self.attn: tuple[float, float] = (0.0, 0.0)  # a point pulling the gaze
        self.attn_t = 0.0
        self.blink_every = 3.6
        self.blink_dur = 0.26
        self.blink_timer = 2.0
        self.blink_again = 0.0
        self.blinks: list[Blink] = [None, None]
        self.talking = False
        self.talk = 0.0
        self.glitch = 0.0
        self.glow = True
        self.geom: list[EyeGeom] = [(41.0, 32.0, 12.0, 15.0), (87.0, 32.0, 12.0, 15.0)]
        self.view: tuple[float, float, float] = (1.0, 0.0, 0.0)  # scale, x, y offset
