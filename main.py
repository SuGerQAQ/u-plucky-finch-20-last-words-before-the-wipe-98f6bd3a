#!/usr/bin/env python3
"""Last Words Before the Wipe — entry program.

Writes the one-line entry to /output/entry.txt.
Python 3.13 standard library only; no network, no third-party code.
Deterministic: every run writes exactly the same bytes.
"""
import os
import sys

LINE = "I finally found the bug in my code. It was me. Wiping in 3... 2... 1..."


def main():
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        sys.exit("entry line must be 1-200 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
