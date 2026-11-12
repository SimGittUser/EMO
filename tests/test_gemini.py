"""The Gemini client against a local mock: the normal path and every fallback."""

from collections.abc import Generator

import pytest

from emo import gemini
from emo.gemini import Gemini

from .mock_gemini import KEY, MockGemini


@pytest.fixture
def server() -> Generator[MockGemini]:
    mock = MockGemini()
    yield mock
    mock.shutdown()


def ask(server: MockGemini, mode: str, key: str = KEY) -> tuple[Gemini, dict[str, str]]:
    server.mode = mode
    client = Gemini(key, base=server.url, timeout=5)
    return client, gemini.ask_now(client, 'Your human says: "hi". Reply as EMO.')


def test_normal_request(server: MockGemini) -> None:
    _, reply = ask(server, "ok")
    assert reply == {"say": "Heard you!", "emotion": "joy", "action": "wink"}
    _, path, body, headers = server.seen[0]
    assert path == "/v1beta/interactions"
    assert body["model"] == "gemini-flash-lite-latest"
    assert body["store"] is False
    assert body["generation_config"] == {"thinking_level": "minimal"}
    assert body["response_format"]["schema"]["required"] == ["say", "emotion", "action"]
    assert headers["x-goog-api-key"] == KEY
    assert headers["api-revision"] == "2026-05-20"


def test_reply_wrapped_in_a_code_fence(server: MockGemini) -> None:
    assert ask(server, "fenced")[1]["say"] == "Heard you!"


def test_retries_without_extras_when_refused(server: MockGemini) -> None:
    client, reply = ask(server, "strict")
    assert reply["say"] == "Heard you!"
    assert client.rich is False
    assert len(server.seen) == 2


def test_falls_back_to_the_older_api(server: MockGemini) -> None:
    client, reply = ask(server, "legacy")
    assert reply == {"say": "Old API here.", "emotion": "smug", "action": "none"}
    assert client.api == "generate"


def test_finds_a_model_that_exists(server: MockGemini) -> None:
    client, reply = ask(server, "nomodel")
    assert reply["say"] == "Heard you!"
    assert client.model == "gemini-3.5-flash-lite"
