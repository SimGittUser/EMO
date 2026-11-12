"""Driving the whole app frame by frame against a fake terminal."""

import hashlib
from typing import Any

from emo.app import App, Options, draw, on_event, tick
from emo.brain import Step, play
from emo.brain.notes import say

from .helpers import FakeTerm

FRAMES = 30 * 24


def drive(color: str, cols: int, rows: int, events: dict[str, Any]) -> dict[str, Any]:
    """Run 24 seconds of EMO, feeding ``events`` (frame number -> events)."""
    term = FakeTerm(cols, rows)
    app = App(Options(seed=5, color=color), term)
    app.now = 100.0
    play(app.brain, [Step("sleepy", 0.8), Step("happy", 1.6)])
    say(app.brain, "hello")
    h = hashlib.sha256()
    texts = []
    for i in range(FRAMES):
        for ev in events.get(str(i), ()):
            on_event(app, tuple(ev))
        app.now += 1 / 30
        tick(app, 1 / 30)
        draw(app)
        h.update("".join(term.out).encode())
        term.out.clear()
        if i % 90 == 89:
            status = app.prev.get(1, "")[:60]
            texts.append([app.brain.current, app.speech, app.you, app.mode, status])
    return {"out": h.hexdigest(), "texts": texts}
