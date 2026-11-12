"""Everything the running app remembers."""

from collections.abc import Callable
from random import Random
from typing import Protocol

from ..brain import Brain
from ..canvas import Canvas
from ..effects import Effects
from ..face import Face
from ..gemini import Gemini
from ..term import Pixels, detect_color
from .options import Options
from .screen import Layout


class Screen(Protocol):
    """What the app needs from the thing it draws on."""

    def size(self) -> tuple[int, int]: ...
    def write(self, s: str) -> None: ...


class App:
    def __init__(self, opts: Options, term: Screen, ai: Gemini | None = None) -> None:
        self.o = opts
        self.term = term
        self.ai = ai
        self.rng = Random(opts.seed)
        self.face = Face(self.rng)
        self.fx = Effects(self.rng)
        self.brain = Brain(self.face, self.fx, self.rng)
        self.canvas = Canvas(96, 48)
        self.color = detect_color() if opts.color == "auto" else opts.color
        self.pixels = Pixels(self.color)
        self.face.glow = self.color == "truecolor" and not opts.no_glow
        self.ai_rest_until = 0.0  # leave the AI alone until then, after an error
        self.last_react = -99.0
        self.chat_tag = 0
        self.mode = "pet"  # 'pet' = keys are sensors, 'chat' = typing
        self.typed = ""
        self.you = ""  # what the human last said, and until when to show it
        self.you_until = 0.0
        self.speech = ""  # what EMO is saying, when it started and ends
        self.speech_at = 0.0
        self.speech_until = 0.0
        self.history: list[tuple[str, str]] = []
        self.show_help: bool | None = None  # None = decide from the window size
        self.gallery_i = -1
        self.demo_next = 0.0
        self.later: list[tuple[float, Callable[[], None]]] = []
        self.press: list[int] | None = None  # mouse button down: col, row, dragged
        self.layout: Layout | None = None
        self.prev: dict[int, str] = {}  # what each screen row last showed
        self.now = 0.0
        self.running = True
