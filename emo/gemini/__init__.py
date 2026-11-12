"""EMO's optional cloud brain: Google Gemini, over plain HTTPS (no SDK needed).

Requests run on a background thread so the face never freezes while waiting.
Each request is self-contained - the recent conversation travels inside the
prompt and nothing is stored on Google's side (``store: false``).

Talks to the Interactions API and falls back to the older generateContent
API if that is all the key / model supports.
"""

from .ask import ask_now, chat, poll, react
from .client import Gemini
from .errors import AIError, explain
from .key import load_key
from .parse import parse_reply

__all__ = [
    "AIError",
    "Gemini",
    "ask_now",
    "chat",
    "explain",
    "load_key",
    "parse_reply",
    "poll",
    "react",
]
