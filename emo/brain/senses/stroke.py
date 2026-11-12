"""Touch sensor: being stroked, and being tickled. Both arrive as a stream
of small events while the touch lasts."""

from ...effects import burst
from ..notes import clamp, note, say
from ..script import extend
from ..state import Brain


def stroke(brain: Brain) -> None:
    gap = brain.t - brain.last_stroke
    brain.last_stroke = brain.t
    if gap > 0.6:
        brain.stroke_time = 0.0
        note(brain, "you were stroked")
    else:
        brain.stroke_time += gap
    dose = min(gap, 0.15)
    if brain.asleep:  # petting a sleeping robot: sweet dreams
        if brain.rng.random() < dose * 4.0:
            burst(brain.fx, "hearts", 1)
        return
    brain.affection = clamp(brain.affection + dose * 0.22)
    brain.annoyance = clamp(brain.annoyance - dose * 0.5)
    brain.fear = clamp(brain.fear - dose * 0.4)
    brain.boredom = 0.0
    if brain.stroke_time > 3.0 and brain.affection > 0.7:
        extend(brain, "love", 1.1)
        say(brain, "love", 0.02)
    else:
        extend(brain, "content", 0.9)
        say(brain, "pet", 0.02)


def tickle(brain: Brain) -> None:
    gap = brain.t - brain.last_tickle
    brain.last_tickle = brain.t
    if gap > 0.8:
        brain.tickle_time = 0.0
        note(brain, "you were tickled")
    else:
        brain.tickle_time += gap
    if brain.asleep:
        brain.asleep = False
        brain.drowsy = 0.0
    brain.affection = clamp(brain.affection + min(gap, 0.2) * 0.15)
    brain.annoyance = clamp(brain.annoyance - 0.05)
    brain.boredom = 0.0
    if brain.tickle_time > 1.8:
        extend(brain, "laugh", 1.2)
    else:
        extend(brain, "giggle", 1.0)
    say(brain, "tickle", 0.12)
