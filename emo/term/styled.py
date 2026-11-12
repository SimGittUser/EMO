"""Building one coloured row of text."""

from .text import clip, text_width

# A piece of text and the ANSI style to show it in ("" = plain, "1" = bold ...).
type Part = tuple[str, str]


def styled(parts: list[Part], width: int) -> str:
    """Join (style, text) pieces, clipped and padded to exactly ``width`` columns."""
    out = []
    left = width
    for sgr, text in parts:
        if left <= 0:
            break
        text = clip(text, left)
        left -= text_width(text)
        out.append(f"\x1b[{sgr}m{text}\x1b[0m" if sgr else text)
    if left > 0:
        out.append(" " * left)
    return "".join(out)
