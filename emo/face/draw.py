"""Drawing the whole face onto a canvas."""

from ..canvas import Canvas
from .draw_eye import draw_eye
from .extras import draw_blush, draw_shine
from .pose import face_pose
from .shades import draw_shades
from .state import Face


def draw(face: Face, canvas: Canvas) -> None:
    pose = face_pose(face, canvas)
    drawn = [draw_eye(face, canvas, pose, i, s) for i, s in ((0, -1.0), (1, 1.0))]
    f = face.f.cur
    if f["shine"] > 0.03:
        draw_shine(canvas, drawn, f["shine"])
    if f["bridge"] > 0.03:
        draw_shades(face, canvas, pose, drawn, f["bridge"])
    if f["blush"] > 0.03:
        draw_blush(face, canvas, pose, f["blush"])


def hit_eye(face: Face, vx: float, vy: float) -> int | None:
    """Which eye (0 / 1) is at this virtual-screen point, or None."""
    for i, (cx, cy, hw, hh) in enumerate(face.geom):
        if abs(vx - cx) <= hw + 2.0 and abs(vy - cy) <= max(hh, 5.0) + 2.0:
            return i
    return None
