"""How moods drift as time passes, and when EMO nods off."""

from .notes import clamp
from .sleep import fall_asleep, wake
from .state import Brain


def _drift(brain: Brain, dt: float) -> None:
    if not brain.asleep:
        brain.energy = clamp(brain.energy - dt / (200.0 if brain.music else 600.0))
    brain.affection += (0.5 - brain.affection) * dt * 0.004
    brain.annoyance = clamp(brain.annoyance - dt * 0.06)
    brain.dizziness = clamp(brain.dizziness - dt * 0.12)
    brain.fear = clamp(brain.fear - dt * 0.08)
    if not brain.asleep and not brain.listening:
        brain.boredom = clamp(brain.boredom + dt / 110.0)
    if brain.music and brain.music_until and brain.t > brain.music_until:
        brain.music = False
        brain.music_until = 0.0
    if brain.pinned and brain.t > brain.pinned_until:
        brain.pinned = None


def _busy(brain: Brain) -> bool:
    return bool(
        brain.step is not None
        or brain.held
        or brain.flipped
        or brain.tilt
        or brain.music
        or brain.listening
        or brain.thinking
        or brain.pinned
    )


def update_moods(brain: Brain, dt: float) -> None:
    awake = not brain.asleep
    _drift(brain, dt)
    if awake:
        sleepy = brain.dark or brain.energy < 0.18 or brain.boredom >= 1.0
        if sleepy and not _busy(brain):
            brain.drowsy += dt / (7.0 if brain.dark else 14.0)
            if brain.drowsy >= 1.0:
                fall_asleep(brain)
        else:
            brain.drowsy = max(0.0, brain.drowsy - dt * 0.5)
    else:
        brain.slept += dt
        brain.energy = clamp(brain.energy + dt / 40.0)
        if brain.energy >= 1.0 and not brain.dark and brain.slept > brain.nap_len:
            wake(brain, "natural")
