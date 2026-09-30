# Lab 4 - Vibe Coding: AI-Assisted Debugging & Feature Completion

Starter repository: `SETAPESU26/48_whack-a-mole` (Pygame)

A partially working Whack-a-Mole game is analysed, debugged and completed with an LLM as the
pair-programming partner. Each of the four tasks went through the same loop: prompt, review the
suggested change, run the game, keep or correct the result.

## Contents

| File | What it is |
|---|---|
| [before.mp4](before.mp4) | 10-second gameplay capture of the starter code, showing the double-score bug and the round ending in a console print |
| [after.mp4](after.mp4) | 10-second gameplay capture after the changes - single-point hits, game-over panel, replay on Hard |
| [chat-history.pdf](chat-history.pdf) | Complete chat history with the LLM - 5 prompts and the responses, including the test results for each fix |
| [main.py](main.py) | Entry point - window setup and the main loop |
| [game/game_engine.py](game/game_engine.py) | Round state, click handling, difficulty settings, game-over panel and rendering |
| [game/hole.py](game/hole.py) | One hole - mole timer and the circular hit test |
| [game/sounds.py](game/sounds.py) | Sound effects synthesised in memory at start-up |
| [requirements.txt](requirements.txt) | Python dependencies (`pygame`) |

## LLM used

| | |
|---|---|
| Tool | Claude Code in VS Code |
| Model | Claude Opus 5.5 |
| Date | 30 September 2026 |

## Running the game

Python 3.10+ is required.

```bash
pip install -r requirements.txt
python main.py
```

## Tasks

| # | Task | What was done | Where |
|---|---|---|---|
| 1 | Refine collision detection | Hit area changed from a 150 px square to a 32 px circle matching the drawn mole; a click whacks only the closest active mole under it | `game/hole.py`, `game/game_engine.py` |
| 2 | Implement game-over condition | Console print replaced by a "Time's Up!" panel with the final score and missed clicks; the game waits for input instead of freezing | `game/game_engine.py` |
| 3 | Add replay option | Easy / Medium / Hard and Exit buttons on the panel, with keyboard shortcuts; choosing a level resets score, misses and timer | `game/game_engine.py` |
| 4 | Add sound feedback | Tones for a hit, a miss and the round ending, generated at start-up so no audio files are needed | `game/sounds.py` |

## Bugs found in the starter code

**Double scoring.** Each hole had a square hit box 150 px wide, but the holes sit only 125 px
apart horizontally and 120 px vertically, so neighbouring hit boxes overlapped. The click handler
also checked every hole and never stopped at the first hit, so one click on the border between
two raised moles scored 2 points.

**Loose hits.** For the same reason a click on the grass well outside a mole still scored.

**No end of round.** When the timer reached zero the game printed the score to the console and
the window froze, with no way to replay or exit other than closing it.

**Timer rounding.** The timer rounded down, showing 29s at the start and sitting on 0s for the
whole last second. It now rounds up.

## Collision test

Two neighbouring moles up, after the fix:

| Click position | Result |
|---|---|
| On the border between them (187, 200) | 0 points, counted as a miss |
| On the edge of the left mole (157, 200) | 1 point |
| One pixel outside the mole (158, 200) | 0 points, counted as a miss |
| Centre of the left mole (125, 200) | 1 point |

No click scores more than one point.

## Difficulty levels

| Level | Key | Spawn chance per hole per frame | Frames a mole stays up |
|---|---|---|---|
| Easy | `1` or `E` | 0.012 | 70 |
| Medium | `2` or `M` | 0.02 | 45 |
| Hard | `3` or `H` | 0.035 | 26 |

Medium keeps the starter code's original values and is the level the first round starts on.
`Esc` or `Q` exits from the game-over panel. A round lasts 30 seconds at 60 FPS.

## Sounds

| Event | Tone |
|---|---|
| Successful whack | Rising two-note beep - 880 Hz then 1320 Hz |
| Missed click | Low 180 Hz tone |
| Round end | Falling three-note tune - 660, 520, 390 Hz |

Each tone fades out to avoid a click at the end. On a machine with no audio device the game runs
silently instead of crashing.
