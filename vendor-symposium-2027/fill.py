"""2027 Okinawa Vendor Symposium pamphlet generator (CROTON Co., Ltd.)

usage: python3 fill.py "2027 Vendor Pamphlet Template.pdf" "Croton Co., Ltd..pdf"
Draws text over the organizer's template and removes its form fields.
Edit the SETTINGS block below, then re-run.
"""
import io
import os
import sys

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

# ===== SETTINGS ============================================================
# MasterCard accepted?  "yes" / "no" / None (= leave blank; decide before submitting)
MASTERCARD = "yes"
# Official logo image (PNG/JPG). None or missing file = text wordmark placeholder.
LOGO = "croton_logo.png"

COMPANY = "CROTON Co., Ltd."
ROWS = {  # template y (px) -> text   (address/phone confirmed by 2026-11 invoice data)
    218: "N/A (not required for this event)",
    295: "1-53-13 Asacha, Urasoe, Okinawa 901-2114 (Toyofuku Bldg. 2F)",
    372: "Tetsuro Shimoji, President & CEO",
    449: "+81-98-877-9610",
    527: "croton@croton.okinawa",
    604: "Pools: croton.okinawa/poollife    Company: croton.jp",
}
BUSINESS_TYPE = {"supplies": True, "services": True, "construction": True}

ABOUT = [
    "Okinawa-based licensed general contractor and first-class registered architect office, founded in 2004, providing building inspection,",
    "design, construction and pool services. Led by a certified construction manager, a first-class waterproofing technician and a first-class",
    "registered architect, we build pools and outdoor spaces designed for Okinawa's climate. Over 100 pools delivered in Okinawa.",
    "Authorized Desjoyaux Japan Partner (Okinawa): Desjoyaux pool systems with built-in filtration - no buried piping, no equipment room. 60 years of history.",
]
CAPS = [
    "- Swimming pool design & construction: residential, hotel and facility pools",
    "- Pool equipment installation (supplied & installed as part of our work): filtration, pumps, heat pumps, cleaning robots, lighting",
    "- Sauna supply & installation: outdoor/indoor saunas for residences, hotels and facilities",
    "- Outdoor living: decks, pergolas, exterior works and landscape",
    "Licenses: Okinawa Gov. Construction License (General) No. 12065 / First-Class Architect Office Reg. No. 183-2732 / Real Estate License (3) No. 4410",
]
# ===========================================================================

W, H = 1683.75, 1190.25
k = 72 / 70
X = lambda px: px * k
Y = lambda py: H - py * k
navy = HexColor("#062a5a")


def fit(c, text, x, y, size, maxw, font="Helvetica"):
    """Draw text, shrinking the font so it never exceeds maxw."""
    while size > 10 and stringWidth(text, font, size) > maxw:
        size -= 0.5
    c.setFont(font, size)
    c.drawString(x, y, text)
    return size


def check(c, px, py):
    c.setLineWidth(5)
    c.line(X(px - 12), Y(py), X(px - 3), Y(py + 12))
    c.line(X(px - 3), Y(py + 12), X(px + 14), Y(py - 14))


def overlay(logo_path):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H))
    # logo box
    c.setFillColor(HexColor("#ffffff")); c.setStrokeColor(HexColor("#c8d1db")); c.setLineWidth(2)
    c.roundRect(X(20), Y(520), X(359), X(350), X(38), stroke=1, fill=1)
    c.setStrokeColor(navy)
    if logo_path and os.path.exists(logo_path):
        pad = X(18)
        c.drawImage(logo_path, X(22) + pad, Y(518) + pad, X(355) - 2 * pad, X(338) - 2 * pad,
                    preserveAspectRatio=True, anchor="c", mask="auto")
    else:
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 72); c.drawCentredString(X(200), Y(345), "CROTON")
        c.setFont("Helvetica", 24); c.drawCentredString(X(200), Y(392), "Pool & Outdoor Living")
    # company name
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 36); c.drawCentredString(X(200), Y(578), COMPANY)
    # info rows (field width ~ 612pt)
    for py, t in ROWS.items():
        size = 24 if len(t) < 50 else 20
        fit(c, t, X(685), Y(py) - size * 0.35, size, 600)
    # business type / MasterCard checkboxes
    for key, py in (("supplies", 303), ("services", 352), ("construction", 401)):
        if BUSINESS_TYPE[key]:
            check(c, 1328, py)
    if MASTERCARD == "yes":
        check(c, 1328, 557)
    elif MASTERCARD == "no":
        check(c, 1328, 607)
    # about / capabilities (box width ~ 1620pt)
    for i, l in enumerate(ABOUT):
        fit(c, l, X(22), Y(722) - i * 29, 22, 1610,
            font="Helvetica-Bold" if l.startswith("Authorized") else "Helvetica")
    for i, l in enumerate(CAPS):
        fit(c, l, X(22), Y(900) - i * 34, 24, 1610,
            font="Helvetica-Bold" if l.startswith("Licenses") else "Helvetica")
    c.save()
    buf.seek(0)
    return PdfReader(buf)


def main():
    src, out = sys.argv[1], sys.argv[2]
    here = os.path.dirname(os.path.abspath(__file__))
    logo = LOGO if (LOGO is None or os.path.isabs(LOGO)) else os.path.join(here, LOGO)
    base = PdfReader(src)
    p = base.pages[0]
    if "/Annots" in p:
        del p["/Annots"]
    p.merge_page(overlay(logo).pages[0])
    w = PdfWriter()
    w.add_page(p)
    if "/AcroForm" in w._root_object:
        del w._root_object["/AcroForm"]
    w.write(out)
    if MASTERCARD is None:
        print("NOTE: MasterCard Yes/No is still blank (set MASTERCARD in fill.py)")
    if not (logo and os.path.exists(logo)):
        print("NOTE: logo image not found -> text placeholder used")


if __name__ == "__main__":
    main()
