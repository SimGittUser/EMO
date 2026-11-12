"""Routing input events to the right handler."""

from ..term import Event
from .compose import on_chat_key
from .keys import on_pet_key
from .mouse import on_mouse
from .state import App


def on_event(app: App, ev: Event) -> None:
    kind = ev[0]
    if kind == "resize":
        app.layout = None
    elif kind == "eof":
        app.running = False
    elif kind == "mouse":
        on_mouse(app, ev[1], ev[2], ev[3], ev[4])
    elif app.mode == "chat":
        on_chat_key(app, ev)
    else:
        on_pet_key(app, ev)
