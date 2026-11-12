"""Keyboard input while the human is typing a message."""

from ..term import Event
from .chat import send_chat
from .state import App

MAX_MESSAGE = 240


def leave_chat(app: App) -> None:
    app.mode = "pet"
    app.typed = ""
    app.brain.listening = False


def on_chat_key(app: App, ev: Event) -> None:
    if ev[0] == "char":
        if len(app.typed) < MAX_MESSAGE:
            app.typed += ev[1]
        return
    name = ev[1]
    if name == "enter":
        text = app.typed.strip()
        app.typed = ""
        if text:
            send_chat(app, text)
        else:
            leave_chat(app)
    elif name in ("esc", "ctrl-d"):
        leave_chat(app)
    elif name == "backspace":
        app.typed = app.typed[:-1]
    elif name == "ctrl-u":
        app.typed = ""
    elif name == "ctrl-w":
        app.typed = app.typed.rstrip().rpartition(" ")[0]
