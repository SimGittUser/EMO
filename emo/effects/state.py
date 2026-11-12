"""What the overlay effects remember between frames."""

from random import Random

from .particle import Particle


class Effects:
    def __init__(self, rng: Random) -> None:
        self.rng = rng
        self.t = 0.0
        self.active: dict[str, float] = {}  # effect name -> seconds since it started
        self.cool: dict[str, float] = {}  # emitter name -> seconds until next spawn
        self.parts: list[Particle] = []
        self.flip = 0  # alternates between the two eyes


def set_effects(fx: Effects, names: list[str] | tuple[str, ...]) -> None:
    """Choose which effects are running; anything else winds down."""
    names = list(names)
    for n in list(fx.active):
        if n not in names:
            del fx.active[n]
    for n in names:
        if n not in fx.active:
            fx.active[n] = 0.0
            fx.cool[n] = 0.0


def every(fx: Effects, name: str, dt: float, period: float) -> bool:
    """True once per ``period`` seconds for the emitter called ``name``."""
    fx.cool[name] = fx.cool.get(name, 0.0) - dt
    if fx.cool[name] <= 0.0:
        fx.cool[name] = period
        return True
    return False
