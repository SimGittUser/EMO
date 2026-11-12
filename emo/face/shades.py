"""Sunglasses: a bridge between the eyes and a glint sweeping across."""

from .. import shapes
from ..canvas import Canvas, fill_sdf
from .draw_eye import Drawn
from .pose import Pose
from .state import Face

GLINT = (60, 150, 255)


def draw_shades(face: Face, canvas: Canvas, pose: Pose, drawn: list[Drawn], amount: float) -> None:
    a = min(1.0, amount)
    S = pose.S
    left, right = drawn
    yb = (left.pcy - left.hh + right.pcy - right.hh) / 2.0 + 0.36 * (left.hh + right.hh)
    bridge = shapes.pill(
        (left.pcx + right.pcx) / 2.0, yb, (right.pcx - left.pcx) / 2.0, max(0.8, 1.3 * S)
    )
    fill_sdf(
        canvas, bridge, left.pcx, yb - 2.0 * S, right.pcx, yb + 2.0 * S, pose.color, alpha=a
    )
    if not face.expr.get("glint"):
        return
    u = (face.t % 2.6) / 0.7
    if u >= 1.0:
        return
    for d in drawn:
        stripe = shapes.band(d.pcx + (u * 2.0 - 1.0) * d.hw * 1.9, d.pcy, 0.8, 0.6, d.hw * 0.16)
        fill_sdf(
            canvas, shapes.both(d.sdf, stripe), d.pcx - d.ex, d.pcy - d.ey,
            d.pcx + d.ex, d.pcy + d.ey, GLINT, alpha=0.85 * a,
        )
