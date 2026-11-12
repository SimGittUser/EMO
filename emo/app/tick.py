"""Advancing the whole robot by one frame."""

from .. import brain, effects, face, gemini
from .chat import on_ai
from .keys import browse
from .state import App
from .talk import CPS, voice


def _run_due(app: App) -> None:
    """Run the things that were scheduled for about now."""
    if not app.later:
        return
    due = [fn for when, fn in app.later if when <= app.now]
    app.later = [(when, fn) for when, fn in app.later if when > app.now]
    for fn in due:
        fn()


def tick(app: App, dt: float) -> None:
    now = app.now
    _run_due(app)
    if app.ai:
        for res in gemini.poll(app.ai):
            on_ai(app, res)
    if app.o.demo and now >= app.demo_next:
        app.demo_next = now + 2.8
        browse(app, 1, hold=3.2)
    brain.update(app.brain, dt)
    if app.brain.outbox:
        for key in app.brain.outbox:
            voice(app, key)
        app.brain.outbox.clear()
    if app.speech and now > app.speech_until:
        app.speech = ""
    app.face.talking = bool(app.speech) and (now - app.speech_at) * CPS < len(app.speech)
    face.update(app.face, dt)
    effects.update(app.fx, dt, app.face)
