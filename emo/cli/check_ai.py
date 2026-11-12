"""`--check-ai`: one request to Gemini, and a plain report of how it went."""

from ..gemini import AIError, Gemini, ask_now, explain, load_key

NO_KEY = (
    "No API key found. Put  GEMINI_API_KEY=your-key  in a file named .env "
    "in this folder (see .env.example)."
)


def check_ai(model: str | None) -> int:
    """Return 0 if Gemini answered, 1 otherwise."""
    key = load_key()
    if not key:
        print(NO_KEY)
        return 1
    ai = Gemini(key, model=model)
    asked = ai.model
    print(f"Key found ({len(key)} characters, not shown). Asking {ai.model} ...")
    try:
        reply = ask_now(ai, 'Your human says: "hello". Reply as EMO.')
    except AIError as e:
        print("Not connected: " + explain(e.kind, e.message.replace(key, "<key>")))
        return 1
    print(f'Connected. EMO says: "{reply["say"]}"  (face: {reply["emotion"]})')
    if ai.model != asked:
        print(f"Note: {asked} was not available, so EMO is using {ai.model}.")
    return 0
