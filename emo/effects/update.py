"""Advancing the overlay effects by one frame."""

from ..face import Face
from .emit_air import notes, puff, sparkles, zzz
from .emit_love import hearts, hearts_few
from .emit_water import sweat, sweat_up, tear1, tears
from .state import Effects

MAX_PARTICLES = 80

# The order matters: emitters share one random stream.
EMITTERS = (hearts, hearts_few, tears, tear1, zzz, sweat, sweat_up, notes, sparkles, puff)


def update(fx: Effects, dt: float, face: Face) -> None:
    fx.t += dt
    for n in fx.active:
        fx.active[n] += dt
    for emit in EMITTERS:
        emit(fx, dt, face)
    alive = []
    for p in fx.parts:
        p.age += dt
        if p.age >= p.life:
            continue
        p.vy += p.ay * dt
        p.x += p.vx * dt
        p.y += p.vy * dt
        alive.append(p)
    fx.parts = alive[-MAX_PARTICLES:]
