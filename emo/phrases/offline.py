"""A tiny keyword brain so chatting works without an API key."""

from random import Random

from ..brain import Brain
from .offline_requests import requests
from .offline_smalltalk import smalltalk
from .types import Reply

NEEDS_AI = "Hmm... I'd need my Gemini brain for that one. Give me an API key!"
FILLERS = ["Tell me more!", "Beep boop?", "Ooh, interesting!", "I'm listening!"]


def offline_reply(rng: Random, text: str, brain: Brain) -> Reply:
    """Answer ``text`` from a handful of keyword rules."""
    t = " " + "".join(c if c.isalnum() else " " for c in text.lower()) + " "

    def has(*words: str) -> bool:
        return any(" " + w + " " in t for w in words)

    reply = requests(rng, t, has, brain) or smalltalk(rng, t, has, brain)
    if reply:
        return reply
    if "?" in text:
        return NEEDS_AI, "thinking", "none"
    return rng.choice(FILLERS), "curious", "none"
