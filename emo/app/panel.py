"""The black panel that plays the part of EMO's screen."""

from .. import effects, face
from ..canvas import glitch
from ..term import pixel_row
from .screen import Layout
from .state import App

# quarter blocks that leave one corner of a cell empty
TOP_CORNERS = ("▟", "▙")
BOTTOM_CORNERS = ("▜", "▛")


def panel_rows(app: App, L: Layout) -> dict[int, str]:
    """Draw this frame and return it as screen row -> text."""
    canvas = app.canvas
    canvas.clear()
    face.draw(app.face, canvas)
    effects.draw(app.fx, canvas, app.face)
    if app.face.glitch > 0.02:
        glitch(canvas, app.rng, app.face.glitch)
    rows = canvas.rows
    pad = " " * L.px0
    black = "\x1b[38;2;0;0;0m" if app.color == "truecolor" else "\x1b[38;5;16m"
    rounded = app.color != "mono" and L.pw > 4
    lines = {}
    for r in range(L.ph):
        top, bot = rows[2 * r], rows[2 * r + 1]
        if rounded and r in (0, L.ph - 1):
            # nibble the corners so the black panel reads as a screen
            a, z = TOP_CORNERS if r == 0 else BOTTOM_CORNERS
            middle = pixel_row(app.pixels, top[1:-1], bot[1:-1])
            body = f"{black}{a}\x1b[0m{middle}{black}{z}\x1b[0m"
        else:
            body = pixel_row(app.pixels, top, bot)
        lines[L.py0 + r] = pad + body + "\x1b[K"
    return lines
