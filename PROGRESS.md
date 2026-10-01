# PULSE Medicine Vol 1 — Progress

Updated **2026-10-01** (Chapters 1–6 shipped — Gastroenterology block live). Standalone offline quiz based on *PULSE Medicine Vol 1*, printed Book p1–375 (Marrow Edition 8).

- Repository: `Deva20045/Med-V1`
- Session branch: `arena/01a0f576-med-v1`
- Published URL: https://deva20045.github.io/Med-V1/
- Editable source of truth: `data/chNN.json`; generated offline deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- **Build status: 6 live chapters / 61 · 714 questions / 77 units.** All remaining roadmap chapters are listed as Soon; Book p1–45 is fully covered line to line.

## This release — Chapters 1 to 6 (Gastroenterology, Book p1–45)

Every chapter was read sheet-by-sheet from the scanned source in printed order, inventoried line to line, and encoded as strictly ordered questions with non-predictable distractors. Chapters 2–6 were added in this release on top of Chapter 1.

| Ch | Title | Printed pages | PDF sheets | Questions | Units |
|---:|---|---:|---:|---:|---:|
| 1 | Diarrhea | 1–5 | 01.pdf PDF13–17 | 66 | 9 |
| 2 | Physiology of GIT Absorption and Selective Malabsorption | 6–13 | 01.pdf PDF18–25 | 150 | 15 |
| 3 | Clinical Features And Tests For Malabsorption | 14–17 | 01.pdf PDF26–29 | 80 | 9 |
| 4 | Global Malabsorption | 18–29 | 01.pdf PDF30–41 | 196 | 19 |
| 5 | Inflammatory Bowel Disease : Part 1 | 30–36 | 01.pdf PDF42–48 | 94 | 11 |
| 6 | Inflammatory Bowel Disease : Part 2 | 37–45 | 01.pdf PDF49–57 | 128 | 14 |
| **Release total** |  | **45 book pages** |  | **714** | **77** |

Question format distribution across the release: 444 recall, 78 match, 61 numeric, 41 fillup, 36 scenario, 32 oddoneout, 20 truefalse, 2 management.

### Chapter 2 — Physiology of GIT Absorption and Selective Malabsorption (p6–13)

Stages of absorption and their anatomy, small-intestinal histology, the luminal–mucosal–post-mucosal fat pathway, bile acid physiology (500 g formed and excreted daily, 4 g pool), carbohydrate transporters and disaccharidases, protein absorption, lactase deficiency and lactose intolerance, abetalipoproteinemia and intestinal lymphangiectasia.

### Chapter 3 — Clinical Features And Tests For Malabsorption (p14–17)

Steps for evaluating malabsorption, the full clinical-feature list by system, fat malabsorption tests, the D-xylose test (25 g orally, urine over 4–6 hours, normal at least 4.5 g) with its false-positive causes, hydrogen breath tests, obsolete tests and biopsy diagnoses, and the Schilling test with its four phases.

### Chapter 4 — Global Malabsorption (p18–29)

Celiac disease (iceberg phenomenon, types, pathophysiology, associations, serology and biopsy, complications, gluten-free response), Whipple's disease, tropical sprue, bile acid versus fatty acid diarrhea, short bowel syndrome (below 200 cm, very severe below 100 cm) and small intestinal bacterial overgrowth (jejunal aspirate above 10³ CFU/mL as gold standard, rifaximin first line, macrolides avoided).

### Chapter 5 — Inflammatory Bowel Disease : Part 1 (p30–36)

Entities of IBD, microscopic and diversion colitis, normal colonic histology, epidemiology of UC and Crohn's, genetic syndromes, IPEX syndrome and early onset childhood IBD, pathogenesis, and the site, macroscopy and microscopy of both ulcerative colitis and Crohn's disease.

### Chapter 6 — Inflammatory Bowel Disease : Part 2 (p37–45)

Ulcerative colitis clinical features and endoscopy, barium enema, Crohn's clinical features, endoscopic and cross-sectional imaging signs, intestinal tuberculosis versus Crohn's disease, extraintestinal manifestations, other investigations and serology, Truelove and Witt's classification, medical management of UC, sulfasalazine and surgery, Crohn's grading and severity-based management, and malignancy in IBD.

## Quality and ordering contract delivered

1. Every printed page p1–45 was read top-to-bottom in printed order from the scans (no text layer exists), so headings, table cells, image labels, flowchart arms, numeric thresholds and notes are captured in exact book order. Verified page map: `01.pdf` PDF13 = p1 … PDF57 = p45; no sheets missing.
2. `audit/coverage.json` now holds **714 inventoried points** across the six audited chapters; every ledger point resolves to exactly one question, in exact question order, with the matching book page.
3. Distractors are not predictable: match options require an exact bijection and are shuffled, true/false uses balanced True/False pairs, numeric thresholds use nearby plausible values, scenarios embed the full clinical context, and fill-ups target a single printed word.
4. IDs are sequential `MED-C<N>-<seq>`; the question array is strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, every unit guide is 2–4 lines, and every explanation ends with its exact `(Book pX)` citation matching the question page.
5. All six chapters are embedded in the standalone app with their live flags set; **6/61 roadmap chapters are now live — next chapter is Infectious Diarrhoea (p46).**

## Verified PDF → printed-page map

Printed page numbers are ground truth. `uploads/01.pdf` is sequential after 12 unnumbered front-matter sheets (cover, author, title, instructions, 8 pages of combined Contents); `uploads/02.pdf` continues at Book p118; `uploads/03.pdf` continues at Book p248. Full mappings are in [audit/page-map.json](audit/page-map.json).

- `uploads/01.pdf` PDF13–129 = Book p1–117
- `uploads/02.pdf` PDF1–130  = Book p118–247
- `uploads/03.pdf` PDF1–128  = Book p248–375  (PDF129–131 are blank/end-quote matter)
- **PDF → Book formula:** `01.pdf: Book p = PDF page − 12`; `02.pdf: Book p = PDF page + 117`; `03.pdf: Book p = PDF page + 247`

Chapter sheet coverage verified so far:

| Ch | Book pages | 01.pdf sheets |
|---:|---|---|
| 1 | 1–5 | PDF13–17 |
| 2 | 6–13 | PDF18–25 |
| 3 | 14–17 | PDF26–29 |
| 4 | 18–29 | PDF30–41 |
| 5 | 30–36 | PDF42–48 |
| 6 | 37–45 | PDF49–57 |
| 7 (next) | 46 | PDF58 |

## Schema and order contract

- Chapter: exact roadmap number/title, `pageRange` starts at the roadmap page, nonempty `questions` and `units`.
- Question: sequential `MED-C<N>-<seq>` ID; section/page/format/stem; exactly four unique options; one answer; explanation ending exactly `(Book pX)` matching `page`.
- Units: sequential `MED-U<N>-<n>` IDs; each has a 2–4-line guide; its IDs are rebuilt from exactly one section in original question order; flattened units equal the full chapter sequence.
- Questions are in printed book-page order; all printed pages in every live chapter are represented.
- The source-order inventory is fail-closed: the validator requires a ledger mapping for every question in audited Chapters 1–61, in exact question order and with matching book page.
- Questions are educational book-study material, not a substitute for current clinical guidelines or patient care.

## Build, audit and test workflow

```sh
# Generate chapter artifacts (one generator per chapter).
python3 tools/generate_ch0N.py
python3 tools/update_ledger.py     # rebuilds audit/coverage.json from every data/ch*.json

# Fail-closed source gate, standalone-app build, and embedded-array gate.
python3 validate_content.py
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
| 2 | Basics of Absorption & Stages | 6 | MED-C2-01–MED-C2-09 | 9 |
| 2 | Anatomy of the Small Intestine | 6 | MED-C2-10–MED-C2-15 | 6 |
| 2 | Histology: Mucosa | 6 | MED-C2-16–MED-C2-29 | 14 |
| 2 | Small Intestine Layers & Peyer's Patches | 7 | MED-C2-30–MED-C2-34 | 5 |
| 2 | Fat Absorption: Luminal Phase | 7 | MED-C2-35–MED-C2-40 | 6 |
| 2 | Bile Acid Physiology | 7 | MED-C2-41–MED-C2-50 | 10 |
| 2 | Defects in Luminal & Mucosal Phase | 8 | MED-C2-51–MED-C2-58 | 8 |
| 2 | Post-Mucosal Phase & Types of Fatty Acids | 8 | MED-C2-59–MED-C2-74 | 16 |
| 2 | Carbohydrate Absorption Mechanism | 9 | MED-C2-75–MED-C2-88 | 14 |
| 2 | Defects in Carbohydrate Absorption | 9–10 | MED-C2-89–MED-C2-93 | 5 |
| 2 | Protein Absorption & Selective Defects | 10 | MED-C2-94–MED-C2-102 | 9 |
| 2 | Lactose Intolerance: Physiology to Pathogenesis | 10–11 | MED-C2-103–MED-C2-116 | 14 |
| 2 | Lactose Intolerance: Presentation & Investigations | 11 | MED-C2-117–MED-C2-125 | 9 |
| 2 | Abetalipoproteinemia | 12 | MED-C2-126–MED-C2-137 | 12 |
| 2 | Intestinal Lymphangiectasia | 13 | MED-C2-138–MED-C2-150 | 13 |
| 3 | Steps for Evaluating Malabsorption | 14 | MED-C3-01–MED-C3-05 | 5 |
| 3 | Clinical Features: Gastrointestinal | 14 | MED-C3-06–MED-C3-15 | 10 |
| 3 | Clinical Features: Musculoskeletal & Cutaneous | 14 | MED-C3-16–MED-C3-23 | 8 |
| 3 | Clinical Features: Miscellaneous & Kidney Stones | 14–15 | MED-C3-24–MED-C3-39 | 16 |
| 3 | Fat Malabsorption Tests | 15 | MED-C3-40–MED-C3-44 | 5 |
| 3 | D-Xylose Test | 15 | MED-C3-45–MED-C3-52 | 8 |
| 3 | False Positives & Hydrogen Breath Tests | 16 | MED-C3-53–MED-C3-63 | 11 |
| 3 | Obsolete Tests & Biopsy Diagnoses | 16 | MED-C3-64–MED-C3-71 | 8 |
| 3 | Schilling Test | 17 | MED-C3-72–MED-C3-80 | 9 |
| 4 | Global Malabsorption: Overview | 18 | MED-C4-01–MED-C4-05 | 5 |
| 4 | Celiac Disease: Features & Iceberg Phenomenon | 18 | MED-C4-06–MED-C4-12 | 7 |
| 4 | Celiac Disease: Types | 18 | MED-C4-13–MED-C4-18 | 6 |
| 4 | Celiac Pathophysiology & Disease Progression | 19 | MED-C4-19–MED-C4-33 | 15 |
| 4 | Celiac Clinical Features | 20 | MED-C4-34–MED-C4-47 | 14 |
| 4 | Celiac Associations | 20 | MED-C4-48–MED-C4-54 | 7 |
| 4 | Celiac Diagnosis: Serology & Biopsy | 21 | MED-C4-55–MED-C4-70 | 16 |
| 4 | Celiac Interpretation, Complications & Treatment | 22 | MED-C4-71–MED-C4-80 | 10 |
| 4 | Whipple's Disease: Presentation | 22 | MED-C4-81–MED-C4-86 | 6 |
| 4 | Whipple's Disease: Clinical Features | 23 | MED-C4-87–MED-C4-105 | 19 |
| 4 | Whipple's Disease: Diagnosis & Treatment | 24 | MED-C4-106–MED-C4-111 | 6 |
| 4 | Tropical Sprue: Pathogenesis | 24 | MED-C4-112–MED-C4-119 | 8 |
| 4 | Tropical Sprue: Features, Investigations & Treatment | 25 | MED-C4-120–MED-C4-131 | 12 |
| 4 | Bile Acid Diarrhea & Fatty Acid Diarrhea | 25–26 | MED-C4-132–MED-C4-143 | 12 |
| 4 | Short Bowel Syndrome: Definition & Etiology | 26 | MED-C4-144–MED-C4-147 | 4 |
| 4 | Short Bowel Syndrome: Clinical Presentation | 27 | MED-C4-148–MED-C4-160 | 13 |
| 4 | Short Bowel Syndrome: Deficiencies & Management | 28 | MED-C4-161–MED-C4-168 | 8 |
| 4 | SIBO: Physiology, Pathology & Etiology | 28 | MED-C4-169–MED-C4-175 | 7 |
| 4 | SIBO: Presentation, Investigations & Management | 29 | MED-C4-176–MED-C4-196 | 21 |
| 5 | Entities of IBD & Microscopic Colitis | 30 | MED-C5-01–MED-C5-09 | 9 |
| 5 | Diversion Colitis & Normal Histology of Colon | 30 | MED-C5-10–MED-C5-13 | 4 |
| 5 | Colonic Mucosa & Definition of Diarrhea | 31 | MED-C5-14–MED-C5-17 | 4 |
| 5 | Epidemiology of UC and Crohn's Disease | 31 | MED-C5-18–MED-C5-30 | 13 |
| 5 | Genetic Syndromes Associated with IBD | 32 | MED-C5-31–MED-C5-41 | 11 |
| 5 | IPEX Syndrome & Early Onset Childhood IBD | 32–33 | MED-C5-42–MED-C5-50 | 9 |
| 5 | Pathogenesis of IBD | 33 | MED-C5-51–MED-C5-58 | 8 |
| 5 | Ulcerative Colitis: Site & Macroscopy | 34 | MED-C5-59–MED-C5-67 | 9 |
| 5 | Ulcerative Colitis: Microscopy | 35 | MED-C5-68–MED-C5-73 | 6 |
| 5 | Crohn's Disease: Site & Macroscopy | 35 | MED-C5-74–MED-C5-86 | 13 |
| 5 | Crohn's Disease: Microscopy | 36 | MED-C5-87–MED-C5-94 | 8 |
| 6 | Ulcerative Colitis: Clinical Features | 37 | MED-C6-01–MED-C6-09 | 9 |
| 6 | Fecal Calprotectin & Endoscopy in UC | 37 | MED-C6-10–MED-C6-16 | 7 |
| 6 | Radiology: Barium Enema in UC | 38 | MED-C6-17–MED-C6-23 | 7 |
| 6 | Crohn's Disease: Clinical Features | 38 | MED-C6-24–MED-C6-32 | 9 |
| 6 | Endoscopy & Cross Sectional Imaging in Crohn's | 39 | MED-C6-33–MED-C6-41 | 9 |
| 6 | Intestinal Tuberculosis versus Crohn's Disease | 40 | MED-C6-42–MED-C6-46 | 5 |
| 6 | Extraintestinal Manifestations of IBD | 40 | MED-C6-47–MED-C6-54 | 8 |
| 6 | Others, Other Investigations & Serology | 41 | MED-C6-55–MED-C6-70 | 16 |
| 6 | Truelove And Witt's Classification | 42 | MED-C6-71–MED-C6-79 | 9 |
| 6 | Medical Management of Ulcerative Colitis | 42 | MED-C6-80–MED-C6-88 | 9 |
| 6 | Sulfasalazine & Surgery in Ulcerative Colitis | 43 | MED-C6-89–MED-C6-96 | 8 |
| 6 | Crohn's Disease: Grading & Medical Management | 43 | MED-C6-97–MED-C6-103 | 7 |
| 6 | Crohn's Disease: Management by Severity | 44 | MED-C6-104–MED-C6-116 | 13 |
| 6 | Malignancy in IBD | 45 | MED-C6-117–MED-C6-128 | 12 |


## Full roadmap

| Ch | Title | Starts | State |
|---:|---|---:|---|
| 1 | Diarrhea | 1 | **Live** |
| 2 | Physiology of GIT Absorption and Selective Malabsorption | 6 | **Live** |
| 3 | Clinical Features And Tests For Malabsorption | 14 | **Live** |
| 4 | Global Malabsorption | 18 | **Live** |
| 5 | Inflammatory Bowel Disease : Part 1 | 30 | **Live** |
| 6 | Inflammatory Bowel Disease : Part 2 | 37 | **Live** |
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

1. Render source PDF pages (the scan has no text layer) and read them line-to-line; crop and re-read at higher zoom wherever a digit, threshold or table cell is ambiguous.
2. Inventory every line, table cell, diagram label, flowchart arm, value and note in strict book order into `audit/coverage.json`.
3. Generate `data/chNN.json` with strict `MED-C<N>-<seq>` ordering, `page` nondecreasing, `exp` citing `(Book pX)`, units slicing by `sec`, guides 2–4 lines.
4. Run `validate_content.py`, `tests`, and `build_content.py` to embed; verify live flags and embedded arrays.
5. Commit, push, PR to `main` — live link updates via GitHub Pages.

*Next up:* **Chapter 7 — Infectious Diarrhoea (p46)** — render `uploads/01.pdf` PDF58 onward, inventory p46–51, same pipeline.
