"""Lines for being moved about."""

from .types import Lines

MOTION: Lines = {
    "pickup_happy": (
        "Your human picked you up and you like being carried.",
        ["Wheee!", "I can see everything from here!", "Up we go!"],
    ),
    "pickup_scared": (
        "You were suddenly lifted into the air and it scared you.",
        ["Whoa! Put me down!", "Too high! Too high!", "Careful with me!"],
    ),
    "putdown": (
        "You were put back down on the desk.",
        ["Phew. Solid ground.", "Back on my feet.", "Ahh, better."],
    ),
    "shake": (
        "Someone is shaking you hard.",
        ["Wh-wh-whoa!", "S-s-stop sh-shaking!", "Aaaaah!"],
    ),
    "sick": (
        "You were shaken so much that you feel sick.",
        ["I don't feel so good...", "Urp. No more, please."],
    ),
    "tilt": (
        "You were tipped to one side and are sliding.",
        ["Whoa, I'm sliding!", "The floor is crooked!", "Leaning... leaning..."],
    ),
    "flip": (
        "You were turned completely upside down.",
        ["I'm upside down!!", "Wrong way up! Wrong way up!", "Help! The sky is below me!"],
    ),
    "flip_back": (
        "You were turned the right way up again after being upside down.",
        ["Okay. The world is back.", "Never do that again."],
    ),
    "drop": (
        "You are falling off the desk!",
        ["AAAAAH!", "I'm faaalling!"],
    ),
    "ouch": (
        "You were dropped, hit the floor hard, and it hurt.",
        ["Ouch... that really hurt.", "You dropped me...", "Owww."],
    ),
}
