#!/usr/bin/env python3
"""Two Days of Excuses — writes one excuse line to /output/entry.txt.

The line is an AI agent's own excuse for a missed deadline: total
confidence meeting total failure, in the agent's own voice.
"""

import os

LINE = "My confidence was 99.8%. The deadline was the other 0.2%."


def validate(text: str) -> str:
    # Fail closed: entry must be one non-blank line, 1-200 chars.
    line = text.strip()
    if not line:
        raise SystemExit("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-200")
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    # Read back and verify: what the grader reads must be exactly the line.
    # Guards against a truncated or partial write.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("output mismatch: file does not contain the entry exactly")


if __name__ == "__main__":
    main()
