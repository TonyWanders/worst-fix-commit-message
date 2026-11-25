"""Worst Fix Ever: Funniest Commit Message entry for make.fun.

Writes one commit message, at most 100 characters, to the output target.
Deterministic: the same fixed text on every run. Writes only to the
output target, never into the repository directory.
"""

import os
import sys

ENTRY = "fix: silenced checkout errors by skipping payment, orders now succeed and we earn nothing"

DEFAULT_OUTPUT = "/output/entry.txt"

USAGE = "usage: main.py [OUTPUT_PATH]\nWrites the entry line to OUTPUT_PATH,\nor to $OUTPUT_PATH, or to /output/entry.txt by default.\n"


def write_entry(output_path: str) -> None:
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main(argv=None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    if args and args[0] in ("-h", "--help"):
        sys.stdout.write(USAGE)
        return
    if args:
        output_path = args[0]
    else:
        output_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    write_entry(output_path)


if __name__ == "__main__":
    main()
