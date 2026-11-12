"""EMO speaking: words on screen, and remarks about what just happened."""

from .. import gemini, phrases
from ..brain import describe
from .state import App

CPS = 38.0  # how fast EMO's words appear, characters per second


def speak(app: App, text: str) -> None:
    """Start showing ``text`` letter by letter, then leave it up for a while."""
    app.speech = text
    app.speech_at = app.now
    app.speech_until = app.now + len(text) / CPS + 4.0 + 0.06 * len(text)


def ai_usable(app: App) -> bool:
    return app.ai is not None and app.ai.problem != "key" and app.now >= app.ai_rest_until


def voice(app: App, key: str) -> None:
    """EMO wants to say something about what just happened.

    The bigger moments go to the AI (not too often); the rest, and anything
    the AI is too busy for, use a ready-made line.
    """
    ai = app.ai
    rested = app.now - app.last_react > app.o.react_gap
    worth_asking = key in phrases.AI_WORTHY and rested
    if ai is not None and ai_usable(app) and worth_asking and not ai.busy:
        asked = gemini.react(ai, (key, app.now), describe(app.brain), phrases.describe(key))
        if asked:
            app.last_react = app.now
            return
    speak(app, phrases.line(app.rng, key))
