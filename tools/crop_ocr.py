#!/usr/bin/env python3
"""Crop a region of a rendered scan sheet and OCR it at high zoom.

Usage: .venv/bin/python tools/crop_ocr.py uploads/04.pdf 61 x0 y0 x1 y1 [zoom]
Coordinates are in PDF points (origin top-left of the sheet). Prints OCR rows
sorted top-to-bottom, left-to-right so table columns can be reconstructed.
"""
from __future__ import annotations
import sys
from pathlib import Path

import pymupdf
from rapidocr_onnxruntime import RapidOCR

ROOT = Path(__file__).resolve().parents[1]
ocr = RapidOCR()


def main() -> None:
    pdf, sheet = sys.argv[1], int(sys.argv[2])
    x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
    zoom = float(sys.argv[7]) if len(sys.argv) > 7 else 8.0
    doc = pymupdf.open(ROOT / pdf)
    page = doc[sheet - 1]
    clip = pymupdf.Rect(x0, y0, x1, y1)
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), clip=clip)
    png = ROOT / ".audit-render" / f"crop_{Path(pdf).stem}{sheet}_{int(x0)}_{int(y0)}.png"
    pix.save(png)
    result = ocr(str(png))
    if result and result[0]:
        rows = []
        for box, text, score in result[0]:
            ys = [p[1] for p in box]
            xs = [p[0] for p in box]
            rows.append((min(ys) / zoom + y0, min(xs) / zoom + x0, str(text), float(score)))
        rows.sort(key=lambda r: (round(r[0] / 7), r[1]))
        for y, x, text, score in rows:
            print(f"{y:7.1f} {x:7.1f} {score:4.2f}  {text}")
    else:
        print("(no text found)")


if __name__ == "__main__":
    main()
