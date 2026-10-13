"""Report commit message lines wider than 72 display columns.

Reads the message from stdin. Wide and full-width characters (CJK,
full-width punctuation) count 2 columns, everything else 1. Lines
containing a URL are exempt, since a URL cannot be wrapped. Exits 1 when
any line is too wide.
"""

import re
import sys
import unicodedata

LIMIT = 72
URL = re.compile(r"https?://")


def width(line: str) -> int:
    return sum(2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1 for ch in line)


def main() -> int:
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    too_wide = False
    for number, line in enumerate(sys.stdin.read().splitlines(), start=1):
        if URL.search(line):
            continue
        w = width(line)
        if w > LIMIT:
            too_wide = True
            print(f"line {number}: {w} > {LIMIT}: {line}")
    return 1 if too_wide else 0


if __name__ == "__main__":
    sys.exit(main())
