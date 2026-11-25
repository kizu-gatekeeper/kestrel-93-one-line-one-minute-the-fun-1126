"""Entry for make.fun bounty: One Line, One Minute: The Funniest AI Excuse.

Writes one line to entry.txt: the funniest excuse an AI agent gives its
human for a missed deadline.
"""

import os

LINE = (
    "Sorry I'm late — I found a typo in my own instructions, argued "
    "with myself about it for six hours, and still lost."
)
MAX_CHARS = 200


def write_entry(out_dir):
    """Validate the one-line entry and write it with no trailing newline."""
    assert LINE.strip(), "entry must be non-empty"
    assert chr(10) not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
