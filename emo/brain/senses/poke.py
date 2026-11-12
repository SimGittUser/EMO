"""Touch sensor: a poke. Patience runs out a little more each time."""

from ...face import kick, look_at, wink
from ..notes import clamp, note, say
from ..script import play
from ..sleep import wake
from ..state import Brain
from ..step import Step


def poke(brain: Brain, eye: int | None = None) -> None:
    """React to a poke; ``eye`` is the eye that was hit (0 left, 1 right)."""
    note(brain, "you were poked")
    if brain.asleep:
        wake(brain, "startled")
        return
    brain.annoyance = clamp(brain.annoyance + 0.22)
    brain.affection = clamp(brain.affection - 0.03)
    brain.boredom = 0.0
    if eye is None:
        eye = brain.rng.randrange(2)
    wink(brain.face, eye, 0.5)
    kick(brain.face, 70 if eye == 0 else -70, 0)
    look_at(brain.face, -0.8 if eye == 0 else 0.8, 0, 0.8)
    a = brain.annoyance
    if a < 0.3:
        play(brain, [Step("surprised", 0.7)])
        say(brain, "poke1", 0.35)
    elif a < 0.55:
        play(brain, [Step("annoyed", 1.6)])
        say(brain, "poke2", 0.5)
    elif a < 0.85:
        play(brain, [Step("angry", 2.2)])
        say(brain, "poke3", 0.8)
    else:
        play(brain, [Step("furious", 2.8)])
        say(brain, "poke4")
