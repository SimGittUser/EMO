"""One beat of a scripted reaction."""

from collections.abc import Callable
from typing import NamedTuple

type Callback = Callable[[], object]


class Step(NamedTuple):
    """Show ``face`` for ``seconds``; ``then`` runs as the step begins."""

    face: str
    seconds: float
    then: Callback | None = None
