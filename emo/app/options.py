"""The settings the app is started with."""

from dataclasses import dataclass


@dataclass
class Options:
    color: str = "auto"  # 'auto', 'truecolor', '256' or 'mono'
    fps: int = 30
    no_mouse: bool = False
    no_glow: bool = False
    react_gap: float = 20.0  # minimum seconds between AI remarks on events
    demo: bool = False  # cycle through every face until a key is pressed
    seed: int | None = None
