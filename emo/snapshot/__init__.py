"""Render faces to images - handy for checking them without a terminal.

    python3 -m emo --snapshot faces.png
"""

from .render import render
from .sheet import sheet

__all__ = ["render", "sheet"]
