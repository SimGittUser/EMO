"""What EMO asks Gemini: chat replies and reactions to events."""

import queue
from typing import Any

from .client import Gemini
from .parse import parse_reply
from .request import request
from .worker import submit


def chat(client: Gemini, tag: Any, state: str, history: list[tuple[str, str]], text: str) -> bool:
    """Ask for a reply to what the human typed. Always answered eventually."""
    lines = [state, ""]
    if history:
        lines.append("Conversation so far:")
        lines += [f"{who}: {said}" for who, said in history]
        lines.append("")
    lines.append(f'Your human says: "{text}"')
    lines.append("Reply as EMO.")
    return submit(client, "chat", tag, "\n".join(lines), wait=True)


def react(client: Gemini, tag: Any, state: str, happened: str) -> bool:
    """Ask for a remark about something that just happened; dropped if busy."""
    prompt = f"{state}\n\nSomething just happened: {happened}\nReact out loud as EMO, in 8 words or fewer."
    return submit(client, "react", tag, prompt, wait=False)


def ask_now(client: Gemini, prompt: str) -> dict[str, str]:
    """One blocking request; returns the parsed reply or raises AIError."""
    return parse_reply(request(client, prompt))


def poll(client: Gemini) -> list[dict[str, Any]]:
    """Finished requests: dicts with kind, tag, ok, say, emotion, action, error."""
    out = []
    while True:
        try:
            out.append(client.results.get_nowait())
        except queue.Empty:
            return out
