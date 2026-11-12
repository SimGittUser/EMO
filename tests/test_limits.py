"""AGENTS.md rule 9: every file and every function fits on one sheet of paper."""

import ast
from pathlib import Path

ROOT = Path(__file__).parent.parent
LIMIT = 60
SOURCES = sorted([*(ROOT / "emo").rglob("*.py"), *(ROOT / "tests").rglob("*.py")])


def test_no_file_is_longer_than_a_page() -> None:
    long = {str(p.relative_to(ROOT)): n for p in SOURCES if (n := len(p.read_text().splitlines())) > LIMIT}
    assert long == {}


def test_no_function_is_longer_than_a_page() -> None:
    long = {}
    for path in SOURCES:
        for node in ast.walk(ast.parse(path.read_text())):
            if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
                lines = (node.end_lineno or node.lineno) - node.lineno + 1
                if lines > LIMIT:
                    long[f"{path.relative_to(ROOT)}:{node.name}"] = lines
    assert long == {}


def test_no_checks_are_silenced() -> None:
    banned = ("# no" + "qa", "# type" + ": ignore", "pytest.mark." + "skip", "x" + "fail")
    hits = [str(p.relative_to(ROOT)) for p in SOURCES if any(b in p.read_text() for b in banned)]
    assert hits == []
