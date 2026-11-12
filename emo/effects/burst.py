"""One-off puffs of particles, e.g. hearts when patted."""

from .particle import Particle
from .sprites import HEART, PINKS, SPARK, SPARK_S, STAR, WHITE, YELLOW
from .state import Effects


def _one(fx: Effects, kind: str) -> Particle | None:
    r = fx.rng
    if kind == "hearts":
        return Particle(
            HEART, r.uniform(26, 102), r.uniform(30, 48),
            vx=r.uniform(-8, 8), vy=r.uniform(-30, -16), life=r.uniform(1.0, 1.6),
            size=r.choice((1, 1, 2)), color=r.choice(PINKS),
            wob=2.0, wob_hz=1.3, seed=r.random(),
        )
    if kind == "sparkles":
        return Particle(
            r.choice((SPARK, SPARK_S)), r.uniform(10, 118), r.uniform(5, 58),
            life=r.uniform(0.3, 0.7), size=r.choice((1, 1, 2)),
            color=r.choice((YELLOW, WHITE)),
        )
    if kind == "stars":
        return Particle(
            r.choice((STAR, SPARK)), 64 + r.uniform(-10, 10), 30,
            vx=r.uniform(-70, 70), vy=r.uniform(-70, -15), ay=150.0,
            life=r.uniform(0.6, 1.0), size=1, color=YELLOW,
        )
    return None


def burst(fx: Effects, kind: str, n: int = 5) -> None:
    for _ in range(n):
        p = _one(fx, kind)
        if p is not None:
            fx.parts.append(p)
