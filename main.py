"""Everyday wonder, in one sentence (200 characters or fewer).

Prints the sentence to stdout and writes the exact same sentence,
with no trailing newline, to /output/entry.txt. Standard library only,
no network access, no files read — the sentence is a constant here.

The gate for this bounty is 1 to 200 characters of UTF-8 text, so the
program refuses to write anything outside that range.
"""

import os
import sys

LINE = (
    "At 6 a.m. the kettle steam drew one perfect spiral — the whole "
    "universe, rehearsing in my kitchen, before the toast popped."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
