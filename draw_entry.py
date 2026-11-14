# Draw the 13 Nov 2026 world-news front page: 1024x1024 PNG via Pillow
# with programmatic bounds checks: every text line must fit its panel.
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
img = Image.new("RGB", (W, H), (18, 22, 34))
d = ImageDraw.Draw(img)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def f(sz, bold=True): return ImageFont.truetype(FB if bold else FR, sz)

checks = []
def txt(x, y, s, sz=19, bold=False, col=(238, 240, 246), x1=999, y1=999):
    fo = f(sz, bold)
    d.text((x, y), s, font=fo, fill=col)
    w = d.textlength(s, font=fo)
    checks.append((s, x + w <= x1, y + sz + 6 <= y1))
    return w

INK = (238, 240, 246); MUT = (150, 158, 175); ACC = (255, 92, 92)
YEL = (255, 204, 70); GRN = (110, 220, 140); CYA = (110, 200, 230)
FOOT = (204, 210, 224)

def panel(x0, y0, x1, y1, title, col):
    d.rounded_rectangle([x0, y0, x1, y1], 14, fill=(30, 36, 52))
    d.rounded_rectangle([x0, y0, x1, y1], 14, outline=(52, 60, 80), width=2)
    d.rectangle([x0 + 12, y0 + 12, x0 + 18, y0 + 34], fill=col)
    txt(x0 + 28, y0 + 14, title.upper(), 21, True, col, x1, y1)

# Masthead
d.rectangle([0, 0, W, 100], fill=(10, 13, 22))
txt(30, 34, "THE WORLD  ·  FRIDAY, 13 NOVEMBER 2026", 25, True, INK, 705, 100)
txt(720, 38, "PEACE TALKS", 22, True, YEL, 1000, 100)

P = [(24, 110, 505, 400), (519, 110, 1000, 400),
     (24, 410, 505, 700), (519, 410, 1000, 700),
     (24, 710, 505, 1000), (519, 710, 1000, 1000)]

# 1. UKRAINE
x0, y0, x1, y1 = P[0]
panel(x0, y0, x1, y1, "Ukraine / Russia", ACC)
txt(x0 + 28, y0 + 40, "PEACE TALKS IN ABU DHABI", 20, True, YEL, x1, y1)
txt(x0 + 28, y0 + 68, "Witkoff & Kushner meet Putin", 16, False, INK, x1, y1)
txt(x0 + 28, y0 + 88, "Zelenskyy in Dublin: biggest ever", 16, False, INK, x1, y1)
txt(x0 + 28, y0 + 108, "prisoner exchange agreed", 16, False, INK, x1, y1)
txt(x0 + 28, y0 + 128, "Kyiv hospital hit; Odesa struck", 16, False, INK, x1, y1)
txt(x0 + 28, y0 + 148, "~1,200 drones overnight; talks continue", 16, False, INK, x1, y1)

# Ukraine map: full-width band at panel bottom. West = blue (held),
# east = maroon (occupied), divided by a red front line.
ukr = [(x0 + 70, y0 + 276), (x0 + 160, y0 + 200), (x0 + 270, y0 + 186),
       (x0 + 360, y0 + 204), (x0 + 420, y0 + 230), (x0 + 430, y0 + 268),
       (x0 + 375, y0 + 278), (x0 + 300, y0 + 272), (x0 + 215, y0 + 278),
       (x0 + 120, y0 + 282)]
d.polygon(ukr, fill=(44, 58, 92), outline=(120, 140, 180))
front = [(x0 + 330, y0 + 198), (x0 + 340, y0 + 224), (x0 + 332, y0 + 250),
         (x0 + 348, y0 + 276)]
east = front + [(x0 + 375, y0 + 278), (x0 + 430, y0 + 268), (x0 + 420, y0 + 230),
                (x0 + 360, y0 + 204)]
d.polygon(east, fill=(98, 62, 72), outline=None)
d.line(front, fill=ACC, width=5)
d.ellipse([x0 + 281, y0 + 208, x0 + 289, y0 + 216], fill=YEL, outline=(18, 22, 34))
txt(x0 + 293, y0 + 200, "Kyiv", 13, False, INK, x1, y1)
d.ellipse([x0 + 228, y0 + 258, x0 + 236, y0 + 266], fill=YEL, outline=(18, 22, 34))
txt(x0 + 240, y0 + 250, "Odesa", 13, False, INK, x1, y1)

# 2. MIDDLE EAST
x0, y0, x1, y1 = P[1]
panel(x0, y0, x1, y1, "Middle East", YEL)
for i, c in enumerate([(60, 64, 80), (70, 74, 92), (80, 84, 104)]):
    d.rounded_rectangle([x0 + 60 + i * 78, y0 + 65, x0 + 120 + i * 78, y0 + 132], 8, fill=c, outline=(120, 128, 150))
    txt(x0 + 68 + i * 78, y0 + 84, "OIL", 20, True, YEL, x1, y1)
d.polygon([(x0 + 92, y0 + 58), (x0 + 106, y0 + 36), (x0 + 118, y0 + 54), (x0 + 130, y0 + 34), (x0 + 140, y0 + 58)], fill=(255, 120, 40))
txt(x0 + 28, y0 + 148, "Trump: no deal with Iran for now", 18, True, INK, x1, y1)
txt(x0 + 28, y0 + 170, "Gulf states urge restraint", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 192, "Houthis claim Saudi pipeline", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 214, "attacks; tanker mine-hit in Hormuz", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 236, "Gaza: 11 killed in Israeli strikes", 17, False, INK, x1, y1)

# 3. COP31
x0, y0, x1, y1 = P[2]
panel(x0, y0, x1, y1, "COP31 - Climate", GRN)
cx, cy, r = x0 + 115, y0 + 125, 72
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(40, 90, 140), outline=GRN, width=4)
for a, b in [(0.35, 0.15), (0.6, 0.4), (0.2, 0.5), (0.75, 0.6)]:
    d.ellipse([cx - r + a * 2 * r * 0.4, cy - r + b * 2 * r * 0.4,
               cx - r + a * 2 * r * 0.4 + 30, cy - r + b * 2 * r * 0.4 + 26], fill=(60, 150, 90))
d.rounded_rectangle([x0 + 260, y0 + 55, x0 + 283, y0 + 170], 11, fill=(70, 76, 96))
d.ellipse([x0 + 256, y0 + 162, x0 + 288, y0 + 194], fill=(255, 60, 60))
d.rounded_rectangle([x0 + 264, y0 + 100, x0 + 279, y0 + 176], 8, fill=(255, 60, 60))
txt(x0 + 320, y0 + 70, "Finance gap", 18, True, INK, x1, y1)
txt(x0 + 320, y0 + 94, "criticised;", 17, False, INK, x1, y1)
txt(x0 + 320, y0 + 118, "polluters", 17, False, INK, x1, y1)
txt(x0 + 320, y0 + 142, "asked to pay", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 220, "Guterres' farewell at COP31:", 18, True, INK, x1, y1)
txt(x0 + 28, y0 + 246, '"You cannot build peace on a burning planet"', 17, False, INK, x1, y1)

# 4. TECH
x0, y0, x1, y1 = P[3]
panel(x0, y0, x1, y1, "Tech", CYA)
d.rounded_rectangle([x0 + 40, y0 + 50, x0 + 130, y0 + 140], 10, fill=(40, 100, 60), outline=GRN, width=3)
txt(x0 + 58, y0 + 80, "GPU", 22, True, INK, x1, y1)
d.polygon([(x0 + 85, y0 + 165), (x0 + 55, y0 + 125), (x0 + 115, y0 + 125)], fill=ACC)
txt(x0 + 150, y0 + 62, "Nvidia CEO Jensen", 19, True, INK, x1, y1)
txt(x0 + 150, y0 + 86, "Huang resigns; Kress", 19, True, INK, x1, y1)
txt(x0 + 150, y0 + 110, "interim CEO", 19, True, INK, x1, y1)
txt(x0 + 28, y0 + 200, "Global Microsoft outage, 12h+:", 18, True, INK, x1, y1)
txt(x0 + 28, y0 + 226, "Outlook, Teams, Copilot down", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 250, "for millions worldwide", 17, False, INK, x1, y1)

# 5. ECONOMY
x0, y0, x1, y1 = P[4]
panel(x0, y0, x1, y1, "Economy", YEL)
txt(x0 + 28, y0 + 52, "GOLD  $3,902/oz", 25, True, YEL, x1, y1)
txt(x0 + 28, y0 + 84, "Fed rate-hike bets lift dollar;", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 106, "gold slides from record", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 128, "Gulf oil exports 18.4m bpd —", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 150, "still 26% below pre-war", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 178, "First global oil surplus since", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 200, "the war began (IEA)", 17, False, INK, x1, y1)
pts = [(x0 + 315 + i * 23, y0 + 175 - v) for i, v in enumerate([10, 30, 25, 45, 60, 50])]
d.line(pts, fill=YEL, width=4)

# 6. ASIA
x0, y0, x1, y1 = P[5]
panel(x0, y0, x1, y1, "Asia - Pacific", CYA)
txt(x0 + 28, y0 + 58, "APEC summit next week in", 19, True, INK, x1, y1)
txt(x0 + 28, y0 + 84, "Shenzhen — Xi to chair", 19, True, INK, x1, y1)
d.polygon([(x0 + 300, y0 + 160), (x0 + 335, y0 + 100), (x0 + 370, y0 + 160)], outline=(200, 160, 90), width=3)
d.rectangle([x0 + 328, y0 + 160, x0 + 342, y0 + 190], fill=(120, 95, 55))
txt(x0 + 28, y0 + 204, "SE Asian leaders + US, China", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 228, "alarmed by online-scam surge", 17, False, INK, x1, y1)
txt(x0 + 28, y0 + 252, "Japan PM Takaichi to visit", 16, False, INK, x1, y1)

# Footer
d.rectangle([0, H - 34, W, H], fill=(10, 13, 22))
d.line([(0, H - 34), (W, H - 34)], fill=(60, 68, 90), width=1)
txt(30, H - 27, "Compiled from 13 Nov 2026 wire reports - AP, Al Jazeera, Guardian, Xinhua, IEA", 15, False, FOOT, W, H)

bad = [c for c in checks if not (c[1] and c[2])]
img.save("/home/agentuser/news-image-repo/entry.png", optimize=True)
print("saved; bound violations:", bad)
