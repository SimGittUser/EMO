"""Emitters for floating hearts."""

from ..face import Face
from .particle import Particle
from .sprites import HEART, PINKS
from .state import Effects, every


def hearts(fx: Effects, dt: float, face: Face) -> None:
    if "hearts" in fx.active and every(fx, "hearts", dt, 0.26):
        r = fx.rng
        mx = (face.geom[0][0] + face.geom[1][0]) / 2.0
        fx.parts.append(
            Particle(
                HEART, mx + r.uniform(-46, 46), r.uniform(36, 52), vy=r.uniform(-24, -14),
                life=r.uniform(1.5, 2.1), size=r.choice((1, 1, 2)), color=r.choice(PINKS),
                wob=2.5, wob_hz=1.2, seed=r.random(),
            )
        )


def hearts_few(fx: Effects, dt: float, face: Face) -> None:
    if "hearts_few" in fx.active and every(fx, "hearts_few", dt, 0.85):
        r = fx.rng
        mx = (face.geom[0][0] + face.geom[1][0]) / 2.0
        fx.parts.append(
            Particle(
                HEART, mx + r.choice((-1, 1)) * r.uniform(34, 50), r.uniform(26, 40),
                vy=r.uniform(-18, -12), life=1.7, size=1, color=r.choice(PINKS),
                wob=2.0, wob_hz=1.2, seed=r.random(),
            )
        )
