"""Emitters for tears and sweat."""

from ..face import Face
from .particle import Particle
from .sprites import DROP, SWEAT_BLUE, TEAR, TEAR_BLUE
from .state import Effects, every


def tears(fx: Effects, dt: float, face: Face) -> None:
    if "tears" in fx.active and every(fx, "tears", dt, 0.2):
        r = fx.rng
        fx.flip ^= 1
        ex, ey, ehw, ehh = face.geom[fx.flip]
        x = ex + r.uniform(-0.6, 0.6) * ehw
        fx.parts.append(
            Particle(TEAR, x, ey + ehh + 1, vy=r.uniform(6, 14), ay=70.0, life=0.85,
                     size=1, color=TEAR_BLUE)
        )


def tear1(fx: Effects, dt: float, face: Face) -> None:
    """A single tear at the corner of one eye, for yawning."""
    if "tear1" in fx.active and every(fx, "tear1", dt, 1.1):
        rx, ry, rhw, rhh = face.geom[1]
        fx.parts.append(
            Particle(TEAR, rx + rhw * 0.8, ry + rhh + 2, vy=5.0, ay=30.0, life=1.0,
                     size=1, color=TEAR_BLUE)
        )


def sweat(fx: Effects, dt: float, face: Face) -> None:
    if "sweat" in fx.active and every(fx, "sweat", dt, 1.25):
        rx, ry, rhw, rhh = face.geom[1]
        fx.parts.append(
            Particle(DROP, rx + rhw + 9, ry - rhh + 1, vy=9.0, ay=14.0, life=1.15,
                     size=1, color=SWEAT_BLUE)
        )


def sweat_up(fx: Effects, dt: float, face: Face) -> None:
    """Sweat flying upwards - what happens when you are upside down."""
    if "sweat_up" in fx.active and every(fx, "sweat_up", dt, 0.5):
        fx.flip ^= 1
        ex, ey, ehw, _ = face.geom[fx.flip]
        side = 1 if fx.flip else -1
        fx.parts.append(
            Particle(TEAR, ex + side * (ehw + 7), ey + 4, vy=-12.0, ay=-40.0, life=0.9,
                     size=1, color=SWEAT_BLUE)
        )
