"""Putting EMO's situation into words, for the AI."""

from .state import Brain


def describe(brain: Brain) -> str:
    bits = [
        f"energy {int(brain.energy * 100)}%",
        f"affection for your human {int(brain.affection * 100)}%",
    ]
    if brain.annoyance > 0.3:
        bits.append(f"annoyed {int(brain.annoyance * 100)}%")
    if brain.fear > 0.3:
        bits.append("frightened")
    if brain.dizziness > 0.3:
        bits.append("dizzy")
    if brain.boredom > 0.6:
        bits.append("bored")
    if brain.held:
        bits.append("being held in the air")
    if brain.tilt:
        bits.append("tipped to one side")
    if brain.flipped:
        bits.append("upside down")
    if brain.dark:
        bits.append("the room is dark")
    if brain.music:
        bits.append("music is playing")
    out = "Right now: " + ", ".join(bits) + ". Your face shows: " + brain.current + "."
    if brain.recent:
        events = " ".join(f"({int(brain.t - when)}s ago) {what}" for when, what in brain.recent)
        out += " Recent events, oldest first: " + events
    return out
