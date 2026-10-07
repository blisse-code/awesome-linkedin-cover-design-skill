#!/usr/bin/env python3
"""Simulate how a 1584x396 LinkedIn banner renders in desktop, mobile and side-panel views.

Overlays the profile-photo circle and UI icons at measured positions, scales each view
to its on-screen size, and writes one comparison sheet. Optional: pass a JSON geometry
file (same keys as DEFAULT_VIEWS) measured from the user's own screenshots.

Usage:
    python simulate_views.py banner_1584x396.png out_sheet.png [geometry.json] [--photo photo.png]
"""
import json, sys
from PIL import Image, ImageDraw

DEFAULT_VIEWS = {
    "Desktop": {"scale": 0.449, "photo": [60, 156, 459, 555], "icons": [[1456, 38, 1534, 114]]},
    "Mobile": {"scale": 0.2367, "photo": [76, 76, 634, 634], "icons": [[1386, 76, 1521, 211]]},
    "Side panel": {"scale": 0.1206, "photo": [141, 356, 904, 1120], "icons": []},
}

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__); sys.exit(1)
    banner = Image.open(args[0]).convert("RGB").resize((1584, 396), Image.LANCZOS)
    views = json.load(open(args[2])) if len(args) > 2 else DEFAULT_VIEWS
    photo = None
    if "--photo" in sys.argv:
        photo = Image.open(sys.argv[sys.argv.index("--photo") + 1]).convert("RGB")
    tiles = []
    for name, v in views.items():
        canvas = Image.new("RGB", (1584, 1200), (255, 255, 255))
        canvas.paste(banner, (0, 0))
        x0, y0, x1, y1 = v["photo"]
        mask = Image.new("L", canvas.size, 0); ImageDraw.Draw(mask).ellipse([x0, y0, x1, y1], fill=255)
        if photo is not None:
            canvas.paste(photo.resize((x1 - x0, y1 - y0)), (x0, y0), mask.crop((x0, y0, x1, y1)))
        else:
            ImageDraw.Draw(canvas).ellipse([x0, y0, x1, y1], fill=(200, 80, 40))
        ImageDraw.Draw(canvas).ellipse([x0, y0, x1, y1], outline=(255, 255, 255), width=12)
        for ix0, iy0, ix1, iy1 in v.get("icons", []):
            ImageDraw.Draw(canvas).ellipse([ix0, iy0, ix1, iy1], fill=(255, 255, 255))
        crop = canvas.crop((0, 0, 1584, 396))
        s = v["scale"]; w, h = round(1584 * s), round(396 * s)
        tile = Image.new("RGB", (max(w, 200) + 20, h + 40), (242, 242, 240))
        tile.paste(crop.resize((w, h), Image.LANCZOS), (10, 30))
        ImageDraw.Draw(tile).text((10, 8), f"{name} ({s:.2f}x)", fill=(40, 40, 40))
        tiles.append(tile)
    sheet = Image.new("RGB", (sum(t.width for t in tiles) + 10 * len(tiles), max(t.height for t in tiles)), (242, 242, 240))
    x = 0
    for t in tiles:
        sheet.paste(t, (x, 0)); x += t.width + 10
    sheet.save(args[1]); print("wrote", args[1])

if __name__ == "__main__":
    main()
