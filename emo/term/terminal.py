"""The terminal as an input and output device."""

import codecs
import os
import select
import shutil
import sys

from .keys import Event
from .parse import parse


class Terminal:
    def __init__(self, mouse: bool = True) -> None:
        self.fd = sys.stdin.fileno()
        self.mouse = mouse
        self.resized = True
        self.buf = ""
        self.decode = codecs.getincrementaldecoder("utf-8")("replace")

    def size(self) -> tuple[int, int]:
        """Columns and rows."""
        s = shutil.get_terminal_size((80, 24))
        return s.columns, s.lines

    def write(self, s: str) -> None:
        sys.stdout.write(s)
        sys.stdout.flush()

    def poll(self, timeout: float) -> list[Event]:
        """Wait up to ``timeout`` seconds and return whatever input arrived."""
        events: list[Event] = []
        ready, _, _ = select.select([self.fd], [], [], max(0.0, timeout))
        if ready:
            data = os.read(self.fd, 4096)
            if not data:
                events.append(("eof",))
            else:
                found, self.buf = parse(self.buf + self.decode.decode(data))
                events.extend(found)
        if self.resized:
            self.resized = False
            events.append(("resize",))
        return events
