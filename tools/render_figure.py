"""Render a page (or a clip of a page) of an archived study PDF to a high-DPI PNG for
figure digitization by vision. GUI-free alternative to WebPlotDigitizer.

Usage:
  uv run python tools/render_figure.py <citekey> <page> [x0 y0 x1 y1] [--zoom N]
  - page is 1-indexed.
  - x0 y0 x1 y1 are clip fractions of the page (0..1); omit for the whole page.
Outputs temp/<citekey>_p<page>[_clip].png, then open it with the Read tool to read curves.
"""
from __future__ import annotations

import sys
from pathlib import Path

import fitz  # pymupdf

REPO = Path(__file__).resolve().parent.parent
PDF_DIR = REPO / "data/raw/literature/pdf"
OUT_DIR = REPO / "temp"


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    ck = sys.argv[1]
    page = int(sys.argv[2])
    zoom = 6.0
    if "--zoom" in sys.argv:
        zoom = float(sys.argv[sys.argv.index("--zoom") + 1])
    fracs = [a for a in sys.argv[3:] if a.replace(".", "", 1).isdigit()][:4]

    pdf = PDF_DIR / f"{ck}.pdf"
    if not pdf.exists():
        print(f"not found: {pdf}")
        return 1
    OUT_DIR.mkdir(exist_ok=True)
    doc = fitz.open(pdf)
    p = doc[page - 1]
    r = p.rect
    clip = None
    tag = ""
    if len(fracs) == 4:
        x0, y0, x1, y1 = (float(f) for f in fracs)
        clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
        tag = "_clip"
    pix = p.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    out = OUT_DIR / f"{ck}_p{page}{tag}.png"
    pix.save(out)
    doc.close()
    print(f"{out}  ({pix.width}x{pix.height})  zoom={zoom}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
