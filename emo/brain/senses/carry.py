"""Motion sensor: being picked up, put down, and shaken."""

from ...face import kick, look_at
from ..notes import clamp, note, say
from ..script import play
from ..state import Brain
from ..step import Step


def pickup(brain: Brain) -> None:
    """Toggle: lifts EMO into the air, or puts it back down."""
    if brain.held:
        brain.held = False
        note(brain, "you were put down")
        kick(brain.face, 0, 60)
        play(brain, [Step("relieved", 1.3)])
        say(brain, "putdown", 0.5)
        return
    note(brain, "you were picked up")
    if brain.asleep:
        brain.asleep = False
    brain.held = True
    brain.boredom = 0.0
    kick(brain.face, 0, 110)
    look_at(brain.face, 0, 0.9, 1.5)
    if brain.affection >= 0.45:
        play(brain, [Step("startled", 0.5), Step("joy", 1.8)])
        say(brain, "pickup_happy", 0.7)
    else:
        brain.fear = clamp(brain.fear + 0.3)
        play(brain, [Step("startled", 0.5), Step("scared", 1.7)])
        say(brain, "pickup_scared", 0.8)


def shake(brain: Brain) -> None:
    note(brain, "you were shaken")
    was_asleep = brain.asleep
    brain.asleep = False
    brain.dizziness = clamp(brain.dizziness + 0.3)
    brain.annoyance = clamp(brain.annoyance + (0.25 if was_asleep else 0.04))
    brain.boredom = 0.0
    kick(brain.face, brain.rng.choice((-1, 1)) * 160, brain.rng.uniform(-60, 60))
    if brain.dizziness > 0.95:
        play(brain, [Step("shaken", 0.6), Step("dizzy", 2.4), Step("sick", 3.0)], prio=2)
        say(brain, "sick", 0.9)
    else:
        play(brain, [Step("shaken", 0.6), Step("dizzy", 1.2 + 3.0 * brain.dizziness)], prio=2)
        say(brain, "shake", 0.5)
