"""Everything EMO's brain remembers: moods, the situation, the running script."""

from collections import deque
from random import Random

from ..effects import Effects
from ..face import Face
from .step import Callback, Step


class Brain:
    def __init__(self, face: Face, fx: Effects, rng: Random | None = None) -> None:
        self.face = face
        self.fx = fx
        self.rng = rng or Random()
        self.t = 0.0
        # moods, all 0..1
        self.energy = 0.85
        self.affection = 0.55
        self.annoyance = 0.0
        self.dizziness = 0.0
        self.fear = 0.0
        self.boredom = 0.0
        self.drowsy = 0.0
        # the situation
        self.held = False
        self.tilt = 0  # -1 left, +1 right
        self.flipped = False
        self.dark = False
        self.music = False
        self.music_until = 0.0
        self.asleep = False
        self.slept = 0.0
        self.nap_len = 30.0
        self.listening = False  # the human is typing to us
        self.thinking = False  # waiting for the AI
        self.pinned: str | None = None  # a face held on screen by the gallery
        self.pinned_until = 0.0
        # the running script
        self.script: deque[Step] = deque()
        self.step: Step | None = None
        self.step_left = 0.0
        self.priority = 0
        self.after: Callback | None = None
        self.current = "neutral"
        # bookkeeping
        self.stamps: dict[str, list[float]] = {}
        self.last_stroke = -99.0
        self.stroke_time = 0.0
        self.last_tickle = -99.0
        self.tickle_time = 0.0
        self.idle_next = 6.0
        self.outbox: list[str] = []  # phrase keys for the app to speak
        self.last_say = -99.0
        self.recent: deque[tuple[float, str]] = deque(maxlen=6)
