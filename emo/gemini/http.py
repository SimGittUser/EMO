"""One HTTP request to the Gemini service."""

import json
import urllib.error
import urllib.request
from typing import Any

from .client import Gemini
from .errors import AIError
from .tls import tls_context


def _error_message(raw: str) -> str:
    """The human-readable part of an error response body."""
    try:
        err = json.loads(raw).get("error")
    except (ValueError, AttributeError):
        return raw[:300]
    if isinstance(err, dict):
        return str(err.get("message") or err.get("status") or raw[:300])
    return raw[:300]


def http(
    client: Gemini,
    method: str,
    path: str,
    body: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Send a request and return the decoded JSON, or raise AIError."""
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(client.base + path, method=method, data=data)
    req.add_header("x-goog-api-key", client.key)
    req.add_header("Content-Type", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        if client.tls is None:
            client.tls = tls_context()
        with urllib.request.urlopen(req, timeout=client.timeout, context=client.tls) as resp:
            return json.loads(resp.read().decode("utf-8", "replace") or "{}")
    except urllib.error.HTTPError as e:
        raise AIError(e.code, _error_message(e.read().decode("utf-8", "replace"))) from None
    except (urllib.error.URLError, OSError, ValueError) as e:
        raise AIError(0, str(getattr(e, "reason", e))) from None
