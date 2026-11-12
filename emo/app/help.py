"""The key list shown at the bottom of the screen."""

from ..term import Part, styled, text_width
from .keymap import HELP


def _group(name: str, items: list[tuple[str, str]]) -> list[Part]:
    parts: list[Part] = [("1;36", name + " ")]
    for i, (key, what) in enumerate(items):
        if i:
            parts.append(("2", " · "))
        parts.append(("1", key))
        parts.append(("2", " " + what))
    return parts


def help_lines(cols: int) -> list[str]:
    """The key list, flowed into as many rows as ``cols`` columns need."""
    lines: list[list[Part]] = [[]]
    used = 1
    for name, items in HELP:
        parts = _group(name, items)
        w = sum(text_width(t) for _, t in parts)
        if used > 1 and used + 3 + w > cols:
            lines.append([])
            used = 1
        gap: Part = ("", "   ") if used > 1 else ("", " ")
        lines[-1] += [gap, *parts]
        used += w + (3 if used > 1 else 0)
    return [styled(parts, cols) for parts in lines]
