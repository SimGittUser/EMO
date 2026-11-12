"""Every face must render exactly as recorded."""

from typing import Any

import pytest

from emo import snapshot
from emo.expressions import AI_EMOTIONS, EXPRESSIONS, GALLERY

from .helpers import sha


@pytest.mark.parametrize("name", GALLERY)
def test_face_renders_as_recorded(name: str, golden: dict[str, Any]) -> None:
    assert sha(snapshot.render(name).rows) == golden["faces"][name]


def test_gallery_covers_every_expression() -> None:
    assert sorted(GALLERY) == sorted(EXPRESSIONS)
    assert len(GALLERY) == 45


def test_ai_emotions_are_real_faces() -> None:
    assert set(AI_EMOTIONS) <= set(EXPRESSIONS)


def test_sheet_writes_a_png(tmp_path: Any) -> None:
    path = tmp_path / "faces.png"
    assert snapshot.sheet(str(path), ["neutral", "love"], cols=2) == 2
    assert path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
