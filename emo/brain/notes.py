"""Small bookkeeping shared by the reactions."""

from .state import Brain


def clamp(v: float) -> float:
    """Keep a mood within 0..1."""
    return 0.0 if v < 0.0 else min(v, 1.0)


def say(brain: Brain, key: str, chance: float = 1.0) -> None:
    """Maybe ask the app to speak the phrase ``key`` (never twice in a row)."""
    if brain.rng.random() < chance and brain.t - brain.last_say > 1.8:
        brain.last_say = brain.t
        brain.outbox.append(key)


def count(brain: Brain, name: str, window: float) -> int:
    """How many times ``name`` happened within the last ``window`` seconds."""
    times = [x for x in brain.stamps.get(name, ()) if brain.t - x <= window]
    times.append(brain.t)
    brain.stamps[name] = times[-8:]
    return len(times)


def note(brain: Brain, what: str) -> None:
    """Remember an event so the AI can be told about it."""
    brain.recent.append((brain.t, what))
