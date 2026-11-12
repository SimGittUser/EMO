"""The two Gemini endpoints EMO can talk to."""

from typing import Any

from .client import Gemini
from .errors import AIError
from .http import http
from .prompt import SCHEMA, SYSTEM
from .texts import response_text


def interactions(client: Gemini, prompt: str, rich: bool) -> str:
    """Ask through the Interactions API; ``rich`` adds the schema and hints."""
    body: dict[str, Any] = {
        "model": client.model,
        "system_instruction": SYSTEM,
        "input": prompt,
        "store": False,
    }
    if rich:
        body["response_format"] = {
            "type": "text",
            "mime_type": "application/json",
            "schema": SCHEMA,
        }
        body["generation_config"] = {"thinking_level": "minimal"}
    obj = http(client, "POST", "/v1beta/interactions", body, {"Api-Revision": "2026-05-20"})
    text = response_text(obj)
    if not text:
        raise AIError(500, f"empty reply (status: {obj.get('status')})")
    return text


def generate(client: Gemini, prompt: str) -> str:
    """Ask through the older generateContent API."""
    body = {
        "systemInstruction": {"parts": [{"text": SYSTEM}]},
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"responseMimeType": "application/json"},
    }
    obj = http(client, "POST", f"/v1beta/models/{client.model}:generateContent", body)
    text = response_text(obj)
    if not text:
        raise AIError(500, "empty reply")
    return text
