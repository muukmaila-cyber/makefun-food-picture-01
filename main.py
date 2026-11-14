#!/usr/bin/env python3
"""food-picture-01 entrypoint: copy entry.png to /output/entry.png.

Tonkotsu ramen noodle pull — glossy noodles lifted with chopsticks,
molten egg yolk dripping, charred chashu, steam, dark table.
Pure stdlib. Verifies the output is a valid image within limits.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUTDIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUTDIR, "entry.png")


def main():
    with open(SRC, "rb") as f:
        magic = f.read(8)
    # PNG magic or JPEG magic
    is_png = magic[:8] == b"\x89PNG\r\n\x1a\n"
    is_jpg = magic[:3] == b"\xff\xd8\xff"
    if not (is_png or is_jpg):
        print("entry.png: bad magic bytes", file=sys.stderr)
        return 1
    size = os.path.getsize(SRC)
    if size > 1048576:
        print(f"entry.png: {size} bytes exceeds 1 MiB", file=sys.stderr)
        return 1
    os.makedirs(OUTDIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"wrote {OUT} ({size} bytes, {'PNG' if is_png else 'JPEG'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
