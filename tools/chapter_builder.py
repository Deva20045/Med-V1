#!/usr/bin/env python3
"""Shared deterministic writer for the Book p307–345 chapter artifacts.

The six generators remain separate, readable source files; this helper only
enforces the same schema, page ordering, four-option rule and deterministic
answer-position rotation used by the earlier chapters.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


class ChapterBuilder:
    def __init__(self, number: int, title: str, pages: str, seed: int):
        self.number = number
        self.title = title
        self.pages = pages
        self.seed = seed
        self.raw: list[tuple[str, int, str, str, list[str], int, str]] = []
        self.guides: dict[str, str] = {}

    def add(
        self,
        sec: str,
        page: int,
        fmt: str,
        stem: str,
        correct: str,
        distractors: list[str] | tuple[str, ...],
        explanation: str,
    ) -> None:
        options = [correct, *distractors]
        if len(options) != 4 or len(set(options)) != 4:
            raise ValueError(f"ch{self.number} {stem[:55]}: four distinct options required")
        if fmt not in {"recall", "fillup", "match", "truefalse", "scenario", "oddoneout", "numeric", "management"}:
            raise ValueError(f"ch{self.number}: unsupported format {fmt}")
        if fmt == "fillup" and "____" not in stem:
            raise ValueError(f"ch{self.number}: fill-up missing blank: {stem}")
        if fmt == "match":
            if " — 1) " not in stem or " … A) " not in stem:
                raise ValueError(f"ch{self.number}: match grammar: {stem}")
        if fmt == "truefalse":
            if sum(o.startswith("True") for o in options) != 2 or sum(o.startswith("False") for o in options) != 2:
                raise ValueError(f"ch{self.number}: true/false balance: {stem}")
        rng = random.Random(self.seed + len(self.raw) * 7907)
        rng.shuffle(options)
        answer = options.index(correct)
        exp = explanation.rstrip()
        suffix = f"(Book p{page})"
        if not exp.endswith(suffix):
            exp = f"{exp} {suffix}"
        self.raw.append((sec, page, fmt, stem, options, answer, exp))

    def guide(self, sec: str, text: str) -> None:
        lines = [line for line in text.strip().splitlines() if line.strip()]
        if not 2 <= len(lines) <= 4:
            raise ValueError(f"ch{self.number}: guide for {sec[:30]} must have 2–4 non-empty lines")
        self.guides[sec] = "\n".join(lines)

    def write(self) -> Path:
        pages = [row[1] for row in self.raw]
        if pages != sorted(pages):
            raise ValueError(f"ch{self.number}: questions must be authored in book-page order")
        first, last = map(int, self.pages.split("-", 1))
        if not pages or pages[0] != first or pages[-1] != last or set(pages) != set(range(first, last + 1)):
            raise ValueError(f"ch{self.number}: every page in {self.pages} must be represented")
        sections = list(dict.fromkeys(row[0] for row in self.raw))
        missing = [s for s in sections if s not in self.guides]
        if missing:
            raise ValueError(f"ch{self.number}: missing guides for {missing}")
        questions = []
        for i, (sec, page, fmt, stem, opts, ans, exp) in enumerate(self.raw, 1):
            questions.append({
                "id": f"MED-C{self.number}-{i:02d}",
                "sec": sec,
                "page": page,
                "fmt": fmt,
                "q": stem,
                "opts": opts,
                "ans": ans,
                "exp": exp,
            })
        units = []
        for n, sec in enumerate(sections, 1):
            units.append({
                "id": f"MED-U{self.number}-{n}",
                "ch": self.number,
                "n": n,
                "title": sec,
                "sec": sec,
                "guide": self.guides[sec],
                "qs": [q["id"] for q in questions if q["sec"] == sec],
            })
        DATA.mkdir(exist_ok=True)
        out = DATA / f"ch{self.number:02d}.json"
        out.write_text(json.dumps({
            "chapter": self.number,
            "title": self.title,
            "pageRange": self.pages,
            "questions": questions,
            "units": units,
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {out.name}: {len(questions)} questions / {len(units)} units")
        return out


if __name__ == "__main__":
    raise SystemExit("Import this helper from a chapter generator.")
