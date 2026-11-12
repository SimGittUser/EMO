"""Hooks for conversation, the AI, and the face gallery."""

from .script import cancel
from .sleep import wake
from .state import Brain


def chat_started(brain: Brain) -> None:
    if brain.asleep:
        wake(brain, "gentle")
    brain.boredom = 0.0
    brain.listening = True


def set_thinking(brain: Brain, on: bool) -> None:
    brain.thinking = on
    if on:
        cancel(brain, 1)


def pin(brain: Brain, name: str, seconds: float = 6.0) -> None:
    """Hold one face on screen (used when browsing the gallery)."""
    cancel(brain, 9)
    brain.asleep = False
    brain.pinned = name
    brain.pinned_until = brain.t + seconds
