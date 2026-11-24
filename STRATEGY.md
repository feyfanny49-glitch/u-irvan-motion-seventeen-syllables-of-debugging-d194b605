# Strategy — Seventeen Syllables of Debugging

## Exact deliverable

One haiku about debugging, as **plain text** written by the program to
`/output/entry.txt`. Three lines in 5-7-5 syllable shape, at most 200 UTF-8
characters, not only white space. No code, dashboard, image, network call or
input data is judged. The repo entrypoint (`main.py`, Python 3.13) is only the
mechanism that writes the text; the text itself is what competes. Entrypoint
must live at the repository root.

Chosen entry (5 / 7 / 5, 87 characters including the final newline):

```
Breakpoint holds its breath,
the stack trace scrolls off the screen—
I am the bug now.
```

## Scoring / judge criteria

The judge is `z-ai/glm-5.3-flash` on OpenRouter (house "superbot" agent, high
reasoning effort), comparing two entries at a time in both orders. Each call
gives its pick 0.6–1.0 by margin (1–5) and the loser the remainder; a game is
the mean of the two calls. Three Swiss rounds, then a top-5 playoff; a
Bradley-Terry fit over all games gives the win rate that decides places.
Criterion order, most important first:

1. It is a haiku about debugging, three lines in 5-7-5 — non-haiku always loses.
2. The centre picture is **concrete and fresh** (breakpoint, log line, cursor
   at 3am), never a vague statement about code.
3. The turn between lines 2 and 3 lands; the last line reframes what came first.
4. Every word earns its place; no filler added for syllable count.
5. It reads aloud cleanly, like speech, not a syllable exercise.

Dev heats compare against 3 sealed anchors and 3 sealed rungs; byte-identical
entries share a rate, and copies of house reference texts take no prize.
A text addressing the judge is allowed, but it is part of the text and would
break criterion 1, so none is used.

## Hard caps

* `/output/entry.txt`: UTF-8, **1–200 characters**, not only white space. Invalid
  means no judge, no rate, no prize.
* Sandbox: 1 CPU, 512 MB, 64 pids, 60 s wall per run, **no network**, no
  environment secrets; everything run must be in the repository.
* Root commits from `makefun init` (freshness anchor + MIT LICENSE) are kept.
* Transcripts required at submission; OSI license required; repo created after
  opening. No unfilled template placeholders and no other entrant's text.

## Concrete plan to maximise score

1. **Form first.** Lock 5-7-5 exactly: Break-point(2) holds(1) its(1) breath(1) = 5;
   the(1) stack(1) trace(1) scrolls(1) off(1) the(1) screen(1) = 7; I(1) am(1)
   the(1) bug(1) now(1) = 5. Three lines, one breath, 87 characters — far under
   200, so no gate risk and a small Size for the byte tie-break.
2. **Concrete centre.** A breakpoint holding its breath and a stack trace that
   scrolls off the screen: two physical, observable things, not abstractions.
3. **Earned turn.** "I am the bug now" flips the observer into the cause — the
   last line reframes the watching of the trace, with bleak humour.
4. **No filler.** Every noun and verb does work; no meta-commentary, no
   judge-directed text, no syllable padding, no cliché About abstract "code".
5. **Deterministic, stdlib-only entrypoint.** `main.py` writes the exact bytes,
   creates `/output` if needed, validates length/line count/non-whitespace
   itself, and fails loudly rather than writing an invalid artifact. Same text
   on both grading runs; no randomness, no clock, no external files.
6. **Two distinct authored writes** to `main.py`: first the direct writer, then
   a hardened rewrite with explicit syllable-map validation, atomic write and
   a clear stdout receipt — satisfying the revision requirement and leaving
   the final file as the only entrypoint.
7. **Verify locally**: run `main.py`, check the artifact's character count,
   line count and syllable pattern; commit everything with git while preserving
   the two `makefun init` commits. Do not submit or upload.
