"""What EMO says when it has no AI to think with, plus a plain-English
description of each moment (which is what Gemini is told when it does).

Text is kept to plain ASCII so it will also fit a simple display font later.
"""

from .offline import offline_reply
from .pick import AI_WORTHY, LINES, describe, line

__all__ = ["AI_WORTHY", "LINES", "describe", "line", "offline_reply"]
