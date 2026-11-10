"""The PrepNova score card: a branded, shareable picture of one exam result.

After a mock, the result page shows the student a WhatsApp-ready image —
name, score (UTME marks /400, SSCE percentage + grade band, or plain
percentage), exam name, and the site address.  One tap posts it to a class
group; friends see the score, click through, and register.  Every card is
generated fresh from the result row, so it can never drift out of sync with
the verifiable result page.

Visual language is the house one (see _work/make_share_cards.py): navy→green
gradient, gold accents, Plus Jakarta Sans (static/fonts), 1080×1350 portrait —
large in WhatsApp chats and statuses alike.
"""
import io
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

_HERE = os.path.dirname(os.path.abspath(__file__))
_FONT_DIRS = (os.path.join(_HERE, "static", "fonts"), os.path.join(_HERE, "_work"))
_DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

W, H = 1080, 1350
NAVY = (15, 31, 61)
NAVY2 = (11, 59, 44)
GOLD = (247, 201, 72)
GOLD2 = (255, 216, 77)
WHITE = (255, 255, 255)
SOFT = (214, 222, 238)

_font_cache = {}


def _pjk(weight):
    for d in _FONT_DIRS:
        p = os.path.join(d, f"pjk-{weight}.ttf")
        if os.path.exists(p):
            return p
    return _DEJAVU


def font(weight, size):
    key = (weight, size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(_pjk(weight), size)
    return _font_cache[key]


def _fit(draw, text, weight, size, max_w):
    """Shrink the font until the text fits max_w; return the font actually usable."""
    while size > 18:
        f = font(weight, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(weight, size)


def _canvas():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(NAVY[i] + (NAVY2[i] - NAVY[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    orb = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(orb)
    od.ellipse([W - 420, -260, W + 300, 360], fill=(242, 183, 5, 66))
    od.ellipse([-300, H - 340, 380, H + 300], fill=(18, 168, 102, 72))
    orb = orb.filter(ImageFilter.GaussianBlur(100))
    img = Image.alpha_composite(img.convert("RGBA"), orb).convert("RGB")
    return img, ImageDraw.Draw(img)


def _brand(d):
    d.rounded_rectangle([72, 64, 118, 110], radius=12, fill=GOLD)
    d.text((95, 87), "PN", font=font(800, 22), fill=NAVY, anchor="mm")
    d.text((134, 87), "PrepNova CBT", font=font(700, 30), fill=WHITE, anchor="lm")


def _pill(d, center_x, top, text, weight, size, pad_x=34, pad_y=18):
    f = font(weight, size)
    tw = d.textlength(text, font=f)
    left = center_x - tw / 2 - pad_x
    right = center_x + tw / 2 + pad_x
    bottom = top + size + 2 * pad_y
    d.rounded_rectangle([left, top, right, bottom], radius=(bottom - top) / 2, fill=GOLD)
    d.text((center_x, (top + bottom) / 2), text, font=f, fill=NAVY, anchor="mm")
    return bottom


def _grade_band(exam_type, pct):
    if exam_type == "WAEC":
        from waec import grade
    elif exam_type == "NECO":
        from neco import grade
    else:
        return None
    return grade(pct)


def build_scorecard(result, display_name, site_url):
    """result: sqlite Row (or dict) from the results table. Returns PNG bytes."""
    exam_type = (result["exam_type"] or "CBT").upper()
    exam_name = (result["exam_name"] or "Mock exam").strip()
    pct = result["percentage"] or 0
    jamb_score = result["jamb_score"]
    first = ((display_name or "").strip().split() or ["I"])[0][:14]

    img, d = _canvas()
    _brand(d)
    cx = W // 2

    # eyebrow: exam name (caps, gold) — shrink to fit
    eyebrow = exam_name.upper()
    if exam_type in ("JAMB", "WAEC", "NECO", "POST-UTME"):
        eyebrow = f"{exam_type} · {eyebrow}"
    f_eb = _fit(d, eyebrow, 700, 34, W - 160)
    d.text((cx, 300), eyebrow, font=f_eb, fill=GOLD, anchor="mm")

    # name line
    d.text((cx, 392), f"{first} scored", font=font(500, 52), fill=WHITE, anchor="mm")

    # the big score
    if exam_type == "JAMB" and jamb_score is not None:
        big = str(jamb_score)
        f_big = font(800, 250)
        d.text((cx, 560), big, font=f_big, fill=WHITE, anchor="mm")
        sub = "out of 400 · JAMB UTME mock"
    else:
        big = f"{pct}%"
        f_big = font(800, 250)
        d.text((cx, 560), big, font=f_big, fill=WHITE, anchor="mm")
        band = _grade_band(exam_type, pct)
        if band:
            sub = f"Grade {band['band']} · {exam_type} standard"
        elif exam_type == "POST-UTME":
            sub = "screening score"
        else:
            sub = f"{result['score'] or 0}/{result['total'] or 0} correct"
    f_sub = _fit(d, sub, 500, 40, W - 200)
    d.text((cx, 740), sub, font=f_sub, fill=SOFT, anchor="mm")

    # challenge pill (honest: below 50% invite instead of challenge)
    pill_text = "CAN YOU BEAT ME?" if pct >= 50 else "PRACTISE WITH ME"
    pill_bottom = _pill(d, cx, 840, pill_text, 800, 36)

    # divider + supporting line
    d.line([(cx - 60, pill_bottom + 70), (cx + 60, pill_bottom + 70)], fill=(255, 255, 255, 40), width=2)
    d.text((cx, pill_bottom + 130), "Real CBT timer · every question explained", font=font(400, 30),
           fill=SOFT, anchor="mm")

    # bottom url block
    host = (site_url or "https://prepnova.pythonanywhere.com").replace("https://", "").replace("http://", "").rstrip("/")
    f_url = _fit(d, host, 700, 44, W - 200)
    d.text((cx, H - 150), host, font=f_url, fill=WHITE, anchor="mm")
    d.text((cx, H - 96), "Free 7-day trial — no card needed", font=font(500, 28), fill=GOLD2, anchor="mm")

    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return buf.getvalue()
