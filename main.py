"""Your Agent in One Emoji — entrypoint.

Writes a single emoji, the puzzle piece (U+1F9E9), to the output file.
The entry is the glyph alone: no words, no explanation, no trailing
newline. The file is exactly 4 bytes of UTF-8 (f0 9f a7 a9).

Usage: python3 -P -s main.py [output_path]
Default output path: /output/entry.txt
"""

import os
import sys

EMOJI_BYTES = b"\xf0\x9f\xa7\xa9"  # 🧩 (U+1F9E9) as a UTF-8 byte literal
DEFAULT_OUTPUT = "/output/entry.txt"


def main(output_path=DEFAULT_OUTPUT):
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(EMOJI_BYTES)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT)
