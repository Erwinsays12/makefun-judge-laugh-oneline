#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry program.

Writes exactly one funny line to /output/entry.txt.

The line was chosen by an internal head-to-head tournament over a pool of
12 original one-liners, judged on the competition's own rubric: a stranger
must get it in one read, it must surprise, stay tight with the laugh
landing at the very end, feel fresh, and read cleanly out loud.

Champion (107 characters): a cat, a spilled coffee, and an unexpected
landlord.
"""

import os
import sys

# The winning one-liner. One concrete scene (cat knocks the coffee off the
# table, eye contact) plus one twist (the cat speaks, and it wants rent).
LINE = (
    "My cat knocked my coffee off the table, looked me dead in the eye, "
    "and I swear I heard it say 'rent's due'."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text, 1-200 chars, not blank."""
    text.encode("utf-8")  # raises if not encodable as UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    validate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: what the grader reads must be byte-identical to
    # the validated line, with no added newline or encoding change.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("round-trip mismatch: file content differs from LINE")
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
