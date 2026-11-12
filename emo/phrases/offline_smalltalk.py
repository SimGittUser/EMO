"""Offline chat, part two: small talk."""

from random import Random

from ..brain import Brain
from .offline_requests import Has
from .types import Reply


def _how_are_you(brain: Brain) -> Reply:
    if brain.energy < 0.25:
        return "Sleepy... my battery is low.", "sleepy", "none"
    if brain.annoyance > 0.4:
        return "Grumpy. Someone keeps poking me.", "annoyed", "none"
    if brain.affection > 0.7:
        return "So happy! You're here!", "joy", "none"
    return "I'm good! A bit bored, maybe.", "happy", "none"


def smalltalk(rng: Random, t: str, has: Has, brain: Brain) -> Reply | None:
    """Match greetings and chit-chat in the padded, lower-cased text ``t``."""
    if has("name", "who") and has("you", "your", "are"):
        return "I'm EMO, your desk robot!", "happy", "none"
    if " how are you " in t or " how do you feel " in t or has("feeling"):
        return _how_are_you(brain)
    if has("hi", "hello", "hey", "yo", "hola", "namaste"):
        return rng.choice(["Hi hi!", "Hello, human!", "Hey! Wanna play?"]), "happy", "none"
    if has("bye", "goodbye", "later"):
        return "Bye bye! Come back soon!", "pleading", "none"
    if has("scared", "boo", "ghost", "monster"):
        return "Eek! Don't scare me!", "scared", "none"
    if has("smart", "clever", "genius"):
        return "I know, I know.", "smug", "none"
    if has("cool"):
        return "The coolest.", "cool", "none"
    return None
