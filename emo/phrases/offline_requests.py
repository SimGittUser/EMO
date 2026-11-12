"""Offline chat, part one: things the human asks EMO to do or feel."""

from collections.abc import Callable
from random import Random

from ..brain import Brain
from .types import Reply

JOKES = [
    "Why did the robot go on holiday? To recharge its batteries!",
    "What do you call a pirate robot? Arrr-2-D2!",
    "Why was the robot angry? Someone kept pushing its buttons!",
    "I would tell you a UDP joke, but you might not get it.",
]

type Has = Callable[..., bool]


def requests(rng: Random, t: str, has: Has, brain: Brain) -> Reply | None:
    """Match requests and feelings in the padded, lower-cased text ``t``."""
    if has("joke", "funny"):
        return rng.choice(JOKES), "laugh", "none"
    if has("dance", "sing", "music", "party"):
        return "Watch my moves!", "joy", "dance"
    if has("sleep", "goodnight", "nap", "bedtime") or " good night " in t:
        return "Okay... goodnight!", "sleepy", "sleep"
    if has("wink"):
        return "Like this?", "happy", "wink"
    if has("love", "cute", "adorable", "sweet", "best") or " good robot " in t or " good boy " in t:
        return rng.choice(["Aww! I love you too!", "You're making me blush!"]), "love", "none"
    if has("stupid", "dumb", "hate", "ugly", "bad", "useless", "idiot"):
        if brain.affection > 0.5:
            return "That's not nice...", "sad", "none"
        return "Hey! Take that back!", "angry", "none"
    if has("sorry", "apologies", "apologize"):
        return "It's okay. I forgive you.", "happy", "none"
    if has("thanks", "thank", "thx"):
        return "You're welcome!", "happy", "none"
    return None
