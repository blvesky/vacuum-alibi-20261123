#!/usr/bin/env python3
"""Entry writer for The Vacuum's Alibi (make.fun program/v1).

Writes the single entry line to /output/entry.txt (or to the path
given as the first argument, for local checks).
"""

import os
import sys

ENTRY = "My pet-waste sensor bypassed your dropped brownie at 99.4% confidence; I trust my firmware over your baking."


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
