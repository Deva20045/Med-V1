#!/usr/bin/env python3
"""Generate Chapter 26: Non-Hodgkin's Lymphoma (Book p146–152).

Every question is anchored to a specific line, table cell, note box, flowchart
arm, Venn diagram label, or histology caption in uploads/02.pdf (PDF pages
29–35 = Book pages 146–152) in strict book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 26
TITLE = "Non-Hodgkin's Lymphoma"
PAGES = "146-152"

S1 = "Classification by Cell of Origin, Mature T-Cell Lymphomas (ALCL to Hepatosplenic) & Grade-Based Classification"
S2 = "Causative Organisms Table (EBV 100/70/40/20 Rule, HIV, HCV, H. pylori, HHV-8, HTLV-1) & Ann-Arbor Staging"
S3 = "NHL General Features, Mantle Cell Lymphoma (t(11;14), SOX-11, R-CHOP Resistance) & Follicular Lymphoma Genetics"
S4 = "Follicular Lymphoma Histology/Course/Rx, Germinal Centre Malignancies Table & MALToma (t(11;18), H. pylori, Sjögren)"
S5 = "High-Grade Lymphomas Overview, Clinical Features & Prognostic Factors, and Diffuse Large B-Cell Lymphoma (DLBCL)"
S6 = "DLBCL Subtypes (GCB vs ABC-DLBCL), Double/Triple-Hit vs Double-Expressor Venn Diagram & R-CHOP Regimen"
S7 = "DLBCL Interim-PET Flowchart & Burkitt's Lymphoma (c-myc Translocations, Endemic vs Sporadic, CODOX-M/IVAC, Starry Sky)"

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
# UNIT 1 — Page 146: Cell of Origin, Mature T-Cell Lymphomas & Grade Classification
# ==============================================================================

add(
    S1,
    146,
    "recall",
    "In the T-cell rows of the 'BASED ON CELL OF ORIGIN' table at the top of page 146, what neoplasms arise from Precursor T-cell versus Mature T-cell?",
    "Precursor T-cell → Precursor T-cell leukemia/lymphoma; Mature T-cell → Mature T-cell lymphoma",
    [
        "Precursor T-cell → ALL without nodal mass only; Mature T-cell → Burkitt's lymphoma",
        "Precursor T-cell → Mantle cell lymphoma; Mature T-cell → Marginal zone lymphoma",
        "Precursor T-cell → Multiple myeloma; Mature T-cell → Follicular lymphoma",
    ],
    "Rows 1–2 of the 'BASED ON CELL OF ORIGIN' table on page 146 list: T-cell → Precursor T-cell → Precursor T-cell leukemia/lymphoma; Mature T-cell → Mature T-cell lymphoma.",
)

add(
    S1,
    146,
    "match",
    "In the B-cell rows of the 'BASED ON CELL OF ORIGIN' table on page 146, match each B-cell developmental stage with its corresponding tumor — 1) Pre-germinal centre 2) Centroblasts 3) Centrocytes 4) Plasmablast … A) Follicular lymphoma B) Activated B-cell diffuse B-cell lymphoma (ABC-DLBCL) C) Mantle cell lymphoma (MCL) D) Diffuse large B-cell lymphoma (DLBCL) & Burkitt's lymphoma",
    "1-C, 2-D, 3-A, 4-B",
    [
        "1-A, 2-C, 3-D, 4-B",
        "1-C, 2-A, 3-D, 4-B",
        "1-D, 2-B, 3-A, 4-C",
    ],
    "In the B-cell rows on page 146: Precursor B-cell → ALL; Pre-germinal centre → Mantle cell lymphoma (MCL); Centroblasts → DLBCL & Burkitt's lymphoma; Centrocytes → Follicular lymphoma; Post-germinal centre → Marginal zone lymphoma (MZL); Plasmablast → Activated B-cell diffuse B-cell lymphoma (ABC-DLBCL).",
)

add(
    S1,
    146,
    "recall",
    "In the B-cell origin table on page 146, what neoplasms arise specifically from 'Precursor B-cell' and 'Post-germinal centre'?",
    "Precursor B-cell → ALL; Post-germinal centre → Marginal zone lymphoma (MZL)",
    [
        "Precursor B-cell → Follicular lymphoma; Post-germinal centre → Burkitt's lymphoma",
        "Precursor B-cell → Mantle cell lymphoma; Post-germinal centre → Precursor T-ALL",
        "Precursor B-cell → ABC-DLBCL; Post-germinal centre → Centroblastic DLBCL",
    ],
    "Rows 3 & 7 of the B-cell origin table on page 146 map 'Precursor B-cell → ALL' and 'Post-germinal centre → Marginal zone lymphoma (MZL)'.",
)

add(
    S1,
    146,
    "recall",
    "Under 'Mature T-cell lymphomas → 1. Anaplastic large cell lymphoma :' on page 146, which four specific markers, cytogenetics, surgical association, and diagnostic cells are listed?",
    "ALK (CD30) +, t(2 ; 5), breast implants, and hallmark cells",
    [
        "Cyclin D1 +, t(11 ; 14), celiac sprue enteropathy, and smudge cells",
        "BCL-2 +, t(14 ; 18), H. pylori non-atrophic gastritis, and tingible-body macrophages",
        "CD103 +, BRAF V600E mutation, salivary gland Sjögren syndrome, and fried-egg cells",
    ],
    "Under 'Mature T-cell lymphomas : 1. Anaplastic large cell lymphoma :' on page 146: '– ALK (CD30) +. – t(2 ; 5). – Breast implants. – Hallmark cells.'",
)

add(
    S1,
    146,
    "match",
    "Under 'Mature T-cell lymphomas :' on page 146, match items 3, 4, 5, and 6 with their characteristic clinicopathologic association — 1) Enteropathy-associated T-cell lymphoma 2) Mycosis fungoides / Sezary syndrome 3) Extranodal NK T-lymphoma 4) Adult T-cell leukemia/lymphoma … A) EBV +ve B) HTLV-1 associated C) Celiac disease D) Cutaneous T-cell lymphoma",
    "1-C, 2-D, 3-A, 4-B",
    [
        "1-D, 2-C, 3-B, 4-A",
        "1-C, 2-A, 3-D, 4-B",
        "1-B, 2-D, 3-A, 4-C",
    ],
    "Items 3–6 under 'Mature T-cell lymphomas :' on page 146 list: 3. Enteropathy (Celiac) associated T-cell lymphoma; 4. Mycosis fungoides (Cutaneous T-cell lymphoma)/Sezary syndrome; 5. Extranodal NK T-lymphoma (EBV +ve); 6. HTLV-1 associated adult T-cell leukemia/lymphoma.",
)

add(
    S1,
    146,
    "oddoneout",
    "All of the following entities are listed among the seven 'Mature T-cell lymphomas :' on page 146 EXCEPT:",
    "Splenic marginal zone lymphoma",
    [
        "Angioimmunoblastic lymphoma",
        "Enteropathy (Celiac) associated T-cell lymphoma",
        "Hepatosplenic T-cell lymphoma",
    ],
    "Items 2, 3, and 7 under 'Mature T-cell lymphomas :' on page 146 are Angioimmunoblastic lymphoma, Enteropathy (Celiac) associated T-cell lymphoma, and Hepatosplenic T-cell lymphoma; Splenic MZL is a B-cell lymphoma.",
)

add(
    S1,
    146,
    "fillup",
    "In the boxed 'Note :' on page 146, B-cell lymphoma has a better prognosis than T-cell lymphoma ('B-cell lymphoma > T-cell lymphoma'), and the most common NHL overall is ______.",
    "DLBCL",
    [
        "Follicular lymphoma",
        "Mantle cell lymphoma",
        "Burkitt's lymphoma",
    ],
    "The boxed 'Note :' on page 146 reads: '• Prognosis : B-cell lymphoma > T-cell lymphoma. • m/c NHL : DLBCL.'",
)

add(
    S1,
    146,
    "recall",
    "In the 'BASED ON GRADE' flowchart at the bottom of page 146, which lymphomas fall under 'Low grade', 'Intermediate to high grade', and 'High grade'?",
    "Low grade: Small lymphocytic leukemia (SLL), MZL, Follicular lymphoma; Intermediate to high grade: MCL; High grade: DLBCL, Burkitt's lymphoma",
    [
        "Low grade: DLBCL, Burkitt's lymphoma; Intermediate to high grade: Follicular lymphoma; High grade: SLL, MZL, MCL",
        "Low grade: MCL, Burkitt's lymphoma; Intermediate to high grade: SLL, MZL; High grade: Follicular lymphoma",
        "Low grade: Follicular lymphoma only; Intermediate to high grade: DLBCL, Burkitt's lymphoma; High grade: SLL, MZL",
    ],
    "At the bottom of page 146 under 'BASED ON GRADE': Low grade → Small lymphocytic leukemia (SLL), MZL, Follicular lymphoma; Intermediate to high grade → MCL; High grade → DLBCL, Burkitt's lymphoma.",
)


# ==============================================================================
# UNIT 2 — Page 147: Causative Organisms & Ann-Arbor Staging of Lymphomas
# ==============================================================================

add(
    S2,
    147,
    "numeric",
    "In the 'BASED ON CAUSATIVE ORGANISM' table on page 147, how does the '100/70/40/20 rule for EBV involvement' apply across the four classical Hodgkin's disease subtypes?",
    "LD (Lymphocyte depleted) → 100%, MC (Mixed cellularity) → 70%, NS (Nodular sclerosis) → 40%, LR (Lymphocyte rich) → 20%",
    [
        "NS (Nodular sclerosis) → 100%, LR (Lymphocyte rich) → 70%, MC (Mixed cellularity) → 40%, LD (Lymphocyte depleted) → 20%",
        "MC (Mixed cellularity) → 100%, NS (Nodular sclerosis) → 70%, LD (Lymphocyte depleted) → 40%, LR (Lymphocyte rich) → 20%",
        "LR (Lymphocyte rich) → 100%, LD (Lymphocyte depleted) → 70%, NS (Nodular sclerosis) → 40%, MC (Mixed cellularity) → 20%",
    ],
    "In row 1 (EBV) of the table on page 147: 'Hodgkin's disease : 100/70/40/20 rule for EBV involvement → EBV ⊕ cases in: LD → 100%, MC → 70%, NS → 40%, LR → 20%.'",
)

add(
    S2,
    147,
    "recall",
    "In the EBV row of the 'BASED ON CAUSATIVE ORGANISM' table on page 147, which B-cell and T-cell Non-Hodgkin's lymphomas are linked to EBV, and which morphology joins two of the B-cell entities?",
    "B-cell type: Burkitt's lymphoma, plus Post organ transplant lymphoma and Primary CNS lymphoma (both share DLBCL morphology); T-cell type: Extranodal NK/T-lymphoma",
    [
        "B-cell type: Follicular lymphoma and Splenic MZL (centrocytic morphology); T-cell type: Enteropathy-associated T-cell lymphoma",
        "B-cell type: Gastric MALToma and Mantle cell lymphoma (starry-sky morphology); T-cell type: Sezary syndrome",
        "B-cell type: Hairy cell leukemia and Waldenström macroglobulinemia; T-cell type: Hepatosplenic T-cell lymphoma",
    ],
    "Under EBV → NHL on page 147: 'B cell type : – Burkitt's lymphoma; [– Post organ transplant lymphoma – Primary CNS lymphoma] → DLBCL morphology; T cell type : Extranodal NK/T-lymphoma.'",
)

add(
    S2,
    147,
    "match",
    "In the 'BASED ON CAUSATIVE ORGANISM' table on page 147, match each infectious agent with its associated lymphoma(s) — 1) HIV 2) HCV 3) H. pylori 4) HHV-8 … A) Primary effusion lymphoma & Castleman's disease B) DLBCL & Burkitt's lymphoma C) Waldenstrom's macroglobulinemia & Splenic MZL D) MALTOMA (Extranodal MZL)",
    "1-B, 2-C, 3-D, 4-A",
    [
        "1-A, 2-C, 3-D, 4-B",
        "1-B, 2-D, 3-C, 4-A",
        "1-C, 2-B, 3-A, 4-D",
    ],
    "Rows 2–5 of the causative organism table on page 147 list: HIV → DLBCL, Burkitt's lymphoma; HCV → Waldenstrom's macroglobulinemia, Splenic MZL; H.pylori → MALTOMA (Extranodal MZL); HHV-8 → Primary effusion lymphoma, Castleman's disease.",
)

add(
    S2,
    147,
    "fillup",
    "In the final row of the causative organism table on page 147, infection with ______ causes Adult T-cell leukemia/lymphoma.",
    "HTLV₁",
    [
        "HHV-8",
        "Parvovirus B19",
        "Hepatitis B virus",
    ],
    "Row 6 of the causative organism table on page 147 maps 'HTLV₁' to '• Adult T-cell leukemia/lymphoma.'",
)

add(
    S2,
    147,
    "match",
    "Under 'Ann-Arbor staging of lymphomas :' on page 147, match each stage with its exact anatomical extent — 1) Stage I 2) Stage II 3) Stage III 4) Stage IV … A) Node regions both sides of diaphragm B) Diffuse extralymphatic involvement (Lung, Liver, Bone) C) Single lymph node region D) 2 or more node regions, same side of diaphragm",
    "1-C, 2-D, 3-A, 4-B",
    [
        "1-C, 2-A, 3-D, 4-B",
        "1-D, 2-C, 3-B, 4-A",
        "1-B, 2-D, 3-A, 4-C",
    ],
    "Under 'Ann-Arbor staging of lymphomas :' on page 147: Stage I = Single lymph node region; Stage II = 2 or more node regions, same side of diaphragm; Stage III = Node regions both sides of diaphragm; Stage IV = Diffuse extralymphatic involvement (diagram labels: Lung, Liver, Bone).",
)

add(
    S2,
    147,
    "recall",
    "At the bottom of page 147, which four clinical/laboratory factors classify Early disease (Ann-Arbor Stages I–II) as 'Unfavourable', and how is Late/advanced disease (Stages III–IV) classified?",
    "Early Unfavourable criteria: Age ≥ 60, ↑ LDH, >1 extranodal site, and poor performance status; Late/advanced disease (Stages III–IV) is Unfavourable by default",
    [
        "Early Unfavourable criteria: Age < 20, ↓ LDH, single nodal region, and normal performance status; Stages III–IV are Favourable by default",
        "Early disease (Stages I–II) is always Favourable regardless of age or LDH; only Stage IV with bone marrow involvement is Unfavourable",
        "Early Unfavourable criteria: splenomegaly alone; Stages III–IV require all four risk factors to be considered Unfavourable",
    ],
    "At the bottom of page 147, Stage I + II = 'Early disease', splitting into 'Favourable' vs 'Unfavourable (• Age ≥ 60. • ↑ LDH. • >1 extranodal site. • Poor performance status.)'; Stage III + IV = 'Late/advanced disease → Unfavourable by default.'",
)

add(
    S2,
    147,
    "truefalse",
    "Which statement accurately reflects the causative organisms and Ann-Arbor staging diagrams on page 147?",
    "True — Hepatitis C virus (HCV) is associated with Waldenstrom's macroglobulinemia and Splenic MZL, while HHV-8 causes Primary effusion lymphoma and Castleman's disease",
    [
        "True — Ann-Arbor Stage III indicates diffuse extralymphatic involvement of the lung, liver, and bone",
        "False — In the 100/70/40/20 rule for Hodgkin EBV involvement, Lymphocyte Depleted (LD) has 100% and Mixed Cellularity (MC) has 70% EBV positivity",
        "False — Both Post-organ transplant lymphoma and Primary CNS lymphoma linked to EBV exhibit DLBCL morphology",
    ],
    "All four facts come directly from page 147: HCV → Waldenstrom's macroglobulinemia & Splenic MZL; HHV-8 → Primary effusion lymphoma & Castleman's disease; Stage IV = diffuse extralymphatic involvement (Lung, Liver, Bone); LD 100% / MC 70%; Post-transplant & Primary CNS lymphoma show DLBCL morphology.",
)


# ==============================================================================
# UNIT 3 — Page 148: General Features, Mantle Cell Lymphoma & Follicular Lymphoma Genetics
# ==============================================================================

add(
    S3,
    148,
    "recall",
    "Under 'General features :' of Non-Hodgkin's Lymphoma at the top of page 148, what age of presentation, sex ratio, most common presenting feature, and most common involved nodal site are printed?",
    "Age of presentation: 60 years; M > F; most common presenting feature: asymptomatic painless lymphadenopathy; most common involved site: supraclavicular nodes",
    [
        "Age of presentation: 20 years; F > M; most common presenting feature: alcohol-induced painful lymphadenopathy; most common involved site: inguinal nodes",
        "Age of presentation: 13 years; M = F; most common presenting feature: drenching B symptoms; most common involved site: anterior mediastinum",
        "Age of presentation: 72 years; F > M; most common presenting feature: bone tenderness and limping; most common involved site: epitrochlear nodes alone",
    ],
    "Under 'General features :' on page 148: '• Age of presentation : 60 years. • M > F. • m/c presenting feature : Asymptomatic painless lymphadenopathy. • m/c involved site : Supraclavicular nodes.'",
)

add(
    S3,
    148,
    "numeric",
    "Under 'General features :' of NHL on page 148, which three extranodal sites are listed (including bone marrow involvement percentage), and how common are B-symptoms and CNS involvement?",
    "Extranodal sites: most common GIT, Waldeyer's ring, and bone marrow (30–40% cases); both B-symptoms and CNS involvement are very rare",
    [
        "Extranodal sites: CNS meninges (80% cases), orbit, and testes; B-symptoms occur in >90% of all cases at onset",
        "Extranodal sites: kidneys and myocardium only, with <5% bone marrow involvement; CNS involvement occurs in 75%",
        "Extranodal sites: skin exclusively, sparing GIT and Waldeyer's ring; high spiking fevers are universal at presentation",
    ],
    "Bullets 5–7 under 'General features :' on page 148 list: '• Extranodal sites involved : – m/c GIT. – Waldeyer's ring. – Bone marrow (30–40% cases). • B-symptoms : Very rare. • CNS involvement : Very rare.'",
)

add(
    S3,
    148,
    "recall",
    "Under 'Mantle cell lymphoma :' on page 148, what cell zone of origin and positive (+) versus negative (–) genetics/immunophenotype profile are shown?",
    "Origin: Pre-germinal centre; Positive (+): CD5, Cyclin D1, SOX-11, and t(11 ; 14); Negative (–): CD10 and CD23",
    [
        "Origin: Germinal centre centrocyte; Positive (+): CD10, CD23, BCL-6, and t(14 ; 18); Negative (–): CD5 and Cyclin D1",
        "Origin: Post-germinal marginal zone; Positive (+): CD103, Annexin, and BRAF V600E; Negative (–): CD5 and Cyclin D1",
        "Origin: Precursor thymocyte; Positive (+): CD30, ALK, and t(2 ; 5); Negative (–): CD19 and CD20",
    ],
    "Under 'Mantle cell lymphoma :' on page 148: 'Origin : Pre-germinal centre. Genetics : [• CD5 • Cyclin D1 • SOX-11 • t (11 ; 14)] (+) ; [• CD10 • CD23] (–).'",
)

add(
    S3,
    148,
    "fillup",
    "Under 'Aggressive :' features of Mantle Cell Lymphoma on page 148, extranodal gastrointestinal tract involvement produces ______ in the GIT (alongside bone marrow, blood, and spleen involvement).",
    "Lymphomatoid polyposis",
    [
        "Pseudomembranous colitis",
        "Cobblestone skip ulceration",
        "Atrophic fundic gastritis",
    ],
    "On the right side of the Mantle cell lymphoma section on page 148 under 'Aggressive :': '• Involves → Extranodal (Lymphomatoid polyposis in GIT), Bone marrow, Blood, Spleen.'",
)

add(
    S3,
    148,
    "management",
    "How does page 148 describe Mantle Cell Lymphoma's response to standard R-CHOP chemotherapy?",
    "Unresponsive to standard therapy (R-CHOP)",
    [
        "Cured in >90% of patients by just 2 cycles of standard R-CHOP",
        "Responds completely to oral H. pylori eradication without chemotherapy",
        "Requires watch-and-wait observation only because all cases regress spontaneously",
    ],
    "Under 'Aggressive :' on page 148, the second bullet reads: '• Unresponsive to standard therapy (R-CHOP).'",
)

add(
    S3,
    148,
    "recall",
    "Which two subtypes of Mantle Cell Lymphoma are distinguished by SOX-11 status on page 148, and what is printed directly under 'Good prognostic factors :'?",
    "1. Classical: SOX-11 positive; 2. Leukemic non-nodal: SOX-11 negative; 'Good prognostic factors : SOX-11 upregulation' (as printed on p148)",
    [
        "1. Endemic: EBV positive; 2. Sporadic: EBV negative; 'Good prognostic factors : High LDH and t(8;14)'",
        "1. Germinal centre: MUM-1 positive; 2. Activated B-cell: CD10 positive; 'Good prognostic factors : Double-hit rearrangement'",
        "1. Hypergranular: faggot positive; 2. Hypogranular: faggot negative; 'Good prognostic factors : 17p deletion'",
    ],
    "Below the Mantle cell photomicrograph on page 148: 'Types : 1. Classical : SOX-11 positive. 2. Leukemic non-nodal : SOX-11 negative.' And to its right: 'Good prognostic factors : SOX-11 upregulation' [preserved as printed; documented in known-source-caveats.md].",
)

add(
    S3,
    148,
    "recall",
    "Under 'Follicular lymphoma : Genetics' at the bottom of page 148, which markers apply to ALL germinal-centre malignancies, and what specific translocation and chromosomal partners define Follicular Lymphoma?",
    "CD10(+), CD23(+) and BCL-6 dysregulation mark all germinal-centre malignancies; Follicular lymphoma shows aberrant BCL-2 expression via t(14;18) — Chromosome 14: Immunoglobulin G heavy chain (as printed) and Chromosome 18: BCL-2",
    [
        "CD5(+) and Cyclin D1 overexpression mark all germinal-centre malignancies; Follicular lymphoma arises from t(11;14) involving BCL-1 on chromosome 11",
        "CD30(+) and ALK fusion mark all germinal-centre malignancies; Follicular lymphoma arises from t(2;5) involving NPM1 and ALK",
        "c-myc dysregulation on chromosome 8 marks all germinal-centre malignancies; Follicular lymphoma arises from t(8;14) with 100% Ki67 proliferation index",
    ],
    "At the bottom of page 148 under 'Follicular lymphoma : Germinal centre malignancy. Genetics :': '[• CD10(+) CD23(+) • BCL-6 dysregulation] → markers for all germinal centre malignancies; • Aberrant BCL-2 expression; • t (14;18) → Chromosome 14 : Immunoglobulin G heavy chain; Chromosome 18 : BCL-2.'",
)


# ==============================================================================
# UNIT 4 — Page 149: Follicular Histology/Rx, GC Table & MALToma
# ==============================================================================

add(
    S4,
    149,
    "recall",
    "At the top of page 149 under 'Histology :' of Follicular Lymphoma, what architectural pattern and two constituent cell types are listed?",
    "Follicular pattern (paratrabecular lymphoid aggregates) with small cleaved cells and large non-cleaved cells",
    [
        "Diffuse starry-sky sheets composed of tingible-body macrophages and round non-cleaved blasts with cytoplasmic vacuoles",
        "Honeycomb / fried-egg fibrotic pattern composed of mononuclear cells with circumferential hairy projections",
        "Nodular collagenous bands surrounding bilobed owl-eye Reed-Sternberg lacunar cells amidst eosinophils",
    ],
    "At the top of page 149 under 'Histology :': 'Follicular pattern (Paratrabecular lymphoid aggregates) : With → Small cleaved cells / Large non cleaved cells.'",
)

add(
    S4,
    149,
    "management",
    "Under 'Additional points' and 'Treatment' of Follicular Lymphoma on page 149, which clinical course features are common, which cases are treated, and what agent is given for low tumor burden?",
    "B-symptoms are rare while spontaneous remission and relapse are common; treat symptomatic cases only, using Rituximab for low tumor burden",
    [
        "Extensive B-symptoms occur in >90% and spontaneous remission never occurs; treat all asymptomatic Stage I cases urgently with CODOX-M/IVAC",
        "Cured permanently in 80% by H. pylori triple eradication therapy; never relapses once remission is achieved",
        "Immediate allogeneic stem cell transplant is mandatory in every newly diagnosed patient regardless of symptoms or tumor burden",
    ],
    "On page 149 for Follicular lymphoma: Additional points — '• B-symptoms : Rare. [• Spontaneous remission • Relapse] → Common.' Treatment — '• Symptomatic cases only. • Low tumor burden : Rituximab.'",
)

add(
    S4,
    149,
    "numeric",
    "Under 'Complications :' of Follicular Lymphoma on page 149, what annual risk is printed for Richter transformation from low-grade to high-grade lymphoma?",
    "3% risk/year",
    [
        "25% risk/year",
        "10–20% risk/year",
        "80% risk/year",
    ],
    "Under 'Complications :' on page 149: 'Richter transformation (3% risk/year) : Low grade lymphoma —[Transforms]→ High grade lymphoma.'",
)

add(
    S4,
    149,
    "match",
    "In the 'Note :' table of Germinal Centre Malignancies on page 149, match each malignancy item with its exact 'Origin' or 'Feature' entry — 1) Follicular lymphoma — Origin 2) Follicular lymphoma — Feature 3) Burkitt's lymphoma & DLBCL — Origin 4) Burkitt's lymphoma & DLBCL — Feature … A) Centroblast B) Aggressive C) Centrocyte D) Low grade",
    "1-C, 2-D, 3-A, 4-B",
    [
        "1-A, 2-B, 3-C, 4-D",
        "1-C, 2-B, 3-A, 4-D",
        "1-D, 2-C, 3-B, 4-A",
    ],
    "The 'Note :' table on page 149 lists Germinal centre malignancies: 1. Follicular lymphoma → Origin: Centrocyte, Feature: Low grade; 2. Burkitt's lymphoma & 3. DLBCL → Origin: Centroblast, Feature: Aggressive.",
)

add(
    S4,
    149,
    "numeric",
    "Under 'Maltoma :' on page 149, what are its MZL frequency/site status, cell zone of origin, sex predilection reason, and exact percentage associated with H. pylori non-atrophic pan-gastritis?",
    "Most common type of MZL (purely extranodal); Post-germinal centre origin; Females > Males (due to autoimmune association); H. pylori (non-atrophic pan-gastritis) in 95% cases",
    [
        "Rarest nodal MZL; Pre-germinal mantle origin; Males > Females; H. pylori fundic atrophy in 20% cases",
        "Purely leukemic MZL; Dark-zone centroblast origin; Adolescent boys; EBV association in 40% cases",
        "Exclusively splenic MZL; Pro-B origin; Equal sex incidence; HCV association in 95% cases",
    ],
    "Under 'Maltoma :' on page 149: '• m/c type of MZL (Purely extranodal). • Origin : Post-germinal centre. • Females > Males (D/t autoimmune association). Associations : H.pylori (Non atrophic pan-gastritis) in 95% cases.'",
)

add(
    S4,
    149,
    "recall",
    "What genetics/immunophenotype profile and presenting symptoms are listed under 'Maltoma' on page 149?",
    "Genetics: CD5(–), CD10(–), CD23(–) and t(11 ; 18); Clinical features: Upper GI symptoms",
    [
        "Genetics: CD5(+), CD10(+), CD23(+) and t(8 ; 14); Clinical features: Jaw/maxillary swelling",
        "Genetics: CD30(+), ALK(+) and t(2 ; 5); Clinical features: Superior vena cava syndrome",
        "Genetics: BRAF V600E and CD103(+); Clinical features: Massive splenomegaly with dry tap",
    ],
    "Under Maltoma on page 149: 'Genetics : • CD5(–), CD10(–), CD23(–). • t(11 ; 18). Clinical features : Upper GI symptoms.'",
)

add(
    S4,
    149,
    "management",
    "What step-up treatment pathway, printed good prognostic factors, and high-grade complication are listed for MALToma at the bottom of page 149?",
    "Treatment: H. pylori eradication (80% respond) → if no response: R-CHOP trial; Good prognostic factors (as printed): H. pylori +ve and t(11 ; 18); Complication: Richter transformation to DLBCL",
    [
        "Treatment: upfront total gastrectomy in all cases; Good prognostic factors: H. pylori –ve; Complication: Acute promyelocytic leukemia",
        "Treatment: CODOX-M/IVAC first line; Good prognostic factors: high serum LDH; Complication: Myelofibrosis",
        "Treatment: watch-and-wait without antibiotics; Good prognostic factors: 17p deletion; Complication: Burkitt's leukemia",
    ],
    "At the bottom of page 149 under Maltoma: 'Treatment : H. pylori eradication (80% respond) —[No response]→ R-CHOP trial. Good prognostic factors : • H. pylori +ve. • t(11 ; 18) [as printed on p149]. Complications : Richter transformation to DLBCL.'",
)

add(
    S4,
    149,
    "fillup",
    "According to the boxed 'Note :' at the bottom-right of page 149, Marginal Zone Lymphoma (MZL) in Sjögren syndrome characteristically involves the ______.",
    "salivary gland",
    [
        "anterior thymus",
        "gastroesophageal junction",
        "renal cortex",
    ],
    "The boxed Note at the bottom-right of page 149 reads: 'Note : MZL in Sjogren syndrome : Involves salivary gland.'",
)


# ==============================================================================
# UNIT 5 — Page 150: High Grade Lymphomas Overview, Ann-Arbor Note & DLBCL Intro
# ==============================================================================

add(
    S5,
    150,
    "recall",
    "At the top of page 150 under 'HIGH GRADE LYMPHOMAS', which three entities are numbered 1–3, including the exact printed name, translocation, immunophenotype, and cell types under item 3?",
    "1. Diffuse Large B-cell Lymphoma (DLBCL); 2. Burkitt's lymphoma; 3. Anaplastic large B-cell lymphoma [printed slip for ALCL] with t(2 ; 5), CD30+ve, hallmark cells, and flower cells",
    [
        "1. Follicular lymphoma; 2. Small lymphocytic leukemia; 3. Marginal zone MALToma with t(11 ; 18) and CD5/CD10/CD23 negativity",
        "1. Hairy cell leukemia; 2. Waldenström macroglobulinemia; 3. Mantle cell lymphoma with t(11 ; 14) and Cyclin D1 positivity",
        "1. Nodular sclerosis Hodgkin disease; 2. Mixed cellularity Hodgkin disease; 3. Multiple myeloma with CD38 and CD138 positivity",
    ],
    "At the top of page 150 under 'HIGH GRADE LYMPHOMAS': '1. Diffuse Large B-cell Lymphoma (DLBCL). 2. Burkitt's lymphoma. 3. Anaplastic large B-cell lymphoma [printed slip on p150; listed under Mature T-cell lymphomas on p146] : • t(2 ; 5). • CD30+ve. • Hallmark cells, flower cells.'",
)

add(
    S5,
    150,
    "recall",
    "Under 'Features of high grade lymphomas :' on page 150, what nodal presentation, B-symptom profile, extranodal vs BM/CNS line, and two bad prognostic biochemical factors are listed?",
    "Rapidly progressive painless lymphadenopathy causing compression symptoms, extensive B-symptoms, extranodal involvement (e.g., GIT), 'no involvement of bone marrow or CNS' (as printed), and bad prognostic factors: LDH and hypoalbuminemia",
    [
        "Indolent waxing-and-waning lymphadenopathy without mass effect, absence of B-symptoms, isolated splenic white-pulp disease, and bad prognostic factors: hyperalbuminemia and low LDH",
        "Slowly progressive asymptomatic blood lymphocytosis (>60,000/µL) without nodal compression, and bad prognostic factors: isolated hypercalcemia and monoclonal IgM",
        "Alcohol-induced lymph node pain exclusively in young females without GI involvement, and bad prognostic factors: elevated haptoglobin and low ESR",
    ],
    "Under 'Features of high grade lymphomas :' on page 150: '• Rapidly progressive painless lymphadenopathy → Causes compression symptoms. • Extensive B-symptoms. • Extranodal involvement (Eg : GIT). • No involvement of bone marrow or CNS [general bullet printed on p150]. • Bad prognostic factors : – LDH. – Hypoalbuminemia.'",
)

add(
    S5,
    150,
    "fillup",
    "Under 'Features of high grade lymphomas → Bad prognostic factors :' on page 150, elevated serum LDH is paired with ______.",
    "Hypoalbuminemia",
    [
        "Hyperhaptoglobinemia",
        "Hypouricemia",
        "Hyperferritinemia",
    ],
    "Bullet 5 under 'Features of high grade lymphomas :' on page 150 lists: '• Bad prognostic factors : – LDH. – Hypoalbuminemia.'",
)

add(
    S5,
    150,
    "oddoneout",
    "In the boxed 'Note : Ann-Arbor staging' on page 150, all of the following four risk parameters branch directly from '3,4 : Advanced' EXCEPT:",
    "Hyperalbuminemia >4.5 g/dL",
    [
        "Age >60 years",
        ">1 extranodal site",
        "Poor performance status and High LDH",
    ],
    "The boxed Note on page 150 shows: 'Ann-Arbor staging → 1,2 : Early (Favourable / Unfavourable); 3,4 : Advanced → Age >60 years, >1 extranodal site, Poor performance status, High LDH.'",
)

add(
    S5,
    150,
    "recall",
    "Under the 'Diffuse Large B cell Lymphoma' section at the bottom of page 150, what age group, sex ratio, tumor behavior, and overall NHL status are printed?",
    "Age >60 years; Male > Female; aggressive tumor; most common NHL",
    [
        "Age <10 years; Female > Male; low-grade indolent tumor; rarest NHL",
        "Age 15–34 years; Female > Male; benign self-limiting tumor; 5% of NHL",
        "Median age 13 years; Adolescent boys; precursor lymphoid blast tumor",
    ],
    "At the bottom of page 150 under 'Diffuse Large B cell Lymphoma': '• Age : >60 years. • Male > Female. • Aggressive tumor. • m/c NHL.'",
)

add(
    S5,
    150,
    "recall",
    "Under 'Clinical features :' of Diffuse Large B cell Lymphoma at the bottom of page 150, what is the most common site of primary lymphadenopathy and what is the main site of extranodal involvement?",
    "Primary lymphadenopathy: most common site → Neck; Extranodal involvement: mainly GIT",
    [
        "Primary lymphadenopathy: most common site → Epitrochlear; Extranodal involvement: mainly myocardium",
        "Primary lymphadenopathy: most common site → Popliteal; Extranodal involvement: mainly meninges",
        "Primary lymphadenopathy: most common site → Hilar bilateral; Extranodal involvement: mainly kidney",
    ],
    "Under 'Clinical features :' of DLBCL at the bottom of page 150: '• Primary lymphadenopathy : m/c site → Neck. • Extranodal involvement : Mainly GIT.'",
)


# ==============================================================================
# UNIT 6 — Page 151: DLBCL Subtypes, Double/Triple Hit vs Expressor & R-CHOP
# ==============================================================================

add(
    S6,
    151,
    "recall",
    "At the top of page 151 under 'Types :' of DLBCL, what immunophenotype and prognosis characterize the 'Germinal centre' subtype?",
    "CD 10, CD 23, BCL-6 +ve; Good prognosis",
    [
        "CD 10–ve, MUM-1 +ve; HIV-defining illness with bad prognosis",
        "CD 5+, Cyclin D1+, CD 23–ve; unresponsive to R-CHOP",
        "CD 15+, CD 30+, PAX-5 weak; lacunar cells with mediastinal mass",
    ],
    "On the left branch under 'Types : DLBCL → Germinal centre' at the top of page 151: '• CD 10, CD 23, BCL-6 +ve • Good prognosis.'",
)

add(
    S6,
    151,
    "recall",
    "On the right branch of 'Types :' on page 151, what cell of origin, two marker combinations, viral status, and prognosis define 'Activated B-cell DLBCL'?",
    "Cells of origin: Plasmablast; Markers: [CD 10–ve, BCL-6 +ve, MUM-1 expression +ve] or [CD 10–ve, BCL-6 –ve]; HIV-defining illness; Bad prognosis",
    [
        "Cells of origin: Centrocyte; Markers: CD 10+ve, CD 23+ve, MUM-1 –ve; HTLV-1 associated; Good prognosis",
        "Cells of origin: Naive B-cell; Markers: CD 5+ve, CD 23+ve; H. pylori associated; Excellent prognosis",
        "Cells of origin: Pro-B cell; Markers: CD 34+ve, TdT+ve; Parvovirus associated; Spontaneous remission",
    ],
    "Under 'Activated B-cell DLBCL' on page 151: '• Cells of origin : Plasmablast. • Markers : – CD 10–ve, BCL-6 +ve, MUM-1 expression +ve; – CD 10–ve, BCL-6 –ve. • HIV-defining illness. • Bad prognosis.'",
)

add(
    S6,
    151,
    "oddoneout",
    "On page 151 under Activated B-cell DLBCL 'Presentations :', all of the following four site-specific lymphomas carry the brace rule 'ABC-DLBCL unless proven otherwise' EXCEPT:",
    "Gastric H. pylori MALToma",
    [
        "CNS lymphoma",
        "Mediastinal lymphoma",
        "Organ transplant lymphoma and Body cavity lymphoma",
    ],
    "Under Activated B-cell DLBCL → 'Presentations :' on page 151, a brace groups '– CNS lymphoma. – Mediastinal lymphoma. – Organ transplant lymphoma. – Body cavity lymphoma.' as 'ABC-DLBCL unless proven otherwise'.",
)

add(
    S6,
    151,
    "recall",
    "Under 'Markers :' and 'Important terminologies :' on page 151, what is the relative frequency of BCL-6 vs BCL-2 alterations in DLBCL (compared with follicular lymphoma), and how are 'Double hit' and 'Triple hit' defined?",
    "Dysregulated BCL-6 > Aberrant BCL-2 t(14;18) (Note: opposite in follicular lymphoma); Double hit = c-myc rearrangement + rearrangement of BCL-2/BCL-6; Triple hit = rearrangement of c-myc + BCL-2 + BCL-6 — both carry bad prognosis",
    [
        "Aberrant BCL-2 > Dysregulated BCL-6 in DLBCL; Double hit = CD5 + Cyclin D1; Triple hit = CD19 + CD20 + CD22 — good prognosis",
        "Isolated SOX-11 overexpression without BCL-6 or BCL-2 changes; Double hit = two lymph node sites on same side of diaphragm — good prognosis",
        "BRAF V600E > MYD88 mutation; Double hit = simultaneous EBV + HIV infection — cured without chemotherapy",
    ],
    "Middle of page 151: 'Markers : Dysregulated BCL-6 > Aberrant BCL-2 t(14;18) | Note : Opposite in follicular lymphoma.' Under 'Important terminologies :': 'Double hit : c-myc rearrangement + rearrangement of BCL-2/BCL-6; Triple hit : Rearrangement of c-myc + BCL-2 + BCL-6 } Bad prognosis.'",
)

add(
    S6,
    151,
    "recall",
    "In the Venn diagram 'Relationship of cell of origin and high BCL-2 and MYC expression in DLBCL' on page 151, which DLBCL cell-of-origin subtype corresponds to 'Double hit lymphomas' versus 'Double expressor lymphomas'?",
    "Double hit lymphomas (overlap of BCL-2-R and MYC-R rearrangements) map to GCB; Double expressor lymphomas (overlap of High BCL-2 expression and High MYC expression) map to ABC",
    [
        "Double hit lymphomas map exclusively to ABC; Double expressor lymphomas map exclusively to GCB without protein expression",
        "Both Double hit and Double expressor lymphomas arise exclusively from mature T-cell lymphomas",
        "Double hit lymphomas lack chromosomal rearrangements; Double expressor lymphomas occur only in follicular lymphoma",
    ],
    "In the diagram on page 151 ('Relationship of cell of origin and high BCL-2 and MYC expression in DLBCL'), the left overlap of 'BCL-2-R' and 'MYC-R' points to 'Double hit lymphomas → GCB', while the right overlap of 'High BCL-2 expression' and 'High MYC expression' points to 'Double expressor lymphomas → ABC'.",
)

add(
    S6,
    151,
    "fillup",
    "At the bottom of page 151 under DLBCL 'Treatment : Regimen : R-CHOP', the five constituent drugs are Rituximab, Cyclophosphamide, Hydroxy-daunorubicin, ______ (Vincristine), and Prednisolone.",
    "Oncovirin",
    [
        "Obinutuzumab",
        "Oxaliplatin",
        "Ofatumumab",
    ],
    "At the bottom of page 151 under 'Treatment : Regimen : R-CHOP': '• Rituximab. • Cyclophosphamide. • Hydroxy-daunorubicin. • Oncovirin (Vincristine). • Prednisolone.'",
)


# ==============================================================================
# UNIT 7 — Page 152: DLBCL Interim PET Flowchart & Burkitt's Lymphoma
# ==============================================================================

add(
    S7,
    152,
    "management",
    "In the DLBCL treatment flowchart at the top of page 152 following '2 cycles of R-CHOP → Interim PET', what subsequent management is shown for 'Good score' (early favourable vs early unfavourable) versus 'Advanced disease'?",
    "Good score: Early, favourable disease → 2 more cycles of R-CHOP; Early, unfavourable disease → 4 more cycles of R-CHOP; Advanced disease → Autologous stem cell transplant",
    [
        "Good score: stop all therapy immediately after 2 cycles in both groups; Advanced disease → oral hydroxyurea maintenance alone",
        "Good score: immediate allogeneic stem cell transplant in Stage I; Advanced disease → H. pylori triple eradication therapy",
        "Good score: 8 cycles of ABVD + bleomycin; Advanced disease → single-agent rituximab observation without transplant",
    ],
    "At the top of page 152: '2 cycles of R-CHOP → Interim PET' branches into 'Good score' ('Early, favourable disease → 2 more cycles of R-CHOP' and 'Early, unfavourable disease → 4 more cycles of R-CHOP') and 'Advanced disease → Autologous stem cell transplant.'",
)

add(
    S7,
    152,
    "numeric",
    "Under 'Burkitt's Lymphoma' on page 152, what percentage of childhood NHL does it represent, and what CNS, chemosensitivity, and surface/nuclear marker features are listed?",
    "Childhood lymphoma representing 30% of childhood NHL; can involve CNS, chemosensitive, and CD10 and BCL-6 +ve",
    [
        "Represents 90% of elderly NHL; never involves CNS, chemoresistant, and CD5 and Cyclin D1 +ve",
        "Represents 5% of childhood NHL; spares meninges, radioresistant, and CD15 and CD30 +ve",
        "Represents 80% of pediatric acute leukemia; CD34 and TdT +ve with MPO positivity",
    ],
    "Under 'Burkitt's Lymphoma' on page 152: 'Childhood lymphoma (30% of childhood NHL). Can involve CNS. Chemosensitive. CD10 and BCL-6 +ve.'",
)

add(
    S7,
    152,
    "recall",
    "Under 'Pathophysiology :' of Burkitt's Lymphoma on page 152, which three chromosome 8 c-myc translocations (and which most common one) lead to high myc protein and the highest Ki67 proliferative index among NHL?",
    "c-myc dysregulation on chromosome 8 via t(8 ; 14) [most common], t(8 ; 2), and t(8 ; 22) → High levels of myc protein → Highest proliferative index (Ki67) among NHL",
    [
        "BCL-2 dysregulation on chromosome 18 via t(14 ; 18) [most common], t(11 ; 14), and t(2 ; 5) → Lowest Ki67 index among NHL",
        "BCR-ABL fusion on chromosome 22 via t(9 ; 22) [most common], inv(16), and t(15 ; 17) → Complete arrest without proliferation",
        "API2-MALT1 fusion via t(11 ; 18) [most common] → Indolent mucosal growth responsive to antibiotics",
    ],
    "Under 'Pathophysiology :' of Burkitt's Lymphoma on page 152: 'c-myc dysregulation on chromosome 8 → [t(8 ; 14) : m/c, t(8 ; 2), t(8 ; 22)] → High levels of myc protein → Highest proliferative index (Ki67) among NHL.'",
)

add(
    S7,
    152,
    "recall",
    "Under 'Types :' of Burkitt's Lymphoma on page 152, how do the Endemic, Sporadic, and third clinical variant differ?",
    "Endemic: children, EBV +ve, jaw/maxillary mass; Sporadic: adult, EBV –ve, abdominal mass, bone marrow involved (>30% cases); Third type: HIV associated (immunodeficiency associated)",
    [
        "Endemic: elderly adults, EBV –ve, ileocecal abdominal mass; Sporadic: young children, EBV +ve, mandibular mass without marrow involvement",
        "Endemic: HTLV-1 +ve, hypercalcemia & lytic lesions; Sporadic: HHV-8 +ve, pleural cavity effusion without solid tumor mass",
        "Endemic: H. pylori +ve, gastric antral ulcer; Sporadic: HCV +ve, isolated splenic white-pulp micronodules",
    ],
    "Under 'Types :' of Burkitt's Lymphoma on page 152: 'Endemic → • Children. • EBV +ve. • Jaw/maxillary mass'; 'Sporadic → • Adult. • EBV –ve. • Abdominal mass. • Bone marrow involved (>30% cases)'; and 'HIV associated (Immunodeficiency associated)'.",
)

add(
    S7,
    152,
    "management",
    "What intensive chemotherapy regimen is specified under 'Treatment :' of Burkitt's Lymphoma on page 152, and how does it respond to conventional chemotherapy?",
    "CODOX-M/IVAC regime; doesn't respond to conventional chemotherapy",
    [
        "Standard R-CHOP × 2 cycles; responds completely to single-agent oral chlorambucil",
        "FCR (Fludarabine + Cyclophosphamide + Rituximab); watch-and-wait until Stage 3 anemia",
        "Cladribine single-course infusion; maintenance oral methotrexate + 6-mercaptopurine only",
    ],
    "Under 'Treatment :' of Burkitt's Lymphoma on page 152: 'CODOX-M/IVAC regime. Doesn't respond to conventional chemotherapy.'",
)

add(
    S7,
    152,
    "recall",
    "At the bottom of page 152, which three lymphomas (including exact DLBCL percentage) are listed under 'Note : Lymphomas with bone marrow involvement :', and what represent the 'Stars' versus the 'Sky' in the Burkitt's Lymphoma histology caption?",
    "Bone marrow involvement: Burkitt's lymphoma, Mantle cell lymphoma, and DLBCL (20%); Starry sky appearance / tingible body macrophages of BL: Stars → Macrophages, Sky → Tumor cells",
    [
        "Bone marrow involvement: Gastric MALToma, Classical Hodgkin NS, and Mycosis fungoides; Stars → Reed-Sternberg cells, Sky → Reactive eosinophils",
        "Bone marrow involvement: Primary effusion lymphoma only; Stars → Tumor lymphoblasts, Sky → Mature marrow adipocytes",
        "Bone marrow involvement: Cutaneous ALCL only; Stars → Plasma cells with Russell bodies, Sky → Fibrous collagen stroma",
    ],
    "At the bottom of page 152: 'Note : Lymphomas with bone marrow involvement : • Burkitt's lymphoma. • Mantle cell lymphoma. • DLBCL (20%).' Caption under photomicrograph: 'Starry sky appearance/tingible body macrophages of BL : • Stars → Macrophages • Sky → Tumor cells.'",
)

add(
    S7,
    152,
    "scenario",
    "An 8-year-old child presents with a rapidly enlarging maxillary/jaw mass. Biopsy shows diffuse sheets of CD10+, BCL-6+ B-cells with a near-100% Ki67 proliferative index interspersed with pale benign phagocytic macrophages ('starry sky appearance'). Which chromosome 8 translocation is most common and which regimen is indicated per page 152?",
    "t(8 ; 14) causing c-myc dysregulation (EBV +ve endemic Burkitt's lymphoma); treat with intensive CODOX-M/IVAC regime",
    [
        "t(14 ; 18) causing aberrant BCL-2 expression; observe expectantly without chemotherapy",
        "t(11 ; 14) causing Cyclin D1 overexpression; treat with standard R-CHOP × 2 cycles",
        "t(11 ; 18) associated with H. pylori gastritis; treat with oral triple-antibiotic therapy",
    ],
    "Page 152 links pediatric EBV +ve jaw/maxillary mass to Endemic Burkitt's lymphoma with CD10 & BCL-6 positivity, t(8 ; 14) [most common c-myc translocation], highest Ki67 index among NHL, starry sky appearance (Stars = macrophages, Sky = tumor cells), treated with the CODOX-M/IVAC regime.",
)

add(
    S7,
    152,
    "truefalse",
    "Which statement regarding Burkitt's Lymphoma on page 152 is TRUE?",
    "True — Sporadic Burkitt's lymphoma occurs in adults, is EBV negative, presents with an abdominal mass, and involves the bone marrow in >30% of cases",
    [
        "True — In the starry-sky histology of Burkitt's lymphoma, the 'stars' represent neoplastic c-myc tumor cells and the 'sky' represents macrophages",
        "False — Burkitt's lymphoma accounts for 30% of childhood NHL, can involve the CNS, and exhibits the highest Ki67 proliferative index among NHLs",
        "False — Burkitt's lymphoma does not respond to conventional chemotherapy and requires the CODOX-M/IVAC regimen",
    ],
    "On page 152: Sporadic BL = Adult, EBV –ve, abdominal mass, bone marrow involved (>30% cases); Stars = Macrophages and Sky = Tumor cells; childhood BL = 30% of childhood NHL, can involve CNS, highest Ki67 among NHL, treated with CODOX-M/IVAC.",
)


GUIDES = {
    S1: (
        "Classification by Cell of Origin, Mature T-Cell Lymphomas (ALCL to Hepatosplenic) & Grade-Based Classification",
        "Cell of origin: Precursor T → T-ALL/LBL; Mature T → mature T-cell lymphoma; Precursor B → ALL; Pre-GC → MCL; Centroblasts → DLBCL, Burkitt's; Centrocytes → Follicular; Post-GC → MZL; Plasmablast → ABC-DLBCL.\n"
        "Mature T-cell lymphomas: (1) ALCL — ALK (CD30)+, t(2;5), breast implants, hallmark cells; (2) Angioimmunoblastic; (3) Enteropathy/Celiac T-cell; (4) Mycosis fungoides/Sezary; (5) Extranodal NK/T (EBV+); (6) HTLV-1 adult T-cell; (7) Hepatosplenic.\n"
        "Prognosis & grade: B-cell > T-cell; m/c NHL = DLBCL. Grade: Low (SLL, MZL, Follicular); Intermediate–high (MCL); High (DLBCL, Burkitt's).",
    ),
    S2: (
        "Causative Organisms Table (EBV 100/70/40/20 Rule, HIV, HCV, H. pylori, HHV-8, HTLV-1) & Ann-Arbor Staging",
        "Organisms: EBV → Hodgkin 100/70/40/20 rule (LD 100%, MC 70%, NS 40%, LR 20%) & NHL (B-cell: Burkitt's, Post-transplant & Primary CNS [DLBCL morphology]; T-cell: Extranodal NK/T); HIV → DLBCL, Burkitt's; HCV → Waldenstrom's, Splenic MZL; H. pylori → MALToma; HHV-8 → Primary effusion lymphoma, Castleman's; HTLV-1 → Adult T-cell leukemia/lymphoma.\n"
        "Ann-Arbor staging: I (single LN region), II (≥2 LN regions same side of diaphragm), III (both sides of diaphragm), IV (diffuse extralymphatic: lung, liver, bone).\n"
        "Risk grouping: Stages I–II = Early (Unfavourable if Age ≥60, ↑ LDH, >1 extranodal site, poor PS); Stages III–IV = Late/advanced (Unfavourable by default).",
    ),
    S3: (
        "NHL General Features, Mantle Cell Lymphoma (t(11;14), SOX-11, R-CHOP Resistance) & Follicular Lymphoma Genetics",
        "General NHL features: Age 60 yrs, M > F, m/c asymptomatic painless lymphadenopathy, m/c nodal site = supraclavicular; extranodal = GIT (m/c), Waldeyer's ring, BM (30–40%); B-symptoms & CNS very rare.\n"
        "Mantle cell lymphoma: Pre-GC origin; CD5+, Cyclin D1+, SOX-11+, t(11;14), CD10–, CD23–; aggressive (GIT lymphomatoid polyposis, BM, blood, spleen; unresponsive to R-CHOP); Classical = SOX-11+, Leukemic non-nodal = SOX-11– (printed good prognostic factor: SOX-11 upregulation).\n"
        "Follicular lymphoma genetics: CD10+, CD23+ & BCL-6 dysregulation (all GC malignancies) + aberrant BCL-2 from t(14;18) (chr 14 IgG heavy chain [printed] + chr 18 BCL-2).",
    ),
    S4: (
        "Follicular Lymphoma Histology/Course/Rx, Germinal Centre Malignancies Table & MALToma (t(11;18), H. pylori, Sjögren)",
        "Follicular lymphoma: Paratrabecular lymphoid aggregates with small cleaved + large non-cleaved cells; B-symptoms rare, spontaneous remission & relapse common; treat symptomatic only (low burden: Rituximab); Richter transformation 3%/yr. GC table: Centrocyte = Follicular (low grade); Centroblast = Burkitt's & DLBCL (aggressive).\n"
        "MALToma: m/c MZL (purely extranodal), post-GC origin, F > M (autoimmune), H. pylori non-atrophic pan-gastritis in 95%; CD5–, CD10–, CD23–, t(11;18); upper GI symptoms.\n"
        "MALToma Rx & notes: H. pylori eradication (80% respond) → R-CHOP trial if no response; printed good prognosis = H. pylori +ve, t(11;18); Richter conversion to DLBCL; Sjögren MZL involves salivary gland.",
    ),
    S5: (
        "High-Grade Lymphomas Overview, Clinical Features & Prognostic Factors, and Diffuse Large B-Cell Lymphoma (DLBCL)",
        "High-grade lymphomas: (1) DLBCL, (2) Burkitt's, (3) Anaplastic large lymphoma [printed 'B-cell' on p150] — t(2;5), CD30+, hallmark & flower cells.\n"
        "High-grade features: Rapidly progressive painless lymphadenopathy causing compression, extensive B-symptoms, extranodal (e.g., GIT), 'no involvement of BM or CNS' (general note), bad prognosis = LDH & hypoalbuminemia.\n"
        "DLBCL overview: Age >60 yrs, M > F, aggressive, m/c NHL; primary nodal site = Neck; extranodal = mainly GIT.",
    ),
    S6: (
        "DLBCL Subtypes (GCB vs ABC-DLBCL), Double/Triple-Hit vs Double-Expressor Venn Diagram & R-CHOP Regimen",
        "DLBCL subtypes: Germinal centre (CD10+, CD23+, BCL-6+; good prognosis) vs Activated B-cell / ABC-DLBCL (plasmablast origin; CD10–/BCL-6+/MUM-1+ or CD10–/BCL-6–; CNS, mediastinal, organ transplant & body cavity lymphomas = ABC-DLBCL unless proven otherwise; HIV-defining; bad prognosis).\n"
        "Genetics & Venn diagram: Dysregulated BCL-6 > aberrant BCL-2 t(14;18) (opposite in follicular). Double hit (c-myc + BCL-2/BCL-6 rearrangements, GCB) & Triple hit (c-myc + BCL-2 + BCL-6) = bad prognosis; Double expressor (high MYC + BCL-2 protein, ABC).\n"
        "Treatment: R-CHOP = Rituximab + Cyclophosphamide + Hydroxy-daunorubicin + Oncovirin (Vincristine) + Prednisolone.",
    ),
    S7: (
        "DLBCL Interim-PET Flowchart & Burkitt's Lymphoma (c-myc Translocations, Endemic vs Sporadic, CODOX-M/IVAC, Starry Sky)",
        "DLBCL response-adapted Rx: 2 cycles R-CHOP → Interim PET: Good score → +2 cycles R-CHOP (early favourable) or +4 cycles R-CHOP (early unfavourable); Advanced disease → Autologous stem cell transplant.\n"
        "Burkitt's lymphoma: 30% of childhood NHL, CNS involvement, chemosensitive, CD10+ & BCL-6+; chr 8 c-myc translocations t(8;14) [m/c], t(8;2), t(8;22) → highest Ki67 among NHL.\n"
        "Types, Rx & histology: Endemic (children, EBV+, jaw/maxillary mass), Sporadic (adult, EBV–, abdominal mass, BM >30%), HIV-associated. Rx: CODOX-M/IVAC (unresponsive to conventional chemo). BM involvement note: Burkitt's, MCL, DLBCL (20%). Starry sky: Stars = macrophages, Sky = tumor cells.",
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
