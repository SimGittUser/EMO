"""Shared fixtures.

``golden.json`` is a recording of what EMO did before it was split into
small modules. The tests replay the same inputs and expect the same output.
"""

import json
from pathlib import Path
from typing import Any

import pytest


@pytest.fixture(scope="session")
def golden() -> dict[str, Any]:
    return json.loads((Path(__file__).parent / "golden.json").read_text(encoding="utf-8"))
