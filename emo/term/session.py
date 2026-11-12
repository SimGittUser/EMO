"""Taking over the terminal for the app, and always handing it back."""

import io
import signal
import sys
import termios
import tty
from collections.abc import Generator
from contextlib import contextmanager

from .terminal import Terminal

MOUSE_ON = "\x1b[?1000h\x1b[?1002h\x1b[?1003h\x1b[?1006h"
MOUSE_OFF = "\x1b[?1006l\x1b[?1003l\x1b[?1002l\x1b[?1000l"
ENTER = "\x1b[?1049h\x1b[?25l\x1b[?7l\x1b[2J"  # alt screen, hide cursor, no wrap
LEAVE = "\x1b[0m\x1b[?7h\x1b[?25h\x1b[?1049l"


def _quit(*_: object) -> None:
    raise SystemExit(0)


@contextmanager
def session(mouse: bool = True) -> Generator[Terminal]:
    """A Terminal in raw mode on the alternate screen, restored on exit."""
    term = Terminal(mouse)
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    old = termios.tcgetattr(term.fd)
    tty.setcbreak(term.fd)
    mode = termios.tcgetattr(term.fd)
    mode[0] &= ~termios.IXON  # let Ctrl-S / Ctrl-Q through
    termios.tcsetattr(term.fd, termios.TCSANOW, mode)
    term.write(ENTER + (MOUSE_ON if mouse else ""))

    def on_resize(*_: object) -> None:
        term.resized = True

    handlers = {
        signal.SIGWINCH: signal.signal(signal.SIGWINCH, on_resize),
        signal.SIGTERM: signal.signal(signal.SIGTERM, _quit),
        signal.SIGHUP: signal.signal(signal.SIGHUP, _quit),
        signal.SIGTSTP: signal.signal(signal.SIGTSTP, signal.SIG_IGN),
    }
    try:
        yield term
    finally:
        for sig, handler in handlers.items():
            signal.signal(sig, handler)
        term.write((MOUSE_OFF if mouse else "") + LEAVE)
        termios.tcsetattr(term.fd, termios.TCSADRAIN, old)
