"""Motion sensor: being tipped sideways or turned upside down."""

from ...face import kick
from ..notes import clamp, note, say
from ..script import play
from ..sleep import wake
from ..state import Brain
from ..step import Step


def flip(brain: Brain) -> None:
    """Toggle: turns EMO upside down, or the right way up again."""
    brain.boredom = 0.0
    if brain.flipped:
        brain.flipped = False
        note(brain, "you were turned the right way up")
        brain.dizziness = clamp(brain.dizziness + 0.2)
        play(brain, [Step("dizzy", 1.6), Step("relieved", 1.2)], prio=2)
        say(brain, "flip_back", 0.7)
        return
    note(brain, "you were turned upside down")
    brain.asleep = False
    brain.flipped = True
    brain.fear = clamp(brain.fear + 0.3)
    kick(brain.face, 0, -120)
    play(brain, [Step("startled", 0.55)], prio=2)
    say(brain, "flip", 0.9)


def level(brain: Brain) -> None:
    if brain.tilt or brain.flipped:
        note(brain, "you were set level again")
    if brain.flipped:
        flip(brain)
    brain.tilt = 0


def _tilt(brain: Brain, way: int) -> None:
    if brain.tilt == way:
        level(brain)
        return
    note(brain, "you were tipped to the %s" % ("left" if way < 0 else "right"))
    if brain.asleep:
        wake(brain, "startled")
    brain.tilt = way
    brain.boredom = 0.0
    kick(brain.face, way * 90, 0)
    play(brain, [Step("surprised", 0.45)])
    say(brain, "tilt", 0.45)


def tilt_left(brain: Brain) -> None:
    _tilt(brain, -1)


def tilt_right(brain: Brain) -> None:
    _tilt(brain, 1)
