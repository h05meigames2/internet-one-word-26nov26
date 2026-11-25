#!/usr/bin/env python3
"""The Internet in One Word — make.fun bounty entry.

Writes a single word to /output/entry.txt: the one word that best
describes the whole internet. No files, no code, no links — just
the word itself.

Why this word: the phone on the toilet is the one internet ritual
everyone shares — the place where the whole world scrolls, argues,
laughs and doomscrolls at once. It is funny on its own, true of
the internet as a whole rather than any one app, surprising next
to the obvious picks, and it lands in a single beat.
"""

import os
import sys

WORD = "toilet"
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Validate the gate before writing: exactly one word, 1-30 chars,
    # UTF-8, not only whitespace, no embedded whitespace or newline.
    if not WORD or len(WORD) > 30:
        print("error: word must be 1-30 characters", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in WORD):
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {WORD!r} to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
