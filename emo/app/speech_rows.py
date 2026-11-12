"""The three rows under the face: what was said, by whom."""

from ..term import Part, styled, wrap
from .state import App
from .talk import CPS


def _revealed(app: App, cols: int) -> tuple[list[str], bool]:
    """EMO's words so far, as up to two rows; and whether row one starts them."""
    shown = int((app.now - app.speech_at) * CPS)
    wrapped = wrap(app.speech, max(8, cols - 12)) or [""]
    reveal = []
    for w in wrapped:
        if shown <= 0:
            break
        reveal.append(w[:shown])
        shown -= len(w) + 1
    reveal = reveal[-2:] or [""]
    starts = reveal[0] == wrapped[0][: len(reveal[0])]
    return reveal, len(wrapped) <= 2 or len(reveal) < 2 or starts


def speech_rows(app: App, cols: int) -> list[str]:
    """Row one: what the human last said. Rows two and three: EMO's words,
    appearing letter by letter."""
    blank = " " * cols
    you = blank
    if app.you and app.now < app.you_until:
        you = styled([("2", "   you › "), ("2", app.you)], cols)
    say = [blank, blank]
    if app.speech:
        reveal, first = _revealed(app, cols)
        for i, text in enumerate(reveal):
            head: Part = ("1;36", "   EMO › ") if i == 0 and first else ("", "         ")
            say[i] = styled([head, ("1", text)], cols)
    return [you, *say]
