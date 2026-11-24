#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line - an alien tourist's review of planet Earth -
to /output/entry.txt. Standard library only.
"""

import os
from pathlib import Path

# The line: one joke, one observation only an alien would make.
# Humans queue for hours for unknown reasons and then rate the queue -
# the reviewer gets absorbed into the ritual ("I joined in"), which is
# where the laugh comes from. The rating closes it like a real review,
# and the punch lands at the end. Deliberately avoids the obvious
# first thoughts (traffic, gravity, money, weather).
ENTRY = (
    "Two days on Earth: the locals queue for hours without knowing "
    "what for, then rate the queue five stars. I joined in. 4/5 stars."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    out = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
