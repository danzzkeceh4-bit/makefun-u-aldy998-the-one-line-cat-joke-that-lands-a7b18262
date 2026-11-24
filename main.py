#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun entry.

Writes one funny line about cats to /output/entry.txt: exactly 118
characters, no trailing newline. Then reads it back and asserts the
content matches the constant exactly. No network, no external input.
"""

import os

# Why this joke: every cat owner has watched their cat deliberately
# knock something off a table, then stare at the mess with total
# innocence. The line leans into that shared image, lets the cat
# blame gravity, and lands the twist at the end — the cat was only
# the "supervisor", never the culprit.
ENTRY = (
    "My cat knocked my coffee off the table, stared at the spill, and "
    "filed it under 'gravity did it, I merely supervised.'"
)


def main() -> None:
    """Write ENTRY to entry.txt and verify it byte-for-byte.

    Gates the entry at 1-200 characters (the competition's length
    rule) and rejects whitespace-only text, then writes the file with
    no trailing newline and reads it back, asserting the content on
    disk matches the constant exactly before reporting success.
    """
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.environ.get("OUTPUT_PATH", os.path.join(output_dir, "entry.txt"))
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, (
        f"entry mismatch: read back {len(written)} chars, "
        f"expected {len(ENTRY)} chars"
    )
    assert len(written) == 118, f"entry must be 118 chars, got {len(written)}"
    print(f"Wrote {len(written)} characters to {output_path}")


if __name__ == "__main__":
    main()
