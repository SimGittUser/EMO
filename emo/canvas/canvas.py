"""The framebuffer itself: rows of packed 0xRRGGBB pixels on a black background."""


class Canvas:
    def __init__(self, w: int, h: int) -> None:
        self.w = 1
        self.h = 1
        self.rows: list[list[int]] = []
        self._blank: list[int] = []
        self._dy0 = 0
        self._dy1 = 0
        self.resize(w, h)

    def resize(self, w: int, h: int) -> None:
        self.w = max(1, int(w))
        self.h = max(1, int(h))
        self._blank = [0] * self.w
        self.rows = [[0] * self.w for _ in range(self.h)]
        self._dy0 = self.h
        self._dy1 = 0

    def clear(self) -> None:
        """Blank only the rows that were drawn on since the last clear."""
        if self._dy1 > self._dy0:
            blank = self._blank
            rows = self.rows
            for y in range(self._dy0, self._dy1):
                rows[y][:] = blank
        self._dy0 = self.h
        self._dy1 = 0

    def touch(self, y0: int, y1: int) -> None:
        """Remember that rows y0..y1 now hold something."""
        self._dy0 = min(self._dy0, y0)
        self._dy1 = max(self._dy1, y1)
