"""Showing pixels as text: each character cell holds two stacked pixels."""

UPPER, LOWER, FULL = "▀", "▄", "█"


def _palette_index(r: int, g: int, b: int) -> int:
    """The closest colour in the terminal's 256-colour palette."""
    if max(r, g, b) - min(r, g, b) < 12:  # near grey: use the grey ramp
        v = (r + g + b) // 3
        return 16 if v < 5 else 231 if v > 246 else 232 + min(23, (v - 3) // 10)
    q = [0 if c < 48 else 1 if c < 115 else (c - 35) // 40 for c in (r, g, b)]
    return 16 + 36 * q[0] + 6 * q[1] + q[2]


class Pixels:
    """Encodes pairs of pixel rows as one row of half-block characters."""

    def __init__(self, mode: str) -> None:
        self.mode = mode  # 'truecolor', '256' or 'mono'
        self.fg: dict[int, str] = {}
        self.bg: dict[int, str] = {}

    def codes(self, p: int) -> None:
        """Remember the escape codes that select pixel colour ``p``."""
        if len(self.fg) > 30000:
            self.fg.clear()
            self.bg.clear()
        r, g, b = (p >> 16) & 255, (p >> 8) & 255, p & 255
        if self.mode == "truecolor":
            self.fg[p] = f"\x1b[38;2;{r};{g};{b}m"
            self.bg[p] = f"\x1b[48;2;{r};{g};{b}m"
        else:
            i = _palette_index(r, g, b)
            self.fg[p] = f"\x1b[38;5;{i}m"
            self.bg[p] = f"\x1b[48;5;{i}m"


def mono_row(top: list[int], bot: list[int]) -> str:
    """1-bit preview: what a single-colour OLED would show."""
    out = ["\x1b[97;40m"]
    for t, b in zip(top, bot):
        lt = max(t >> 16, (t >> 8) & 255, t & 255) >= 100
        lb = max(b >> 16, (b >> 8) & 255, b & 255) >= 100
        out.append(FULL if lt and lb else UPPER if lt else LOWER if lb else " ")
    out.append("\x1b[0m")
    return "".join(out)
