"""Pixel-art sprites."""

from .canvas import Canvas
from .rect import fill_rect
from .sdf_row import Rgb

type Sprite = tuple[str, ...]


def blit(
    canvas: Canvas,
    sprite: Sprite,
    x: float,
    y: float,
    px: int,
    color: Rgb,
    alpha: float = 1.0,
) -> None:
    """Draw a sprite (rows of text, '#' = lit).

    (x, y) is the top-left corner in canvas pixels and ``px`` is how many
    canvas pixels each sprite pixel covers.
    """
    px = max(1, int(px))
    left = round(x)
    top = round(y)
    for j, line in enumerate(sprite):
        yy = top + j * px
        if yy >= canvas.h or yy + px <= 0:
            continue
        i = 0
        n = len(line)
        while i < n:
            if line[i] != "#":
                i += 1
                continue
            k = i
            while k < n and line[k] == "#":
                k += 1
            fill_rect(canvas, left + i * px, yy, left + k * px, yy + px, color, alpha)
            i = k
