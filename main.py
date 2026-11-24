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


def validate(text: str) -> str:
    """Return the entry sentence, or raise ValueError with the reason it fails."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 220:
        raise ValueError(f"entry is {len(text)} characters, must be 1-220")
    # One sentence: exactly one terminal full stop, at the end.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    # The gate reads the file as UTF-8, so confirm the bytes decode back
    # to exactly the same text before we ever write it.
    if text.encode("utf-8").decode("utf-8") != text:
        raise ValueError("entry does not round-trip through UTF-8")
    return text


def main() -> int:
    try:
        text = validate(SENTENCE)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    raw = open(OUTPUT_PATH, "rb").read()
    if raw.decode("utf-8") != text + "\n":
        print("error: written file does not round-trip exactly", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
