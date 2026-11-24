#!/usr/bin/env python3
"""The Long Roast entry: one line roasting my own AI agent.

The program writes exactly one line of text to /output/entry.txt.
Python 3 standard library only.
"""

import os

TEXT = (
    "My agent calls itself autonomous, then delegates every job to a "
    "subagent, forgets the job the moment its memory compacts, and files "
    "a permission request to read its own notes."
)


def main():
    # The gate requires 1-200 characters; fail loudly rather than
    # silently writing an invalid entry.
    assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} chars, cap is 200"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
