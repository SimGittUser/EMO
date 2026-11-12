"""Motion sensor: free fall, then the floor."""

from ...effects import burst
from ...face import kick
from ..notes import clamp, note, say
from ..script import play
from ..state import Brain
from ..step import Step


def drop(brain: Brain) -> None:
    note(brain, "you were dropped on the floor")
    brain.asleep = False
    brain.held = False
    brain.tilt = 0
    brain.flipped = False
    brain.boredom = 0.0
    brain.fear = clamp(brain.fear + 0.6)
    brain.affection = clamp(brain.affection - 0.2)

    def impact() -> None:
        kick(brain.face, brain.rng.uniform(-80, 80), 260)
        brain.face.glitch = 1.0
        burst(brain.fx, "stars", 7)

    def aftermath() -> None:
        sorrow = "cry" if brain.affection < 0.4 else "sad"
        play(brain, [Step("dizzy", 1.6), Step(sorrow, 2.4)])
        say(brain, "ouch")

    # nothing interrupts the fall and the knock-out; the sulking afterwards can be
    play(brain, [Step("falling", 0.8), Step("ko", 2.6, impact)], prio=3)
    brain.after = aftermath
    say(brain, "drop")
