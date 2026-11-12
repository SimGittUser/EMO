"""Switching the face to a named expression."""

from ..expressions import ANIMS, EXPRESSIONS, EYE_DEFAULTS, FACE_DEFAULTS
from .state import Face


def _face_targets(face: Face) -> dict[str, float]:
    e = face.expr
    ft = dict(FACE_DEFAULTS)
    settings = dict(e.get("face", {}))
    color = settings.pop("color", None)
    if color:
        ft["cr"], ft["cg"], ft["cb"] = (float(c) for c in color)
    ft.update(settings)
    anim = e.get("anim", {})
    for a in ANIMS:
        if a in anim:
            ft[a], face.hz[a] = float(anim[a][0]), float(anim[a][1])
        else:
            ft[a] = 0.0
    ft["lx"], ft["ly"] = face.f.tgt["lx"], face.f.tgt["ly"]
    return ft


def set_expression(face: Face, name: str) -> None:
    """Aim every spring at the named expression; the face flows into it."""
    if name not in EXPRESSIONS:
        name = "neutral"
    e = EXPRESSIONS[name]
    face.name = name
    face.expr = e
    face.speed = e.get("speed", 1.0)
    for i, side in enumerate(("left", "right")):
        t = dict(EYE_DEFAULTS)
        t.update(e.get("eyes", {}))
        t.update(e.get(side, {}))
        t["mix"] = face.eyes[i].tgt["mix"]  # the morph is driven in update()
        face.eyes[i].tgt.update((k, float(v)) for k, v in t.items())
        face.want_shape[i] = e.get("shape")
    face.f.tgt.update(_face_targets(face))
    face.gaze_mode = e.get("gaze", "wander")
    face.gaze_fixed = e.get("look", (0.0, 0.0))
    face.gaze_timer = 0.0
    face.blink_every = e.get("blink", 3.6)
    face.blink_dur = e.get("blink_dur", 0.26)
    if face.blink_every:
        face.blink_timer = min(face.blink_timer, face.blink_every)
