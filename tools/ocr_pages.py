#!/usr/bin/env python3
"""OCR a range of scanned sheets in reading order and save transcripts.

Scans in uploads/ have no text layer, so every chapter read is visual. This
helper produces a mechanical first pass (RapidOCR on a 4x render) that the
visual review in .audit-render/ is checked against; it never replaces it.

Usage: .venv/bin/python tools/ocr_pages.py uploads/04.pdf 35 60
Writes .audit-render/ocr_<pdf><sheet>.txt for each sheet.
"""
from __future__ import annotations
import sys
from pathlib import Path

import pymupdf
from rapidocr_onnxruntime import RapidOCR

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    pdf, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    tag = Path(pdf).stem
    out = ROOT / ".audit-render"
    out.mkdir(exist_ok=True)
    ocr = RapidOCR()
    doc = pymupdf.open(ROOT / pdf)
    for sheet in range(first, last + 1):
        page = doc[sheet - 1]
        png = out / f"{tag}_{sheet}_4x.png"
        page.get_pixmap(matrix=pymupdf.Matrix(4, 4)).save(png)
        result = ocr(str(png))
        lines = []
        if result and result[0]:
            rows = []
            for box, text, score in result[0]:
                ys = [p[1] for p in box]
                xs = [p[0] for p in box]
                rows.append((min(ys), min(xs), str(text), float(score)))
            rows.sort(key=lambda r: (round(r[0] / 14), r[1]))
            for y, x, text, score in rows:
                lines.append(f"{y:7.1f} {x:7.1f} {score:4.2f}  {text}")
        dest = out / f"ocr_{tag}{sheet}.txt"
        dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
        png.unlink()
        print(f"{tag} PDF{sheet}: {len(lines)} OCR lines -> {dest.name}", flush=True)


if __name__ == "__main__":
    main()
