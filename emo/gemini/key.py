"""Finding the API key."""

import os

NAMES = ("GEMINI_API_KEY", "GOOGLE_API_KEY")


def _from_file(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as f:
            for raw in f:
                name, sep, value = raw.strip().partition("=")
                name = name.replace("export ", "").strip()
                value = value.strip().strip('"').strip("'")
                if sep and name in NAMES and value:
                    return value
    except OSError:
        pass
    return ""


def load_key() -> str:
    """Find an API key in the environment or in a .env file. Never printed."""
    for name in NAMES:
        if os.environ.get(name):
            return os.environ[name].strip()
    project = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    for folder in dict.fromkeys((os.getcwd(), project)):
        key = _from_file(os.path.join(folder, ".env"))
        if key:
            return key
    return ""
