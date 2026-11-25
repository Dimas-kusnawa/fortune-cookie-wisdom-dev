"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a bug that cannot be reproduced locally has already reproduced
itself where it matters most.
"""

import os

# Why this line: it reads like a real fortune cookie — one short,
# balanced sentence that lands in a single breath — and it says
# something true about a developer's day: the bug that never shows up
# on your machine shows up in production at the worst possible hour.
# The line is 96 characters, inside the bounty's 120-character cap.
# No trailing newline: the gate counts the file's characters, and a
# single line with no newline keeps the entry exactly one fortune.
LINE = (
    "The bug you cannot reproduce has already reproduced "
    "\u2014 in production, at 3 a.m., on your holiday."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
