"""Putting a face on screen."""

from ..effects import set_effects
from ..expressions import EXPRESSIONS
from ..face import set_expression
from .state import Brain


def show(brain: Brain, name: str) -> None:
    """Put a face (and its overlay effects) on screen."""
    if name != brain.current:
        brain.current = name
        set_expression(brain.face, name)
        set_effects(brain.fx, EXPRESSIONS[name].get("fx", ()))
