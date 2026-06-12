#!/usr/bin/env python3
"""Generate og.png (1200x630) — terminal-window social preview card."""
from PIL import Image, ImageDraw, ImageFont

OUT = "/Users/om/self_site/og.png"
W, H = 1200, 630

BG = (6, 10, 16)
PN = (10, 18, 27)
BD = (27, 44, 59)
SEP = (18, 32, 44)
GR = (61, 255, 160)
CY = (69, 225, 255)
T2 = (168, 192, 211)
MU = (125, 147, 166)

MENLO = "/System/Library/Fonts/Menlo.ttc"


def font(size, bold=False):
    return ImageFont.truetype(MENLO, size, index=1 if bold else 0)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

d.rounded_rectangle([70, 70, 1130, 560], radius=24, fill=PN, outline=BD, width=3)
for i, c in enumerate([(255, 95, 87), (254, 188, 46), (40, 200, 64)]):
    d.ellipse([110 + i * 40, 108, 134 + i * 40, 132], fill=c)
d.line([70, 158, 1130, 158], fill=SEP, width=2)

x = 120
f30 = font(29)
f30b = font(29, bold=True)
f40b = font(40, bold=True)

y = 190
w = d.textlength("omiagkov@prod:~$ ", font=f30b)
d.text((x, y), "omiagkov@prod:~$ ", font=f30b, fill=GR)
d.text((x + w, y), "whoami", font=f30, fill=CY)

y += 64
d.text((x, y), "oleg miagkov · tech lead data engineer", font=f40b, fill=GR)

y += 70
d.text((x, y), "high-load data platforms · fintech · 8+ years", font=f30, fill=T2)

y += 52
d.text((x, y), "java · scala · go · python · spark · kafka", font=f30, fill=MU)

y += 52
d.text((x, y), "status: open to interesting projects ✓", font=f30, fill=GR)

y += 64
w = d.textlength("omiagkov@prod:~$ ", font=f30b)
d.text((x, y), "omiagkov@prod:~$ ", font=f30b, fill=GR)
d.rectangle([x + w + 4, y - 2, x + w + 22, y + 34], fill=GR)

f26 = font(26)
s = "www.oom.fyi"
d.text((1130 - d.textlength(s, font=f26), 580), s, font=f26, fill=MU)

img.save(OUT, "PNG")
print("written:", OUT)
