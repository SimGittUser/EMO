"""A 3 x 5 pixel font, just big enough to label faces in a snapshot."""

from ..canvas import Canvas, blit

# Each letter is five rows of three bits, top to bottom.
FONT = {
    "a": "010101111101101", "b": "110101110101110", "c": "011100100100011",
    "d": "110101101101110", "e": "111100110100111", "f": "111100110100100",
    "g": "011100101101011", "h": "101101111101101", "i": "111010010010111",
    "j": "001001001101010", "k": "101101110101101", "l": "100100100100111",
    "m": "101111111101101", "n": "110101101101101", "o": "010101101101010",
    "p": "110101110100100", "q": "010101101110011", "r": "110101110101101",
    "s": "011100010001110", "t": "111010010010010", "u": "101101101101111",
    "v": "101101101101010", "w": "101101111111101", "x": "101101010101101",
    "y": "101101010010010", "z": "111001010100111", "_": "000000000000111",
}

LABEL_GREY = (150, 150, 160)


def draw_label(canvas: Canvas, text: str, x: int, y: int) -> None:
    for ch in text.lower():
        bits = FONT.get(ch)
        if bits:
            rows = (bits[i : i + 3] for i in range(0, 15, 3))
            sprite = tuple(row.replace("1", "#").replace("0", ".") for row in rows)
            blit(canvas, sprite, x, y, 1, LABEL_GREY)
        x += 4
