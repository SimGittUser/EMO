"""Light sensor and power: lights, charging, and being sent to sleep."""

from ..notes import note, say
from ..script import play
from ..sleep import fall_asleep, wake
from ..state import Brain
from ..step import Step


def light(brain: Brain) -> None:
    """Toggle: the lights go out or come back on."""
    brain.dark = not brain.dark
    if brain.dark:
        note(brain, "the lights went out")
        if not brain.asleep:
            uneasy = "nervous" if brain.fear > 0.3 else "sleepy"
            play(brain, [Step("surprised", 0.6), Step(uneasy, 1.5)])
            say(brain, "dark", 0.7)
        return
    note(brain, "the lights came on")
    if brain.asleep:
        wake(brain, "light")
    else:
        brain.drowsy = 0.0
        play(brain, [Step("dazzled", 1.2)])
        say(brain, "light", 0.6)


def charge(brain: Brain) -> None:
    note(brain, "you were plugged in to charge")
    brain.asleep = False
    brain.energy = 1.0
    brain.drowsy = 0.0
    play(brain, [Step("charging", 2.2), Step("joy", 1.4)], prio=2)
    say(brain, "charged", 0.8)


def sleep(brain: Brain) -> None:
    """Toggle: sends EMO to sleep, or wakes it."""
    if brain.asleep:
        wake(brain, "gentle")
    else:
        fall_asleep(brain)
