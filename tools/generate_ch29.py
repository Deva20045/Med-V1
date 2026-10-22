#!/usr/bin/env python3
"""Generate Chapter 29: Platelets - Basics (Book p169–172).

Every question is anchored to a specific line, flowchart arrow, receptor list,
stage label, table cell or photomicrograph caption in uploads/02.pdf
(PDF pages 52–55 = Book pages 169–172) in strict book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 29
TITLE = "Platelets - Basics"
PAGES = "169-172"

S1 = "Myeloid Progenitor Lineages, Thrombopoiesis (Early vs Late), Megakaryocyte Stages & Morphological Variants"
S2 = "Platelet Counts, Lifespan, Sample Handling, Pseudothrombocytopenia & Platelet Transfusion (SDP vs RDP)"
S3 = "Platelet Cascade I: Endothelial Antiplatelet/Anticoagulant/Fibrinolytic Roles, vWF Adhesion Receptors & Granules"
S4 = "Clotting Cascade (Intrinsic, Extrinsic, Common), Fibrinolysis Checkpoints, Antifibrinolytics & aPTT/PT Tests"

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
        assert " — 1)" in stem and " … A)" in stem, f"match stem must use grammar: {stem}"
    clean_exp = explanation.rstrip()
    final_exp = clean_exp if clean_exp.endswith(f"(Book p{page})") else f"{clean_exp} (Book p{page})"
    RAW.append((sec, page, fmt, stem, options, options.index(correct), final_exp))


# ==============================================================================
# UNIT 1 — Page 169
# ==============================================================================

add(
    S1, 169, "recall",
    "In the 'Common myeloid progenitor' branching diagram at the top of page 169, which four cell lines are shown arising from the common myeloid progenitor, and which of them is drawn as the direct parent of the platelet?",
    "RBC, Granulocyte, Monocyte and Megakaryocyte; the Megakaryocyte is drawn as the parent of the Platelet",
    [
        "RBC, Granulocyte, Monocyte and Lymphocyte; the Monocyte is drawn as the parent of the Platelet",
        "RBC, Eosinophil, Basophil and Megakaryocyte; the Basophil is drawn as the parent of the Platelet",
        "RBC, Granulocyte, Natural killer cell and Megakaryocyte; the NK cell is drawn as the parent of the Platelet",
    ],
    "The top diagram reads 'common myeloid progenitor' with four arrows: '→ RBC', '→ Granulocyte', '→ monocyte', and '→ megakaryocyte → Platelet', so the megakaryocyte arrow continues directly into 'Platelet'. (Book p169)",
)

add(
    S1, 169, "recall",
    "Under 'Thrombopoiesis' on page 169, the diagram splits into an 'Early' and a 'Late' limb. Which requirement is printed against the 'Late' limb?",
    "Requires SDF-1",
    [
        "Requires IL-3",
        "Requires colony-stimulating factor (CSF)",
        "Requires erythropoietin",
    ],
    "Under the 'Thrombopoiesis' bracket, 'Early' leads to 'Requires :' (thrombopoietin, IL-3, IL-11) whereas the 'Late' arrow points to the single line 'Requires SDF-1'. (Book p169)",
)

add(
    S1, 169, "recall",
    "Page 169 prints a boxed arrow from 'Thrombopoietin' onto the myeloid stem cell. What is given inside that box as the source of thrombopoietin?",
    "From kidneys and liver",
    [
        "From liver only",
        "From megakaryocytes and spleen",
        "From bone marrow stroma and lung",
    ],
    "The boxed arrow reads 'Thrombopoietin / From kidneys and liver', and points into 'Myeloid stem cell' before Megakaryoblast. Note that the 'Early' limb of the same page prints 'Thrombopoietin : From liver.', so the two statements are both in the book and are tested separately. (Book p169)",
)

add(
    S1, 169, "recall",
    "On page 169 the 'Early' branch of thrombopoiesis lists three requirements. Which three are printed?",
    "Thrombopoietin (from liver), IL-3 (platelet development) and IL-11",
    [
        "Thrombopoietin (from kidney), IL-2 and IL-6",
        "SDF-1, IL-3 and thrombopoietin (from endothelium)",
        "Thrombopoietin (from liver), IL-1 and GM-CSF",
    ],
    "Under the 'Early' limb of 'Thrombopoiesis :': 'Requires : • Thrombopoietin : From liver. • IL-3 : Platelet development. • IL-11 :'. (Book p169)",
)

add(
    S1, 169, "fillup",
    "Under 'IL-11' on page 169, the recombinant form is named ______, and it is used for the 'Rx of Induced thrombocytopenia in chemotherapy.'",
    "Oprelvekin",
    [
        "Romipiostim",
        "Eltrombopag",
        "Anagrelide",
    ],
    "Page 169 prints under IL-11: '– Recombinant IL-11 (Oprelvekin). – Rx of Induced thrombocytopenia in chemotherapy.' (Book p169)",
)

add(
    S1, 169, "recall",
    "Page 169 labels four morphological stages of the megakaryocyte in the left-hand lineage. Which stage descriptions are printed for Stage III and Stage IV respectively?",
    "Stage III: maximal granules, multilobed nuclei; Stage IV: mature, lesser granules, pyknotic nuclei",
    [
        "Stage III: basophilic cytoplasm; Stage IV: maximal granules with multilobed nuclei",
        "Stage III: mature with pyknotic nuclei; Stage IV: maximal granules with multilobed nuclei",
        "Stage III: lesser granules with multilobed nuclei; Stage IV: basophilic with maximal granules",
    ],
    "Beside the megakaryocyte the book prints: 'Stage II : Basophilic. Stage III : maximal granules, multilobed nuclei. Stage IV : mature, lesser granules, pyknotic nuclei.' (Book p169)",
)

add(
    S1, 169, "recall",
    "On page 169, what exactly does the book define 'Endomitosis' to be?",
    "Process of multiplication of megakaryocytes",
    [
        "Process by which megakaryocytes shed platelet precursor extensions into sinusoids",
        "Process of nuclear extrusion producing an anucleate platelet",
        "Process of granule release from megakaryocyte alpha granules",
    ],
    "The bottom right of the lineage box prints: '→ Endomitosis : Process of multiplication of megakaryocytes.' The shedding of 'Platelet precursor extensions' is a separate, separately labelled arrow on the same page. (Book p169)",
)

add(
    S1, 169, "match",
    "At the bottom of page 169, match each labelled megakaryocyte morphology with the condition printed beneath it — 1) Giant megakaryocyte 2) Dwarf megakaryocyte 3) Cloud megakaryocyte 4) Staghorn megakaryocyte … A) Chronic myeloid leukemia B) Immune thrombocytopenic purpura C) Essential thrombocytosis D) Primary myelofibrosis",
    "1-B, 2-A, 3-D, 4-C",
    [
        "1-A, 2-B, 3-C, 4-D",
        "1-B, 2-A, 3-C, 4-D",
        "1-D, 2-C, 3-A, 4-B",
    ],
    "The four captions of the 'MORPHOLOGICAL VARIATION OF MEGAKARYOCYTES' panel read in order: 'Giant megakaryocyte : Immune thrombocytopenic purpura', 'Dwarf megakaryocyte : Chronic myeloid leukemia', 'Cloud megakaryocyte : Primary myelofibrosis', 'Staghorn megakaryocyte : Essential thrombocytosis'. (Book p169)",
)

# ==============================================================================
# UNIT 2 — Page 170
# ==============================================================================

add(
    S2, 170, "numeric",
    "Under 'BASICS OF PLATELETS' on page 170, what lifespan is printed for a platelet, and what lifespan is printed for platelets in stored blood?",
    "Lifespan 10 days; life span in stored blood 72 hrs",
    [
        "Lifespan 7 days; life span in stored blood 48 hrs",
        "Lifespan 120 days; life span in stored blood 72 hrs",
        "Lifespan 10 days; life span in stored blood 24 hrs",
    ],
    "Page 170 opens: 'Lifespan : 10 days.' and later, after the bleeding thresholds, 'Life span in stored blood : 72 hrs.' (Book p170)",
)

add(
    S2, 170, "numeric",
    "Page 170 gives a normal platelet count and three count-defined thresholds. Which set is printed exactly?",
    "Normal 1.5 – 4 lakh/µL; thrombocytopenia < 1,00,000/µL; bleeding < 20,000/µL; significant bleeding < 10,000/µL",
    [
        "Normal 1.5 – 4 lakh/µL; thrombocytopenia < 1,50,000/µL; bleeding < 50,000/µL; significant bleeding < 20,000/µL",
        "Normal 1 – 3 lakh/µL; thrombocytopenia < 1,00,000/µL; bleeding < 30,000/µL; significant bleeding < 10,000/µL",
        "Normal 1.5 – 4 lakh/µL; thrombocytopenia < 1,00,000/µL; bleeding < 40,000/µL; significant bleeding < 5,000/µL",
    ],
    "Page 170 prints: 'Normal count : 1.5 – 4 lakh/µL. Thrombocytopenia : < 1,00,000/µL. • Bleeding : < 20,000/µL. • Significant bleeding : < 10,000/µL.' (Book p170)",
)

add(
    S2, 170, "recall",
    "Under 'Investigations :' on page 170, which sample is used for coagulation studies and which for platelet studies?",
    "Coagulation studies: platelet poor plasma; platelet studies: platelet rich plasma",
    [
        "Coagulation studies: platelet rich plasma; platelet studies: platelet poor plasma",
        "Coagulation studies: whole blood; platelet studies: serum",
        "Coagulation studies: platelet poor plasma; platelet studies: serum",
    ],
    "Page 170 prints: 'Coagulation studies : Platelet poor plasma. Platelet studies : Platelet rich plasma.' (Book p170)",
)

add(
    S2, 170, "recall",
    "Page 170 states the temperature at which these investigations are conducted, together with a single printed exception. What is that exception?",
    "Room temperature, except lupus anticoagulant at 4°C",
    [
        "37°C, except lupus anticoagulant at 4°C",
        "Room temperature, except pseudothrombocytopenia at 37°C",
        "4°C, except platelet aggregation studies at room temperature",
    ],
    "Beneath the two plasma lines the book prints: 'Conducted at room temperature (Exception : Lupus anticoagulant at 4°C).' (Book p170)",
)

add(
    S2, 170, "scenario",
    "A 30-year-old asymptomatic man has a CBC platelet count of 40,000/µL, but the reported count does not fit his well-being. The lab reports platelet clumping on the smear; the report links the clumping to EDTA and advises a particular anticoagulant for a repeat sample. Which explanation and corrective anticoagulant does page 170 print?",
    "Pseudothrombocytopenia (satellitism) caused by EDTA; repeat in 3.2% trisodium citrate",
    [
        "True immune thrombocytopenia caused by EDTA; repeat in heparin",
        "Pseudothrombocytopenia caused by heparin; repeat in 3.2% trisodium citrate",
        "Platelet satellitism caused by citrate; repeat in EDTA",
    ],
    "The photomicrograph captioned 'Pseudothrombocytopenia' is annotated: 'AKA satellitism : Caused by EDTA → Clumping of platelet. Rx : 3.2% trisodium citrate.' — i.e. the 'treatment' is re-sampling into citrate so the artefact disappears. (Book p170)",
)

add(
    S2, 170, "numeric",
    "Under 'Platelet transfusion :' on page 170, within what time must a platelet transfusion be completed?",
    "Within 20 mins",
    [
        "Within 4 hours",
        "Within 30 mins",
        "Within 6 hours",
    ],
    "Page 170 prints: 'Platelet transfusion : Completed within 20 mins.' followed by 'Types :' and the SDP/RDP table. (Book p170)",
)

add(
    S2, 170, "match",
    "Match the three rows of the SDP vs RDP table on page 170 with the values printed for Single donor platelet (SDP) — 1) Process 2) Cost 3) Others … A) Apheresis B) Costly C) No entry (dash) so that RDP is the 'Commonly used' product",
    "1-A, 2-B, 3-C",
    [
        "1-A, 2-C, 3-B",
        "1-B, 2-A, 3-C",
        "1-C, 2-A, 3-B",
    ],
    "The table columns are 'Single donor platelet (SDP)' and 'Random donor platelet (RDP)'. Against SDP: Process = 'Apheresis', Cost = 'Costly', Others = '–'; against RDP: Process = 'Pooling & centrifugation', Cost = 'Cheap', Others = 'Commonly used'. (Book p170)",
)

add(
    S2, 170, "numeric",
    "On page 170, what post-transfusion platelet increment is bracketed for '1 unit of SDP' and for '4–6 units of RDP', and what increment is printed for '1 unit of RDP' alone?",
    "1 unit SDP and 4–6 units RDP: ↑ by 30,000 – 50,000/µL; 1 unit RDP: ↑ by 6,000/µL",
    [
        "1 unit SDP and 4–6 units RDP: ↑ by 6,000/µL; 1 unit RDP: ↑ by 30,000 – 50,000/µL",
        "1 unit SDP and 4–6 units RDP: ↑ by 10,000 – 20,000/µL; 1 unit RDP: ↑ by 3,000/µL",
        "1 unit SDP and 4–6 units RDP: ↑ by 50,000 – 1,00,000/µL; 1 unit RDP: ↑ by 10,000/µL",
    ],
    "Page 170 prints: 'Post-transfusion increase in platelet count : • 1 unit of SDP ⎫ • 4–6 units of RDP ⎬ ↑ by 30,000 – 50,000/µL' and separately '• 1 unit of RDP : ↑ by 6,000/µL.' (Book p170)",
)

add(
    S2, 170, "management",
    "A thrombocytopenic patient needs a platelet transfusion and the team must choose between single donor and random donor product. According to the page 170 table and increment data, which plan matches the book's own numbers?",
    "Use 1 unit of SDP (or 4–6 units of RDP) for a rise of 30,000–50,000/µL, remembering that 1 unit of RDP alone raises the count by only 6,000/µL and that SDP is apheresis-derived, costly, while RDP is pooled, cheap and commonly used",
    [
        "Use 1 unit of RDP for a rise of 30,000–50,000/µL, remembering that 4–6 units of RDP raise the count by only 6,000/µL and that RDP is apheresis-derived and costly",
        "Use 1 unit of SDP for a rise of 6,000/µL, since SDP is the cheap, commonly used, pooled product",
        "Give platelets only if the count is below 1,00,000/µL, completing the transfusion over 2 hours",
    ],
    "Page 170's table gives SDP = apheresis/costly and RDP = pooling & centrifugation/cheap/'Commonly used'; the increment lines bracket '1 unit of SDP' with '4–6 units of RDP' as raising the count '↑ by 30,000 – 50,000/µL', while '1 unit of RDP : ↑ by 6,000/µL', and transfusion is 'Completed within 20 mins'. (Book p170)",
)

# ==============================================================================
# UNIT 3 — Page 171
# ==============================================================================

add(
    S3, 171, "recall",
    "At the start of 'Role of endothelium :' on page 171, two statements define why endothelial injury is needed before platelets can stick. Which pair is printed?",
    "'Endothelial injury is mandatory for platelet adhesion' and 'Endothelium is antithrombotic, subendothelium is prothrombotic'",
    [
        "'Endothelial injury is optional for platelet adhesion' and 'Endothelium is prothrombotic, subendothelium is antithrombotic'",
        "'Endothelial injury is mandatory for platelet aggregation' and 'Endothelium and subendothelium are both antithrombotic'",
        "'Endothelial injury is mandatory for platelet adhesion' and 'Endothelium is prothrombotic, subendothelium is antithrombotic'",
    ],
    "Page 171 prints under 'Role of endothelium :': '• Endothelial injury is mandatory for platelet adhesion. • Since endothelium is antithrombotic, subendothelium is prothrombotic.' (Book p171)",
)

add(
    S3, 171, "recall",
    "Under '(a) Antiplatelet :' on page 171, which three endothelial antiplatelet substances are listed?",
    "PGI2, nitric oxide, ADPase",
    [
        "PGI2, nitric oxide, thrombomodulin",
        "ADPase, tissue factor pathway inhibitor, nitric oxide",
        "PGI2, tissue plasminogen activator, ADPase",
    ],
    "Page 171 lists: 'a. Antiplatelet : PGI₂, nitric oxide, ADPase.' Thrombomodulin and TFPI belong to the separate '(b) Anticoagulant :' limb, and tPA to '(c) Fibrinolysis :'. (Book p171)",
)

add(
    S3, 171, "match",
    "Match each of the three endothelial anticoagulant mechanisms printed under '(b) Anticoagulant :' on page 171 with the factors it inactivates — 1) Heparin like molecules 2) Thrombomodulin 3) Tissue factor pathway inhibitor (TFPI) … A) Inactivates II, IX, X, XI, XII B) Inactivates V and VIII C) Inactivates VII and X (Tissue factor : III)",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 171 prints: '• Heparin like molecules → Binds with AT-III → Inactivates II, IX, X, XI, XII. • Thrombomodulin → Binds to thrombin → Activates protein C → Inactivates V & VIII. • Tissue factor pathway inhibitor (TFPI) → Inactivates VII & X (Tissue factor : III).' (Book p171)",
)

add(
    S3, 171, "recall",
    "Which endothelial fibrinolytic mechanism is printed under '(c) Fibrinolysis :' on page 171?",
    "Release of tissue plasminogen activator (tPA)",
    [
        "Release of plasminogen activator inhibitor (PAI)",
        "Release of alpha-2 antiplasmin",
        "Release of thrombin-activatable fibrinolysis inhibitor (TAFI)",
    ],
    "Page 171 prints: 'c. Fibrinolysis : Release of tissue plasminogen activator (tPA).' PAI, α2-antiplasmin and TAFI appear later on page 172 in the t-PA inhibitor list, i.e. as antifibrinolytics. (Book p171)",
)

add(
    S3, 171, "recall",
    "In the 'mechanism :' flowchart for adhesion on page 171, which two receptors are listed under 'Receptors :' and which ligand does each bind?",
    "Gp VI on collagen; Gp Ib-IX on platelet",
    [
        "Gp Ib-IX on collagen; Gp VI on platelet",
        "Gp IIb-IIIa on collagen; Gp Ib-IX on fibrinogen",
        "Gp VI on platelet; Gp IIb-IIIa on vWF",
    ],
    "Page 171 prints 'Receptors : • Gp VI on collagen. • Gp Ib-IX on platelet.' after the 'Endothelial injury → Release of von willebrand factor (vWF)' step. Gp IIb-IIIa appears separately under '3. AGGREGATION'. (Book p171)",
)

add(
    S3, 171, "fillup",
    "In the adhesion mechanism on page 171, vWF has two printed sources — megakaryocyte and endothelium — and the endothelial store is described as a '______ form' held 'In weibel palade granule.'",
    "Coiled",
    [
        "Uncoiled",
        "Globular",
        "Cleaved",
    ],
    "Page 171 prints: 'Source : • megakaryocyte. • Endothelium : – Coiled form. – In weibel palade granule.' The 'uncoiled' state is mentioned on page 181, only after release following endothelial injury. (Book p171)",
)

add(
    S3, 171, "match",
    "Under '2. ACTIVATION / DEGRANULATION' on page 171, the degranulation arrows split into two granule types. Match each granule with what is printed for it — 1) α granules 2) δ granules (dense) 3) Contents specified under the δ granule arrow … A) ADP > ATP, calcium, histamine, serotonin B) No contents are listed in the flow diagram C) Dense granules",
    "1-B, 2-C, 3-A",  # aPTT = intrinsic & common; drawback = poor sensitivity; PT = extrinsic & common
    [
        "1-A, 2-B, 3-C",
        "1-C, 2-A, 3-B",
        "1-B, 2-A, 3-C",
    ],
    "The degranulation flow diagram prints two arrows, 'α granules' and 'δ granules (dense)', with no contents written under α granules; the single content list 'ADP > ATP, calcium, histamine, serotonin' hangs only beneath the δ (dense) granule arrow. (Book p171)",
)

add(
    S3, 171, "recall",
    "Under '3. AGGREGATION' on page 171, only two lines are printed. Which are they?",
    "Gp IIb – IIIa, and 'Fibrinogen : Bind to platelets.'",
    [
        "Gp VI, and 'Collagen : Bind to platelets.'",
        "Gp Ib-IX, and 'vWF : Bind to platelets.'",
        "Gp IIb – IIIa, and 'Thrombin : Bind to platelets.'",
    ],
    "Page 171 ends with: '3. AGGREGATION • Gp IIb – IIIa. • Fibrinogen : Bind to platelets.' (Book p171)",
)

# ==============================================================================
# UNIT 4 — Page 172
# ==============================================================================

add(
    S4, 172, "recall",
    "Page 172 titles the two coagulation arms as cascades occurring where. What parenthetical location is printed for each?",
    "Intrinsic cascade (in vitro); extrinsic cascade (in vivo)",
    [
        "Intrinsic cascade (in vivo); extrinsic cascade (in vitro)",
        "Intrinsic cascade (in vitro); extrinsic cascade (in vitro)",
        "Intrinsic cascade (in vivo); extrinsic cascade (in vivo)",
    ],
    "The two boxes on page 172 are headed 'Intrinsic cascade (in vitro)' and 'Extrinsic cascade (in vivo)'. (Book p172)",
)

add(
    S4, 172, "recall",
    "In the intrinsic box on page 172, activation of factor XII is annotated with a cofactor list. Which three are printed there, and what is the arrow into the box labelled?",
    "High molecular weight kininogen and kallikrein; the arrow into the box is labelled 'Back amplification of thrombin'",
    [
        "High molecular weight kininogen and prekallikrein; the arrow into the box is labelled 'Endothelial injury'",
        "Tissue factor and kallikrein; the arrow into the box is labelled 'Back amplification of thrombin'",
        "High molecular weight kininogen and kallikrein; the arrow into the box is labelled 'Thromboplastin (tissue factor)'",
    ],
    "The intrinsic box prints 'XII —— High molecular weight kininogen, kallikrein → XIIa' and above it 'Back amplification of thrombin'. 'Endothelial injury' opens the extrinsic box only. (Book p172)",
)

add(
    S4, 172, "match",
    "Match each intrinsic-cascade step on page 172 with the cofactors printed beside its arrow — 1) IX → IXa 2) X → Xa (intrinsic side) 3) Prothrombin → Thrombin … A) vIII, Ca²⁺ Phospholipid B) vII, Ca²⁺ C) Calcium phospholipase va",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The intrinsic box prints 'IX → IXa' with 'vIII, Ca²⁺ / Phospholipid', the arrow from the intrinsic IXa into 'Factor X → Factor Xa' is annotated 'vII, Ca²⁺', and the common-cascade arrow 'Prothrombin → Thrombin (factor II)' carries 'Calcium phospholipase va'. (Book p172)",
)

add(
    S4, 172, "recall",
    "In the extrinsic box on page 172, the sequence is 'Endothelial injury → Thromboplastin (tissue factor)'. What is printed with it to identify 'Factor III', and what is needed for Factor VII to become Factor VIIa?",
    "Factor III = thromboplastin; Factor VII → Factor VIIa needs Calcium, phospholipid",
    [
        "Factor III = tissue factor pathway inhibitor; Factor VII → Factor VIIa needs heparin",
        "Factor III = factor V; Factor VII → Factor VIIa needs phospholipid alone, without calcium",
        "Factor III = thromboplastin; Factor VII → Factor VIIa needs high molecular weight kininogen",
    ],
    "The extrinsic box prints 'Thromboplastin (tissue factor) / Factor III' with the arrow 'Calcium, phospholipid' leading to 'Factor VIIa ← Factor VII'. (Book p172)",
)

add(
    S4, 172, "recall",
    "At the end of the common cascade on page 172, which factor is printed as responsible for 'Clot stabilisation', and what does the fibrinolysis line begin and end with?",
    "Clot stabilisation by XIII; fibrinogen → fibrin → 'Fibrin degradation Products (FDP)'",
    [
        "Clot stabilisation by XII; fibrinogen → fibrin → 'D-Dimer'",
        "Clot stabilisation by Xa; fibrinogen → fibrin → 'plasminogen'",
        "Clot stabilisation by XIII; fibrin → fibrinogen → 'FDP'",
    ],
    "The common-cascade box ends 'Fibrinogen → Fibrin → Clot stabilisation by XIII', and the fibrinolysis line runs 'Fibrinogen → Fibrin … → Fibrin degradation Products (FDP)'. (Book p172)",
)

add(
    S4, 172, "recall",
    "On page 172 fibrinolysis is activated by tPA acting on plasminogen. Which three 'Check points :' are printed for preventing uncontrolled activation?",
    "Protein C, S : V, VIII; t-PA; Tissue factor pathway inhibitor (TFPI)",
    [
        "Protein C, S : II, VII; PAI-1; antithrombin III",
        "Protein Z, S : V, VIII; thrombin; heparin cofactor II",
        "Protein C, S : IX, XI; TAFI; α2-antiplasmin",
    ],
    "Page 172 prints: 'Check points : Prevent uncontrolled activation. • Protein C, S : V, VIII. • t-PA. • Tissue factor pathway inhibitor TFPI.' (Book p172)",
)

add(
    S4, 172, "oddoneout",
    "Page 172 lists four items under 't-PA inhibitors :' with the caption 'Antifibrinolytic → Promote thrombosis.' Which of the following is NOT one of those four printed t-PA inhibitors?",
    "Tissue factor pathway inhibitor (TFPI)",
    [
        "α-2 antiplasmin",
        "TAFI",
        "Lipoprotein A",
    ],
    "The 't-PA inhibitors : Antifibrinolytic → Promote thrombosis.' list prints exactly '• α-2 antiplasmin. • TAFI. • Plasminogen activator inhibitor (PAI). • Lipoprotein A.' TFPI is listed separately under the right-hand 'Check points' box. (Book p172)",
)

add(
    S4, 172, "match",
    "Match each of the three statements at the foot of page 172 with its printed partner — 1) aPTT 2) aPTT drawback 3) PT … A) Extrinsic & common cascade B) Intrinsic & common cascade C) Poor Sensitivity",
    "1-B, 2-C, 3-A",  # aPTT = intrinsic & common; drawback = poor sensitivity; PT = extrinsic & common
    [
        "1-A, 2-C, 3-B",
        "1-B, 2-A, 3-C",
        "1-C, 2-B, 3-A",
    ],
    "Under 'TESTS' the bracket splits: 'aPTT • Intrinsic & common cascade. • Poor Sensitivity.' and 'PT • Extrinsic & common cascade.' (Book p172)",
)

add(
    S4, 172, "truefalse",
    "Which statement about the clotting cascade as drawn on page 172 is accurate?",
    "True — Both the intrinsic and extrinsic arms converge on Factor X, and from Factor X the common cascade proceeds through prothrombin to fibrin",
    [
        "True — The extrinsic arm reaches fibrin without passing through Factor X, which is why PT is a poor screening test",
        "False — The intrinsic arm joins the common cascade at thrombin rather than at Factor X",
        "False — aPTT is printed as assessing the extrinsic and common cascade with good sensitivity",
    ],
    "Both boxes on p172 point into the single red-bordered 'Common cascade' box, whose first entry is 'Factor X → Factor Xa'. The other statements contradict the printed arrows and the aPTT/PT bracket. (Book p172)",
)

GUIDES = {
    S1: (
        "Myeloid Progenitor Lineages, Thrombopoiesis (Early vs Late), Megakaryocyte Stages & Morphological Variants",
        "Lineages & thrombopoiesis (p169): common myeloid progenitor → RBC, granulocyte, monocyte, megakaryocyte → platelet; thrombopoietin boxed as 'From kidneys and liver' acting on the myeloid stem cell. Thrombopoiesis → Early requires thrombopoietin ('From liver'), IL-3 (platelet development) and IL-11 (recombinant = Oprelvekin, for chemotherapy-induced thrombocytopenia); Late requires SDF-1.\n"
        "Megakaryocyte maturation: myeloid stem cell → megakaryoblast → megakaryocyte → platelet precursor extensions → platelets; Stage II basophilic, Stage III maximal granules with multilobed nuclei, Stage IV mature with lesser granules and pyknotic nuclei; endomitosis = multiplication of megakaryocytes.\n"
        "Morphological variations (photos): giant megakaryocyte in ITP, dwarf in CML, cloud in primary myelofibrosis, staghorn in essential thrombocytosis.",
    ),
    S2: (
        "Platelet Counts, Lifespan, Sample Handling, Pseudothrombocytopenia & Platelet Transfusion (SDP vs RDP)",
        "Basics (p170): lifespan 10 days, normal 1.5–4 lakh/µL, life span in stored blood 72 hrs; thresholds — thrombocytopenia < 1,00,000/µL, bleeding < 20,000/µL, significant bleeding < 10,000/µL.\n"
        "Investigations: coagulation studies need platelet poor plasma, platelet studies need platelet rich plasma, all at room temperature except lupus anticoagulant at 4°C. Pseudothrombocytopenia = satellitism, caused by EDTA, clumping of platelets, remedied by re-sampling in 3.2% trisodium citrate.\n"
        "Transfusion: complete within 20 mins; SDP = apheresis/costly, RDP = pooling & centrifugation/cheap/commonly used; 1 unit SDP or 4–6 units RDP raise the count by 30,000–50,000/µL, whereas 1 unit RDP alone raises it by 6,000/µL.",
    ),
    S3: (
        "Platelet Cascade I: Endothelial Antiplatelet/Anticoagulant/Fibrinolytic Roles, vWF Adhesion Receptors & Granules",
        "Adhesion (p171): endothelial injury is mandatory; endothelium is antithrombotic, subendothelium prothrombotic. Antiplatelet = PGI₂, nitric oxide, ADPase. Anticoagulant = heparin-like molecules (with AT-III, inactivating II, IX, X, XI, XII), thrombomodulin (thrombin → protein C → inactivates V and VIII), TFPI (inactivates VII and X; tissue factor = III). Fibrinolysis = release of tPA.\n"
        "Adhesion mechanism: endothelial injury → release of vWF; sources megakaryocyte and endothelium (coiled form in Weibel-Palade granule); receptors Gp VI on collagen and Gp Ib-IX on platelet.\n"
        "Activation/degranulation: α granules and δ (dense) granules, the latter carrying ADP > ATP, calcium, histamine, serotonin. Aggregation: Gp IIb-IIIa with fibrinogen binding to platelets.",
    ),
    S4: (
        "Clotting Cascade (Intrinsic, Extrinsic, Common), Fibrinolysis Checkpoints, Antifibrinolytics & aPTT/PT Tests",
        "Clotting cascade (p172): intrinsic (in vitro) with back amplification of thrombin — XII → XIIa (high molecular weight kininogen, kallikrein), XI → XIa, IX → IXa (vIII, Ca²⁺, phospholipid), then X → Xa (vII, Ca²⁺); extrinsic (in vivo) — endothelial injury → thromboplastin/tissue factor (factor III) with calcium and phospholipid → factor VIIa, converging on factor X.\n"
        "Common cascade: X → Xa → prothrombin → thrombin (factor II) with calcium phospholipase va → fibrinogen → fibrin → clot stabilisation by XIII. Fibrinolysis: tPA converts plasminogen to plasmin, generating FDPs; check points are protein C and S (V, VIII), t-PA and TFPI; t-PA inhibitors that promote thrombosis are α-2 antiplasmin, TAFI, PAI and lipoprotein A.\n"
        "Tests: aPTT assesses intrinsic and common cascade with poor sensitivity; PT assesses extrinsic and common cascade.",
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
