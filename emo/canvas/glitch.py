"""A post effect: the picture tearing, like a display taking a knock."""

from random import Random

from .canvas import Canvas


def glitch(canvas: Canvas, rng: Random, amount: float) -> None:
    """Tear a few horizontal bands of the canvas sideways."""
    if amount <= 0:
        return
    canvas.touch(0, canvas.h)
    bands = 1 + int(amount * 5)
    reach = int(canvas.w * 0.18 * amount) + 1
    for _ in range(bands):
        y0 = rng.randrange(canvas.h)
        hh = 1 + rng.randrange(max(1, int(canvas.h * 0.12)))
        k = rng.randint(-reach, reach)
        if not k:
            continue
        for y in range(y0, min(canvas.h, y0 + hh)):
            row = canvas.rows[y]
            row[:] = row[-k:] + row[:-k]
