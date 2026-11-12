"""The baseline: the face the mood and situation call for when no script runs."""

from .state import Brain


def _situation(brain: Brain) -> str | None:
    """Faces forced by what is physically happening to EMO."""
    if brain.pinned:
        return brain.pinned
    if brain.asleep:
        return "sleeping"
    if brain.thinking:
        return "thinking"
    if brain.flipped:
        return "upside_down"
    if brain.dizziness > 0.55:
        return "dizzy"
    if brain.music and brain.music_until:  # a dance it was asked to do
        return "dance"
    if brain.listening:
        return "listening"
    if brain.tilt:
        return "tilt_left" if brain.tilt < 0 else "tilt_right"
    if brain.held:
        return "nervous" if (brain.fear > 0.3 or brain.affection < 0.4) else "curious"
    if brain.music:
        return "dance"
    return None


def baseline(brain: Brain) -> str:
    forced = _situation(brain)
    if forced:
        return forced
    if brain.annoyance > 0.6:
        return "angry"
    if brain.annoyance > 0.3:
        return "annoyed"
    if brain.fear > 0.55:
        return "scared"
    if brain.dark or brain.energy < 0.18 or brain.drowsy > 0.5:
        return "sleepy"
    if brain.boredom > 0.8 and brain.affection < 0.3:
        return "sad"
    if brain.boredom > 0.6:
        return "bored"
    if brain.affection > 0.75:
        return "happy"
    return "neutral"
