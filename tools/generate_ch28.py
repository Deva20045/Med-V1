#!/usr/bin/env python3
"""Generate Chapter 28: Plasma Cell Disorders (Book p159–168).

Every question is anchored to a specific line, table cell, flowchart branch,
smear/radiology/clinical photograph caption, or Note box in uploads/02.pdf
(PDF pages 42–51 = Book pages 159–168) in strict book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 28
TITLE = "Plasma Cell Disorders"
PAGES = "159-168"

S1 = "Normal Plasma Cell Morphology, Russell/Dutcher Bodies & Polyclonal vs Monoclonal Hypergammaglobulinemia"
S2 = "Plasma Cell Disorder Classification, Myeloma Overview, Smear Variants (Mott/Flame), MGUS vs SMM vs MM & Slim-CRAB"
S3 = "Myeloma Investigations (SPEP/UPEP, IFE, sFLC, ISS β2-M/Albumin, FISH, Whole-Body Low-Dose CT) & Therapeutics"
S4 = "Bony & Renal Pathogenesis (DKK-1/RANK-L, Myeloma Kidney, Type II RTA, Amyloidosis) & Hypercalcemia / Infection Mechanisms"
S5 = "Neuromyeloma Diagram, POEM Syndrome, Solitary Plasmacytoma, Poor Prognostic Factors & Waldenström Intro"
S6 = "Waldenström's Macroglobulinemia: Chr 6q / MYD88 L265P Pathogenesis, Hyperviscosity, Cryoglobulins & Bing-Neel Syndrome"
S7 = "POEMS Syndrome, Heavy Chain Diseases Table (Franklin's, Seligmann's, Mu) & Amyloidosis Definition/Types"
S8 = "Primary AL vs Secondary AA vs Dialysis (Aβ2M) vs Familial/Senile ATTR Amyloidosis & Organ Overview"
S9 = "Amyloidosis Organ Manifestations I: Renal, Cardiac (Restrictive CMP, Sparkle Sign, Digoxin) & Hepatic Bleeding Risk"
S10 = "Amyloidosis Organ Manifestations II: Spleen/GI/ANS/CNS/Endocrine/Hemorrhagic Signs, Congo Red Biopsy & Rx"

RAW: list[tuple] = []


def add(sec: str, page: int, fmt: str, stem: str, correct: str, distractors: list[str], explanation: str) -> None:
    options_check = [correct, *distractors]
    if len(options_check) != 4 or len(set(options_check)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    idx = len(RAW)
    block_rng = random.Random(23000 + CHAPTER * 10000 + (idx // 4))
    block = [0, 1, 2, 3]
    block_rng.shuffle(block)
    target_ans = block[idx % 4]
    rng = random.Random(23000 + CHAPTER * 10000 + idx)
    shuffled_distractors = list(distractors)
    rng.shuffle(shuffled_distractors)
    options = list(shuffled_distractors)
    options.insert(target_ans, correct)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2, f"truefalse True count: {stem}"
        assert sum(o.startswith("False") for o in options) == 2, f"truefalse False count: {stem}"
    if fmt == "fillup":
        assert "______" in stem, f"fillup stem must contain ______: {stem}"
    if fmt == "match":
        assert " — 1)" in stem and " … A)" in stem, f"match stem must use ' — 1) ... … A) ...' grammar: {stem}"
    clean_exp = explanation.rstrip()
    if clean_exp.endswith(f"(Book p{page})"):
        final_exp = clean_exp
    else:
        final_exp = f"{clean_exp} (Book p{page})"
    RAW.append((sec, page, fmt, stem, options, options.index(correct), final_exp))


# ==============================================================================
# UNIT 1 — Page 159: Normal Plasma Cell, Russell/Dutcher Bodies & Poly vs Monoclonal
# ==============================================================================

add(
    S1,
    159,
    "recall",
    "At the top of page 159 under 'Normal Plasma Cell :', what cell of origin and two classical morphological features are listed and illustrated?",
    "Origin: B cells; Morphology: Eccentric cartwheel-shaped nucleus and perinuclear halo due to Golgi complex",
    [
        "Origin: Thymic T cells; Morphology: Bilobed mirror-image nucleus with prominent eosinophilic nucleoli",
        "Origin: Myeloid blasts; Morphology: High nuclear-cytoplasmic ratio with cytoplasmic MPO+ Auer rods",
        "Origin: Splenic red-pulp macrophages; Morphology: Circumferential hairy projections with folded reniform nucleus",
    ],
    "At the top of page 159 under 'Normal Plasma Cell :': '• Origin : B cells. • Morphology : – Eccentric cartwheel shaped nucleus. – Perinuclear halo due to Golgi complex.'",
)

add(
    S1,
    159,
    "fillup",
    "Under 'Normal Plasma Cell → Function :' on page 159, plasma cells produce antibodies composed of 2 heavy chains + 2 light chains, where the heavy chains are IgG, IgA, IgM, ______, or IgE and light chains are kappa (κ) or lambda (λ).",
    "IgD",
    [
        "IgY",
        "IgW",
        "Secretory piece J-chain",
    ],
    "Under 'Function :' on page 159: 'Produce antibodies → Made of 2 heavy chains + 2 light chains. Heavy chains : IgG, IgA, IgM, IgD, IgE. Light chains : κ, λ.'",
)

add(
    S1,
    159,
    "numeric",
    "Under 'Function :' on page 159, what is the normal ratio of kappa to lambda light chains ('κ : λ')?",
    "2 : 1",
    [
        "1 : 2",
        "10 : 1",
        "100 : 1",
    ],
    "Under 'Function :' on page 159, the third sub-bullet states: '– Normal ratio of κ : λ = 2 : 1.'",
)

add(
    S1,
    159,
    "recall",
    "In the two photomicrographs across the middle of page 159, how are 'Russell body' and 'Dutcher body' distinguished by location?",
    "Russell body = Cytoplasmic immunoglobulins; Dutcher body = Intranuclear inclusions of immunoglobulins",
    [
        "Russell body = Intranuclear inclusions of immunoglobulins; Dutcher body = Cytoplasmic immunoglobulins",
        "Russell body = Precipitated ribosomal RNA in red cells; Dutcher body = Denatured beta-globin tetramers",
        "Russell body = Fused primary azurophilic granules; Dutcher body = Phagocytosed nuclear debris in macrophages",
    ],
    "The left photomicrograph on page 159 is captioned 'Russell body → Cytoplasmic immunoglobulins' and the right photomicrograph is captioned 'Dutcher body → Intranuclear inclusions of immunoglobulins.'",
)

add(
    S1,
    159,
    "recall",
    "In the comparison table at the bottom of page 159, how do 'Polyclonal Hypergammaglobulinemia' and 'Monoclonal Hypergammaglobulinemia' differ in clonal antibody pattern and κ : λ ratio?",
    "Polyclonal: Different type of Ab with Normal κ : λ ratio; Monoclonal: Single clone of Ab with Abnormal κ : λ ratio",
    [
        "Polyclonal: Single clone of Ab with Abnormal κ : λ ratio; Monoclonal: Different type of Ab with Normal κ : λ ratio",
        "Both Polyclonal and Monoclonal hypergammaglobulinemia preserve a strictly normal 2 : 1 κ : λ ratio",
        "Polyclonal produces exclusively free light chains without heavy chains; Monoclonal produces all 5 Ig classes equally",
    ],
    "Rows 1 & 4 of the table at the bottom of page 159 compare Polyclonal ('• Different type of Ab', '• Normal κ : λ ratio') vs Monoclonal ('• Single clone of Ab', '• Abnormal κ : λ ratio').",
)

add(
    S1,
    159,
    "recall",
    "In row 2 of the Polyclonal vs Monoclonal Hypergammaglobulinemia table on page 159, how does 'Immunophenotyping' distinguish normal polyclonal plasma cells from monoclonal neoplastic plasma cells?",
    "Polyclonal: CD₁₉, CD₃₈, CD₁₃₈; Monoclonal: CD19–, CD38+, CD138+, CD45–",
    [
        "Polyclonal: CD19–, CD38–, CD138–, CD45+; Monoclonal: CD19+, CD20+, CD5+, CD23+",
        "Polyclonal: CD15+, CD30+; Monoclonal: CD34+, TdT+, MPO+",
        "Polyclonal: CD103+, Annexin A1+; Monoclonal: CD19+, CD45+, CD38–",
    ],
    "Row 2 of the table on page 159 lists Immunophenotyping: Polyclonal = 'CD₁₉, CD₃₈, CD₁₃₈' vs Monoclonal = 'CD19–, CD38+, CD138+, CD45–.'",
)

add(
    S1,
    159,
    "oddoneout",
    "In row 3 ('Seen in :') of the Polyclonal vs Monoclonal table on page 159, all of the following conditions cause Polyclonal Hypergammaglobulinemia EXCEPT:",
    "Multiple myeloma",
    [
        "HIV infection and TB",
        "Autoimmune diseases",
        "CLD (chronic liver disease) and Malaria",
    ],
    "Under Polyclonal Hypergammaglobulinemia → 'Seen in :' on page 159: '– HIV infection – Autoimmune diseases – TB – CLD – Malaria', whereas under Monoclonal Hypergammaglobulinemia → 'Seen in :': '– Multiple myeloma – Waldenstrom macroglobulinemia.'",
)

add(
    S1,
    159,
    "recall",
    "Which two neoplasms are listed as the classic examples under 'Monoclonal Hypergammaglobulinemia → Seen in :' at the bottom of page 159?",
    "Multiple myeloma and Waldenstrom macroglobulinemia",
    [
        "Tuberculosis and Chronic liver disease",
        "Malaria and Systemic lupus erythematosus",
        "Nodular lymphocyte-predominant Hodgkin disease and Infectious mononucleosis",
    ],
    "In the right column at the bottom of page 159 under Monoclonal Hypergammaglobulinemia: '• Seen in : – Multiple myeloma – Waldenstrom macroglobulinemia.'",
)


# ==============================================================================
# UNIT 2 — Page 160: Classification, Myeloma Intro, Smears, MGUS/SMM/MM & Slim-CRAB
# ==============================================================================

add(
    S2,
    160,
    "recall",
    "At the top of page 160 under 'Classification :', how are Plasma Cell Disorders divided between '↑ Proliferation of plasma cell' and 'Only ↑ antibody production'?",
    "↑ Proliferation of plasma cell: MGUS, Smoldering myeloma, Multiple myeloma, Solitary plasmacytoma, Plasma cell leukemia; Only ↑ antibody production: Waldenstrom macroglobulinemia, Heavy chain disease, Primary amyloidosis",
    [
        "↑ Proliferation of plasma cell: Waldenstrom macroglobulinemia and AA amyloidosis only; Only ↑ antibody production: Multiple myeloma and Plasma cell leukemia",
        "↑ Proliferation of plasma cell: HIV and Malaria; Only ↑ antibody production: Burkitt's lymphoma and Follicular lymphoma",
        "All eight entities show ≥60% bone marrow plasma cell proliferation without isolated paraprotein syndromes",
    ],
    "At the top of page 160 under 'Classification :': '1. ↑ Proliferation of plasma cell : MGUS, Smoldering myeloma, Multiple myeloma, Solitary plasmacytoma, Plasma cell leukemia. 2. Only ↑ antibody production : Waldenstrom macroglobulinemia, Heavy chain disease, Primary amyloidosis.'",
)

add(
    S2,
    160,
    "numeric",
    "Under 'Multiple Myeloma' on page 160, what epidemiologic rank, age/race/sex profile, descending heavy-chain frequency order, and light-chain-only percentage are printed?",
    "2nd m/c hematological malignancy; elderly (>70 years), Blacks, M > F; IgG (55%) > IgA > IgM > IgD > IgE; Only light chain: 20%",
    [
        "Rarest hematological malignancy; children (<10 years), Asians, F > M; IgM (80%) > IgE > IgD > IgA > IgG; Only light chain: 2%",
        "1st m/c solid malignancy; young women (20–30 years); IgE (55%) > IgD > IgM > IgA > IgG; Only light chain: 75%",
        "Median age 13 years; M = F; IgA (70%) > IgM > IgG; Only light chain: 0%",
    ],
    "Under 'Multiple Myeloma' on page 160: '• 2nd m/c hematological malignancy. • Elderly (>70 years), Blacks, M > F. • IgG (55%) > IgA > IgM > IgD > IgE • Only light chain : 20%.'",
)

add(
    S2,
    160,
    "recall",
    "Which environmental exposure is specifically highlighted under 'Etiology :' of Multiple Myeloma on page 160?",
    "Exposure to pesticides",
    [
        "Non-atrophic Helicobacter pylori pan-gastritis",
        "Childhood Epstein-Barr virus infection",
        "Silicone breast implant capsule inflammation",
    ],
    "Under 'Multiple Myeloma' on page 160: '• Etiology : Exposure to pesticides.'",
)

add(
    S2,
    160,
    "match",
    "Match each of the three peripheral/marrow smear findings illustrated on page 160 with its morphological description — 1) Rouleaux formation 2) Mott cell 3) Flame cell … A) Eosinophilic pink/magenta-rimmed cytoplasm in IgA myeloma B) Multiple grape-like cytoplasmic immunoglobulin vacuoles C) Stacked coin-like aggregation of red blood cells",
    "1-C, 2-B, 3-A",
    [
        "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B",
        "1-A, 2-B, 3-C",
    ],
    "Across the middle of page 160, the three labelled photomicrographs depict 'Rouleaux formation' (stacked RBCs), 'Mott cell' (grape-like intracytoplasmic immunoglobulin droplets), and 'Flame cell' (eosinophilic Ig-rich cytoplasmic rim).",
)

add(
    S2,
    160,
    "numeric",
    "In the comparison table across the middle of page 160, how do 'MGUS', 'Smoldering Myeloma', and 'Multiple Myeloma' differ across M-protein level, bone marrow plasma cell percentage, CRAB features, and annual risk of progression?",
    "MGUS: M protein < 3 g/dl, BM plasma cells < 10%, No CRAB, 1% risk of progression/year; Smoldering Myeloma: M protein > 3 g/dl, BM plasma cells 10%–60%, No CRAB, 10% risk/year; Multiple Myeloma: M protein > 3 g/dl, BM plasma cells > 10% + MDE OR > 60% without MDE",
    [
        "MGUS: M protein > 3 g/dl, BM plasma cells 10%–60%, CRAB present, 10% risk/year; Smoldering Myeloma: M protein < 3 g/dl, BM plasma cells < 10%, 1% risk/year",
        "MGUS: BM plasma cells > 60%; Smoldering Myeloma: CRAB features mandatory; Multiple Myeloma: M protein < 1 g/dl without MDE",
        "All three require CRAB end-organ damage at baseline and carry an identical 25% annual progression risk",
    ],
    "The three-column table on page 160 contrasts MGUS ('M protein < 3 g/dl', 'Plasma cells in BM < 10%', 'No CRAB features', '1% risk of progression per year'), Smoldering Myeloma ('M protein > 3 g/dl', 'Plasma cells in BM : 10%–60%', 'No CRAB features', '10% risk of progression per year'), and Multiple Myeloma ('M protein > 3 g/dl', 'Plasma cells in BM : > 10% + MDE OR > 60% without MDE').",
)

add(
    S2,
    160,
    "numeric",
    "In the boxed 'Myeloma Defining Events (MDE) (Slim-CRAB)' criteria at the bottom of page 160, what exact cutoffs define the FOUR 'CRAB' features?",
    "C — S. Ca²⁺ >11 mg/dl; R — S. creatinine >2 mg/dl or GFR <40 ml/min; A — Anemia (Hb <10 g/dl); B — ≥1 osteolytic lesion (>5 mm in size on X-ray/CT/PET)",
    [
        "C — S. Ca²⁺ >9.5 mg/dl; R — S. creatinine >1.0 mg/dl; A — Hb <13 g/dl; B — diffuse osteosclerosis only",
        "C — S. Ca²⁺ <8.0 mg/dl; R — nephrotic proteinuria alone with normal GFR; A — Hb <7 g/dl; B — ≥5 fractures",
        "C — S. Ca²⁺ >14 mg/dl; R — anuria requiring dialysis; A — pancytopenia; B — Tc-99m hot spots >10 mm",
    ],
    "Inside the 'Myeloma Defining Events (MDE) (Slim-CRAB)' box on page 160: 'C : S. Ca²⁺ >11 mg/dl; R : S. creatinine >2 mg/dl or GFR <40 ml/min; A : Anemia (Hb <10 g/dl); B : ≥1 osteolytic lesion (>5 mm in size on X-ray/CT/PET).'",
)

add(
    S2,
    160,
    "numeric",
    "In the same 'Myeloma Defining Events (MDE) (Slim-CRAB)' box at the bottom of page 160, what THREE additional biomarker ('SLiM') criteria establish Multiple Myeloma even without end-organ CRAB damage?",
    "Clonal plasma cells ≥60% in BM; >1 focal lesion on MRI (≥5 mm in size); and Involved / Uninvolved serum free light chain ratio ≥100",
    [
        "Clonal plasma cells ≥20% in BM; any 1-mm lesion on chest radiograph; and sFLC ratio ≥10",
        "Clonal plasma cells ≥5% in peripheral blood; hepatosplenomegaly on ultrasound; and κ : λ ratio of 2 : 1",
        "M-protein >1.5 g/dL; elevated ESR >50 mm/hr; and positive urinary dipstick for albumin",
    ],
    "The lower three bullets of the 'Myeloma Defining Events (MDE) (Slim-CRAB)' box on page 160 state: '• Clonal plasma cells ≥60% in BM. • >1 focal lesion on MRI (≥5 mm in size). • Involved / Uninvolved serum free light chain ≥100.'",
)

add(
    S2,
    160,
    "numeric",
    "According to the bottom-most bullet on page 160, how is 'Plasma cell leukemia' defined in peripheral blood (including the immunoglobulin class noted in parentheses)?",
    "≥20% plasma cells in peripheral blood (IgE)",
    [
        "≥5% plasma cells in bone marrow aspirate (IgM)",
        "≥60% lymphoblasts in peripheral blood (IgG)",
        "≥10% smudge cells in peripheral blood (IgA)",
    ],
    "The final line at the bottom of page 160 reads: '• Plasma cell leukemia : ≥20% plasma cells in peripheral blood (IgE).'",
)


# ==============================================================================
# UNIT 3 — Page 161: Investigations, ISS Staging, Low-Dose CT & Treatment
# ==============================================================================

add(
    S3,
    161,
    "recall",
    "At the top of page 161 under 'INVESTIGATIONS → Screening :', what does Serum Protein Electrophoresis (SPEP) detect, how is Urine Protein Electrophoresis (UPEP) performed, and why is UPEP superior in 20% of myeloma cases?",
    "SPEP detects 'M' spike, missing the 20% of MM with only light chain involvement; UPEP uses 24-hour urine for Bence Jones protein (casts of light chains) — NOT detected on dipstick — and is a better screening test",
    [
        "SPEP detects all free light chains with 100% sensitivity; random spot urine dipstick is the gold standard for Bence Jones protein",
        "SPEP shows a broad polyclonal beta-gamma bridge in all MM cases; UPEP requires 1st-void morning midstream urine only",
        "SPEP measures serum β2-microglobulin only; UPEP detects Tamm-Horsfall mucoprotein without free light chains",
    ],
    "Under 'Screening :' on page 161: '1. Serum protein electrophoresis (SPEP) → Detects \"M\" spike. NOTE: In 20% cases of MM there is only light chain involvement (Missed in SPEP). 2. Urine protein electrophoresis (UPEP) → 24 hour urine → Bence Jones protein (Casts of light chains) : Better screening test. Not detected on dipstick.'",
)

add(
    S3,
    161,
    "recall",
    "Under 'INVESTIGATIONS' items 3 and 4 on page 161, what is the role of Serum immunofixation electrophoresis (IFE) and how is the Serum Free Light Chain (sFLC) assay used?",
    "Serum IFE tells the exact heavy and light chain; sFLC assay is diagnostic if ratio is ≥100 and is also used for monitoring disease activity",
    [
        "Serum IFE replaces bone marrow aspirate for counting blasts; sFLC is diagnostic only when ratio <0.5",
        "Serum IFE detects osteolytic lesions directly; sFLC is used only once at autopsy and cannot monitor disease",
        "Serum IFE detects amyloid fibrils in fat pad; sFLC measures only intact IgM pentamers",
    ],
    "Items 3 & 4 on page 161 read: '3. Serum immunofixation electrophoresis → Tells the exact heavy and light chain. 4. Serum free light chain assay : Diagnostic if ratio is ≥100. Also used for monitoring disease activity.'",
)

add(
    S3,
    161,
    "numeric",
    "Under '6. Staging : International Staging System (ISS)' on page 161, which single parameter is the single most powerful predictor of survival, and what exact cutoffs define ISS Stage I, Stage II, and Stage III?",
    "Serum β₂-microglobulin (single most powerful predictor of survival): Stage I = S. β₂M <3.5 AND S. Albumin ≥3.5; Stage II = Neither I nor III; Stage III = S. β₂M >5.5",
    [
        "Serum M-protein spike: Stage I = <1.0 g/dL; Stage II = 1.0–3.0 g/dL; Stage III = >3.0 g/dL",
        "Bone marrow plasma cell percentage: Stage I = <10%; Stage II = 10%–60%; Stage III = >60%",
        "Serum calcium & creatinine: Stage I = normal Ca²⁺; Stage II = Hb <10 g/dL; Stage III = ≥4 lytic bone lesions",
    ],
    "Under '6. Staging : International Staging System (ISS)' on page 161: '• S. β₂-microglobulin (Single most powerful predictor of survival). • S. Albumin. Stage I : S. β₂M <3.5 and S. Albumin ≥3.5; Stage II : Neither I nor III; Stage III : S. β₂M >5.5.'",
)

add(
    S3,
    161,
    "recall",
    "Under '7. Cytogenetics and FISH :' on page 161, which four high-risk genetic abnormalities are explicitly listed?",
    "t(4;14), t(14;16), del(17p), and chr 1q amp",
    [
        "t(11;14), trisomy 12, del(13q14), and hyperdiploidy",
        "t(8;14), t(14;18), t(15;17), and inv(16)",
        "t(9;22), BRAF V600E, MYD88 L265P, and JAK2 V617F",
    ],
    "Item 7 on page 161 reads: '7. Cytogenetics and FISH : • t(4;14) • t(14;16) • del(17p) • chr 1q amp.'",
)

add(
    S3,
    161,
    "recall",
    "Under '8. Imaging :' on page 161, what is the investigation of choice (IOC), what is preferred in neurological emergencies or plasmacytomas, and why does Tc-99m bone scan show NO hot spots in multiple myeloma?",
    "IOC: Low-dose whole-body CT; MRI preferred in neurological emergencies & plasmacytomas; PET-CT useful to follow treatment response; Tc-99m bone scan has NO hot spots because osteoblastic activity is NOT present",
    [
        "IOC: Tc-99m MDP skeletal scintigraphy showing intense hot spots throughout the skull; low-dose CT is contraindicated",
        "IOC: Plain abdominal ultrasound; MRI is contraindicated in cord compression; Tc-99m scan shows diffuse superscan",
        "IOC: Dual-energy X-ray absorptiometry (DEXA) only; osteoblastic new bone formation masks lytic lesions on CT",
    ],
    "Under '8. Imaging :' on page 161: '• Low dose whole body CT (IOC). • MRI : Preferred in neurological emergencies, plasmacytomas. • PET-CT : Useful to follow up response to Rx. • Bone scan : Tc-99m scan has NO hot spots (Osteoblastic activity NOT present).'",
)

add(
    S3,
    161,
    "management",
    "Under 'TREATMENT' on page 161, which plasma cell conditions require NO treatment, what is the first step in Multiple Myeloma evaluation, and what induction triplet + definitive therapy are given to stem-cell-transplant-eligible patients?",
    "No treatment for MGUS and Smoldering MM (monitor M protein); 1st step in MM = check eligibility for stem cell transplantation; Eligible → Triplet therapy [Lenalidomide + Bortezomib + Dexamethasone] → Autologous stem cell transplant",
    [
        "Immediate myeloablative allogeneic BMT for MGUS and Smoldering MM; standard R-CHOP × 6 cycles for transplant-eligible MM",
        "Single-agent oral chlorambucil for all young fit patients, reserving triplet VRD strictly for MGUS",
        "Immediate plasmapheresis monotherapy without bortezomib, lenalidomide, or autologous stem cell transplant",
    ],
    "Under 'TREATMENT' on page 161: 'No treatment required for : • MGUS • Smoldering MM (Monitor M protein). Multiple myeloma : Check eligibility for stem cell transplantation (1st step) → Yes : Triplet therapy [Lenalidomide + Bortezomib + Dexamethasone] → Autologous stem cell transplant.'",
)

add(
    S3,
    161,
    "match",
    "Match each anti-myeloma drug class or agent listed at the bottom of page 161 with its specific prototype or surface target — 1) Proteasome inhibitor 2) Immunomodulators (IMiDs) 3) Daratumumab / Isatuximab 4) Elotuzumab … A) Anti-CD 38 B) SLAM F7 C) Bortezomib / Carfilzomib D) Thalidomide / Lenalidomide / Pomalidomide",
    "1-C, 2-D, 3-A, 4-B",
    [
        "1-D, 2-C, 3-B, 4-A",
        "1-C, 2-A, 3-D, 4-B",
        "1-B, 2-D, 3-A, 4-C",
    ],
    "Under 'Drugs used :' at the bottom of page 161: Proteasome inhibitor = Bortezomib, Carfilzomib; Immunomodulators (IMiDs) = Thalidomide, Lenalidomide, Pomalidomide; Targeted drugs = Anti-CD 38 (Daratumumab, Isatuximab), Anti-CD 20 (Rituximab), SLAM F7 (Elotuzumab).",
)

add(
    S3,
    161,
    "fillup",
    "In the 'Supportive care :' box at the bottom-right of page 161, hydration and analgesia are paired with ______ for bone protection.",
    "Bisphosphonates",
    [
        "Recombinant PTH (teriparatide)",
        "High-dose calcitriol",
        "Thiazide diuretics",
    ],
    "The 'Supportive care :' box at the bottom-right of page 161 lists: '• Hydration • Analgesia • Bisphosphonates.'",
)


# ==============================================================================
# UNIT 4 — Page 162: Bony & Renal Pathogenesis, Hypercalcemia & Recurrent Infections
# ==============================================================================

add(
    S4,
    162,
    "fillup",
    "At the very top of page 162, the boxed 'Note :' states: 'm/c hematological malignancy : ______.'",
    "Leukemia",
    [
        "Hodgkin's disease",
        "Waldenström macroglobulinemia",
        "Heavy chain disease",
    ],
    "The boxed 'Note :' at the top of page 162 states verbatim: 'Note : m/c hematological malignancy : Leukemia' [documented alongside p160 in known-source-caveats.md].",
)

add(
    S4,
    162,
    "recall",
    "Under 'CLINICAL FEATURES → 1. Bony lesions :' on page 162, what is the most common symptom of Multiple Myeloma, which bones are involved in descending frequency, and what are the two signaling arms of bone destruction?",
    "Bone pain is the m/c symptom; Vertebra > Rib > Skull ('raindrop' punched-out lytic lesions) > Pelvis > Femur > Clavicle > Scapula; Tumor cells secrete Dickkopf-1 (inhibits osteoblasts → ↓ ALP, negative bone scan) AND IL-6/IL-1β/TNF-α → ↑ RANK-L → stimulates osteoclasts → hypercalcemia & lytic lesions",
    [
        "Painless splenomegaly is the m/c symptom; Distal phalanges > Tarsals; Tumor cells stimulate osteoblasts → markedly ↑↑ ALP and diffuse Tc-99m hot spots",
        "Morning joint stiffness is the m/c symptom; Sacroiliac joints exclusively; Osteoclast inhibition causes osteopetrosis and hypocalcemia",
        "Jaw swelling is the m/c symptom; Maxilla > Mandible only; PTHrP secretion stimulates osteoid synthesis with normal osteoclast activity",
    ],
    "Under '1. Bony lesions :' on page 162: '• Bone pain : m/c symptom. • Involvement : Vertebra > Rib > Skull > Pelvis > Femur > Clavicle > Scapula. • \"Raindrop\" skull : Punched out lytic lesions.' Flowchart: 'Tumor cells → Dickkopf-1 → Inhibits osteoblasts → No healing → ↓ ALP, Negative bone scan' AND 'Tumor cells → IL-6, IL-1β, TNF-α → ↑ RANK-L → Stimulate osteoclast → Bone resorption → Hypercalcemia, Lytic lesions.'",
)

add(
    S4,
    162,
    "recall",
    "Under '2. Renal failures :' on page 162, what is the MOST COMMON cause of renal failure in Multiple Myeloma and what is the MOST COMMON cause of tubular damage (Myeloma kidney)?",
    "Most common cause of renal failure: Hypercalcemia (causes vasoconstriction); Most common cause of tubular damage (Myeloma kidney): Cast nephropathy — light chain casts combine with Tamm-Horsfall protein to block tubules",
    [
        "Most common cause of renal failure: Bilateral ureteric uric-acid stones; Most common cause of tubular damage: Immune-complex crescentic glomerulitis",
        "Most common cause of renal failure: Renal vein thrombosis; Most common cause of tubular damage: Papillary necrosis from sickle cells",
        "Most common cause of renal failure: AA amyloidosis; Most common cause of tubular damage: Distal Type I RTA",
    ],
    "Under '2. Renal failures :' on page 162: '• Hypercalcemia : m/c cause of renal failure (Causes vasoconstriction).' And under '• Myeloma kidney : Cast nephropathy (m/c cause of tubular damage) → Light chain casts combine with Tamm Horsfall protein → Blocks the tubule.'",
)

add(
    S4,
    162,
    "recall",
    "Under '2. Renal failures :' on page 162, which type of Renal Tubular Acidosis (RTA) occurs from direct toxic effects of light chains on proximal tubules, and what are its four listed features?",
    "Type II RTA — Fanconi syndrome: glycosuria, aminoaciduria, phosphaturia, and hypouricemia",
    [
        "Type I distal RTA — nephrocalcinosis, alkaline urine pH >6.5, hyperuricemia, and absence of glycosuria",
        "Type IV hyperkalemic RTA — hypoaldosteronism, severe hyperkalemia, absence of phosphaturia, and polycythemia",
        "Bartter syndrome — metabolic alkalosis, hypercalciuria, hyperreninemia, and conserved proximal glucose transport",
    ],
    "Bullet 3 under '2. Renal failures :' on page 162 reads: '• Type II RTA : Direct toxic effects of light chain — Fanconi syndrome: glycosuria, aminoaciduria, phosphaturia, hypouricemia.'",
)

add(
    S4,
    162,
    "recall",
    "Which glomerular lesion on page 162 presents specifically with 'Nephrotic syndrome + Normal sized kidneys' in Multiple Myeloma (alongside monoclonal light-chain deposition disease)?",
    "Amyloidosis (AL type)",
    [
        "Minimal change disease with selective albuminuria",
        "Autosomal dominant polycystic kidney disease",
        "Post-streptococcal diffuse proliferative glomerulonephritis",
    ],
    "Bullets 4–5 under '2. Renal failures :' on page 162 list: '• Amyloidosis (AL type) : Nephrotic syndrome + Normal sized kidneys. • Monoclonal light chain deposition disease.'",
)

add(
    S4,
    162,
    "recall",
    "Under '3. Hypercalcemia :' at the bottom of page 162, how does hypercalcemia lead to dehydration, acute renal failure, and coma?",
    "Hypercalcemia → Polyuria, Polydipsia (Nephrogenic DI) → Dehydration → Acute renal failure, and also causes Coma (Neurological emergencies)",
    [
        "Hypercalcemia → SIADH with water retention and dilutional hyponatremia → Cerebral edema without renal injury",
        "Hypercalcemia → Osmotic glycosuria from pancreatic beta-cell destruction → Diabetic ketoacidosis",
        "Hypercalcemia → Efferent arteriolar vasodilation → Glomerular hyperfiltration and polycythemia",
    ],
    "Under '3. Hypercalcemia :' on page 162: 'Hypercalcemia → Polyuria, Polydipsia (Nephrogenic DI) → Dehydration → Acute renal failure; → Coma (Neurological emergencies).'",
)

add(
    S4,
    162,
    "recall",
    "Under '4. Recurrent infections :' at the bottom of page 162, what is the MOST COMMON cause of death in Multiple Myeloma, which two organ systems are most commonly infected (with top organism), and why?",
    "Infections are the m/c cause of death — Respiratory tract (m/c: S. pneumoniae) and Urinary tract — due to hypogammaglobulinemia, abnormal antibodies, CD4 lymphocytopenia, and decreased neutrophil lysozyme",
    [
        "Hemorrhagic stroke is the m/c cause of death — CNS toxoplasmosis only — due to isolated IgE excess",
        "Hepatic failure is the m/c cause of death — hepatosplenic candidiasis — due to severe agranulocytosis alone",
        "Pulmonary embolism is the m/c cause of death — skin staphylococcal abscesses — due to hypercomplementemia",
    ],
    "At the bottom of page 162 under '4. Recurrent infections : (m/c cause of death)': '• Respiratory tract (m/c : S. pneumoniae). • Urinary tract. D/t : Hypogammaglobulinemia, Abnormal antibodies, CD4 lymphocytopenia, Decreased neutrophil lysozyme.'",
)


# ==============================================================================
# UNIT 5 — Page 163: Neuromyeloma, POEM, Solitary Plasmacytoma, Prognosis & WM Intro
# ==============================================================================

add(
    S5,
    163,
    "recall",
    "At the top of page 163 in the '5. Neuromyeloma :' diagram, which FOUR mechanisms explain neurological manifestations in Multiple Myeloma?",
    "Hypercalcemia (causes coma), Hyperviscosity ('d/t ↑ plasma cells' as printed), Cord compression, and Amyloidosis / Light chain neuropathy (causes sensory neuropathy, especially IgM & IgG)",
    [
        "Direct meningeal blast infiltration, PML from JC virus, subacute combined degeneration, and Wernicke encephalopathy",
        "Paraneoplastic anti-Yo cerebellar degeneration, myasthenia gravis, optic neuritis, and cavernous sinus thrombosis",
        "Intracranial berry aneurysm rupture, sagittal sinus thrombosis from JAK2 mutation, and Guillain-Barré syndrome",
    ],
    "At the top of page 163, 'Neuromyeloma' branches into four boxes: 'Hypercalcemia (Causes coma)', 'Hyperviscosity (D/t ↑ plasma cells)', 'Cord compression', and 'Amyloidosis / Light chain neuropathy (Causes sensory neuropathy, especially IgM & IgG)'.",
)

add(
    S5,
    163,
    "recall",
    "Right below the Neuromyeloma diagram on page 163, what is 'POEM syndrome' (paraneoplastic manifestation) and what characteristic radiographic lesion accompanies it?",
    "Polyneuropathy, Organomegaly, Endocrinopathy, and M-protein, with Osteosclerotic bone lesions",
    [
        "Pancytopenia, Osteopenia, Erythromelalgia, and Macrocytosis, with Raindrop osteolytic skull lesions",
        "Purpura, Ophthalmoplegia, Eosinophilia, and Myocarditis, with Bamboo spine syndesmophytes",
        "Pruritus, Orthopnea, Effusion, and Mediastinal mass, with Codman triangle periosteal reaction",
    ],
    "On page 163: '• POEM syndrome : Paraneoplastic manifestation → Polyneuropathy, Organomegaly, Endocrinopathy, M-protein. Osteosclerotic bone lesions.'",
)

add(
    S5,
    163,
    "management",
    "Under 'SOLITARY PLASMACYTOMA' on page 163, what bone marrow and CRAB criteria define it, what are its two clinical types (and most common extramedullary site), and what is the treatment?",
    "No CRAB features and BM <10% plasma cells; Types: Solitary bone plasmacytoma and Extramedullary (m/c in nasal pharynx); Treatment: Responds to radiation (curative)",
    [
        "Mandatory CRAB features and BM >60% plasma cells; Extramedullary m/c in spleen; Treatment: Urgent allogeneic BMT",
        "Serum M-protein >5 g/dL and renal failure; Extramedullary m/c in kidney; Treatment: CODOX-M/IVAC chemotherapy",
        "Peripheral blood ≥20% plasma cells; Extramedullary m/c in skin; Treatment: Watch-and-wait observation only",
    ],
    "Under 'SOLITARY PLASMACYTOMA' on page 163: '• No CRAB features. • BM <10% plasma cells. • Types : – Solitary bone plasmacytoma – Extramedullary (m/c in nasal pharynx). • Treatment : Responds to radiation (Curative).'",
)

add(
    S5,
    163,
    "oddoneout",
    "Under 'POOR PROGNOSTIC FACTORS' of Multiple Myeloma on page 163, all of the following factors are explicitly listed EXCEPT:",
    "Serum Albumin >4.0 g/dL with ISS Stage I",
    [
        "↑ LDH and ISS Stage III",
        "↑ β₂ glycoprotein (as printed on p163) and Circulating plasma cells",
        "Plasma cell hypodiploidy and Deletion of 17p",
    ],
    "Under 'POOR PROGNOSTIC FACTORS' on page 163: '• ↑ LDH. • ↑ β₂ glycoprotein [printed slip on p163 for β₂ microglobulin]. • Circulating plasma cells. • ISS Stage III. • Plasma cell hypodiploidy. • Deletion of 17p.'",
)

add(
    S5,
    163,
    "recall",
    "What captions accompany the clinical neck mass photograph and the lateral skull radiograph on page 163?",
    "Clinical neck photograph: 'Plasmacytosis' (as printed); Lateral skull radiograph: 'Multiple Myeloma → Punched out bone lesions'",
    [
        "Clinical neck photograph: 'Scrofuloderma'; Lateral skull radiograph: 'Hair-on-end crew-cut periosteal reaction'",
        "Clinical neck photograph: 'Cystic hygroma'; Lateral skull radiograph: 'Cotton-wool osteoblastic Paget skull'",
        "Clinical neck photograph: 'Goiter'; Lateral skull radiograph: 'Salt-and-pepper hyperparathyroid skull'",
    ],
    "On page 163, the neck clinical photo is captioned 'Plasmacytosis' [preserved as printed] and the skull X-ray is captioned 'Multiple Myeloma → Punched out bone lesions.'",
)

add(
    S5,
    163,
    "recall",
    "Under 'Waldenstrom's Macroglobulinemia' at the bottom of page 163, what cell type and paraprotein define it, what are its age/sex demographics, and why is it compared directly to 'IgM secreting CLL'?",
    "Lymphoplasmacytic lymphoma secreting IgM (hyperviscosity); Elderly (>60 years), M > F; resembles 'IgM secreting CLL' because it has NO lytic bone lesions, NO renal disease, and NO hypercalcemia, while causing lymphadenopathy and splenomegaly",
    [
        "Pure plasma-blast leukemia secreting IgE; Children (<10 years), F > M; causes extensive raindrop osteolytic lesions, hypercalcemia, and cast nephropathy without splenomegaly",
        "Pre-germinal mantle cell neoplasm secreting IgA; Young adults; causes gastrointestinal lymphomatoid polyposis without lymphadenopathy",
        "Post-germinal marginal zone lymphoma secreting IgD; Females > Males; cured by H. pylori eradication",
    ],
    "At the bottom of page 163 under 'Waldenstrom's Macroglobulinemia': '• Lymphoplasmacytic lymphoma secreting IgM (Hyperviscosity). • Elderly (>60 years), M > F. • IgM secreting CLL : – No lytic bone lesion. – No renal disease. – No hypercalcemia. – Lymphadenopathy & splenomegaly seen.'",
)


# ==============================================================================
# UNIT 6 — Page 164: WM Pathogenesis (6q/MYD88), Hyperviscosity, Bing-Neel & Rx
# ==============================================================================

add(
    S6,
    164,
    "recall",
    "In the 'PATHOGENESIS' flowchart of Waldenstrom's Macroglobulinemia at the top of page 164, what chromosomal deletion and somatic point mutation occur in post-germinal B cells, and what markers appear in the 'Lymphoplasmacytic cells' box?",
    "Deletion of long arm of chr 6 + Somatic mutation in MYD 88 L265P → Lymphoplasmacytic cells (box prints: CD19, CD20, CD38, CD135 [as printed], S.IgM)",
    [
        "Translocation t(11;14) + SOX-11 overexpression → Pre-germinal mantle cells (CD5+, Cyclin D1+, S.IgD)",
        "Translocation t(14;18) + BCL-2 overexpression → Germinal-centre centrocytes (CD10+, BCL-6+, S.IgG)",
        "Deletion of 17p + BRAF V600E mutation → Hairy cells (CD103+, Annexin A1+, S.IgE)",
    ],
    "At the top of page 164 under 'PATHOGENESIS': 'Post germinal B cells + Deletion of long arm of chr 6 + Somatic mutation in MYD 88 L265P → Lymphoplasmacytic cells : CD19, CD20, CD38, CD135 [printed in box vs CD 138– under Criteria below], S.IgM.'",
)

add(
    S6,
    164,
    "recall",
    "Under 'CLINICAL FEATURES' of Waldenstrom's Macroglobulinemia on page 164, what are the most common symptom, hepatosplenomegaly/lymphadenopathy/anemia pattern, retinal vein finding, and cryoglobulinemia features?",
    "Fatigue (m/c symptom), HSM, lymphadenopathy, anemia; hyperviscosity causing diplopia, blurriness, tinnitus, headache, ataxia, dilated & segmented retinal veins, stroke, and congestive cardiac failure; cryoglobulinemia causing Raynaud's phenomenon and cold urticaria",
    [
        "Vertebral crush fracture pain (m/c symptom), shrunken fibrotic spleen, punched-out lytic skull lesions, and nephrogenic diabetes insipidus from hypercalcemia",
        "Alcohol-induced cervical lymph node pain, Pel-Ebstein cyclical fever, vanishing bile duct syndrome, and minimal change nephropathy",
        "Pancytopenia with dry tap marrow fibrosis, opportunistic M. kansasii infection, and absent monocytopenia",
    ],
    "Under 'CLINICAL FEATURES' on page 164: '• Fatigue (m/c symptom). • HSM, lymphadenopathy, anemia. • Hyperviscosity : – Visual & auditory disturbances (Diplopia, blurriness, tinnitus) – Headache, ataxia – Dilated and segmented retinal veins – Stroke – Congestive cardiac failure. • Cryoglobulinemia : Raynaud's phenomenon, Cold urticaria.'",
)

add(
    S6,
    164,
    "fillup",
    "Under peripheral neuropathy of Waldenstrom's Macroglobulinemia on page 164, sensorimotor antibodies target ______ (anti-MAG antibodies).",
    "myelin associated glycoprotein",
    [
        "acetylcholine nicotinic receptors",
        "voltage-gated calcium channels",
        "aquaporin-4 water channels",
    ],
    "Bullet 5 under 'CLINICAL FEATURES' on page 164 reads: '• Peripheral neuropathy : Sensorimotor Ab vs myelin associated glycoprotein.'",
)

add(
    S6,
    164,
    "recall",
    "Under 'DIAGNOSIS' of Waldenstrom's Macroglobulinemia on page 164, what peripheral smear finding, bone marrow infiltrate, MYD88 prevalence, and four 'Criteria' bullets are listed?",
    "Peripheral smear: Rouleaux formation & positive Coombs test; Bone marrow: >10% lymphoplasmacytoid cells + mast cells; MYD88 (L265P) seen in >90% cases; Criteria: IgM protein, Lymphoplasmacytic marrow infiltrates, MYD 88 (+), and CD 20+, CD 19+, CD 138–, CD 5+",
    [
        "Peripheral smear: Smudge cells & negative Coombs test; Bone marrow: >60% CD19–, CD138+ plasma cells without mast cells; MYD88 negative",
        "Peripheral smear: Auer rods in faggot cells; Bone marrow: dry tap reticulin fibrosis; Criteria: IgG kappa + t(15;17)",
        "Peripheral smear: Tear-drop poikilocytes; Bone marrow: Reed-Sternberg lacunar cells; Criteria: CD15+, CD30+, EBV+",
    ],
    "Under 'DIAGNOSIS' on page 164: '• Peripheral smear : Rouleaux formation, Positive Coombs test. • Bone marrow : >10% lymphoplasmacytoid cells. Mast cells also seen. • MYD88 (L265P) seen in >90% cases. • Criteria : 1. IgM protein 2. Lymphoplasmacytic marrow infiltrates 3. MYD 88 (+) 4. CD 20+, CD 19+, CD 138–, CD 5+ [as printed].'",
)

add(
    S6,
    164,
    "management",
    "Under 'TREATMENT' of Waldenstrom's Macroglobulinemia on page 164, how is Hyperviscosity treated urgently, and which systemic agents are listed for severe cases?",
    "Hyperviscosity: Plasmapheresis; Severe cases: Bortezomib, Rituximab, Bendamustine, and Ibrutinib",
    [
        "Hyperviscosity: Packed RBC transfusion; Severe cases: Standard ABVD + Bleomycin",
        "Hyperviscosity: Oral desmopressin; Severe cases: H. pylori triple eradication therapy",
        "Hyperviscosity: Loop diuretics + dehydration; Severe cases: ATRA + Arsenic trioxide",
    ],
    "Under 'TREATMENT' on page 164: '• Hyperviscosity : Plasmapheresis. • Severe cases : Bortezomib, Rituximab, Bendamustine, Ibrutinib.'",
)

add(
    S6,
    164,
    "recall",
    "According to the boxed 'Note : Bing-Neel syndrome' at the bottom of page 164, what is Bing-Neel syndrome and which two features occur?",
    "Neurological complication of WM characterized by leptomeningeal infiltration with tumor cells and hyperviscosity",
    [
        "Renal complication of MM characterized by Tamm-Horsfall cast nephropathy and Fanconi proximal RTA",
        "Cutaneous complication of CTCL characterized by Pautrier microabscesses and generalized erythroderma",
        "Hepatic complication of Hodgkin's disease characterized by cholangitis and vanishing bile duct syndrome",
    ],
    "The boxed 'Note :' at the bottom of page 164 reads: 'Bing-Neel syndrome : Neurological complication of WM. • Leptomeningeal infiltration with tumor cells. • Hyperviscosity.'",
)


# ==============================================================================
# UNIT 7 — Page 165: POEMS Syndrome, Heavy Chain Diseases Table & Amyloidosis Intro
# ==============================================================================

add(
    S7,
    165,
    "recall",
    "At the top of page 165 under 'POEMS Syndrome', what does each letter of the acronym P-O-E-M-S stand for, including the exact clinical findings listed for P, O, E, M, and S?",
    "P — Polyneuropathy (1st presenting symptom: progressive symmetric sensorimotor neuropathy); O — Organomegaly (HSM, lymphadenopathy); E — Endocrinopathy (gynecomastia, impotence, amenorrhea, Type II DM, hypothyroidism); M — Monoclonal plasma cells; S — Skin changes (hyperpigmentation, hypertrichosis, thickening, clubbing)",
    [
        "P — Pancytopenia; O — Osteolysis with raindrop skull; E — Exophthalmos; M — Macroglossia; S — Splenic atrophy",
        "P — Pruritus; O — Orthostatic hypotension; E — Eosinophilia; M — Mastocytosis; S — Sclerodactyly",
        "P — Pericarditis; O — Optic neuritis; E — Encephalopathy; M — Myositis; S — Sicca syndrome",
    ],
    "At the top of page 165, 'POEMS Syndrome' lists every letter's clinical findings, plus '• Osteosclerotic bone lesions' and '• Thrombocytosis & erythrocytosis'.",
)

add(
    S7,
    165,
    "management",
    "Under 'POEMS Syndrome' on page 165, what hematologic count abnormalities accompany its osteosclerotic bone lesions, and what is the treatment?",
    "Thrombocytosis & erythrocytosis accompany osteosclerotic bone lesions; Treatment: Autologous HSCT",
    [
        "Severe pancytopenia & monocytopenia accompany lytic lesions; Treatment: Watch-and-wait observation",
        "Isolated agranulocytosis accompanies normal bone scans; Treatment: Splenectomy",
        "Coagulopathy with factor X deficiency; Treatment: Oral colchicine monotherapy",
    ],
    "Bullets 6–8 under 'POEMS Syndrome' on page 165 state: '• Osteosclerotic bone lesions. • Thrombocytosis & erythrocytosis. • Treatment : Autologous HSCT.'",
)

add(
    S7,
    165,
    "match",
    "In the 'Heavy Chain Disease' table across the middle of page 165, match each disease row with its defining heavy chain, clinical triad/association, or smear finding — 1) Franklin's disease (γ heavy chain) 2) Seligmann's disease (α heavy chain — m/c) 3) Mu heavy chain disease (μ heavy chain) … A) Associated with CLL & vacuolated lymphocytes; κ chains secreted in urine B) Lymphadenopathy + Waldeyer's ring + palatal edema; rapid downhill course, death due to infections C) IPSID, diarrhea/weight loss/malabsorption; responds to antibiotics; may progress to high-grade lymphomas D) Autoimmune hemolytic anemia without paraproteinemia",
    "1-B, 2-C, 3-A",
    [
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-D",
        "1-A, 2-C, 3-B",
    ],
    "Wait — match options must use exact bijective length matching the column count! Let's ensure both columns have 4 items.",
)

# Fix previous item immediately in place? No — pop RAW[-1] cleanly right here and add a 4x4 match!
RAW.pop()

add(
    S7,
    165,
    "match",
    "In the 'Heavy Chain Disease' table across the middle of page 165, match each item with its exact entry — 1) Franklin's disease 2) Seligmann's disease 3) Seligmann's disease — Management 4) Mu heavy chain disease … A) α heavy chain (m/c); IPSID with diarrhea, weight loss, malabsorption B) Associated with CLL; vacuolated lymphocytes; κ chains secreted in urine C) γ heavy chain; lymphadenopathy + Waldeyer's ring + palatal edema; death due to infections D) Responds to antibiotics; may progress to high-grade lymphomas",
    "1-C, 2-A, 3-D, 4-B",
    [
        "1-A, 2-C, 3-D, 4-B",
        "1-C, 2-B, 3-A, 4-D",
        "1-D, 2-A, 3-C, 4-B",
    ],
    "In the 'Heavy Chain Disease' table on page 165: Franklin's disease (γ) = lymphadenopathy + Waldeyer's ring + palatal edema, rapid downhill course, death d/t infections; Seligmann's disease (α — m/c) = Immunoproliferative small intestinal disease (IPSID), diarrhea/weight loss/malabsorption, responds to antibiotics, may progress to high-grade lymphomas; Mu heavy chain disease (μ) = associated with CLL, vacuolated lymphocytes, κ chains secreted in urine.",
)

add(
    S7,
    165,
    "recall",
    "At the bottom of page 165 under 'Amyloidosis', what ultrastructural secondary protein structure defines Amyloidosis, and what four major types are listed?",
    "Extracellular tissue deposition of fibrils composed of low-molecular-weight protein subunits that adopt a Beta-pleated sheet structure; Types: 1. Primary AL amyloidosis, 2. Secondary AA amyloidosis, 3. Dialysis related amyloidosis, 4. Familial (hereditary) amyloidosis",
    [
        "Intracellular nuclear accumulation of alpha-helical collagen triple-helix monomers; Types: 1. Keloid, 2. Hypertrophic scar, 3. Scleroderma, 4. Morphea",
        "Intravascular polymerization of deoxygenated beta-globin chains under hypoxia; Types: HbS, HbC, HbD, HbE",
        "Lysosomal storage of unesterified sphingomyelin and glucocerebroside in macrophages; Types: Gaucher, Niemann-Pick, Tay-Sachs, Fabry",
    ],
    "At the bottom of page 165 under 'Amyloidosis': '• Extracellular tissue deposition of fibrils composed of low molecular weight protein subunits. • Beta-pleated sheet structure. Types : 1. Primary AL amyloidosis 2. Secondary AA amyloidosis 3. Dialysis related amyloidosis 4. Familial (hereditary) amyloidosis.'",
)


# ==============================================================================
# UNIT 8 — Page 166: AL, AA, Dialysis Aβ2M & ATTR Amyloidosis + Organ Overview
# ==============================================================================

add(
    S8,
    166,
    "recall",
    "At the top of page 166 under 'Primary AL Amyloidosis', what alternative name is printed, what rank does it hold among systemic amyloidoses, which light chain is more amyloidogenic ('λ vs κ'), and how does it progress?",
    "'AKA light chain disease' (as printed); most common cause of systemic amyloidosis; associated with MM (20%) & WM; λ light chains are more amyloidogenic than κ; rapidly progressive and fatal without treatment",
    [
        "Rarest localized amyloidosis; associated exclusively with TB; κ light chains are 10× more amyloidogenic than λ; benign self-limiting course",
        "Associated exclusively with chronic hemodialysis; composed of Serum Amyloid A; regresses spontaneously without therapy",
        "Autosomal dominant liver mutant transthyretin disease; seen only in patients >90 years; affects joints exclusively",
    ],
    "At the top of page 166 under 'Primary AL Amyloidosis': 'AKA light chain disease [as printed]. • m/c cause of systemic amyloidosis. • Associated with MM (20%), WM. • λ light chains are more amyloidogenic than κ. • Rapidly progressive and fatal without treatment.'",
)

add(
    S8,
    166,
    "recall",
    "Under 'Secondary Amyloidosis' on page 166, which precursor acute-phase reactant forms AA fibrils, what infectious vs inflammatory conditions cause it (including the ONLY infective cause), and which organ is MOST COMMONLY affected?",
    "Serum Amyloid A (SAA), an acute-phase reactant; Only infective cause = TB; Chronic inflammatory diseases = Rheumatoid arthritis, IBD, Ank. spondylitis, Familial Mediterranean fever (IL-1 mutation); Kidney is the most common organ affected",
    [
        "Transthyretin (prealbumin); Infective causes = HIV & Malaria; Heart is the only organ affected, completely sparing the kidney",
        "Monoclonal lambda light chain; Infective cause = H. pylori; Tongue and periorbital skin are most commonly affected",
        "Beta-2 microglobulin; Inflammatory cause = Osteoarthritis; Carpal tunnel synovium is the only site affected",
    ],
    "Under 'Secondary Amyloidosis' on page 166: '• Composed of Serum Amyloid A (SAA), an acute phase reactant. • Seen in : – Chronic infection : TB (Only infective cause). – Chronic inflammatory diseases : Rheumatoid arthritis, IBD, Ank. spondylitis, Familial Mediterranean fever (IL-1 mutation). • Kidney is the m/c organ affected.'",
)

add(
    S8,
    166,
    "recall",
    "Under 'Dialysis Related Amyloidosis' on page 166, what fibril protein deposits and which two musculoskeletal manifestations are highlighted?",
    "Amyloid deposition of β₂ microglobulin (Aβ₂M), causing Arthropathy and Carpal tunnel syndrome",
    [
        "Amyloid deposition of Serum Amyloid A (SAA), causing hepatosplenomegaly and Type II RTA",
        "Amyloid deposition of mutant Apo A1, causing macroglossia and periorbital purpura",
        "Amyloid deposition of atrial natriuretic peptide, causing isolated left atrial dilation",
    ],
    "Under 'Dialysis Related Amyloidosis' on page 166: '• Seen in ESRD patients on chronic dialysis. • Amyloid deposition of β₂ microglobulin (Aβ₂M). • Arthropathy, carpal tunnel syndrome.'",
)

add(
    S8,
    166,
    "match",
    "In the 'Familial & Senile Systemic Amyloidosis' section on page 166, match each item with its exact precursor protein, genetics, clinical phenotype, or therapy — 1) ATTRm (hereditary ATTR) 2) ATTRwt (wild-type / senile systemic) 3) Apo A1, Apo A2, Gelsolin, Fibrinogen Aα, Lysozyme 4) Tafamidis … A) Unmutated TTR in >70 years old causing restrictive cardiomyopathy B) Autosomal dominant TTR mutation (liver-produced thyroid-hormone transporter) → peripheral neuropathy, cardiomyopathy & CNS C) Stabilizes TTR tetramers and prevents misfolding (Rx for ATTR CMP) D) Rare precursor proteins that can also cause hereditary amyloidosis",
    "1-B, 2-A, 3-D, 4-C",
    [
        "1-A, 2-B, 3-D, 4-C",
        "1-B, 2-C, 3-A, 4-D",
        "1-D, 2-A, 3-B, 4-C",
    ],
    "Under 'Familial & Senile Systemic Amyloidosis' on page 166: ATTRm = AD inheritance of TTR (liver transporter of thyroid hormones) causing peripheral neuropathy, cardiomyopathy & CNS; ATTRwt = wild-type unmutated TTR in >70 yrs old causing restrictive CMP; Rare precursors = Apo A1, Apo A2, Gelsolin, Fibrinogen Aα, Lysozyme; Rx for ATTR CMP = Tafamidis (stabilizes TTR tetramers & prevents misfolding).",
)

add(
    S8,
    166,
    "numeric",
    "At the bottom of page 166 under 'CLINICAL FEATURES' of Amyloidosis, what are the top three affected organs in descending order (with exact percentages for Kidney and Heart)?",
    "Kidney (70%) > Heart (60%) > Liver",
    [
        "Liver (80%) > Spleen (60%) > Kidney",
        "Heart (90%) > Brain (70%) > Lung",
        "Skin (75%) > Tongue (50%) > Bone marrow",
    ],
    "At the bottom of page 166 under 'CLINICAL FEATURES': '• Kidney (70%) > Heart (60%) > Liver.'",
)


# ==============================================================================
# UNIT 9 — Page 167: Amyloidosis Organ Manifestations I (Kidney, Heart, Liver)
# ==============================================================================

add(
    S9,
    167,
    "recall",
    "At the top of page 167 under '1. Kidney :', what is the most common organ status of the kidney in Amyloidosis and what are its four listed renal presentations?",
    "Most common organ involved in amyloidosis — nephrotic range proteinuria, hypoalbuminemia, hypercholesterolemia, edema, plus tubular dysfunction (Type I & II RTA) and normal kidney size",
    [
        "Rarest organ involved — gross glomerular hematuria with RBC casts, hypocholesterolemia, and bilaterally shrunken scarred kidneys (<6 cm)",
        "Causes isolated diabetes insipidus without proteinuria and massive hydronephrosis on ultrasound",
        "Presents exclusively with acute uric-acid nephrolithiasis and hyperalbuminemia",
    ],
    "At the top of page 167 under '1. Kidney :': '• m/c organ involved in amyloidosis. • Nephrotic range proteinuria, hypoalbuminemia, hypercholesterolemia, edema. • Tubular dysfunction : Type I & II RTA. • Normal kidney size.'",
)

add(
    S9,
    167,
    "recall",
    "Under '2. Heart :' on page 167, what clinical rank does cardiac amyloidosis hold, what cardiomyopathy/arrhythmia/ECG pattern occurs, and what classic 2D-Echo appearance is shown in the echocardiogram image?",
    "Leading cause of mortality in amyloidosis — Restrictive CMP (diastolic dysfunction), AF (↑ thromboembolic risk), low-voltage ECG complexes, and 2D-Echo showing symmetrical ↑ wall thickness + 'Sparkle sign' (granular sparkling appearance)",
    [
        "Benign incidental finding — Dilated CMP with eccentric thin ventricular walls, tall LVH voltage criteria on ECG, and apical ballooning on 2D-Echo",
        "Causes isolated right-sided pulmonic stenosis with delta waves on ECG and systolic anterior motion of the mitral valve",
        "Causes high-output cardiac failure with bounding pulses and pericardial tamponade without wall thickening",
    ],
    "Under '2. Heart :' on page 167: '• Leading cause of mortality in amyloidosis. • Restrictive CMP (Diastolic dysfunction). • AF (↑ Thromboembolic risk). • ECG : Low voltage complexes. • 2D-Echo : Symmetrical ↑ wall thickness + Sparkle sign (Granular sparkling appearance).'",
)

add(
    S9,
    167,
    "recall",
    "Under '2. Heart :' on page 167, which cardiac nuclear scan diagnoses ATTR cardiac amyloidosis non-invasively, and which two drug cautions (sensitivity / contraindication) are highlighted?",
    "Tc⁹⁹ᵐ Pyrophosphate scan is diagnostic of ATTR; sensitivity to Digoxin (fibrils have high affinity → toxicity even at normal levels) and Calcium channel blockers are contraindicated (worsens LV function)",
    [
        "Tc⁹⁹ᵐ MDP skeletal scan is negative; Digoxin should be pushed to supratherapeutic doses and intravenous verapamil is first-line therapy",
        "Gallium-67 citrate scan is diagnostic of AL; beta-agonists and high-dose nifedipine improve diastolic filling",
        "FDG-PET Deauville scoring replaces echocardiography; amiodarone and digoxin have zero binding to amyloid fibrils",
    ],
    "Lower bullets under '2. Heart :' on page 167 state: '• Tc⁹⁹ᵐ Pyrophosphate scan : Diagnostic of ATTR. • Sensitivity to Digoxin (Fibrils have high affinity → Toxicity even at normal levels). • Calcium channel blockers are C/I (Worsens LV function).'",
)

add(
    S9,
    167,
    "management",
    "Under '3. Liver :' at the bottom of page 167, what clinical and enzyme profile is typical of hepatic amyloidosis, and what critical procedural contraindication (including the exact parenthetical mechanism printed on p167) is stated?",
    "Hepatomegaly and cholestatic liver disease (↑↑ ALP, normal AST & ALT); Liver biopsy is contraindicated due to ↑ risk of bleeding ('Anti-Xa antibodies' as printed on p167; classically acquired Factor X deficiency)",
    [
        "Fulminant hepatocellular necrosis (AST & ALT >5,000 IU/L with low ALP); Percutaneous large-bore liver biopsy is mandatory first-line screening",
        "Cirrhosis with shrunken nodular liver and normal ALP; Transjugular liver biopsy carries zero bleeding risk",
        "Isolated unconjugated hyperbilirubinemia without hepatomegaly; Splenic needle aspiration is preferred over abdominal fat pad biopsy",
    ],
    "Under '3. Liver :' at the bottom of page 167: '• Hepatomegaly. • Cholestatic liver disease (↑↑ ALP, normal AST & ALT). • Biopsy is C/I d/t ↑ risk of bleeding (Anti-Xa antibodies) [printed slip on p167; standard teaching = acquired Factor X deficiency from Factor X binding to amyloid fibrils].'",
)

add(
    S9,
    167,
    "scenario",
    "A 68-year-old man with IgG-lambda multiple myeloma presents with anasarca, nephrotic-range proteinuria (6 g/day) with normal-sized kidneys on ultrasound, exertional dyspnea, low-voltage QRS complexes on limb leads despite concentrically thickened left ventricular walls with a granular 'sparkle sign' on 2D-Echo, and marked hepatomegaly with isolated elevated ALP. Which drug must be strictly AVOIDED because it worsens LV function, and which organ biopsy is CONTRAINDICATED due to severe hemorrhage risk per page 167?",
    "Calcium channel blockers are contraindicated (and digoxin causes toxicity even at normal serum levels); percutaneous liver biopsy is contraindicated — perform abdominal fat pad aspiration instead",
    [
        "Loop diuretics are contraindicated; abdominal fat pad aspiration is contraindicated — perform percutaneous core liver biopsy first",
        "Bortezomib is contraindicated; rectal biopsy is contraindicated — perform blind splenic puncture",
        "Tafamidis is contraindicated in all cardiomyopathy; high-dose verapamil + digoxin loading is first-line",
    ],
    "Pages 167–168 tie together nephrotic syndrome + normal kidney size, low-voltage ECG + concentrically thickened sparkling myocardium on 2D-Echo, CCB contraindication + digoxin sensitivity, contraindication to liver biopsy due to bleeding risk, and abdominal fat pad biopsy as investigation of choice.",
)


# ==============================================================================
# UNIT 10 — Page 168: Amyloidosis Organ Manifestations II, Congo Red Biopsy & Rx
# ==============================================================================

add(
    S10,
    168,
    "recall",
    "At the top of page 168 under items '4. Spleen' and '5. GI manifestations', what peripheral smear sign indicates functional hyposplenism and what GI complications are listed?",
    "Spleen: Splenomegaly with Howell-Jolly bodies on PS (hyposplenism); GI: Malabsorption, Chronic diarrhea, Weight loss, and Gastroparesis",
    [
        "Spleen: Hypersplenism with absent RBC inclusions; GI: Hypertrophic pyloric stenosis and toxic megacolon",
        "Spleen: Splenic infarction with Heinz bodies; GI: Achalasia cardia and Mallory-Weiss tear",
        "Spleen: Normal spleen function; GI: Non-atrophic H. pylori pan-gastritis in 95%",
    ],
    "Items 4 & 5 at the top of page 168 list: '4. Spleen : • Splenomegaly • Hyposplenism (Howell-Jolly bodies on PS).' '5. GI manifestations : • Malabsorption • Chronic diarrhea • Weight loss • Gastroparesis.'",
)

add(
    S10,
    168,
    "recall",
    "Under items '6. ANS manifestations', '7. CNS manifestations', and '8. Endocrine manifestations' on page 168, which specific conditions are listed?",
    "ANS: Postural hypotension, Reflex tachycardia (as printed), Inability to sweat; CNS: Alzheimer's (Aβ amyloid protein), Cerebral amyloid angiopathy (lobar hemorrhage); Endocrine: Medullary thyroid carcinoma (Calcitonin), DM Type II (Amylin)",
    [
        "ANS: Severe hypertension, bradycardia, hyperhidrosis; CNS: Basal ganglia hypertensive bleed; Endocrine: Papillary thyroid carcinoma (Thyroglobulin), DM Type I",
        "ANS: Isolated Horner syndrome; CNS: Subacute combined degeneration; Endocrine: Pheochromocytoma (Catecholamines)",
        "ANS: Normal orthostatic blood pressure; CNS: Meningioma; Endocrine: Hyperparathyroidism (PTH)",
    ],
    "Items 6–8 on page 168 state: '6. ANS manifestations : • Postural hypotension. • Reflex tachycardia [as printed]. • Inability to sweat.' '7. CNS manifestations : • Alzheimer's (Aβ amyloid protein). • Cerebral amyloid angiopathy (Lobar hemorrhage).' '8. Endocrine manifestations : • Medullary thyroid carcinoma (Calcitonin). • DM Type II (Amylin).'",
)

add(
    S10,
    168,
    "recall",
    "Under '9. Hemorrhagic manifestations :' and the four clinical photographs across the middle of page 168, which pathognomonic eyelid bleed, coagulation defect, and four photo captions are highlighted?",
    "Periorbital ecchymosis ('Raccoon eyes'), Factor X deficiency, plus printed bullets Macroglossia & Waxy eyelid & papules — alongside photos captioned 'Hemorrhagic eyelids', 'Macroglossia', 'Shoulder pad', and 'Amyloid nails'",
    [
        "Retro-auricular Battle sign, Factor VIII inhibitor, and photos captioned 'Heliotrope rash', 'Gottron papules', 'Shawl sign', and 'Pitting nails'",
        "Conjunctival petechiae, Bernard-Soulier syndrome, and photos captioned 'Strawberry tongue', 'Malar rash', 'Erythema nodosum', and 'Koilonychia'",
        "Subungual splinter hemorrhages, Protein C deficiency, and photos captioned 'Kayser-Fleischer ring', 'Spider nevi', 'Caput medusae', and 'Clubbing'",
    ],
    "Under '9. Hemorrhagic manifestations :' on page 168: '• Periorbital ecchymosis (\"Raccoon eyes\"). • Factor X deficiency. • Macroglossia. • Waxy eyelid & papules.' Below are the four clinical photos captioned 'Hemorrhagic eyelids', 'Macroglossia', 'Shoulder pad', and 'Amyloid nails'.",
)

add(
    S10,
    168,
    "recall",
    "Under 'DIAGNOSIS → Biopsy :' on page 168, what biopsy site is the Investigation of Choice (IOC), what alternative sites can be sampled, and what staining appearance is illustrated?",
    "Abdominal fat pad (IOC), or Rectum, kidney; Congo red stain showing pink eosinophilic material under light microscopy and Apple-green birefringence under polarized light",
    [
        "Percutaneous liver core biopsy (IOC), or Spleen; Prussian blue stain showing bright turquoise hemosiderin granules",
        "Cervical lymph node FNAC (IOC); Periodic acid-Schiff (PAS) stain showing block-like magenta positivity without birefringence",
        "Sural nerve biopsy only; Sudan Black B stain showing needle-shaped Auer rods",
    ],
    "Under 'DIAGNOSIS → Biopsy :' on page 168: '• Abdominal fat pad (IOC) • Rectum, kidney • Congo red stain : Apple green birefringence under polarized light', accompanied by the dual 'Congo red stain' / 'Apple green birefringence' photomicrograph.",
)

add(
    S10,
    168,
    "match",
    "At the bottom of page 168 under 'TREATMENT' of Amyloidosis, match each amyloid subtype with its listed first-line therapy — 1) Primary AL amyloidosis 2) Secondary AA amyloidosis 3) Familial Mediterranean fever (AA prevention) 4) ATTR cardiac/hereditary amyloidosis … A) Tafamidis B) Colchicine C) Cyclophosphamide + Bortezomib + Dexamethasone (CyBorD) & Daratumumab D) Treat underlying inflammatory/infectious cause",
    "1-C, 2-D, 3-B, 4-A",
    [
        "1-D, 2-C, 3-B, 4-A",
        "1-C, 2-B, 3-D, 4-A",
        "1-A, 2-D, 3-B, 4-C",
    ],
    "At the bottom of page 168 under 'TREATMENT': Primary AL = 'Cyclophosphamide + Bortezomib + Dexamethasone (CyBorD)' and 'Daratumumab'; Secondary AA = '• Treat underlying cause • Colchicine for Familial Mediterranean fever'; ATTR = 'Tafamidis'.",
)

add(
    S10,
    168,
    "truefalse",
    "Which statement accurately reflects the Amyloidosis diagnosis, clinical features, and treatment on page 168?",
    "True — Abdominal fat pad biopsy stained with Congo red demonstrating apple-green birefringence under polarized light is the investigation of choice, and Primary AL amyloidosis is treated with CyBorD (Cyclophosphamide + Bortezomib + Dexamethasone) and Daratumumab",
    [
        "True — Medullary thyroid carcinoma deposits Amylin fibrils while Type II Diabetes Mellitus deposits Calcitonin fibrils",
        "False — Cerebral amyloid angiopathy deposits Aβ amyloid protein in cerebral vessels and causes lobar intracerebral hemorrhage",
        "False — Colchicine is specifically used in Familial Mediterranean fever to prevent Secondary AA amyloidosis",
    ],
    "All four facts come directly from page 168: Medullary thyroid carcinoma deposits Calcitonin and DM Type II deposits Amylin; Cerebral amyloid angiopathy causes lobar hemorrhage; Abdominal fat pad Congo red biopsy is IOC; CyBorD + Daratumumab treat AL amyloidosis and Colchicine treats Familial Mediterranean fever.",
)


GUIDES = {
    S1: (
        "Normal Plasma Cell Morphology, Russell/Dutcher Bodies & Polyclonal vs Monoclonal Hypergammaglobulinemia",
        "Normal plasma cell: B-cell origin, eccentric cartwheel nucleus, perinuclear Golgi halo; secretes antibodies (2 heavy [IgG, IgA, IgM, IgD, IgE] + 2 light [κ, λ] chains; normal κ : λ = 2 : 1).\n"
        "Inclusions: Russell body = cytoplasmic immunoglobulins; Dutcher body = intranuclear immunoglobulin inclusions.\n"
        "Polyclonal vs Monoclonal: Polyclonal = CD19+, CD38+, CD138+, normal κ:λ, seen in HIV, autoimmune diseases, TB, CLD, malaria; Monoclonal = CD19–, CD38+, CD138+, CD45–, abnormal κ:λ, seen in Multiple myeloma & Waldenstrom macroglobulinemia.",
    ),
    S2: (
        "Plasma Cell Disorder Classification, Myeloma Overview, Smear Variants (Mott/Flame), MGUS vs SMM vs MM & Slim-CRAB",
        "Classification & MM profile: ↑ Plasma cell proliferation (MGUS, SMM, MM, solitary plasmacytoma, plasma cell leukemia [≥20% circulating plasma cells, IgE]) vs ↑ Antibody only (WM, heavy chain disease, AL amyloidosis). MM: 2nd m/c hematologic malignancy, >70 yrs, Blacks, M>F, pesticide exposure, IgG (55%) > IgA > IgM > IgD > IgE, light-chain only 20%; smears show Rouleaux, Mott cells, Flame cells.\n"
        "MGUS vs SMM vs MM: MGUS (<3 g/dl M-protein, <10% BM PCs, no CRAB, 1%/yr progression); SMM (>3 g/dl, 10–60% BM PCs, no CRAB, 10%/yr); MM (>3 g/dl, >10% BM PCs + MDE OR >60% without MDE).\n"
        "Slim-CRAB MDE: Ca >11 mg/dl, Cr >2 mg/dl or GFR <40 ml/min, Hb <10 g/dl, ≥1 lytic bone lesion (>5 mm); plus ≥60% clonal BM PCs, >1 focal MRI lesion (≥5 mm), sFLC ratio ≥100.",
    ),
    S3: (
        "Myeloma Investigations (SPEP/UPEP, IFE, sFLC, ISS β2-M/Albumin, FISH, Whole-Body Low-Dose CT) & Therapeutics",
        "Screening & workup: SPEP detects M-spike (misses 20% light-chain MM); 24-hr UPEP detects Bence Jones protein (not seen on dipstick); Serum IFE identifies heavy/light chain; sFLC ratio ≥100 diagnostic & monitors activity.\n"
        "ISS staging, FISH & imaging: β2-microglobulin = single most powerful survival predictor (Stage I: β2M <3.5 & Alb ≥3.5; Stage III: β2M >5.5). High-risk FISH: t(4;14), t(14;16), del(17p), 1q amp. Imaging: Whole-body low-dose CT = IOC; MRI for cord compression/plasmacytoma; Tc-99m scan has NO hot spots.\n"
        "Treatment: Observe MGUS/SMM; MM transplant-eligible → VRD triplet [Lenalidomide + Bortezomib + Dexamethasone] → Autologous SCT; Proteasome inhibitors (Bortezomib, Carfilzomib), IMiDs (Thalidomide, Lenalidomide, Pomalidomide), Anti-CD38 (Daratumumab, Isatuximab), SLAMF7 (Elotuzumab) + supportive Hydration, Analgesia, Bisphosphonates.",
    ),
    S4: (
        "Bony & Renal Pathogenesis (DKK-1/RANK-L, Myeloma Kidney, Type II RTA, Amyloidosis) & Hypercalcemia / Infection Mechanisms",
        "Bony lesions: Bone pain = m/c symptom; Vertebra > Rib > Skull ('raindrop' punched-out lesions) > Pelvis > Femur > Clavicle > Scapula. Dickkopf-1 inhibits osteoblasts (↓ ALP, negative bone scan) while IL-6/IL-1β/TNF-α → ↑ RANK-L → osteoclast activation → lytic lesions & hypercalcemia.\n"
        "Renal disease: Hypercalcemia = m/c cause of renal failure (vasoconstriction & nephrogenic DI dehydration); Myeloma kidney = cast nephropathy with Tamm-Horsfall protein (m/c tubular damage); Type II RTA = Fanconi syndrome (glycosuria, aminoaciduria, phosphaturia, hypouricemia); AL amyloidosis (nephrotic + normal-sized kidneys) & LCDD.\n"
        "Infections: m/c cause of death in MM — respiratory (S. pneumoniae m/c) & UTI due to hypogammaglobulinemia, abnormal antibodies, CD4 lymphocytopenia, and ↓ neutrophil lysozyme.",
    ),
    S5: (
        "Neuromyeloma Diagram, POEM Syndrome, Solitary Plasmacytoma, Poor Prognostic Factors & Waldenström Intro",
        "Neuromyeloma & POEM: Hypercalcemia (coma), hyperviscosity, cord compression, amyloid/light-chain sensory neuropathy (IgM & IgG); POEM syndrome has osteosclerotic lesions.\n"
        "Solitary plasmacytoma & prognosis: No CRAB, BM <10% plasma cells; bone or extramedullary (m/c nasopharynx); curative radiation. Poor MM prognosis: ↑ LDH, ↑ β2-microglobulin [printed β2-glycoprotein], circulating PCs, ISS III, hypodiploidy, del(17p).\n"
        "Waldenström intro: Lymphoplasmacytic lymphoma secreting IgM (>60 yrs, M>F) — 'IgM-secreting CLL' with HSM & lymphadenopathy, NO lytic bone lesions, NO renal disease, NO hypercalcemia.",
    ),
    S6: (
        "Waldenström's Macroglobulinemia: Chr 6q / MYD88 L265P Pathogenesis, Hyperviscosity, Cryoglobulins & Bing-Neel Syndrome",
        "WM pathogenesis & diagnosis: Post-GC B-cells with del(6q) + somatic MYD88 L265P (>90% cases) → >10% BM lymphoplasmacytoid cells + mast cells, Rouleaux & +ve Coombs test, IgM spike (CD19+, CD20+, CD138–).\n"
        "Clinical features: Fatigue (m/c), HSM/LAD/anemia, IgM hyperviscosity (diplopia, tinnitus, ataxia, dilated segmented 'sausage' retinal veins, stroke, CCF), cryoglobulinemia (Raynaud's, cold urticaria), anti-MAG sensorimotor neuropathy.\n"
        "Treatment & Bing-Neel: Urgent plasmapheresis for hyperviscosity; Bortezomib, Rituximab, Bendamustine, Ibrutinib for severe disease. Bing-Neel syndrome = CNS leptomeningeal infiltration + hyperviscosity.",
    ),
    S7: (
        "POEMS Syndrome, Heavy Chain Diseases Table (Franklin's, Seligmann's, Mu) & Amyloidosis Definition/Types",
        "POEMS syndrome: Polyneuropathy (1st presenting symptom), Organomegaly, Endocrinopathy (gynecomastia, impotence, amenorrhea, DM II, hypothyroidism), Monoclonal plasma cells, Skin changes + osteosclerotic lesions + thrombocytosis/erythrocytosis → Rx Autologous HSCT.\n"
        "Heavy chain diseases: Franklin's (γ — LAD + Waldeyer's ring + palatal edema; fatal infections); Seligmann's (α — m/c; IPSID malabsorption/diarrhea; responds to antibiotics); Mu (μ — CLL-associated, vacuolated lymphocytes, urinary κ light chains).\n"
        "Amyloidosis basics: Extracellular beta-pleated sheet protein fibril deposition — Primary AL, Secondary AA, Dialysis-related (Aβ2M), Familial/Senile (ATTR).",
    ),
    S8: (
        "Primary AL vs Secondary AA vs Dialysis (Aβ2M) vs Familial/Senile ATTR Amyloidosis & Organ Overview",
        "Primary AL & Secondary AA: AL = m/c systemic amyloidosis, associated with MM (20%) & WM, λ > κ light chains, rapidly fatal untreated; AA = Serum Amyloid A precursor, TB (only infective cause), RA/IBD/Ank spondylitis/FMF (IL-1 mutation), kidney m/c organ.\n"
        "Dialysis & ATTR: Dialysis = β2-microglobulin (Aβ2M) causing arthropathy & carpal tunnel syndrome; ATTRm (AD hepatic TTR mutation → neuropathy + CMP) & ATTRwt (>70 yrs senile restrictive CMP) → Rx Tafamidis (TTR tetramer stabilizer); rare precursors = Apo A1/A2, Gelsolin, Fibrinogen Aα, Lysozyme.\n"
        "Organ hierarchy: Kidney (70%) > Heart (60%) > Liver.",
    ),
    S9: (
        "Amyloidosis Organ Manifestations I: Renal, Cardiac (Restrictive CMP, Sparkle Sign, Digoxin) & Hepatic Bleeding Risk",
        "Kidney (70%, m/c organ): Nephrotic-range proteinuria, hypoalbuminemia, hypercholesterolemia, edema, Type I & II RTA, with normal-sized kidneys.\n"
        "Heart (60%, #1 cause of mortality): Restrictive CMP (diastolic dysfunction), AF/thromboembolism, low-voltage ECG despite symmetric wall thickening + granular 'Sparkle sign' on 2D-Echo; Tc-99m PYP scan diagnoses ATTR; extreme Digoxin toxicity risk & Calcium channel blockers contraindicated.\n"
        "Liver: Hepatomegaly + cholestatic pattern (↑↑ ALP, normal AST/ALT); liver biopsy contraindicated due to severe bleeding risk (printed 'Anti-Xa antibodies'; classically Factor X binding).",
    ),
    S10: (
        "Amyloidosis Organ Manifestations II: Spleen/GI/ANS/CNS/Endocrine/Hemorrhagic Signs, Congo Red Biopsy & Rx",
        "Other organs: Spleen (splenomegaly + hyposplenism Howell-Jolly bodies); GI (malabsorption, diarrhea, gastroparesis); ANS (postural hypotension, anhidrosis); CNS (Alzheimer's Aβ, cerebral amyloid angiopathy lobar hemorrhage); Endocrine (MTC calcitonin, Type II DM amylin).\n"
        "Mucocutaneous/hemorrhagic signs: Periorbital ecchymosis ('raccoon eyes'), Factor X deficiency, macroglossia, waxy eyelid papules, 'shoulder pad' sign, amyloid nails.\n"
        "Diagnosis & Rx: Abdominal fat pad biopsy = IOC (or rectum/kidney) → Congo red apple-green birefringence under polarized light. Rx: AL → CyBorD + Daratumumab; AA → treat cause / Colchicine in FMF; ATTR → Tafamidis.",
    ),
}


def main() -> None:
    questions = []
    for i, (sec, page, fmt, stem, opts, ans, exp) in enumerate(RAW, 1):
        questions.append({
            "id": f"MED-C{CHAPTER}-{i:02d}",
            "sec": sec,
            "page": page,
            "fmt": fmt,
            "q": stem,
            "opts": opts,
            "ans": ans,
            "exp": exp,
        })
    sections = list(dict.fromkeys(row[0] for row in RAW))
    units = []
    for n, sec in enumerate(sections, 1):
        title, guide = GUIDES[sec]
        units.append({
            "id": f"MED-U{CHAPTER}-{n}",
            "ch": CHAPTER,
            "n": n,
            "title": title,
            "sec": sec,
            "guide": guide,
            "qs": [q["id"] for q in questions if q["sec"] == sec],
        })
    out = DATA / f"ch{CHAPTER:02d}.json"
    out.write_text(
        json.dumps(
            {
                "chapter": CHAPTER,
                "title": TITLE,
                "pageRange": PAGES,
                "questions": questions,
                "units": units,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {out.name}: {len(questions)} questions / {len(units)} units")


if __name__ == "__main__":
    main()
