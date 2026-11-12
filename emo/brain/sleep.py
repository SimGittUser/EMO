"""Falling asleep and waking up."""

from ..face import pop
from .notes import clamp, say
from .script import play
from .state import Brain
from .step import Step


def fall_asleep(brain: Brain) -> None:
    if brain.asleep:
        return
    brain.asleep = True
    brain.slept = 0.0
    brain.drowsy = 0.0
    brain.nap_len = brain.rng.uniform(25.0, 50.0)
    brain.music = False
    play(brain, [Step("yawn", 1.3), Step("sleepy", 1.4)], prio=2)
    say(brain, "sleep", 0.5)


def wake(brain: Brain, how: str = "gentle") -> None:
    """Wake up: 'gentle', 'startled', by 'light', or 'natural' (slept enough)."""
    if not brain.asleep:
        return
    brain.asleep = False
    brain.drowsy = 0.0
    brain.boredom = min(brain.boredom, 0.4)
    if how == "startled":
        brain.annoyance = clamp(brain.annoyance + 0.2)
        play(brain, [Step("startled", 0.6), Step("annoyed", 1.6)], prio=2)
        pop(brain.face, 2.0)
        say(brain, "wake_rude")
    elif how == "light":
        play(brain, [Step("dazzled", 1.3), Step("sleepy", 0.9)], prio=2)
        say(brain, "light", 0.7)
    elif how == "natural":
        play(brain, [Step("sleepy", 1.0), Step("yawn", 1.2), Step("happy", 1.2)], prio=2)
        say(brain, "wake", 0.7)
    else:
        play(brain, [Step("sleepy", 0.9), Step("happy", 1.3)], prio=2)
        say(brain, "wake", 0.7)
