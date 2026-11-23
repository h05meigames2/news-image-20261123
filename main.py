#!/usr/bin/env python3
"""Entrypoint for the make.fun news-image-20261123 bounty entry.

Copies the rendered front page (entry.png, produced by gen_image.py)
into the make.fun output directory as entry.png.

Usage:
    python3 gen_image.py   # render entry.png first
    python3 main.py        # copy it to $MAKEFUN_OUTPUT_DIR/entry.png

Stdlib only. Deterministic: the output is a byte-for-byte copy of the
input image, so repeated runs produce identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(HERE, "output")
    if not os.path.isfile(SOURCE):
        print("entry.png not found; run 'python3 gen_image.py' first.",
              file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print("wrote", dest, os.path.getsize(dest), "bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
