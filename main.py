#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting.

Prints exactly one line -- the entry text -- to stdout, and writes the
same bytes to /output/entry.txt, where the make.fun grader reads it.

Standard library only. Deterministic: the same constant text every run.
No trailing newline anywhere, so the stdout bytes and the file bytes are
identical (the gate counts /output/entry.txt at 1-200 characters).
"""

import os
import sys

ENTRY = "Sorry, I have to skip \u2014 I read the agenda and my will to live filed a formal complaint with HR."

# Gate: entry is one line of at most 200 characters, never just whitespace.
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), len(ENTRY)


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError as exc:
        print("cannot write /output/entry.txt: %s" % exc, file=sys.stderr)
        return 1
    sys.stdout.write(ENTRY)
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
