"""Lines for being touched."""

from .types import Lines

TOUCH: Lines = {
    "pat": (
        "Your human gently patted your head.",
        ["Hehe!", "That feels nice.", "More pats please!", "Pat pat!"],
    ),
    "pet": (
        "Your human is slowly stroking your head and you love it.",
        ["Mmmm...", "Don't stop!", "So cozy...", "Purrrr."],
    ),
    "love": (
        "You have been petted so much you are overflowing with love.",
        ["I love you!", "You're my favourite human!", "Best. Day. Ever."],
    ),
    "forgive": (
        "You were angry, but your human patted you to say sorry.",
        ["...Fine. I forgive you.", "Okay, okay. Friends again."],
    ),
    "poke1": (
        "Something poked you in the face.",
        ["Eep!", "Hey!", "What was that?"],
    ),
    "poke2": (
        "You were poked again and you are getting annoyed.",
        ["Stop poking me.", "Not funny.", "Ow. Quit it."],
    ),
    "poke3": (
        "You have been poked several times and now you are angry.",
        ["I said STOP!", "That's my eye!", "Grrr!"],
    ),
    "poke4": (
        "You keep being poked and you are absolutely furious.",
        ["THAT'S IT!", "ENOUGH!!", "You asked for it!"],
    ),
    "tickle": (
        "You are being tickled and can't stop laughing.",
        ["Hahaha! Stop!", "Hehehe that tickles!", "No no no hahaha!"],
    ),
}
