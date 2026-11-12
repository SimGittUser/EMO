"""What can go wrong when asking Gemini, and how to say it plainly."""


class AIError(Exception):
    def __init__(self, code: int, message: str) -> None:
        super().__init__(message)
        self.code = code  # HTTP status, or 0 for network trouble
        self.message = message

    @property
    def kind(self) -> str:
        """One of 'limit', 'key', 'offline' or 'error'."""
        low = self.message.lower()
        if self.code == 429:
            return "limit"
        if self.code in (401, 403) or (self.code == 400 and "api key" in low):
            return "key"
        if self.code == 0:
            return "offline"
        return "error"


def explain(kind: str, detail: str = "") -> str:
    """Say what went wrong in plain words (for the status line and --check-ai)."""
    if kind == "key":
        return "Google rejected the API key - check the one in .env"
    if kind == "limit":
        return "the free quota is used up for the moment - it will come back"
    if kind == "offline":
        if "CERTIFICATE" in detail.upper():
            return f"this Python cannot verify HTTPS certificates ({detail[:80]})"
        return f"cannot reach Google - is the internet up? ({detail[:80]})"
    return detail[:120] or "unexpected reply from Gemini"
