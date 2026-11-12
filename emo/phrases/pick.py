"""Looking phrases up."""

from random import Random

from .moods import MOODS
from .motion import MOTION
from .touch import TOUCH
from .types import Lines
from .world import WORLD

LINES: Lines = {**WORLD, **TOUCH, **MOTION, **MOODS}

# Moments worth spending an AI request on (everything else uses LINES).
AI_WORTHY = {
    "love", "forgive", "poke3", "poke4", "pickup_happy", "pickup_scared",
    "sick", "flip", "ouch", "loud", "music_on", "dark", "wake", "wake_rude",
    "lonely", "hungry", "charged", "hello",
}


def line(rng: Random, key: str) -> str:
    """Something for EMO to say about ``key`` without the AI."""
    return rng.choice(LINES[key][1])


def describe(key: str) -> str:
    """What ``key`` means, in words the AI can react to."""
    return LINES[key][0]
