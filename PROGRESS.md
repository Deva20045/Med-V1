# PULSE Medicine Vol 1 — Progress

Updated **2026-10-01** (Chapter 1 shipped — first chapter live). Standalone offline quiz based on *PULSE Medicine Vol 1*, printed Book p1–375 (Marrow Edition 8).

- Repository: `Deva20045/Med-V1`
- Session branch: `arena/01a0f576-med-v1`
- Published URL: https://deva20045.github.io/Med-V1/
- Editable source of truth: `data/chNN.json`; generated offline deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- **Build status: 1 live chapter / 61 · 66 questions / 9 units.** All roadmap chapters are listed as Soon until live; Book p1–5 is fully covered.

## This release — Chapter 1 (Diarrhea)

The first Gastroenterology chapter — Diarrhea — covers Book p1–5 (`uploads/01.pdf` PDF13–17), was read line-to-line, source-ordered and made live. With this release learners can master the introductory diarrhea chapter without opening the PDF: definition, Bristol chart, physiology, frequency classification, pathological classifications and the approach flowchart are all encoded as ordered MCQs.

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 1 | Diarrhea | 1–5 | 66 | 9 |
| **Release total** |  | **5 book pages** | **66** | **9** |

### Quality and ordering contract delivered

1. All 5 pages were read top-to-bottom in printed order at 120 dpi (`/tmp/ch1_p01_dpi120.png` … `p05`), because the scan has no text layer. Visual extraction covered every heading, table cell (Frequency Classification, Chronic D/d, Osmotic vs Secretory comparison, Stool osmotic gap, Factitious findings, Small vs Large comparison), flowchart arm (Approach to Diarrhea), Bristol chart icons and labels, physiologic notes, numeric thresholds and “Active space” timers in exact book order. Verified page map: 01.pdf PDF13 = p1 Diarrhea start, PDF17 = p5 Approach end, PDF18 = p6 next chapter start. No sheets missing in p1–5.
2. Chapter 1 adds **66 ordered mappings** to `audit/coverage.json`; `tools/generate_ch01.py` regenerates the chapter file and appends the ledger idempotently, and every ledger point resolves to exactly one question.
3. Questions use all requested formats with non-obvious distractors and reasoning-first stems: fillup etc. (Full distribution: 6 fillup, 10 match, 18 recall, 4 oddoneout, 10 scenario, 11 truefalse, 6 numeric, 1 management — see validation output). No fill-up or match is predictable: match options require exact bijection, true/false uses balanced pairs, numeric thresholds use ±distractors, scenarios embed the full clinical table context.
4. IDs are sequential `MED-C1-01..66`; question array is strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, every unit guide is 2–4 lines, and every explanation ends with its exact `(Book pX)` citation.
5. Chapter 1 is embedded in the standalone app and live flag for Ch1 is set; **1/61 roadmap chapters are now live with 66 questions and 9 units — next chapter is Physiology of GIT Absorption and Selective Malabsorption (p6).**


## Verified PDF → printed-page map

Printed page numbers are ground truth. Every sheet used so far was rendered at 120 dpi and checked visually against the footer page number (e.g. “Medicine • v1.0 • Marrow 8.0 • 2024” footer with blue tab). `uploads/01.pdf` is sequential after 12 unnumbered front-matter sheets (cover, author, title, instructions, 8 pages of combined Contents); `uploads/02.pdf` continues at Book p118; `uploads/03.pdf` continues at Book p248. Full mappings are in [audit/page-map.json](audit/page-map.json).

- `uploads/01.pdf` PDF13–129 = Book p1–117 (Ch1 starts at PDF13)
- `uploads/02.pdf` PDF1–130  = Book p118–247
- `uploads/03.pdf` PDF1–128  = Book p248–375  (PDF129–131 are blank/end-quote Matter: “The practice of medicine ...”)
- **PDF → Book formula:** `01.pdf: Book p = PDF page − 12` (PDF page is 1-indexed; e.g. PDF13 → p1); `02.pdf: Book p = PDF page + 117`; `03.pdf: Book p = PDF page + 247`
- Chapter 1 (Diarrhea) uses 01.pdf PDF13–17 = Book p1–5

Verified page map: 01.pdf PDF13 = p1 Diarrhea start, PDF17 = p5 Approach to Diarrhea end, PDF18 = p6 next chapter “Physiology of GIT Absorption...” start. No sheets missing in p1–5.


## Schema and order contract

- Chapter: exact roadmap number/title, `pageRange` starts at the roadmap page, nonempty `questions` and `units`.
- Question: sequential `MED-C<N>-<seq>` ID; section/page/format/stem; exactly four unique options; one answer; explanation ending exactly `(Book pX)` matching `page`.
- Units: sequential `MED-U<N>-<n>` IDs; each has a 2–4-line guide; its IDs are rebuilt from exactly one section in original question order; flattened units equal the full chapter sequence.
- Questions are in printed book-page order; all printed pages in every live chapter are represented.
- The source-order inventory is fail-closed: the validator requires a ledger mapping for every question in audited Chapters 1–61, in exact question order and with matching book page.
- Questions are educational book-study material, not a substitute for current clinical guidelines or patient care.

## Build, audit and test workflow

```sh
# Generate/edit chapter artifacts only when source artefacts need regeneration.
python3 tools/generate_ch01.py           # Chapter 1 (Diarrhea)

# Fail-closed source gate, standalone-app build, and embedded-array gate.
python3 validate_content.py --ledger
python3 -m unittest discover -s tests -v
python3 build_content.py
python3 validate_content.py --embedded
node tests/app_parsers.cjs
```

## Per-chapter units

| Ch | Unit | Pages | Question range | Count |
|---:|---|---|---|---:|
| 1 | Definition & Bristol Chart | 1 | MED-C1-01–MED-C1-10 | 10 |
| 1 | Physiology & Macronutrients | 1 | MED-C1-11–MED-C1-15 | 5 |
| 1 | Frequency Classification & Acute Etiology | 1 | MED-C1-16–MED-C1-21 | 6 |
| 1 | Chronic Diarrhea & Malassimilation | 2 | MED-C1-22–MED-C1-24 | 3 |
| 1 | Osmotic Diarrhea & Steatorrhea | 2 | MED-C1-25–MED-C1-28 | 4 |
| 1 | Steatorrhea Investigations | 2 | MED-C1-29–MED-C1-34 | 6 |
| 1 | Secretory Diarrhea & Stool Osmotic Gap | 3 | MED-C1-35–MED-C1-44 | 10 |
| 1 | Factitious & Anatomical Classification | 4 | MED-C1-45–MED-C1-59 | 15 |
| 1 | Approach to Diarrhea | 5 | MED-C1-60–MED-C1-66 | 7 |


## Full roadmap

| Ch | Title | Starts | State |
|---:|---|---:|---|
| 1 | Diarrhea | 1 | **Live** |
| 2 | Physiology of GIT Absorption and Selective Malabsorption | 6 | Soon |
| 3 | Clinical Features And Tests For Malabsorption | 14 | Soon |
| 4 | Global Malabsorption | 18 | Soon |
| 5 | Inflammatory Bowel Disease : Part 1 | 30 | Soon |
| 6 | Inflammatory Bowel Disease : Part 2 | 37 | Soon |
| 7 | Infectious Diarrhoea | 46 | Soon |
| 8 | Stomach | 52 | Soon |
| 9 | Gastrinoma | 60 | Soon |
| 10 | Irritable Bowel Syndrome | 63 | Soon |
| 11 | Clinical Approach to Anemia | 66 | Soon |
| 12 | Iron Metabolism | 70 | Soon |
| 13 | Approach To Microcytic Hypochromic Anemia | 77 | Soon |
| 14 | Macrocytic Anemia | 82 | Soon |
| 15 | Approach to Hemolysis | 89 | Soon |
| 16 | Immune Mediated Hemolytic Anemia | 92 | Soon |
| 17 | Non-Immune Mediated Hemolytic Anemia | 97 | Soon |
| 18 | Hemolytic Anemia : Miscellaneous | 103 | Soon |
| 19 | Myeloproliferative Neoplasms : Part 1 | 107 | Soon |
| 20 | Myeloproliferative Neoplasms : Part 2 | 118 | Soon |
| 21 | Bone Marrow Failure Syndromes | 121 | Soon |
| 22 | Acute Leukemia | 126 | Soon |
| 23 | Acute Myeloid Leukemia V/S Acute Lymphoblastic Leukemia | 136 | Soon |
| 24 | World of Lymphomas | 140 | Soon |
| 25 | Chronic Lymphocytic Leukemia | 142 | Soon |
| 26 | Non-Hodgkin's Lymphoma | 146 | Soon |
| 27 | Hodgkin's Disease | 153 | Soon |
| 28 | Plasma Cell Disorders | 159 | Soon |
| 29 | Platelets - Basics | 169 | Soon |
| 30 | Approach to Bleeding Disorders | 173 | Soon |
| 31 | Clinical Anatomy of Lungs | 185 | Soon |
| 32 | Clinical Physiology of Lungs | 193 | Soon |
| 33 | Pulmonary Function Tests | 197 | Soon |
| 34 | Venous Thromboembolism | 206 | Soon |
| 35 | Pulmonary Hypertension | 213 | Soon |
| 36 | Bronchiectasis | 218 | Soon |
| 37 | Occupational Lung Diseases | 223 | Soon |
| 38 | Respiratory Failure and Acute Respiratory Distress Syndrome | 230 | Soon |
| 39 | Interstitial Lung Disease | 236 | Soon |
| 40 | Bronchial Asthma | 243 | Soon |
| 41 | Pulmonary Eosinophilia | 249 | Soon |
| 42 | Allergic Bronchopulmonary Aspergillosis | 253 | Soon |
| 43 | Hypersensitivity Pneumonitis | 257 | Soon |
| 44 | Pleural Effusion | 260 | Soon |
| 45 | Obstructive Sleep Apnea Syndrome | 264 | Soon |
| 46 | Chronic Obstructive Airway Disease | 267 | Soon |
| 47 | Community Acquired Pneumonia | 274 | Soon |
| 48 | Atypical Pneumonia and Pneumonia in Immunocompromised | 286 | Soon |
| 49 | Cardiac Cycle With Heart Sounds | 296 | Soon |
| 50 | Added Heart Sounds | 303 | Soon |
| 51 | Aortic Stenosis | 307 | Soon |
| 52 | Aortic Regurgitation | 313 | Soon |
| 53 | Heart Failure | 318 | Soon |
| 54 | Acute Decompensated Heart Failure | 326 | Soon |
| 55 | Cardiomyopathy : Part 1 | 331 | Soon |
| 56 | Cardiomyopathy : Part 2 | 336 | Soon |
| 57 | Mitral Regurgitation | 346 | Soon |
| 58 | Mitral Stenosis | 352 | Soon |
| 59 | CCP, CT, RCM and Acute Pericarditis | 358 | Soon |
| 60 | Pulse | 364 | Soon |
| 61 | Jugular Venous Pulse (JVP) | 370 | Soon |


## Per-chapter pipeline

1. Render source PDF pages at 120 dpi (e.g. `pymupdf` 120 dpi) and read visually line-to-line; no text layer exists.
2. Inventory every line, table cell, diagram label, flowchart arm, value and note in strict book order into `audit/coverage.json`.
3. Generate `data/chNN.json` with strict `MED-C<N>-<seq>` ordering, `page` nondecreasing, `exp` citing `(Book pX)`, units slicing by `sec`, guides 2–4 lines.
4. Run `validate_content.py`, `tests`, and `build_content.py` to embed; verify live flags and embedded arrays.
5. Commit, push, PR to `main` — live link updates via GitHub Pages.

*Next up:* **Chapter 2 — Physiology of GIT Absorption and Selective Malabsorption (p6)** — render `uploads/01.pdf` PDF18 onward, inventory p6–13, same pipeline.
