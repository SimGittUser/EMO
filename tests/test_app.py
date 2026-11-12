"""The whole app must put exactly the recorded bytes on screen."""

from typing import Any

import pytest

from emo.app import App, Options, draw, on_event

from .drive import drive
from .helpers import FakeTerm

CASES = [("truecolor", 100, 34), ("256", 80, 24), ("mono", 60, 20)]


@pytest.mark.parametrize(("color", "cols", "rows"), CASES)
def test_session_matches_recording(color: str, cols: int, rows: int, golden: dict[str, Any]) -> None:
    want = golden["app"][f"{color}_{cols}x{rows}"]
    got = drive(color, cols, rows, golden["app_events"])
    assert got["texts"] == want["texts"]
    assert got["out"] == want["out"]


def test_tiny_window_matches_recording(golden: dict[str, Any]) -> None:
    keys_only = {
        frame: [e for e in events if e[0] != "mouse"]
        for frame, events in golden["app_events"].items()
    }
    assert drive("truecolor", 20, 6, keys_only) == golden["app"]["truecolor_20x6"]


def test_mouse_in_a_tiny_window_is_ignored() -> None:
    """This used to crash: there is no face panel to click on."""
    app = App(Options(seed=1, color="mono"), FakeTerm(20, 6))
    draw(app)
    on_event(app, ("mouse", "press", 3, 3, 0))
    on_event(app, ("mouse", "release", 3, 3, 0))
    assert app.brain.current == "neutral"
