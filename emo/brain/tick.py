"""Advancing the brain by one frame."""

from .baseline import baseline
from .idle_options import idle_options
from .moods import update_moods
from .script import advance
from .show import show
from .state import Brain

CALM = ("neutral", "happy", "bored", "sleepy")


def _idle(brain: Brain, dt: float) -> None:
    """Small unprompted behaviours, so EMO never just sits there."""
    if brain.asleep or brain.pinned or brain.listening or brain.thinking:
        return
    brain.idle_next -= dt
    if brain.idle_next > 0.0:
        return
    brain.idle_next = brain.rng.uniform(5.0, 11.0)
    if brain.current not in CALM:
        return
    options = idle_options(brain)
    pick = brain.rng.uniform(0.0, sum(w for w, _ in options))
    for w, run in options:
        pick -= w
        if pick <= 0.0:
            run()
            break


def update(brain: Brain, dt: float) -> None:
    brain.t += dt
    update_moods(brain, dt)
    if brain.step is not None:
        brain.step_left -= dt
        if brain.step_left <= 0.0:
            advance(brain)
    if brain.step is None:
        show(brain, baseline(brain))
        _idle(brain, dt)
