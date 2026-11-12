"""EMO's personality: moods, reactions to the senses, and idle behaviour.

The brain knows nothing about terminals or sensors. It is fed *events*
("pat", "shake", "light" ...) and decides which face to show.

Two layers decide the face:
  * a *script* - a short scripted reaction, e.g. startled -> dizzy -> sick
  * the *baseline* - what the mood and situation call for when no script runs
"""

from .baseline import baseline
from .chat import chat_started, pin, set_thinking
from .describe import describe
from .events import EVENTS, event
from .express import express
from .script import play
from .state import Brain
from .step import Step
from .tick import update

__all__ = [
    "EVENTS",
    "Brain",
    "Step",
    "baseline",
    "chat_started",
    "describe",
    "event",
    "express",
    "pin",
    "play",
    "set_thinking",
    "update",
]
