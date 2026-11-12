"""Picking a model that exists when the configured one does not."""

from .client import Gemini
from .errors import AIError
from .http import http

NOT_FOR_CHAT = ("image", "tts", "audio", "live", "embed", "omni")


def discover_model(client: Gemini) -> bool:
    """Switch to the best available Flash model. True if the model changed."""
    try:
        obj = http(client, "GET", "/v1beta/models?pageSize=200")
    except AIError:
        return False
    best = None
    for m in obj.get("models") or []:
        name = str(m.get("name", "")).split("/")[-1]
        methods = m.get("supportedGenerationMethods")
        if "flash" not in name or (methods and "generateContent" not in methods):
            continue
        if any(bad in name for bad in NOT_FOR_CHAT):
            continue
        # prefer the lighter models, then stable ones, then the newest name
        score = ("lite" in name, "preview" not in name and "exp" not in name, name)
        if best is None or score > best[0]:
            best = (score, name)
    if best is None or best[1] == client.model:
        return False
    client.model = best[1]
    return True
