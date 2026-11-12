"""Running requests on a background thread so the face never freezes."""

import threading
from typing import Any

from .client import Gemini
from .errors import AIError
from .parse import parse_reply
from .request import request


def _answer(client: Gemini, kind: str, tag: Any, prompt: str) -> dict[str, Any]:
    res: dict[str, Any] = {"kind": kind, "tag": tag, "ok": False, "error": ""}
    try:
        res.update(parse_reply(request(client, prompt)))
        res["ok"] = bool(res["say"])
        if not res["ok"]:
            res["error"] = "error"
        client.problem = client.detail = ""
    except AIError as e:
        res["error"] = client.problem = e.kind
        client.detail = e.message[:160]
    return res


def _work(client: Gemini, kind: str, tag: Any, prompt: str) -> None:
    while True:
        client.results.put(_answer(client, kind, tag, prompt))
        with client.lock:
            nxt, client.waiting = client.waiting, None
            if nxt is None:
                client.busy = False
                return
        kind, tag, prompt = nxt


def submit(client: Gemini, kind: str, tag: Any, prompt: str, wait: bool) -> bool:
    """Start a request. If one is running, ``wait`` queues this one behind it;
    otherwise it is dropped and False is returned."""
    with client.lock:
        if client.busy:
            if not wait:
                return False
            client.waiting = (kind, tag, prompt)
            return True
        client.busy = True
    threading.Thread(target=_work, args=(client, kind, tag, prompt), daemon=True).start()
    return True
