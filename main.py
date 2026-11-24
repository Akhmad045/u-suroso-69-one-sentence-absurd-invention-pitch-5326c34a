#!/usr/bin/env python3
"""Entry for 'One-Sentence Absurd Invention Pitch'.

Writes one sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to /output/entry.txt, then verifies the written file
round-trips exactly. Standard library only; no network access.
"""

import os
import sys

SENTENCE = (
    "A toaster that fires each slice out on a tiny parachute, "
    "so your toast can never land butter-side down."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    if not SENTENCE or not SENTENCE.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in SENTENCE or "\r" in SENTENCE:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(SENTENCE) <= 220:
        print(
            f"error: entry is {len(SENTENCE)} characters, must be 1-220",
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE + "\n")

    raw = open(OUTPUT_PATH, "rb").read()
    if raw.decode("utf-8") != SENTENCE + "\n":
        print("error: written file does not round-trip exactly", file=sys.stderr)
        return 1

    print(f"wrote {len(SENTENCE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
