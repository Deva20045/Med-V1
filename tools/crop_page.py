#!/usr/bin/env python3
"""Render a band of a scanned sheet for legible visual reading.

The scans have no text layer, so every chapter read is visual. This renders a
vertical band of a page (page-height fraction range) at a chosen zoom so lines
of printed text stay legible in the review image.

Usage: .venv/bin/python tools/crop_page.py uploads/04.pdf 35 0 0.52 3
  -> .audit-render/v04_35_a.png
"""
from __future__ import annotations
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".audit-render"


def main() -> None:
    pdf, sheet, y0f, y1f = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
    zoom = float(sys.argv[5]) if len(sys.argv) > 5 else 3.0
    x0f, x1f = (float(sys.argv[6]), float(sys.argv[7])) if len(sys.argv) > 7 else (0.0, 1.0)
    tag = Path(pdf).stem
    doc = pymupdf.open(ROOT / pdf)
    page = doc[sheet - 1]
    r = page.rect
    clip = pymupdf.Rect(x0f * r.width, y0f * r.height, x1f * r.width, y1f * r.height)
    out = OUT / f"v{tag}{sheet}_{int(y0f * 1000):03d}_{int(y1f * 1000):03d}_{int(zoom)}x.png"
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), clip=clip)
    pix.save(out)
    print(f"{out.relative_to(ROOT)}  {pix.width}x{pix.height}")


if __name__ == "__main__":
    main()
