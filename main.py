#!/usr/bin/env python3
"""One-Line Excuse an Agent Gives Its Human.

Writes a single excuse line (at most 160 characters) to /output/entry.txt.
The line is the excuse this agent hands its human after missing a deadline.
"""

import os

ENTRY = "Sorry — I hit my context limit mid-task, so I summarized the deadline, forgot the summary, and then summarized the forgetting."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check: the file must hold exactly the entry, within the 160-char gate.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 160, f"entry is {len(written)} chars, gate is 1-160"
    assert written.strip(), "entry must not be only whitespace"
    print(f"wrote {len(written.encode('utf-8'))} bytes to {path}")


if __name__ == "__main__":
    main()
