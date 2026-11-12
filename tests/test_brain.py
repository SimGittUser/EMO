"""The brain must react to a long recorded session exactly as before."""

from typing import Any

import pytest

from emo import brain
from emo.brain import EVENTS, Brain

from .replay import replay


@pytest.fixture(scope="module")
def session(golden: dict[str, Any]) -> tuple[Brain, dict[str, Any]]:
    return replay(golden["script"])


def test_faces_and_speech_match(session: tuple[Brain, dict[str, Any]], golden: dict[str, Any]) -> None:
    _, got = session
    assert got["trace"] == golden["brain"]["trace"]
    assert got["said"] == golden["brain"]["said"]


def test_every_frame_matches(session: tuple[Brain, dict[str, Any]], golden: dict[str, Any]) -> None:
    assert session[1]["frames"] == golden["brain"]["frames"]


def test_moods_and_description_match(session: tuple[Brain, dict[str, Any]], golden: dict[str, Any]) -> None:
    mind, _ = session
    moods = [round(v, 6) for v in (mind.energy, mind.affection, mind.annoyance, mind.boredom)]
    assert moods == golden["brain"]["mood"]
    assert brain.describe(mind) == golden["brain"]["describe"]


def test_ai_reply_and_gallery_hooks(golden: dict[str, Any]) -> None:
    mind, _ = replay(golden["script"])
    brain.chat_started(mind)
    brain.set_thinking(mind, True)
    brain.set_thinking(mind, False)
    brain.express(mind, "love", 3, "dance")
    assert [mind.current, mind.music, brain.baseline(mind)] == golden["brain"]["after_express"]
    brain.pin(mind, "cool", 5)
    brain.update(mind, 1 / 30)
    assert mind.current == golden["brain"]["pinned"]


def test_unknown_event_is_refused(golden: dict[str, Any]) -> None:
    mind, _ = replay([])
    assert brain.event(mind, "teleport") is False
    assert len(EVENTS) == 17
