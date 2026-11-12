"""Deciding what `python3 -m emo` should do."""

import sys

from .. import snapshot
from ..app import Options, run
from ..expressions import GALLERY
from ..gemini import Gemini, load_key
from .args import parse_args
from .check_ai import check_ai


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.faces:
        print("\n".join(GALLERY))
        return 0
    if args.snapshot:
        n = snapshot.sheet(args.snapshot)
        print(f"saved {n} faces to {args.snapshot}")
        return 0
    if args.check_ai:
        return check_ai(args.model)
    if not (sys.stdin.isatty() and sys.stdout.isatty()):
        print("EMO needs an interactive terminal. Run:  python3 -m emo", file=sys.stderr)
        return 2

    key = "" if args.no_ai else load_key()
    ai = Gemini(key, model=args.model) if key else None
    opts = Options(
        color=args.color,
        fps=args.fps,
        no_mouse=args.no_mouse,
        no_glow=args.no_glow,
        react_gap=args.react_gap,
        demo=args.demo,
        seed=args.seed,
    )
    run(opts, ai)
    print("EMO went to sleep. Bye!")
    return 0
