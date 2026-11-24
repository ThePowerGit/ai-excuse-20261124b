"""make.fun entry: "The One-Line AI Excuse for Breaking Production".

The entry is one line of at most 180 characters: the excuse an AI agent
gives its human after breaking production. The agent has already written
the postmortem, and the human is the one credited as its author.

entry.txt holds the canonical bytes. This script copies them verbatim to
/output/entry.txt, so every grading run sees identical output. Before
copying, it checks the two rules that make the entry valid: at most 180
characters, and exactly one line with no trailing newline. A violation
raises instead of shipping a broken entry.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The output directory comes from MAKEFUN_OUTPUT_DIR and defaults to
/output, so the same code serves the grader and a local checkout.
"""

import os
import shutil

# The entry may be no longer than this, per the competition rules.
MAX_CHARS = 180

# Name of the canonical entry file, stored next to this script.
ENTRY_NAME = "entry.txt"


def read_entry(source: str) -> bytes:
    """Return the entry bytes, after enforcing the one-line 180-char rule.

    Raises:
        ValueError: if the entry is empty, longer than MAX_CHARS, spans
            more than one line, or ends with a newline.
    """
    with open(source, "rb") as handle:
        raw = handle.read()

    text = raw.decode("utf-8")
    if not text:
        raise ValueError(f"{ENTRY_NAME} is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"{ENTRY_NAME} is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError(f"{ENTRY_NAME} must be a single line with no trailing newline")

    return raw


def main() -> None:
    """Copy the canonical entry line into the output directory."""
    # Resolve paths relative to this file so the script works from any cwd.
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), ENTRY_NAME)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    destination = os.path.join(output_dir, ENTRY_NAME)

    # Validate first, so a malformed entry fails loudly instead of shipping.
    read_entry(source)

    # shutil.copyfile copies raw bytes only: no newline translation, no
    # re-encoding, so the graded file is identical to the one here.
    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
