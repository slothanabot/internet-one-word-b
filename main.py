#!/usr/bin/env python3
"""make.fun entry: The Internet in One Word (internet-one-word-b).

The entry is a single word for the whole internet, written to
/output/entry.txt. The word is "Doomscrollable": the internet is
the place you open for one quick look and leave an hour later,
thumb sore, having learned nothing and forgotten why you came.
It is funny because it is a diagnosis, it fits the internet as
a whole rather than one corner of it, and it surprises by turning
a habit everyone is slightly ashamed of into a single adjective.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 30


def build_entry():
    """Return the one-word entry, my own wording throughout."""
    # "Doomscrollable" names the defining act of the modern
    # internet: endless scrolling through bad news you cannot
    # stop reading. One invented word carries the setup (doom),
    # the habit (scrolling) and the punch (it is a property of
    # the place itself, not of the user).
    return "Doomscrollable"


def validate(word):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not word.strip():
        problems.append("empty")
    if word != word.strip():
        problems.append("leading/trailing whitespace")
    if len(word) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(word))
    if " " in word or "\n" in word:
        problems.append("not a single word")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    word = build_entry()
    validate(word)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(word, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
