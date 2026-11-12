"""Lines for EMO's own states: sleep, boredom, hunger."""

from .types import Lines

MOODS: Lines = {
    "sleep": (
        "You are falling asleep.",
        ["Goodnight...", "So sleepy... zzz", "Just five minutes..."],
    ),
    "wake": (
        "You just woke up from a nice nap.",
        ["Good morning!", "*yawn* I'm up!", "Did I miss anything?"],
    ),
    "wake_rude": (
        "You were rudely woken up while sleeping.",
        ["Hey! I was sleeping!", "Rude!", "Huh?! What?!"],
    ),
    "bored": (
        "Nobody has played with you for a while and you are bored.",
        ["I'm bored...", "*sigh*", "Nothing to do..."],
    ),
    "lonely": (
        "You have been ignored for a long time and want attention.",
        ["Play with me?", "Hello? Anyone there?", "Pat me, please?"],
    ),
    "hungry": (
        "Your battery is running low.",
        ["My battery is low...", "Feed me electricity!", "Need... charge..."],
    ),
    "charged": (
        "You were just plugged in and your battery is full.",
        ["Fully charged!", "Yum, electricity!", "I feel alive!"],
    ),
    "hum": (
        "You are happily humming a tune to yourself.",
        ["La la la~", "Doo dee doo~", "Hmm hmm hmm~"],
    ),
    "yawn": (
        "You are getting tired and yawned.",
        ["*yaaawn*", "So tired..."],
    ),
}
