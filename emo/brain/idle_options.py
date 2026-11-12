"""The little unprompted things EMO might do, weighted by mood."""

from collections.abc import Callable

from .idle_acts import act, double_blink, glance, hop
from .state import Brain

type Option = tuple[float, Callable[[], None]]


def idle_options(brain: Brain) -> list[Option]:
    options: list[Option] = [
        (3.0, act(brain, "curious", 1.6)),
        (2.0, lambda: double_blink(brain)),
        (2.0, lambda: glance(brain)),
        (1.0, act(brain, "suspicious", 2.0)),
        (0.7, act(brain, "smug", 1.8)),
        (0.7, act(brain, "mischief", 1.8)),
        (0.7, act(brain, "thinking", 1.8)),
    ]
    if brain.affection > 0.45:
        options.append((2.0, lambda: hop(brain)))
    if brain.affection > 0.6:
        options.append((1.0, act(brain, "wink", 0.9)))
        if brain.boredom < 0.6:
            options.append((1.0, act(brain, "dance", 2.6, "hum", 0.5)))
    if brain.affection > 0.8:
        options.append((0.6, act(brain, "shy", 2.0)))
    if brain.energy < 0.45:
        options.append((4.0, act(brain, "yawn", 1.4, "yawn", 0.3)))
    if brain.energy < 0.25:
        options.append((5.0, act(brain, "hungry", 2.6, "hungry", 0.6)))
    if brain.boredom > 0.4:
        options.append((3.0, act(brain, "bored", 2.4, "bored", 0.35)))
    if brain.boredom > 0.7:
        options.append((3.0, act(brain, "pleading", 2.6, "lonely", 0.6)))
    return options
