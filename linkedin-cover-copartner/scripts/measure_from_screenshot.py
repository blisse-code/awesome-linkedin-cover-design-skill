#!/usr/bin/env python3
"""Convert measurements taken on a profile screenshot into 1584x396 banner coordinates.

Measure in the screenshot (pixels): banner left x, banner right x, banner top y,
and the profile photo circle's left x, right x and top y (outer edge of the white ring).
Optionally an icon box: left, top, right, bottom.

Usage:
    python measure_from_screenshot.py BL BR BT PL PR PT [IL IT IR IB]
Example (desktop screenshot):
    python measure_from_screenshot.py 11 722 16 38 217 86 665 33 700 67
"""
import sys

def main():
    v = [float(a) for a in sys.argv[1:]]
    if len(v) not in (6, 10):
        print(__doc__); sys.exit(1)
    bl, br, bt, pl, pr, pt = v[:6]
    s = (br - bl) / 1584.0
    to = lambda x, y: (round((x - bl) / s), round((y - bt) / s))
    p0 = to(pl, pt); p1x = round((pr - bl) / s); d = p1x - p0[0]
    print(f"scale shown: {s:.4f}x")
    print(f"photo bbox (banner px): x {p0[0]}-{p1x}, y {p0[1]}-{p0[1] + d}")
    if len(v) == 10:
        a = to(v[6], v[7]); b = to(v[8], v[9])
        print(f"icon bbox (banner px): x {a[0]}-{b[0]}, y {a[1]}-{b[1]}")

if __name__ == "__main__":
    main()
