"""Lines for sounds, light, and the start of the day."""

from .types import Lines

WORLD: Lines = {
    "hello": (
        "You just woke up and noticed your human.",
        ["Hi! I'm EMO!", "Oh! Hello there!", "Beep boop. Hi!"],
    ),
    "loud": (
        "There was a sudden loud bang.",
        ["What was THAT?!", "Too loud!", "Eek!"],
    ),
    "clap": (
        "Your human clapped to get your attention.",
        ["Oh! Applause!", "Yes? You called?", "Clap clap!"],
    ),
    "music_on": (
        "Music started playing and you want to dance.",
        ["Ooh, I love this song!", "Dance time!", "Music!"],
    ),
    "music_off": (
        "The music stopped.",
        ["Aww, it stopped.", "One more song?"],
    ),
    "dark": (
        "The lights just went out.",
        ["Who turned off the lights?", "It's dark... sleepy time?"],
    ),
    "light": (
        "The lights suddenly came on.",
        ["Too bright!", "Ah! My eyes!", "Morning already?"],
    ),
    "ai_error": ("", ["My thinking cloud is fuzzy right now.", "I can't reach my brain cloud..."]),
    "ai_limit": ("", ["My brain needs a rest. Ask me again in a bit!"]),
    "ai_key": ("", ["My brain key doesn't seem to work..."]),
}
