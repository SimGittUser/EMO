"""Springs: nothing on the face snaps, every number chases its target."""

from math import sqrt


class Springs:
    """A bag of named numbers, each easing toward its own target."""

    def __init__(
        self,
        defaults: dict[str, float],
        conf: dict[str, tuple[float, float]],
    ) -> None:
        self.cur = dict(defaults)
        self.tgt = dict(defaults)
        self.vel = dict.fromkeys(defaults, 0.0)
        self.k: dict[str, float] = {}
        self.c: dict[str, float] = {}
        for key in defaults:
            k, zeta = conf.get(key, (200.0, 1.0))
            self.k[key] = float(k)
            self.c[key] = 2.0 * zeta * sqrt(k)

    def step(self, h: float, speed: float) -> None:
        """Advance every spring by ``h`` seconds."""
        cur, tgt, vel, kk, cc = self.cur, self.tgt, self.vel, self.k, self.c
        s2 = speed * speed
        for key in cur:
            pull = kk[key] * s2 * (tgt[key] - cur[key])
            v = vel[key] + (pull - cc[key] * speed * vel[key]) * h
            vel[key] = v
            cur[key] += v * h
