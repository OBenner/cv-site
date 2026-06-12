#!/usr/bin/env python3
"""Generate site icons: apple-touch-icon (180), icon-192, icon-512 — dark square with the green cursor block."""
from PIL import Image, ImageDraw

BG = (6, 10, 16)
GR = (61, 255, 160)


def make(size, path):
    img = Image.new("RGB", (size, size), BG)
    d = ImageDraw.Draw(img)
    x = round(size * 0.28)
    y = round(size * 0.22)
    w = round(size * 0.25)
    h = round(size * 0.56)
    d.rectangle([x, y, x + w, y + h], fill=GR)
    img.save(path, "PNG")
    print("written:", path)


make(180, "/Users/om/self_site/apple-touch-icon.png")
make(192, "/Users/om/self_site/icon-192.png")
make(512, "/Users/om/self_site/icon-512.png")
