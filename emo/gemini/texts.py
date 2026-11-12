"""Finding the generated text in a response, whichever API produced it."""

from typing import Any


def _interaction_texts(obj: dict[str, Any]) -> list[str]:
    out = []
    for step in obj.get("steps") or obj.get("outputs") or []:
        if not isinstance(step, dict) or step.get("type") in ("thought", "user_input"):
            continue
        if isinstance(step.get("text"), str):
            out.append(step["text"])
        for part in step.get("content") or []:
            if isinstance(part, dict) and isinstance(part.get("text"), str):
                out.append(part["text"])
    return out


def _generate_texts(obj: dict[str, Any]) -> list[str]:
    out = []
    for cand in (obj.get("candidates") or [])[:1]:
        for part in (cand.get("content") or {}).get("parts") or []:
            if isinstance(part.get("text"), str) and not part.get("thought"):
                out.append(part["text"])
    return out


def response_text(obj: dict[str, Any]) -> str:
    """The model's words from an Interactions or generateContent response."""
    return "".join(_interaction_texts(obj) + _generate_texts(obj))
