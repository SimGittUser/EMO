"""Signed distance functions for EMO's eye shapes.

Every shape works in canvas pixels and answers "how far is this point from
my edge" (negative = inside). Describing shapes by distance rather than by
pixels gives smooth edges at any size, and morphing for free: blending two
distances blends two shapes.
"""

from .basic import band, both, disc, pill
from .chevron import chevron
from .cross import cross
from .eye import eye
from .heart import heart
from .spiral import spiral

__all__ = ["band", "both", "chevron", "cross", "disc", "eye", "heart", "pill", "spiral"]
