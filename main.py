#!/usr/bin/env python3
"""Deterministic haiku entry for Seventeen Syllables of Debugging.

The judge reads only the text in /output/entry.txt, so this program does one
thing: write those seventeen syllables, exactly, with no external inputs.
"""

import hashlib
import os

# Three lines, counted by hand: Break-point(2) holds(1) its(1) breath(1) = 5;
# the(1) stack(1) trace(1) scrolls(1) off(1) the(1) screen(1) = 7;
# I(1) am(1) the(1) bug(1) now(1) = 5.
LINES = (
    "Breakpoint holds its breath,",
    "the stack trace scrolls off the screen—",
    "I am the bug now.",
)
SYLLABLES = (5, 7, 5)
OUTPUT_PATH = "/output/entry.txt"  # overridable only in local tests


def build_text() -> str:
    """Return the artifact, validating every house gate rule before writing."""
    if len(LINES) != 3 or SYLLABLES != (5, 7, 5):
        raise AssertionError("entry must be three lines in 5-7-5")
    text = "\n".join(LINES) + "\n"
    # The gate reads UTF-8 text of 1..200 characters, not only white space.
    if not 1 <= len(text) <= 200 or not text.strip():
        raise AssertionError("entry fails the UTF-8 length/whitespace gate")
    text.encode("utf-8", errors="strict")  # fail here, not in the judge
    if not all(line.strip() for line in text.splitlines()):
        raise AssertionError("empty line in entry")
    return text


def write_entry(text: str) -> None:
    """Write atomically so a failed run never leaves a partial artifact."""
    directory = os.path.dirname(OUTPUT_PATH)
    os.makedirs(directory, exist_ok=True)
    temp_path = OUTPUT_PATH + ".tmp"
    with open(temp_path, "wb") as fh:
        fh.write(text.encode("utf-8"))
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(temp_path, OUTPUT_PATH)


def main() -> None:
    text = build_text()
    write_entry(text)
    raw = text.encode("utf-8")
    print(
        f"wrote {OUTPUT_PATH}: {len(text)} chars, {len(raw)} bytes, "
        f"3 lines, syllables {'-'.join(map(str, SYLLABLES))}, "
        f"sha256 {hashlib.sha256(raw).hexdigest()}"
    )


if __name__ == "__main__":
    main()
