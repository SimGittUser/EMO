"""What the mock Gemini service answers, in each of its moods."""

import json
from typing import Any

type Answer = tuple[int, dict[str, Any]]


def _error(code: int, message: str) -> Answer:
    return code, {"error": {"code": code, "message": message}}


def _words(say: str, emotion: str, action: str = "none") -> str:
    return json.dumps({"say": say, "emotion": emotion, "action": action})


def _interaction(mode: str, body: dict[str, Any]) -> Answer:
    if mode == "legacy":
        return _error(404, "no such endpoint")
    if mode == "strict" and "response_format" in body:
        return _error(400, "Unknown field response_format")
    text = _words("Heard you!", "joy", "wink")
    if mode == "fenced":
        text = "Sure!\n```json\n" + text + "\n```"
    steps = [
        {"type": "thought", "signature": "abc"},
        {"type": "model_output", "content": [{"type": "text", "text": text}]},
    ]
    return 200, {"status": "completed", "steps": steps}


def reply_for(mode: str, path: str, body: dict[str, Any], key: str | None) -> Answer:
    """The (status, json) the service gives for one POST."""
    if key != "test-key":
        return _error(400, "API key not valid. Please pass a valid API key.")
    if mode == "limit":
        return _error(429, "Quota exceeded")
    interaction = path == "/v1beta/interactions"
    model = body.get("model") if interaction else path.split("/models/")[-1].split(":")[0]
    if mode == "nomodel" and model != "gemini-3.5-flash-lite":
        return _error(404, f"model {model} not found")
    if interaction:
        return _interaction(mode, body)
    parts = [{"text": "hmm", "thought": True}, {"text": _words("Old API here.", "smug")}]
    return 200, {"candidates": [{"content": {"parts": parts}}]}
