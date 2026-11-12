"""The individual things EMO does when left alone."""

from collections.abc import Callable

from ..face import blink, kick, look_at
from .notes import say
from .script import play
from .state import Brain
from .step import Step


def act(brain: Brain, face: str, seconds: float, key: str = "", chance: float = 0.0) -> Callable[[], None]:
    """An option that shows a face and maybe says something."""

    def run() -> None:
        play(brain, [Step(face, seconds)])
        if key:
            say(brain, key, chance)

    return run


def glance(brain: Brain) -> None:
    r = brain.rng
    look_at(brain.face, r.choice((-0.9, 0.9)), r.uniform(-0.3, 0.3), 1.2)


def double_blink(brain: Brain) -> None:
    blink(brain.face)
    brain.face.blink_again = 0.32


def hop(brain: Brain) -> None:
    play(brain, [Step("happy", 1.3)])
    kick(brain.face, 0, -40)
