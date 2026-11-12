"""The state of one connection to Gemini."""

import os
import queue
import ssl
import threading
from typing import Any

from .prompt import DEFAULT_BASE, DEFAULT_MODEL

# A request waiting its turn: (kind, tag, prompt).
type Job = tuple[str, Any, str]


class Gemini:
    def __init__(
        self,
        key: str,
        model: str | None = None,
        base: str | None = None,
        timeout: float = 20.0,
    ) -> None:
        self.key = key
        self.model = model or os.environ.get("EMO_GEMINI_MODEL") or DEFAULT_MODEL
        self.base = (base or os.environ.get("EMO_GEMINI_URL") or DEFAULT_BASE).rstrip("/")
        self.timeout = timeout
        self.api = "interactions"  # falls back to "generate" if need be
        self.rich = True  # send schema + thinking hints until refused
        self.busy = False
        self.problem = ""  # '', 'limit', 'key', 'offline', 'error'
        self.detail = ""
        self.results: queue.Queue[dict[str, Any]] = queue.Queue()
        self.waiting: Job | None = None  # a chat that arrived while busy
        self.lock = threading.Lock()
        self.tls: ssl.SSLContext | None = None
