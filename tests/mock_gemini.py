"""A local stand-in for the Gemini service."""

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from .mock_replies import reply_for

KEY = "test-key"


class MockGemini(ThreadingHTTPServer):
    """Serves canned replies. ``mode`` picks how it misbehaves."""

    def __init__(self) -> None:
        super().__init__(("127.0.0.1", 0), Handler)
        self.mode = "ok"
        self.seen: list[tuple[str, str, dict[str, Any], dict[str, str]]] = []
        threading.Thread(target=self.serve_forever, daemon=True).start()

    @property
    def url(self) -> str:
        return f"http://127.0.0.1:{self.server_port}"


class Handler(BaseHTTPRequestHandler):
    def _mock(self) -> MockGemini:
        assert isinstance(self.server, MockGemini)
        return self.server

    def log_message(self, format: str, *args: Any) -> None:
        """Keep the test output quiet."""

    def _send(self, code: int, obj: dict[str, Any]) -> None:
        raw = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:
        self._mock().seen.append(("GET", self.path, {}, dict(self.headers)))
        names = ["gemini-3.8-flash", "gemini-3.5-flash-lite", "gemini-3.1-flash-image"]
        self._send(200, {"models": [{"name": "models/" + n} for n in names]})

    def do_POST(self) -> None:
        size = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(size) or b"{}")
        headers = {k.lower(): v for k, v in self.headers.items()}
        mock = self._mock()
        mock.seen.append(("POST", self.path, body, headers))
        self._send(*reply_for(mock.mode, self.path, body, headers.get("x-goog-api-key")))
