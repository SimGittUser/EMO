"""Getting an answer one way or another: retries and fallbacks."""

from .apis import generate, interactions
from .client import Gemini
from .discover import discover_model
from .errors import AIError

ENDPOINT_MISSING = (404, 405, 501)


def _try_apis(client: Gemini, prompt: str) -> str:
    if client.api != "interactions":
        return generate(client, prompt)
    try:
        return interactions(client, prompt, client.rich)
    except AIError as e:
        if e.code == 400 and client.rich and e.kind != "key":
            out = interactions(client, prompt, False)  # retry, bare minimum
            client.rich = False
            return out
        if e.code not in ENDPOINT_MISSING:
            raise
        first = e
    try:
        out = generate(client, prompt)
    except AIError as e:
        raise (first if e.code == 404 else e) from None
    client.api = "generate"
    return out


def request(client: Gemini, prompt: str) -> str:
    """Return the model's raw reply to ``prompt``, or raise AIError.

    If the configured model is unknown, look for one that exists and retry.
    """
    try:
        return _try_apis(client, prompt)
    except AIError as e:
        if e.code != 404 or not discover_model(client):
            raise
    return _try_apis(client, prompt)
