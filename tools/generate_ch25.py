#!/usr/bin/env python3
"""Generate Chapter 25: Chronic Lymphocytic Leukemia (Book p142–145).

Every question is anchored to a specific line, note box, flowchart arrow, table
cell, or peripheral smear / bone marrow caption in uploads/02.pdf (PDF pages
25–28 = Book pages 142–145) in strict book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 25
TITLE = "Chronic Lymphocytic Leukemia"
PAGES = "142-145"

S1 = "CLL Overview, Epidemiology, Defective Apoptosis Pathophysiology, Small Lymphocytic Leukemia (SLL) & Etiology"
S2 = "CLL Investigations, Smudge Cells, Richter Transformation, Warm AIHA, Staging Table & Indications for Treatment"
S3 = "CLL Prognostic Factors Table, FCR & BR Treatment Regimens, and Hairy Cell Leukemia Overview & Pathogenesis"
S4 = "Hairy Cell Leukemia Investigations (Smear, Fried-Egg Marrow, Immunophenotype), Treatment & PAN Association"

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
# UNIT 1 — Page 142: CLL Overview, Pathophysiology, SLL Note & Etiology
# ==============================================================================

add(
    S1,
    142,
    "recall",
    "Under 'Overview' on page 142, what is the status of Chronic Lymphocytic Leukemia (CLL) among lymphoid leukemias, its sex predilection, its grade, and the boxed Note on the most common myeloid leukemia?",
    "Most common lymphoid leukemia; Males > Females; low-grade leukemia; boxed Note states most common myeloid leukemia is AML",
    [
        "Rarest lymphoid leukemia; Females > Males; high-grade acute leukemia; boxed Note states most common myeloid leukemia is CML",
        "Most common childhood leukemia; Females = Males; aggressive leukemia; boxed Note states most common myeloid leukemia is APML",
        "Second most common lymphoid leukemia after hairy cell leukemia; Females > Males; high-grade leukemia; m/c myeloid leukemia is MDS",
    ],
    "Under 'Overview :' on page 142: '• Most common lymphoid leukemia. • Males > Females. • Low grade leukemia.' The right-side boxed Note reads: 'Note : m/c myeloid leukemia : AML.'",
)

add(
    S1,
    142,
    "numeric",
    "What percentage of patients with CLL are asymptomatic at presentation, and what median age of diagnosis is printed under 'Overview' on page 142?",
    "Asymptomatic: 80–85% (mostly indolent); median age of diagnosis: 72 years",
    [
        "Asymptomatic: 10–15% (rapidly progressive); median age of diagnosis: 13 years",
        "Asymptomatic: 50% (acute marrow failure); median age of diagnosis: 40–60 years",
        "Asymptomatic: 20–25% (early hyperviscosity); median age of diagnosis: 65 years",
    ],
    "Bullets 4–5 under 'Overview :' on page 142 read: '• Asymptomatic : 80–85% (mostly indolent). • Median age of diagnosis : 72 years.'",
)

add(
    S1,
    142,
    "numeric",
    "According to the final bullet under 'Overview' on page 142, what is the median survival in CLL and what percentage of patients undergo spontaneous regression?",
    "Median survival: 10 years (can be increased with drugs); 1–2% undergo spontaneous regression",
    [
        "Median survival: 2–3 months untreated; 25% undergo spontaneous regression",
        "Median survival: 5 years with transplant only; 10–20% undergo spontaneous regression",
        "Median survival: 2–3 years; 0% ever undergo spontaneous regression",
    ],
    "Bullet 6 under 'Overview :' on page 142 reads: '• Median survival : 10 years (can be increased with drugs); 1–2% undergo spontaneous regression.'",
)

add(
    S1,
    142,
    "recall",
    "Under 'Pathophysiology → Physiology : Naive B cells (in blood)' on page 142, what normal surface marker profile and fate do circulating naive B cells exhibit?",
    "Express CD19, CD20, CD21, CD22, CD79a, CD79b, and Surface IgM; normally undergo apoptosis",
    [
        "Express CD5, CD23, Cyclin D, and Surface IgD; normally undergo indefinite clonal self-renewal",
        "Express CD34, HLA-DR, PAX-5, and TdT without surface immunoglobulin; normally differentiate into plasma cells in blood",
        "Express CD10, BCL-6, Annexin, and TRAP; normally migrate directly into splenic red pulp cords",
    ],
    "Under 'Physiology : Naive B cells (in blood) :' on page 142: '• CD19, CD20, CD21, CD22, CD79a, CD79b, Surface IgM. • Normally undergo apoptosis.'",
)

add(
    S1,
    142,
    "recall",
    "In the 'Pathology' cascade on page 142, what sequential events lead from defective apoptosis of naive B-cells to CLL, and which two aberrant surface markers are acquired?",
    "Defective apoptosis of naive B-cells → clonal naive B-cell expansion with acquisition of CD5 and CD23 → monoclonal B cell lymphocytosis → CLL",
    [
        "Complete arrest of differentiation → myeloblast expansion with acquisition of CD13 and CD33 → myelodysplasia → CLL",
        "Somatic hypermutation in germinal centre dark zone → acquisition of CD10 and BCL-6 → polyclonal lymphocytosis → CLL",
        "Gain of BRAF mutation in post-germinal memory B cell → acquisition of CD103 and TRAP → marrow fibrosis → CLL",
    ],
    "Under 'Pathology :' on page 142: 'Defective apoptosis of naive B-cells → • Clonal naive B-cell expansion • Acquire CD5, CD23 → Monoclonal B cell lymphocytosis → If lymphocyte >5000 cells/µL → CLL.'",
)

add(
    S1,
    142,
    "numeric",
    "In the pathology flowchart on page 142, monoclonal B-cell lymphocytosis is diagnosed as Chronic Lymphocytic Leukemia (CLL) when the blood lymphocyte count exceeds what cutoff?",
    ">5000 cells/µL",
    [
        ">50,000 cells/µL",
        ">1,00,000 cells/µL",
        ">1500 cells/µL",
    ],
    "The arrow between 'Monoclonal B cell lymphocytosis' and 'CLL' on page 142 specifies: 'If lymphocyte >5000 cells/µL → CLL.'",
)

add(
    S1,
    142,
    "fillup",
    "Under 'Note : Small lymphocytic leukemia (SLL)' on page 142, SLL arises from a ______ B cell, shares the same immunophenotyping and features as CLL, and causes monoclonal B lymphocytosis in the lymph node.",
    "memory",
    [
        "pro-B",
        "immature",
        "centroblast",
    ],
    "Under 'Note : Small lymphocytic leukemia (SLL)' on page 142: '• Arises from memory B cell. • Immunophenotyping : Same as CLL. • Features : Same as CLL. • Monoclonal B lymphocytosis in lymph node : – Painless asymptomatic lymphadenopathy. – Can have splenomegaly.'",
)

add(
    S1,
    142,
    "recall",
    "What clinical manifestations result from 'monoclonal B lymphocytosis in lymph node' in Small Lymphocytic Leukemia (SLL) on page 142?",
    "Painless asymptomatic lymphadenopathy and can have splenomegaly",
    [
        "Exquisitely tender suppurative lymphadenitis with overlying skin sinus tracts and absence of splenic enlargement",
        "Anterior mediastinal thymic mass with acute tracheal compression and superior vena cava obstruction in adolescent boys",
        "Orbital soft-tissue chloroma with gingival hypertrophy and perianal abscesses without lymph node enlargement",
    ],
    "Under 'Note : Small lymphocytic leukemia (SLL)' on page 142: '• Monoclonal B lymphocytosis in lymph node : – Painless asymptomatic lymphadenopathy. – Can have splenomegaly.'",
)

add(
    S1,
    142,
    "truefalse",
    "Which statement accurately reflects the 'Etiology' section at the bottom of page 142?",
    "True — Chronic lymphocytic leukemia demonstrates strong familial inheritance and carries no risk with radiation",
    [
        "True — High-dose ionizing radiation within 6–8 years is the leading environmental cause of chronic lymphocytic leukemia",
        "False — Small lymphocytic leukemia (SLL) shares the same immunophenotyping and clinical features as CLL",
        "False — Monoclonal B-cell lymphocytosis progresses to CLL when peripheral blood lymphocytes exceed 5000 cells/µL",
    ],
    "At the bottom of page 142 under 'Etiology :': '• Strong familial inheritance. • No risk with radiation.'",
)


# ==============================================================================
# UNIT 2 — Page 143: Investigations, Smudge Cell, Richter Transformation, Staging & Rx Indications
# ==============================================================================

add(
    S2,
    143,
    "numeric",
    "Under 'Investigation → Blood count' on page 143, what typical unexplained lymphocytosis level is seen in CLL, and which cytopenias appear rarely?",
    "Unexplained lymphocytosis around 60,000–70,000; rarely normocytic normochromic anemia and thrombocytopenia",
    [
        "Unexplained lymphocytosis around 5,000–6,000; universally microcytic hypochromic anemia and thrombocytosis",
        "Unexplained leukopenia around 1,000–2,000; universally macrocytic megaloblastic anemia and monocytopenia",
        "Unexplained lymphocytosis around 5,00,000–8,00,000; universally teardrop cells and basophilia",
    ],
    "At the top of page 143 under 'Investigation : → Blood count :': '– Unexplained lymphocytosis (Around 60,000–70,000). – Rarely : Normocytic normochromic anemia, thrombocytopenia.'",
)

add(
    S2,
    143,
    "recall",
    "Which four morphological features describe the 'CLL lymphocyte' on peripheral smear on page 143?",
    "Small, blue, round cell; pale cytoplasm; no granules; moderate condensation of chromatin",
    [
        "Large cell with high N:C ratio; deep basophilic vacuolated cytoplasm; abundant granules; lacy open chromatin",
        "Mononuclear cell with bilobed eccentric nucleus; abundant sky-blue cytoplasm; circumferential hairy projections",
        "Large binucleate mirror-image cell; abundant amphophilic cytoplasm; prominent eosinophilic owl-eye nucleoli",
    ],
    "Under 'Peripheral smear : CLL lymphocyte' on page 143: '– Small, blue, round. – Pale cytoplasm. – No granules. – Moderate condensation of chromatin.'",
)

add(
    S2,
    143,
    "fillup",
    "On the 'Peripheral smear : CLL' photomicrograph on page 143, ruptured fragile leukemic lymphocytes visible alongside small blue round lymphocytes are labelled ______.",
    "Smudge cell",
    [
        "Hairy cell",
        "Faggot cell",
        "Bite cell",
    ],
    "The right-hand panel of the 'Peripheral smear : CLL' image on page 143 labels the crushed lymphocyte remnant 'Smudge cell'. Also listed below it: 'Immunophenotyping' and 'Lymph node (LN) biopsy : Diffuse effacement of lymph node architecture (For SLL).'",
)

add(
    S2,
    143,
    "recall",
    "What lymph node (LN) biopsy finding is specified on page 143 for Small Lymphocytic Leukemia (SLL)?",
    "Diffuse effacement of lymph node architecture",
    [
        "Nodular fibrotic bands surrounding lacunar Reed-Sternberg cells",
        "Starry-sky sheets of tingible-body macrophages amidst medium blasts",
        "Non-caseating epithelioid cell granulomas restricted to subcapsular sinuses",
    ],
    "Page 143 states: 'Lymph node (LN) biopsy : Diffuse effacement of lymph node architecture (For SLL).'",
)

add(
    S2,
    143,
    "recall",
    "Under 'Indicators for high risk → 1. Richter transformation' on page 143, which classical low-grade-to-high-grade lymphoma conversion defines Richter transformation?",
    "Low-grade lymphoma (classically SLL) → High-grade lymphoma (classically DLBCL : Diffuse large B cell lymphoma)",
    [
        "Low-grade CLL → Acute promyelocytic leukemia (APML M3) with t(15;17) translocation",
        "Low-grade follicular lymphoma → Hairy cell leukemia with BRAF V600E mutation",
        "Low-grade marginal zone lymphoma → Multiple myeloma with lytic bone lesions",
    ],
    "Under 'Indicators for high risk :' on page 143: '1. Richter transformation : Low grade lymphoma (Classically SLL) → High grade lymphoma (Classically DLBCL : Diffuse large B cell lymphoma).'",
)

add(
    S2,
    143,
    "numeric",
    "Which clinical, biochemical, and PET-scan criteria are listed under 'Features' of Richter transformation on page 143?",
    "↑ lymphadenopathy and B symptoms: weight loss >10% in 6 months, fever >100.4°F, ↑↑ LDH, and ↑ uptake in lymph nodes on PET scan",
    [
        "Shrinking lymph nodes with weight loss >5% in 12 months, low-grade temperature <99°F, normal LDH, and photopenic lymph nodes on PET scan",
        "Isolated splenomegaly without lymphadenopathy, weight gain from edema, subnormal body temperature, ↓ LDH, and negative bone scan",
        "Painless stable cervical nodes, nocturnal pruritus alone, normal body weight, normal LDH, and isolated hepatic uptake on PET scan",
    ],
    "Under 'Features :' of Richter transformation on page 143: '• ↑ lymphadenopathy. • B symptoms : – Weight loss : >10% in 6 months. – Fever >100.4°F. – ↑↑ LDH. – ↑ uptake in lymph nodes in PET scan.'",
)

add(
    S2,
    143,
    "recall",
    "What second high-risk association is listed under 'Indicators for high risk' on page 143 in CLL, and which test identifies it?",
    "Warm antibody AIHA association — identified by DAT / Coomb's test",
    [
        "Cold agglutinin disease — identified only after cooling serum to 0–4 °C",
        "Paroxysmal cold hemoglobinuria — identified by Donath-Landsteiner test",
        "Hereditary spherocytosis — identified by eosin-5-maleimide (EMA) flow cytometry",
    ],
    "Item 2 under 'Indicators for high risk :' on page 143 states: '2. Warm antibody AIHA association : Identified by DAT/Coomb's test.'",
)

add(
    S2,
    143,
    "recall",
    "In the 'Rai and Binet staging :' table on page 143, which two stages fall under 'No treatment', and what are their respective clinical features?",
    "Stage 0 (Lymphocytosis) and Stage 1 (Lymphocytosis + lymphadenopathy) — both require 'No treatment'",
    [
        "Stage 0 (Lymphocytosis) only — whereas Stage 1 (Lymphocytosis + lymphadenopathy) requires immediate FCR chemotherapy",
        "Stage 1 (Hepatosplenomegaly) and Stage 2 (Anemia) — both require 'No treatment'",
        "All five stages (Stage 0 through Stage 4) require immediate systemic chemo-immunotherapy at diagnosis",
    ],
    "In the 'Rai and Binet staging :' table on page 143: Stage 0 = Lymphocytosis ('No treatment') and Stage 1 = Lymphocytosis + lymphadenopathy ('No treatment'), while Stages 2–4 fall under 'Treatment required'.",
)

add(
    S2,
    143,
    "match",
    "In the 'Rai and Binet staging :' table as printed on page 143, match Stages 1 through 4 with their printed 'Features' and 'Treatment' column entry — 1) Stage 1 2) Stage 2 3) Stage 3 4) Stage 4 … A) Hepatosplenomegaly — Treatment required B) Lymphocytosis + lymphadenopathy — No treatment C) Pancytopenia (as printed) — Treatment required D) Anemia — Treatment required",
    "1-B, 2-A, 3-D, 4-C",
    [
        "1-B, 2-D, 3-A, 4-C",
        "1-A, 2-B, 3-C, 4-D",
        "1-C, 2-A, 3-D, 4-B",
    ],
    "The 'Rai and Binet staging :' table on page 143 prints: Stage 0 = Lymphocytosis (No treatment); Stage 1 = Lymphocytosis + lymphadenopathy (No treatment); Stage 2 = Hepatosplenomegaly (Treatment required); Stage 3 = Anemia (Treatment required); Stage 4 = Pancytopenia [as printed] (Treatment required).",
)

add(
    S2,
    143,
    "management",
    "At the bottom of page 143, what are ALL the listed 'Indications of treatment :' in Chronic Lymphocytic Leukemia?",
    "Features of Richter transformation; AIHA unresponsive to steroids; and Stage 2, 3, 4 disease (massive splenomegaly, marrow failure)",
    [
        "Stage 0 isolated lymphocytosis >5,000 cells/µL and Stage 1 painless cervical lymphadenopathy immediately upon diagnosis",
        "Any positive Coombs test that responds promptly to oral steroids, or isolated smudge cells on routine peripheral blood smear",
        "Chromosome 13q deletion with hypermutated Ig heavy chain in an asymptomatic 75-year-old patient with Stage 0 disease",
    ],
    "At the bottom of page 143 under 'Indications of treatment :': '• Features of Richter transformation. • AIHA unresponsive to steroids. • Stage 2, 3, 4 : – Massive splenomegaly. – Marrow failure.'",
)

add(
    S2,
    143,
    "scenario",
    "A 74-year-old man under observation for Stage 1 CLL (lymphocytosis + painless cervical lymphadenopathy) returns with rapidly enlarging cervical nodes, drenching night sweats, temperature 101.6°F, 12% weight loss over 5 months, markedly elevated serum LDH, and intense FDG uptake on lymph node PET scan. What complication has developed and what management change is indicated per page 143?",
    "Richter transformation into high-grade DLBCL; active treatment is required (no longer watch-and-wait)",
    [
        "Spontaneous regression of CLL (seen in 1–2% of patients); continue observation without biopsy or chemotherapy",
        "Progression from Stage 0 to Stage 1 CLL; continue observation without treatment as Stages 0 and 1 require no therapy",
        "Parvovirus B19 transient aplastic crisis; administer intravenous immunoglobulin alone without lymphoma therapy",
    ],
    "On page 143, enlarging lymphadenopathy + weight loss >10% in 6 months + fever >100.4°F + ↑↑ LDH + ↑ nodal uptake on PET scan are classic features of Richter transformation (SLL → DLBCL), which is a primary indication for treatment.",
)


# ==============================================================================
# UNIT 3 — Page 144: CLL Prognostic Factors & Regimens; Hairy Cell Leukemia Overview & Pathogenesis
# ==============================================================================

add(
    S3,
    144,
    "recall",
    "Which two prognostic markers are listed under the 'Good' column of the CLL 'Prognostic factors :' table on page 144?",
    "Hypermutated Ig heavy chain and Chromosome 13q deletion",
    [
        "Unmutated Ig heavy chain and Chromosome 17p deletion",
        "Chromosome 11q deletion, Trisomy 12, and Zap-70 positivity",
        "Elevated serum β2-microglobulin and elevated LDH levels",
    ],
    "In the 'Prognostic factors :' table on page 144, the 'Good' column lists: '• Hypermutated Ig heavy chain • Chromosome 13q deletion.'",
)

add(
    S3,
    144,
    "oddoneout",
    "All of the following are listed in the 'Bad' column of the CLL Prognostic Factors table on page 144 EXCEPT:",
    "Hypermutated Ig heavy chain",
    [
        "Unmutated Ig heavy chain",
        "All other chromosome deletions (11q del, 17p del, trisomy 12)",
        "β2 microglobulin, ↑ LDH levels, and Zap-70",
    ],
    "In the Prognostic factors table on page 144, 'Bad' includes: '• Unmutated Ig heavy chain • All other chromosome deletion (11q del, 17p del, trisomy 12) • β2 microglobulin • ↑ LDH levels • Zap-70', whereas 'Hypermutated Ig heavy chain' is in the 'Good' column.",
)

add(
    S3,
    144,
    "recall",
    "Which three chromosomal abnormalities are specifically named in parentheses under 'Bad' prognosis in CLL on page 144?",
    "11q deletion, 17p deletion, and trisomy 12",
    [
        "13q deletion, 5q deletion, and 20q deletion",
        "t(15 ; 17), t(8 ; 21), and inv(16)",
        "t(12 ; 21), hyperdiploidy, and 11q23",
    ],
    "Bullet 2 of the 'Bad' column on page 144 states: '• All other chromosome deletion (11q del, 17p del, trisomy 12).'",
)

add(
    S3,
    144,
    "management",
    "Under 'Treatment :' of CLL on page 144, what are the exact constituent drugs and clinical status of the FCR regimen versus the BR regimen?",
    "FCR regimen (Fludarabine + Cyclophosphamide + Rituximab) is treatment of choice (TOC) if fit; BR regimen (Bendamustine + Rituximab) is more commonly used",
    [
        "FCR regimen (Folinic acid + Cytarabine + Rituximab) is palliative only; BR regimen (Bleomycin + Rituximab) is treatment of choice if fit",
        "FCR regimen (Fludarabine + Cladribine + Rituximab) is used only in relapse; BR regimen (Bortezomib + Rituximab) is used in Stage 0",
        "FCR regimen (Fludarabine + Cyclophosphamide + Ruxolitinib) is used for AIHA only; BR regimen (Busulfan + Rituximab) is obsolete",
    ],
    "Under 'Treatment :' on page 144: '• FCR regimen (If fit) : TOC — Fludarabine, Cyclophosphamide, Rituximab. • BR regimen : More commonly used — Bendamustine, Rituximab.'",
)

add(
    S3,
    144,
    "recall",
    "Under 'Hairy Cell Leukemia' on page 144, how is the disease characterized by frequency/grade, cell of origin, age group, and sex ratio?",
    "Rare low-grade B-cell neoplasm; arises from memory B cell; age group >60 years (Male > Female)",
    [
        "Common high-grade T-cell neoplasm; arises from thymic pre-T lymphoblast; age group <20 years (Male > Female)",
        "Indolent naive B-cell neoplasm; arises from bone marrow pro-B cell; median age 13 years (Female > Male)",
        "Aggressive germinal-centre neoplasm; arises from dark-zone centroblast; age group 20–30 years (Female > Male)",
    ],
    "Under 'Hairy Cell Leukemia' on page 144: 'Rare low grade B cell neoplasm. Arise from memory B cell. Age group : >60 years (Male > Female).'",
)

add(
    S3,
    144,
    "fillup",
    "In the 'Pathogenesis' flowchart of Hairy Cell Leukemia on page 144, a memory B cell acquires a ______ mutation to become a hairy cell.",
    "BRAF",
    [
        "JAK2",
        "MYD88",
        "NOTCH-1",
    ],
    "Under 'Pathogenesis :' on page 144: 'Memory B cell ——[BRAF mutation]——> Hairy cell.'",
)

add(
    S3,
    144,
    "recall",
    "In the 'Pathogenesis' diagram of Hairy Cell Leukemia at the bottom of page 144, what effects occur in the Spleen and Bone marrow?",
    "Spleen develops massive splenomegaly; Bone marrow develops pancytopenia (specifically neutropenia and monocytopenia) plus fibrosis",
    [
        "Spleen undergoes splenic atrophy with Howell-Jolly bodies; Bone marrow shows erythroid hyperplasia without fibrosis",
        "Spleen remains normal in size; Bone marrow shows isolated thrombocytosis and hypersegmented megakaryocytes",
        "Spleen develops solitary calcified granulomas; Bone marrow shows pure red cell aplasia with normal neutrophils and monocytes",
    ],
    "In the Pathogenesis diagram on page 144, Hairy cell branches into: 'Spleen : Massive splenomegaly' and 'Bone marrow : • Pancytopenia (Neutropenia, monocytopenia) • Fibrosis.'",
)

add(
    S3,
    144,
    "oddoneout",
    "Because of neutropenia, monocytopenia, and marrow fibrosis, Hairy Cell Leukemia patients on page 144 are specifically listed as prone to all of the following opportunistic infections EXCEPT:",
    "Pneumocystis jirovecii pneumonia (PCP)",
    [
        "Aspergillosis",
        "MAC (Mycobacterium avium complex)",
        "M. kansasii (printed M. kansasi)",
    ],
    "At the bottom of page 144, under Bone marrow → 'Prone to :', the three listed infections are: '• Aspergillosis • MAC • M. kansasi.'",
)


# ==============================================================================
# UNIT 4 — Page 145: Hairy Cell Leukemia Investigations, Treatment & PAN Note
# ==============================================================================

add(
    S4,
    145,
    "recall",
    "Under 'Investigations → Peripheral smear' on page 145, which five cytological features describe the Hairy cell?",
    "Mononuclear, bilobed eccentric nuclei, hairy projections, low N:C ratio, and abundant cytoplasm",
    [
        "Small round nucleus, clumped soccer-ball chromatin, no cytoplasmic projections, high N:C ratio, and scanty cytoplasm",
        "Multilobed hypersegmented nucleus, azurophilic granules, bundles of Auer rods, high N:C ratio, and basophilic cytoplasm",
        "Clefted 'coffee-bean' central nucleus, prominent owl-eye eosinophilic nucleoli, high N:C ratio, and scanty pale cytoplasm",
    ],
    "At the top of page 145 (next to the 'Hairy cell' smear image): '• Peripheral smear : – Hairy cell : mononuclear, bilobed eccentric nuclei, hairy projections, low N : C ratio, abundant cytoplasm.'",
)

add(
    S4,
    145,
    "fillup",
    "On bone marrow biopsy in Hairy Cell Leukemia on page 145, hairy cells and fibrosis are accompanied by the classic ______ appearance (also termed honeycomb appearance).",
    "Fried egg",
    [
        "Starry sky",
        "Owl eye",
        "Clock face",
    ],
    "Under 'Bone marrow biopsy :' (and matching the photomicrograph caption 'Fried egg appearance in bone marrow') on page 145: '– Hairy cells. – Fibrosis. – Fried egg appearance/honey comb appearance.'",
)

add(
    S4,
    145,
    "recall",
    "Under 'Immunophenotyping :' of Hairy Cell Leukemia on page 145, which four specific surface hairy-cell CD markers accompany pan-B markers CD19, CD20, and CD22?",
    "CD11c, CD25, CD103, and CD123 : Positive",
    [
        "CD5, CD10, CD21, and CD23 : Positive",
        "CD15, CD30, CD34, and CD117 : Positive",
        "CD3, CD4, CD8, and CD56 : Positive",
    ],
    "Under 'Immunophenotyping :' on page 145: '– CD19, CD20, CD22, CD11c, CD25, CD103, CD123 : Positive.'",
)

add(
    S4,
    145,
    "recall",
    "Alongside surface CD markers on page 145, which protein and cytochemical enzyme stain are POSITIVE in Hairy Cell Leukemia?",
    "Annexin : Positive and TRAP (Tartarate resistant acid phosphatase) : Positive",
    [
        "Myeloperoxidase (MPO) : Positive and Sudan black B : Positive",
        "Cyclin D1 : Positive and Terminal deoxynucleotidyl transferase (TdT) : Positive",
        "SOX-11 : Positive and Leukocyte alkaline phosphatase (LAP) : Positive",
    ],
    "Sub-bullets 2–3 under 'Immunophenotyping :' on page 145 list: '– Annexin : Positive. – TRAP (Tartarate resistant acid phosphatase) : Positive.'",
)

add(
    S4,
    145,
    "recall",
    "Which two specific B-cell markers are explicitly printed as NEGATIVE under 'Immunophenotyping :' of Hairy Cell Leukemia on page 145?",
    "CD₁₀ and CD₂₁ : Negative",
    [
        "CD₁₉ and CD₂₀ : Negative",
        "CD₁₁c and CD₁₀₃ : Negative",
        "Annexin and TRAP : Negative",
    ],
    "The fourth sub-bullet under 'Immunophenotyping :' on page 145 prints specifically: '– CD₁₀, CD₂₁ : Negative.'",
)

add(
    S4,
    145,
    "match",
    "Under 'Treatment :' of Hairy Cell Leukemia on page 145, match each agent with its exact therapeutic role — 1) Cladribine 2) Pentostatin 3) Vemurafenib 4) Rituximab … A) Second-choice purine nucleoside analogue after Cladribine B) Oral BRAF inhibitor — mostly used in relapse C) Anti-CD20 monoclonal antibody — used for maintenance D) Purine nucleoside analogue — treatment of choice (TOC) / drug of choice (DOC)",
    "1-D, 2-A, 3-B, 4-C",
    [
        "1-A, 2-D, 3-C, 4-B",
        "1-B, 2-A, 3-D, 4-C",
        "1-D, 2-C, 3-B, 4-A",
    ],
    "Under 'Treatment :' on page 145: '• Purine nucleoside analogue (TOC) : Cladribine (DOC) > Pentostatin. • BRAF inhibitor : Vemurafenib (mostly used in relapse). • Rituximab : For maintenence.'",
)

add(
    S4,
    145,
    "scenario",
    "A 66-year-old man presents with massive splenomegaly, fever, neutropenia, monocytopenia, pulmonary MAC infection, and livedo reticularis with mononeuritis multiplex and renal microaneurysms. Bone marrow biopsy confirms hairy cell leukemia with Annexin+, TRAP+, CD103+ cells. Which systemic vasculitis does the 'Note' at the bottom of page 145 associate with hairy cell leukemia and Hepatitis B?",
    "Polyarteritis nodosa (PAN)",
    [
        "Eosinophilic granulomatosis with polyangiitis (EGPA)",
        "Giant cell (temporal) arteritis",
        "Microscopic polyangiitis (MPA)",
    ],
    "The Note at the bottom of page 145 reads: 'Note : Polyarteritis nodosa : Association with hairy cell leukemia & hepatitis B.'",
)

add(
    S4,
    145,
    "truefalse",
    "Which statement regarding Hairy Cell Leukemia on page 145 is TRUE?",
    "True — Purine nucleoside analogue Cladribine is the drug of choice (> Pentostatin), Vemurafenib is mostly used in relapse, and Rituximab is used for maintenance",
    [
        "True — Hairy cells display a high nuclear-to-cytoplasmic (N:C) ratio, scanty agranular cytoplasm, and strong positivity for CD10 and CD21",
        "False — Hairy cells test positive for TRAP (tartrate-resistant acid phosphatase), Annexin, CD11c, CD25, CD103, and CD123",
        "False — Polyarteritis nodosa is specifically associated with both hairy cell leukemia and hepatitis B virus infection",
    ],
    "All four lines on page 145 confirm: low N:C ratio with abundant cytoplasm, CD10 & CD21 Negative, CD19/CD20/CD22/CD11c/CD25/CD103/CD123 + Annexin + TRAP Positive, Cladribine (DOC) > Pentostatin with Vemurafenib in relapse and Rituximab for maintenance, and PAN associated with hairy cell leukemia & hepatitis B.",
)


GUIDES = {
    S1: (
        "CLL Overview, Epidemiology, Defective Apoptosis Pathophysiology, Small Lymphocytic Leukemia (SLL) & Etiology",
        "Overview: CLL is the most common lymphoid leukemia (AML = m/c myeloid leukemia), Males > Females, low-grade; 80–85% asymptomatic/indolent, median age 72 yrs, median survival 10 yrs, 1–2% spontaneous regression.\n"
        "Pathophysiology: Defective apoptosis of naive B-cells (CD19, CD20, CD21, CD22, CD79a, CD79b, S.IgM) → clonal expansion + acquire CD5, CD23 → monoclonal B-cell lymphocytosis → CLL if lymphocytes >5000 cells/µL.\n"
        "SLL & Etiology: SLL arises from memory B cell with identical immunophenotype/features and painless lymphadenopathy ± splenomegaly; CLL has strong familial inheritance and no risk with radiation.",
    ),
    S2: (
        "CLL Investigations, Smudge Cells, Richter Transformation, Warm AIHA, Staging Table & Indications for Treatment",
        "Investigations: Unexplained lymphocytosis (~60,000–70,000; rarely normocytic normochromic anemia, thrombocytopenia); smear shows small blue round CLL lymphocytes (pale cytoplasm, no granules, moderate chromatin condensation) + Smudge cells; LN biopsy shows diffuse effacement (SLL).\n"
        "High-risk indicators: (1) Richter transformation — low-grade (classically SLL) → high-grade (classically DLBCL) with ↑ lymphadenopathy & B symptoms (>10% weight loss in 6 mo, fever >100.4°F, ↑↑ LDH, ↑ PET nodal uptake); (2) Warm antibody AIHA (DAT/Coomb's test).\n"
        "Staging & Rx indications: Stages 0 (lymphocytosis) & 1 (+ lymphadenopathy) = no treatment; Stages 2 (HSM), 3 (anemia), 4 (pancytopenia, as printed) = treatment required. Rx indications: Richter features, steroid-refractory AIHA, Stages 2–4 (massive splenomegaly, marrow failure).",
    ),
    S3: (
        "CLL Prognostic Factors Table, FCR & BR Treatment Regimens, and Hairy Cell Leukemia Overview & Pathogenesis",
        "CLL prognosis & Rx: Good = hypermutated Ig heavy chain, chr 13q del; Bad = unmutated Ig heavy chain, other deletions (11q del, 17p del, trisomy 12), β2-microglobulin, ↑ LDH, Zap-70. Regimens: FCR (Fludarabine + Cyclophosphamide + Rituximab, TOC if fit); BR (Bendamustine + Rituximab, more commonly used).\n"
        "Hairy Cell Leukemia: Rare low-grade B-cell neoplasm arising from memory B cell, >60 yrs (M > F). Pathogenesis: Memory B cell + BRAF mutation → Hairy cell → Spleen (massive splenomegaly) & Bone marrow (pancytopenia with neutropenia + monocytopenia, fibrosis → Aspergillosis, MAC, M. kansasii).",
    ),
    S4: (
        "Hairy Cell Leukemia Investigations (Smear, Fried-Egg Marrow, Immunophenotype), Treatment & PAN Association",
        "Investigations: Smear shows mononuclear hairy cells (bilobed eccentric nuclei, hairy projections, low N:C ratio, abundant cytoplasm); marrow biopsy shows hairy cells, fibrosis & fried-egg / honeycomb appearance.\n"
        "Immunophenotyping: Positive = CD19, CD20, CD22, CD11c, CD25, CD103, CD123, Annexin, TRAP (tartrate-resistant acid phosphatase); Negative = CD10, CD21.\n"
        "Treatment & association: Purine nucleoside analogue (TOC) = Cladribine (DOC) > Pentostatin; BRAF inhibitor Vemurafenib (relapse); Rituximab (maintenance). Note: Polyarteritis nodosa is associated with hairy cell leukemia & hepatitis B.",
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
