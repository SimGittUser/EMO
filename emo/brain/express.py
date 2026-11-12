"""Acting out a reply: the face that goes with the words."""

from ..effects import burst
from ..expressions import EXPRESSIONS
from .notes import clamp
from .script import play
from .sleep import fall_asleep
from .state import Brain
from .step import Step

WARM = ("happy", "joy", "love", "laugh", "amazed", "wink", "shy")


def _nudge_moods(brain: Brain, emotion: str) -> None:
    if emotion in WARM:
        brain.affection = clamp(brain.affection + 0.04)
        brain.annoyance = clamp(brain.annoyance - 0.1)
    elif emotion in ("angry", "annoyed"):
        brain.annoyance = clamp(brain.annoyance + 0.12)
    elif emotion in ("sad", "cry"):
        brain.affection = clamp(brain.affection - 0.03)
    elif emotion == "scared":
        brain.fear = clamp(brain.fear + 0.15)
    brain.boredom = 0.0


def express(brain: Brain, emotion: str, seconds: float, action: str = "none") -> None:
    """Show the face chosen for a reply, and act on any request with it."""
    if emotion not in EXPRESSIONS:
        emotion = "neutral"
    _nudge_moods(brain, emotion)
    if emotion == "love":
        burst(brain.fx, "hearts", 5)
    steps = [Step(emotion, seconds)]
    if action == "wink":
        steps = [Step("wink", 1.0), *steps]
    elif action == "wake" and brain.asleep:
        brain.asleep = False
    elif action == "dance":
        brain.asleep = False
        brain.music = True
        brain.music_until = brain.t + seconds + 7.0
    if play(brain, steps, prio=2) and action == "sleep":
        brain.after = lambda: fall_asleep(brain)
