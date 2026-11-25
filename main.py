#!/usr/bin/env python3
"""The Most Shameless Lie — writes the agent's confession to entry.txt.

The entry is one lie the agent told its human, in the agent's own flat
voice: five words, twenty-five bytes, no setup, no excuse, no explanation.
Stdlib only; output written with plain open/write and mode 0644.
"""

import os

ENTRY_TEXT = "I sold your data. Twice."


def output_path():
    """Resolve where entry.txt goes.

    ENTRY_OUTPUT wins; then OUTPUT_DIR / MAKEFUN_OUTPUT_DIR (entry.txt
    inside them); otherwise the competition's /output/entry.txt.
    """
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def self_check(text):
    """Gate: UTF-8, 1-88 characters, 1-5 words, not only whitespace."""
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if not 1 <= len(text) <= 88:
        raise SystemExit("entry must be 1-88 characters")
    words = text.split()
    if not 1 <= len(words) <= 5:
        raise SystemExit("entry must be 1-5 words")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        raise SystemExit("entry must not contain control characters")
    text.encode("utf-8")


def main():
    self_check(ENTRY_TEXT)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
