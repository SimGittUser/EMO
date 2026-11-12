"""The Gemini client when things go wrong, and its background worker."""

import time
from collections.abc import Generator
from typing import Any

import pytest

from emo import gemini
from emo.gemini import AIError, Gemini

from .mock_gemini import KEY, MockGemini


@pytest.fixture
def server() -> Generator[MockGemini]:
    mock = MockGemini()
    yield mock
    mock.shutdown()


def kind_of_failure(client: Gemini) -> str:
    with pytest.raises(AIError) as caught:
        gemini.ask_now(client, "hi")
    return caught.value.kind


def test_rate_limit_is_recognised(server: MockGemini) -> None:
    server.mode = "limit"
    assert kind_of_failure(Gemini(KEY, base=server.url, timeout=5)) == "limit"


def test_bad_key_is_recognised_and_not_retried_blindly(server: MockGemini) -> None:
    client = Gemini("wrong", base=server.url, timeout=5)
    assert kind_of_failure(client) == "key"
    assert client.rich is True


def test_unreachable_service_is_offline() -> None:
    assert kind_of_failure(Gemini(KEY, base="http://127.0.0.1:9", timeout=5)) == "offline"


def wait_for(client: Gemini, n: int) -> list[dict[str, Any]]:
    got: list[dict[str, Any]] = []
    deadline = time.time() + 8
    while len(got) < n and time.time() < deadline:
        got += gemini.poll(client)
        time.sleep(0.01)
    return got


def test_background_chat_and_reaction(server: MockGemini) -> None:
    client = Gemini(KEY, base=server.url, timeout=5)
    assert gemini.chat(client, 7, "state", [("Human", "hi")], "how are you?") is True
    first = wait_for(client, 1)[0]
    assert (first["kind"], first["tag"], first["ok"], first["emotion"]) == ("chat", 7, True, "joy")
    assert 'Your human says: "how are you?"' in server.seen[0][2]["input"]
    assert gemini.react(client, ("pat", 0.0), "state", "You were patted.") is True
    assert wait_for(client, 1)[0]["kind"] == "react"
    assert client.busy is False
