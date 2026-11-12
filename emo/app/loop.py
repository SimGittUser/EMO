"""The main loop."""

import time

from ..brain import Step, play
from ..brain.notes import say
from ..gemini import Gemini
from ..term import session
from .draw import draw
from .events import on_event
from .options import Options
from .state import App
from .tick import tick


def run(opts: Options, ai: Gemini | None = None) -> None:
    """Run EMO in the terminal until the human quits."""
    frame = 1.0 / max(5, min(60, opts.fps))
    with session(mouse=not opts.no_mouse) as term:
        app = App(opts, term, ai)
        last = nxt = time.monotonic()
        app.now = last
        play(app.brain, [Step("sleepy", 0.8), Step("happy", 1.6)])  # wake up, say hi
        say(app.brain, "hello")
        try:
            while app.running:
                for ev in term.poll(nxt - time.monotonic()):
                    on_event(app, ev)
                now = time.monotonic()
                if now < nxt:
                    continue
                dt = min(0.1, now - last)
                last = now
                nxt = max(nxt + frame, now)
                app.now = now
                tick(app, dt)
                draw(app)
        except KeyboardInterrupt:
            pass
