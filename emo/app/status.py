"""The status bar along the top of the screen."""

from ..term import Part, styled, text_width
from .state import App

AI_NOTES = {
    "limit": "AI rate-limited, resting",
    "key": "AI key was rejected",
    "offline": "AI unreachable",
    "error": "AI error",
}


def _bar(v: float, n: int = 6) -> str:
    k = round(max(0.0, min(1.0, v)) * n)
    return "█" * k + "░" * (n - k)


def _ai_note(app: App) -> str:
    if app.ai is None:
        return "AI off (no key)"
    if app.ai.problem:
        return AI_NOTES.get(app.ai.problem, "AI error")
    if app.ai.busy:
        return "AI thinking..."
    return "AI " + app.ai.model


def status_line(app: App, cols: int) -> str:
    b = app.brain
    energy = "32" if b.energy > 0.5 else "33" if b.energy > 0.2 else "31"
    left: list[Part] = [
        ("1;30;46", " EMO "),
        ("", " "),
        ("1", b.current.replace("_", " ")),
        ("", "   "),
        ("2", "energy "),
        (energy, _bar(b.energy)),
        ("", "  "),
        ("2", "love "),
        ("35", _bar(b.affection)),
    ]
    states = (
        (b.asleep, "asleep"),
        (b.held, "held"),
        (b.tilt, "tilted"),
        (b.flipped, "upside down"),
        (b.dark, "dark"),
        (b.music, "music"),
    )
    flags = [name for on, name in states if on]
    if flags:
        left += [("", "  "), ("36", " · ".join(flags))]
    right = _ai_note(app)
    gap = cols - sum(text_width(t) for _, t in left) - text_width(right) - 1
    if gap >= 2:
        left += [("", " " * gap), ("2", right)]
    return styled(left, cols)
