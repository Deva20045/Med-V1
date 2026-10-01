#!/usr/bin/env python3
"""Rebuild audit/coverage.json from the live chapter artifacts in data/.

The ledger is the human visual-review inventory: every printed point that a
question is built from, in strict book order. This helper regenerates it
deterministically from data/chNN.json so the order contract can never drift
from the shipped artifacts.
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
AUDIT = ROOT / "audit"


def main() -> None:
    ledger = []
    for path in sorted(DATA.glob("ch*.json")):
        chapter = json.loads(path.read_text(encoding="utf-8"))
        for q in chapter["questions"]:
            ledger.append({
                "chapter": chapter["chapter"],
                "page": q["page"],
                "point": f"{q['sec']} — {q['id']}: {q['q'][:70]}",
                "question": q["id"],
            })
    AUDIT.mkdir(exist_ok=True)
    (AUDIT / "coverage.json").write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote audit/coverage.json with {len(ledger)} inventoried points "
          f"across {len(set(r['chapter'] for r in ledger))} chapter(s).")


if __name__ == "__main__":
    main()
