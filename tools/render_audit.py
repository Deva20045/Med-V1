#!/usr/bin/env python3
"""Reproduce 2x scan renders for manual printed-number/content review.

Install pymupdf in a virtualenv. Rendered PNGs are intentionally ignored by Git.
No OCR/text extraction or arithmetic page-number inference is performed here.
"""
from pathlib import Path
import pymupdf

root = Path(__file__).resolve().parents[1]
out = root / '.audit-render'
out.mkdir(exist_ok=True)
with pymupdf.open(root / 'uploads/01.pdf') as doc:
    for pdf_page, page in enumerate(doc, 1):
        page.get_pixmap(matrix=pymupdf.Matrix(2, 2)).save(out / f'pdf{pdf_page}.png')
        print(f'Rendered PDF page {pdf_page}; read the printed number visually.')
