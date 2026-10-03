#!/usr/bin/env python3
"""Generate Chapter 21: Bone Marrow Failure Syndromes (Book p121–125).

Every question is anchored to a specific line, table cell, image label, or
flowchart step in uploads/02.pdf (PDF pages 4–8 = Book pages 121–125) in
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
CHAPTER = 21
TITLE = "Bone Marrow Failure Syndromes"
PAGES = "121-125"

S1 = "Approach to Pancytopenia: Marrow Cellularity Flowchart & Aplastic Anemia Overview"
S2 = "Inherited vs Acquired Aplastic Anemia: Fanconi, Dyskeratosis Congenita, Shwachman-Diamond"
S3 = "Drugs Causing Aplastic Anemia, Presentation, Severity Criteria & Treatment"
S4 = "Pure Red Cell Aplasia & MDS Overview: Global Versus India Presentation"
S5 = "MDS Blood Parameters, Prognostic Scoring & Treatment Flowchart"

RAW: list[tuple] = []


def add(sec: str, page: int, fmt: str, stem: str, correct: str, distractors: list[str], explanation: str) -> None:
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    rng = random.Random(21000 + CHAPTER * 10000 + len(RAW))
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
# UNIT 1 — Page 121: diseases, pancytopenia flowchart, aplastic anemia intro
# ==============================================================================

add(
    S1,
    121,
    "recall",
    "Which four diseases head the Bone Marrow Failure Syndromes chapter on page 121?",
    "Aplastic anemia, myelodysplastic syndrome/neoplasia (MDS), pure red cell aplasia, and myelophthisis (secondary myelofibrosis)",
    [
        "Aplastic anemia, CML, PNH and hairy cell leukemia",
        "MDS, PMF, ET and PCRV",
        "Pure red cell aplasia, thymoma, PRCA of childhood and Diamond-Blackfan anemia",
    ],
    "The diseases list prints aplastic anemia, myelodysplastic syndrome/neoplasia (MDS), pure red cell aplasia, and myelophthisis (secondary myelofibrosis).",
)

add(
    S1,
    121,
    "fillup",
    "Myelophthisis on page 121 is also labelled secondary ______.",
    "myelofibrosis",
    [
        "osteosclerosis",
        "marrow infiltration by lymphoma",
        "hematopoiesis",
    ],
    "The diseases list prints myelophthisis (secondary myelofibrosis).",
)

add(
    S1,
    121,
    "recall",
    "In the page 121 approach-to-pancytopenia flowchart, what is the first step and its branching variable?",
    "Bone marrow aspiration + biopsy, branching on cellularity of marrow (hypercellular versus hypocellular)",
    [
        "Peripheral smear first, branching on MCV",
        "Flow cytometry first, branching on CD55/CD59",
        "Serum B12/folate first, branching on reticulocyte count",
    ],
    "The flowchart runs bone marrow aspiration + biopsy → cellularity of marrow → hypercellular marrow versus hypocellular marrow arms.",
)

add(
    S1,
    121,
    "match",
    "Match each hypercellular-marrow cause on page 121 with its printed note — 1) Acute leukemia 2) Hairy cell leukemia 3) Megaloblastic anemia 4) Paroxysmal nocturnal hemoglobinuria … A) Unless proven otherwise (in adults AML 80%, ALL 20%) B) Good prognosis; pancytopenia + massive splenomegaly C) Good prognosis D) Listed as item 6 of the hypercellular arm",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-C, 3-B, 4-D",
        "1-C, 2-B, 3-A, 4-D",
    ],
    "The hypercellular arm prints acute leukemia (unless proven otherwise; adults AML 80%, ALL 20%), MDS, PMF, hairy cell leukemia (good prognosis; pancytopenia + massive splenomegaly), megaloblastic anemia (good prognosis), PNH and systemic causes.",
)

add(
    S1,
    121,
    "recall",
    "Which systemic causes of a hypercellular marrow does page 121 list under item 7?",
    "SLE, HIV, TB, brucellosis, leishmaniasis and sarcoidosis",
    [
        "SLE, HIV, typhoid, malaria and histoplasmosis",
        "Rheumatoid arthritis, Sjögren's, TB and brucellosis",
        "SLE, HIV, EBV, CMV and toxoplasmosis",
    ],
    "Item 7 prints systemic : SLE, HIV, TB, brucellosis, leishmaniasis, sarcoidosis.",
)

add(
    S1,
    121,
    "recall",
    "List the causes printed under the hypocellular marrow arm with pancytopenia (+) on page 121.",
    "Aplastic anemia, 20% of MDS cases, aleukemic leukemia, copper deficiency and lymphoma",
    [
        "Aplastic anemia, 80% of MDS cases, hairy cell leukemia and PNH",
        "Q fever, Legionella, anorexia and TB",
        "Acute leukemia, MDS, PMF and megaloblastic anemia",
    ],
    "The + pancytopenia branch lists aplastic anemia, 20% of MDS cases, aleukemic leukemia, copper deficiency and lymphoma.",
)

add(
    S1,
    121,
    "recall",
    "Which causes sit under the hypocellular marrow arm with ± pancytopenia on page 121?",
    "Q fever, Legionella, anorexia and TB",
    [
        "SLE, HIV, brucellosis and sarcoidosis",
        "Copper deficiency, lymphoma, aplastic anemia and MDS",
        "Hepatitis viruses, EBV, CMV and parvovirus",
    ],
    "The ± pancytopenia branch prints Q fever, Legionella, anorexia and TB.",
)

add(
    S1,
    121,
    "recall",
    "What two one-liners does page 121 print for PMF and hairy cell leukemia in the pancytopenia approach?",
    "PMF : pancytopenia + fibrosis; hairy cell leukemia : pancytopenia + massive splenomegaly",
    [
        "PMF : pancytopenia + lymphadenopathy; hairy cell : pancytopenia + skin lesions",
        "PMF : leukoerythroblastosis + thrombocytosis; hairy cell : monocytopenia only",
        "PMF : pancytopenia + osteosclerosis; hairy cell : pancytopenia + hepatomegaly",
    ],
    "The footer prints PMF : Pancytopenia + Fibrosis and hairy cell leukemia : Pancytopenia + massive splenomegaly.",
)

add(
    S1,
    121,
    "recall",
    "Page 121 prints 'Pancytopenia with hypercellular marrow' under the aplastic anemia heading. How does the rest of the book define the aplastic anemia marrow?",
    "Hypocellular marrow — the same page's flowchart sends aplastic anemia down the hypocellular arm, and page 123 prints 'hypocellular bone marrow with fat cells'; the p121 line is a printed slip",
    [
        "Hypercellular marrow with fibrosis as printed",
        "Normocellular marrow with dysplasia",
        "Hypercellular marrow packed with blasts",
    ],
    "The p121 bullet prints 'hypercellular' as a slip; the flowchart on the same page places aplastic anemia under hypocellular marrow (+ pancytopenia), and p123 confirms a hypocellular bone marrow with fat cells.",
)

add(
    S1,
    121,
    "recall",
    "What bimodal age distribution does page 121 give for aplastic anemia?",
    "Inherited < 20 years, acquired > 60 years",
    [
        "Inherited < 10 years, acquired > 40 years",
        "Inherited < 30 years, acquired > 70 years",
        "Inherited < 20 years, acquired 20–40 years",
    ],
    "The line prints bimodal age distribution (inherited < 20 yrs, acquired > 60 yrs), verified visually from the scan.",
)

add(
    S1,
    121,
    "recall",
    "Which cause and infection labels, and which prognosis note, does page 121 print for aplastic anemia?",
    "m/c cause : drug dependent (good prognosis); m/c infection : non-A, non-B hepatitis; and a 'bad prognosis' note as printed",
    [
        "m/c cause : idiopathic (bad prognosis); m/c infection : EBV; good prognosis note",
        "m/c cause : radiation; m/c infection : hepatitis B; variable prognosis",
        "m/c cause : drug dependent (bad prognosis); m/c infection : HIV; good prognosis note",
    ],
    "The bullets print m/c cause drug dependent (good prognosis), m/c infection non-A, non-B hepatitis, and a bare 'bad prognosis' line as printed (attached to the idiopathic setting in teaching).",
)

add(
    S1,
    121,
    "oddoneout",
    "The page 121 hypercellular-marrow arm lists several causes. Pick the ODD ONE OUT — the one NOT in that arm:",
    "Aplastic anemia",
    [
        "Megaloblastic anemia",
        "Paroxysmal nocturnal hemoglobinuria",
        "Primary myelofibrosis",
    ],
    "Aplastic anemia sits under the hypocellular (+ pancytopenia) arm; megaloblastic anemia, PNH and PMF are hypercellular-arm items.",
)

# ==============================================================================
# UNIT 2 — Page 122: classification, inherited syndromes, acquired causes
# ==============================================================================

add(
    S2,
    122,
    "match",
    "Match each inherited aplastic anemia with its printed defect on page 122 — 1) Fanconi's anemia 2) Dyskeratosis congenita 3) Shwachman-Diamond syndrome … A) Autosomal recessive; FANCA > FANCB, FANCC; complex DNA-repair defect B) DKC mutation; telomere repair defect C) Ribosomopathy",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The classification prints Fanconi's anemia (autosomal recessive, FANCA > FANCB/FANCC, complex repair defect), dyskeratosis congenita (DKC mutation, telomere repair) and Shwachman-Diamond syndrome (ribosomopathy).",
)

add(
    S2,
    122,
    "recall",
    "Which features of Fanconi's anemia are printed on page 122?",
    "Short stature, café au lait macules, gonadal dysgenesis, ↑ risk of AML and SCC (head & neck), and esophageal atresia",
    [
        "Tall stature, hypopigmented macules, gonadal hypertrophy, ↑ risk of CML",
        "Short stature, café au lait macules, renal agenesis only, ↑ risk of lymphoma",
        "Normal stature, reticular pigmentation, dystrophic nails, oral leukoplakia",
    ],
    "The Fanconi features list prints short stature, café au lait macules, gonadal dysgenesis, ↑ risk of AML & SCC (head neck), and esophageal atresia.",
)

add(
    S2,
    122,
    "match",
    "Match the Fanconi image panels on page 122 with what each shows — 1) Panel A 2) Panel B 3) Panel C … A) Facial photograph with café au lait pigmentation B) Hand photograph with thumb/radial ray anomaly C) Chromosome breakage figure",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-C, 2-B, 3-A",
        "1-A, 2-C, 3-B",
    ],
    "The printed Fanconi panel shows A the facies with pigmentation, B the hand with a radial-ray/thumb anomaly and C the chromosome breakage karyotype figure.",
)

add(
    S2,
    122,
    "recall",
    "Which two dyskeratosis congenita photographs carry printed captions on page 122, and what do they show?",
    "Reticular skin pigmentation and dystrophic nails",
    [
        "Oral leukoplakia and palmoplantar keratosis",
        "Café au lait macules and absent radii",
        "Nail pitting and alopecia",
    ],
    "The captioned DC photographs are 'Reticular skin pigmentation' and 'Dystrophic nails'.",
)

add(
    S2,
    122,
    "recall",
    "Which two features define Shwachman-Diamond syndrome on page 122?",
    "Pancreatic exocrine insufficiency and metaphyseal dysplasia",
    [
        "Pancreatic endocrine failure and epiphyseal dysplasia",
        "Intestinal lymphangiectasia and metaphyseal chondrodysplasia",
        "Exocrine insufficiency and cortical bone sclerosis",
    ],
    "The syndrome (a ribosomopathy) prints pancreatic exocrine insufficiency and metaphyseal dysplasia.",
)

add(
    S2,
    122,
    "recall",
    "List the acquired aplastic anemia causes printed on page 122, naming the most common.",
    "Idiopathic (m/c), drugs, toxins (benzene), virus (non-A, B, C hepatitis virus), others (PNH), and autoimmune eosinophilic fasciitis (scleroderma mimic)",
    [
        "Idiopathic (m/c), radiation, toxins (lead), virus (EBV), others (SLE)",
        "Drugs (m/c), idiopathic, toxins (arsenic), virus (hepatitis B), others (PNH)",
        "Idiopathic (m/c), drugs, toxins (benzene), virus (HIV), others (hypothyroidism)",
    ],
    "Causes print idiopathic (m/c), drugs, toxins : benzene, virus : non-A, B, C hepatitis virus, others : PNH, and autoimmune : eosinophilic fasciitis (scleroderma mimic).",
)

add(
    S2,
    122,
    "oddoneout",
    "Page 122 lists inherited aplastic anemias. Pick the ODD ONE OUT — the syndrome NOT on that printed list:",
    "Diamond-Blackfan anemia",
    [
        "Fanconi's anemia",
        "Dyskeratosis congenita",
        "Shwachman-Diamond syndrome",
    ],
    "The inherited column prints Fanconi's anemia, dyskeratosis congenita and Shwachman-Diamond syndrome; Diamond-Blackfan anemia is not listed there.",
)

add(
    S2,
    122,
    "truefalse",
    "Judge the page 122 classification statements as printed.",
    "True — Fanconi's anemia is autosomal recessive with FANCA mutations outnumbering FANCB/FANCC",
    [
        "True — Eosinophilic fasciitis, a scleroderma mimic, is listed among autoimmune acquired causes",
        "False — Dyskeratosis congenita is linked to a DKC mutation with defective telomere repair",
        "False — Shwachman-Diamond syndrome is described as a ribosomopathy",
    ],
    "All printed facts hold, so the 'False' framings contradict page 122.",
)

add(
    S2,
    122,
    "recall",
    "Which malignancies does page 122 say are increased in Fanconi's anemia?",
    "AML and squamous cell carcinoma of the head & neck",
    [
        "CML and adenocarcinoma of the stomach",
        "ALL and hepatoblastoma",
        "AML and esophageal adenocarcinoma",
    ],
    "The line prints ↑ risk of AML & SCC (head neck); esophageal atresia is a separate feature bullet.",
)

# ==============================================================================
# UNIT 3 — Page 123: drugs, presentation, severity, treatment
# ==============================================================================

add(
    S3,
    123,
    "match",
    "Match each drug with its printed aplastic-anemia category on page 123 — 1) Busulfan 2) Chloramphenicol 3) Gold 4) D-penicillamine … A) Anticancer drug — dose dependent, temporary myelosuppression B) Dose-independent antibiotic C) Dose-independent metal therapy D) Dose-independent chelating agent",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-C, 3-B, 4-D",
        "1-D, 2-B, 3-C, 4-A",
    ],
    "The dose-dependent column lists anticancer drugs (fluorouracil, mercaptopurine, doxorubicin, cyclophosphamide, busulfan) causing temporary myelosuppression; chloramphenicol, sulfonamides, gold, acetazolamide, PTU and D-penicillamine sit in the dose-independent column.",
)

add(
    S3,
    123,
    "oddoneout",
    "Page 123's dose-dependent (anticancer) column causes temporary myelosuppression. Pick the ODD ONE OUT — the drug NOT in that column:",
    "Chloramphenicol",
    [
        "Fluorouracil",
        "Mercaptopurine",
        "Cyclophosphamide",
    ],
    "Chloramphenicol is printed in the dose-independent column; fluorouracil, mercaptopurine, doxorubicin (Donorubicin as printed), cyclophosphamide and busulfan are the anticancer dose-dependent list.",
)

add(
    S3,
    123,
    "recall",
    "What order of clinical presentation does page 123 print for aplastic anemia?",
    "Bleeding (m/c) > anemia > infection",
    [
        "Infection (m/c) > bleeding > anemia",
        "Anemia (m/c) > infection > bleeding",
        "Bleeding (m/c) > infection > anemia",
    ],
    "Clinical presentation prints bleeding (m/c) > anemia > infection.",
)

add(
    S3,
    123,
    "recall",
    "Which findings argue against a diagnosis of aplastic anemia per page 123?",
    "Hepatomegaly, splenomegaly, lymphadenopathy and fever",
    [
        "Pallor, bruising and petechiae",
        "Pancytopenia with a hypocellular marrow",
        "Mucosal bleeding with a normal spleen",
    ],
    "The line prints 'Features against diagnosis of aplastic anemia : Hepatomegaly, splenomegaly, lymphadenopathy, fever'.",
)

add(
    S3,
    123,
    "recall",
    "State all four severe-aplastic-anemia blood-count thresholds exactly as printed on page 123.",
    "Hb <9 g/dL; reticulocyte <30.0 × 10⁹/L; absolute neutrophil count <0.5 × 10⁹/L; platelet <30.0 × 10⁹/L",
    [
        "Hb <7 g/dL; reticulocyte <20.0 × 10⁹/L; ANC <1.0 × 10⁹/L; platelet <20.0 × 10⁹/L",
        "Hb <9 g/dL; reticulocyte <60.0 × 10⁹/L; ANC <0.5 × 10⁹/L; platelet <50.0 × 10⁹/L",
        "Hb <10 g/dL; reticulocyte <30.0 × 10⁹/L; ANC <1.5 × 10⁹/L; platelet <30.0 × 10⁹/L",
    ],
    "The severe bracket prints Hb <9 g/dl, reticulocyte <30.0 × 10⁹/L, ANC <0.5 × 10⁹/L and platelet <30.0 × 10⁹/L (values verified visually as printed) → Rx : AHSCT.",
)

add(
    S3,
    123,
    "recall",
    "What treatment does the severe bracket on page 123 point to?",
    "AHSCT (allogeneic hematopoietic stem cell transplant)",
    [
        "Equine ATG alone",
        "Eltrombopag monotherapy",
        "Cyclosporine alone",
    ],
    "The brace of severe criteria points to 'Rx : AHSCT'.",
)

add(
    S3,
    123,
    "recall",
    "Describe the bone marrow picture printed for aplastic anemia on page 123.",
    "Hypocellular bone marrow with fat cells",
    [
        "Hypercellular marrow with fibrosis",
        "Hypocellular marrow with gelatinous transformation only",
        "Normocellular marrow with increased megakaryocytes",
    ],
    "The image caption prints 'Hypocellular bone marrow with fat cells'.",
)

add(
    S3,
    123,
    "recall",
    "State the printed first-line immunosuppressive regimen for aplastic anemia with its time to action and success rate.",
    "Equine ATG + cyclosporine; time to action 6 months; success rate 50%",
    [
        "Rabbit ATG + tacrolimus; 3 months; 70%",
        "Equine ATG + cyclosporine; 6 weeks; 90%",
        "Methylprednisolone + cyclosporine; 6 months; 50%",
    ],
    "Treatment prints equine ATG + cyclosporine with time to action 6 months and success rate 50%.",
)

add(
    S3,
    123,
    "recall",
    "Which thrombopoietic analogue is listed in the page 123 treatment of aplastic anemia?",
    "Eltrombopag",
    [
        "Romiplostim",
        "Luspatercept",
        "Danazol",
    ],
    "The last bullet prints eltrombopag : thrombopoietic analogue.",
)

add(
    S3,
    123,
    "numeric",
    "What success rate does page 123 quote for equine ATG + cyclosporine in aplastic anemia?",
    "50%",
    [
        "30%",
        "70%",
        "90%",
    ],
    "The line prints 'Success rate : 50%'.",
)

add(
    S3,
    123,
    "truefalse",
    "Assess the page 123 statements as printed.",
    "True — Bleeding is the most common presentation of aplastic anemia, ahead of anemia and infection",
    [
        "True — Hepatomegaly, splenomegaly, lymphadenopathy and fever are features against the diagnosis",
        "False — Severe disease (per the printed thresholds) is directed to AHSCT",
        "False — The marrow in aplastic anemia is hypocellular with fat cells",
    ],
    "All printed facts hold, so the 'False' framings contradict page 123.",
)

# ==============================================================================
# UNIT 4 — Page 124: pure red cell aplasia and MDS presentation
# ==============================================================================

add(
    S4,
    124,
    "recall",
    "Which acquired causes of pure red cell aplasia does page 124 print?",
    "Thymoma and CLL",
    [
        "Thymoma and CML",
        "Hodgkin's disease and CLL",
        "Thymoma and SLE only",
    ],
    "Causes print thymoma/CLL (acquired).",
)

add(
    S4,
    124,
    "recall",
    "How does page 124 describe transient aplastic crisis, its smear and its treatment?",
    "Sudden reticulocytopenia; smear shows giant pronormoblasts; Rx : IVIG",
    [
        "Sudden leukopenia; smear shows giant myeloblasts; Rx : G-CSF",
        "Gradual reticulocytopenia; smear shows spherocytes; Rx : steroids",
        "Sudden thrombocytopenia; smear shows megakaryocyte nuclei; Rx : platelets",
    ],
    "Transient aplastic crisis prints sudden reticulocytopenia, smear giant pronormoblasts and Rx : IVIG.",
)

add(
    S4,
    124,
    "recall",
    "What is MDS also called on page 124, and which two lineage statements accompany it?",
    "AKA myeloid neoplasm; dysplasia + ineffective erythropoiesis = MDS, while myeloblast proliferation (immature myeloid cell) = acute myeloid leukemia",
    [
        "AKA myeloid failure; effective erythropoiesis with dysplasia = MDS; lymphoblast proliferation = ALL",
        "AKA preleukemia only; dysplasia + ineffective granulopoiesis = MDS; monoblast proliferation = CML",
        "AKA myeloid neoplasm; dysplasia + ineffective erythropoiesis = AML; myeloblast proliferation = MDS",
    ],
    "Page 124 prints MDS AKA myeloid neoplasm; dysplasia + ineffective erythropoiesis : MDS; MDS + MPN overlap : chronic myelomonocytic leukemia; myeloblast proliferation (immature myeloid cell) : acute myeloid leukemia.",
)

add(
    S4,
    124,
    "recall",
    "Which overlap syndrome does page 124 name between MDS and MPN?",
    "Chronic myelomonocytic leukemia",
    [
        "Chronic myeloid leukemia",
        "Juvenile myelomonocytic leukemia",
        "Atypical CML",
    ],
    "The line prints 'MDS + MPN overlap : Chronic myelomonocytic leukemia'.",
)

add(
    S4,
    124,
    "match",
    "Match the MDS presentation contrast printed on page 124 — 1) Global age 2) India age 3) Global sex/lineage 4) India sex/lineage … A) 70 years B) 40–60 years (D/t 5q deletion) C) M > F with single/multilineage disease D) Female predominance with RBC-lineage disease (lenalidomide good response)",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-B, 3-D, 4-C",
        "1-C, 2-D, 3-A, 4-B",
    ],
    "Presentation prints global 70 yrs, M > F, single/multilineage disease; India 40-60 yrs (D/t 5q deletion), female predominance, RBC lineage disease and lenalidomide (good response).",
)

add(
    S4,
    124,
    "numeric",
    "Why is MDS younger in India per page 124, and what is the printed age range?",
    "40–60 years, due to 5q deletion",
    [
        "30–50 years, due to trisomy 8",
        "40–60 years, due to monosomy 7",
        "50–70 years, due to 5q deletion",
    ],
    "The India column prints 40-60 yrs (D/t 5q deletion).",
)

add(
    S4,
    124,
    "recall",
    "Summarize the marrow, transformation and symptom notes for MDS on page 124.",
    "Pancytopenia with hypercellular (80%) or hypocellular (20%) marrow; progresses to AML (25%); no extramedullary hematopoiesis; m/c symptom fatigue",
    [
        "Pancytopenia with hypocellular (80%) marrow; progresses to AML (50%); massive splenomegaly; m/c symptom fever",
        "Pancytopenia with hypercellular (80%) marrow; progresses to CML (25%); no EMH; m/c symptom bleeding",
        "Isolated anemia with hypercellular marrow; no AML progression; EMH present; m/c symptom fatigue",
    ],
    "The bullets print pancytopenia hypercellular (80%)/hypocellular (20%), progresses to AML (25%), no extramedullary hematopoiesis, and m/c symptom fatigue.",
)

add(
    S4,
    124,
    "recall",
    "List the printed RBC-lineage blood parameters of MDS on page 124, including the stain used for ring sideroblasts.",
    "Anemia (m/c presentation), ringed sideroblasts (SF3B1 mutation MDS), oval macrocytes (m/c), megaloblasts and nucleated RBCs, Howell-Jolly bodies, basophilic stippling and Cabot rings; ring sideroblasts shown in Perls staining",
    [
        "Microcytic cells only, target cells and pencil cells; iron stain Prussian blue negative",
        "Anemia, spherocytes and schistocytes; ring sideroblasts on H&E",
        "Polycythemia with macrocytes; ring sideroblasts on PAS stain",
    ],
    "The RBC list prints anemia (m/c), ringed sideroblasts (SF3B1 mutation MDS), oval macrocytes (m/c), megaloblasts/nucleated RBC, Howell-Jolly body/basophilic stippling/Cabot's ring, with the image 'Ring sideroblasts in Perls staining'.",
)

add(
    S4,
    124,
    "oddoneout",
    "Page 124 lists several red-cell inclusions/shapes for MDS. Pick the ODD ONE OUT — the one NOT printed there:",
    "Pencil (cigar) cells",
    [
        "Howell-Jolly bodies",
        "Basophilic stippling",
        "Cabot rings",
    ],
    "The printed list is Howell-Jolly body, basophilic stippling and Cabot's ring (with oval macrocytes and megaloblasts); pencil cells belong to the microcytic-smear chapter, not this page.",
)

add(
    S4,
    124,
    "truefalse",
    "Judge the page 124 MDS statements as printed.",
    "True — MDS shows no extramedullary hematopoiesis",
    [
        "True — The most common MDS symptom is fatigue",
        "False — MDS progresses to AML in 25% as printed",
        "False — Indian MDS shows female predominance with RBC-lineage disease responding to lenalidomide",
    ],
    "All printed facts hold, so the 'False' framings contradict page 124.",
)

# ==============================================================================
# UNIT 5 — Page 125: WBC/platelet parameters, scoring, treatment flowchart
# ==============================================================================

add(
    S5,
    125,
    "recall",
    "Which WBC findings does page 125 print for MDS?",
    "Blast cells 5–19%, pseudo-Pelger-Huët (2 lobes), hypersegmented forms, toxic granules and Döhle bodies",
    [
        "Blast cells ≥20%, hypo-segmented forms only, no toxic granules",
        "Blast cells 5–19%, hypersegmented forms only, Auer rods",
        "No blasts, pseudo-Pelger-Huët (3 lobes), toxic granules only",
    ],
    "The WBC list prints blast cells 5-19%, pseudo Pelger-Huët (2 lobes), hypersegmented, toxic granules and Döhle bodies.",
)

add(
    S5,
    125,
    "match",
    "Match each platelet/megakaryocyte image label on page 125 with its picture — 1) 'Pawn ball (multiple nuclear lobes) megakaryocyte' 2) 'Binucleate megakaryocyte' 3) 'Dysplastic megakaryocyte' … A) Megakaryocyte whose lobes resemble a pawn-ball arrangement B) Megakaryocyte with two nuclei C) Generic dysplastic megakaryocyte photograph",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-C, 2-B, 3-A",
        "1-A, 2-C, 3-B",
    ],
    "The three printed dysplastic platelet-lineage captions are pawn ball (multiple nuclear lobes) megakaryocyte, binucleate megakaryocyte and dysplastic megakaryocyte.",
)

add(
    S5,
    125,
    "recall",
    "List the diagnostic features of MDS printed on page 125.",
    "Pancytopenia with >10% dysplastic cells; hypocellular; cytogenetic abnormality; no AML; no other cause",
    [
        "Pancytopenia with >20% blasts; hypercellular; no cytogenetic abnormality; AML present",
        "Isolated thrombocytopenia with >10% dysplastic cells; hypercellular; cytogenetic abnormality; no AML",
        "Pancytopenia with >10% dysplastic cells; hypocellular; normal cytogenetics; AML excluded by blasts >20%",
    ],
    "Diagnostic features print pancytopenia >10% dysplastic cells, hypocellular, cytogenic abnormality, no AML and no other cause.",
)

add(
    S5,
    125,
    "match",
    "Match the printed gene lesions with their prognostic tier on page 125 — 1) 7q deletion, monosomy 7 2) 5q deletion, 20q deletion 3) 11q deletion … A) Poor (seen in paediatric MDS) B) Good C) Best",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The prognosis table prints poor for 7q deletion/monosomy 7 (seen in paediatric MDS), good for 5q deletion/20q deletion and best for 11q deletion.",
)

add(
    S5,
    125,
    "recall",
    "Which scoring system is named on page 125 for MDS prognosis?",
    "Revised International Prognostic Scoring System",
    [
        "Sokal index",
        "Hasford prognostic scale",
        "WHO classification score",
    ],
    "The heading prints 'Revised international prognostic scoring system'.",
)

add(
    S5,
    125,
    "recall",
    "Walk the single-lineage arm of the page 125 MDS treatment flowchart.",
    "Single lineage → 5q deletion: present → lenalidomide; absent → erythropoietin",
    [
        "Single lineage → 5q deletion: present → erythropoietin; absent → lenalidomide",
        "Single lineage → trisomy 8: present → lenalidomide; absent → decitabine",
        "Single lineage → 5q deletion: present → azacytidine; absent → transplant",
    ],
    "The flowchart prints single lineage → 5q deletion → present : lenalidomide, absent : erythropoietin.",
)

add(
    S5,
    125,
    "recall",
    "Walk the trilineage arm of the page 125 MDS treatment flowchart and name the hypomethylating agents.",
    "Trilineage → bone marrow transplantation or hypomethylating agent; the agents are azacytidine and decitabine",
    [
        "Trilineage → lenalidomide or erythropoietin; agents are hydroxyurea and cytarabine",
        "Trilineage → hypomethylating agent only; agents are azacytidine and cytarabine",
        "Trilineage → observation or splenectomy; agents are decitabine and cladribine",
    ],
    "The trilineage arm branches to bone marrow transplantation and hypomethylating agent, with azacytidine and decitabine listed under the latter.",
)

add(
    S5,
    125,
    "recall",
    "What does the page 125 note at the top of the page qualify?",
    "Other conditions (as printed) — the page opens with 'Note : Other conditions' continuing the discussion from page 124",
    [
        "The blast percentage required for AML",
        "The drugs used in PRCA",
        "The definition of severe aplastic anemia",
    ],
    "Page 125 opens with 'Note : Other conditions' as printed, bridging from the p124 MDS presentation.",
)

add(
    S5,
    125,
    "truefalse",
    "Assess the page 125 statements as printed.",
    "True — Pseudo-Pelger-Huët cells in MDS are hypolobated (2 lobes)",
    [
        "True — Monosomy 7/7q deletion carries a poor prognosis and is seen in paediatric MDS",
        "False — Lenalidomide is the printed single-lineage treatment when the 5q deletion is present",
        "False — Azacytidine and decitabine are the printed hypomethylating agents",
    ],
    "All printed facts hold, so the 'False' framings contradict page 125.",
)

add(
    S5,
    125,
    "scenario",
    "An elderly MDS patient's cytogenetics returns an isolated 5q deletion with single-lineage disease. Per the page 125 flowchart and prognosis table, which treatment and prognostic tier apply?",
    "Lenalidomide; good prognosis tier",
    [
        "Erythropoietin; poor prognosis tier",
        "Azacytidine; best prognosis tier",
        "Bone marrow transplantation; poor prognosis tier",
    ],
    "The single-lineage arm sends 5q-deletion-present disease to lenalidomide, and the prognosis table places 5q deletion in the good tier.",
)


GUIDES = {
    S1: (
        "Approach to Pancytopenia: Marrow Cellularity Flowchart & Aplastic Anemia Overview",
        "Diseases: aplastic anemia, MDS, pure red cell aplasia, myelophthisis (secondary myelofibrosis); workup: bone marrow aspiration + biopsy → cellularity.\n"
        "Hypercellular arm: acute leukemia (unless proven otherwise; adults AML 80%/ALL 20%), MDS, PMF, hairy cell leukemia (good prognosis), megaloblastic anemia (good prognosis), PNH, systemic (SLE, HIV, TB, brucellosis, leishmaniasis, sarcoidosis).\n"
        "Hypocellular arm: + pancytopenia (aplastic anemia, 20% of MDS, aleukemic leukemia, copper deficiency, lymphoma); ± pancytopenia (Q fever, Legionella, anorexia, TB); PMF = pancytopenia + fibrosis; hairy cell = pancytopenia + massive splenomegaly.\n"
        "Aplastic anemia intro: p121 prints 'hypercellular' as a slip (flowchart and p123 show hypocellular); bimodal (inherited <20 yrs, acquired >60 yrs); m/c cause drug dependent (good prognosis); m/c infection non-A, non-B hepatitis; 'bad prognosis' as printed.",
    ),
    S2: (
        "Inherited vs Acquired Aplastic Anemia: Fanconi, Dyskeratosis Congenita, Shwachman-Diamond",
        "Inherited: Fanconi (AR, FANCA > FANCB/FANCC, complex DNA-repair defect; short stature, café au lait macules, gonadal dysgenesis, ↑ AML & head-neck SCC, esophageal atresia; panels A facies, B hand/thumb anomaly, C chromosome breakage), dyskeratosis congenita (DKC mutation, telomere repair; captioned photos reticular skin pigmentation and dystrophic nails), Shwachman-Diamond (ribosomopathy; pancreatic exocrine insufficiency, metaphyseal dysplasia).\n"
        "Acquired: idiopathic (m/c), drugs, toxins (benzene), virus (non-A, B, C hepatitis), others (PNH), autoimmune eosinophilic fasciitis (scleroderma mimic).",
    ),
    S3: (
        "Drugs Causing Aplastic Anemia, Presentation, Severity Criteria & Treatment",
        "Dose dependent (anticancer → temporary myelosuppression): fluorouracil, mercaptopurine, doxorubicin, cyclophosphamide, busulfan; dose independent: chloramphenicol, sulfonamides, gold, acetazolamide, PTU, D-penicillamine.\n"
        "Presentation bleeding (m/c) > anemia > infection; features against diagnosis: hepatomegaly, splenomegaly, lymphadenopathy, fever.\n"
        "Severe thresholds (as printed): Hb <9 g/dl, reticulocyte <30.0 × 10⁹/L, ANC <0.5 × 10⁹/L, platelet <30.0 × 10⁹/L → Rx AHSCT; marrow hypocellular with fat cells; treatment equine ATG + cyclosporine (6 months to act, 50% success), AHSCT, eltrombopag (TPO analogue).",
    ),
    S4: (
        "Pure Red Cell Aplasia & MDS Overview: Global Versus India Presentation",
        "PRCA: acquired thymoma/CLL; transient aplastic crisis = sudden reticulocytopenia, giant pronormoblasts on smear, Rx IVIG.\n"
        "MDS AKA myeloid neoplasm: dysplasia + ineffective erythropoiesis; MDS/MPN overlap = CMML; myeloblast proliferation = AML.\n"
        "Global 70 yrs, M > F, single/multilineage vs India 40–60 yrs (5q deletion), female predominance, RBC-lineage disease, lenalidomide good response; hypercellular 80%/hypocellular 20%; AML progression 25%; no EMH; fatigue m/c.\n"
        "RBC parameters: anemia (m/c), ringed sideroblasts (SF3B1), oval macrocytes (m/c), megaloblasts/nucleated RBCs, HJ bodies/basophilic stippling/Cabot rings; Perls staining image.",
    ),
    S5: (
        "MDS Blood Parameters, Prognostic Scoring & Treatment Flowchart",
        "WBC: blasts 5–19%, pseudo-Pelger-Huët (2 lobes), hypersegmented, toxic granules, Döhle bodies; platelet images: pawn-ball multinucleated, binucleate and dysplastic megakaryocytes.\n"
        "Diagnostic features: pancytopenia with >10% dysplastic cells, hypocellular, cytogenetic abnormality, no AML, no other cause; R-IPSS named; prognosis poor = 7q deletion/monosomy 7 (paediatric), good = 5q/20q deletion, best = 11q deletion.\n"
        "Treatment: single lineage → 5q deletion present lenalidomide / absent erythropoietin; trilineage → bone marrow transplantation or hypomethylating agent (azacytidine, decitabine).",
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
