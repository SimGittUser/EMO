"""Splitting the raw input stream into events."""

from .keys import CSI_KEYS, CTRL_KEYS, Event, csi


def _escape(s: str, i: int, out: list[Event]) -> int:
    """Handle the escape at s[i]; return where to carry on, or -1 to wait."""
    n = len(s)
    if i + 1 >= n:  # a bare Escape key
        out.append(("key", "esc"))
        return i + 1
    c2 = s[i + 1]
    if c2 == "[":
        j = i + 2
        while j < n and not ("@" <= s[j] <= "~"):
            j += 1
        if j >= n:  # incomplete: wait for the rest, unless it is garbage
            return n if n - i > 64 else -1
        ev = csi(s[i + 2 : j], s[j])
        if ev:
            out.append(ev)
        return j + 1
    if c2 == "O" and i + 2 < n:
        if s[i + 2] in "ABCD":
            out.append(("key", CSI_KEYS[s[i + 2]]))
        return i + 3
    if c2 == "\x1b":
        out.append(("key", "esc"))
        return i + 1
    return i + 2  # Alt+key: ignore


def parse(s: str) -> tuple[list[Event], str]:
    """Decode buffered input. Returns the events and any unfinished tail."""
    n = len(s)
    i = 0
    out: list[Event] = []
    while i < n:
        c = s[i]
        if c == "\x1b":
            nxt = _escape(s, i, out)
            if nxt < 0:
                break
            i = nxt
        elif c in CTRL_KEYS:
            out.append(("key", CTRL_KEYS[c]))
            i += 1
        elif c < " ":
            i += 1
        else:
            out.append(("char", c))
            i += 1
    return out, s[i:]
