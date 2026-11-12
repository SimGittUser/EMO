"""Replaying a recorded script of sensor events through the brain."""

from random import Random
from typing import Any

from emo import brain, effects, face
from emo.brain import Brain
from emo.canvas import Canvas, glitch
from emo.effects import Effects
from emo.face import Face

from .helpers import digest, sha


def replay(script: list[Any]) -> tuple[Brain, dict[str, Any]]:
    """Run ``script`` (event names, [name, eye] pokes, and seconds to wait)."""
    rng = Random(3)
    emo, fx = Face(rng), Effects(rng)
    mind = Brain(emo, fx, rng)
    canvas = Canvas(96, 48)
    trace: list[str] = []
    said: list[str] = []
    frames: list[str] = []
    n = 0
    for s in script:
        if isinstance(s, str):
            brain.event(mind, s)
            continue
        if isinstance(s, list):
            brain.event(mind, s[0], eye=s[1])
            continue
        for _ in range(int(s * 30)):
            brain.update(mind, 1 / 30)
            face.update(emo, 1 / 30)
            effects.update(fx, 1 / 30, emo)
            canvas.clear()
            face.draw(emo, canvas)
            effects.draw(fx, canvas, emo)
            if emo.glitch > 0.02:
                glitch(canvas, rng, emo.glitch)
            if not trace or trace[-1] != mind.current:
                trace.append(mind.current)
            said += mind.outbox
            mind.outbox.clear()
            n += 1
            if n % 15 == 0:
                frames.append(sha(canvas.rows))
    return mind, {"trace": trace, "said": said, "frames": digest("".join(frames))}
