"""Where overlays go relative to the eyes, and how sprites get drawn there."""

from typing import NamedTuple

from ..canvas import Canvas, blit
from ..canvas.blit import Sprite
from ..canvas.sdf_row import Rgb
from ..face import VW, Face


class Anchors(NamedTuple):
    mx: float  # midway between the eyes
    top: float  # the top of the higher eye
    corner_x: float  # the spot up and to the right of the eyes
    corner_y: float


def anchors(face: Face) -> Anchors:
    (lx, ly, _, lhh), (rx, ry, rhw, rhh) = face.geom
    top = min(ly - lhh, ry - rhh)
    return Anchors(
        (lx + rx) / 2.0,
        top,
        min(VW - 9.0, rx + rhw + 11.0),
        max(7.0, top - 4.0),
    )


def draw_sprite(
    canvas: Canvas,
    face: Face,
    sprite: Sprite,
    x: float,
    y: float,
    size: float,
    color: Rgb,
    alpha: float = 1.0,
) -> None:
    """Draw a sprite centred on virtual-screen point (x, y)."""
    S, ox, oy = face.view
    px = max(1, int(size * S + 0.5))
    w = len(sprite[0]) * px
    h = len(sprite) * px
    blit(canvas, sprite, ox + x * S - w / 2.0, oy + y * S - h / 2.0, px, color, alpha)
