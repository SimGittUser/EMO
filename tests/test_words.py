"""What EMO says offline, and how AI replies are read."""

from random import Random
from typing import Any

from emo import phrases
from emo.brain import Brain
from emo.effects import Effects
from emo.face import Face
from emo.gemini import explain, parse_reply
from emo.gemini.texts import response_text

QUESTIONS = [
    "hello!", "tell me a joke", "i love you", "you are stupid", "can you dance?",
    "what is 2+2?", "go to sleep", "how are you", "wink at me", "sorry", "thanks",
    "what is your name", "bye", "boo", "so smart", "cool", "blah blah", "good night",
    "good robot",
]

REPLIES = [
    "just plain words",
    '{"say": "Hi — I’m EMO…", "emotion": "Excited", "action": "fly"}',
    'Sure!\n```json\n{"say":"ok  there","emotion":"smug","action":"wink"}\n```',
    '{"say": 5}',
]

RESPONSES: list[dict[str, Any]] = [
    {"steps": [{"type": "thought", "text": "x"}, {"type": "model_output", "content": [{"type": "text", "text": "A"}]}]},
    {"outputs": [{"type": "text", "text": "B"}]},
    {"candidates": [{"content": {"parts": [{"text": "t", "thought": True}, {"text": "C"}]}}]},
    {},
]


def test_offline_chat(golden: dict[str, Any]) -> None:
    r = Random(1)
    mind = Brain(Face(r), Effects(r), r)
    got = [list(phrases.offline_reply(r, q, mind)) for q in QUESTIONS]
    assert got == golden["offline"]


def test_canned_lines(golden: dict[str, Any]) -> None:
    keys = sorted(phrases.LINES)
    assert [phrases.line(Random(2), k) for k in keys] == golden["lines"]
    assert [phrases.describe(k) for k in keys] == golden["describe_keys"]
    assert phrases.AI_WORTHY <= set(keys)


def test_ai_replies_are_read_forgivingly(golden: dict[str, Any]) -> None:
    assert [parse_reply(x) for x in REPLIES] == golden["parse_reply"]
    assert [response_text(x) for x in RESPONSES] == golden["texts"]


def test_errors_are_explained(golden: dict[str, Any]) -> None:
    cases = [("key", ""), ("limit", ""), ("offline", "CERTIFICATE_VERIFY_FAILED x"),
             ("offline", "no route"), ("error", ""), ("error", "boom")]
    assert [explain(k, d) for k, d in cases] == golden["explain"]
