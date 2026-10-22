#!/usr/bin/env python3
"""Generate Chapter 24: World of Lymphomas (Book p140–141).

Every question is anchored to a specific line, box, flowchart arrow, marker list,
or summary row in uploads/02.pdf (PDF pages 23–24 = Book pages 140–141) in strict
book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 24
TITLE = "World of Lymphomas"
PAGES = "140-141"

S1 = "Initial Investigations, Common Lymphoid Progenitor Markers, Precursor B-Cell Maturation & CLL Origin"
S2 = "Lymph Node Zones (Pre-Germinal, Germinal Centre, Post-Germinal/Marginal Zone), Myeloma Markers & CD Summary"

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
# UNIT 1 — Page 140: Investigations, Common Lymphoid Progenitor, B-Cell Stages & CLL Origin
# ==============================================================================

add(
    S1,
    140,
    "recall",
    "Under 'Investigation' at the top of page 140 in World of Lymphomas, what finding is shown on FNAC, trucut/excision biopsy, and which modality is stated as diagnostic?",
    "FNAC, trucut/excision biopsy shows loss of lymph node architecture; immunophenotyping is diagnostic",
    [
        "FNAC alone confirms follicular architecture preservation; serum protein electrophoresis is diagnostic",
        "Peripheral blood smear shows hypersegmented neutrophils; Sudan black cytochemistry is diagnostic",
        "Bone marrow trephine biopsy shows ring sideroblasts on Perls stain; karyotyping alone is diagnostic",
    ],
    "Under 'Investigation :' at the top of page 140: 'FNAC, trucut/excision biopsy : Loss of lymph node architecture. Immunophenotyping : Diagnostic.'",
)

add(
    S1,
    140,
    "recall",
    "In the 'Common lymphoid progenitor' diagram on page 140, which lineage-defining surface CD markers correspond to B cell, T cell, and NK cell respectively?",
    "B cell — CD 19; T cell — CD 3; NK cell — CD 56",
    [
        "B cell — CD 3; T cell — CD 56; NK cell — CD 19",
        "B cell — CD 34; T cell — CD 117; NK cell — CD 13",
        "B cell — CD 56; T cell — CD 19; NK cell — CD 3",
    ],
    "The Common lymphoid progenitor tree on page 140 branches into: B cell → CD 19, T Cell → CD 3, and NK cell → CD 56.",
)

add(
    S1,
    140,
    "recall",
    "In the first box under 'B-Cell Lymphoma' on page 140 ('pro-B cell'), what are the heavy-chain rearrangement status, surface/immature markers, and prognosis?",
    "Incomplete rearrangement of heavy chain; marker CD 19 with immature markers CD 34, HLA-DR, PAX-5; bad prognosis",
    [
        "Complete rearrangement of heavy chain; markers CD 10 (CALLA) and TdT with loss of CD 34 and HLA-DR; good prognosis",
        "Complete rearrangement of heavy and light chains; surface IgM positive with loss of CD 10 and TdT; good prognosis",
        "Somatic hypermutation of light chain in dark zone; markers BCL-6, CD 10, and CD 23; intermediate prognosis",
    ],
    "The left 'pro-B cell :' box on page 140 lists: 'Incomplete rearrangement of heavy chain. marker : CD 19. Immature markers : CD 34, HLA-DR, PAX-5. Bad prognosis.'",
)

add(
    S1,
    140,
    "recall",
    "In the second box under 'B-Cell Lymphoma' on page 140 ('Pre-B cell'), what heavy-chain status, marker profile, marker loss, and prognosis are listed?",
    "Complete rearrangement of heavy chain; expresses CD 10 (CALLA antigen), TdT, CD 20, CD 21, CD 22, CD 79a, CD 79b + CD 19; loses CD 34 and HLA-DR; good prognosis",
    [
        "Incomplete rearrangement of heavy chain; expresses CD 34, HLA-DR, and PAX-5 only; loses CD 19 and CD 20; bad prognosis",
        "Complete rearrangement of heavy and light chains; expresses S.IgM, CD 5, and CD 23; loses PAX-5 and CD 79a; bad prognosis",
        "No immunoglobulin gene rearrangement; expresses CD 38, CD 138, and cytoplasmic light chains; loses all pan-B markers; good prognosis",
    ],
    "The middle 'Pre-B cell :' box on page 140 lists: 'Complete rearrangement of heavy chain. markers : • CD 10 (CALLA antigen), Tdt, CD 20, CD 21, CD 22, CD 79a, CD 79b + CD 19. • Loses CD 34, HLA-DR. Good prognosis.'",
)

add(
    S1,
    140,
    "recall",
    "In the third box under 'B-Cell Lymphoma' on page 140 ('Immature-B cell'), what immunoglobulin gene rearrangement occurs, which markers are gained or lost, and what is the prognosis?",
    "Complete rearrangement of heavy & light chain; expresses S.IgM with CD 19, CD 20, CD 21, CD 22, CD79a, CD 79b; loses CD 10 and TdT; bad prognosis",
    [
        "Incomplete rearrangement of light chain only; expresses CD 34, HLA-DR, CD 10, and TdT without S.IgM; good prognosis",
        "Complete rearrangement of delta heavy chain in lymph node; gains S.IgD, BCL-6, and Cyclin D; loses S.IgM; good prognosis",
        "Absence of heavy & light chain rearrangement; expresses CD 3, CD 56, and MPO; loses CD 19 and CD 20; good prognosis",
    ],
    "The right 'Immature-B cell :' box on page 140 lists: 'Complete rearrangement of heavy & light chain. marker : • S.IgM. • CD 19, CD 20, CD 21, CD 22, CD79a, CD 79b. • Loses CD 10, Tdt. Bad prognosis.'",
)

add(
    S1,
    140,
    "fillup",
    "In the brace spanning pro-B cell, Pre-B cell, and Immature-B cell on page 140, all three stages give rise to Precursor B cell ALL, of which the most common subtype is ______.",
    "Pre-B ALL",
    [
        "Pro-B ALL",
        "Immature-B ALL",
        "Burkitt's ALL",
    ],
    "Below the three precursor B-cell boxes on page 140, the spanning brace reads: 'Precursor B cell ALL. m/c : Pre-B ALL.'",
)

add(
    S1,
    140,
    "match",
    "On page 140, match each B-cell developmental stage with its defining feature — 1) Pro-B cell 2) Pre-B cell 3) Immature-B cell 4) Naive B cell … A) Complete heavy chain rearrangement; gains CD 10 (CALLA) & TdT, loses CD 34 & HLA-DR; good prognosis B) Incomplete heavy chain rearrangement; expresses CD 19 with immature markers CD 34, HLA-DR, PAX-5; bad prognosis C) No antigen encounter; expresses CD 19, CD 20, CD21, CD 22, CD79a, CD 79b, S.IgM before entering lymph node or undergoing apoptosis D) Complete heavy & light chain rearrangement; expresses S.IgM, loses CD 10 & TdT; bad prognosis",
    "1-B, 2-A, 3-D, 4-C",
    [
        "1-A, 2-B, 3-C, 4-D",
        "1-B, 2-D, 3-A, 4-C",
        "1-C, 2-A, 3-D, 4-B",
    ],
    "On page 140: Pro-B = incomplete heavy chain + CD 34/HLA-DR/PAX-5 (bad prognosis); Pre-B = complete heavy chain + CD 10/TdT, loses CD 34/HLA-DR (good prognosis); Immature-B = complete heavy & light chain + S.IgM, loses CD 10/TdT (bad prognosis); Naive B cell = no antigen encounter, expresses CD 19, CD 20, CD21, CD 22, CD79a, CD 79b, S.IgM.",
)

add(
    S1,
    140,
    "recall",
    "According to the bottom diagram on page 140, what cellular defect converts a Naive B Cell (no antigen encounter) into Chronic Lymphocytic Leukemia (CLL), and what full marker profile does CLL express?",
    "Failure of apoptosis leading to clonal proliferation; expresses CD 5, CD 23, CD 19, CD 20, CD 21, CD 22, CD79a, CD 79b, and S.IgM",
    [
        "Somatic hypermutation in the germinal centre dark zone; expresses CD 10, BCL-6, CD 34, and TdT without S.IgM",
        "Complete arrest of myeloid differentiation; expresses CD 13, CD 33, CD 117, MPO, and HLA-DR",
        "Gain of S.IgD with Cyclin D overexpression in the mantle layer; expresses CD 5 and Cyclin D while losing CD 23",
    ],
    "At the bottom of page 140, Naive B Cell (no antigen encounter) shows a blocked arrow to Apoptosis → 'Failure of apoptosis → Clonal proliferation → Chronic lymphocytic leukemia (CLL) : markers : CD 5, CD 23, CD 19, CD 20, CD 21, CD 22, CD79a, CD 79b, S.IgM.'",
)

add(
    S1,
    140,
    "truefalse",
    "Which of the following statements about B-cell maturation and lymphomagenesis on page 140 is TRUE?",
    "True — Pre-B cell acute lymphoblastic leukemia is the most common precursor B-cell ALL subtype, loses CD 34 and HLA-DR, and carries a good prognosis",
    [
        "True — Immature-B cell retains high levels of CD 10 (CALLA antigen) and TdT and carries the best prognosis among precursor B-cell stages",
        "False — Pro-B cell exhibits incomplete heavy-chain rearrangement, expresses CD 34, HLA-DR, and PAX-5, and carries a bad prognosis",
        "False — Chronic lymphocytic leukemia arises from failure of apoptosis and clonal proliferation of naive B cells with acquisition of CD 5 and CD 23",
    ],
    "On page 140, Pre-B cell loses CD 34 and HLA-DR, carries a good prognosis, and is the most common ('m/c : Pre-B ALL') among precursor B-cell ALLs; Pro-B and Immature-B both have bad prognosis, and CLL arises from failure of apoptosis of naive B cells.",
)


# ==============================================================================
# UNIT 2 — Page 141: Zones in Lymph Node, Germinal/Post-Germinal Neoplasms & Summary Table
# ==============================================================================

add(
    S2,
    141,
    "recall",
    "Under 'Zones in lymph node' at the top of page 141, what are the three numbered zones, and what surface immunoglobulin does a Naive B cell gain in the interfollicular area before entering the lymph node?",
    "1. Pre germinal centre, 2. Germinal centre (Activation/maturation zone), 3. Post germinal centre; gains S.IgD in the interfollicular area of LN",
    [
        "1. Paracortical T-zone, 2. Medullary sinus, 3. Subcapsular sinus; gains secretory IgA in Peyer's patches",
        "1. Red pulp, 2. Periarteriolar lymphoid sheath, 3. Marginal sinus; gains IgE in splenic cords of Billroth",
        "1. Pro-B zone, 2. Pre-B zone, 3. Immature-B zone; gains CD 34 and TdT in the interfollicular area of LN",
    ],
    "At the top of page 141 under 'Zones in lymph node': '1. Pre germinal centre. 2. Germinal centre (Activation/maturation zone). 3. Post germinal centre.' Below it: 'Naive B cell → Interfollicular area of LN : Gains S.IgD → Lymph node.'",
)

add(
    S2,
    141,
    "recall",
    "In the 'Pre-germinal centre/mantle cell layer' box on page 141, which lymphoma arises from proliferation here and what marker panel is listed?",
    "Mantle cell lymphoma (MCL); markers: CD 5, cyclin D, CD 19, CD 20, CD 21, CD 22, CD 79a, CD 79b, S.IgM, S.IgD",
    [
        "Follicular lymphoma; markers: CD 10, CD 23, BCL-6, CD 34, and TdT without CD 5 or cyclin D",
        "Hairy cell leukemia; markers: CD 11c, CD 25, CD 103, CD 123, Annexin, and TRAP without S.IgD",
        "Multiple myeloma; markers: CD 38, CD 138, and C19 (CD 19) with complete loss of CD 20 and S.IgM",
    ],
    "The left box on page 141 reads: 'Pre-germinal centre/mantle cell layer : Proliferation → mantle cell lymphoma (MCL). Specific marker : CD 5, cyclin D, CD 19, CD 20, CD 21, CD 22, CD 79a, CD 79b, S.IgM, S.IgD.'",
)

add(
    S2,
    141,
    "recall",
    "In the 'Germinal centre' box on page 141, which markers define germinal-centre B cells, and which two processes convert a Centroblast (dark zone) into a Centrocyte (light zone)?",
    "Markers: CD 10, CD 23, BCL-6 (with CD 19, CD 20, CD 21, CD 22, CD 79a, CD 79b, S.IgM, S.IgD); Somatic hypermutation and Affinity maturation convert Centroblast (dark zone) to Centrocyte (light zone)",
    [
        "Markers: CD 5, Cyclin D, and TdT only; V(D)J heavy-chain recombination converts Centrocyte (dark zone) to Centroblast (light zone)",
        "Markers: CD 38, CD 138, and CD 56 only; Receptor editing and apoptosis inhibition convert Memory B cell to Naive B cell",
        "Markers: CD 11c, CD 25, and CD 103 only; Class-switch deletion of BCL-6 converts Plasma cell to Centroblast (dark zone)",
    ],
    "In the Germinal centre box on page 141: 'markers : CD 10, CD 23, BCL-6, CD 19, CD 20, CD 21, CD 22, CD 79a, CD 79b, S.IgM, S.IgD' and 'Centroblast (dark zone) —[Somatic hypermutation / Affinity maturation]→ Centrocyte (light zone)'.",
)

add(
    S2,
    141,
    "recall",
    "Within the 'Germinal centre' box on page 141, which lymphomas arise specifically from the Centroblast (dark zone) versus the Centrocyte (light zone)?",
    "Centroblast (dark zone) gives rise to Diffuse large B cell lymphoma (DLBCL) and Burkitt's lymphoma; Centrocyte (light zone) gives rise to Follicular lymphoma (and differentiates toward Plasma blast and marginal zone)",
    [
        "Centroblast (dark zone) gives rise exclusively to Follicular lymphoma; Centrocyte (light zone) gives rise to Mantle cell lymphoma and Burkitt's lymphoma",
        "Centroblast (dark zone) gives rise to Hairy cell leukemia and SLL; Centrocyte (light zone) gives rise to Chronic lymphocytic leukemia",
        "Centroblast (dark zone) gives rise to Waldenstrom's macroglobulinemia; Centrocyte (light zone) gives rise exclusively to Multiple myeloma",
    ],
    "Inside the Germinal centre diagram on page 141, the arrow from Centroblast (dark zone) points to '• Diffuse large B cell lymphoma (DLBCL). • Burkitt's lymphoma.', while Centrocyte (light zone) sends arrows to 'Follicular lymphoma', 'Plasma blast', and 'marginal zone'.",
)

add(
    S2,
    141,
    "recall",
    "Following the 'Plasma blast → Plasma cell' pathway on the left side of page 141, what lymphoma arises from proliferation of the Plasma blast, and what marker profile is printed for Multiple myeloma arising from the Plasma cell?",
    "Plasma blast proliferation causes Activated B cell type DLBCL (ABC–DLBCL); Plasma cell gives rise to Multiple myeloma expressing CD 38, CD 138, and C19 [printed for CD 19], while losing all other markers",
    [
        "Plasma blast proliferation causes Burkitt's lymphoma; Plasma cell gives rise to Waldenstrom's macroglobulinemia expressing CD 5, CD 10, and BCL-6",
        "Plasma blast proliferation causes Mantle cell lymphoma; Plasma cell gives rise to Follicular lymphoma expressing CD 20, CD 21, and S.IgD",
        "Plasma blast proliferation causes Pre-B ALL; Plasma cell gives rise to Hairy cell leukemia expressing CD 34, TdT, and PAX-5",
    ],
    "On the middle-left of page 141: 'Plasma blast → Proliferation : Activated B cell type DLBCL (ABC–DLBCL)' and downward 'Plasma blast → Plasma cell → multiple myeloma : markers : CD 38, CD 138, C19 [printed as C19]. Loses all other markers.'",
)

add(
    S2,
    141,
    "fillup",
    "In the Plasma blast differentiation pathway on page 141, proliferation of the plasma blast produces ______ (ABC–DLBCL), whereas maturation to a plasma cell produces multiple myeloma.",
    "Activated B cell type DLBCL",
    [
        "Mantle cell lymphoma",
        "Follicular lymphoma",
        "Precursor T-cell ALL",
    ],
    "On page 141, the leftward arrow from 'Plasma blast' reads: 'Proliferation : Activated B cell type DLBCL (ABC–DLBCL)'.",
)

add(
    S2,
    141,
    "recall",
    "In the 'Post germinal cell zone/marginal zone' box on page 141, what markers are listed for Marginal zone lymphoma, and which three B-cell neoplasms arise from the Memory B cell?",
    "Marginal zone lymphoma expresses CD 19, CD20, CD 21, CD 22, CD 79a, CD 79b, S.IgM, S.IgD; Memory B cell gives rise to Hairy cell leukemia, Small lymphocyte leukemia (SLL), and Waldenstrom's macroglobulinemia",
    [
        "Marginal zone lymphoma expresses CD 5, CD 10, and Cyclin D; Memory B cell gives rise to Burkitt's lymphoma, Follicular lymphoma, and Pre-B ALL",
        "Marginal zone lymphoma expresses CD 38 and CD 138 only; Memory B cell gives rise to Pro-B ALL, Mantle cell lymphoma, and T-cell ALL",
        "Marginal zone lymphoma expresses CD 34 and TdT; Memory B cell gives rise to Chronic myeloid leukemia, Polycythemia vera, and Essential thrombocytosis",
    ],
    "In the bottom-right box 'Post germinal cell zone/marginal zone :' on page 141: 'marginal zone → marginal Zone lymphoma : markers : CD 19, CD20, CD 21, CD 22, CD 79a, CD 79b, S.IgM, S.IgD' and 'marginal zone → memory B cell → • Hairy cell leukemia. • Small lymphocyte leukemia (SLL). • Waldenstrom's macroglobulinemia.'",
)

add(
    S2,
    141,
    "oddoneout",
    "All of the following B-cell neoplasms arise from the 'memory B cell' in the post-germinal cell zone diagram on page 141 EXCEPT:",
    "Mantle cell lymphoma (MCL)",
    [
        "Hairy cell leukemia",
        "Small lymphocyte leukemia (SLL)",
        "Waldenstrom's macroglobulinemia",
    ],
    "On page 141, 'memory B cell' gives rise to Hairy cell leukemia, Small lymphocyte leukemia (SLL), and Waldenstrom's macroglobulinemia, whereas Mantle cell lymphoma (MCL) arises from the Pre-germinal centre / mantle cell layer.",
)

add(
    S2,
    141,
    "match",
    "In the 'Summary :' box at the bottom-left of page 141, match each CD 5 / CD 10 / CD 23 immunophenotype with its corresponding B-cell entity — 1) CD 5+, CD 10–, CD 23+ 2) CD 5+, CD 10–, CD 23– 3) CD 5–, CD 10+, CD 23+ 4) CD 5–, CD 10–, CD 23– … A) MCL (Mantle cell lymphoma) B) MZL (Marginal zone lymphoma) C) CLL (Chronic lymphocytic leukemia) D) GC (Germinal centre)",
    "1-C, 2-A, 3-D, 4-B",
    [
        "1-A, 2-C, 3-D, 4-B",
        "1-C, 2-B, 3-A, 4-D",
        "1-D, 2-A, 3-C, 4-B",
    ],
    "The 'Summary :' box at the bottom-left of page 141 prints: 'CD 5+, CD 10–, CD 23+ → CLL. CD 5+, CD 10–, CD 23– → MCL. CD 5–, CD 10+, CD 23+ → GC. CD 5–, CD 10–, CD 23– → MZL.'",
)

add(
    S2,
    141,
    "scenario",
    "An adult presents with generalized lymphadenopathy, and lymph node excision biopsy reveals effaced architecture due to a mature CD19+, CD20+, S.IgM+, S.IgD+ B-cell neoplasm. Flow cytometry demonstrates CD 5+, CD 10–, CD 23– cells with nuclear Cyclin D positivity. According to page 141, from which lymph node zone does this lymphoma arise?",
    "Pre-germinal centre / mantle cell layer — Mantle cell lymphoma (MCL)",
    [
        "Germinal centre dark zone centroblast — Burkitt's lymphoma",
        "Post-germinal cell zone marginal zone — Marginal zone lymphoma (MZL)",
        "Bone marrow naive B-cell apoptosis failure — Chronic lymphocytic leukemia (CLL)",
    ],
    "On page 141, CD 5+, CD 10–, CD 23– with specific markers CD 5 and Cyclin D (plus CD 19, CD 20, CD 21, CD 22, CD 79a, CD 79b, S.IgM, S.IgD) defines Mantle cell lymphoma (MCL), arising from proliferation of the Pre-germinal centre/mantle cell layer.",
)

add(
    S2,
    141,
    "management",
    "When evaluating an enlarged cervical lymph node suspected of B-cell lymphoma using the diagnostic principles on pages 140–141, how does immunophenotyping distinguish Chronic Lymphocytic Leukemia (CLL) from Marginal Zone Lymphoma (MZL) when both express pan-B markers (CD 19, CD 20, CD 21, CD 22, CD 79a, CD 79b, S.IgM) and lack CD 10?",
    "CLL co-expresses both CD 5+ and CD 23+ (CD 5+, CD 10–, CD 23+), whereas MZL is negative for both markers (CD 5–, CD 10–, CD 23–)",
    [
        "CLL is negative for both CD 5 and CD 23, whereas MZL strongly co-expresses CD 5+, CD 10+, and BCL-6+",
        "CLL loses all pan-B markers and expresses only CD 38 and CD 138, whereas MZL expresses CD 34 and TdT",
        "CLL expresses CD 5+ with Cyclin D and lacks CD 23, whereas MZL expresses CD 56 and CD 3",
    ],
    "From page 140 (Immunophenotyping : Diagnostic) and the Summary box on page 141: CLL is 'CD 5+, CD 10–, CD 23+' while MZL is 'CD 5–, CD 10–, CD 23–'.",
)

add(
    S2,
    141,
    "numeric",
    "How many distinct lymph node zones are enumerated under 'Zones in lymph node' on page 141, and how many diagnostic CD marker combinations are contrasted in the bottom-left 'Summary :' box?",
    "3 lymph node zones (Pre germinal centre, Germinal centre, Post germinal centre) and 4 immunophenotypic patterns (CLL, MCL, GC, MZL)",
    [
        "2 lymph node zones (Cortical zone, Medullary zone) and 2 immunophenotypic patterns (Hodgkin, Non-Hodgkin)",
        "4 lymph node zones (Pro-B, Pre-B, Immature-B, Naive-B) and 6 immunophenotypic patterns",
        "5 lymph node zones and 3 immunophenotypic patterns (T-ALL, B-ALL, NK-lymphoma)",
    ],
    "Page 141 lists 3 numbered lymph node zones at the top (1. Pre germinal centre, 2. Germinal centre, 3. Post germinal centre) and 4 rows in the bottom-left Summary box (CLL, MCL, GC, MZL).",
)


GUIDES = {
    S1: (
        "Initial Investigations, Common Lymphoid Progenitor Markers, Precursor B-Cell Maturation & CLL Origin",
        "Investigations: FNAC, trucut/excision biopsy shows loss of lymph node architecture; immunophenotyping is diagnostic. Common lymphoid progenitor → B cell (CD 19), T cell (CD 3), NK cell (CD 56).\n"
        "Precursor B-cell stages (Precursor B-cell ALL; m/c = Pre-B ALL): Pro-B = incomplete heavy chain, CD 19 + CD 34/HLA-DR/PAX-5 (bad prognosis); Pre-B = complete heavy chain, CD 10 (CALLA), TdT, CD 20/21/22/79a/79b + CD 19, loses CD 34/HLA-DR (good prognosis); Immature-B = complete heavy & light chain, S.IgM, loses CD 10/TdT (bad prognosis).\n"
        "Naive B cell (no antigen encounter; CD 19/20/21/22/79a/79b, S.IgM): failure of apoptosis → clonal proliferation → CLL (acquires CD 5, CD 23).",
    ),
    S2: (
        "Lymph Node Zones (Pre-Germinal, Germinal Centre, Post-Germinal/Marginal Zone), Myeloma Markers & CD Summary",
        "LN zones: 1. Pre-germinal centre/mantle layer (after Naive B cell gains S.IgD in interfollicular area) → Mantle cell lymphoma (CD 5, Cyclin D); 2. Germinal centre (CD 10, CD 23, BCL-6): Centroblast (dark zone) → DLBCL, Burkitt's; somatic hypermutation & affinity maturation → Centrocyte (light zone) → Follicular lymphoma, Plasma blast, or Marginal zone.\n"
        "Plasma blast proliferation → ABC-DLBCL; Plasma cell → Multiple myeloma (CD 38, CD 138, C19 [printed]; loses all other markers). Post-germinal/marginal zone → Marginal zone lymphoma; Memory B cell → Hairy cell leukemia, SLL, Waldenstrom's macroglobulinemia.\n"
        "Summary panel: CD5+ CD10– CD23+ = CLL; CD5+ CD10– CD23– = MCL; CD5– CD10+ CD23+ = GC; CD5– CD10– CD23– = MZL.",
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
