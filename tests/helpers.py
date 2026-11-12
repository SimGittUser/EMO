"""Small helpers shared by the tests."""

import hashlib


def sha(rows: list[list[int]]) -> str:
    """A short fingerprint of a canvas."""
    h = hashlib.sha256()
    for row in rows:
        h.update(repr(row).encode())
    return h.hexdigest()[:16]


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


class FakeTerm:
    """A terminal that records what is written to it."""

    def __init__(self, cols: int, rows: int) -> None:
        self.cols = cols
        self.rows = rows
        self.out: list[str] = []

    def size(self) -> tuple[int, int]:
        return self.cols, self.rows

    def write(self, s: str) -> None:
        self.out.append(s)
