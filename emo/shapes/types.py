"""Shared type names for shapes."""

from collections.abc import Callable

# A signed distance function: how far a point is from a shape's edge, in
# pixels, negative when the point is inside.
type Sdf = Callable[[float, float], float]

# A straight eyelid: removes where a*x + b*y + c > 0.
type Line = tuple[float, float, float]

# A curved eyelid: removes the inside of the circle (x, y, radius).
type Disc = tuple[float, float, float]
