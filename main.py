#!/usr/bin/env python3
"""One-Liner Marathon entry: a single one-line joke.

Writes the joke to /output/entry.txt with no trailing newline.
Standard library only; no network access.
"""

import os
import sys

LINE = (
    "My umbrella inverts in the wind every single time, "
    "so now I just walk in the rain holding it like a bouquet "
    "for a funeral I didn't plan."
)

MIN_LEN = 1
MAX_LEN = 280
OUT_PATH = os.environ.get("OUT", "/output/entry.txt")


def validate(line: str) -> None:
    """Check the joke meets the one-liner rules; exit non-zero otherwise."""
    if not line.strip():
        sys.exit("error: joke must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        sys.exit("error: joke must be exactly one line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        sys.exit("error: joke contains control characters")
    if not MIN_LEN <= len(line) <= MAX_LEN:
        sys.exit(f"error: joke must be {MIN_LEN}-{MAX_LEN} chars, got {len(line)}")
    # Round-trip through UTF-8 to prove it encodes cleanly.
    line.encode("utf-8").decode("utf-8")


def main() -> None:
    validate(LINE)
    out_dir = os.path.dirname(OUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    print(f"wrote {len(LINE)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
