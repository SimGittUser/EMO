"""Putting a frame on the screen, rewriting only the rows that changed."""

from ..term import styled
from .input_row import input_row
from .layout import compute_layout
from .panel import panel_rows
from .screen import Layout
from .speech_rows import speech_rows
from .state import App
from .status import status_line


def _frame(app: App, L: Layout) -> dict[int, str]:
    """Everything that should be on screen now, as row number -> text."""
    if L.small:
        return {1: styled([("1", "EMO needs a bigger window")], L.cols)}
    lines = {1: status_line(app, L.cols)}
    lines.update(panel_rows(app, L))
    for i, row in enumerate(speech_rows(app, L.cols)):
        lines[L.speech + i] = row
    lines[L.input] = input_row(app, L)
    for i, row in enumerate(L.helps):
        lines[L.help_row + i] = row
    return lines


def draw(app: App) -> None:
    if app.layout is None:
        app.layout = compute_layout(app)
    out = []
    prev = app.prev
    for y, s in _frame(app, app.layout).items():
        if prev.get(y) != s:
            prev[y] = s
            out.append(f"\x1b[{y};1H{s}")
    if out:
        # synchronized output: the terminal shows the frame all at once
        app.term.write("\x1b[?2026h" + "".join(out) + "\x1b[?2026l")
