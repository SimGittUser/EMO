"""One floating sprite."""

from ..canvas.blit import Sprite

type Color = tuple[int, int, int]


class Particle:
    __slots__ = (
        "age",
        "ay",
        "color",
        "grow",
        "life",
        "seed",
        "size",
        "sprite",
        "vx",
        "vy",
        "wob",
        "wob_hz",
        "x",
        "y",
    )

    def __init__(
        self,
        sprite: Sprite,
        x: float,
        y: float,
        vx: float = 0.0,
        vy: float = 0.0,
        ay: float = 0.0,
        life: float = 1.0,
        size: float = 1.0,
        grow: float = 0.0,
        color: Color = (255, 255, 255),
        wob: float = 0.0,
        wob_hz: float = 1.0,
        seed: float = 0.0,
    ) -> None:
        self.sprite = sprite
        self.x, self.y, self.vx, self.vy, self.ay = x, y, vx, vy, ay
        self.age = 0.0
        self.life = life
        self.size = size
        self.grow = grow  # extra size per second
        self.color = color
        self.wob = wob  # sideways wobble: amount, speed, and a random start
        self.wob_hz = wob_hz
        self.seed = seed
