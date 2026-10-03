#!/usr/bin/env python3
"""Generate Chapter 23: Acute Myeloid Leukemia V/S Acute Lymphoblastic Leukemia (Book p136–139).

Every question is anchored to a specific line, table cell, diagram label,
bone marrow smear caption, or flowchart step in uploads/02.pdf (PDF pages 19–22
= Book pages 136–139) in strict book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 23
TITLE = "Acute Myeloid Leukemia V/S Acute Lymphoblastic Leukemia"
PAGES = "136-139"

S1 = "ALL Pathophysiology, Survival by Age, B-Cell vs T-Cell Lineage & Lymphoblast vs Myeloblast Morphology"
S2 = "ALL Risk Factors, Presenting Features (B-ALL, T-ALL, High-Count Sanctuary Sites) & Laboratory Features"
S3 = "B-Cell Subtypes (Pro-B, Pre-B, Early Pre-B CALLA, Immature B), B-ALL vs T-ALL Clinical Features & Smear Notes"
S4 = "ALL Prognostic Factors Table, BFM-19 Treatment Protocol (Induction, MRD, Consolidation, Maintenance) & Other Drugs"

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
# UNIT 1 — Page 136: Pathophysiology, Survival, B- vs T-Cell Lineage & Lymphoblast vs Myeloblast
# ==============================================================================

add(
    S1,
    136,
    "numeric",
    "Under 'Pathophysiology' on page 136, what percentage of adult leukemias does ALL represent and what is its survival rate in adults?",
    "20% of adult leukemias : 40–45% survival",
    [
        "80% of adult leukemias : 85–90% survival across all adult age groups",
        "10% of adult leukemias : almost NIL survival even after bone marrow transplantation",
        "50% of adult leukemias : 70–75% survival with standard oral hydroxyurea monotherapy",
    ],
    "The top branch under Pathophysiology → ALL on page 136 reads: '20% of adult leukemias : 40–45% survival.'",
)

add(
    S1,
    136,
    "numeric",
    "In the 'Pathophysiology' diagram on page 136, what percentage of child/adolescent leukemias is ALL, and what are the survival rates for ages 10–19 years versus <10 years?",
    "90% of child/adolescent leukemias — 10–19 years: 70–75% survival; <10 years: 90–95% survival",
    [
        "80% of child/adolescent leukemias — 10–19 years: 90–95% survival; <10 years: 40–45% survival",
        "10% of child/adolescent leukemias — 10–19 years: 40–45% survival; <10 years: 70–75% survival",
        "75% of child/adolescent leukemias — 10–19 years: 50–55% survival; <10 years: 60–65% survival",
    ],
    "Under Pathophysiology → ALL on page 136, the lower branch reads: '90% of child/adolescent leukemias → 10–19 years : 70–75% survival; <10 years : 90–95% survival.'",
)

add(
    S1,
    136,
    "numeric",
    "What is the median age of patients with acute lymphoblastic leukemia (ALL) printed on page 136?",
    "13 years",
    [
        "65 years (with equal incidence across all adult decades)",
        "4 years (exclusively affecting preschool children)",
        "40–60 years (matching the Indian 5q-deletion MDS peak)",
    ],
    "Page 136 prints: 'Median age : 13 years.'",
)

add(
    S1,
    136,
    "recall",
    "In the 'Lymphoblasts' lineage diagram on page 136, what percentage of ALL is Precursor B cell ALL and what is its tissue involvement pattern?",
    "80% of ALL; only involves marrow (only leukemias)",
    [
        "20% of ALL; involves bone marrow together with an anterior mediastinal thymic mass",
        "50% of ALL; involves peripheral lymph nodes and spleen without bone marrow replacement",
        "90% of ALL; involves orbital soft tissue (chloroma) and gingival mucosa exclusively",
    ],
    "The left arm of the Lymphoblasts flowchart on page 136 shows: B cell → Precursor B cell ALL (80%) → Only involves marrow (Only leukemias).",
)

add(
    S1,
    136,
    "recall",
    "In the 'Lymphoblasts' lineage diagram on page 136, what are the percentage, prognosis, tissue involvement, and classic demographic of Precursor T cell ALL?",
    "20% of ALL; poor prognosis; involves bone marrow ± mass (leukemias/lymphomas) in thymus causing mediastinal widening and dyspnea; common in adolescent boys",
    [
        "80% of ALL; favourable prognosis; restricted strictly to bone marrow without thymic or nodal masses; common in female toddlers aged 2–5 years at presentation",
        "10% of ALL; good prognosis; involves isolated splenic red pulp and hepatic sinusoids causing portal hypertension; common in elderly women >65 years of age",
        "50% of ALL; intermediate prognosis; involves extensor forearm skin nodules and gingival hypertrophy without chest symptoms; common in infants <1 year of age",
    ],
    "The right arm of the Lymphoblasts flowchart on page 136 shows: T cell → Precursor T cell ALL (20%) → • Poor prognosis. • Involves bone marrow ± mass (Leukemias/lymphomas) in thymus → – Causes mediastinal widening, dyspnea. – Common in adolescent boys.",
)

add(
    S1,
    136,
    "fillup",
    "In the lymphoblast lineage diagram on page 136, Precursor T cell ALL (20%) involves the bone marrow ± a mass in the ______, leading to mediastinal widening and dyspnea in adolescent boys.",
    "thymus",
    [
        "orbit",
        "spleen",
        "gingiva",
    ],
    "Under Precursor T cell ALL (20%) on page 136: '• Involves bone marrow ± mass (Leukemias/lymphomas) in thymus → – Causes mediastinal widening, dyspnea. – Common in adolescent boys.'",
)

add(
    S1,
    136,
    "recall",
    "In the 'Lymphoblast vs Myeloblast' table on page 136, how do cell size, nucleoli, and cytoplasmic granules compare between a lymphoblast and a myeloblast?",
    "Lymphoblast: smaller size, nucleoli absent, granules absent; Myeloblast: larger size, nucleoli present, granules present",
    [
        "Lymphoblast: larger size, 1–4 prominent nucleoli, abundant dark granules; Myeloblast: smaller size, nucleoli absent, granules absent",
        "Lymphoblast: equal size to myeloblast, bilobed butterfly nucleus, faggot-cell Auer rod bundles; Myeloblast: clock-face chromatin without nucleoli",
        "Lymphoblast: larger size, nucleoli absent, Auer rods present; Myeloblast: smaller size, nucleoli present, granules absent",
    ],
    "Rows 1–3 of the comparison table on page 136 read: Size — Smaller (Lymphoblast) vs Larger (Myeloblast); Nucleoli — Absent vs Present; Granules — Absent vs Present.",
)

add(
    S1,
    136,
    "match",
    "In the comparison table on page 136, match each cytochemical stain with its reaction in Lymphoblast versus Myeloblast — 1) MPO (myeloperoxidase) 2) Sudan black 3) PAS (periodic acid–Schiff) 4) Acid phosphatase … A) Positive in Lymphoblast; '–' in Myeloblast (block-like glycogen positivity) B) Positive in Lymphoblast; '–' in Myeloblast (focal T-lymphoblast positivity) C) Negative in Lymphoblast; Positive in Myeloblast (peroxidase reaction) D) Negative in Lymphoblast; Positive in Myeloblast (phospholipid granule stain)",
    "1-C, 2-D, 3-A, 4-B",
    [
        "1-A, 2-B, 3-C, 4-D",
        "1-C, 2-A, 3-D, 4-B",
        "1-B, 2-D, 3-A, 4-C",
    ],
    "Rows 4–7 of the Lymphoblast vs Myeloblast table on page 136 list: MPO — Negative vs Positive; Sudan black — Negative vs Positive; PAS — Positive vs –; Acid phosphatase — Positive vs –.",
)

add(
    S1,
    136,
    "recall",
    "In the bottom schematic diagram captioned 'Myeloblast vs lymphoblast' on page 136, which four morphological labels are shown and how do they map to the two blasts?",
    "Scanty cytoplasm and Nucleoli point to both blasts, whereas Cytoplasmic granules and Auer rod point solely to the myeloblast (left cell)",
    [
        "Cytoplasmic granules and Auer rod point solely to the lymphoblast (right cell), whereas Scanty cytoplasm points only to the myeloblast",
        "Faggot-cell bundles and Heinz bodies point to the myeloblast, whereas Howell-Jolly bodies and basophilic stippling point to the lymphoblast",
        "Bilobed dumbbell nucleus and Döhle bodies point to the myeloblast, whereas Auer rods point to both the myeloblast and lymphoblast",
    ],
    "The schematic diagram 'Myeloblast vs lymphoblast' at the bottom of page 136 shows four central labels: 'Scanty cytoplasm' (lines to both cells), 'Cytoplasmic granules' (line to left cell, myeloblast), 'Nucleoli' (lines to both cells in the drawing), and 'Auer rod' (line to left cell, myeloblast).",
)

add(
    S1,
    136,
    "truefalse",
    "Which of the following statements from page 136 comparing ALL and AML blasts is TRUE?",
    "True — Lymphoblasts are smaller, lack granules, are MPO and Sudan black negative, and stain positive for PAS and acid phosphatase",
    [
        "True — Precursor B cell ALL accounts for 20% of ALL cases and characteristically produces an anterior mediastinal thymic mass in adolescent boys",
        "False — In children under 10 years of age, acute lymphoblastic leukemia (ALL) carries a 90–95% survival rate with modern therapy",
        "False — Myeloblasts are larger than lymphoblasts, contain cytoplasmic granules and Auer rods, and stain positive for MPO and Sudan black",
    ],
    "In the page 136 table, lymphoblasts are smaller, have absent nucleoli and absent granules, are MPO negative and Sudan black negative, and are PAS positive and acid phosphatase positive.",
)


# ==============================================================================
# UNIT 2 — Page 137: ALL Risk Factors, Presenting Features & Laboratory Features
# ==============================================================================

add(
    S2,
    137,
    "recall",
    "Under 'RISK FACTORS → Down syndrome' at the top of page 137, what is the descending order of frequency printed after 'M/c malignancy'?",
    "Transient abnormal myelopoiesis > ALL > AML",
    [
        "AML (megakaryocytic M7) > Transient abnormal myelopoiesis > ALL",
        "ALL > Hodgkin lymphoma > Chronic lymphocytic leukemia (CLL)",
        "Myelodysplastic syndrome (MDS) > Primary myelofibrosis > AML",
    ],
    "Under RISK FACTORS → Down syndrome on page 137: 'M/c malignancy : Transient abnormal myelopoiesis > ALL > AML.'",
)

add(
    S2,
    137,
    "recall",
    "Under 'RISK FACTORS' on page 137, which two inherited syndromes are listed under 'Defective DNA repair', and what physical exposure follows them?",
    "Ataxia-telangiectasia and Bloom's syndrome; followed by Radiation",
    [
        "Noonan syndrome and Kostmann syndrome; followed by Benzene exposure",
        "Diamond-Blackfan syndrome and Shwachman-Diamond syndrome; followed by Alkylating agents",
        "Wiskott-Aldrich syndrome and Chédiak-Higashi syndrome; followed by Etoposide",
    ],
    "Under RISK FACTORS on page 137: Defective DNA repair lists Ataxia-telangiectasia and Bloom's syndrome, followed by Radiation.",
)

add(
    S2,
    137,
    "recall",
    "What does the right-hand 'Note' under RISK FACTORS on page 137 state regarding Defective DNA repair and Radiation (as printed)?",
    "Defective DNA repair : in AML, ALL; Radiation : in AML, ALL, CLL (as printed)",
    [
        "Defective DNA repair : only in CML and CLL; Radiation : only in hairy cell leukemia and myeloma",
        "Defective DNA repair : protective against ALL; Radiation : in Hodgkin lymphoma and polycythemia vera only",
        "Defective DNA repair : in MDS and PMF only; Radiation : never associated with acute leukemias",
    ],
    "The Note on the right side of RISK FACTORS on page 137 prints: '• Defective DNA repair : in AML, ALL. • Radiation : in AML, ALL, CLL.' (Note: standard references state CLL is not radiation-associated; this is tested as printed on page 137.)",
)

add(
    S2,
    137,
    "recall",
    "Under 'Presenting Features' on page 137, how does B-cell ALL present in adults versus in children?",
    "Adult: Pancytopenia; Children: Limping, bone tenderness, inability to walk",
    [
        "Adult: Limping and bone pain; Children: Asymptomatic splenomegaly with thrombocytosis",
        "Adult: Anterior mediastinal mass with superior vena cava obstruction; Children: Gingival hypertrophy and orbital chloroma",
        "Adult: Sweet syndrome and aquagenic pruritus; Children: Painless cervical lymphadenopathy without bone tenderness",
    ],
    "Under Presenting Features on page 137: '• B-cell ALL in → Adult : Pancytopenia; → Children : Limping, bone tenderness, inability to walk.'",
)

add(
    S2,
    137,
    "scenario",
    "An adolescent boy presents to the emergency department with progressive dyspnea. Chest imaging reveals mediastinal widening due to an anterior mediastinal mass. According to page 137, which leukemia subtype characteristically presents in this manner?",
    "T cell ALL in adolescents",
    [
        "Precursor B cell ALL in children",
        "Acute promyelocytic leukemia (AML M3)",
        "Acute myelomonocytic leukemia (AML M4 Eo)",
    ],
    "Bullet 2 under Presenting Features on page 137 reads: '• T cell ALL in adolescents : Dyspnea d/t mediastinal widening (Anterior mediastinal mass).'",
)

add(
    S2,
    137,
    "recall",
    "Under 'Presenting Features → High count ALL' on page 137, what are its prognosis, the two 'sanctuary sites' involved, their clinical consequence, and the required treatment?",
    "Very poor prognosis; involves 'sanctuary sites' (CNS, testes), which are the cause for relapse after treatment and require intrathecal chemotherapy",
    [
        "Favourable prognosis; involves 'sanctuary sites' (spleen, liver), which resolve spontaneously within 2–3 months and require only oral hydroxyurea",
        "Good prognosis; involves 'sanctuary sites' (thymus, pleura), which prevent bone marrow relapse and require upfront surgical thymectomy",
        "Intermediate prognosis; involves 'sanctuary sites' (gingiva, orbit), which respond completely to oral corticosteroids without intrathecal therapy",
    ],
    "Under 'High count ALL' on page 137: '– Very poor prognosis. – Involves \"sanctuary sites\" : CNS, testes. Cause for relapse after treatment. Requires intrathecal chemotherapy.'",
)

add(
    S2,
    137,
    "fillup",
    "Because high-count ALL infiltrates the sanctuary sites (CNS and testes) and causes relapse after treatment, it requires ______ chemotherapy.",
    "intrathecal",
    [
        "subcutaneous",
        "inhalational",
        "intra-arterial",
    ],
    "Under High count ALL on page 137: 'Involves \"sanctuary sites\" : CNS, testes. Cause for relapse after treatment. Requires intrathecal chemotherapy.'",
)

add(
    S2,
    137,
    "recall",
    "Under 'Other symptoms' on page 137, what general findings are listed, how does organomegaly compare between B-ALL and T-ALL, and which organ involvements are labelled 'Rare'?",
    "Fatigue, lethargy; pallor, petechiae, ecchymosis; Organomegaly is rare in B-ALL and ± in T-ALL; ocular, skin, salivary, cranial nerve, pericardium, and pleural involvement are rare",
    [
        "Organomegaly is universal (100%) in B-ALL and completely absent in T-ALL; ocular, skin, salivary gland, and cranial nerve infiltration are the most common presenting signs",
        "Severe hyperviscosity microvascular thrombosis and priapism are common; pericardial tamponade and massive pleural effusions occur at presentation in >80% of B-ALL cases",
        "Painless generalized lymphadenopathy with Pel-Ebstein cyclical fever is universal in B-ALL; isolated cranial nerve palsies and salivary hypertrophy occur in 75% of adults",
    ],
    "Under Other symptoms on page 137: '– Fatigue, lethargy. – Pallor, petechiae, ecchymosis. – Organomegaly → Rare in B-ALL; → ± in T-ALL. – Ocular, skin, salivary, cranial nerve, pericardium, pleural involvement : Rare.'",
)

add(
    S2,
    137,
    "recall",
    "Under 'Laboratory Features' at the bottom of page 137, what findings are listed under '1. In blood' and '2. In CSF'?",
    "1. In blood: Anemia, neutropenia, thrombocytopenia; circulating blasts; highly variable presenting counts; hypereosinophilia precedes blasts by several months; 2. In CSF: leukemic blasts +ve",
    [
        "1. In blood: Absolute polycythemia, basophilia, and thrombocytosis; complete absence of circulating blasts on peripheral smear; 2. In CSF: acellular fluid with oligoclonal IgG bands",
        "1. In blood: Microcytic hypochromic anemia with ringed sideroblasts and teardrop dacryocytes; fixed low leucocyte count; 2. In CSF: xanthochromia and elevated protein without blasts",
        "1. In blood: Isolated normocytic anemia with normal platelet count and normal absolute neutrophil count in all patients; 2. In CSF: India-ink positive encapsulated yeast cells",
    ],
    "Under Laboratory Features on page 137: '1. In blood : • Anemia, neutropenia, thrombocytopenia. • Circulating blasts. • Highly variable presenting counts. • Hypereosinophilia : Precedes blasts by several months. 2. In CSF : leukemic blasts +ve.'",
)

add(
    S2,
    137,
    "fillup",
    "Under 'Laboratory Features → 1. In blood' on page 137, ______ may precede the appearance of circulating leukemic blasts by several months.",
    "hypereosinophilia",
    [
        "monocytopenia",
        "reticulocytosis",
        "thrombocytosis",
    ],
    "Bullet 4 under '1. In blood' on page 137 reads: '• Hypereosinophilia : Precedes blasts by several months.'",
)


# ==============================================================================
# UNIT 3 — Page 138: B-Cell Subtypes, Types of ALL (B-ALL vs T-ALL), Smears & Bottom Note
# ==============================================================================

add(
    S3,
    138,
    "recall",
    "In the top 'Note : Subtypes of B cell' diagram on page 138, what are the three subtypes and which one is the most common (m/c)?",
    "Pro B cell, Pre B cell (m/c), and Immature B cell",
    [
        "Naive B cell, Memory B cell (m/c), and Plasma cell",
        "Myeloblast, Monoblast (m/c), and Megakaryoblast",
        "Centroblast, Centrocyte (m/c), and Immunoblast",
    ],
    "At the top of page 138, 'Subtypes of B cell' branches into Pro B cell, Pre B cell (• m/c), and Immature B cell.",
)

add(
    S3,
    138,
    "recall",
    "Under 'Pre B cell' in the top diagram on page 138, what are the two printed features of 'Early pre B-cell'?",
    "Best prognosis; expresses CD 10⁺ : CALLA antigen",
    [
        "Worst prognosis; expresses surface IgM and CD 5⁺",
        "Intermediate prognosis; expresses CD 13⁺, CD 33⁺, and cytoplasmic MPO",
        "Poor prognosis; expresses CD 41⁺, CD 61⁺, and glycophorin",
    ],
    "Under Pre B cell → Early pre B-cell on page 138: '– Best prognosis. – CD 10⁺ : CALLA antigen.'",
)

add(
    S3,
    138,
    "fillup",
    "In early pre B-cell ALL (which carries the best prognosis), the surface marker CD 10⁺ is known as the ______ antigen.",
    "CALLA",
    [
        "FLAER",
        "HLA-DR",
        "MIRL",
    ],
    "Under Pre B cell → Early pre B-cell on page 138: '– Best prognosis. – CD 10⁺ : CALLA antigen.'",
)

add(
    S3,
    138,
    "recall",
    "Under 'Types of ALL → B cell ALL' on page 138, what is its rank among childhood cancers, and what are the incidence and mechanism of fever?",
    "Most common (m/c) childhood cancer; fever occurs in 50% of cases due to cytokine production by lymphoblasts",
    [
        "Rarest childhood cancer; fever is completely absent (0% of cases) because lymphoblasts produce no cytokines",
        "Third most common childhood cancer after neuroblastoma and Wilms tumor; fever occurs in 100% due to endotoxemia",
        "Exclusively an adult malignancy (>60 years); fever occurs only after G-CSF administration due to Sweet syndrome",
    ],
    "Under B cell ALL on page 138: '• M/c childhood cancer. • Features of bone marrow failure. • Fever : – In 50 % cases. – D/t cytokine production by lymphoblasts.'",
)

add(
    S3,
    138,
    "recall",
    "Besides bone marrow failure features and fever, what other clinical manifestations are listed under 'B cell ALL' on page 138, and which two conditions is it misdiagnosed as?",
    "Expansion of marrow cavity, bleeding tendencies, and CNS involvement; misdiagnosed as Idiopathic thrombocytopenic purpura and Aplastic anemia",
    [
        "Anterior mediastinal mass, pleural effusion, and superior vena cava syndrome; misdiagnosed as Hodgkin lymphoma and malignant thymoma",
        "Gingival hypertrophy, bilateral orbital chloroma, and perianal proctitis; misdiagnosed as vitamin C deficiency (scurvy) and Crohn's disease",
        "Massive splenomegaly, portal hypertension, and acute gouty arthritis; misdiagnosed as decompensated cirrhosis and primary myelofibrosis",
    ],
    "Under B cell ALL on page 138: '• Expansion of marrow cavity. • Bleeding tendencies. • CNS involvement. • Misdiagnosed as → Idiopathic thrombocytopenic purpura; → Aplastic anemia.'",
)

add(
    S3,
    138,
    "recall",
    "Under 'Types of ALL → T cell ALL' on page 138, what is its classical presentation, what other site is involved, and how does the presence or absence of pancytopenia classify the disease?",
    "Classical presentation: Mediastinal mass + pleural effusion, with CNS involvement; Pancytopenia (+) defines T cell leukemia, whereas Pancytopenia (–) defines T cell lymphoma",
    [
        "Classical presentation: Orbital chloroma + gingival hypertrophy, without CNS involvement; Pancytopenia (+) defines T cell lymphoma, whereas Pancytopenia (–) defines T cell leukemia",
        "Classical presentation: Massive splenomegaly + portal hypertension; Pancytopenia (+) defines hairy cell leukemia, whereas Pancytopenia (–) defines Hodgkin disease",
        "Classical presentation: Punched-out lytic bone lesions + renal failure; Pancytopenia (+) defines plasma cell leukemia, whereas Pancytopenia (–) defines smoldering myeloma",
    ],
    "Under T cell ALL on page 138: '• Classical presentation : Mediastinal mass + pleural effusion. • CNS involvement. • Pancytopenia → (+) : T cell leukemia; → (–) : T cell lymphoma.'",
)

add(
    S3,
    138,
    "recall",
    "What do the two bone marrow smear photomicrographs on page 138 illustrate, and what are their exact captions?",
    "Both arrows point to 'Large lymphoblasts' in 'Bone marrow smear in ALL' (left) and 'Bone marrow smear of precursor B cell ALL' (right)",
    [
        "Both arrows point to 'Hypergranular myeloblasts' in 'Bone marrow smear in AML M3' (left) and 'Faggot cells with Auer rods in APML' (right)",
        "Both arrows point to 'Cup-shape blasts' in 'Bone marrow smear of NPM1-mutated AML' (left) and 'Abnormal eosinophils in AML M4 Eo' (right)",
        "Both arrows point to 'Pawn-ball megakaryocytes' in 'Bone marrow smear of MDS' (left) and 'Ringed sideroblasts on Perls stain' (right)",
    ],
    "Page 138 displays two bone marrow smear images with arrows from 'Large lymphoblasts', captioned 'Bone marrow smear in ALL' (left) and 'Bone marrow smear of precursor B cell ALL' (right).",
)

add(
    S3,
    138,
    "recall",
    "What two statements are printed in the bottom 'Note' on page 138?",
    "AML : No fever; and HTLV-1 (Human T-lymphotropic virus -1) : Organism that produces adult T cell lymphoma",
    [
        "AML : Fever in 80% of cases; and EBV (Epstein-Barr virus) : Organism that produces precursor B cell ALL in children",
        "ALL : No fever at presentation; and HIV-1 : Organism that produces childhood T cell lymphoblastic leukemia",
        "CML : No splenomegaly; and HHV-8 (human herpesvirus-8) : Organism that produces hairy cell leukemia in adults",
    ],
    "The bottom Note on page 138 reads: '• AML : No fever. • HTLV-1 (Human T-lymphotropic virus -1) : Organism that produces adult T cell lymphoma.'",
)

add(
    S3,
    138,
    "truefalse",
    "Which of the following statements from page 138 is TRUE?",
    "True — Fever occurs in 50% of B-cell ALL cases due to cytokine production by lymphoblasts, whereas AML has no fever",
    [
        "True — In T-cell ALL, the presence of pancytopenia (+) is classified as T-cell lymphoma and the absence of pancytopenia (–) as T-cell leukemia",
        "False — Pre B-cell is the most common subtype of B-cell ALL, and early pre B-cell (CD10⁺ / CALLA) has the best prognosis",
        "False — HTLV-1 (Human T-lymphotropic virus-1) is the organism that produces adult T-cell lymphoma",
    ],
    "On page 138: B-cell ALL has fever in 50% of cases due to cytokine production by lymphoblasts, while the bottom Note contrasts 'AML : No fever' and notes HTLV-1 as the organism producing adult T-cell lymphoma.",
)


# ==============================================================================
# UNIT 4 — Page 139: Prognostic Factors Table, Treatment of ALL (BFM-19) & Other Drugs
# ==============================================================================

add(
    S4,
    139,
    "match",
    "In the 'Prognostic Factors' table of ALL on page 139, match each demographic or FAB morphological parameter with its Good prognosis versus Bad prognosis assignment — 1) Race (Good vs Bad) 2) Age (Good vs Bad) 3) Sex (Good vs Bad) 4) FAB Type (Good vs Bad) … A) 2–9 years vs <1 yr or >10 yrs B) L1 vs L2, L3 C) White vs Black D) Female vs Male",
    "1-C, 2-A, 3-D, 4-B",
    [
        "1-A, 2-C, 3-B, 4-D",
        "1-C, 2-D, 3-A, 4-B",
        "1-D, 2-A, 3-C, 4-B",
    ],
    "In the Prognostic Factors table on page 139 (Good prognosis vs Bad prognosis): Race — White vs Black; Age — 2–9 years vs <1 yr or >10 yrs; Sex — Female vs Male; Type — L1 vs L2, L3.",
)

add(
    S4,
    139,
    "recall",
    "In the 'Prognostic Factors' table on page 139, how are CNS involvement, Testes involvement, Hepatosplenomegaly, Lymphadenopathy, and Mediastinal mass classified across Good prognosis versus Bad prognosis?",
    "All five clinical features are absent (–) in Good prognosis and present (+) in Bad prognosis",
    [
        "All five clinical features are present (+) in Good prognosis and absent (–) in Bad prognosis",
        "Hepatosplenomegaly and lymphadenopathy indicate Good prognosis (+), whereas CNS, testes, and mediastinal mass indicate Bad prognosis (+)",
        "Mediastinal mass and testicular involvement indicate Good prognosis (+), whereas CNS involvement indicates Bad prognosis (+)",
    ],
    "Rows 4–8 of the Prognostic Factors table on page 139 (CNS involvement, Testes involvement, Hepatosplenomegaly, Lymphadenopathy, Mediastinal mass) all show '–' under Good prognosis and '+' under Bad prognosis.",
)

add(
    S4,
    139,
    "match",
    "In the lower half of the 'Prognostic Factors' table on page 139, match each cytogenetic, molecular, or immunophenotypic row (Good prognosis vs Bad prognosis) — 1) Cytogenetics (Good vs Bad) 2) Molecular genetics: Translocations (Good vs Bad) 3) Molecular genetics: Mutations (Good vs Bad) 4) Immunophenotype (Good vs Bad) … A) t(12;21) vs t(9;22), t(4;11), t(1;19) B) NOTCH-1 , HOX 11 vs '–' C) Early pre B cell vs T cell D) Hyperdiploidy vs Hypodiploidy",
    "1-D, 2-A, 3-B, 4-C",
    [
        "1-A, 2-D, 3-C, 4-B",
        "1-D, 2-B, 3-A, 4-C",
        "1-C, 2-A, 3-B, 4-D",
    ],
    "In the Prognostic Factors table on page 139 (Good vs Bad prognosis): Cytogenetics — Hyperdiploidy vs Hypodiploidy; Translocations — t(12 ; 21) vs t(9 ; 22), t(4 ; 11), t(1 ; 19); Mutations — NOTCH-1, HOX 11 vs –; Immunophenotype — Early pre B cell vs T cell.",
)

add(
    S4,
    139,
    "oddoneout",
    "All of the following translocations are listed in the 'Bad prognosis' column of the ALL Prognostic Factors table on page 139 EXCEPT:",
    "t(12 ; 21)",
    [
        "t(9 ; 22) [Ph+]",
        "t(4 ; 11)",
        "t(1 ; 19)",
    ],
    "In the Molecular genetics → Translocations row on page 139, t(12 ; 21) is in the Good prognosis column, whereas t(9 ; 22), t(4 ; 11), and t(1 ; 19) are in the Bad prognosis column.",
)

add(
    S4,
    139,
    "recall",
    "In the 'Molecular genetics → Mutations' row of the ALL Prognostic Factors table on page 139, which two mutations are listed under 'Good prognosis'?",
    "NOTCH-1 and HOX 11",
    [
        "FLT3-ITD and c-Kit",
        "JAK2 V617F and MPL",
        "SF3B1 and GATA-1",
    ],
    "In the Molecular genetics → Mutations row on page 139, 'NOTCH-1 , HOX 11' is printed under Good prognosis (with '–' under Bad prognosis).",
)

add(
    S4,
    139,
    "recall",
    "Under 'Treatment of ALL → 1. Induction phase (2 cycles)' on page 139, what are the stated goal, protocol name, and four-drug regimen?",
    "Goal: To achieve remission; follows BFM-19 protocol; Regimen: Steroids + Vincristine + Daunorubicin + Cyclophosphamide",
    [
        "Goal: Palliative cytoreduction; follows 7+3 protocol; Regimen: Low-dose Cytarabine (7 days continuous) + Daunorubicin (3 days I.V)",
        "Goal: Promyelocyte differentiation; follows Sanz protocol; Regimen: All-trans retinoic acid (ATRA) + Arsenic trioxide + Idarubicin",
        "Goal: Epigenetic hypomethylation; follows R-IPSS protocol; Regimen: Azacitidine + Decitabine + Oral Venetoclax (BCL-2 inhibitor)",
    ],
    "Under '1. Induction phase (2 cycles)' on page 139: '• Goal : To achieve remission. • Follows BFM-19 protocol. • Regimen : Steroids + Vincristine + Daunorubicin + Cyclophosphamide.'",
)

add(
    S4,
    139,
    "recall",
    "According to the '1. Induction phase (2 cycles)' section on page 139, what is the current status of L-asparaginase in ALL induction and why?",
    "Not used now due to widespread thrombosis",
    [
        "Mandatory first-line agent in all adults because it prevents CNS relapses",
        "Reserved exclusively for T-cell ALL because it reverses anterior mediastinal widening",
        "Discontinued due to irreversible dose-dependent anthracycline cardiomyopathy",
    ],
    "Bullet 4 under '1. Induction phase (2 cycles)' on page 139 reads: '• L-asparaginase : Not used now d/t widespread thrombosis.'",
)

add(
    S4,
    139,
    "management",
    "In the 'Treatment of ALL' flowchart on page 139, how does '2. Bone marrow study : MRD status' after induction direct steps 3 and 4 for MRD-Negative versus MRD-Positive patients?",
    "MRD Negative → 3. Consolidation phase (another 2 cycles of chemotherapy) → 4. Maintenance phase (Methotrexate + 6-mercaptopurine for 2–3 years); MRD Positive → 3. 2 cycles of chemotherapy → 4. Transplant",
    [
        "MRD Negative → 3. Immediate allogeneic hematopoietic stem cell transplantation without consolidation; MRD Positive → 3. Oral methotrexate + 6-mercaptopurine maintenance therapy for 2–3 years without transplant",
        "MRD Negative → 3. Discontinue all cytotoxic chemotherapy immediately after induction; MRD Positive → 3. High-dose cytarabine consolidation monotherapy (with stem cell transplantation not mandatory)",
        "MRD Negative → 3. Six cycles of ATRA + arsenic trioxide differentiation therapy; MRD Positive → 3. Rituximab + intrathecal methotrexate maintenance monotherapy for 5 years without stem cell transplant",
    ],
    "The flowchart under '2. Bone marrow study : MRD status' on page 139 branches into: Negative → 3. Consolidation phase (Another 2 cycles of chemotherapy) → 4. Maintenance phase (Methotrexate + 6 mercaptopurine for 2–3 years); and Positive → 3. 2 cycles of chemotherapy → 4. Transplant.",
)

add(
    S4,
    139,
    "numeric",
    "In step '4. Maintenance phase' of the MRD-negative ALL treatment pathway on page 139, which two drugs are administered and for what duration?",
    "Methotrexate + 6-mercaptopurine for 2–3 years",
    [
        "Cytarabine + Daunorubicin for 10–14 days of continuous infusion",
        "Azacitidine + Oral Venetoclax for 6 months of consolidation",
        "Prednisolone + Intravenous Vincristine for 4–6 weeks of induction",
    ],
    "Step 4 on the MRD-Negative branch on page 139 reads: '4. Maintenance phase (Methotrexate + 6 mercaptopurine for 2–3 years)'.",
)

add(
    S4,
    139,
    "match",
    "Under 'Other drugs' at the bottom of page 139, match each agent used in ALL with its printed indication or mechanism — 1) Rituximab 2) Intrathecal methotrexate 3) Blinatumomab 4) Tyrosine kinase inhibitors … A) Bispecific T-cell engager (Anti-CD 19 + Anti-CD 3) B) Add if CD20 +ve C) If BCR-ABL +ve → Gives better prognosis D) ↓ CNS relapses",
    "1-B, 2-D, 3-A, 4-C",
    [
        "1-A, 2-B, 3-D, 4-C",
        "1-B, 2-C, 3-A, 4-D",
        "1-D, 2-B, 3-C, 4-A",
    ],
    "Under 'Other drugs' at the bottom of page 139: '• Rituximab : Add if CD20 +ve. • Intrathecal methotrexate : ↓ CNS relapses. • Blinatumomab : Bispecific T-cell engager (Anti-CD 19 + Anti-CD 3). • Tyrosine kinase inhibitors : If BCR-ABL +ve → Gives better prognosis.'",
)

add(
    S4,
    139,
    "scenario",
    "A 15-year-old boy with precursor B-cell ALL completes 2 cycles of BFM-19 induction (steroids + vincristine + daunorubicin + cyclophosphamide). Bone marrow study reveals MRD-positive disease, and immunotherapy with blinatumomab is considered. Which dual specificity defines blinatumomab, and what is the subsequent step after 2 further cycles of chemotherapy on the page 139 pathway?",
    "Bispecific T-cell engager targeting Anti-CD 19 + Anti-CD 3; followed by Transplant (step 4 of the MRD-positive arm)",
    [
        "Antibody-drug conjugate targeting Anti-CD 33 + calicheamicin; followed by 2–3 years of oral methotrexate + 6-mercaptopurine maintenance",
        "Monoclonal antibody targeting Anti-CD 20 + complement C5; followed by observation without further chemotherapy or transplant",
        "Small-molecule inhibitor targeting BCL-2 + FLT3-ITD; followed by prophylactic splenic irradiation and hydroxyurea",
    ],
    "On page 139, MRD-positive ALL proceeds to '3. 2 cycles of chemotherapy → 4. Transplant', and under Other drugs, Blinatumomab is a 'Bispecific T-cell engager (Anti-CD 19 + Anti-CD 3)'.",
)


GUIDES = {
    S1: (
        "ALL Pathophysiology, Survival by Age, B-Cell vs T-Cell Lineage & Lymphoblast vs Myeloblast Morphology",
        "Epidemiology & survival: ALL = 20% of adult leukemias (40–45% survival) and 90% of child/adolescent leukemias (10–19 yrs: 70–75% survival; <10 yrs: 90–95% survival); median age 13 years.\n"
        "Lineages: Precursor B-cell ALL (80%) only involves marrow (only leukemias); Precursor T-cell ALL (20%) has poor prognosis, involves bone marrow ± mass (leukemias/lymphomas) in thymus → mediastinal widening, dyspnea, common in adolescent boys.\n"
        "Lymphoblast vs Myeloblast: Lymphoblast is smaller, nucleoli absent, granules absent, MPO negative, Sudan black negative, PAS positive, acid phosphatase positive (myeloblast is larger, nucleoli & granules present, MPO & Sudan black positive, Auer rod).",
    ),
    S2: (
        "ALL Risk Factors, Presenting Features (B-ALL, T-ALL, High-Count Sanctuary Sites) & Laboratory Features",
        "Risk factors: Down syndrome (m/c malignancy: transient abnormal myelopoiesis > ALL > AML), defective DNA repair (ataxia-telangiectasia, Bloom's syndrome — in AML, ALL), radiation (printed note: in AML, ALL, CLL).\n"
        "Presenting features: B-cell ALL in adults = pancytopenia, in children = limping, bone tenderness, inability to walk; T-cell ALL in adolescents = dyspnea d/t mediastinal widening (anterior mediastinal mass); High-count ALL = very poor prognosis, involves sanctuary sites (CNS, testes → cause for relapse, requires intrathecal chemotherapy); organomegaly rare in B-ALL, ± in T-ALL.\n"
        "Lab features: (1) Blood — anemia, neutropenia, thrombocytopenia, circulating blasts, highly variable counts, hypereosinophilia precedes blasts by several months; (2) CSF — leukemic blasts +ve.",
    ),
    S3: (
        "B-Cell Subtypes (Pro-B, Pre-B, Early Pre-B CALLA, Immature B), B-ALL vs T-ALL Clinical Features & Smear Notes",
        "B-cell subtypes: Pro B cell, Pre B cell (m/c; includes Early pre B-cell → best prognosis, CD10⁺ = CALLA antigen), Immature B cell.\n"
        "B-cell ALL: m/c childhood cancer, bone marrow failure features, fever in 50% d/t cytokine production by lymphoblasts, marrow cavity expansion, bleeding, CNS involvement; misdiagnosed as ITP or aplastic anemia.\n"
        "T-cell ALL: classical presentation = mediastinal mass + pleural effusion, CNS involvement, pancytopenia (+) = T-cell leukemia vs (–) = T-cell lymphoma. Smears show large lymphoblasts; Note: AML has no fever; HTLV-1 produces adult T-cell lymphoma.",
    ),
    S4: (
        "ALL Prognostic Factors Table, BFM-19 Treatment Protocol (Induction, MRD, Consolidation, Maintenance) & Other Drugs",
        "Prognostic factors (Good vs Bad): White vs Black; 2–9 yrs vs <1 or >10 yrs; Female vs Male; CNS/testes/HSM/LAP/mediastinal mass – vs +; L1 vs L2, L3; Hyperdiploidy vs Hypodiploidy; t(12;21) vs t(9;22), t(4;11), t(1;19); NOTCH-1, HOX 11 vs –; Early pre B cell vs T cell.\n"
        "Treatment: 1. Induction (2 cycles, BFM-19 protocol: Steroids + Vincristine + Daunorubicin + Cyclophosphamide; L-asparaginase not used now d/t widespread thrombosis) → 2. Bone marrow MRD status: Negative → 3. Consolidation (another 2 cycles) → 4. Maintenance (Methotrexate + 6-MP for 2–3 yrs); Positive → 3. 2 cycles chemo → 4. Transplant.\n"
        "Other drugs: Rituximab (add if CD20 +ve), Intrathecal methotrexate (↓ CNS relapses), Blinatumomab (bispecific T-cell engager: Anti-CD19 + Anti-CD3), TKIs (if BCR-ABL +ve → better prognosis).",
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
