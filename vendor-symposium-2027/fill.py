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
MASTERCARD = None
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
BUSINESS_TYPE = {"supplies": False, "services": True, "construction": True}

ABOUT = [
    "Okinawa-based first-class registered architect office and licensed general contractor providing building inspection,",
    "design, construction and pool services. Led by a first-class registered architect and first-class certified waterproofing",
    "technician (PVC membrane), we build and restore swimming pools and outdoor spaces built for Okinawa's coastal climate.",
]
CAPS = [
    "- Swimming pool design & construction: residential, hotel and facility pools",
    "- Pool renovation & leak repair: PVC membrane re-lining, waterproofing, salt-damage & corrosion repair, tile restoration",
    "- Pool equipment installation: filtration systems, pumps and lighting",
    "- Pool & building inspection: leak investigation, waterproofing and concrete deterioration (salt damage) surveys",
    "- Outdoor living: decks, pergolas, exterior works and landscape",
    "Licenses: Construction Business License (Okinawa Pref.) / First-Class Architect Office / Real Estate Brokerage",
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
    c.setFillColor(HexColor("#c8d1db"))
    c.roundRect(X(22), Y(518), X(355), X(338), X(38), stroke=0, fill=1)
    if logo_path and os.path.exists(logo_path):
        pad = X(30)
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
        fit(c, l, X(22), Y(728) - i * 32, 24, 1610)
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
