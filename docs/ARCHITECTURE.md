# Architecture

EMO is a pipeline that runs about 30 times a second:

```
keyboard / mouse ──► events ──► brain ──► face + effects ──► canvas ──► terminal
   (term)            (app)     (moods)     (animation)       (pixels)    (term)
                                  ▲
                                  └── gemini (optional, background thread)
```

Only `term` knows about the terminal, and only `brain.event` knows about
sensors. Those are the two seams a hardware build replaces.

## Conventions

- **State is a class; behaviour is functions.** Each package has one small
  class that only holds state (`Face`, `Effects`, `Brain`, `Gemini`, `App`,
  `Canvas`), in `state.py` or a file named after it. Everything that acts on
  it is a function taking that object first: `face.update(emo, dt)`,
  `brain.event(mind, "pat")`. This is what keeps every file short.
- **Each package's `__init__.py` is its public face.** Import from the
  package (`from emo.brain import event`), not from its inner modules.
- **No file or function exceeds 60 lines** (`tests/test_limits.py` enforces
  it). When something grows, split it by concern into a new module.
- **Typed, modern Python 3.14**: `type` aliases, `X | None`, built-in
  generics.

## Packages, bottom up

| Package | What it owns |
| --- | --- |
| `shapes` | Signed distance functions for eye shapes. A shape answers "how far is this point from my edge", which gives smooth edges and free morphing. |
| `canvas` | `Canvas` (rows of `0xRRGGBB` pixels) and drawing: `fill_sdf`, `fill_rect`, `blit`, `glitch`, `to_png`. |
| `expressions` | The 45 faces as data, grouped by mood, merged into `EXPRESSIONS`. |
| `face` | `Face` state, springs, gaze, blinking, and drawing the eyes. |
| `effects` | Particles and icons around the face. Emitters share one random stream, so their order is fixed in `effects/update.py`. |
| `brain` | Moods, the script/baseline layers, and one module per kind of sensing under `brain/senses/`. |
| `phrases` | Canned lines, their descriptions for the AI, and the keyword chat used without a key. |
| `gemini` | HTTPS client: prompt, request with fallbacks, background worker, reply parsing. |
| `term` | Half-block pixel encoding, colour detection, input parsing, the raw-mode session. |
| `app` | `App` state, the main loop, input handlers, layout and the rows of the screen. |
| `snapshot`, `cli` | Rendering faces to a PNG; the command line. |

Dependencies only point upward in this table (for example `brain` uses
`face` and `effects`, never the reverse), so there are no import cycles.

## How a face is chosen

Two layers, in `brain`:

1. A **script** — a short reaction made of `Step(face, seconds)` items, started
   with `play()`. Scripts have a priority; a fall cannot be interrupted by a pat.
2. The **baseline** — when no script is running, `baseline()` picks a face
   from the situation (asleep, held, upside down …) and then the moods.

`show()` hands the chosen name to `face.set_expression`, which only moves the
springs' targets. The eyes then flow there over the next frames.

## How a frame is drawn

`app.draw` asks `panel_rows` to render the face and effects into the canvas,
`term.pixel_row` turns each pair of pixel rows into one row of half-block
characters, and only the screen rows that changed since the last frame are
written.

## Tests

`tests/golden.json` is a recording made before the code was split into small
modules: every face's pixels, a long session of sensor events, and the exact
bytes the app wrote to the terminal for a scripted session at three sizes.
The tests replay the same inputs and require identical results, so they
catch any unintended change in behaviour. The Gemini client is tested against
a small local mock server (`tests/mock_gemini.py`).
