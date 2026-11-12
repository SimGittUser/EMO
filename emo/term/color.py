"""Working out how many colours the terminal can show."""

import os
import platform

TRUECOLOR_APPS = (
    "iTerm.app", "WezTerm", "ghostty", "vscode", "Hyper", "Tabby",
    "WarpTerminal", "rio", "zed",
)
TRUECOLOR_TERMS = ("kitty", "ghostty", "alacritty", "wezterm", "foot", "direct")


def _modern_apple_terminal() -> bool:
    """Terminal.app gained 24-bit colour in macOS 26."""
    try:
        return int(platform.mac_ver()[0].split(".")[0]) >= 26
    except ValueError:
        return False


def detect_color() -> str:
    """Best guess at what the terminal can show: 'truecolor', '256' or 'mono'."""
    env = os.environ
    if env.get("NO_COLOR"):
        return "mono"
    ct = env.get("COLORTERM", "").lower()
    if "truecolor" in ct or "24bit" in ct:
        return "truecolor"
    term = env.get("TERM", "").lower()
    prog = env.get("TERM_PROGRAM", "")
    if prog in TRUECOLOR_APPS:
        return "truecolor"
    if any(k in term for k in TRUECOLOR_TERMS):
        return "truecolor"
    if prog == "Apple_Terminal" and _modern_apple_terminal():
        return "truecolor"
    if term in ("dumb", ""):
        return "mono"
    return "256"
