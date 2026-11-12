"""Mixing a colour into a packed pixel."""


def blend(p: int, r: float, g: float, b: float, a: float) -> int:
    """Return pixel ``p`` moved a fraction ``a`` of the way to colour (r, g, b)."""
    pr = p >> 16
    pg = (p >> 8) & 255
    pb = p & 255
    return (
        (int(pr + (r - pr) * a) << 16)
        | (int(pg + (g - pg) * a) << 8)
        | int(pb + (b - pb) * a)
    )


def edge_alpha(d: float, glow: float, glow_strength: float) -> float:
    """Coverage of a pixel ``d`` pixels from a shape's edge, halo included."""
    if d < 0.5:
        a = 0.5 - d
        if glow:
            a += (1.0 - a) * glow_strength
        return a
    t = 1.0 - (d - 0.5) / glow
    return glow_strength * t * t
