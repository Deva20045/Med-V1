#!/usr/bin/env python3
"""Generate Chapter 19: Myeloproliferative Neoplasms : Part 1 (Book p107–115).

Every question is anchored to a specific line, table cell, diagram label, or
flowchart step in uploads/01.pdf (PDF pages 119–127 = Book pages 107–115) in
strict book order. Handwritten numerals were cross-checked visually against
high-zoom renders (.audit-render/); items reproduced verbatim from the scan
are labelled "as printed".
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 19
TITLE = "Myeloproliferative Neoplasms : Part 1"
PAGES = "107-115"

S1 = "Overview: CMP Physiology, MPN Pathology and the Printed MPN List with Mutations"
S2 = "Clinical Features of MPN, Polycythemia Thresholds and Relative Polycythemia (Gaisböck's)"
S3 = "Absolute Polycythemia: Types, EPO/TC/PLC Table and Secondary Etiologies"
S4 = "Polycythemia Rubra Vera: JAK2 Mutations and Clinical Features"
S5 = "PCRV Investigations, Diagnostic Criteria and Management; Primary Myelofibrosis Etiology"
S6 = "Primary Myelofibrosis: Pathogenesis and Clinical Features"
S7 = "Primary Myelofibrosis: Investigations and Management"
S8 = "Essential Thrombocytosis: Etiology, Clinical Features, Investigations and Complications"
S9 = "Essential Thrombocytosis: Evaluation and Risk-Stratified Management"

RAW: list[tuple] = []


def add(sec: str, page: int, fmt: str, stem: str, correct: str, distractors: list[str], explanation: str) -> None:
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    rng = random.Random(19000 + CHAPTER * 10000 + len(RAW))
    rng.shuffle(options)
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
# UNIT 1 — Page 107: Overview, physiology diagram and the MPN list
# ==============================================================================

add(
    S1,
    107,
    "recall",
    "In the physiology diagram on page 107, the common myeloid progenitor (CMP) is shown giving rise to which terminal myeloid cells?",
    "RBCs, platelets, monocytes, eosinophils and basophils",
    [
        "RBCs, platelets, T-lymphocytes and NK cells",
        "Monocytes, eosinophils, basophils and B-lymphocytes",
        "RBCs, platelets, monocytes and lymphocytes",
    ],
    "The page 107 physiology diagram runs from the common myeloid progenitor (CMP) to terminal myeloid cells listed as RBC, platelets, monocytes, eosinophils and basophils.",
)

add(
    S1,
    107,
    "recall",
    "How does page 107 define the pathology of myeloproliferative neoplasms?",
    "Proliferation of (mature cells) of multiple lineages, with no dysplastic or immature cells seen",
    [
        "Proliferation of a single immature cell lineage with marrow replacement",
        "Ineffective proliferation of terminal myeloid cells ending in pancytopenia",
        "Proliferation of dysplastic blasts of multiple lineages",
    ],
    "Under PATHOLOGY, MPN is proliferation of (mature cells) of multiple lineages with no dysplastic or immature cells seen — contrasting with acute leukemia (single immature cell) and MDS (ineffective proliferation → pancytopenia).",
)

add(
    S1,
    107,
    "recall",
    "Which entity heads the printed MPN list on page 107 as the most common (m/c) member?",
    "Polycythemia rubra vera (PCRV)",
    [
        "Chronic myeloid leukemia (CML)",
        "Primary myelofibrosis (PMF)",
        "Essential thrombocytosis (ET)",
    ],
    "Item 1 of the list is 'Polycythemia rubra vera (PCRV) : m/c'.",
)

add(
    S1,
    107,
    "match",
    "Match each myeloproliferative neoplasm with the molecular lesion printed beside it on page 107 — 1) Chronic myeloid leukemia (CML) 2) Chronic neutrophilic leukemia (CNL) 3) Chronic eosinophilic leukemia (CEL) 4) Primary myelofibrosis (PMF), additional lesion … A) BCR-ABL translocation t(9;22) B) CSF3R mutation C) PDGFRA mutation D) Deletion on chr 9p",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-A, 2-C, 3-B, 4-D",
        "1-D, 2-B, 3-C, 4-A",
        "1-B, 2-A, 3-C, 4-D",
    ],
    "Page 107 pairs CML with BCR-ABL translocation t(9;22), CNL with CSF3R mutation, CEL with PDGFRA mutation, and adds 'Deletion on chr 9p' next to PMF within the JAK-2 bracket.",
)

add(
    S1,
    107,
    "recall",
    "The bracket on page 107 groups which three entities under the JAK-2 mutation?",
    "Polycythemia rubra vera, primary myelofibrosis and essential thrombocytosis",
    [
        "CML, CNL and CEL",
        "PCRV, CML and JMML",
        "PMF, ET and systemic mastocytosis",
    ],
    "The JAK-2 mutation brace covers items 1–3: PCRV (m/c), primary myelofibrosis and essential thrombocytosis/thrombocythemia.",
)

add(
    S1,
    107,
    "oddoneout",
    "Page 107 lists the following under the BCR-ABL negative arm. Pick the ODD ONE OUT — the entity that is NOT in that group:",
    "Chronic myeloid leukemia (CML)",
    [
        "Chronic neutrophilic leukemia (CNL)",
        "Juvenile myelomonocytic leukemia (JMML)",
        "MPN, not otherwise specified",
    ],
    "CML sits under the BCR-ABL translocation arm; the BCR-ABL negative arm lists CNL, CEL, JMML and MPN not otherwise specified.",
)

add(
    S1,
    107,
    "truefalse",
    "Which statements about the page 107 notes are TRUE as printed?",
    "True — Systemic mastocytosis (mast cell disease) carries a c-kit mutation and is excluded from the MPN list",
    [
        "True — Primary myelofibrosis (myelophthisis) is listed as a cause of bone marrow excess",
        "False — Chronic eosinophilic leukemia is paired with a CSF3R mutation",
        "False — The JAK-2 bracket on page 107 covers CML, CNL and CEL",
    ],
    "The note states 1° myelofibrosis (myelophthisis) = bone marrow failure (not excess), and systemic mastocytosis (c-kit) is excluded from MPN; CEL carries PDGFRA (not CSF3R), and the JAK-2 bracket covers PCRV/PMF/ET (not the BCR-ABL group).",
)

add(
    S1,
    107,
    "fillup",
    "Item 8 of the page 107 MPN list reads 'MPN, ______'.",
    "not otherwise specified",
    [
        "not otherwise classified",
        "unclassifiable with fibrosis",
        "in accelerated transformation",
    ],
    "The eighth printed item is 'MPN, not otherwise specified'.",
)

# ==============================================================================
# UNIT 2 — Page 108: MPN clinical features, polycythemia table, relative polycythemia
# ==============================================================================

add(
    S2,
    108,
    "recall",
    "Page 108 lists extramedullary hematopoiesis in MPN at which sites, and which is the most common?",
    "Spleen (m/c), skin, liver etc.",
    [
        "Liver (m/c), spleen, lymph nodes etc.",
        "Spleen (m/c), thymus, thyroid etc.",
        "Skin (m/c), spleen, kidney etc.",
    ],
    "Extramedullary hematopoiesis is printed as spleen (m/c), skin, liver etc.",
)

add(
    S2,
    108,
    "match",
    "Match the printed grade of splenomegaly with its disease on page 108 — 1) Massive 2) Moderate 3) Mild … A) PCRV B) ET C) CML and PMF",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "Page 108 prints massive splenomegaly with CML and PMF, moderate with PCRV, and mild with ET.",
)

add(
    S2,
    108,
    "numeric",
    "Classical B symptoms (fever, night sweats, weight loss) occur in what percentage of MPN patients as printed on page 108?",
    "20%",
    [
        "10%",
        "40%",
        "50%",
    ],
    "The line reads 'Classical B symptoms : In 20% (Fever, night sweats, weight loss)'.",
)

add(
    S2,
    108,
    "recall",
    "According to the page 108 note, acute leukemia and MDS differ from MPN how?",
    "Acute leukemia = proliferation of a single immature cell; MDS = ineffective proliferation of terminal myeloid cells → pancytopenia",
    [
        "Acute leukemia = proliferation of mature cells of multiple lineages; MDS = effective hyperproliferation",
        "Acute leukemia = ineffective erythropoiesis; MDS = proliferation of a single immature cell",
        "Acute leukemia = no dysplastic cells; MDS = mature multilineage proliferation",
    ],
    "The note contrasts MPN with acute leukemia (proliferation of single immature cell) and defines MDS as ineffective proliferation of terminal myeloid cells → pancytopenia; MPN symptoms arise from cytokines, hyperviscosity and classical B symptoms.",
)

add(
    S2,
    108,
    "truefalse",
    "Assess the page 108 statements as printed.",
    "True — MPN can transform into each other or into AML",
    [
        "True — The MDS/MPN overlap is included in the WHO 5th edition classification",
        "False — Myelodysplastic syndrome causes pancytopenia through ineffective proliferation of terminal myeloid cells",
        "False — MPN symptoms are attributed to cytokines, hyperviscosity and classical B symptoms",
    ],
    "Page 108 states MPN can transform into each other or AML and that the MDS/MPN overlap is included in the WHO 5th edition classification; MDS does cause pancytopenia via ineffective proliferation and the symptom list is as printed, so those two 'False' framings are wrong.",
)

add(
    S2,
    108,
    "match",
    "Match the polycythemia screening threshold printed in the page 108 table — 1) Male, Hb (gm%) 2) Male, PCV 3) Female, Hb (gm%) 4) Female, PCV … A) ≥16.5 B) 49 C) ≥16 D) 48",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-C, 2-D, 3-A, 4-B",
        "1-A, 2-B, 3-D, 4-C",
        "1-B, 2-A, 3-C, 4-D",
    ],
    "The table prints Hb (gm%) ≥16.5 and PCV 49 for males and ≥16 and 48 for females.",
)

add(
    S2,
    108,
    "recall",
    "What are the two printed types of polycythemia on page 108?",
    "Relative and absolute",
    [
        "Primary and secondary only",
        "Congenital and acquired",
        "Stress and sporadic",
    ],
    "'Types : Relative, absolute.' is printed; absolute polycythemia is then subdivided into primary (PCRV) and secondary on page 109.",
)

add(
    S2,
    108,
    "recall",
    "Relative polycythemia on page 108 is eponymously labelled as:",
    "Gaisböck's syndrome",
    [
        "Chuvash polycythemia",
        "Stress erythrocytosis of Osler",
        "Hepatomaplus syndrome",
    ],
    "The heading reads RELATIVE POLYCYTHEMIA (GAISBÖCK'S SYNDROME).",
)

add(
    S2,
    108,
    "recall",
    "What etiopathogenesis is printed for relative polycythemia, and which post-infectious association is noted?",
    "↓ plasma volume (dehydration) → ↑ Hb%; a post-viral association is listed",
    [
        "↑ RBC mass from hypoxia → ↑ Hb%; post-bacterial association",
        "↓ EPO feedback from hepatoma → ↑ Hb%; post-viral association",
        "↑ plasma volume (overhydration) → ↓ Hb%; no infectious link",
    ],
    "Etiopathogenesis is ↓ plasma volume (dehydration) → ↑ Hb%, with 'Post viral' listed beneath.",
)

add(
    S2,
    108,
    "oddoneout",
    "In relative polycythemia the page 108 investigations are printed as follows. Pick the ODD ONE OUT — the result NOT as printed:",
    "Hb : decreased",
    [
        "RBC mass : normal",
        "Total count (TC) : normal",
        "Platelet count (PLC) : normal",
    ],
    "Page 108 prints RBC mass normal, ↑ Hb, TC normal and PLC normal — Hb is increased, not decreased.",
)

add(
    S2,
    108,
    "scenario",
    "A patient reviewed after a viral illness shows a raised Hb with a normal RBC mass, normal total count and normal platelet count. Which page 108 label fits best?",
    "Relative polycythemia (Gaisböck's syndrome) from ↓ plasma volume",
    [
        "Primary polycythemia (PCRV)",
        "Secondary polycythemia from hypoxia",
        "Essential thrombocytosis",
    ],
    "Raised Hb with normal RBC mass/TC/PLC matches relative polycythemia (Gaisböck's), whose mechanism is ↓ plasma volume (dehydration) → ↑ Hb%, listed with a post-viral association.",
)

# ==============================================================================
# UNIT 3 — Page 109: absolute polycythemia table and secondary etiologies
# ==============================================================================

add(
    S3,
    109,
    "recall",
    "Absolute polycythemia on page 109 is characterized by which RBC mass finding and which two types?",
    "RBC mass increased; types primary (PCRV) and secondary",
    [
        "RBC mass normal; types relative and stress",
        "RBC mass decreased; types primary and tertiary",
        "RBC mass increased; types relative and absolute",
    ],
    "The management box opens with 'RBC mass : Increased' and 'Types : Primary (PCRV), Secondary'.",
)

add(
    S3,
    109,
    "match",
    "Match the parameter with its printed value in the page 109 primary-versus-secondary table — 1) EPO in primary (PCRV) 2) EPO in secondary 3) TC and PLC together in primary 4) TC and PLC together in secondary … A) Normal to low B) Increased C) Both increased D) Both normal",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-B, 3-D, 4-C",
        "1-C, 2-B, 3-A, 4-D",
    ],
    "The table prints EPO normal to low in PCRV versus increased in secondary; TC and PLC are both increased in PCRV but both normal in secondary polycythemia.",
)

add(
    S3,
    109,
    "recall",
    "Page 109 gives the EPO abbreviation and locates its production where?",
    "Erythropoietin; cortex and outer medulla of kidney",
    [
        "Erythropoietin; juxtaglomerular apparatus only",
        "Erythropoietin; hepatic sinusoids",
        "Erythropoietin; adrenal medulla",
    ],
    "The footnote reads 'EPO : Erythropoietin' with production noted at the cortex ('and outer medulla of kidney' legible on the scan).",
)

add(
    S3,
    109,
    "oddoneout",
    "Page 109 lists hypoxic causes of secondary polycythemia. Pick the ODD ONE OUT — the item NOT filed under hypoxia:",
    "Renal artery stenosis",
    [
        "COPD and OSAS (Obstructive Sleep Apnea Syndrome)",
        "High altitude and CO intoxication",
        "Hepatopulmonary syndrome",
    ],
    "Hypoxia lists COPD, OSAS, high altitude, CO intoxication and hepatopulmonary syndrome; renal artery stenosis is a separate (item 2) renal cause.",
)

add(
    S3,
    109,
    "recall",
    "Which paraneoplastic causes of secondary polycythemia are printed on page 109?",
    "Renal carcinoma (hypernephroma), cerebellar hemangioblastoma, meningioma, pheochromocytoma, hepatoma and uterine fibroids",
    [
        "Hepatoma, Wilms tumour, adrenal adenoma and cholangiocarcinoma",
        "Renal carcinoma, pituitary adenoma, meningioma and thymoma",
        "Cerebellar hemangioblastoma, pheochromocytoma, GIST and osteoblastoma",
    ],
    "The paraneoplastic list is renal carcinoma (hypernephroma), cerebellar hemangioblastoma (a/w von Hippel-Lindau syndrome), meningioma, pheochromocytoma, hepatoma and uterine fibroids.",
)

add(
    S3,
    109,
    "recall",
    "Cerebellar hemangioblastoma on page 109 is associated with which syndrome?",
    "Von Hippel-Lindau syndrome",
    [
        "Tuberous sclerosis",
        "Neurofibromatosis type 1",
        "Li-Fraumeni syndrome",
    ],
    "The parenthetical reads '(a/w von Hippel-Lindau syndrome)'.",
)

add(
    S3,
    109,
    "recall",
    "What does page 109 state about pallor in pheochromocytoma?",
    "Presence of pallor in pheochromocytoma indicates malignancy",
    [
        "Pallor indicates benign behaviour",
        "Pallor is due to coexisting iron deficiency",
        "Pallor excludes catecholamine excess",
    ],
    "The note reads 'Presence of pallor in pheochromocytoma indicates malignancy' (as printed).",
)

add(
    S3,
    109,
    "fillup",
    "On page 109, uterine fibroids and hepatoma appear under the ______ causes of secondary polycythemia.",
    "paraneoplastic",
    [
        "hypoxic",
        "renal",
        "idiopathic",
    ],
    "Both sit under '3. Paraneoplastic' in the secondary polycythemia etiology list.",
)

add(
    S3,
    109,
    "recall",
    "Which clinical features of secondary polycythemia are printed on page 109, and in which group are they seen?",
    "Headache, dizziness and hypertension; seen in paraneoplastic patients",
    [
        "Aquagenic pruritus, erythromelalgia and gout; seen in hypoxic patients",
        "Headache, dizziness and hypotension; seen in all secondary patients",
        "Bleeding, thrombosis and splenomegaly; seen in PCRV only",
    ],
    "Clinical features are printed as headache, dizziness and hypertension, 'Seen in paraneoplastic patients'.",
)

add(
    S3,
    109,
    "truefalse",
    "Judge the page 109 table statements as printed.",
    "True — In secondary polycythemia the EPO level is increased while TC and PLC remain normal",
    [
        "True — In primary polycythemia (PCRV) the EPO level is normal to low",
        "False — Hepatopulmonary syndrome is listed among hypoxic causes of secondary polycythemia",
        "False — CO intoxication is printed as a hypoxic cause of secondary polycythemia",
    ],
    "The table prints EPO normal-to-low in PCRV and increased in secondary (with TC/PLC normal in secondary); hepatopulmonary syndrome and CO intoxication both sit under hypoxia, so the two 'False' framings contradict the page.",
)

# ==============================================================================
# UNIT 4 — Page 110: PCRV genetics and clinical features
# ==============================================================================

add(
    S4,
    110,
    "recall",
    "Page 110 gives the epidemiology of primary polycythemia (PCRV) as:",
    "m/c MPN; age 50–60 years; female > male",
    [
        "Rare MPN; age 20–30 years; male > female",
        "m/c MPN; age >70 years; male > female",
        "Second commonest MPN; age 50–60 years; male = female",
    ],
    "The printed bullets are m/c MPN, age 50-60 years, gender female > male.",
)

add(
    S4,
    110,
    "numeric",
    "The JAK-2 mutation is seen in what percentage of PCRV patients on page 110?",
    "100%",
    [
        "50%",
        "75%",
        "95%",
    ],
    "The line reads 'JAK-2 mutation (Seen in 100% patients)'.",
)

add(
    S4,
    110,
    "match",
    "Match the JAK-2 detail printed on page 110 — 1) Overall JAK-2 frequency in PCRV 2) Exon 14 mutation 3) Exon 12 mutation … A) 100% B) 95% (V617F) C) 5%",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 110 prints JAK-2 in 100% of patients, exon 14 mutation (95%) as V617F, and exon 12 mutation (5%).",
)

add(
    S4,
    110,
    "recall",
    "How does page 110 order thrombosis in PCRV, and which examples are printed for each compartment?",
    "Arterial > venous; arterial = stroke in young; venous = Budd-Chiari syndrome and DVT; microvascular = erythromelalgia",
    [
        "Venous > arterial; venous = stroke in young; arterial = Budd-Chiari and DVT",
        "Arterial > venous; arterial = myocardial infarction only; venous = portal vein thrombosis only",
        "Arterial = venous; both limited to cerebral vessels",
    ],
    "Thrombosis is printed arterial > venous with arterial stroke in young, venous Budd-Chiari syndrome/deep vein thrombosis, and microvascular erythromelalgia.",
)

add(
    S4,
    110,
    "oddoneout",
    "Page 110 assigns thrombosis examples to compartments. Pick the ODD ONE OUT — the pairing NOT as printed:",
    "Stroke in young listed as a venous event",
    [
        "Budd-Chiari syndrome listed as a venous event",
        "Deep vein thrombosis listed as a venous event",
        "Erythromelalgia listed as a microvascular event",
    ],
    "Stroke in young is printed under arterial thrombosis; Budd-Chiari and DVT are venous and erythromelalgia microvascular.",
)

add(
    S4,
    110,
    "recall",
    "Which page 110 mechanism explains aquagenic pruritus (pruritus after bath) in PCRV?",
    "Basophilia (mast cell → histamine)",
    [
        "Neutrophilia with toxic granulation",
        "Eosinophilia with major basic protein release",
        "Thrombocytosis with acquired von Willebrand disease",
    ],
    "Basophilia (mast cell → histamine) is printed as the cause of aquagenic pruritus (pruritus after bath).",
)

add(
    S4,
    110,
    "recall",
    "Mature granulocytes in PCRV raise which transport protein and therefore which capacity, per page 110?",
    "↑ transcobalamin-I → ↑ vitamin B12 binding capacity",
    [
        "↑ transferrin → ↑ iron binding capacity",
        "↑ haptoglobin → ↑ hemoglobin binding capacity",
        "↑ transcobalamin-II → ↓ vitamin B12 binding capacity",
    ],
    "The line reads 'mature granulocytes : ↑ transcobalamin-I → ↑ vit B12 binding capacity'.",
)

add(
    S4,
    110,
    "recall",
    "Why does bleeding (epistaxis) occur in PCRV thrombocytosis according to page 110?",
    "↑ dysfunctional platelets causing acquired von Willebrand disease",
    [
        "Platelet consumption in splenic sinusoids",
        "Vitamin K deficiency from hepatomegaly",
        "Fibrinogen consumption in microthrombi",
    ],
    "Thrombocytosis (↑ dysfunctional platelets) is linked to bleeding (epistaxis) via acquired von Willebrand disease.",
)

add(
    S4,
    110,
    "fillup",
    "Erythromelalgia is described on page 110 as burning pain of hands and feet due to ______ thrombosis.",
    "microvascular",
    [
        "arterial",
        "venous",
        "lymphatic",
    ],
    "Item 4 prints erythromelalgia (burning pain of hand and feet) 'D/t microvascular thrombosis'.",
)

add(
    S4,
    110,
    "recall",
    "Hyperuricemia in PCRV is attributed on page 110 to:",
    "Increased turnover of cells",
    [
        "Renal tubular urate retention",
        "Purine-free diet deficiency",
        "Xanthine oxidase induction by JAK-2",
    ],
    "Item 6 prints 'Hyperuricemia : D/t ↑ turnover of cells'.",
)

add(
    S4,
    110,
    "truefalse",
    "Assess the page 110 investigation findings as printed.",
    "True — ESR is low because of ↓ rouleaux formation",
    [
        "True — Leukocyte alkaline phosphatase (LAP) from mature neutrophils is high",
        "False — The peripheral smear shows microcytosis with erythrocytosis",
        "False — Vitamin B12 binding capacity is increased",
    ],
    "Page 110 prints RBC increased with ↓ MCV/normal MCH, ESR low (↓ rouleaux), PS microcytosis with erythrocytosis, LAP high and ↑ vit B12 binding capacity — so the two 'False' framings contradict the printed lines.",
)

# ==============================================================================
# UNIT 5 — Page 111: PCRV note, criteria, management; PMF etiology
# ==============================================================================

add(
    S5,
    111,
    "recall",
    "What mechanism does the page 111 note give for the low ESR in PCRV?",
    "↓ MCV (to conserve MCH) → no rouleaux formation",
    [
        "↑ fibrinogen → enhanced rouleaux",
        "↑ plasma volume diluting globulins",
        "Hyperviscosity preventing sedimentation outright",
    ],
    "The note reads '↓ MCV (To conserve MCH) → No rouleaux formation'.",
)

add(
    S5,
    111,
    "oddoneout",
    "The page 111 note lists causes of microcytosis. Pick the ODD ONE OUT — the one NOT on that printed list:",
    "Iron deficiency anemia",
    [
        "Hypoxia",
        "Thalassemia",
        "PCRV",
    ],
    "The printed microcytosis list is hypoxia, thalassemia and PCRV; iron deficiency anemia is not listed there.",
)

add(
    S5,
    111,
    "match",
    "Match transcobalamin facts from the page 111 diagram — 1) Site of production 2) Role … A) Neutrophils B) For transport : liver, etc.",
    "1-A, 2-B",
    [
        "1-B, 2-A",
        "1-A, 2-A",
        "1-B, 2-B",
    ],
    "The small diagram prints transcobalamin produced by neutrophils and used for transport (liver, etc.).",
)

add(
    S5,
    111,
    "numeric",
    "State the haemoglobin major criterion for PCRV on page 111 for men and women respectively.",
    ">16.5 g/dL in men and >16 g/dL in women",
    [
        ">15.5 g/dL in men and >14.5 g/dL in women",
        ">17.5 g/dL in men and >17 g/dL in women",
        ">16.0 g/dL in men and >15.0 g/dL in women",
    ],
    "Major criterion 1 prints Hb >16.5 g/dL in men and >16 g/dL in women.",
)

add(
    S5,
    111,
    "recall",
    "List the remaining major criteria and the minor criterion for PCRV as printed on page 111.",
    "Major: bone marrow hypercellularity and JAK-2 mutation; minor: subnormal serum erythropoietin level",
    [
        "Major: splenomegaly and LAP score; minor: raised serum EPO",
        "Major: Ph chromosome and basophilia; minor: normal serum EPO",
        "Major: thrombocytosis and hyperuricemia; minor: raised serum EPO",
    ],
    "Major criteria 2–3 are bone marrow hypercellularity and JAK-2 mutation; the minor criterion is a subnormal serum erythropoietin level.",
)

add(
    S5,
    111,
    "management",
    "A 45-year-old PCRV patient without prior thrombosis is stratified low risk on page 111. What treatment is printed?",
    "Phlebotomy weekly (maintain Hb 13–14 g/dL) + aspirin",
    [
        "Phlebotomy + aspirin 75 mg + ruxolitinib 10 mg BD",
        "Hydroxyurea 0.5–2 g/day alone",
        "Immediate allogeneic stem cell transplant",
    ],
    "The low-risk arm (<60 years) is phlebotomy weekly (maintain Hb 13-14 g/dL) + aspirin.",
)

add(
    S5,
    111,
    "management",
    "A 65-year-old PCRV patient with a history of thrombosis is stratified high risk on page 111. Which regimen is printed?",
    "Phlebotomy + aspirin 75 mg + JAK inhibitor ruxolitinib 10 mg BD (or) hydroxyurea 0.5–2 g/day",
    [
        "Aspirin 75 mg alone with observation",
        "Weekly phlebotomy alone maintaining Hb 13–14 g/dL",
        "Ruxolitinib without phlebotomy or aspirin",
    ],
    "The high-risk arm (>60 yrs, h/o thrombosis) prints phlebotomy + aspirin 75 mg + JAK inhibitor ruxolitinib 10 mg BD (or) hydroxyurea 0.5-2 g/day.",
)

add(
    S5,
    111,
    "match",
    "Match the PMF mutation with its printed frequency on page 111 — 1) JAK-2 2) Calreticulin (CALR) 3) MPL gene 4) Triple negative PMF … A) 50% B) 30–40% C) 10–20% D) Absence of the above mutations (poor prognosis)",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-C, 3-B, 4-D",
        "1-C, 2-B, 3-A, 4-D",
    ],
    "PMF etiology prints JAK-2 50%, CALR 30–40%, MPL 10–20%, and triple negative PMF as absence of the above mutations with poor prognosis.",
)

add(
    S5,
    111,
    "recall",
    "The MPL gene mutated in PMF codes for which molecule, per page 111?",
    "Thrombopoietin (its receptor pathway)",
    [
        "Erythropoietin",
        "Granulocyte colony-stimulating factor",
        "Interleukin-3",
    ],
    "The parenthetical reads 'mPL gene mutation (Codes for thrombopoietin)'.",
)

add(
    S5,
    111,
    "recall",
    "Besides the mutation list, which cytogenetic lesion is printed at the foot of the PMF etiology on page 111?",
    "Deletion 13q",
    [
        "Deletion 20q",
        "Monosomy 7",
        "Isochromosome 17",
    ],
    "The last etiology line prints 'Deletion 13q'.",
)

# ==============================================================================
# UNIT 6 — Page 112: PMF pathogenesis and clinical features
# ==============================================================================

add(
    S6,
    112,
    "recall",
    "In the page 112 pathogenesis of PMF, dysplastic megakaryocytes lack which receptor?",
    "CXCR4 receptors",
    [
        "CD55/CD59 GPI anchors",
        "TPO (MPL) receptors",
        "Fcγ receptors",
    ],
    "The diagram labels dysplastic megakaryocytes as '(Lack CXCR4 receptors)' alongside myeloproliferation (hypercellular marrow).",
)

add(
    S6,
    112,
    "recall",
    "Which two growth factors drive marrow fibrosis on page 112, and which is called the most potent pathogenic fibrogenic cytokine?",
    "TGF-β (most potent) and PDGF (platelet derived growth factor); fibrosis shows ↑ type-III collagen",
    [
        "VEGF (most potent) and FGF; ↑ type-I collagen",
        "TGF-α (most potent) and EGF; ↑ type-IV collagen",
        "PDGF (most potent) and IL-6; ↑ type-II collagen",
    ],
    "The pathway prints TGF-β (most potent pathogenic fibrogenic cytokine) and PDGF causing marrow fibrosis (↑ in type-III collagen).",
)

add(
    S6,
    112,
    "recall",
    "What peripheral smear consequence follows the release of premature cells in PMF on page 112?",
    "Leukoerythroblastosis in peripheral smear, with pancytopenia",
    [
        "Pure erythroid predominance without immature cells",
        "Isolated thrombocytosis without nucleated red cells",
        "Rouleaux formation with normal counts",
    ],
    "The diagram shows release of premature cells → pancytopenia and leukoerythroblastosis in peripheral smear.",
)

add(
    S6,
    112,
    "recall",
    "Summarize the demographic and presentation notes for PMF on page 112.",
    "Most cases present in fibrotic stage; age >60 years; male = female",
    [
        "Most cases present in proliferative stage; age <40 years; female > male",
        "Most cases present in fibrotic stage; age >60 years; male > female",
        "Most cases present acutely with blast crisis; male = female",
    ],
    "The clinical features print most cases presenting in the fibrotic stage, age >60 years, gender male = female.",
)

add(
    S6,
    112,
    "recall",
    "How does page 112 rank thrombosis risk across the MPNs?",
    "PCRV > ET > PMF",
    [
        "PMF > ET > PCRV",
        "ET > PCRV > PMF",
        "PCRV > PMF > ET",
    ],
    "The line reads 'Thrombosis (↑ risk in PCRV > ET > PMF)'.",
)

add(
    S6,
    112,
    "recall",
    "Which symptom is labelled the most common in PMF pancytopenia on page 112?",
    "Fatigue from anemia",
    [
        "Bleeding from thrombocytopenia",
        "Bone pain from osteosclerosis",
        "Pruritus from basophilia",
    ],
    "Under pancytopenia, anemia : fatigue is printed as the m/c symptom, with bleeding listed next.",
)

add(
    S6,
    112,
    "recall",
    "When does gout appear in PMF according to page 112?",
    "During the proliferation stage",
    [
        "Only after splenectomy",
        "During the fibrotic stage",
        "After hydroxyurea therapy",
    ],
    "The bullet reads 'Gout : During proliferation stage'.",
)

add(
    S6,
    112,
    "match",
    "Match the extramedullary hematopoiesis manifestation printed on page 112 with its detail — 1) Massive splenomegaly 2) Osteosclerosis 3) Hepatomegaly 4) Skin … A) 75% of cases B) Bony involvement C) Portal hypertension D) Febrile neutrophilic dermatosis (Sweet syndrome)",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-C, 2-B, 3-A, 4-D",
        "1-A, 2-D, 3-C, 4-B",
        "1-B, 2-A, 3-D, 4-C",
    ],
    "Page 112 prints massive splenomegaly (75%), osteosclerosis, hepatomegaly (portal hypertension) and skin involvement as febrile neutrophilic dermatosis (Sweet syndrome).",
)

add(
    S6,
    112,
    "recall",
    "What does the page 112 note say about febrile neutrophilic dermatosis (Sweet syndrome)?",
    "It is characteristic of AML",
    [
        "It is characteristic of CML chronic phase",
        "It is specific for PMF among all MPNs",
        "It indicates benign disease",
    ],
    "The note reads 'Febrile neutrophilic dermatosis is characteristic of AML'.",
)

add(
    S6,
    112,
    "match",
    "Match each cutaneous image caption on page 112 to what it shows — 1) 'Annular lesions (A,B,D)' 2) 'Erythematous lesions on lower limb' 3) 'Erythematous papules and plaques' … A) Ring-shaped lesions labelled in panels A, B and D B) Reddish lesions photographed on the leg C) Raised red papules/plaques photograph",
    "1-A, 2-B, 3-C",
    [
        "1-C, 2-A, 3-B",
        "1-A, 2-C, 3-B",
        "1-B, 2-C, 3-A",
    ],
    "The three printed cutaneous-manifestation captions are annular lesions (A,B,D), erythematous lesions on lower limb, and erythematous papules and plaques.",
)

# ==============================================================================
# UNIT 7 — Page 113: PMF investigations and management
# ==============================================================================

add(
    S7,
    113,
    "recall",
    "Which two peripheral smear findings open the PMF investigations on page 113?",
    "Anisopoikilocytosis with teardrop red cells/dacryocytes, and cloud-like megakaryocytes",
    [
        "Spherocytes with polychromasia, and dwarf megakaryocytes",
        "Schistocytes with helmet cells, and staghorn megakaryocytes",
        "Rouleaux with cryoglobulins, and giant platelets",
    ],
    "Peripheral smear prints anisopoikilocytosis with teardrop red cells/dacryocyte and thrombocytosis with cloud-like megakaryocytes.",
)

add(
    S7,
    113,
    "recall",
    "Which serum peptide is increased in PMF on page 113, mirroring the fibrosis marker?",
    "Serum type-III procollagen peptide",
    [
        "Serum type-I procollagen peptide",
        "Serum alkaline phosphatase only",
        "Serum beta-2 microglobulin",
    ],
    "The investigations list 'Serum type-III procollagen peptide : Increased' (matching the ↑ type-III collagen fibrosis on p112).",
)

add(
    S7,
    113,
    "recall",
    "What does page 113 state about the bone marrow aspirate and biopsy in PMF?",
    "Aspirate : dry tap; biopsy : silver impregnation shows reticulin fibrosis ± collagen fibrosis, with fibrosis and hypercellular marrow",
    [
        "Aspirate : markedly hypercellular wet tap; biopsy : only fat replacement",
        "Aspirate : dry tap; biopsy : hypocellular marrow without fibrosis",
        "Aspirate : hemodilute tap; biopsy : granulomas with caseation",
    ],
    "Bone marrow aspirate is a dry tap; biopsy shows silver impregnation reticulin fibrosis ± collagen fibrosis and fibrosis with hypercellular marrow.",
)

add(
    S7,
    113,
    "match",
    "Match each page 113 image caption with its picture — 1) 'Peripheral smear with tear drop cells' 2) 'Marrow cavity replaced by fibrous tissue' 3) 'Peripheral smear with nucleated RBC's and blast cells' … A) Smear photograph dominated by dacryocytes B) Biopsy view showing fibrous replacement C) Smear showing nucleated red cells and blasts",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The three captions run exactly as listed: teardrop smear, marrow cavity replaced by fibrous tissue, and smear with nucleated RBCs and blast cells.",
)

add(
    S7,
    113,
    "recall",
    "What does the page 113 note highlight about megakaryocytes?",
    "Megakaryocytes appear in the peripheral smear",
    [
        "Megakaryocytes are absent in the marrow",
        "Megakaryocytes are seen only in lymph nodes",
        "Peripheral megakaryocytes exclude PMF",
    ],
    "The note reads 'megakaryocytes in peripheral smear'.",
)

add(
    S7,
    113,
    "match",
    "Match the printed megakaryocyte descriptor with its disease on page 113 (and neighbouring pages) — 1) Staghorn 2) Giant 3) Cloud-like 4) Dwarf … A) ET B) ITP C) PMF D) CML",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-B, 3-D, 4-C",
        "1-C, 2-D, 3-A, 4-B",
    ],
    "Page 113 prints staghorn : ET and giant : ITP, adds cloud-like megakaryocytes for PMF in the smear list, and dwarf megakaryocytes for CML appear on p118–119.",
)

add(
    S7,
    113,
    "numeric",
    "What median survival does page 113 quote for PMF?",
    "5 years",
    [
        "2 years",
        "10 years",
        "15 years",
    ],
    "The management section opens with 'median survival of 5 years'.",
)

add(
    S7,
    113,
    "recall",
    "State the printed medical and definitive treatments of PMF with the transplant limitations on page 113.",
    "Medical : oral ruxolitinib (in JAK-2 mutation) and lenalidomide; definitive : allogeneic hematopoietic stem cell transplant (AHSCT), limited by needing a complete match and ↑ infection risk",
    [
        "Medical : hydroxyurea first line; definitive : splenectomy",
        "Medical : eltrombopag; definitive : autologous stem cell transplant",
        "Medical : interferon; definitive : no curative option listed",
    ],
    "Medical treatment is oral ruxolitinib in JAK-2 mutation plus lenalidomide; definitive treatment is AHSCT with limitations complete match required and ↑ risk of infection.",
)

add(
    S7,
    113,
    "truefalse",
    "Judge the page 113 PMF statements as printed.",
    "True — The bone marrow aspirate in PMF is a dry tap",
    [
        "True — Silver impregnation of the biopsy demonstrates reticulin fibrosis ± collagen fibrosis",
        "False — Leukoerythroblastosis with teardrop cells is part of the PMF peripheral smear picture",
        "False — Allogeneic HSCT is listed as the definitive treatment of PMF",
    ],
    "All four printed facts hold (dry tap, silver impregnation reticulin ± collagen fibrosis, teardrop leukoerythroblastosis, AHSCT definitive), so the 'False' framings contradict page 113.",
)

# ==============================================================================
# UNIT 8 — Page 114: essential thrombocytosis
# ==============================================================================

add(
    S8,
    114,
    "recall",
    "How does page 114 characterize essential thrombocytosis overall?",
    "Benign disease with good prognosis",
    [
        "Aggressive disease with poor prognosis",
        "Premalignant disease invariably transforming to AML",
        "Self-limiting reactive phenomenon",
    ],
    "The opening line prints 'Benign disease : Good prognosis'.",
)

add(
    S8,
    114,
    "match",
    "Match the ET mutation with its printed frequency on page 114 — 1) JAK-2 2) CALR 3) MPL … A) 50–60% B) 30–40% C) 10–20%",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "ET etiology prints JAK-2 mutation (50-60%), CALR mutation (30-40%) and MPL mutation (10-20%).",
)

add(
    S8,
    114,
    "recall",
    "Which clinical features of ET are printed on page 114?",
    "Mild splenomegaly; thrombosis (D/t hyperplasia) > bleeding (D/t dysplastic cells); female > male",
    [
        "Massive splenomegaly; bleeding > thrombosis; male > female",
        "Mild splenomegaly; bleeding > thrombosis; male = female",
        "No splenomegaly; thrombosis only; female > male",
    ],
    "Clinical features print mild splenomegaly, thrombosis (D/t hyperplasia) > bleeding (D/t dysplastic cells), and gender female > male.",
)

add(
    S8,
    114,
    "numeric",
    "What platelet count threshold defines ET on page 114?",
    ">4.5 lakhs",
    [
        ">2.5 lakhs",
        ">6.5 lakhs",
        ">10 lakhs",
    ],
    "Investigations print PLC : >4.5 lakhs with RBC and WBC normal.",
)

add(
    S8,
    114,
    "recall",
    "How are the megakaryocytes described in the ET bone marrow biopsy on page 114?",
    "Hyperplasia (few dysplastic) with staghorn cells — giant cells having mature cytoplasm and hyperlobulated nuclei",
    [
        "Hypoplasia with dwarf megakaryocytes",
        "Hyperplasia with monolobated micromegakaryocytes",
        "Clusters of immature blastic megakaryocytes",
    ],
    "The biopsy prints megakaryocyte hyperplasia (few dysplastic) and staghorn cells defined as giant cells with mature cytoplasm, hyperlobulated nuclei.",
)

add(
    S8,
    114,
    "match",
    "Match the page 114 image captions with their photographs — 1) 'Bone marrow biopsy with ↑ megakaryocyte' 2) 'Hyperlobulated nuclei of megakaryocyte' 3) 'Megakaryocyte in bone marrow of aspirate' … A) Biopsy field crowded with megakaryocytes B) High-power view of a hyperlobulated nucleus C) Aspirate film showing a megakaryocyte",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The three captions print exactly as listed on page 114.",
)

add(
    S8,
    114,
    "recall",
    "What does page 114 say about the risk of conversion of ET to myelofibrosis and to AML?",
    "Least risk of conversion to myelofibrosis; AML conversion order PCRV > PMF > ET",
    [
        "Highest risk of conversion to myelofibrosis; AML order ET > PMF > PCRV",
        "No risk of myelofibrosis; AML order PMF > PCRV > ET",
        "Least risk of AML but highest risk of myelofibrosis",
    ],
    "Complications print least risk of conversion to myelofibrosis and AML (PCRV > PMF > ET).",
)

add(
    S8,
    114,
    "truefalse",
    "Assess the page 114 ET statements as printed.",
    "True — In ET the RBC and WBC counts are normal while the platelet count exceeds 4.5 lakhs",
    [
        "True — Thrombosis outweighs bleeding in ET because hyperplasia drives clotting while dysplastic cells cause lesser bleeding",
        "False — Staghorn cells in ET are giant cells with mature cytoplasm and hyperlobulated nuclei",
        "False — ET carries the least risk of conversion to myelofibrosis among the MPNs",
    ],
    "All printed facts hold (normal RBC/WBC with PLC >4.5 lakhs, thrombosis > bleeding, staghorn definition, least myelofibrosis conversion), so the 'False' framings contradict page 114.",
)

# ==============================================================================
# UNIT 9 — Page 115: ET evaluation and management
# ==============================================================================

add(
    S9,
    115,
    "recall",
    "Why is ET called a diagnosis by exclusion on page 115, and which two exclusions are printed?",
    "Rule out reactive thrombocytosis (normal RBC and WBC; response to inflammation) and rule out other MPN/MDS (JAK-2 mutation, calreticulin, MPL)",
    [
        "Rule out iron deficiency and sepsis only",
        "Rule out ITP and TTP via staghorn cells",
        "Rule out CML by LAP score alone",
    ],
    "Evaluation prints diagnosis by exclusion: rule out reactive thrombocytosis (normal RBC and WBC, response to inflammation) and rule out other MPN/MDS using JAK-2 mutation, calreticulin, MPL.",
)

add(
    S9,
    115,
    "fillup",
    "Reactive thrombocytosis on page 115 is described as a response to ______, with normal RBC and WBC.",
    "inflammation",
    [
        "hemorrhage",
        "splenectomy",
        "malignancy",
    ],
    "The exclusion box prints '(Response to inflammation)' beside reactive thrombocytosis.",
)

add(
    S9,
    115,
    "management",
    "A 40-year-old ET patient without thrombosis is low risk per page 115. What is printed?",
    "Aspirin 75 mg/day",
    [
        "Aspirin + hydroxyurea immediately",
        "Interferon first line",
        "Anagrelide monotherapy",
    ],
    "The low-risk arm (<60 yrs) is aspirin 75 mg/day.",
)

add(
    S9,
    115,
    "management",
    "A 65-year-old ET patient with prior thrombosis and platelets above 1.5 × 10⁶ is high risk per page 115. Which cytoreductive hierarchy is printed alongside aspirin?",
    "Hydroxyurea > interferon > anagrelide",
    [
        "Anagrelide > interferon > hydroxyurea",
        "Interferon > hydroxyurea > anagrelide",
        "Ruxolitinib > hydroxyurea > interferon",
    ],
    "The high-risk arm (>60 yrs, h/o thrombosis, platelets >1.5 × 10⁶) prints aspirin plus hydroxyurea > interferon > anagrelide.",
)

add(
    S9,
    115,
    "numeric",
    "State the three printed high-risk criteria for ET on page 115.",
    ">60 years, history of thrombosis, and platelets >1.5 × 10⁶",
    [
        ">50 years, history of bleeding, platelets >1.0 × 10⁶",
        ">70 years, history of thrombosis, platelets >2.5 × 10⁶",
        ">60 years, splenomegaly, platelets >4.5 lakhs",
    ],
    "High risk prints >60 yrs, h/o thrombosis, platelets >1.5 × 10⁶ (as printed).",
)

add(
    S9,
    115,
    "truefalse",
    "Judge the page 115 ET evaluation statements as printed.",
    "True — Reactive thrombocytosis is excluded by noting normal RBC and WBC counts",
    [
        "True — JAK-2, calreticulin and MPL testing helps rule out other MPN/MDS",
        "False — Low-risk ET (<60 yrs) is managed with aspirin 75 mg/day",
        "False — In high-risk ET the printed cytoreductive preference is hydroxyurea over interferon over anagrelide",
    ],
    "Both exclusions and both treatment arms are exactly as printed on page 115, so the 'False' framings contradict the page.",
)


GUIDES = {
    S1: (
        "Overview: CMP Physiology, MPN Pathology and the Printed MPN List with Mutations",
        "Physiology diagram: CMP → terminal myeloid cells (RBC, platelets, monocytes, eosinophils, basophils); pathology = proliferation of mature cells of multiple lineages with no dysplastic/immature cells.\n"
        "MPN list: 1 PCRV (m/c), 2 PMF, 3 ET — bracketed under JAK-2 (PMF additionally deletion on chr 9p); 4 CML = BCR-ABL t(9;22); 5 CNL = CSF3R; 6 CEL = PDGFRA; 7 JMML and 8 MPN-NOS are BCR-ABL negative.\n"
        "Notes: 1° myelofibrosis (myelophthisis) = bone marrow failure; systemic mastocytosis (c-kit) is excluded from MPN.",
    ),
    S2: (
        "Clinical Features of MPN, Polycythemia Thresholds and Relative Polycythemia (Gaisböck's)",
        "EMH at spleen (m/c), skin, liver; splenomegaly massive in CML/PMF, moderate in PCRV, mild in ET; classical B symptoms in 20%; MPN can transform into each other or AML; MDS = ineffective proliferation → pancytopenia; MDS/MPN overlap in WHO 5th edition.\n"
        "Polycythemia table: male Hb ≥16.5 gm%/PCV 49, female ≥16/48; types relative and absolute.\n"
        "Relative polycythemia (Gaisböck's): ↓ plasma volume (dehydration) → ↑ Hb%, post-viral; investigations show normal RBC mass/TC/PLC with ↑ Hb.",
    ),
    S3: (
        "Absolute Polycythemia: Types, EPO/TC/PLC Table and Secondary Etiologies",
        "Absolute = increased RBC mass; primary (PCRV) vs secondary; table: EPO normal-to-low in PCRV vs increased in secondary; TC/PLC increased in PCRV vs normal in secondary.\n"
        "EPO = erythropoietin (cortex and outer medulla of kidney); hypoxic causes: COPD, OSAS, high altitude, CO intoxication, hepatopulmonary syndrome; renal artery stenosis separate.\n"
        "Paraneoplastic: renal carcinoma (hypernephroma), cerebellar hemangioblastoma (von Hippel-Lindau), meningioma, pheochromocytoma (pallor ⇒ malignancy), hepatoma, uterine fibroids; features headache, dizziness, hypertension in paraneoplastic patients.",
    ),
    S4: (
        "Polycythemia Rubra Vera: JAK2 Mutations and Clinical Features",
        "PCRV = m/c MPN, age 50–60, female > male; JAK-2 in 100% (exon 14 V617F 95%, exon 12 5%).\n"
        "Erythrocytosis: hyperviscosity, thrombosis arterial > venous (arterial stroke in young; venous Budd-Chiari/DVT; microvascular erythromelalgia), hypertension.\n"
        "Granulocytosis: neutrophilia, basophilia → histamine → aquagenic pruritus, ↑ transcobalamin-I → ↑ B12 binding capacity; thrombocytosis → dysfunctional platelets → bleeding (epistaxis, acquired vWD); moderate splenomegaly; hyperuricemia (↑ turnover).\n"
        "Investigations: ↑ RBC with ↓ MCV/normal MCH, low ESR (↓ rouleaux), PS microcytosis with erythrocytosis, LAP high, ↑ B12 binding capacity.",
    ),
    S5: (
        "PCRV Investigations, Diagnostic Criteria and Management; Primary Myelofibrosis Etiology",
        "Note: ↓ MCV (to conserve MCH) → no rouleaux; microcytosis list hypoxia, thalassemia, PCRV; transcobalamin from neutrophils for transport (liver, etc.).\n"
        "Criteria: major Hb >16.5 men/>16 women, marrow hypercellularity, JAK-2; minor subnormal serum EPO.\n"
        "Management: low risk <60 yrs — phlebotomy weekly (Hb 13–14) + aspirin; high risk >60 yrs/h/o thrombosis — phlebotomy + aspirin 75 mg + ruxolitinib 10 mg BD (or) hydroxyurea 0.5–2 g/day.\n"
        "PMF etiology: JAK-2 50%, CALR 30–40%, MPL (codes for thrombopoietin) 10–20%, triple negative = poor prognosis, deletion 13q.",
    ),
    S6: (
        "Primary Myelofibrosis: Pathogenesis and Clinical Features",
        "Dysplastic megakaryocytes (lack CXCR4) in hypercellular marrow release TGF-β (most potent fibrogenic cytokine) and PDGF → marrow fibrosis (↑ type-III collagen); premature-cell release → leukoerythroblastosis and pancytopenia.\n"
        "Most present in fibrotic stage; age >60; male = female; thrombosis risk PCRV > ET > PMF; B symptoms 20%; fatigue (m/c) from anemia; gout in proliferation stage.\n"
        "EMH: massive splenomegaly (75%), osteosclerosis, hepatomegaly (portal hypertension), skin febrile neutrophilic dermatosis (Sweet syndrome — note: characteristic of AML); cutaneous photos show annular lesions (A,B,D), erythematous lower-limb lesions, erythematous papules and plaques.",
    ),
    S7: (
        "Primary Myelofibrosis: Investigations and Management",
        "PS: anisopoikilocytosis with teardrop cells/dacryocytes; cloud-like megakaryocytes; serum type-III procollagen peptide increased; aspirate dry tap; biopsy silver impregnation reticulin ± collagen fibrosis with hypercellular marrow; note megakaryocytes in peripheral smear.\n"
        "Megakaryocyte glossary: staghorn ET, giant ITP, cloud-like PMF, dwarf CML.\n"
        "Median survival 5 years; medical oral ruxolitinib (JAK-2) and lenalidomide; definitive AHSCT limited by complete-match requirement and ↑ infection risk.",
    ),
    S8: (
        "Essential Thrombocytosis: Etiology, Clinical Features, Investigations and Complications",
        "Benign disease, good prognosis; JAK-2 50–60%, CALR 30–40%, MPL 10–20%; mild splenomegaly; thrombosis (hyperplasia) > bleeding (dysplastic cells); female > male.\n"
        "RBC/WBC normal, PLC >4.5 lakhs; biopsy megakaryocyte hyperplasia (few dysplastic) with staghorn cells (giant, mature cytoplasm, hyperlobulated nuclei); photos: ↑ megakaryocytes, hyperlobulated nuclei, megakaryocyte in aspirate.\n"
        "Least conversion to myelofibrosis; AML order PCRV > PMF > ET.",
    ),
    S9: (
        "Essential Thrombocytosis: Evaluation and Risk-Stratified Management",
        "Diagnosis by exclusion: rule out reactive thrombocytosis (normal RBC/WBC, response to inflammation) and other MPN/MDS (JAK-2, calreticulin, MPL).\n"
        "Low risk <60 yrs: aspirin 75 mg/day; high risk (>60 yrs, h/o thrombosis, platelets >1.5 × 10⁶): aspirin + hydroxyurea > interferon > anagrelide.",
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
