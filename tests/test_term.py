"""Terminal encoding and input decoding must match the recording."""

from typing import Any

import pytest

from emo import snapshot
from emo.term import Pixels, clip, parse, pixel_row, styled, text_width, wrap

from .helpers import digest

RAW_INPUT = (
    "ab\x1b[A\x1b[1;5C\x1bOB\r\x7f\t\x04\x15\x17\x01Z\x1b[<0;10;5M\x1b[<0;10;5m"
    "\x1b[<35;3;4M\x1b[<32;7;8M\x1b[<64;1;1M\x1b[<65;1;1M\x1b[<2;9;9M\x1b[3~\x1bx"
    "\x1b\x1b[Zé\x1b"
)


@pytest.mark.parametrize("mode", ["truecolor", "256", "mono"])
def test_pixels_encode_as_recorded(mode: str, golden: dict[str, Any]) -> None:
    rows = snapshot.render("love").rows
    px = Pixels(mode)
    text = "".join(pixel_row(px, rows[2 * r], rows[2 * r + 1]) for r in range(24))
    assert digest(text) == golden["pixels"][mode]


def test_input_decodes_as_recorded(golden: dict[str, Any]) -> None:
    events, rest = parse(RAW_INPUT)
    assert [list(e) for e in events] == golden["parse"]
    assert rest == golden["parse_left"] == ""


def test_unfinished_sequence_waits_for_more(golden: dict[str, Any]) -> None:
    events, rest = parse("q\x1b[<0;1")
    assert [[list(e) for e in events], rest] == golden["parse_partial"]


def test_text_helpers(golden: dict[str, Any]) -> None:
    g = golden["text"]
    long = "the quick brown fox jumps over the lazy dog supercalifragilisticexpialidocious ok"
    assert wrap(long, 12) == g["wrap"]
    assert clip("héllo wörld 日本語", 9) == g["clip"]
    assert text_width("日本語 abc") == g["width"]
    parts = [("1;36", "EMO "), ("", "says hi"), ("2", " and more text")]
    assert styled(parts, 16) == g["styled"]
