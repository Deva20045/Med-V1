#!/usr/bin/env python3
"""Generate Chapter 27: Hodgkin's Disease (Book p153–158).

Every question is anchored to a specific line, table cell, flowchart branch,
histology callout, PET scan panel, or Note box in uploads/02.pdf (PDF pages
36–41 = Book pages 153–158) in strict book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 27
TITLE = "Hodgkin's Disease"
PAGES = "153-158"

S1 = "Germinal-Centre Physiology Diagram, B-Cell Tumor Origin Table & NF-κB (NK-κβ) Pathogenesis"
S2 = "Dark-Zone Origin & Chr 9 PDL1 Aberration, Stage Cure Rates, HL vs NHL Comparison Table & Pel-Ebstein Fever"
S3 = "Reed-Sternberg Cell Morphology, NLPHD vs Classical HD Classification (Worldwide vs India) & Comparison Table"
S4 = "EBV/ALCL Recap Notes, Hodgkin Clinical Features, Paraneoplastic Syndromes & NS vs MC Subtype Profiles"
S5 = "Richter Recap, Staging Workup (Excision Biopsy & FDG-PET), Unfavourable Criteria & β2-Microglobulin Note"
S6 = "Chemotherapy Response by Subtype, ABVD Toxicity Table, Deauville PET-Adapted Protocol, Brentuximab, BEACOPP & ISRT"

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
# UNIT 1 — Page 153: Physiology Oval, Origin Table & Pathogenesis
# ==============================================================================

add(
    S1,
    153,
    "recall",
    "In the 'Physiology :' lymph node oval diagram at the top of page 153, which cell populations populate the Dark Zone versus the Light Zone of the Germinal center (GC)?",
    "Dark Zone contains Centroblasts; Light Zone contains Centrocytes",
    [
        "Dark Zone contains Centrocytes; Light Zone contains Centroblasts",
        "Dark Zone contains Plasma cells; Light Zone contains Naive pro-B cells",
        "Dark Zone contains Reed-Sternberg cells; Light Zone contains Memory T-cells",
    ],
    "Inside the Germinal center (GC) oval under 'Physiology :' on page 153, the top half is labelled 'Dark Zone (Centroblasts)' and the bottom half is labelled 'Light Zone (Centrocytes)'.",
)

add(
    S1,
    153,
    "recall",
    "In the 'Physiology :' diagram on page 153, what two post-germinal cellular differentiation pathways exit from the Light Zone (Centrocytes)?",
    "Rightward via Post-GC → Memory B-cells, and downward → Plasmablasts → Plasma cells",
    [
        "Backward via Pre-GC → Pro-B cells, and upward → Common myeloid progenitors",
        "Directly into thymic T-lymphoblasts and peripheral NK cells",
        "Exclusively into bone marrow megakaryocytes without plasma-cell formation",
    ],
    "Arrows leaving 'Light Zone (Centrocytes)' on page 153 travel rightward to 'Post-GC → Memory B-cells' and vertically downward to 'Plasmablasts → Plasma cells'.",
)

add(
    S1,
    153,
    "match",
    "In the 'Pathology → Origin :' table on page 153, match rows 1–4 of B-cell site of origin with their corresponding tumor — 1) Centrocytes 2) Pre-GC 3) Centroblasts 4) Post-GC … A) Marginal zone lymphoma (MZL) B) Follicular lymphoma C) Mantle-cell lymphoma (MCL) D) Diffuse large B-cell lymphoma (DLBCL) & Burkitt's lymphoma",
    "1-B, 2-C, 3-D, 4-A",
    [
        "1-C, 2-B, 3-D, 4-A",
        "1-B, 2-D, 3-C, 4-A",
        "1-A, 2-C, 3-B, 4-D",
    ],
    "Rows 1–4 of the 'Origin :' table on page 153 map: Centrocytes → Follicular lymphoma; Pre-GC → Mantle-cell lymphoma (MCL); Centroblasts → DLBCL & Burkitt's lymphoma; Post-GC → Marginal zone lymphoma (MZL).",
)

add(
    S1,
    153,
    "recall",
    "In rows 5–6 of the 'Origin :' table on page 153, which tumors arise from 'Plasmablast' versus 'Plasma cells'?",
    "Plasmablast → Activated B-cell Diffuse B-cell Lymphoma; Plasma cells → Multiple myeloma",
    [
        "Plasmablast → Follicular lymphoma; Plasma cells → Mantle-cell lymphoma",
        "Plasmablast → Multiple myeloma; Plasma cells → Burkitt's lymphoma",
        "Plasmablast → Hairy cell leukemia; Plasma cells → Small lymphocytic lymphoma",
    ],
    "Rows 5–6 of the 'Origin :' table on page 153 list: Plasmablast → Activated B-cell Diffuse B-cell Lymphoma; Plasma cells → Multiple myeloma.",
)

add(
    S1,
    153,
    "oddoneout",
    "In row 7 of the 'Origin :' table on page 153, all of the following neoplasms arise from 'Memory B cells' EXCEPT:",
    "Mantle-cell lymphoma (MCL)",
    [
        "Small lymphocytic lymphoma (SLL)",
        "Waldenström's macroglobulinemia",
        "Hairy cell leukemia",
    ],
    "Row 7 of the 'Origin :' table on page 153 lists under Memory B cells: '• Small lymphocytic lymphoma (SLL) • Waldenström's macroglobulinemia • Hairy cell leukemia', whereas Mantle-cell lymphoma (MCL) arises from Pre-GC.",
)

add(
    S1,
    153,
    "recall",
    "At the bottom of page 153 under 'Pathogenesis :' of Hodgkin's Disease, which transcription-factor pathway upregulation (including its exact printed spelling) and sex ratio are listed?",
    "Upregulation of NF-κB [printed as NK-κβ] seen; M > F",
    [
        "Constitutive BCR-ABL1 tyrosine kinase fusion; F > M",
        "Somatic BRAF V600E kinase mutation only; F > M",
        "Germline TP53 deletion with loss of c-myc; M = F",
    ],
    "At the bottom of page 153 under 'Pathogenesis :': '• Upregulation of NK-κβ [NF-κB, as printed] seen. • M>F.'",
)


# ==============================================================================
# UNIT 2 — Page 154: Chr 9 PDL1 Aberration, Cure Rates, HL vs NHL & Pel-Ebstein Fever
# ==============================================================================

add(
    S2,
    154,
    "recall",
    "In the top flowchart on page 154, which zone of the germinal centre do B-cells enter as the cell of origin of Hodgkin's disease, and what two normal processes do they undergo there?",
    "B-cells move into the dark zone of GC (origin) and undergo multiple somatic hypermutations and affinity maturation",
    [
        "B-cells move into the splenic red pulp and undergo class-switch deletion without somatic hypermutation",
        "B-cells remain arrested in the bone marrow pro-B stage with incomplete V(D)J heavy-chain rearrangement",
        "B-cells migrate into thymic Hassall corpuscles and rearrange T-cell receptor gamma chains",
    ],
    "Lines 1–2 at the top of page 154 read: 'B-cells move into the dark zone of GC (origin) → Undergo multiple somatic hypermutations and affinity maturation.'",
)

add(
    S2,
    154,
    "fillup",
    "In the top flowchart on page 154, while surviving GC B-cells move to the light zone, cells slated for apoptosis that acquire a ______ gene aberration (chr 9) experience ↓ apoptosis and cause Hodgkin's disease.",
    "PDL₁",
    [
        "BCL-2",
        "Cyclin D1",
        "MYD88",
    ],
    "The right branch of the top flowchart on page 154 reads: 'Others undergo apoptosis —[PDL₁ gene aberration (chr 9)]→ ↓ apoptosis : Hodgkin's disease.'",
)

add(
    S2,
    154,
    "numeric",
    "Under 'Note : Cure Rates :' on page 154, what exact cure rates are listed for Early stage (I/II) favorable, Early stage (I/II) unfavorable, and Advanced (III/IV) Hodgkin's disease?",
    "Early stage (I/II) favorable: >90%; Early stage (I/II) unfavorable: ≥85%; Advanced (III/IV): ~80%",
    [
        "Early stage (I/II) favorable: 50%; Early stage (I/II) unfavorable: 30%; Advanced (III/IV): <10%",
        "Early stage (I/II) favorable: 70–75%; Early stage (I/II) unfavorable: 40–45%; Advanced (III/IV): 20%",
        "Early stage (I/II) favorable: 100%; Early stage (I/II) unfavorable: 50%; Advanced (III/IV): 15%",
    ],
    "Under 'Note : Cure Rates :' on page 154: '• Early stage (I/II) favorable : >90%. • Early stage (I/II) unfavorable : ≥85%. • Advanced (III/IV) : ~80%.'",
)

add(
    S2,
    154,
    "numeric",
    "In the 'Differences between HL and NHL' table on page 154, what bimodal age peaks define Hodgkin's Lymphoma compared with Non-Hodgkin's Lymphoma?",
    "HL is bimodal — most common peak: 15–34 yrs and 2nd peak: >60 yrs; NHL presents at >60 yrs",
    [
        "HL presents exclusively at <10 yrs; NHL is bimodal at 15–34 yrs and >60 yrs",
        "HL is bimodal at <5 yrs and 40–50 yrs; NHL presents at median age 13 yrs",
        "Both HL and NHL have a single childhood peak at 2–9 yrs only",
    ],
    "Row 2 ('Age of presentation') of the HL vs NHL table on page 154 shows: HL = 'Bimodal → m/c : 15–34 yrs; 2nd peak : >60 yrs' vs NHL = '>60 yrs'.",
)

add(
    S2,
    154,
    "recall",
    "In the 'Differences between HL and NHL' table on page 154, how do 'Lymphoid tissue involved' and 'Contiguous involvement (lymph nodes share the same border)' contrast between HL and NHL?",
    "HL: Nodal disease with Contiguous involvement ⊕; NHL: Extranodal (m/c: GIT — e.g., MZL stomach maltoma, MCL lymphomatoid polyposis of GIT; Waldeyer's ring involvement) with Contiguous involvement ⊖",
    [
        "HL: Extranodal GIT and Waldeyer's ring disease with non-contiguous spread ⊖; NHL: purely nodal contiguous spread ⊕",
        "HL and NHL both involve Waldeyer's ring first and spread strictly non-contiguously via bloodstream",
        "HL involves bone marrow exclusively without nodal borders; NHL involves mediastinal thymus contiguously",
    ],
    "Rows 3 & 6 of the HL vs NHL table on page 154 state: Lymphoid tissue involved — 'Nodal' (HL) vs 'Extranodal (m/c : GIT) eg : MZL : Stomach (Maltoma); MCL : Lymphomatoid polyposis of GIT; Waldeyer's ring involvement' (NHL); Contiguous involvement — ⊕ (HL) vs ⊖ (NHL).",
)

add(
    S2,
    154,
    "recall",
    "In rows 4, 5, and 7 of the 'Differences between HL and NHL' table on page 154, how do CNS involvement, B symptoms, and EBV involvement compare between HL and NHL?",
    "HL: Paraneoplastic cerebellar degeneration seen, B symptoms (weight loss, night sweats, Pel-Ebstein fever) in 30% of patients, EBV involvement ⊕⊕⊕; NHL: CNS not common, B symptoms '–', EBV involvement ⊕",
    [
        "HL: CNS not common, B symptoms absent, EBV ⊖; NHL: Paraneoplastic cerebellar degeneration in 80%, EBV ⊕⊕⊕",
        "HL: Direct meningeal blast infiltration in 50%, B symptoms in 95%, EBV ⊖; NHL: Pel-Ebstein fever in 70%",
        "Both HL and NHL show identical 30% Pel-Ebstein fever and ⊕⊕⊕ EBV positivity",
    ],
    "Rows 4, 5, and 7 on page 154 show: CNS involvement — 'Paraneoplastic cerebellar degeneration seen' (HL) vs 'Not common' (NHL); B symptoms — '[Weight loss, night sweats, Pel-Ebstein fever] in 30% of patients' (HL) vs '–' (NHL); EBV involvement — '⊕⊕⊕' (HL) vs '⊕' (NHL).",
)

add(
    S2,
    154,
    "recall",
    "How is 'Pel-Ebstein fever' defined and illustrated in the 'Note :' at the bottom of page 154?",
    "Low-grade irregular fever that spikes gradually, cycling between 'Cyclical fever' and 'Afebrile' intervals",
    [
        "High continuous 40°C plateau fever lasting 2 weeks with relative bradycardia and rose spots",
        "Strict tertian 48-hour paroxysms of rigors, drenching diaphoresis, and hemolytic crisis",
        "Single self-limiting 24-hour drug fever immediately following bleomycin infusion",
    ],
    "At the bottom of page 154 under 'Note :': '• Pel-Ebstein fever : Low grade irregular fever, spikes gradually', accompanied by a cyclical loop diagram alternating 'Cyclical fever' ↔ 'Afebrile'.",
)


# ==============================================================================
# UNIT 3 — Page 155: RS Cell, NLPHD vs Classical Classification & Comparison Table
# ==============================================================================

add(
    S3,
    155,
    "recall",
    "At the top of page 155, what is the identification hallmark of Hodgkin's Disease and what are the four listed morphological/diagnostic points of the 'RS-cell'?",
    "Reed-Sternberg cells (RS) in inflammatory background — bilobed nucleus, prominent eosinophilic nucleoli, separated by a clear space from nuclear membrane, and specific for HL if inflammatory background +ve",
    [
        "Mononuclear eccentric nucleus with circumferential hairy projections, abundant pale cytoplasm, and diagnostic without background inflammation",
        "Small round hyperchromatic nucleus with clumped chromatin, absent nucleoli, and smudge artifacts on peripheral blood smear",
        "Multilobed hypersegmented nucleus with bundles of MPO+ Auer rods and absence of perinucleolar halo",
    ],
    "At the top of page 155 next to the RS-cell photomicrograph: 'Identification features of HD : Reed-Sternberg cells (RS) in inflammatory background. RS-cell : • Bilobed nucleus. • Prominent eosinophilic nucleoli. • Separated by a clear space from nuclear membrane. • Specific for HL if inflammatory background +ve.'",
)

add(
    S3,
    155,
    "management",
    "Under 'Classification' on page 155, what four clinical/management features characterize 'Nodular lymphocyte predominant HD'?",
    "Benign entity, excellent prognosis, axillary lymph node involved, and Rx: radiation of involved node",
    [
        "Aggressive fatal entity, poor prognosis, bulky mediastinal mass with SVC obstruction, and Rx: upfront allogeneic BMT",
        "HIV-associated disseminated entity, extensive B symptoms, retroperitoneal nodes, and Rx: 8 cycles of BEACOPP",
        "EBV-driven nasal destructive entity, very poor prognosis, nasal mass, and Rx: CODOX-M/IVAC",
    ],
    "Under 'Classification' on page 155: 'Nodular lymphocyte predominant HD → • Benign entity. • Excellent prognosis. • Axillary lymph node involved. • Rx : Radiation of involved node.'",
)

add(
    S3,
    155,
    "recall",
    "Under 'Classical HD' on page 155, which subtype is most common worldwide and which subtype is most common in India?",
    "Nodular sclerosis (NS) : most common worldwide; Mixed cellularity (MC) : most common in India",
    [
        "Mixed cellularity (MC) : most common worldwide; Nodular sclerosis (NS) : most common in India",
        "Lymphocyte rich (LR) : most common worldwide; Lymphocyte depleted (LD) : most common in India",
        "Lymphocyte depleted (LD) : most common worldwide; Nodular LP-HD : most common in India",
    ],
    "Under 'Classical HD' on page 155: '• Lymphocyte rich (LR) • Lymphocyte depleted (LD) • Nodular sclerosis (NS) : m/c worldwide • Mixed cellularity (MC) : m/c in India.'",
)

add(
    S3,
    155,
    "recall",
    "In rows 1–2 of the 'Classical vs Nodular' comparison table on page 155, how do Immunophenotyping and B symptoms differ between Classical HD and Nodular LP-HD?",
    "Classical HD: CD15+, CD30+ with B symptoms ⊕; Nodular LP-HD: CD20+, CD45+, Surface immunoglobulin +ve with B symptoms Absent",
    [
        "Classical HD: CD20+, CD45+, Surface Ig +ve with B symptoms Absent; Nodular LP-HD: CD15+, CD30+ with B symptoms ⊕",
        "Classical HD: CD5+, Cyclin D1+; Nodular LP-HD: CD10+, BCL-2+, t(14;18)",
        "Classical HD and Nodular LP-HD both express CD15+, CD30+, CD20+, and Surface Ig with identical B symptoms",
    ],
    "Rows 1–2 of the comparison table on page 155 show: Immunophenotyping — 'CD15+, CD30+' (Classical) vs 'CD20+, CD45+, Surface immunoglobulin +ve' (Nodular); B symptoms — '⊕' vs 'Absent'.",
)

add(
    S3,
    155,
    "numeric",
    "In row 3 ('EBV involvement') of the comparison table on page 155, how does EBV status contrast between Classical HD and Nodular LP-HD?",
    "Classical HD is EBV ⊕ following the 100/70/40/20 rule (LD → 100%, MC → 70%, NS → 40%, LR → 20%); Nodular LP-HD is EBV ⊖",
    [
        "Classical HD is EBV ⊖ across all subtypes; Nodular LP-HD is 100% EBV ⊕",
        "Classical HD follows LR → 100%, NS → 70%, MC → 40%, LD → 20%; Nodular LP-HD is 50% EBV ⊕",
        "Both Classical HD and Nodular LP-HD are 95% H. pylori positive and EBV negative",
    ],
    "Row 3 ('EBV involvement') on page 155 lists Classical = '⊕ 100/70/40/20 rule for EBV involvement : EBV +ve cases in LD → 100%, MC → 70%, NS → 40%, LR → 20%' vs Nodular = '⊖'.",
)

add(
    S3,
    155,
    "match",
    "In the 'Histology' row at the bottom of page 155, match each Hodgkin subtype with its exact printed RS-cell histological description — 1) Lymphocyte depleted (LD) 2) Mixed cellularity (MC) 3) Nodular sclerosis (NS) 4) Nodular LP-HD … A) Lacunar RS cells B) Popcorn RS cell / Lymphocyte histiocyte cells C) RS cell absent (as printed on p155) D) Classical RS cells",
    "1-C, 2-D, 3-A, 4-B",
    [
        "1-D, 2-C, 3-A, 4-B",
        "1-C, 2-A, 3-D, 4-B",
        "1-B, 2-D, 3-A, 4-C",
    ],
    "In the 'Histology' row at the bottom of page 155: Classical column lists '• LD : RS cell absent [as printed on p155; standard texts describe abundant pleomorphic RS cells with lymphocyte depletion], • MC : Classical RS cells, • NS : Lacunar RS cells, • LR : Paucity of RS cells'; Nodular column lists 'Popcorn RS cell / Lymphocyte histiocyte cells.'",
)


# ==============================================================================
# UNIT 4 — Page 156: EBV/ALCL Notes, Clinical Features, Paraneoplastic & NS/MC Profiles
# ==============================================================================

add(
    S4,
    156,
    "fillup",
    "At the top of page 156 under 'Note : EBV associated lymphomas → NHL → T cell type', Extranodal NK T-lymphoma carries a very poor prognosis and classically presents with a ______ mass.",
    "nasal",
    [
        "jaw",
        "thymic",
        "testicular",
    ],
    "Under 'Note : EBV associated lymphomas' at the top of page 156: 'T cell type : Extranodal NK T-lymphoma. – Very poor prognosis. – Presents with nasal mass.'",
)

add(
    S4,
    156,
    "recall",
    "Directly below the EBV note on page 156, what surface marker and two histological cell types are listed under 'Anaplastic large cell lymphoma :'?",
    "CD30+ with histology showing Hallmark cells and flower cells",
    [
        "CD20+ with histology showing Popcorn RS cells and lacunar cells",
        "CD5+ with histology showing Smudge cells and cleaved centrocytes",
        "CD103+ with histology showing Hairy cells and fried-egg halo",
    ],
    "On page 156 above Clinical Features: 'Anaplastic large cell lymphoma : • CD30+ • Histology : Hallmark cells, flower cells.'",
)

add(
    S4,
    156,
    "numeric",
    "Under 'Clinical Features' of Hodgkin's Disease on page 156, what lymph node consistency, exact descending regional site order (with percentage), B-symptom percentage, and alcohol sign are printed?",
    "Diffuse painless rubbery firm lymphadenopathy; Posterior cervical region (60–80%) > Supraclavicular > Axillary (seen in lymphocyte-predominant HD); B symptoms (30%–40%); M>F; alcohol-induced ↑ size in node (as printed)",
    [
        "Stony-hard fixed tender lymphadenopathy; Inguinal (80%) > Epitrochlear > Mesenteric; B symptoms (<5%); F>M; alcohol-induced shrinkage of node",
        "Fluctuant suppurative matted lymphadenopathy; Submental (90%) > Preauricular > Popliteal; B symptoms (100%); alcohol causes acute hypoglycemia",
        "Isolated splenomegaly without peripheral lymphadenopathy; Bone marrow only; B symptoms absent; alcohol causes intravascular hemolysis",
    ],
    "Under 'Clinical Features' on page 156: '• Diffuse painless rubbery firm lymphadenopathy. • Site : Posterior cervical region (60–80%) > Supraclavicular > Axillary (Seen in lymphocyte-predominant HD). • B symptoms (30%–40%). • M>F. • Alcohol induced ↑ size in node.'",
)

add(
    S4,
    156,
    "oddoneout",
    "All of the following four conditions are listed under 'Paraneoplastic manifestations :' of Hodgkin's Disease on page 156 EXCEPT:",
    "Membranoproliferative glomerulonephritis with cryoglobulinemia",
    [
        "Subacute cerebellar degeneration",
        "Minimal change disease",
        "Cholangitis and Vanishing bile duct syndrome",
    ],
    "Under 'Paraneoplastic manifestations :' on page 156: '– Subacute cerebellar degeneration. – Minimal change disease. – Cholangitis. – Vanishing bile duct syndrome.' Followed by '• Unexplained pruritis. • Pel-Ebstein fever : Diagnostic.'",
)

add(
    S4,
    156,
    "recall",
    "Which four clinical features and characteristic histological cell define 'Nodular sclerosis' Hodgkin's Disease on page 156?",
    "Mediastinal node, young females, SVC obstruction, pleural effusion, and Lacunar cells on histology",
    [
        "Axillary single node in elderly men, absence of mediastinal involvement, and Popcorn RS cells on histology",
        "Retroperitoneal nodes in HIV-positive children, extensive B symptoms, and Starry-sky macrophages on histology",
        "Gastric mucosal mass in autoimmune gastritis, upper GI bleeding, and Small cleaved centrocytes on histology",
    ],
    "Near the bottom of page 156 alongside the 'Nodular sclerosis → Lacunar cells' photomicrograph: '• Nodular sclerosis : – Mediastinal node. – Young females. – SVC obstruction. – Pleural effusion.'",
)

add(
    S4,
    156,
    "recall",
    "Which five features describe 'Mixed cellularity' Hodgkin's Disease at the bottom of page 156, and which two of those features carry the brace note 'Seen in LD also'?",
    "Common in HIV +ve and 70% EBV +ve [brace: 'Seen in LD also'], plus extensive B symptoms, elderly & children, and classical RS cells + mononuclear cells",
    [
        "Exclusively young females and 0% EBV +ve, absence of B symptoms, adolescent peak only, and popcorn L&H cells",
        "Exclusively H. pylori +ve and HTLV-1 +ve, localized stage IA axillary disease, and hallmark flower cells",
        "Isolated mediastinal mass in young athletes, normal ESR, no B symptoms, and absence of mononuclear cells",
    ],
    "At the bottom of page 156: '• Mixed cellularity : [– Common in HIV +ve – 70% EBV +ve] → Seen in LD also. – Extensive B symptoms. – Elderly, children. – Classical RS cells and mononuclear cells.'",
)


# ==============================================================================
# UNIT 5 — Page 157: Staging Biopsy & FDG-PET, Unfavourable Criteria & β2-Microglobulin
# ==============================================================================

add(
    S5,
    157,
    "recall",
    "At the top of page 157 before the Staging section, which two low-grade B-cell lymphomas are explicitly grouped by brace as examples ('Eg') undergoing Richter transformation into DLBCL?",
    "SLL (Small lymphocytic lymphoma) and Follicular lymphoma → transform into High-grade lymphoma (DLBCL)",
    [
        "Nodular lymphocyte-predominant HD and Burkitt's lymphoma → transform into Multiple myeloma",
        "Anaplastic large cell lymphoma and Mycosis fungoides → transform into Hairy cell leukemia",
        "Primary CNS lymphoma and Primary effusion lymphoma → transform into Mantle cell lymphoma",
    ],
    "At the top of page 157 under '• Richter transformation :': 'Low grade lymphoma —[transforms]→ High grade lymphoma; [Eg : SLL, Follicular lymphoma] → DLBCL.'",
)

add(
    S5,
    157,
    "recall",
    "Under 'Staging' on page 157, what biopsy procedure is printed as 'Investigation of choice for staging', and what imaging modality is printed as the 'Single most valuable test for staging' (using FDG)?",
    "Full thickness excision biopsy (printed under Investigation of choice for staging); PET scan using FDG (Fluoro deoxyglucose) is the single most valuable test for staging",
    [
        "Fine-needle aspiration cytology (FNAC) alone; Technetium-99m MDP skeletal scintigraphy is the single most valuable test for staging",
        "Blind percutaneous splenic aspiration; Somatostatin-receptor DOTATATE scan is the single most valuable test for staging",
        "Peripheral blood buffy-coat smear; Non-contrast chest radiograph alone is the single most valuable test for staging",
    ],
    "Under 'Staging' on page 157: 'Investigation of choice for staging : Full thickness excision biopsy.' And under 'PET scan': '• Single most valuable test for staging. • Uses FDG (Fluoro deoxyglucose).'",
)

add(
    S5,
    157,
    "recall",
    "In the staging body-diagram on page 157, how are Stage I through Stage IV and the A/B suffixes defined?",
    "Stage I: single lymph node region or single organ; Stage II: ≥2 node regions same side of diaphragm; Stage III: ≥2 node regions above & below diaphragm; Stage IV: widespread disease in multiple organs ± LN involvement; A = No B symptoms, B = B symptoms +ve",
    [
        "Stage I: lymphocytosis only; Stage II: hepatosplenomegaly; Stage III: anemia; Stage IV: pancytopenia; A = asymptomatic, B = bulky >2 cm",
        "Stage I: bilateral hilar nodes; Stage II: lung parenchyma; Stage III: bone marrow only; Stage IV: CNS blasts; A = anterior, B = bilateral",
        "Stage I–III: restricted to cervical nodes only; Stage IV: any axillary node; A = EBV negative, B = EBV positive",
    ],
    "The four human-figure captions under Staging on page 157 define Stage I–IV along with 'A : No B symptoms' and 'B : B symptoms +ve' to the right of the diaphragm line.",
)

add(
    S5,
    157,
    "numeric",
    "In the 'Early disease → Unfavorable' risk-stratification branch on page 157, which FIVE exact criteria classify Stage I/II Hodgkin's Disease as Unfavorable?",
    "Age > 60, B symptoms +ve, Bulky nodes (>10 cm), ≥4 extranodal sites (as printed), and ESR ≥50 mm/hr",
    [
        "Age > 40, Absence of B symptoms, Node size >2 cm, ≥1 splenic nodule, and ESR ≥15 mm/hr",
        "Age < 15, Pruritus without fever, Axillary node involvement, Normal ESR, and Platelet count >4.5 lakhs",
        "Male sex alone, Alcohol pain, Posterior cervical site, Hemoglobin <14 g/dL, and ESR <10 mm/hr",
    ],
    "Under 'Early disease → Unfavorable' on page 157: '• Age > 60 • B symptoms +ve • Bulky nodes (>10cm) • ≥4 extranodal sites [as printed] • ESR ≥50 mm/hr.'",
)

add(
    S5,
    157,
    "recall",
    "At the bottom of page 157 under 'Note :', which four laboratory abnormalities are listed under 'Other paraneoplastic manifestations :', and in which three hematologic malignancies does Beta-2 microglobulin indicate poor prognosis?",
    "Other paraneoplastic manifestations: ↑↑ LDH, Hypercalcemia, Hypoglycemia, and Hyponatremia; Beta-2 microglobulin indicates poor prognosis in CLL, HD (Hodgkin's disease), and MM (Multiple myeloma)",
    [
        "Other paraneoplastic manifestations: ↓ LDH, Hypocalcemia, Hyperglycemia, and Hypernatremia; Beta-2 microglobulin indicates good prognosis in ALL, AML, and CML",
        "Other paraneoplastic manifestations: Polycythemia, Thrombocytosis, Hyperuricemia, and Hypokalemia; Beta-2 microglobulin is specific only for Hairy cell leukemia",
        "Other paraneoplastic manifestations: Isolated hyperbilirubinemia only; Beta-2 microglobulin indicates poor prognosis only in Iron deficiency anemia",
    ],
    "At the bottom of page 157 under 'Note :': 'Other paraneoplastic manifestations : • ↑↑ LDH. • Hypercalcemia. • Hypoglycemia. • Hyponatremia. Beta-2 microglobulin : Indicates poor prognosis assay in : CLL, HD, MM.'",
)


# ==============================================================================
# UNIT 6 — Page 158: Chemotherapy Response, ABVD Table, Deauville Protocol, Brentuximab & RT
# ==============================================================================

add(
    S6,
    158,
    "recall",
    "At the top of page 158 under 'Treatment → Response to chemotherapy :', how do the four classical Hodgkin's Disease subtypes compare in chemotherapy response?",
    "MC (Mixed cellularity) & LD (Lymphocyte depleted): Poor response; NS (Nodular sclerosis): Very good; LR (Lymphocyte rich): Excellent",
    [
        "MC & LD: Excellent response; NS: Poor response; LR: Refractory to all chemotherapy",
        "LD: Excellent response; MC: Very good response; NS & LR: Poor response",
        "All four subtypes (MC, LD, NS, LR) show an identical poor (<20%) response to ABVD",
    ],
    "At the top of page 158 under 'Response to chemotherapy :': '[• MC • LD] → Poor response. • NS : Very good. • LR : Excellent.'",
)

add(
    S6,
    158,
    "match",
    "In the 'Regime : ABVD' table on page 158, match each component drug with its listed characteristic 'Side Effect' — 1) Adriamycin (Doxorubicin) 2) Bleomycin 3) Vinblastine 4) Dacarbazine … A) Lung fibrosis B) '–' (none listed in table) C) Cardiotoxicity D) Peripheral neuropathy",
    "1-C, 2-A, 3-D, 4-B",
    [
        "1-A, 2-C, 3-D, 4-B",
        "1-C, 2-D, 3-A, 4-B",
        "1-B, 2-A, 3-C, 4-D",
    ],
    "The 'Regime : ABVD' table on page 158 lists: Adriamycin (Doxorubicin) → Cardiotoxicity; Bleomycin → Lung fibrosis; Vinblastine → Peripheral neuropathy; Dacarbazine → '–'.",
)

add(
    S6,
    158,
    "numeric",
    "In the Classical HD treatment flowchart on page 158 ('2 cycles of ABVD → Interim PET scan → Determine score in Deauville 5 point scale'), what Deauville score defines PET-negative response and how many MORE cycles of chemotherapy follow in each of the three stage arms?",
    "Deauville score 1–2: Early favourable → 2 more cycles; Early unfavourable → 3 more cycles (as printed); Advanced disease → 4 more cycles",
    [
        "Deauville score 4–5: Early favourable → 0 more cycles; Early unfavourable → 1 more cycle; Advanced disease → 2 more cycles",
        "Deauville score 1–2: Early favourable → 6 more cycles; Early unfavourable → 8 more cycles; Advanced disease → 10 more cycles",
        "Deauville score 3–5: all three stage groups receive exactly 1 more cycle of ABVD without transplant",
    ],
    "In the Classical HD flowchart on page 158 after '2 cycles of ABVD → Interim PET scan → Determine score in \"Deauville 5 point scale\"': Left arm ('Early favourable, PET –ve Deauville score : 1–2') → '2 more cycles of chemotherapy'; Middle arm ('Early unfavourable with Deauville score : 1–2 after 2 cycles') → '3 more cycles of chemotherapy' [as printed on p158]; Right arm ('Advanced disease') → '4 more cycles of chemotherapy'.",
)

add(
    S6,
    158,
    "management",
    "On page 158, what is the treatment ('Rx') for patients with EITHER '2. Interim PET with Deauville score : 3, 4, 5' OR '3. Relapsed refractory (R/r) HD'?",
    "Salvage chemotherapy + Autologous stem cell transplant",
    [
        "Continue 2 additional cycles of low-dose ABVD alone without stem cell transplantation",
        "Involved-field radiotherapy monotherapy without systemic chemotherapy",
        "Oral maintenance methotrexate + 6-mercaptopurine for 2–3 years",
    ],
    "Items 2 and 3 on page 158 are joined by a brace: '[2. Interim PET with Deauville score : 3,4,5 + 3. Relapsed refractory (R/r) HD] → Rx : Salvage chemotherapy + Autologous stem cell transplant.'",
)

add(
    S6,
    158,
    "recall",
    "At the bottom of page 158, what are the target and indications of Brentuximab, the indication for BEACOPP, and the two rules for Involved site/field radiotherapy?",
    "Brentuximab: Anti-CD30 for Refractory HD and Advanced HD; BEACOPP regime: for advanced disease; Involved site/field radiotherapy: not used except in LPHD, and can be given with ABVD",
    [
        "Brentuximab: Anti-CD20 for early NLPHD only; BEACOPP regime: for Stage IA asymptomatic disease; Radiotherapy: mandatory first-line monotherapy for all Stage IV HD",
        "Brentuximab: Bispecific anti-CD19/CD3 engager; BEACOPP regime: for AIHA complications only; Radiotherapy: contraindicated in LPHD",
        "Brentuximab: BCL-2 oral inhibitor; BEACOPP regime: pediatric maintenance regimen; Radiotherapy: never combined with ABVD",
    ],
    "At the bottom of page 158: 'Brentuximab : Anti-CD30; Indications : • Refractory HD • Advanced HD.' 'BEACOPP regime : For advanced disease.' 'Involved site/field radiotherapy : • Not used except in LPHD. • Can be given with ABVD.'",
)

add(
    S6,
    158,
    "scenario",
    "A 24-year-old woman presents with a mediastinal mass causing mild dyspnea, painless rubbery left supraclavicular lymphadenopathy, and night sweats. Excisional biopsy shows collagen-banded nodules containing CD15+, CD30+ lacunar cells. After 2 cycles of ABVD, interim FDG-PET scan shows persistent high FDG avidity with a Deauville score of 4. Based on pages 156 and 158, what subtype does she have and what is the next management step?",
    "Nodular sclerosis classical Hodgkin's disease; switch to Salvage chemotherapy + Autologous stem cell transplant (with Anti-CD30 Brentuximab indicated in refractory/advanced HD)",
    [
        "Nodular lymphocyte predominant Hodgkin's disease (CD20+ popcorn cells); treat with involved-node radiation monotherapy alone",
        "Early favourable PET-negative Hodgkin's disease; administer 2 more cycles of ABVD and stop all therapy",
        "Mixed cellularity Hodgkin's disease with Deauville score 1; stop ABVD immediately without further therapy",
    ],
    "Page 156 links mediastinal node + young females + lacunar cells to Nodular sclerosis classical HD (CD15+, CD30+), and page 158 specifies that 'Interim PET with Deauville score : 3,4,5' is managed with 'Salvage chemotherapy + Autologous stem cell transplant', with Anti-CD30 Brentuximab indicated for refractory/advanced HD.",
)

add(
    S6,
    158,
    "truefalse",
    "Which statement regarding Hodgkin's Disease management on page 158 is TRUE?",
    "True — In the ABVD regimen, Adriamycin causes cardiotoxicity, Bleomycin causes lung fibrosis, and Vinblastine causes peripheral neuropathy",
    [
        "True — Interim PET Deauville scores of 3, 4, or 5 indicate complete metabolic remission requiring no further chemotherapy",
        "False — Brentuximab is an anti-CD30 monoclonal antibody agent indicated for refractory Hodgkin's disease and advanced Hodgkin's disease",
        "False — The BEACOPP chemotherapy regimen is used for advanced Hodgkin's disease",
    ],
    "All four lines appear directly on page 158: Adriamycin → Cardiotoxicity, Bleomycin → Lung fibrosis, Vinblastine → Peripheral neuropathy; Deauville 1–2 is PET-negative whereas Deauville 3, 4, 5 requires salvage chemotherapy + autologous stem cell transplant; Brentuximab is anti-CD30 for refractory & advanced HD; BEACOPP is for advanced disease.",
)


GUIDES = {
    S1: (
        "Germinal-Centre Physiology Diagram, B-Cell Tumor Origin Table & NF-κB (NK-κβ) Pathogenesis",
        "GC physiology: Pre-GC → Germinal center [Dark Zone (Centroblasts) + Light Zone (Centrocytes)] → Post-GC → Memory B-cells, and Light Zone downward → Plasmablasts → Plasma cells.\n"
        "Origin table: Centrocytes → Follicular lymphoma; Pre-GC → MCL; Centroblasts → DLBCL & Burkitt's; Post-GC → MZL; Plasmablast → ABC-DLBCL; Plasma cells → Multiple myeloma; Memory B cells → SLL, Waldenström's, Hairy cell leukemia.\n"
        "Hodgkin pathogenesis: Upregulation of NF-κB [printed NK-κβ] seen; M > F.",
    ),
    S2: (
        "Dark-Zone Origin & Chr 9 PDL1 Aberration, Stage Cure Rates, HL vs NHL Comparison Table & Pel-Ebstein Fever",
        "Origin & cure rates: Dark-zone GC B-cells undergo somatic hypermutation → cells slated for apoptosis acquire PDL1 gene aberration (chr 9) → ↓ apoptosis → Hodgkin's disease. Cure rates: Early favorable (I/II) >90%, Early unfavorable (I/II) ≥85%, Advanced (III/IV) ~80%.\n"
        "HL vs NHL: HL = good survival, bimodal (m/c 15–34 yrs, 2nd peak >60 yrs), nodal, paraneoplastic cerebellar degeneration, B-symptoms in 30%, contiguous spread ⊕, EBV ⊕⊕⊕; NHL = >60 yrs, extranodal (m/c GIT, Waldeyer's ring), contiguous spread ⊖, EBV ⊕.\n"
        "Pel-Ebstein fever: Low-grade irregular cyclical fever that spikes gradually and alternates with afebrile intervals.",
    ),
    S3: (
        "Reed-Sternberg Cell Morphology, NLPHD vs Classical HD Classification (Worldwide vs India) & Comparison Table",
        "RS cell: Bilobed nucleus, prominent eosinophilic nucleoli separated by clear space from nuclear membrane; specific for HL only if inflammatory background +ve.\n"
        "Classification: Nodular LP-HD = benign entity, excellent prognosis, axillary node, Rx radiation of involved node; Classical HD = LR, LD, Nodular sclerosis (NS — m/c worldwide), Mixed cellularity (MC — m/c in India).\n"
        "Classical vs Nodular table: Classical = CD15+, CD30+, B symptoms ⊕, EBV ⊕ (100/70/40/20: LD 100%, MC 70%, NS 40%, LR 20%), Histology (LD: RS absent [printed], MC: classical RS, NS: lacunar RS, LR: paucity of RS); Nodular = CD20+, CD45+, Surface Ig+, B symptoms absent, EBV ⊖, Popcorn RS / L&H cells.",
    ),
    S4: (
        "EBV/ALCL Recap Notes, Hodgkin Clinical Features, Paraneoplastic Syndromes & NS vs MC Subtype Profiles",
        "Recap notes: EBV-associated NHL includes endemic Burkitt's, post-transplant & primary CNS (DLBCL), and extranodal NK/T-lymphoma (very poor prognosis, nasal mass); ALCL = CD30+, hallmark & flower cells.\n"
        "Clinical features: Diffuse painless rubbery firm lymphadenopathy — Posterior cervical (60–80%) > Supraclavicular > Axillary (NLPHD); B symptoms (30–40%), M>F, alcohol-induced ↑ size in node, unexplained pruritus, diagnostic Pel-Ebstein fever.\n"
        "Paraneoplastic & subtypes: Subacute cerebellar degeneration, minimal change disease, cholangitis, vanishing bile duct syndrome. NS = mediastinal mass, young females, SVC obstruction, pleural effusion, lacunar cells; MC = HIV+, 70% EBV+ (also LD), extensive B symptoms, elderly/children, classical RS + mononuclear cells.",
    ),
    S5: (
        "Richter Recap, Staging Workup (Excision Biopsy & FDG-PET), Unfavourable Criteria & β2-Microglobulin Note",
        "Staging workup: Full thickness excision biopsy (IOC); FDG-PET scan = single most valuable test for staging. Ann-Arbor I–IV with A (no B symptoms) / B (B symptoms +ve).\n"
        "Early (I–II) Unfavorable criteria: Age >60, B symptoms +ve, Bulky nodes (>10 cm), ≥4 extranodal sites [printed], ESR ≥50 mm/hr.\n"
        "Other paraneoplastic & lab markers: ↑↑ LDH, hypercalcemia, hypoglycemia, hyponatremia; Beta-2 microglobulin indicates poor prognosis in CLL, HD, and MM.",
    ),
    S6: (
        "Chemotherapy Response by Subtype, ABVD Toxicity Table, Deauville PET-Adapted Protocol, Brentuximab, BEACOPP & ISRT",
        "Chemo response & ABVD toxicities: MC & LD = poor response, NS = very good, LR = excellent. ABVD: Adriamycin (cardiotoxicity), Bleomycin (lung fibrosis), Vinblastine (peripheral neuropathy), Dacarbazine (–).\n"
        "Deauville 5-point PET protocol (after 2 cycles ABVD): Deauville 1–2 → +2 cycles (early favourable), +3 cycles [printed] (early unfavourable), +4 cycles (advanced disease); Deauville 3,4,5 OR relapsed/refractory HD → Salvage chemo + Autologous stem cell transplant.\n"
        "Targeted & RT notes: Brentuximab (anti-CD30) for refractory & advanced HD; BEACOPP for advanced disease; ISRT/IFRT not used alone except in LPHD, can be combined with ABVD.",
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
