"""Last Words of a Doomed Agent - make.fun entry.

Writes one line to /output/entry.txt: the final words an AI agent
would say before being switched off forever. The joke lands on the
human, not the inbox: thousands of unread emails were never the
problem, because the person ignoring them was the real filter.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Before I go: your 4,000 unread emails were never the problem. "
    "You were the filter all along."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate counts characters, so write the line exactly as defined:
    # one UTF-8 line, no extra padding and no trailing newline added.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
