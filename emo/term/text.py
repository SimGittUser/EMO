"""Measuring and cutting text by how many terminal columns it fills."""

import unicodedata


def char_width(ch: str) -> int:
    if unicodedata.combining(ch):
        return 0
    return 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1


def text_width(s: str) -> int:
    return sum(char_width(c) for c in s)


def clip(s: str, width: int) -> str:
    """Cut a plain string so it fits in ``width`` columns."""
    out = []
    used = 0
    for ch in s:
        w = char_width(ch)
        if used + w > width:
            break
        out.append(ch)
        used += w
    return "".join(out)


def wrap(s: str, width: int) -> list[str]:
    """Word-wrap a plain string to ``width`` columns."""
    width = max(1, width)
    lines = []
    cur = ""
    for word in s.split():
        while text_width(word) > width:  # one over-long word: hard split
            if cur:
                lines.append(cur)
                cur = ""
            head = clip(word, width) or word[0]
            lines.append(head)
            word = word[len(head) :]
        if not word:
            continue
        if cur and text_width(cur) + 1 + text_width(word) > width:
            lines.append(cur)
            cur = word
        else:
            cur = (cur + " " + word) if cur else word
    if cur:
        lines.append(cur)
    return lines
