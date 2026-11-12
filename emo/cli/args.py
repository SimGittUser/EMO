"""The command line."""

import argparse


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="python3 -m emo",
        description="EMO - a tiny desktop pet robot face that lives in your terminal.",
    )
    p.add_argument(
        "--color",
        choices=("auto", "truecolor", "256", "mono"),
        default="auto",
        help="colour depth (mono previews a 1-bit OLED)",
    )
    p.add_argument("--fps", type=int, default=30, help="frames per second (default 30)")
    p.add_argument("--no-mouse", action="store_true", help="don't capture the mouse")
    p.add_argument("--no-glow", action="store_true", help="draw the eyes without their halo")
    p.add_argument("--no-ai", action="store_true", help="never contact Gemini")
    p.add_argument("--model", help="Gemini model id (default: gemini-flash-lite-latest)")
    p.add_argument(
        "--react-gap",
        type=float,
        default=20.0,
        metavar="SECONDS",
        help="minimum seconds between AI reactions to touch/motion (default 20)",
    )
    p.add_argument(
        "--check-ai",
        action="store_true",
        help="test the Gemini connection, say what is wrong, and exit",
    )
    p.add_argument("--demo", action="store_true", help="cycle through every face")
    p.add_argument("--faces", action="store_true", help="list the faces and exit")
    p.add_argument("--snapshot", metavar="FILE.png", help="save every face to an image and exit")
    p.add_argument("--seed", type=int, help=argparse.SUPPRESS)
    return p.parse_args(argv)
