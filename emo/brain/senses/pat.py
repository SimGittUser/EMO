"""Touch sensor: a pat on the head."""

from ...effects import burst
from ...face import kick
from ..notes import clamp, count, note, say
from ..script import play
from ..sleep import wake
from ..state import Brain
from ..step import Step


def pat(brain: Brain) -> None:
    note(brain, "your head was patted")
    if brain.asleep:
        wake(brain, "gentle")
        return
    was_cross = brain.annoyance > 0.55
    brain.affection = clamp(brain.affection + 0.07)
    brain.annoyance = clamp(brain.annoyance - 0.15)
    brain.fear = clamp(brain.fear - 0.15)
    brain.boredom = 0.0
    n = count(brain, "pat", 2.5)
    kick(brain.face, 0, 45)
    if was_cross:
        brain.annoyance = min(brain.annoyance, 0.2)
        play(brain, [Step("suspicious", 0.9), Step("happy", 1.2)])
        say(brain, "forgive", 0.8)
    elif n >= 4 and brain.affection > 0.6:
        play(brain, [Step("love", 2.6)])
        burst(brain.fx, "hearts", 6)
        say(brain, "love", 0.8)
    elif n >= 2:
        play(brain, [Step("content", 1.8)])
        say(brain, "pat", 0.3)
    else:
        play(brain, [Step("happy", 1.4)])
        say(brain, "pat", 0.35)
