"""Scripts: short scripted reactions, e.g. startled -> dizzy -> sick."""

from collections import deque

from .show import show
from .state import Brain
from .step import Step


def advance(brain: Brain) -> None:
    """Move on to the script's next step, or finish it."""
    if brain.script:
        step = brain.script.popleft()
        brain.step = step
        brain.step_left = step.seconds
        show(brain, step.face)
        if step.then:
            step.then()
        return
    brain.step = None
    brain.priority = 0
    if brain.after:
        f, brain.after = brain.after, None
        f()


def play(brain: Brain, steps: list[Step], prio: int = 1) -> bool:
    """Run a reaction, unless something more important is already playing."""
    if brain.step is not None and prio < brain.priority:
        return False
    brain.script = deque(steps)
    brain.priority = prio
    brain.after = None
    advance(brain)
    return True


def extend(brain: Brain, name: str, seconds: float) -> bool:
    """Keep showing ``name``; if it is already up, just top up its timer."""
    if brain.step is not None and brain.step.face == name and not brain.script:
        brain.step_left = max(brain.step_left, seconds)
        return True
    return play(brain, [Step(name, seconds)])


def cancel(brain: Brain, prio: int = 1) -> None:
    """Stop the running script if it is no more important than ``prio``."""
    if brain.step is not None and brain.priority <= prio:
        brain.script.clear()
        brain.step = None
        brain.priority = 0
        brain.after = None
