"""Encoding two rows of pixels as one row of terminal text."""

from .pixels import UPPER, Pixels, mono_row


def pixel_row(px: Pixels, top: list[int], bot: list[int]) -> str:
    """One text row showing pixel rows ``top`` and ``bot`` stacked.

    A cell whose two pixels match is a space on that background colour;
    otherwise it is an upper half block, foreground over background. Colour
    codes are only written when the colour actually changes.
    """
    if px.mode == "mono":
        return mono_row(top, bot)
    fgs, bgs = px.fg, px.bg
    out = []
    fg = bg = -1
    for t, b in zip(top, bot):
        if t == b:
            if bg != t:
                if t not in bgs:
                    px.codes(t)
                out.append(bgs[t])
                bg = t
            out.append(" ")
        else:
            if fg != t:
                if t not in fgs:
                    px.codes(t)
                out.append(fgs[t])
                fg = t
            if bg != b:
                if b not in bgs:
                    px.codes(b)
                out.append(bgs[b])
                bg = b
            out.append(UPPER)
    out.append("\x1b[0m")
    return "".join(out)
