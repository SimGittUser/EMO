"""Things drawn on top of the eyes: highlights and blush."""

from .. import shapes
from ..canvas import Canvas, fill_sdf
from .draw_eye import Drawn
from .pose import Pose
from .state import Face
from .tuning import VH

SPOTS = ((-0.32, -0.38, 0.30), (0.30, 0.34, 0.15))  # x, y, radius, in eye halves
BLUSH = (255, 105, 150)


def draw_shine(canvas: Canvas, drawn: list[Drawn], amount: float) -> None:
    """Sparkly highlights, for amazed and pleading eyes."""
    a = min(1.0, amount)
    for d in drawn:
        for dx, dy, rr in SPOTS:
            spot = shapes.disc(d.pcx + dx * d.hw, d.pcy + dy * d.hh, rr * d.hw)
            fill_sdf(
                canvas, shapes.both(d.sdf, spot), d.pcx - d.ex, d.pcy - d.ey,
                d.pcx + d.ex, d.pcy + d.ey, (255, 255, 255), alpha=a,
            )


def draw_blush(face: Face, canvas: Canvas, pose: Pose, amount: float) -> None:
    """Pink patches just under the outer corners of the eyes."""
    a = min(1.0, amount) * 0.8
    S = pose.S
    for i, s in ((0, -1.0), (1, 1.0)):
        cx, cy, _, hh = face.geom[i]
        bx = pose.ox + (cx + s * 3.0) * S
        by = pose.oy + min(VH - 4.0, cy + hh + 5.5) * S
        patch = shapes.pill(bx, by, 6.0 * S, 2.3 * S)
        fill_sdf(
            canvas, patch, bx - 6.0 * S, by - 2.3 * S, bx + 6.0 * S, by + 2.3 * S,
            BLUSH, alpha=a,
        )
