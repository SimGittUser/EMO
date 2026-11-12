"""The shape of the screen: which rows and columns hold what."""

from typing import NamedTuple


class Layout(NamedTuple):
    small: bool  # the window is too small to draw in
    cols: int
    ph: int = 0  # the face panel: height and width in cells
    pw: int = 0
    px0: int = 0  # the panel's left margin and first row
    py0: int = 2
    speech: int = 0  # first of the three speech rows
    input: int = 0  # the input / hint row
    helps: tuple[str, ...] = ()  # the key list, ready to print
    help_row: int = 0

    @property
    def help(self) -> bool:
        return bool(self.helps)
