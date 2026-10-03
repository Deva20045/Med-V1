#!/usr/bin/env python3
"""Generate Chapter 20: Myeloproliferative Neoplasms : Part 2 (Book p116–120).

Every question is anchored to a specific line, table cell, diagram label, or
flowchart step spanning uploads/01.pdf PDF128–129 (Book p116–117) and
uploads/02.pdf PDF1–3 (Book p118–120), in strict book order. Handwritten
numerals were cross-checked visually against high-zoom renders; items
reproduced verbatim from the scan are labelled "as printed".
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 20
TITLE = "Myeloproliferative Neoplasms : Part 2"
PAGES = "116-120"

S1 = "CML Pathophysiology: Myelopoiesis, BCR-ABL Molecular Genetics & the Philadelphia Chromosome"
S2 = "CML Versus AML, TKI Note, Risk Factors & Clinical Features"
S3 = "CML Investigations: Peripheral Smear, LAP, Tryptase, Cytogenetics & Bone Marrow Study"
S4 = "CML Bone Marrow Picture, Accelerated Phase (Obsolete) & Prognostic Scales"
S5 = "CML Management: Hydroxyurea, the TKI Table, Response Milestones & Monitoring"

RAW: list[tuple] = []


def add(sec: str, page: int, fmt: str, stem: str, correct: str, distractors: list[str], explanation: str) -> None:
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    rng = random.Random(20000 + CHAPTER * 10000 + len(RAW))
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
# UNIT 1 — Page 116: physiology, molecular genetics and the Ph chromosome
# ==============================================================================

add(
    S1,
    116,
    "recall",
    "Which cells does page 116 list under 'Cells of myeloid origin'?",
    "Eosinophil, basophil, RBC, platelets, monocyte",
    [
        "Eosinophil, basophil, T-cell, B-cell, monocyte",
        "Neutrophil, lymphocyte, RBC, platelets, monocyte",
        "Eosinophil, basophil, RBC, platelets, lymphocyte",
    ],
    "The physiology list prints eosinophil, basophil, RBC, platelets, monocyte.",
)

add(
    S1,
    116,
    "fillup",
    "In the myelopoiesis lines on page 116, segmented forms mature into ______, while myeloblasts become promyelocytes.",
    "mature neutrophils",
    [
        "mature eosinophils",
        "band monocytes",
        "mature lymphocytes",
    ],
    "Myelopoiesis prints 'myeloblast → Promyelocyte' and 'Segmented forms → mature neutrophils'.",
)

add(
    S1,
    116,
    "match",
    "Match each gene/element with its printed chromosomal or functional location on page 116 — 1) BCR gene 2) ABL gene 3) Myristoyl binding site (MBS) … A) Long arm of chromosome 22 B) Long arm of chromosome 9 C) Autoinhibits ABL kinase",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Molecular genetics prints the BCR gene on the long arm of ch 22, the ABL gene on the long arm of ch 9, and the myristoyl binding site (MBS) as the element that autoinhibits ABL kinase.",
)

add(
    S1,
    116,
    "recall",
    "How is the BCR-ABL translocation characterized on page 116, and in which cells is it seen?",
    "Balanced reciprocal (pair) translocation, seen in 100% — myeloid cells > B-cells > T-cells",
    [
        "Unbalanced deletion, seen in 95% — T-cells > B-cells > myeloid cells",
        "Balanced reciprocal translocation, seen only in myeloid cells",
        "Reciprocal inversion, seen in 100% of B-cells only",
    ],
    "Pathology prints BCR-ABL translocation as a balanced reciprocal (pair) translocation seen in 100%, ordered myeloid cells > B-cells > T-cells.",
)

add(
    S1,
    116,
    "recall",
    "Onto which BCR exons does the ABL exon land in the printed translocation on page 116?",
    "Exon 13/14 of BCR",
    [
        "Exon 1/2 of BCR",
        "Exon 9/22 of BCR",
        "Exon 21/22 of BCR",
    ],
    "The scan prints the ABL exon balanced reciprocal translocation onto exon 13/14 of BCR.",
)

add(
    S1,
    116,
    "recall",
    "What is the Philadelphia (Ph) chromosome on page 116, and in what percentage of cases is it seen?",
    "Shortening of the long arm of chromosome 22; seen in 95% of cases",
    [
        "Shortening of the long arm of chromosome 9; seen in 100% of cases",
        "Lengthening of the short arm of chromosome 22; seen in 95% of cases",
        "Shortening of the long arm of chromosome 22; seen in 50% of cases",
    ],
    "The Ph chromosome is the shortening of the long arm of chromosome 22, seen in 95% of cases (the translocation itself is in 100%).",
)

add(
    S1,
    116,
    "recall",
    "Sequence the molecular consequences of the absent myristoyl binding site as printed on page 116.",
    "Absent MBS → constitutively active ABL kinase → acts as docking site of ATP → tyrosine phosphorylation",
    [
        "Absent MBS → suppressed ABL kinase → GTP docking → serine phosphorylation",
        "Present MBS → constitutively active ABL kinase → ATP docking → tyrosine phosphorylation",
        "Absent MBS → constitutively active BCR serine kinase → ATP docking → lipid phosphorylation",
    ],
    "The cascade prints absent myristoyl binding site → constitutively activate ABL kinase → act as docking site of ATP → tyrosine phosphorylation.",
)

add(
    S1,
    116,
    "oddoneout",
    "Page 116 makes several statements about the BCR-ABL lesion. Pick the ODD ONE OUT — the statement NOT as printed:",
    "The BCR-ABL translocation is seen in 95% of myeloid cells",
    [
        "The BCR-ABL translocation is a balanced reciprocal (pair) translocation",
        "The Ph chromosome (shortened long arm of chromosome 22) is seen in 95% of cases",
        "Loss of the myristoyl binding site constitutively activates ABL kinase",
    ],
    "The translocation is printed in 100% (myeloid > B > T); it is the Ph chromosome that is seen in 95% — so the 95%-of-myeloid-cells framing is the odd one out.",
)

add(
    S1,
    116,
    "truefalse",
    "Judge the page 116 molecular statements as printed.",
    "True — The myristoyl binding site normally autoinhibits ABL kinase",
    [
        "True — The constitutively active ABL kinase acts as a docking site for ATP, driving tyrosine phosphorylation",
        "False — The ABL gene sits on the long arm of chromosome 9",
        "False — The BCR gene sits on the long arm of chromosome 22",
    ],
    "All four printed facts hold (MBS autoinhibition, ATP docking/tyrosine phosphorylation, ABL on 9q, BCR on 22q), so the 'False' framings contradict page 116.",
)

# ==============================================================================
# UNIT 2 — Page 117: CML vs AML, TKI note, risk factors, clinical features
# ==============================================================================

add(
    S2,
    117,
    "match",
    "Match the printed CML-versus-AML comparison on page 117 — 1) Differentiation of myeloblast in CML 2) Differentiation of myeloblast in AML 3) Proliferation in CML 4) Proliferation in AML … A) Fairly normal B) Complete arrest C) High (multiple lineage) D) Very high (single lineage)",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-B, 3-D, 4-C",
        "1-C, 2-D, 3-A, 4-B",
    ],
    "The comparison table prints CML differentiation fairly normal versus AML complete arrest, and CML proliferation high (multiple lineage) versus AML very high (single lineage).",
)

add(
    S2,
    117,
    "recall",
    "Which extramedullary hematopoiesis feature tops page 117 for CML?",
    "Massive splenomegaly",
    [
        "Hepatomegaly with portal hypertension",
        "Generalized lymphadenopathy",
        "Cutaneous leukemic infiltrates",
    ],
    "The line reads 'Extramedullary hematopoiesis : massive splenomegaly'.",
)

add(
    S2,
    117,
    "recall",
    "Which tyrosine kinase inhibitor is noted on page 117 as acting on the myristoyl binding site (MBS)?",
    "Asciminib",
    [
        "Imatinib",
        "Dasatinib",
        "Ponatinib",
    ],
    "The margin note prints '…atinib, Asciminib (Acts on MBS)' — asciminib is the MBS-acting agent.",
)

add(
    S2,
    117,
    "recall",
    "List the printed risk factors for CML on page 117.",
    "Age 50–70 years; male > female; high-dose ionizing radiation (6–8 years); germ line susceptibility very low",
    [
        "Age 20–40 years; female > male; benzene exposure; germ line susceptibility high",
        "Age 50–70 years; male = female; alkylator exposure; germ line susceptibility moderate",
        "Any age; male > female; viral exposure; germ line susceptibility very high",
    ],
    "Risk factors print age 50-70 yrs, gender male > female, high-dose ionizing radiation (6-8 years), and germ line susceptibility very low.",
)

add(
    S2,
    117,
    "numeric",
    "What 5-year survival rate does page 117 quote for CML?",
    "85–90%",
    [
    "55–60%",
    "70–75%",
    "95–100%",
    ],
    "The line prints '5 year survival rate : 85-90 %'.",
)

add(
    S2,
    117,
    "recall",
    "What is the most common presentation of the CML chronic phase on page 117?",
    "Asymptomatic leukocytosis (WBC ~ 1 lakh)",
    [
        "Symptomatic hyperviscosity at presentation",
        "Blast crisis at diagnosis",
        "Isolated massive splenomegaly without leukocytosis",
    ],
    "Chronic phase prints asymptomatic leukocytosis (WBC ~ 1 lakh) as m/c presentation.",
)

add(
    S2,
    117,
    "recall",
    "How does page 117 explain fatigue in CML?",
    "D/t anemia — cytokines act on the colony forming unit → ↓ RBC",
    [
        "D/t hyperviscosity slowing cerebral flow",
        "D/t hypothyroidism from marrow infiltration",
        "D/t iron sequestration by hepcidin",
    ],
    "Fatigue is printed as D/t anemia (cytokines act on colony forming unit → ↓ RBC).",
)

add(
    S2,
    117,
    "recall",
    "Which symptom cluster does page 117 attach to massive splenomegaly in CML?",
    "Abdominal distension, left upper quadrant and shoulder pain, early satiety and loss of appetite",
    [
        "Right upper quadrant pain, jaundice and pruritus",
        "Diffuse bone pain with fever only",
        "Dyspnea, orthopnea and paroxysmal nocturnal dyspnea",
    ],
    "Massive splenomegaly lists abdominal distension, left upper quadrant and shoulder pain, early satiety and loss of appetite.",
)

add(
    S2,
    117,
    "recall",
    "Define blast crisis as printed on page 117, and state its natural history in untreated disease.",
    "Blast ≥20% in blood/marrow; presents within 4 years in untreated CML cases, with extramedullary blast proliferation",
    [
        "Blast ≥10% in blood/marrow; presents within 10 years even when treated",
        "Blast ≥20% in marrow only; presents within 1 year in all cases",
        "Blast ≥30% in blood; only after TKI failure",
    ],
    "Blast crisis prints blast ≥20% in blood/marrow, present within 4 years in untreated CML cases, with extramedullary blast proliferation (bone pain, bleeding ↓ PLC, unexplained fever).",
)

add(
    S2,
    117,
    "recall",
    "What causes acute gouty arthritis in CML per page 117?",
    "Hyperuricemia from ↑ cell turnover",
    [
        "Renal urate retention from tumor lysis therapy",
        "Calcium pyrophosphate deposition",
        "Septemic arthritis from neutrophil dysfunction",
    ],
    "The bullet prints acute gouty arthritis : hyperuricemia (↑ cell turnover).",
)

add(
    S2,
    117,
    "recall",
    "Which mechanism explains acne/urticaria/pruritis in CML on page 117?",
    "↑ basophils with histamine release",
    [
        "↑ eosinophils with major basic protein",
        "↑ monocytes with interleukin-1",
        "↑ platelets with serotonin release",
    ],
    "The bullet prints acne/urticaria/pruritis : ↑ basophils (histamine release).",
)

add(
    S2,
    117,
    "numeric",
    "At what WBC threshold do hyperviscosity symptoms appear on page 117, and which symptoms are listed?",
    "WBC > 2 lakh — headache, blurring of vision, priapism, vertigo",
    [
        "WBC > 1 lakh — tinnitus, deafness, stupor",
        "WBC > 4 lakh — headache, blurring of vision, priapism, vertigo",
        "WBC > 2 lakh — only visual blurring",
    ],
    "The note prints 'If WBC > 2 lakh → Symptoms of hyperviscosity : Headache, blurring of vision, priapism, vertigo'.",
)

add(
    S2,
    117,
    "recall",
    "What percentage and caveat does page 117 give for B symptoms in CML?",
    "10–15% (fever, weight loss, night sweats); classically seen in Hodgkin's disease",
    [
        "20–25%; classically seen in multiple myeloma",
        "10–15%; classically seen in non-Hodgkin's lymphoma",
        "5%; classically seen in tuberculosis only",
    ],
    "B-symptoms (10-15%) print fever, weight loss, night sweats with the note 'Classically seen in Hodgkin's disease'.",
)

add(
    S2,
    117,
    "truefalse",
    "Assess the page 117 clinical statements as printed.",
    "True — Blast crisis is defined as ≥20% blasts in blood or marrow and appears within 4 years in untreated CML",
    [
        "True — Massive splenomegaly causes early satiety, abdominal distension and left upper quadrant/shoulder pain",
        "False — Asymptomatic leukocytosis (WBC ~ 1 lakh) is the most common chronic-phase presentation",
        "False — The 5-year survival rate printed for CML is 85–90%",
    ],
    "All printed facts hold, so the two 'False' framings contradict page 117.",
)

# ==============================================================================
# UNIT 3 — Page 118: investigations
# ==============================================================================

add(
    S3,
    118,
    "recall",
    "Summarize the red and white cell findings of the CML peripheral smear on page 118.",
    "RBC : anemia; ↑ WBC (lakh); blast forms <5%; all stages seen with myelocyte maximum (myelocyte bulge) — a granulocyte left shift",
    [
        "RBC : polycythemia; ↓ WBC; blast forms >20%; only mature forms seen",
        "RBC : anemia; ↑ WBC; blast forms <5%; maturation gap with absent myelocytes",
        "RBC : normal; ↑ WBC; blast forms 10–19%; promyelocyte maximum",
    ],
    "The smear prints anemia, ↑ WBC (lakh), blast forms <5%, all stages seen, myelocyte (maximum) as the myelocyte bulge — i.e. a granulocyte left shift.",
)

add(
    S3,
    118,
    "recall",
    "Which additional lineage and platelet findings accompany the CML smear on page 118?",
    "Eosinophilia, basophilia and thrombocytosis (no hemorrhage/thrombosis)",
    [
        "Eosinopenia, basopenia and thrombocytopenia with bleeding",
        "Eosinophilia only, with normal platelets and bleeding",
        "Basophilia only, with thrombocytosis causing thrombosis",
    ],
    "The smear adds eosinophilia, basophilia and thrombocytosis (No hemorrhage/thrombosis).",
)

add(
    S3,
    118,
    "recall",
    "What does page 118 say about the leukocyte alkaline phosphatase (LAP) in CML, and where else is a low LAP score seen?",
    "LAP is low (cytochemical abnormal WBC); a low LAP score is seen in PNH and CML",
    [
        "LAP is high; low LAP is seen in leukemoid reactions",
        "LAP is low; low LAP is seen only in sepsis",
        "LAP is normal; low LAP is seen in ET",
    ],
    "Item 2 prints LAP (leukocyte alkaline phosphatase) : low (cytochemical abnormal WBC), with the note 'Low LAP score (Seen in PNH, CML)'.",
)

add(
    S3,
    118,
    "recall",
    "Which enzyme is increased on page 118 as a marker of hematological neoplasm?",
    "Tryptase",
    [
        "Lactate dehydrogenase isoenzyme-1",
        "Adenosine deaminase",
        "Terminal deoxynucleotidyl transferase",
    ],
    "Item 3 prints 'Tryptase : Increased' with the note 'Diagnosis of hematological neoplasm'.",
)

add(
    S3,
    118,
    "match",
    "Match each laboratory approach with its printed technique on page 118 — 1) Cytology (morphology) 2) Immunophenotyping 3) Conventional karyotyping (G-banding) 4) FISH … A) Smear B) Flow cytometry C) Cell in metaphase D) Cell in interphase",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-B, 3-D, 4-C",
        "1-C, 2-D, 3-A, 4-B",
    ],
    "The methods diagram pairs cytology with the smear, immunophenotyping with flow cytometry, G-banding with the cell in metaphase, and FISH with the cell in interphase.",
)

add(
    S3,
    118,
    "recall",
    "What are items 4 and 5 of the page 118 investigation list used for?",
    "Cytogenetics detects the BCR-ABL gene t(9;22); molecular genetics gives quantitative BCR-ABL",
    [
        "Cytogenetics quantifies blasts; molecular genetics detects PNH clones",
        "Cytogenetics detects CALR; molecular genetics detects JAK-2",
        "Cytogenetics stages fibrosis; molecular genetics monitors LAP",
    ],
    "Item 4 prints cytogenetics to detect BCR-ABL gene t(9;22) and item 5 molecular genetics for quantitative BCR-ABL.",
)

add(
    S3,
    118,
    "recall",
    "List the printed indications of the bone marrow study in CML on page 118.",
    "Conventional karyotyping (mandatory) to rule out additional abnormality (double Ph, trisomy 8, isochromosome 17, deletion of 20q); quantify blasts; determine degree of fibrosis",
    [
        "Optional karyotyping; quantify eosinophils; assess iron stores",
        "FISH only for Ph; quantify reticulocytes; grade dysplasia",
        "Mandatory FISH only; quantify platelets; assess hemophagocytosis",
    ],
    "Indications print conventional karyotyping (mandatory) to rule out additional abnormality (double Ph, trisomy 8, isochromosome 17, deletion of 20q), quantify blasts, and determine degree of fibrosis.",
)

add(
    S3,
    118,
    "oddoneout",
    "Page 118 lists additional cytogenetic abnormalities to rule out in CML. Pick the ODD ONE OUT — the lesion NOT on that list:",
    "Trisomy 12",
    [
        "Double Ph",
        "Trisomy 8 and isochromosome 17",
        "Deletion of 20q",
    ],
    "The printed additional abnormalities are double Ph, trisomy 8, isochromosome 17 and deletion of 20q; trisomy 12 is not listed.",
)

add(
    S3,
    118,
    "recall",
    "What do the two FISH images and the megakaryocyte note on page 118 show?",
    "FISH signals for normal cells versus BCR-ABL+ cells, and dwarf megakaryocytes in the marrow",
    [
        "FISH for PNH clones and giant megakaryocytes",
        "G-banding of normal cells and cloud-like megakaryocytes",
        "FISH for JAK-2 and staghorn megakaryocytes",
    ],
    "The images print FISH : normal cells and FISH : BCR-ABL+ cells, with dwarf megakaryocytes labelled in the marrow picture.",
)

add(
    S3,
    118,
    "truefalse",
    "Judge the page 118 investigation statements as printed.",
    "True — The CML smear shows all maturation stages with a myelocyte bulge and blasts <5%",
    [
        "True — Tryptase is increased and serves as a diagnosis of hematological neoplasm",
        "False — A low LAP score is seen in PNH and CML",
        "False — Molecular genetics is used for quantitative BCR-ABL",
    ],
    "All printed facts hold, so the 'False' framings contradict page 118.",
)

# ==============================================================================
# UNIT 4 — Page 119: bone marrow picture, accelerated phase, prognosis
# ==============================================================================

add(
    S4,
    119,
    "recall",
    "Summarize the CML bone marrow aspirate findings on page 119.",
    "Marked hypercellularity; increased dwarf megakaryocytes; predominant granulopoiesis (30 : 1); decreased erythropoiesis; sea-blue histiocytes (Gaucher cells); fibrosis",
    [
        "Marked hypocellularity; decreased megakaryocytes; predominant erythropoiesis; absent fibrosis",
        "Hypercellularity with increased erythropoiesis and absent megakaryocytes",
        "Normocellular marrow with lymphoid aggregates and no fibrosis",
    ],
    "The aspirate prints marked hypercellularity, predominant granulopoiesis (30:1), decreased erythropoiesis, increased dwarf megakaryocytes, sea-blue histiocytes (Gaucher cells) and fibrosis.",
)

add(
    S4,
    119,
    "recall",
    "What do the Wright-Giemsa-stained images on page 119 demonstrate?",
    "Blast >20% (crisis image), hypercellular marrow with trilineage hematopoiesis (↑ myeloid, eosinophilia, plasmacytosis), sea-blue histiocytosis, and G-banding",
    [
        "Blast <5%, fatty marrow, no histiocytosis",
        "Blast 10–19%, erythroid-predominant marrow, FISH only",
        "Blast >20% but hypocellular marrow with absent megakaryocytes",
    ],
    "The image labels print blast >20%, hypercellular marrow with trilineage hematopoiesis (↑ myeloid, eosinophilia, plasmacytosis), sea-blue histiocytosis and G-banding.",
)

add(
    S4,
    119,
    "fillup",
    "The sea-blue histiocytes on page 119 are equated with ______ cells.",
    "Gaucher",
    [
        "Niemann-Pick",
        "Hodgkin Reed-Sternberg",
        "osteoclast",
    ],
    "The parenthetical reads '(Gaucher cells)'.",
)

add(
    S4,
    119,
    "oddoneout",
    "The accelerated phase (obsolete) on page 119 lists several criteria. Pick the ODD ONE OUT — the item NOT part of that list:",
    "Blasts ≥20% in blood or marrow",
    [
        "Basophilia ≥20%",
        "Blasts 10–19%",
        "Thrombocytosis unresponsive to therapy or thrombocytopenia uncontrolled by therapy",
    ],
    "The obsolete accelerated phase prints basophilia ≥20%, blasts 10–19%, therapy-unresponsive thrombocytosis, therapy-uncontrolled thrombocytopenia and persistent/increased WBC; blasts ≥20% defines blast crisis (p117), not the accelerated phase.",
)

add(
    S4,
    119,
    "recall",
    "Which two obsolete prognostic methods does page 119 name, and why are they obsolete?",
    "Sokal index and Hasford prognostic scale — no longer relevant due to the emergence of TKIs",
    [
        "ELN score and EUTOS score — replaced by FISH",
        "Sokal index and IPSS — replaced by PCR",
        "Hasford scale and IPSS-R — replaced by flow cytometry",
    ],
    "Obsolete methods print 1. Hasford prognostic scale and 2. Sokal index, 'No longer relevant due to emergence of TKIs'.",
)

add(
    S4,
    119,
    "recall",
    "Which five parameters (a–e) does page 119 list beside the prognostic scales?",
    "Circulating blasts, spleen size, platelet count, age, and eosinophils and basophils in blood",
    [
        "Circulating blasts, liver size, hemoglobin, age, and reticulocytes",
        "Blasts in marrow, spleen size, platelet count, sex, and basophils only",
        "Circulating blasts, spleen size, LDH, age, and eosinophils only",
    ],
    "The list prints a. circulating blasts, b. spleen size, c. platelet count, d. age, e. eosinophils and basophils in blood.",
)

add(
    S4,
    119,
    "numeric",
    "What granulopoiesis ratio does the page 119 aspirate print for CML?",
    "30 : 1",
    [
        "3 : 1",
        "10 : 1",
        "30 : 10",
    ],
    "The line reads 'Predominant granulopoiesis (30 : 1)'.",
)

add(
    S4,
    119,
    "truefalse",
    "Assess the page 119 marrow statements as printed.",
    "True — Erythropoiesis is decreased while granulopoiesis predominates in the CML marrow",
    [
        "True — Dwarf megakaryocytes are increased in the CML marrow",
        "False — The accelerated phase (basophilia ≥20%, blasts 10–19%) is labelled obsolete on page 119",
        "False — Sea-blue histiocytes equated with Gaucher cells appear in the CML marrow picture",
    ],
    "All printed facts hold, so the 'False' framings contradict page 119.",
)

# ==============================================================================
# UNIT 5 — Page 120: management, TKI table, outcomes
# ==============================================================================

add(
    S5,
    120,
    "recall",
    "What role does hydroxyurea play in the page 120 CML management?",
    "To ↓ cell turnover",
    [
        "To induce differentiation of blasts",
        "To inhibit the BCR-ABL kinase directly",
        "To chelate iron from transfusions",
    ],
    "Management opens with 'Hydroxyurea : To ↓ cell turnover'.",
)

add(
    S5,
    120,
    "match",
    "Match each TKI with its printed dose on page 120 — 1) Imatinib 2) Bosutinib 3) Nilotinib 4) Dasatinib … A) 400 mg (chronic phase) / 600–800 mg (blast crisis) B) 500 mg/day C) 300 mg BD D) 100 mg/day",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-C, 3-B, 4-D",
        "1-D, 2-B, 3-C, 4-A",
    ],
    "The TKI table prints imatinib 400 mg chronic phase / 600–800 mg blast crisis, bosutinib 500 mg/day, nilotinib 300 mg BD and dasatinib 100 mg/day.",
)

add(
    S5,
    120,
    "match",
    "Match each TKI with its printed side-effect profile on page 120 — 1) Imatinib 2) Bosutinib 3) Nilotinib 4) Dasatinib … A) Hypopigmentation, periorbital edema, muscle cramps B) Colitis C) Peripheral vascular disease, pancreatitis D) Pleural effusion, pericardial effusion, periorbital edema, pulmonary hypertension",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-D, 4-C",
        "1-A, 2-C, 3-B, 4-D",
        "1-D, 2-B, 3-C, 4-A",
    ],
    "The side-effect column prints imatinib hypopigmentation/periorbital edema/muscle cramps, bosutinib colitis, nilotinib peripheral vascular disease/pancreatitis, and dasatinib pleural/pericardial effusion, periorbital edema and pulmonary hypertension.",
)

add(
    S5,
    120,
    "recall",
    "Which TKIs does page 120 group as the second generation, and for what indication?",
    "Bosutinib, nilotinib and dasatinib — for TK domain mutation",
    [
        "Imatinib and bosutinib — for chronic phase only",
        "Ponatinib and asciminib — for TK domain mutation",
        "Nilotinib and ponatinib — for T315I mutation",
    ],
    "The IInd generation row (For TK domain mutation) lists bosutinib, nilotinib and dasatinib.",
)

add(
    S5,
    120,
    "recall",
    "Which agents does page 120 reserve for the T315I mutation, and what does the table print for their doses/side effects?",
    "Ponatinib (45 mg/day) and asciminib; asciminib's dose/side effects print as '—'",
    [
        "Dasatinib and bosutinib; no doses printed",
        "Ponatinib (100 mg/day) and imatinib; both with full side-effect lists",
        "Asciminib alone at 45 mg/day",
    ],
    "The 'For T315I mutation' row prints ponatinib 45 mg/day and asciminib with a dash for dose/side effects; asciminib acts on MBS (p117 note).",
)

add(
    S5,
    120,
    "numeric",
    "What imatinib dose does page 120 print for blast crisis?",
    "600–800 mg",
    [
        "400 mg",
        "500 mg",
        "1000 mg",
    ],
    "Imatinib prints 400 mg for chronic phase and 600–800 mg for blast crisis.",
)

add(
    S5,
    120,
    "scenario",
    "A CML patient on a second-generation TKI develops a pleural effusion and pulmonary hypertension. Per the page 120 table, which drug is the culprit?",
    "Dasatinib",
    [
        "Nilotinib",
        "Bosutinib",
        "Imatinib",
    ],
    "Pleural effusion, pericardial effusion, periorbital edema and pulmonary hypertension are the printed dasatinib side effects; nilotinib causes peripheral vascular disease/pancreatitis and bosutinib colitis.",
)

add(
    S5,
    120,
    "recall",
    "What does a complete cytogenetic response (CCR) at 6 months mean on page 120, and why does it matter?",
    "Cytogenetics shows no Philadelphia chromosome on bone marrow aspiration; it is the most important predictor of long-term survival",
    [
        "PCR shows BCR-ABL <0.1% on peripheral blood; it predicts only short-term response",
        "Smear shows <5% blasts; it predicts hematologic remission only",
        "FISH turns negative in lymph nodes; it predicts transplant success",
    ],
    "Outcome prints complete cytogenic response (CCR) in 6 months = cytogenetics with no Philadelphia chromosome on bone marrow aspiration, the most important predictor of long-term survival.",
)

add(
    S5,
    120,
    "match",
    "Match the printed molecular-response milestones (DNA PCR quantifying BCR-ABL) on page 120 — 1) 3 months 2) 6 months 3) 1 year … A) <10% B) <1% C) <0.1% (major molecular response)",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Molecular response milestones print 3 months <10%, 6 months <1%, and 1 year <0.1% (major molecular response).",
)

add(
    S5,
    120,
    "numeric",
    "What BCR-ABL threshold defines the major molecular response at 1 year on page 120?",
    "<0.1%",
    [
        "<1%",
        "<10%",
        "Undetectable",
    ],
    "The 1-year milestone prints <0.1% (major molecular response).",
)

add(
    S5,
    120,
    "recall",
    "Besides molecular milestones, what does page 120 list under outcome monitoring?",
    "Platelet count, smear, no symptoms",
    [
        "Hemoglobin, reticulocytes, spleen size",
        "LAP score, tryptase, uric acid",
        "WBC differential, LDH, β2-microglobulin",
    ],
    "The outcome line prints platelet count, smear, no symptoms.",
)

add(
    S5,
    120,
    "truefalse",
    "Judge the page 120 management statements as printed.",
    "True — Imatinib 400 mg is the chronic-phase dose while 600–800 mg is reserved for blast crisis",
    [
        "True — Achieving a complete cytogenetic response in 6 months is the most important predictor of long-term survival",
        "False — The major molecular response at 1 year corresponds to BCR-ABL <0.1% by DNA PCR",
        "False — Ponatinib 45 mg/day is the printed agent for the T315I mutation",
    ],
    "All printed facts hold, so the 'False' framings contradict page 120.",
)


GUIDES = {
    S1: (
        "CML Pathophysiology: Myelopoiesis, BCR-ABL Molecular Genetics & the Philadelphia Chromosome",
        "Myeloid origin cells: eosinophil, basophil, RBC, platelets, monocyte; myelopoiesis myeloblast → promyelocyte, segmented forms → mature neutrophils.\n"
        "BCR on long arm of ch 22; ABL on long arm of ch 9; MBS autoinhibits ABL kinase.\n"
        "Pathology: balanced reciprocal (pair) BCR-ABL translocation in 100% (myeloid > B > T), ABL exon onto BCR exon 13/14; Ph chromosome = shortened long arm of ch 22 in 95%; absent MBS → constitutively active ABL kinase → ATP docking → tyrosine phosphorylation.",
    ),
    S2: (
        "CML Versus AML, TKI Note, Risk Factors & Clinical Features",
        "CML vs AML: differentiation fairly normal vs complete arrest; proliferation high (multiple lineage) vs very high (single lineage); EMH massive splenomegaly; asciminib acts on MBS.\n"
        "Risk factors: age 50–70, male > female, high-dose ionizing radiation (6–8 years), germ line susceptibility very low; 5-year survival 85–90%.\n"
        "Chronic phase: asymptomatic leukocytosis (WBC ~1 lakh, m/c), fatigue D/t anemia, massive splenomegaly symptoms, gouty arthritis (↑ turnover), basophil histamine skin signs; blast crisis ≥20% within 4 years untreated; WBC >2 lakh → hyperviscosity (headache, blurred vision, priapism, vertigo); B symptoms 10–15% (classically Hodgkin's).",
    ),
    S3: (
        "CML Investigations: Peripheral Smear, LAP, Tryptase, Cytogenetics & Bone Marrow Study",
        "Smear: anemia, ↑ WBC (lakh), blasts <5%, all stages with myelocyte bulge (left shift), eosinophilia, basophilia, thrombocytosis without hemorrhage/thrombosis.\n"
        "LAP low (low LAP in PNH, CML); tryptase increased (hematological neoplasm); cytology = smear, immunophenotyping = flow cytometry, G-banding = metaphase, FISH = interphase; cytogenetics for t(9;22), molecular for quantitative BCR-ABL.\n"
        "BM study: mandatory conventional karyotyping to rule out additional abnormality (double Ph, trisomy 8, isochromosome 17, del 20q), quantify blasts, grade fibrosis; FISH images normal vs BCR-ABL+; dwarf megakaryocytes.",
    ),
    S4: (
        "CML Bone Marrow Picture, Accelerated Phase (Obsolete) & Prognostic Scales",
        "Aspirate: marked hypercellularity, granulopoiesis (30:1), ↓ erythropoiesis, ↑ dwarf megakaryocytes, sea-blue histiocytes (Gaucher cells), fibrosis; images: blast >20%, trilineage hypercellular marrow, sea-blue histiocytosis, G-banding.\n"
        "Accelerated phase (obsolete): basophilia ≥20%, blasts 10–19%, therapy-unresponsive thrombocytosis, uncontrolled thrombocytopenia, persistent/increased WBC.\n"
        "Obsolete prognosis: Hasford scale and Sokal index (irrelevant post-TKIs) with parameters a–e (circulating blasts, spleen size, platelet count, age, eosinophils/basophils).",
    ),
    S5: (
        "CML Management: Hydroxyurea, the TKI Table, Response Milestones & Monitoring",
        "Hydroxyurea ↓ cell turnover; TKI table: imatinib 400 mg chronic / 600–800 mg blast crisis (hypopigmentation, periorbital edema, muscle cramps); IInd gen for TK domain mutation — bosutinib 500 mg/day (colitis), nilotinib 300 mg BD (peripheral vascular disease, pancreatitis), dasatinib 100 mg/day (pleural/pericardial effusion, periorbital edema, pulmonary hypertension); T315I — ponatinib 45 mg/day, asciminib (—).\n"
        "Outcome: CCR in 6 months (no Ph on cytogenetics) = most important long-term survival predictor; molecular response by DNA PCR: 3 months <10%, 6 months <1%, 1 year <0.1% (MMR); monitor platelet count, smear, no symptoms.",
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
