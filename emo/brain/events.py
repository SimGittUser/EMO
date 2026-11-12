"""The brain's front door: feeding in what the sensors noticed."""

from .senses import HANDLERS, poke
from .state import Brain

EVENTS = ("poke", *HANDLERS)


def event(brain: Brain, name: str, eye: int | None = None) -> bool:
    """React to a sensor event. Returns False if the name is unknown.

    ``eye`` only matters for "poke": which eye was hit (0 left, 1 right).
    """
    if name not in EVENTS:
        return False
    brain.pinned = None
    if name == "poke":
        poke(brain, eye)
    else:
        HANDLERS[name](brain)
    return True
