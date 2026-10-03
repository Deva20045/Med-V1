#!/usr/bin/env python3
"""Embed the chapter JSON artifacts into the standalone PULSE Medicine Vol 1 app.

The browser app is intentionally a single offline HTML file. Structured chapter
artifacts in data/chNN.json are the editable source of truth; run this script
whenever a chapter artifact changes. Chapters without an artifact remain on
the roadmap as "Soon" (live: false).
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_PATH = ROOT / "pulse-medicine.html"
DATA_PATH = ROOT / "data"

# Full Volume-1 roadmap (Book p1-375) from the book's Contents pages,
# cross-verified against the scanned chapter title pages (uploads/01.pdf PDF13 = p1).
# Number, title, starting Book page. The "p" shown on the roadmap is the starting page.
CHAPTERS = [
    (1, "Diarrhea", 1),
    (2, "Physiology of GIT Absorption and Selective Malabsorption", 6),
    (3, "Clinical Features And Tests For Malabsorption", 14),
    (4, "Global Malabsorption", 18),
    (5, "Inflammatory Bowel Disease : Part 1", 30),
    (6, "Inflammatory Bowel Disease : Part 2", 37),
    (7, "Infectious Diarrhoea", 46),
    (8, "Stomach", 52),
    (9, "Gastrinoma", 60),
    (10, "Irritable Bowel Syndrome", 63),
    (11, "Clinical Approach to Anemia", 66),
    (12, "Iron Metabolism", 70),
    (13, "Approach To Microcytic Hypochromic Anemia", 77),
    (14, "Macrocytic Anemia", 82),
    (15, "Approach to Hemolysis", 89),
    (16, "Immune Mediated Hemolytic Anemia", 92),
    (17, "Non-Immune Mediated Hemolytic Anemia", 97),
    (18, "Hemolytic Anemia : Miscellaneous", 103),
    (19, "Myeloproliferative Neoplasms : Part 1", 107),
    # Contents pages print 118, but the scanned chapter heading
    # "MYELOPROLIFERATIVE NEOPLASMS : PART 2" (and the CML pathophysiology
    # that follows it) starts on Book p116; the scan is ground truth.
    (20, "Myeloproliferative Neoplasms : Part 2", 116),
    (21, "Bone Marrow Failure Syndromes", 121),
    (22, "Acute Leukemia", 126),
    (23, "Acute Myeloid Leukemia V/S Acute Lymphoblastic Leukemia", 136),
    (24, "World of Lymphomas", 140),
    (25, "Chronic Lymphocytic Leukemia", 142),
    (26, "Non-Hodgkin's Lymphoma", 146),
    (27, "Hodgkin's Disease", 153),
    (28, "Plasma Cell Disorders", 159),
    (29, "Platelets - Basics", 169),
    (30, "Approach to Bleeding Disorders", 173),
    (31, "Clinical Anatomy of Lungs", 185),
    (32, "Clinical Physiology of Lungs", 193),
    (33, "Pulmonary Function Tests", 197),
    (34, "Venous Thromboembolism", 206),
    (35, "Pulmonary Hypertension", 213),
    (36, "Bronchiectasis", 218),
    (37, "Occupational Lung Diseases", 223),
    (38, "Respiratory Failure and Acute Respiratory Distress Syndrome", 230),
    (39, "Interstitial Lung Disease", 236),
    (40, "Bronchial Asthma", 243),
    (41, "Pulmonary Eosinophilia", 249),
    (42, "Allergic Bronchopulmonary Aspergillosis", 253),
    (43, "Hypersensitivity Pneumonitis", 257),
    (44, "Pleural Effusion", 260),
    (45, "Obstructive Sleep Apnea Syndrome", 264),
    (46, "Chronic Obstructive Airway Disease", 267),
    (47, "Community Acquired Pneumonia", 274),
    (48, "Atypical Pneumonia and Pneumonia in Immunocompromised", 286),
    (49, "Cardiac Cycle With Heart Sounds", 296),
    (50, "Added Heart Sounds", 303),
    (51, "Aortic Stenosis", 307),
    (52, "Aortic Regurgitation", 313),
    (53, "Heart Failure", 318),
    (54, "Acute Decompensated Heart Failure", 326),
    (55, "Cardiomyopathy : Part 1", 331),
    (56, "Cardiomyopathy : Part 2", 336),
    (57, "Mitral Regurgitation", 346),
    (58, "Mitral Stenosis", 352),
    (59, "CCP, CT, RCM and Acute Pericarditis", 358),
    (60, "Pulse", 364),
    (61, "Jugular Venous Pulse (JVP)", 370),
]


def compact(value: object) -> str:
    """Use compact, UTF-8 JSON so the standalone app remains easy to ship."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def between(text: str, start: str, end: str) -> tuple[int, int]:
    first = text.index(start)
    second = text.index(end, first)
    return first, second


def main() -> None:
    # Fail before touching the offline HTML if schema, inventory or app parsing
    # regresses. The visual self-audit is recorded separately in audit/SELF_AUDIT.md.
    from validate_content import validate_all
    validate_all()

    questions: list[dict] = []
    units: list[dict] = []
    live: dict[int, dict] = {}

    for number, title, start_page in CHAPTERS:
        path = DATA_PATH / f"ch{number:02d}.json"
        if not path.exists():
            continue
        chapter = json.loads(path.read_text(encoding="utf-8"))
        if chapter["chapter"] != number:
            raise ValueError(f"{path.name}: chapter number does not match filename")
        if chapter["title"] != title:
            raise ValueError(
                f"{path.name}: expected title {title!r}, got {chapter['title']!r}"
            )
        first = int(chapter["pageRange"].split("-", 1)[0])
        if first != start_page:
            raise ValueError(
                f"{path.name}: pageRange starts at {first}, expected {start_page}"
            )
        questions.extend(chapter["questions"])
        units.extend(chapter["units"])
        live[number] = chapter

    html = APP_PATH.read_text(encoding="utf-8")
    q_start, _ = between(html, "const QUESTIONS = ", "\nconst UNITS = ")
    u_start, _ = between(html, "const UNITS = ", "\nconst CHAPTERS = ")
    c_start, c_end = between(html, "const CHAPTERS = ", "\nconst QBYID = ")

    roadmap = []
    for number, title, start_page in CHAPTERS:
        if number in live:
            first = int(live[number]["pageRange"].split("-", 1)[0])
            roadmap.append({"n": number, "t": title, "p": first, "live": True})
        else:
            roadmap.append({"n": number, "t": title, "p": start_page, "live": False})

    html = (
        html[:q_start]
        + "const QUESTIONS = "
        + compact(questions)
        + ";\nconst UNITS = "
        + compact(units)
        + ";\nconst CHAPTERS = "
        + json.dumps(roadmap, ensure_ascii=False, indent=2)
        + ";"
        + html[c_end:]
    )
    APP_PATH.write_text(html, encoding="utf-8")
    live_count = len(live)
    print(
        f"Embedded {len(questions)} questions and {len(units)} units across "
        f"{live_count} live chapter(s) of {len(CHAPTERS)} roadmap chapters "
        f"in {APP_PATH.name}."
    )


if __name__ == "__main__":
    main()
