"""Working out where everything goes on the screen."""

from .help import help_lines
from .screen import Layout
from .state import App


def compute_layout(app: App) -> Layout:
    """Fit the layout to the window, and wipe the screen to start afresh."""
    cols, rows = app.term.size()
    app.prev.clear()
    app.term.write("\x1b[2J")
    want_help = app.show_help if app.show_help is not None else rows >= 30
    helps = help_lines(cols) if want_help else []
    ph = rows - 1 - 4 - len(helps)
    if ph < 6 and helps:
        helps = []
        ph = rows - 5
    if cols < 28 or ph < 4:
        return Layout(small=True, cols=cols)
    ph = min(ph, (cols + 3) // 4 + 1)
    pw = min(cols, ph * 4)
    app.canvas.resize(pw, ph * 2)
    return Layout(
        small=False,
        cols=cols,
        ph=ph,
        pw=pw,
        px0=(cols - pw) // 2,
        speech=2 + ph,
        input=5 + ph,
        helps=tuple(helps),
        help_row=6 + ph,
    )
