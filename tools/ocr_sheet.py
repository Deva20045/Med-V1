#!/usr/bin/env python3
"""OCR rendered scan sheets and print text in reading order (top-to-bottom).

Scans contain no extractable text layer, so the Chapter reads are visual. This
helper gives a mechanical first pass via RapidOCR (ONNX), to be cross-checked
against the rendered image; it does NOT replace visual review.
"""
from __future__ import annotations

import sys
from pathlib import Path

from rapidocr_onnxruntime import RapidOCR

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    ocr = RapidOCR()
    for arg in sys.argv[1:]:
        path = (ROOT / arg) if not Path(arg).is_absolute() else Path(arg)
        result = ocr(str(path))
        print(f"\n===== {path.name} =====")
        if not result or not result[0]:
            print("(no text detected)")
            continue
        items = result[0]
        # Each item: [box(4 pts), text, score]. Sort top-to-bottom, left-to-right.
        rows = []
        for box, text, score in items:
            ys = [p[1] for p in box]
            xs = [p[0] for p in box]
            rows.append((min(ys), min(xs), str(text), float(score)))
        rows.sort(key=lambda r: (round(r[0] / 12), r[1]))
        for y, x, text, score in rows:
            print(f"{y:7.1f} {x:7.1f}  {text}")


if __name__ == "__main__":
    main()
