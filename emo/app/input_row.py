"""The row where the human types, or where hints are shown."""

from ..expressions import GALLERY
from ..gemini import explain
from ..term import Part, styled, text_width
from .screen import Layout
from .state import App

SEND_HINT = "Enter send · Esc back "


def _typing_row(app: App, cols: int) -> str:
    room = max(4, cols - 12 - len(SEND_HINT))
    typed = app.typed
    while text_width(typed) > room:  # keep the end of a long message in view
        typed = typed[1:]
    cursor = "█" if int(app.now * 2.5) % 2 == 0 else " "
    parts: list[Part] = [("1;32", "   you › "), ("", typed), ("32", cursor)]
    gap = cols - 9 - text_width(typed) - 1 - len(SEND_HINT)
    if gap > 0:
        parts += [("", " " * gap), ("2", SEND_HINT)]
    return styled(parts, cols)


def _hint_row(app: App, L: Layout) -> str:
    pinned = app.brain.pinned
    keys = "hide" if L.help else "show"
    hint = f"   Enter talk to EMO · h {keys} keys · q quit"
    if app.o.demo:
        hint = "   demo: showing every face · press any key to play"
    elif pinned:
        name = pinned.replace("_", " ")
        hint = f"   face {app.gallery_i + 1}/{len(GALLERY)}: {name} · [ ] browse"
    parts: list[Part] = [("2", hint)]
    if app.ai and app.ai.problem and not (app.o.demo or pinned):
        parts.append(("31", "   AI: " + explain(app.ai.problem, app.ai.detail)))
    return styled(parts, L.cols)


def input_row(app: App, L: Layout) -> str:
    if app.mode == "chat":
        return _typing_row(app, L.cols)
    return _hint_row(app, L)
