"""Microphone: bangs, claps and music."""

from ...face import kick, pop
from ..notes import clamp, count, note, say
from ..script import play
from ..sleep import wake
from ..state import Brain
from ..step import Step


def loud(brain: Brain) -> None:
    note(brain, "there was a loud bang")
    brain.fear = clamp(brain.fear + 0.35)
    brain.boredom = min(brain.boredom, 0.3)
    if brain.asleep:
        wake(brain, "startled")
        return
    kick(brain.face, 0, -90)
    pop(brain.face, 2.5)
    follow = Step("scared", 1.4) if brain.fear > 0.55 else Step("suspicious", 1.8)
    play(brain, [Step("startled", 0.7), follow])
    say(brain, "loud", 0.7)


def clap(brain: Brain) -> None:
    note(brain, "someone clapped")
    if brain.asleep:
        wake(brain, "gentle")
        return
    brain.boredom = min(brain.boredom, 0.2)
    if count(brain, "clap", 1.5) >= 2:  # clap-clap means "dance!"
        brain.music = True
        brain.music_until = brain.t + 7.0
        play(brain, [Step("joy", 0.9)])
        say(brain, "music_on", 0.6)
    else:
        pop(brain.face, 1.5)
        play(brain, [Step("surprised", 0.5), Step("happy", 1.2)])
        say(brain, "clap", 0.4)


def music(brain: Brain) -> None:
    """Toggle: music starts or stops."""
    brain.boredom = 0.0
    if brain.music:
        brain.music = False
        brain.music_until = 0.0
        note(brain, "the music stopped")
        play(brain, [Step("pleading", 1.5)])
        say(brain, "music_off", 0.7)
        return
    note(brain, "music started playing")
    if brain.asleep:
        brain.asleep = False
    brain.music = True
    brain.music_until = 0.0
    play(brain, [Step("surprised", 0.4), Step("joy", 0.9)])
    say(brain, "music_on", 0.7)
