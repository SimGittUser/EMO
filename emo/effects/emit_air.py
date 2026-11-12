"""Emitters for snores, music notes, sparkles and sighs."""

import colorsys

from ..face import VH, Face
from .particle import Particle
from .sprites import NOTE, NOTES, PUFF, SPARK, SPARK_S, WHITE, YELLOW, ZED
from .state import Effects, every


def zzz(fx: Effects, dt: float, face: Face) -> None:
    if "zzz" in fx.active and every(fx, "zzz", dt, 1.15):
        rx, ry, rhw, _ = face.geom[1]
        fx.parts.append(
            Particle(ZED, rx + rhw + 4, ry - 8, vx=6.5, vy=-9.0, life=2.6, size=1.0,
                     grow=0.55, color=(120, 200, 255), wob=1.5, wob_hz=0.6,
                     seed=fx.rng.random())
        )


def notes(fx: Effects, dt: float, face: Face) -> None:
    if "notes" in fx.active and every(fx, "notes", dt, 0.42):
        r = fx.rng
        mx = (face.geom[0][0] + face.geom[1][0]) / 2.0
        fx.flip ^= 1
        side = 1 if fx.flip else -1
        red, green, blue = colorsys.hsv_to_rgb(r.random(), 0.6, 1.0)
        fx.parts.append(
            Particle(
                r.choice((NOTE, NOTES)), mx + side * r.uniform(40, 54), r.uniform(34, 50),
                vy=r.uniform(-20, -13), life=1.6, size=1,
                color=(int(red * 255), int(green * 255), int(blue * 255)),
                wob=3.0, wob_hz=1.5, seed=r.random(),
            )
        )


def sparkles(fx: Effects, dt: float, face: Face) -> None:
    if "sparkles" in fx.active and every(fx, "sparkles", dt, 0.11):
        r = fx.rng
        fx.parts.append(
            Particle(
                r.choice((SPARK, SPARK_S, SPARK_S)), r.uniform(6, 122), r.uniform(4, 60),
                life=r.uniform(0.3, 0.6), size=r.choice((1, 1, 2)),
                color=r.choice((YELLOW, WHITE, (170, 240, 255))),
            )
        )


def puff(fx: Effects, dt: float, face: Face) -> None:
    """One little sigh of relief, right as the effect starts."""
    act = fx.active
    if "puff" in act and act["puff"] < 0.5 and every(fx, "puff", dt, 5.0):
        mx = (face.geom[0][0] + face.geom[1][0]) / 2.0
        y = min(VH - 6.0, max(face.geom[0][1], face.geom[1][1]) + 12)
        fx.parts.append(
            Particle(PUFF, mx, y, vx=10.0, vy=-2.0, life=1.0, size=1.0, grow=1.0,
                     color=(170, 215, 235))
        )
