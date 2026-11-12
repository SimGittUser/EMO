"""Keyboard input, in both modes."""

from .. import brain
from ..expressions import GALLERY
from ..term import Event
from .keymap import ARROWS, KEYS
from .state import App


def browse(app: App, step: int, hold: float = 8.0) -> None:
    """Show the next (or previous) face in the gallery for a while."""
    app.gallery_i = (app.gallery_i + step) % len(GALLERY)
    brain.pin(app.brain, GALLERY[app.gallery_i], hold)


def on_pet_key(app: App, ev: Event) -> None:
    """Keys act as sensors."""
    app.o.demo = False
    if ev[0] == "key":
        name = ev[1]
        if name in ("enter", "tab"):
            app.mode = "chat"
            brain.chat_started(app.brain)
        elif name in ARROWS:
            brain.event(app.brain, ARROWS[name])
        elif name == "ctrl-d":
            app.running = False
        return
    c = ev[1].lower()
    if c == "q":
        app.running = False
    elif c in ("h", "?"):
        app.show_help = not app.layout.help if app.layout else True
        app.layout = None
    elif c == "]":
        browse(app, 1)
    elif c == "[":
        browse(app, -1)
    elif c in KEYS:
        brain.event(app.brain, KEYS[c])
