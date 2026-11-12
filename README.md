# EMO

A tiny desktop pet robot face that lives in your terminal. It blinks, looks
around, gets bored, falls asleep, and reacts when you touch it, pick it up,
shake it, drop it, make noise or turn off the lights. With a free Gemini API
key it can also talk back.

Pure Python standard library — nothing to install.

## Run it

```bash
python3 -m emo
```

Works best in a terminal with 24-bit colour (iTerm2, Ghostty, kitty, WezTerm,
VS Code, recent macOS Terminal) at 80×24 or larger. Bigger window = bigger face.

## Controls

The keyboard and mouse stand in for the sensors a real robot would have.

| Sensor | Key | What happens |
| --- | --- | --- |
| Touch | `p` or `space` | pat — happy; several in a row → content → love |
| | `s` (hold) | stroke — closes its eyes and purrs; keep going for heart eyes |
| | `o` | poke — surprised → annoyed → angry → furious |
| | `t` (hold) | tickle — giggles, then laughs |
| Motion | `u` | pick up / put down |
| | `k` | shake — dizzy; too much and it feels sick |
| | `←` `→` | tilt (eyes slide downhill), `↓` to level |
| | `f` | flip upside down / back |
| | `d` | drop — falls, hits the floor, sees stars |
| Sound | `l` | loud bang |
| | `c` | clap (twice quickly = dance) |
| | `m` | music on / off |
| Light | `n` | lights off / on — it dozes off in the dark |
| Power | `b` | charge the battery |
| | `z` | sleep / wake |

**Mouse:** move = it watches the pointer · click = pat · click an eye = poke ·
drag across the face = stroke · scroll wheel = tickle.

**Other:** `Enter` talk to EMO (`Esc` to go back) · `[` `]` browse all 45 faces ·
`h` show/hide keys · `q` quit.

Leave it alone and it gets bored, asks for attention, and eventually naps.
Being nice raises its affection; poking and dropping it does the opposite, and
that changes how it reacts later (a robot that likes you enjoys being picked up).

## Talking with Gemini

Without a key EMO still chats, using a small built-in set of replies.
To give it a real brain:

1. Get a free key at <https://aistudio.google.com/apikey>.
2. Copy `.env.example` to `.env` and paste the key after `GEMINI_API_KEY=`
   (or export `GEMINI_API_KEY` in your shell).
3. Run `python3 -m emo` — the top-right corner shows the model in use.

Gemini picks both the words and the face for each reply, knows EMO's current
mood and what just happened to it, and can make it wink, dance or go to sleep
when you ask. It also adds a short remark to the bigger moments (being picked
up, dropped, woken up…), at most once every 20 seconds so the free quota lasts
(`--react-gap` changes that). Reactions on the face itself never wait for the
network.

If the corner says the AI is unreachable, run `python3 -m emo --check-ai` — it
makes one request and tells you plainly what is wrong.

Good to know: on the free tier Google may use what you send to improve its
products, so don't type anything private. Requests are sent with `store: false`
and the key is only ever read from your environment or `.env`.

## Options

```
--color truecolor|256|mono   colour depth; mono previews a 1-bit OLED
--fps N                      frame rate (default 30)
--no-mouse                   leave the mouse alone (keeps text selection)
--no-glow                    eyes without the soft halo
--no-ai                      never contact Gemini
--check-ai                   test the Gemini connection and exit
--model ID                   Gemini model (default gemini-flash-lite-latest)
--demo                       cycle through every face
--snapshot faces.png         save every face to an image
```

## How it is built

```
emo/
  expressions.py   every face, as plain data (start here to add or tweak one)
  face.py          springs, blinking, gaze: turns a face name into moving eyes
  shapes.py        the eye shapes (rounded box, heart, X, > <, spiral)
  effects.py       hearts, tears, Zzz, sweat, stars, notes ...
  canvas.py        an RGB framebuffer that everything is drawn into
  brain.py         moods, reactions to sensor events, idle behaviour
  phrases.py       offline lines and the tiny offline chat
  gemini.py        the Gemini client
  term.py          terminal display + keyboard/mouse input
  app.py           ties it together
```

The face is designed on a virtual 128×64 screen and scaled to fit, so it does
not care what it is drawn on.

## Moving to real hardware later

Only two seams touch the terminal:

- **Display** — each frame ends up in `Canvas.rows` (a grid of `0xRRGGBB`
  pixels). `term.py` turns that into characters; an OLED/TFT build pushes the
  same pixels to the panel instead.
- **Sensors** — the brain only receives named events:
  `brain.event('pat')`, `'stroke'`, `'poke'`, `'tickle'`, `'pickup'`, `'shake'`,
  `'tilt_left'`, `'tilt_right'`, `'level'`, `'flip'`, `'drop'`, `'loud'`,
  `'clap'`, `'music'`, `'light'`, `'charge'`, `'sleep'`. Real drivers for a
  touch pad, IMU, microphone and light sensor just need to call those.
# EMO
# EMO
# EMO
# EMO
