"""Conversation: sending what the human typed and showing the reply."""

from typing import Any

from .. import brain, gemini, phrases
from .state import App
from .talk import CPS, ai_usable, speak

MAX_HISTORY = 12


def reply(app: App, say: str, emotion: str, action: str) -> None:
    """EMO answers: words on screen, a face to match, maybe an action."""
    brain.set_thinking(app.brain, False)
    app.history.append(("EMO", say))
    del app.history[:-MAX_HISTORY]
    speak(app, say)
    app.you_until = app.speech_until
    brain.express(app.brain, emotion, len(say) / CPS + 2.0, action)


def send_chat(app: App, text: str) -> None:
    app.you = text
    app.you_until = app.now + 60.0
    app.history.append(("Human", text))
    del app.history[:-MAX_HISTORY]
    app.brain.boredom = 0.0
    brain.set_thinking(app.brain, True)
    if app.ai is not None and ai_usable(app):
        app.chat_tag += 1
        gemini.chat(app.ai, app.chat_tag, brain.describe(app.brain), app.history[:-1], text)
    else:
        say, emotion, action = phrases.offline_reply(app.rng, text, app.brain)
        app.later.append((app.now + 0.5, lambda: reply(app, say, emotion, action)))


def on_ai(app: App, res: dict[str, Any]) -> None:
    """Handle a finished AI request."""
    kind = res["error"] or "error"
    if not res["ok"]:
        app.ai_rest_until = app.now + (60.0 if kind == "limit" else 20.0)
    if res["kind"] == "chat":
        if res["tag"] != app.chat_tag:
            return
        if res["ok"]:
            reply(app, res["say"], res["emotion"], res["action"])
        else:
            key = "ai_" + (kind if kind in ("limit", "key") else "error")
            reply(app, phrases.line(app.rng, key), "confused", "none")
        return
    key, when = res["tag"]
    if app.now - when > 6.0:
        return  # too late to be a reaction
    speak(app, res["say"] if res["ok"] else phrases.line(app.rng, key))
