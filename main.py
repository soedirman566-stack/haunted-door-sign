#!/usr/bin/env python3
"""Entrypoint: write the haunted server room door sign to /output/entry.txt."""

from pathlib import Path

LINE_FILE = Path(__file__).with_name("line.txt")
OUTPUT_FILE = Path("/output/entry.txt")


MAX_CHARS = 120  # the competition gate: UTF-8 text of 1 to 120 characters


def main() -> None:
    line = LINE_FILE.read_text(encoding="utf-8").strip()
    if not line or len(line) > MAX_CHARS:
        raise SystemExit(f"line fails the gate: {len(line)} characters")
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
