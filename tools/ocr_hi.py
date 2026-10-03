#!/usr/bin/env python3
"""OCR one scanned sheet at high zoom, in horizontal bands, for fine print.

The 4x pass in tools/ocr_pages.py is a fast first read. Tables, flowcharts and
image labels in the PULSE scans are set small, so this helper re-renders a
single sheet at 8x and runs RapidOCR on three overlapping horizontal bands,
which keeps the detector effective on dense pages. It is still a mechanical
pass: it supports, and never replaces, visual review of the rendered sheet.

Usage: .venv/bin/python tools/ocr_hi.py uploads/01.pdf 119 [zoom] [bands]
Prints rows sorted top-to-bottom, left-to-right.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pymupdf
from rapidocr_onnxruntime import RapidOCR

ROOT = Path(__file__).resolve().parents[1]
SCRATCH = ROOT / ".audit-render"


def main() -> None:
    pdf, sheet = sys.argv[1], int(sys.argv[2])
    zoom = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
    bands = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    doc = pymupdf.open(ROOT / pdf)
    page = doc[sheet - 1]
    rect = page.rect
    ocr = RapidOCR()
    rows: list[tuple[float, float, str, float]] = []
    for index in range(bands):
        y0 = rect.height * index / bands
        y1 = rect.height * (index + 1) / bands
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(zoom, zoom),
            clip=pymupdf.Rect(0, y0, rect.width, y1),
        )
        png = SCRATCH / f"_hi_{Path(pdf).stem}{sheet}_{index}.png"
        png.parent.mkdir(exist_ok=True)
        pix.save(png)
        result = ocr(str(png))
        if result and result[0]:
            for box, text, score in result[0]:
                ys = [point[1] for point in box]
                xs = [point[0] for point in box]
                rows.append((min(ys) / zoom + y0, min(xs) / zoom, str(text), float(score)))
        png.unlink()
    rows.sort(key=lambda row: (round(row[0] / 7), row[1]))
    for y, x, text, score in rows:
        print(f"{y:7.1f} {x:7.1f} {score:4.2f}  {text}")


if __name__ == "__main__":
    main()
