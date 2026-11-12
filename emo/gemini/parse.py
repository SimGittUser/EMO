"""Turning the model's answer into something EMO can act on."""

import json

from ..expressions import AI_EMOTIONS
from .prompt import ACTIONS

SYNONYMS = {
    "excited": "joy", "joyful": "joy", "content": "happy", "loving": "love",
    "laughing": "laugh", "proud": "smug", "playful": "mischief", "embarrassed": "shy",
    "afraid": "scared", "fear": "scared", "nervous": "scared", "crying": "cry",
    "mad": "angry", "furious": "angry", "tired": "sleepy", "sleeping": "sleepy",
    "shocked": "surprised", "startled": "surprised", "listening": "curious",
}

FANCY = (
    ("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
    ("—", "-"), ("–", "-"), ("…", "..."),
)


def _fields(text: str) -> tuple[str, str, str]:
    """Pull say / emotion / action out of the JSON object in ``text``, if any."""
    a, b = text.find("{"), text.rfind("}")
    if a != -1 and b > a:
        try:
            obj = json.loads(text[a : b + 1])
        except ValueError:
            obj = None
        if isinstance(obj, dict):
            return (
                str(obj.get("say", "") or ""),
                str(obj.get("emotion", "neutral")).strip().lower(),
                str(obj.get("action", "none")).strip().lower(),
            )
    return text.strip(), "neutral", "none"


def parse_reply(text: str) -> dict[str, str]:
    """Turn the model's answer into {'say', 'emotion', 'action'}, forgivingly."""
    say, emotion, action = _fields(text)
    emotion = SYNONYMS.get(emotion, emotion)
    if emotion not in AI_EMOTIONS:
        emotion = "neutral"
    if action not in ACTIONS:
        action = "none"
    say = " ".join("".join(c for c in say if c >= " " or c == "\n").split())
    for fancy, plain in FANCY:
        say = say.replace(fancy, plain)
    return {"say": say[:240], "emotion": emotion, "action": action}
