"""The terminal app: wires the face, brain, effects and AI to screen and keyboard."""

from .draw import draw
from .events import on_event
from .loop import run
from .options import Options
from .state import App
from .tick import tick

__all__ = ["App", "Options", "draw", "on_event", "run", "tick"]
