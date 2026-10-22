#!/usr/bin/env python3
"""Generate Chapter 30: Approach to Bleeding Disorders (Book p173–184).

Every question is anchored to a specific row of the printed comparison tables,
flowchart arrow, list item, aggregation-curve caption or Note box in
uploads/02.pdf (PDF pages 56–67 = Book pages 173–184) in strict book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 30
TITLE = "Approach to Bleeding Disorders"
PAGES = "173-184"

S1 = "Evaluation Protocol I: Platelet vs Coagulation Bleed Table, Lineage Chart, Count-Based Bleeding Risk & Drug-Induced Thrombocytopenia"
S2 = "Evaluation Protocol II: Anticonvulsant/Gp IIb-IIIa/NSAID/Quinine/Penicillin Table, Hypersplenism, Smear & ITP Summary Flowchart"
S3 = "Immune Thrombocytopenic Purpura I: Causes, Gp IIb/IIIa & Ib/IX Antibody Pathogenesis, Clinical Signs & Investigations"
S4 = "ITP II: Features Inconsistent with ITP, Duration-Based Classification & First-Line Treatment (Steroids, IVIg/Anti-D)"
S5 = "ITP III: Second-Line Therapy, Follow-Up & Qualitative Platelet Disorders (Causes, Defect Types, PFA-100 & Aggregation Test)"
S6 = "Aggregation Curves (Biphasic vs Monophasic), Ristocetin Agglutination Test + aPTT Logic, Bleeding Time & vWF Functions"
S7 = "Optical Density Traces: Aggregation Defect vs BSS/vWD vs Storage Pool (Granule) Defect Interpretation"
S8 = "Glanzmann Thrombasthenia, Afibrinogenemia, Bernard-Soulier Syndrome, Megathrombocytosis & Drug-Induced Qualitative Bleeding"
S9 = "Von Willebrand Disease I: vWF Gene/Structure Domains, ADAMTS13 Processing, Functions & Types"
S10 = "Von Willebrand Disease II: Type 1 vs Type 3 Table, Type 2 Subtypes (2A/2B/2M/2N), Acquired vWF & Management"
S11 = "DIC I: Clinical Approach by aPTT/PT/Platelet Combinations (Factor XII/XI/Hemophilia A & B/vWD/LAC/Liver/Warfarin) & Etiology"
S12 = "DIC II: Pathogenesis Chain, ICU Monitoring, Purpura Fulminans, Investigations (FDP vs D-Dimer) & Management"

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
# UNIT 1 — Page 173
# ==============================================================================

add(
    S1, 173, "recall",
    "The first row of the 'Platelet related vs Coagulation related bleed' table on page 173 compares the onset of bleeding. What is printed for each column?",
    "Platelet: immediately after trauma; Coagulation: late bleeding",
    [
        "Platelet: late bleeding; Coagulation: immediately after trauma",
        "Platelet: immediately after trauma; Coagulation: bleeding only after surgery",
        "Platelet: bleeding at rest; Coagulation: immediate bleeding after trauma",
    ],
    "Row 1 of the table is 'Onset of bleeding' with 'Immediately after trauma' under Platelet and 'Late bleeding' under Coagulation. (Book p173)",
)

add(
    S1, 173, "match",
    "In the 'Type of bleeding' row on page 173, match each morphological lesion with the exact size range printed against it — 1) Petechiae 2) Purpura 3) Large solitary ecchymotic patch … A) 3–10 mm B) >10 mm C) <3 mm",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "The Platelet column prints 'Petechiae (<3 mm)' and 'Purpura (3–10 mm)', and the Coagulation column prints 'Large solitary ecchymotic patch (>10 mm)'. (Book p173)",
)

add(
    S1, 173, "oddoneout",
    "Every item below is listed in the Coagulation column of the 'Type of bleeding' row on page 173 EXCEPT one. Which belongs to the Platelet column instead?",
    "Mucosal bleeding, with intra-operative bleeding as a printed example",
    [
        "Joint bleeding (Hemarthrosis)",
        "Muscle bleeding, with ilio psoas printed as the most common site",
        "Large solitary ecchymotic patch (>10 mm)",
    ],
    "The Coagulation column prints joint bleeding (hemarthrosis), muscle bleeding ('m/c : Ilio psoas'), hematoma and a large solitary ecchymotic patch. Mucosal bleeding (gum bleed, epistaxis, menorrhagia, intra-operative bleeding), petechiae and purpura are the Platelet column. (Book p173)",
)

add(
    S1, 173, "recall",
    "What is printed in the 'Sex' row of the platelet vs coagulation table on page 173?",
    "Platelet: male = female; Coagulation: male > female",
    [
        "Platelet: male > female; Coagulation: male = female",
        "Platelet: female > male; Coagulation: male > female",
        "Platelet: male = female; Coagulation: female > male",
    ],
    "The last table row 'Sex' reads 'male = Female' under Platelet and 'male > Female' under Coagulation. (Book p173)",
)

add(
    S1, 173, "recall",
    "Under '2. LINEAGE' on page 173, the flowchart splits single lineage from trilineage. Which disorders are printed under the trilineage arm, and what bleeding type is that arm said to produce?",
    "Leukemia, aplastic anemia and MDS, producing platelet related bleeding",
    [
        "Leukemia, lymphoma and myeloma, producing coagulation related bleeding",
        "Aplastic anemia, MDS and ITP, producing primary platelet bleeding",
        "Leukemia, aplastic anemia and hemophilia, producing platelet related bleeding",
    ],
    "The lineage flowchart prints 'Single lineage → 1° platelet bleeding' and 'Trilineage → • Leukemia • Aplastic anemia • MDS' with an arrow down to 'Platelet related bleeding'. (Book p173)",
)

add(
    S1, 173, "numeric",
    "The 'Note : Based on platelet count' box on page 173 links three count bands with three bleeding statements. Which set is printed?",
    ">20,000/µL: no bleeding; <20,000/µL: bleeding +ve; <10,000/µL: severe bleeding (GI bleed, cerebral bleed)",
    [
        ">50,000/µL: no bleeding; <50,000/µL: bleeding +ve; <20,000/µL: severe bleeding",
        ">20,000/µL: no bleeding; <20,000/µL: only petechiae; <5,000/µL: severe bleeding",
        ">1,00,000/µL: no bleeding; <20,000/µL: bleeding +ve; <10,000/µL: purpura only",
    ],
    "Page 173 prints: '• >20,000/µL : No bleeding • <20,000/µL : Bleeding +ve. • <10,000/µL : severe bleeding (GI bleed, cerebral bleed).' (Book p173)",
)

add(
    S1, 173, "recall",
    "Two specific bleeding sites are bracketed in the same Note box on page 173 as indicators of the risk of bleeding. Which two are printed?",
    "Red purpura in pharynx and retinal bleed, marked 'Indicates risk of bleed'",
    [
        "Conjunctival suffusion and scleral icterus, marked 'Indicates risk of bleed'",
        "Oral petechiae and subungual splinter haemorrhages, marked 'Indicates risk of bleed'",
        "Retinal bleed and haemarthrosis, marked 'Indicates risk of bleed'",
    ],
    "The bracket to the right of the count lines on page 173 reads '0/e → Red purpura in pharynx' and '→ Retinal bleed', with the brace labelled 'Indicates risk of bleed'. (Book p173)",
)

add(
    S1, 173, "match",
    "Match each drug group in the step 3 'RULE OUT DRUG INDUCED THROMBOCYTOPENIA' table on page 173 with the mechanism printed beside it — 1) Chemotherapy drugs : Alkylating agents 2) Procainamide, Gold 3) Heparin … A) Produces autoantibody B) Immune complex mediated (Heparin PF4 complex) C) Dose related",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "The step-3 table prints 'Chemotherapy drugs : Alkylating agents → Dose related', 'Procainamide, Gold → Produces autoantibody', 'Heparin → Immune complex mediated (Heparin PF4 complex)'. (Book p173)",
)

# ==============================================================================
# UNIT 2 — Page 174
# ==============================================================================

add(
    S2, 174, "recall",
    "The step-3 drug table continues onto page 174. What mechanism column entry is printed for the three anticonvulsants, and what is printed for NSAIDs?",
    "Both rows carry a dash ('–'), i.e. no mechanism is specified in the table",
    [
        "Both rows are labelled 'Drug specific antibody'",
        "Anticonvulsants are labelled 'Dose related' and NSAIDs 'Hapten dependent antibody'",
        "Anticonvulsants are labelled 'Induce antibody' and NSAIDs 'Immune complex mediated'",
    ],
    "Against 'Anticonvulsants : Carbamazepine, Phenytoin, Valproate' the mechanism cell contains only '–', and the NSAIDs row likewise contains only '–'. (Book p174)",
)

add(
    S2, 174, "recall",
    "Which two Gp IIb/IIIa inhibitors are printed after Abciximab, and what mechanism is shared by the whole Gp IIb/IIIa row?",
    "Eptifibatide and Tirofiban; the mechanism is 'Drug specific antibody'",
    [
        "Eptifibatide and Ticagrelor; the mechanism is 'Hapten dependent antibody'",
        "Tirofiban and Clopidogrel; the mechanism is 'Produces autoantibody'",
        "Eptifibatide and Tirofiban; the mechanism is 'Dose related'",
    ],
    "The row reads 'Gp IIb/IIIa inhibitors : • Abciximab : Thrombocytopenia within 24 hours • Eptifibatide, Tirofiban' with the mechanism column 'Drug specific antibody'. (Book p174)",
)

add(
    S2, 174, "match",
    "Three single-drug/mechanism rows are used to contrast antibody mechanisms on pages 173–174. Match each drug with the exact mechanism printed for it — 1) Quinine 2) Penicillin 3) Procainamide … A) Induce antibody B) Hapten dependent antibody C) Produces autoantibody",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 174 prints 'Quinine → Induce antibody' and 'Penicillin → Hapten dependent antibody'. (Book p174)",
)

add(
    S2, 174, "recall",
    "Under '4. RULE OUT HYPERSPLENISM' on page 174, hypersplenism is explained as sequestration of platelets in which condition, and which of the three arms of the Note flowchart is marked 'm/c'?",
    "Sequestration is 'seen in liver disease'; destruction of platelet is the arm marked 'm/c'",
    [
        "Sequestration is seen in myelofibrosis; bone marrow defect is the arm marked 'm/c'",
        "Sequestration is seen in liver disease; sequestration of platelet is the arm marked 'm/c'",
        "Sequestration is seen in splenic lymphomas; destruction of platelet is the arm marked 'm/c'",
    ],
    "Page 174 prints 'Hypersplenism d/t sequestration of platelets : Seen in liver disease.' In the Note flowchart from '↓ platelet count', the middle arm 'Destruction of platelet' carries 'm/c', while the left arm reads 'Bone marrow defect → No formation of platelet, RBC, WBC' and the right arm 'Sequestration of platelet'. (Book p174)",
)

add(
    S2, 174, "recall",
    "Under '5. PERIPHERAL SMEAR' on page 174, what is the instruction about schistocytes, and which smear pattern is bracketed with immune thrombocytopenic purpura (ITP)?",
    "Schistocytes: 'Rule out HUS/TTP'; a normal smear with 'few giant platelets (Rare)' is bracketed to ITP",
    [
        "Schistocytes: 'Rule out DIC'; a normal smear with no giant platelets is bracketed to ITP",
        "Schistocytes: 'Rule out HUS/TTP'; predominant giant platelets are bracketed to ITP",
        "Schistocytes: 'Rule out TTP'; a normal smear with microspherocytes is bracketed to ITP",
    ],
    "Page 174 prints '• Presence of schistocytes : Rule out HUS/TTP. • Smear normal • Presence of few giant platelets (Rare)' with a brace to 'Immune thrombocytopenic purpura (ITP)'. (Book p174)",
)

add(
    S2, 174, "match",
    "Match each step of the 'SUMMARY' flowchart on page 174 with the next step it leads to — 1) Platelet type bleeding (corresponding to platelet count) 2) Single lineage disorders: RBC, WBC → normal 3) No hypersplenism … A) Not drug induced B) Peripheral smear: normal C) Peripheral smear normal → ITP",
    "1-B, 2-A, 3-C",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B",
    ],
    "The summary flowchart runs downward on page 174: 'Platelet type bleeding (Corresponding to platelet count)' → 'Single lineage disorders : RBC, WBC → Normal' → 'Not drug induced' → 'No hypersplenism' → 'Peripheral smear : Normal' → 'ITP'. (Book p174)",
)

add(
    S2, 174, "truefalse",
    "Which statement about the drug-induced thrombocytopenia step on pages 173–174 is accurate?",
    "True — The step is numbered 3 in the protocol, and heparin acts through an immune complex with platelet factor 4",
    [
        "True — The step is numbered 4 in the protocol, and heparin acts by producing a drug-specific autoantibody",
        "False — Heparin is listed under 'Hapten dependent antibody' in the table",
        "False — Only chemotherapy and antibiotics are listed as causes in this step",
    ],
    "Page 173 numbers the step '3. RULE OUT DRUG INDUCED THROMBOCYTOPENIA' and prints 'Heparin → Immune complex mediated (Heparin PF4 complex)'. Step 4 is hypersplenism on page 174, and the table lists anticonvulsants, Gp IIb/IIIa inhibitors, NSAIDs, quinine and penicillin besides chemotherapy. (Book p174)",
)

# ==============================================================================
# UNIT 3 — Page 175
# ==============================================================================

add(
    S3, 175, "recall",
    "What alternative eponym is printed for Immune Mediated Thrombocytopenic Purpura at the top of page 175, and what age statement immediately follows it?",
    "AKA Werlhof's disease; 'Not seen in elderly'",
    [
        "AKA Evans syndrome; 'Not seen in children'",
        "AKA Werlhof's disease; 'Seen only in elderly'",
        "AKA Moschcowitz disease; 'Not seen in elderly'",
    ],
    "Page 175 opens: 'AKA Werlhof's disease. Not seen in elderly.' Evans syndrome is mentioned later only as the rare indication for a Coombs test. (Book p175)",
)

add(
    S3, 175, "oddoneout",
    "Under 'CAUSES' on page 175, ITP is divided into '1. Primary' and '2. Secondary'. All of the following are printed in the secondary list EXCEPT:",
    "Chronic lymphocytic leukemia",
    [
        "SLE",
        "H. pylori",
        "HCV",
    ],
    "The five secondary causes printed on page 175 are SLE, RA, H. pylori, HIV and HCV — CLL is not among them. (Book p175)",
)

add(
    S3, 175, "recall",
    "Under 'PATHOGENESIS' on page 175, which immunoglobulin class and which two platelet glycoprotein targets are printed for the antibodies, and what second mechanism is stated?",
    "IgG antibodies against Gp IIb/IIIa and Ib/IX, plus inhibition of platelet release from megakaryocytes",
    [
        "IgM antibodies against Gp Ib-IX and Gp VI, plus increased splenic sequestration",
        "IgG antibodies against Gp IIb/IIIa and Gp VI, plus complement-mediated lysis in the liver",
        "IgE antibodies against Gp Ib/IX and Gp IIb/IIIa, plus inhibition of thrombopoietin synthesis",
    ],
    "Page 175 prints: '• Immune (IgG) mediated destruction of platelets (Antibodies against Gp IIb/IIIa & Ib/IX). • Inhibition of platelet release from megakaryocytes.' (Book p175)",
)

add(
    S3, 175, "recall",
    "The three clinical photographs on page 175 are captioned to contrast ITP purpura with vascular purpura. Which description belongs to which?",
    "ITP petechiae and purpura are 'Non palpable, Non blanching'; vascular abnormality related purpura is 'Palpable, branching'",
    [
        "ITP petechiae and purpura are 'Palpable, branching'; vascular purpura is 'Non palpable, non blanching'",
        "ITP petechiae are 'Non palpable but blanching'; vascular purpura is 'Palpable and non blanching'",
        "ITP petechiae and purpura are 'Non palpable, Non blanching'; vascular purpura is 'Non palpable but confluent'",
    ],
    "Beneath the skin photograph the book prints 'Petechiae & purpura : Non palpable. Non blanching.' and, in the Note, 'vascular abnormality related purpura : Palpable, branching.' The other two photographs are 'Oral petechiae' and 'Ecchymosis'. (Book p175)",
)

add(
    S3, 175, "numeric",
    "What platelet count is printed on page 175 as the level below which ITP mucosal bleeding appears, and which specific example is given?",
    "Low platelet count <20,000; the example given is gum bleed",
    [
        "Low platelet count <50,000; the example given is gum bleed",
        "Low platelet count <20,000; the example given is hemarthrosis",
        "Low platelet count <10,000; the example given is epistaxis",
    ],
    "Clinical presentations read 'mucocutaneous bleeding (Low platelet count <20,000). eg : Gum bleed.' (Book p175)",
)

add(
    S3, 175, "match",
    "Match each investigation listed on page 175 with its printed finding — 1) Peripheral smear 2) Bone marrow 3) Coombs test indication … A) Megakaryocyte precursors increased in number B) Evans syndrome (rare), i.e. AIHA plus thrombocytopenia C) Normal RBC, WBC and platelets with few giant platelets",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "Page 175 prints 'Peripheral smear : Normal RBC, WBC, normal platelets & few giant platelets', 'Bone marrow : megakaryocyte, precursors increased in number' and 'Coombs test : • Done in Evans syndrome (Rare). • Common variable immunodeficiency (AIHA) + thrombocytopenia'. (Book p175)",
)

add(
    S3, 175, "recall",
    "Bone marrow examination is not routine in ITP on page 175. Which three situations are listed under 'Done in :' as indications?",
    "Atypical findings (eg. splenomegaly), first episode >60 years, and failure to respond to steroids",
    [
        "Atypical findings (eg. lymphadenopathy), first episode >20 years, and relapse after splenectomy",
        "Splenomegaly, platelet count <10,000/µL, and pregnancy",
        "Atypical findings (eg. splenomegaly), first episode >60 years, and planned splenectomy",
    ],
    "Under 'Bone marrow : … Done in :' the book prints '– Atypical findings (eg : Splenomegaly). – First episode >60 years. – Failure to respond to steroids.' (Book p175)",
)

# ==============================================================================
# UNIT 4 — Page 176
# ==============================================================================

add(
    S4, 176, "oddoneout",
    "Page 176 lists 'Features inconsistent with ITP'. All of the following are printed there EXCEPT:",
    "Predominant normal-sized platelets",
    [
        "Fever, pallor, jaundice and subconjunctival hemorrhage",
        "Bleeding into joints, splenomegaly and lymphadenopathy",
        "Red cell morphological abnormality and WBC abnormality",
    ],
    "Page 176 prints: fever, pallor, jaundice, subconjunctival haemorrhage, bleeding into joints, splenomegaly, lymphadenopathy; then 'Predominant giant platelets'; then red cell morphological abnormality; then WBC abnormality. The option reverses the printed adjective to 'normal-sized'. (Book p176)",
)

add(
    S4, 176, "numeric",
    "The classification flowchart on page 176 defines three ITP durations. Which cut-offs and labels are printed?",
    "<3 months = newly diagnosed; 3 months – 12 months = persistent; >1 year = chronic",
    [
        "<6 months = newly diagnosed; 6–12 months = persistent; >1 year = chronic",
        "<3 months = acute; 3–12 months = persistent; >2 years = chronic",
        "<3 months = newly diagnosed; 3–6 months = persistent; >1 year = chronic",
    ],
    "The 'CLASSIFICATION' bracket headed 'Duration' splits into '<3 months → Newly diagnosed', '3 months – 12 months → Persistent' and '>1 year → Chronic'. (Book p176)",
)

add(
    S4, 176, "numeric",
    "What is the printed treatment goal for ITP on page 176, and how does the treatment flowchart behave above and below that number?",
    "Goal: increase platelet count to 30,000/µL; >30,000 → wait & watch, <30,000 ± bleeding → treat",
    [
        "Goal: increase platelet count to 50,000/µL; >50,000 → wait & watch, <50,000 → treat",
        "Goal: increase platelet count to 30,000/µL; >30,000 → treat, <30,000 ± bleeding → wait & watch",
        "Goal: increase platelet count to 1,00,000/µL; >30,000 → wait & watch, <30,000 ± bleeding → treat",
    ],
    "Page 176 prints 'Goal : Increase platelet count to 30,000/µL to prevent bleeding.', then 'If platelet count' branches to '>30,000 → wait & watch' and '<30,000 ± bleeding → Treat'. (Book p176)",
)

add(
    S4, 176, "recall",
    "What single statement about the course of ITP in children is printed on page 176?",
    "Children: self limiting course",
    [
        "Children: invariably progress to chronic ITP",
        "Children: require splenectomy as first-line therapy",
        "Children: respond only to anti-D immunoglobulin",
    ],
    "Below the wait/watch box the book prints 'Children : Self limiting course.' followed by 'Treatment in adults :'. (Book p176)",
)

add(
    S4, 176, "management",
    "For adults, page 176 gives first-line steroid therapy with a specific dose duration. Which is printed?",
    "Oral prednisolone full dose × 2 weeks, then taper",
    [
        "Oral prednisolone full dose × 6 weeks, then stop abruptly",
        "Oral prednisolone full dose × 2 weeks, then maintain for 6 months",
        "Intravenous methylprednisolone × 3 days, then taper",
    ],
    "Under 'First line : • Steroid :' the book prints 'Oral prednisolone / full dose × 2 weeks' with an arrow down to 'Taper'. (Book p176)",
)

add(
    S4, 176, "recall",
    "Page 176 lists four indications for IVIg/anti-D. Which four are printed?",
    "Surgery, life-threatening bleeding, platelet <10,000/µL, and relapse",
    [
        "Surgery, life-threatening bleeding, platelet <30,000/µL, and pregnancy",
        "Splenomegaly, life-threatening bleeding, platelet <10,000/µL, and relapse",
        "Surgery, chronic ITP >12 months, platelet <10,000/µL, and relapse",
    ],
    "Under 'IVIg/anti-D → a. Indication :' the book prints '– Surgery. – Life threatening bleeding. – Platelet <10,000/µL. – Relapse.' (Book p176)",
)

add(
    S4, 176, "recall",
    "Page 176 explains the mechanism of anti-D and gives two prerequisites. Which combination is printed?",
    "Anti-D binds Rh antigen and is preferentially taken up by the spleen (platelets spared); prerequisites are presence of spleen and Hb >10 mg/dL",
    [
        "Anti-D binds Rh antigen on platelets and is cleared by the liver; prerequisites are presence of spleen and Hb >8 g/dL",
        "Anti-D blocks the Fc receptor in the spleen; prerequisites are presence of spleen and Hb >12 g/dL",
        "Anti-D binds Rh antigen and is preferentially taken up by the spleen (platelets spared); prerequisites are absence of spleen and Hb >10 mg/dL",
    ],
    "Page 176 prints 'b. mechanism : Anti D binds with Rh antigen → Preferentially taken up by spleen (Platelets spared).' and 'c. Pre-requisite : – Presence of spleen. – Hb >10 mg/dL.' The haemoglobin pre-requisite is printed as 'mg/dL' on the page (verified at high zoom on the scan) and is tested without silently correcting the unit. (Book p176)",
)

# ==============================================================================
# UNIT 5 — Page 177
# ==============================================================================

add(
    S5, 177, "recall",
    "Page 177 opens with 'Second line : In relapse'. Which four options are listed?",
    "Rituximab + dexamethasone; thrombopoietin analogue (eltrombopag oral, romiplostim s/c); splenectomy; azathioprine",
    [
        "Rituximab + prednisolone; thrombopoietin analogue (eltrombopag s/c, romiplostim oral); splenectomy; cyclophosphamide",
        "Rituximab + dexamethasone; IVIg; splenectomy; azathioprine",
        "Rituximab + dexamethasone; thrombopoietin analogue (eltrombopag oral, romiplostim s/c); splenic irradiation; azathioprine",
    ],
    "Page 177 prints 'Second line : In relapse • Rituximab + Dexamethasone. • Thrombopoietin analogue, eltrombopag (Oral), romiplostim (s/c). • Splenectomy (Complication). • Azathioprine.' (Book p177)",
)

add(
    S5, 177, "numeric",
    "Under 'Follow up :' on page 177, after how many days is a rise in platelet counts expected following second-line therapy?",
    "2–4 days",
    [
        "7–10 days",
        "24 hours",
        "2–4 weeks",
    ],
    "Page 177 prints 'Follow up : Rise in counts : 2–4 days.' (Book p177)",
)

add(
    S5, 177, "recall",
    "What single line defines a qualitative disorder of platelets on page 177?",
    "Presence of bleeding + normal platelet count",
    [
        "Presence of bleeding + low platelet count",
        "Absence of bleeding + low platelet count",
        "Prolonged bleeding time with thrombocytopenia",
    ],
    "Under 'Qualitative Disorder of Platelets' the book prints 'Presence of bleeding + normal platelet count.' (Book p177)",
)

add(
    S5, 177, "recall",
    "Under qualitative platelet disorder 'CAUSES' on page 177, what is printed as the most common acquired cause, and which other acquired cause is listed?",
    "Uremic bleeding is the m/c acquired cause; the other listed acquired cause is drugs",
    [
        "Drugs are the m/c acquired cause; the other listed acquired cause is uremic bleeding",
        "Liver disease is the m/c acquired cause; the other listed acquired cause is drugs",
        "Uremic bleeding is the m/c acquired cause; the other listed acquired cause is myeloproliferative disease",
    ],
    "The 'CAUSES' bracket on page 177 splits into 'Acquired • uremic bleeding (m/c cause). • Drugs.' and 'Inherited'. (Book p177)",
)

add(
    S5, 177, "match",
    "Match each of the three numbered types of platelet defect on page 177 with the two disorders printed under it — 1) Platelet adhesion defect 2) Granulation defect 3) Activation/aggregation defect … A) Gp IIb-IIIa defect: Glanzmann thrombasthenia, and afibrinogenemia B) Gp Ib-IX defect: Bernard Soulier syndrome (BSS), and von Willebrand disease C) α granule defect: grey platelet, and δ granule defect: Hermansky Pudlak syndrome",
    "1-B, 2-C, 3-A",
    [
        "1-A, 2-C, 3-B",
        "1-B, 2-A, 3-C",
        "1-C, 2-B, 3-A",
    ],
    "Page 177 prints '1. Platelet adhesion defects : • Gp Ib-IX defect : Bernard Soulier syndrome (BSS). • von Willebrand disease (vWD).' ; '2. granulation defect : • α granule defect : Grey platelet. • δ granule defect : Hermansky Pudlak syndrome.' ; '3. Activation/aggregation defect : • Gp IIb-IIIa defect : Glanzmann thrombasthenia. • Afibrinogenemia.' (Book p177)",
)

add(
    S5, 177, "numeric",
    "Under '1. Platelet function analyzer (PFA-100)' on page 177, what does the test screen for and what aperture closure time is printed as abnormal?",
    "It is a screening test; aperture closure time prolonged (>80 sec) indicates a function disorder",
    [
        "It is the gold standard; aperture closure time prolonged (>180 sec) indicates a function disorder",
        "It is a screening test; aperture closure time shortened (<80 sec) indicates a function disorder",
        "It is a confirmatory test; aperture closure time prolonged (>40 sec) indicates a function disorder",
    ],
    "Page 177 prints '• Screening test. • Aperture closure time : Prolonged (>80 sec) → Function disorder.' The aggregation test, not the PFA-100, is labelled the gold standard. (Book p177)",
)

add(
    S5, 177, "match",
    "Match the aggregation-test vocabulary on page 177 with the printed explanation — 1) Weak agents (ADP, epinephrine) 2) All other agents 3) Primary aggregation … A) Directly induce aggregation with no release of granules B) Two waves C) Single wave",
    "1-B, 2-C, 3-A",
    [
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
    ],
    "Page 177 prints: 'weak agents (ADP, epinephrine) → Two waves:', 'All other agents → Single wave', 'a. Primary aggregation : Directly induce aggregation (No release of granules).' and 'b. Secondary aggregation : Release of thromboxane A2 or ADP from granule.' (Book p177)",
)

# ==============================================================================
# UNIT 6 — Page 178
# ==============================================================================

add(
    S6, 178, "match",
    "Match each normal aggregation curve shape illustrated on page 178 with the agents that produce it — 1) Biphasic curve 2) Monophasic curve 3) Biphasic curve, first component … A) Collagen, arachidonic acid, ristocetin B) ADP, epinephrine C) Primary wave (so labelled on the biphasic graph)",
    "1-B, 2-A, 3-C",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B",
    ],
    "The two graphs on page 178 are captioned 'Biphasic curve (ADP epinephrine)' and 'monophasic curve (Collagen, arachidonic acid, ristocetin)' under the heading 'Normal platelet aggregation curve'. (Book p178)",
)

add(
    S6, 178, "recall",
    "The ristocetin agglutination test (RAT) on page 178 is stated to check for what, and which result is printed as 'Negative'?",
    "It checks for adhesion; negative results are Bernard Soulier syndrome (BSS) and von Willebrand disease (vWD)",
    [
        "It checks for aggregation; negative results are Glanzmann thrombasthenia and afibrinogenemia",
        "It checks for adhesion; negative results are Glanzmann thrombasthenia and grey platelet syndrome",
        "It checks for granule release; negative results are BSS and storage pool defect",
    ],
    "Page 178: '3. Ristocetin agglutination test (RAT) : Checks for adhesion' with branches 'Negative : • Bernard soulier syndrome (BSS) • von Willebrand disease (vWD)' and 'Positive → Normal adhesion'. (Book p178)",
)

add(
    S6, 178, "recall",
    "In the RAT flowchart on page 178, a negative RAT is followed by an aPTT. Which result points to vWD and which to BSS, and what parenthetical is printed under aPTT?",
    "Prolonged aPTT → vWD (↓ factor VIII); normal aPTT → BSS; aPTT is labelled '(Common & intrinsic defect)'",
    [
        "Normal aPTT → vWD (↓ factor VIII); prolonged aPTT → BSS; aPTT is labelled '(Extrinsic & common defect)'",
        "Prolonged aPTT → BSS; normal aPTT → vWD; aPTT is labelled '(Common & intrinsic defect)'",
        "Prolonged aPTT → vWD; normal aPTT → Glanzmann thrombasthenia; aPTT is labelled '(Common & extrinsic defect)'",
    ],
    "Page 178 prints 'Check aPTT (Activated partial thromboplastin time) (Common & intrinsic defect)' then 'Prolonged → vWD (↓ factor VIII)' and 'Normal → BSS'. (Book p178)",
)

add(
    S6, 178, "recall",
    "What two line items appear under '4. Bleeding time :' on page 178?",
    "Elevated, and marked '(Obsolete)'",
    [
        "Prolonged, and marked '(Gold standard)'",
        "Normal, and marked '(Screening test)'",
        "Elevated, and marked '(Sensitive but nonspecific)'",
    ],
    "Page 178 prints '4. Bleeding time : Elevated (Obsolete).' (Book p178)",
)

add(
    S6, 178, "recall",
    "The Note box on page 178 lists two functions of von Willebrand factor. Which two are printed?",
    "Platelet adhesion; transports factor VIII",
    [
        "Platelet aggregation; transports factor V",
        "Platelet adhesion; cleaves factor VIII",
        "Endothelial repair; activates protein C",
    ],
    "Page 178 prints 'Note : Function of von willebrand factor : • Platelet adhesion. • Transports factor VIII.' (Book p178)",
)

add(
    S6, 178, "scenario",
    "A patient's platelet aggregation tracings show a normal primary wave with ADP but an absent second wave with ADP and epinephrine, deficient aggregation with collagen, and normal ristocetin agglutination. The page-178 interpretation panel labels this pattern how, and towards which diagnosis does its arrow point?",
    "ADP: primary wave / collagen: deficient / ristocetin: normal, labelled a 'granule defect'",
    [
        "ADP: deficient / collagen: deficient / ristocetin: normal, labelled an 'aggregation defect'",
        "ADP: primary wave / collagen: deficient / ristocetin: absent, labelled a 'granule defect'",
        "ADP: absent / collagen: normal / ristocetin: normal, labelled a 'granule defect'",
    ],
    "The three traces at the foot of page 178 are captioned 'ADP: Primary wave', 'Collagen: Deficient', 'Ristocetin: Normal', with an arrow labelled '→ Granule defect', and the boxed caption reads 'Platelet aggregation curves in storage pool defect (absent the second wave of aggregation with ADP and epinephrine, absent or greatly diminished aggregation with collagen, and normal ristocetin aggregation)'. (Book p178)",
)

add(
    S6, 178, "truefalse",
    "Which statement about the page 178 aggregation figures is accurate?",
    "True — The biphasic curve is so called because a primary wave is followed by a secondary wave, and ADP/epinephrine are the agents that produce it",
    [
        "True — The monophasic curve is produced by ADP and epinephrine and shows two distinct waves",
        "False — Ristocetin is listed among the agents producing a biphasic curve",
        "False — Bleeding time is printed as the gold standard for platelet function on this page",
    ],
    "Page 178 captions the left graph 'Biphasic curve (ADP epinephrine)' showing a labelled 'Primary wave' and 'Secondary wave', and the right graph 'monophasic curve (Collagen, arachidonic acid, ristocetin)'. Bleeding time is labelled obsolete, and the aggregation test (p177) is the gold standard. (Book p178)",
)

# ==============================================================================
# UNIT 7 — Page 179
# ==============================================================================

add(
    S7, 179, "recall",
    "At the foot of the Glanzmann's curves on page 179, two bullet lines distinguish the two defect patterns. Which pair is printed?",
    "'Aggregation defect : No waves seen' and 'granule defect : Primary wave seen in ADP & epinephrine'",
    [
        "'Aggregation defect : Primary wave seen in ADP & epinephrine' and 'granule defect : No waves seen'",
        "'Aggregation defect : Only the second wave is lost' and 'granule defect : No waves seen'",
        "'Aggregation defect : No waves seen' and 'granule defect : Secondary wave preserved with collagen'",
    ],
    "Page 179 prints '• Aggregation defect : No waves seen. • granule defect : Primary wave seen in ADP & epinephrine.' (Book p179)",
)

add(
    S7, 179, "recall",
    "What caption is printed under the Glanzmann's thrombasthenia aggregation curves on page 179, and what arrow label follows them?",
    "Absent aggregation with all agonists except ristocetin; arrow labelled 'Aggregation defect'",
    [
        "Absent aggregation with all agonists including ristocetin; arrow labelled 'Granule defect'",
        "Absent aggregation with ADP and collagen but normal epinephrine; arrow labelled 'Aggregation defect'",
        "Present aggregation with all agonists except ristocetin; arrow labelled 'Adhesion defect'",
    ],
    "Page 179 captions the top traces 'Platelet aggregation curves in Glanzmann's thrombasthenia (absent aggregation with all agonists except ristocetin)' with the arrow 'Aggregation defect'. (Book p179)",
)

add(
    S7, 179, "recall",
    "Under 'optical density test :' on page 179, what relationship between normal agglutination/adhesion and optical density is printed?",
    "Normal agglutination/adhesion → ↓ optical density",
    [
        "Normal agglutination/adhesion → ↑ optical density",
        "Normal agglutination/adhesion → optical density unchanged",
        "Reduced agglutination/adhesion → ↓ optical density",
    ],
    "Page 179 prints 'Optical density test : Normal agglutination/adhesion → ↓ optical density.' (Book p179)",
)

add(
    S7, 179, "match",
    "Match each of the three optical-density interpretation panels on page 179 with its printed reading — 1) Aggregation defect 2) BSS or vWD 3) Storage pool defect / granule defect … A) A: RAT –ve, B: agglutination wave +ve B) A: RAT +ve, B: aggregation –ve C) A: agglutination wave +ve in ADP",
    "1-B, 2-A, 3-C",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B",
    ],
    "The three panels are labelled on their right: 'Aggregation defect — A : RAT +ve, B : Aggregation –ve'; 'BSS or vWD — A : RAT –ve, B : Agglutination wave +ve'; 'Storage pool defect/granule defect — A : Agglutination wave +ve in ADP'. (Book p179)",
)

add(
    S7, 179, "scenario",
    "A 22-year-old woman has lifelong mucocutaneous bleeding, a normal platelet count, absent aggregation with ADP, adrenalin and collagen, but a normal ristocetin response. Which page-179 panel matches this tracing and which single diagnosis does the page's Glanzmann caption imply?",
    "The 'Aggregation defect' panel (A: RAT +ve, B: aggregation –ve), consistent with Glanzmann's thrombasthenia",
    [
        "The 'BSS or vWD' panel (A: RAT –ve, B: agglutination wave +ve), consistent with von Willebrand disease",
        "The 'Storage pool defect/granule defect' panel (A: agglutination wave +ve in ADP), consistent with storage pool defect",
        "The 'Aggregation defect' panel (A: RAT –ve, B: agglutination wave +ve), consistent with Bernard-Soulier syndrome",
    ],
    "Page 179 captions the tracing 'absent aggregation with all agonists except ristocetin' as Glanzmann's thrombasthenia and labels the corresponding right-hand panel 'Aggregation defect — A : RAT +ve, B : Aggregation –ve'. (Book p179)",
)

# ==============================================================================
# UNIT 8 — Page 180
# ==============================================================================

add(
    S8, 180, "recall",
    "Page 180 opens with the reaction 'Fibrinogen —— Thrombin time → Fibrin'. Which disorder is printed with a normal thrombin time and which with a prolonged thrombin time?",
    "Glanzmann thrombasthenia: normal thrombin time; afibrinogenemia: thrombin time prolonged",
    [
        "Glanzmann thrombasthenia: thrombin time prolonged; afibrinogenemia: normal thrombin time",
        "Bernard Soulier syndrome: normal thrombin time; Glanzmann thrombasthenia: thrombin time prolonged",
        "Afibrinogenemia: normal thrombin time; Glanzmann thrombasthenia: thrombin time prolonged",
    ],
    "Under 'Glanzmann thrombasthenia :' the book prints '• Normal thrombin time.' and under 'Afibrinogenemia :' it prints 'Thrombin time prolonged.' in the context of the 'Fibrinogen —Thrombin time→ Fibrin' diagram. (Book p180)",
)

add(
    S8, 180, "recall",
    "Which seven bullet features of Glanzmann thrombasthenia are printed on page 180?",
    "Autosomal recessive; normal thrombin time; GpIIb-IIIa defect (fibrinogen receptor lost); RAT +ve; platelet normal; BT prolonged; recurrent bleeding/heavy menstrual bleeding",
    [
        "Autosomal dominant; prolonged thrombin time; GpIb-IX defect; RAT –ve; platelet low; BT prolonged; recurrent bleeding",
        "Autosomal recessive; normal thrombin time; GpIb-IX defect; RAT –ve; platelet normal; BT normal; recurrent bleeding",
        "Autosomal recessive; normal thrombin time; GpIIb-IIIa defect; RAT –ve; platelet normal; BT prolonged; recurrent bleeding",
    ],
    "Page 180 lists for Glanzmann thrombasthenia: '• Autosomal recessive. • Normal thrombin time. • GpIIb-IIIa defect (Fibrinogen receptor lost). • RAT +Ve. • Platelet normal • BT prolonged • Recurrent episodes of bleeding/heavy menstrual bleeding.' (Book p180)",
)

add(
    S8, 180, "recall",
    "Which three features are printed for Bernard Soulier syndrome on page 180?",
    "Autosomal recessive; deficiency of Gp Ib-IX; RAT negative (adhesion defect)",
    [
        "Autosomal dominant; deficiency of Gp IIb-IIIa; RAT positive (aggregation defect)",
        "Autosomal recessive; deficiency of Gp Ib-IX; RAT positive (adhesion defect)",
        "Autosomal recessive; deficiency of Gp VI; RAT negative (aggregation defect)",
    ],
    "Page 180 prints 'Bernard Soulier syndrome : • Autosomal recessive. • Deficiency of Gp Ib-IX. • RAT negative (Adhesion defect).' (Book p180)",
)

add(
    S8, 180, "recall",
    "What peripheral smear finding is printed for Bernard Soulier syndrome, and what is the caption of the accompanying photomicrograph?",
    "'megathrombocytosis + mild thrombocytopenia'; the photograph is captioned 'megathrombocytosis'",
    [
        "'microthrombocytosis + severe thrombocytopenia'; the photograph is captioned 'megathrombocytosis'",
        "'megathrombocytosis + mild thrombocytopenia'; the photograph is captioned 'giant platelet'",
        "'normal platelets + mild thrombocytopenia'; the photograph is captioned 'platelet clumping'",
    ],
    "Under BSS the book prints 'Peripheral smear : megathrombocytosis + mild thrombocytopenia.' and the smear photograph is captioned 'megathrombocytosis' with arrows on the large platelets. (Book p180)",
)

add(
    S8, 180, "oddoneout",
    "Under 'DRUG INDUCED BLEEDING (QUALITATIVE)' on page 180, all of the following drugs are printed EXCEPT:",
    "Heparin",
    [
        "Aspirin",
        "Beta lactams",
        "Dextran",
    ],
    "The list on page 180 contains Aspirin, Beta lactams, Dipyridamole/Theophylline, Ticlopidine/Clopidogrel and Dextran. Heparin appears instead in the quantitative, thrombocytopenia table on page 173. (Book p180)",
)

add(
    S8, 180, "truefalse",
    "Which statement about the platelet-disorder lines on page 180 is accurate?",
    "True — Afibrinogenemia is distinguished from Glanzmann thrombasthenia by a prolonged thrombin time, because the thrombin-time reaction converts fibrinogen to fibrin",
    [
        "True — Glanzmann thrombasthenia is autosomal dominant and has a prolonged thrombin time",
        "False — Bernard Soulier syndrome has a positive ristocetin agglutination test",
        "False — Megathrombocytosis with mild thrombocytopenia is printed for Glanzmann thrombasthenia",
    ],
    "Page 180 prints the 'Fibrinogen —Thrombin time→ Fibrin' diagram, 'Afibrinogenemia : Thrombin time prolonged.', 'Glanzmann thrombasthenia … Autosomal recessive … Normal thrombin time', 'Bernard Soulier syndrome … RAT negative', and the megathrombocytosis smear under the Bernard Soulier heading. (Book p180)",
)

# ==============================================================================
# UNIT 9 — Page 181
# ==============================================================================

add(
    S9, 181, "recall",
    "What epidemiological claim opens the Von Willebrand Disease section on page 181, and on which chromosome is the gene said to lie?",
    "vWD is the m/c congenital bleeding disorder; the gene is on chromosome 12p",
    [
        "vWD is the second m/c congenital bleeding disorder; the gene is on chromosome 12q",
        "vWD is the m/c congenital bleeding disorder; the gene is on chromosome 7q",
        "vWD is the m/c acquired bleeding disorder; the gene is on chromosome 12p",
    ],
    "Page 181 prints 'VON WILLEBRAND FACTOR : m/c congenital bleeding disorder. gene : On chromosome 12p.' (Book p181)",
)

add(
    S9, 181, "match",
    "Match each vWF structural domain in the table on page 181 with the function printed against it — 1) A 2) D3 3) C … A) Adhesion (Binding of GpIb-IX) B) Carry factor VIII C) For aggregation",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The 'Structure :' table on page 181 prints Site A → 'Adhesion (Binding of GpIb-IX)', D3 → 'Carry factor VIII', and C → 'For aggregation'. (Book p181)",
)

add(
    S9, 181, "recall",
    "The physiology diagram on page 181 traces vWF from megakaryocytes and endothelium. Which assembly sequence and which degrading protease are printed?",
    "vWF monomers → dimers → HMW (high molecular weight) multimers, degraded by ADAMTS 13",
    [
        "vWF monomers → tetramers → LMW multimers, degraded by ADAMTS 13",
        "vWF dimers → monomers → HMW multimers, degraded by plasmin",
        "vWF monomers → dimers → HMW multimers, degraded by thrombin",
    ],
    "Page 181 prints 'megakaryocytes → vWF monomers → Dimers → HMW (High molecular weight) multimers' with 'In circulation → Degraded by ADAMTS 13'. The endothelial alternative is 'In weibel-Palade bodies in endothelium … Stored in the coiled form'. (Book p181)",
)

add(
    S9, 181, "fillup",
    "On the physiology diagram on page 181, the endothelial store of vWF is held 'in the coiled form' and, after 'endothelial injury', vWF is released and ______.",
    "Uncoiled",
    [
        "Cleaved",
        "Polymerised",
        "Internalised",
    ],
    "Page 181 prints the return path 'Stored in the coiled form → endothelial injury → vWF is released and uncoiled'. (Book p181)",
)

add(
    S9, 181, "numeric",
    "Under 'Functions :' on page 181, vWF is said to carry factor VIII with a specific effect on half-life. What values are printed?",
    "↑ T½ : 2 → 12 hours",
    [
        "↑ T½ : 6 → 24 hours",
        "↑ T½ : 12 → 24 hours",
        "↑ T½ : 1 → 6 hours",
    ],
    "Page 181 prints '2. Carry factor VIII (↑ T½ : 2 → 12 hours).' The first listed function is '1. Platelet adhesion.' (Book p181)",
)

add(
    S9, 181, "recall",
    "How are the types of vWD listed at the bottom of page 181, and which type is marked most common and which rare?",
    "Type 1 (m/c); Type 2 with subtypes A, B, M and N; Type 3 (rare)",
    [
        "Type 1 (rare); Type 2 with subtypes A, B, M and N; Type 3 (m/c)",
        "Type 1 (m/c); Type 2 with subtypes A, B and M only; Type 3 (rare)",
        "Type 1 (m/c); Type 2 with subtypes A, B, M and N; Type 3 (m/c)",
    ],
    "Page 181 prints 'TYPES • Type 1 (m/c). • Type 2 — A, B, M, N • Type 3 (Rare).' (Book p181)",
)

# ==============================================================================
# UNIT 10 — Page 182
# ==============================================================================

add(
    S10, 182, "numeric",
    "The Type 1 vs Type 3 table on page 182 gives an incidence figure for Type 1 only. What is printed, and what is printed in the Type 3 incidence cell?",
    "Type 1 incidence 85%; the Type 3 incidence cell carries a dash ('–')",
    [
        "Type 1 incidence 85%; Type 3 incidence 15%",
        "Type 1 incidence 70%; the Type 3 incidence cell carries a dash ('–')",
        "Type 1 incidence 85%; Type 3 incidence 5%",
    ],
    "Row 1 of the table reads 'Incidence | 85% | –', i.e. no numeric incidence is given for Type 3 on this page. (Book p182)",
)

add(
    S10, 182, "match",
    "Match the four table rows for Type 1 vWD on page 182 with the printed entries — 1) Inheritance 2) Type of defect 3) Clinical presentation 4) Age … A) Partial semiquantitative B) Platelet bleed with no coagulation bleed (factor VIII unaffected) and ↑aPTT C) Autosomal dominant (AD) D) 2ⁿᵈ decade",
    "1-C, 2-A, 3-B, 4-D",
    [
        "1-A, 2-C, 3-B, 4-D",
        "1-C, 2-A, 3-D, 4-B",
        "1-D, 2-A, 3-B, 4-C",
    ],
    "The Type 1 column of page 182 reads: Inheritance 'Autosomal dominant (AD)'; Type of defect 'Partial semiquantitative'; Clinical presentation '• Platelet bleed • No coagulation bleed (Factor VIII unaffected) • ↑aPTT'; Age '2ⁿᵈ decade'. (Book p182)",
)

add(
    S10, 182, "recall",
    "In the same table, what is printed for Type 3 vWD across inheritance, defect type, clinical presentation and age?",
    "Autosomal recessive (AR); complete quantitative; severe platelet and coagulation bleed; <5 years",
    [
        "Autosomal recessive (AR); partial semiquantitative; severe platelet bleed only; 2ⁿᵈ decade",
        "Autosomal dominant (AD); complete quantitative; severe platelet and coagulation bleed; <5 years",
        "Autosomal recessive (AR); complete quantitative; severe platelet and coagulation bleed; 2ⁿᵈ decade",
    ],
    "The Type 3 column reads 'Autosomal recessive (AR)', 'Complete quantitative', 'severe platelet and coagulation bleed', and 'Age <5 years'. (Book p182)",
)

add(
    S10, 182, "recall",
    "In the Type 2 sub-table on page 182, which subtype is printed as a gain-of-function mutation producing thrombocytopenia, and which mechanism is given?",
    "2B — gain of function mutation of A-site, with platelet trapping",
    [
        "2A — gain of function mutation of A-site, with absent HMW multimers",
        "2M — gain of function mutation of A-site, with platelet trapping",
        "2N — gain of function mutation of D3 site, with pseudohemophilia",
    ],
    "The Type 2 table prints for 2B: Inheritance AD, 'Gain of function. mutation of A-site : Platelet trapping.', clinical 'Thrombocytopenia'. (Book p182)",
)

add(
    S10, 182, "match",
    "Match each Type 2 subtype on page 182 with its printed defect — 1) 2A 2) 2M 3) 2N … A) Loss of function mutation of A-site (adhesion) B) Qualitative: absent HMW multimers C) Loss of function mutation of D3 site (carry factor VIII)",
    "1-B, 2-A, 3-C",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B",
    ],
    "Page 182 prints 2A 'Qualitative : Absent HMW multimere', 2M 'Loss of function. mutation of A-site : Adhesion.', 2N 'Loss of function. mutation of D3 site : Carry factor VIII.' with clinical 'Coagulation' and 'Pseudohemophilia (Presentation in F)'. (Book p182)",
)

add(
    S10, 182, "fillup",
    "What inheritance pattern is printed for 2N in the Type 2 table, and what is the Note immediately below the table about pseudo von Willebrand disease? Note text: 'Pseudo von willebrand disease : ______ of GpIb – IX.'",
    "Loss of function",
    [
        "Gain of function",
        "Absence",
        "Overexpression",
    ],
    "In the Type 2 table only 2N prints 'AR' while 2A, 2B and 2M print 'AD'; and the Note reads 'Pseudo von willebrand disease : Loss of function of GpIb – IX.' (Book p182)",
)

add(
    S10, 182, "match",
    "Match each disorder in the 'ACQUIRED vWF' table on page 182 with the pathology printed against it — 1) Aortic stenosis 2) Myeloproliferative (PCRV) 3) IgG/IgM paraprotein 4) Hypothyroidism … A) Adhere to platelet : ↑ cleavage B) ↓ Synthesis C) Shear stress and ↑ cleavage D) Immune mediated",
    "1-C, 2-A, 3-D, 4-B",
    [
        "1-A, 2-C, 3-D, 4-B",
        "1-C, 2-D, 3-A, 4-B",
        "1-B, 2-A, 3-D, 4-C",
    ],
    "The acquired vWF table on page 182 lists Aortic stenosis → 'Shear stress and ↑ cleavage'; myeloproliferative (PCRV) → 'Adhere to platelet : ↑ cleavage'; IgG/IgM paraprotein → 'Immune mediated'; Hypothyroidism → '↓ Synthesis'. (Book p182)",
)

add(
    S10, 182, "management",
    "Under 'MANAGEMENT' on page 182, which option is marked '(Best)', what is its mechanism, which type is contraindicated, and what two side effects are printed?",
    "vWF concentrate or desmopressin is the best option; DDAVP works by v2 stimulation raising endothelial vWF; contraindicated in Type 2B; side effects tachyphylaxis and SIADH",
    [
        "vWF concentrate or desmopressin is the best option; it works by v1 stimulation; contraindicated in Type 2N; side effects tachyphylaxis and SIADH",
        "Anti-fibrinolytic therapy is the best option; DDAVP works by v2 stimulation; contraindicated in Type 2M; side effects tachyphylaxis and hypertension",
        "vWF concentrate or desmopressin is the best option; DDAVP works by v2 stimulation; contraindicated in Type 2A; side effects tachyphylaxis and hypernatremia",
    ],
    "Page 182 prints '1. vWF concentrate or 2. Desmopressin (Best)' with 'v2 stimulation → ↑ vWF from endothelium', 'C/I : Type 2B', 'I.V or intranasal', 'S/E : Tachyphylaxis (Developing rapid tolerance) & SIADH' and a bracket 'Only on bleeding', then '3. Anti-fibrinolytic therapy : Add-on.' (Book p182)",
)

# ==============================================================================
# UNIT 11 — Page 183
# ==============================================================================

add(
    S11, 183, "match",
    "Match each clinical-approach row on page 183 (aPTT / PT / Plt) with the disorder group printed against it — 1) Prolonged / Normal / Normal, no bleeding 2) Prolonged / Normal / Normal, mild bleeding 3) Prolonged / Normal / Reduced 4) Normal / INR prolonged / Normal … A) Antiphospholipid syndrome d/t lupus anticoagulant (LAC) B) Factor XII, HMW kininogen and prekallikrein deficiency C) Warfarin, factor VII deficiency and factor III deficiency D) Factor XI deficiency (hemophilia C)",
    "1-B, 2-D, 3-A, 4-C",
    [
        "1-D, 2-B, 3-A, 4-C",
        "1-B, 2-D, 3-C, 4-A",
        "1-A, 2-D, 3-B, 4-C",
    ],
    "Page 183's table prints: prolonged aPTT / normal PT / normal platelets with 'No bleeding → Factor XII deficiency, High molecular weight kininogen deficiency, Prekallikrein deficiency'; with 'mild bleeding → Factor XI deficiency (Hemophilia C)'; then 'Prolonged / Normal / Reduced → Antiphospholipid syndrome : d/t lupus anticoagulant (LAC)'; and 'Normal / INR : Prolonged / Normal → Warfarin, Factor III deficiency, Factor VII deficiency'. (Book p183)",
)

add(
    S11, 183, "match",
    "In the 'severe bleeding' cell of page 183, match each diagnosis with its printed bleeding pattern — 1) Hemophilia A (factor VIII deficiency) 2) Hemophilia B (factor IX deficiency) 3) von Willebrand disease (vWF) … A) Clotting factor type bleed with joint chronic proliferative synovitis and muscle symptoms B) Clotting factor type bleed listed in the same cell as hemophilia A C) Platelet type bleed with RAT (ristocetin agglutination test) negative",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The 'severe bleeding' cell is divided into Hemophilia A, Hemophilia B and von Willebrand disease: the haemophilias carry 'Clotting factor type bleed', 'Joint : Chronic proliferative synovitis' and 'muscle symptoms', whereas vWD carries 'Platelet type bleed' and 'RAT (Ristocetin Agglutination Test) : Negative.' (Book p183)",
)

add(
    S11, 183, "recall",
    "Which two entries share the row 'Prolonged aPTT / Prolonged PT / Reduced platelets' on page 183?",
    "Liver disease (production of all clotting factors except VIII) with dysfibrinogenemia, and disseminated intravascular coagulation",
    [
        "Liver disease (production of all clotting factors except V), and antiphospholipid syndrome",
        "Antiphospholipid syndrome, and disseminated intravascular coagulation",
        "Liver disease (production of all clotting factors except VII), and vitamin K deficiency",
    ],
    "Page 183 prints 'Liver disease (production of all clotting factors except VIII). – Dysfibrinogenemia.' and 'Disseminated intravascular coagulation.' in the prolonged/prolonged/reduced row. (Book p183)",
)

add(
    S11, 183, "recall",
    "In the warfarin row on page 183, what is the printed mechanism, which vitamin-K-dependent factors are listed, and which factor is flagged as having the shortest half-life?",
    "Warfarin inhibits vitamin K epoxide reductase causing vitamin K deficiency; gamma carboxylation of glutamic acid residues of II, VII (shortest t½ : 6 hr), IX, X",
    [
        "Warfarin inhibits vitamin K reductase causing vitamin K deficiency; factors II, VII (shortest t½ : 12 hr), IX, X",
        "Warfarin inhibits vitamin K epoxide reductase; gamma carboxylation of glutamic acid residues of II, VII (shortest t½ : 6 hr), VIII, X",
        "Warfarin inhibits vitamin K epoxide reductase; carboxylation of glutamic acid residues of II, IX (shortest t½ : 6 hr), X, XI",
    ],
    "Page 183 prints 'Warfarin (Inhibit vit K epoxide reductase) → vit K deficiency : gamma carboxylation of glutamic acid residues of II, VII (Shortest t½ : 6hr), IX, X.' followed by 'Factor III deficiency.' and 'Factor VII deficiency.' (Book p183)",
)

add(
    S11, 183, "oddoneout",
    "Under 'ETIOLOGY' on page 183, all of the following are printed EXCEPT:",
    "Nephrotic syndrome",
    [
        "Sepsis (m/c) with monocytes and endothelial injury",
        "Adenocarcinoma cells (lung, colon, prostate)",
        "Kasabach merritt syndrome: cavernous haemangioma traps platelets",
    ],
    "The etiology list on page 183 contains sepsis (m/c), haematological malignancy (APML), placenta and amniotic fluid, adenocarcinoma cells (lung, colon, prostate), trauma, pancreatitis, burns, massive blood transfusion and Kasabach-Merritt syndrome. Nephrotic syndrome is not on it. (Book p183)",
)

add(
    S11, 183, "recall",
    "Which haematological malignancy is named as the DIC trigger on page 183?",
    "Acute promyelocytic leukemia",
    [
        "Acute lymphoblastic leukemia",
        "Chronic myeloid leukemia",
        "Hairy cell leukemia",
    ],
    "Under etiology the book prints 'Hematological malignancy : Acute promyelocytic leukemia.' (Book p183)",
)

# ==============================================================================
# UNIT 12 — Page 184
# ==============================================================================

add(
    S12, 184, "recall",
    "Page 184 draws the DIC pathogenesis as a six-step vertical chain. Which sequence is printed?",
    "Stimulus → endothelial activation → release of tissue factor (thromboplastin) → continuous and excessive thrombin formation and activation → consumption of platelet and clotting factors → bleeding + 2° hyperfibrinolysis (trapping of fibrinogen)",
    [
        "Stimulus → platelet activation → release of vWF → excessive thrombin formation → platelet consumption → thrombosis alone",
        "Stimulus → endothelial activation → release of tissue factor → consumption of clotting factors → excessive thrombin formation → bleeding + 2° hyperfibrinolysis",
        "Stimulus → endothelial activation → release of tissue factor → continuous and excessive thrombin formation → consumption of platelet and clotting factors → thrombosis + 2° hypofibrinolysis",
    ],
    "Page 184 prints the chain: 'Stimulus → Endothelial activation → Release of tissue factor (Thromboplastin) → Continuous and excessive thrombin formation and activation → Consumption of platelet and clotting factors → Bleeding + 2° hyperfibrinolysis (Trapping of fibrinogen)'. (Book p184)",
)

add(
    S12, 184, "recall",
    "The 'Note : monitoring in ICU patients' box on page 184 lists three complications with their monitoring parameters. Which are printed?",
    "ARDS (saturation, chest examination, X-ray), DIC (bleeding with haemorrhagic spots) and myocarditis (tachycardia, hypotension unresponsive to fluids, ↑ troponin I)",
    [
        "ARDS (saturation, chest examination, CT), DIC (bleeding with haemorrhagic spots) and myocarditis (bradycardia, hypertension, ↑ troponin I)",
        "ARDS (saturation, chest examination, X-ray), sepsis (fever, leucocytosis) and myocarditis (tachycardia, hypotension responsive to fluids, ↑ troponin I)",
        "ARDS (saturation, chest examination, X-ray), DIC (thrombosis with gangrene) and pericarditis (tachycardia, hypotension, ↑ troponin I)",
    ],
    "Page 184 prints in the ICU box: 'Acute Respiratory Distress Syndrome (ARDS) : – Saturation. – Chest examination. – X-ray.'; 'DIC : Bleeding (Hemorrhagic spots).'; 'myocarditis : – Pulse rate : Tachycardia. – BP : Hypotension unresponsive to fluids. – ↑ troponin I.' (Book p184)",
)

add(
    S12, 184, "recall",
    "Under 'CLINICAL PRESENTATION' on page 184, which of bleeding and thrombosis is said to dominate, and what parenthetical explains the thrombotic tendency?",
    "Bleeding dominates ('Bleeding … > Thrombosis'); the parenthesis reads '(↓ in anticoagulant factors)'",
    [
        "Thrombosis dominates ('Thrombosis … > Bleeding'); the parenthesis reads '(↑ in anticoagulant factors)'",
        "Bleeding dominates; the parenthesis reads '(↓ in fibrinolytic factors)'",
        "Bleeding and thrombosis occur equally; the parenthesis reads '(↑ in procoagulant factors)'",
    ],
    "Page 184 prints '• Bleeding (↓ clotting factors and platelets) > Thrombosis (↓ in anticoagulant factors)'. It then gives oozing at venipuncture site, petechiae, ecchymosis, and 'Fibrinolysis > anti fibrinolysis.' (Book p184)",
)

add(
    S12, 184, "scenario",
    "An ICU patient with severe DIC develops microvascular thrombosis with necrosis of an extensive area of skin. What name and mechanism does page 184 give for this lesion?",
    "Purpura fulminans — severe DIC with microvascular thrombosis causing necrosis of an extensive area of skin",
    [
        "Purpura fulminans — severe thrombocytopenia causing non-palpable purpura over the limbs",
        "Purpura simplex — microvascular thrombosis causing necrosis of an extensive area of skin",
        "Kasabach-Merritt syndrome — cavernous haemangioma trapping platelets",
    ],
    "Page 184 prints '• Purpura fulminans : Severe DIC (microvascular thrombosis) → Necrosis of extensive area of skin.' (Book p184)",
)

add(
    S12, 184, "match",
    "Match the DIC investigations on page 184 with the superlative printed for them — 1) Fibrin degradation products 2) D-Dimer 3) Peripheral smear … A) Most sensitive, bracketed 'd/t fibrinolysis' B) Most specific, also bracketed 'd/t fibrinolysis' C) Shows fragmented RBC",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 184 prints '• ↑ fibrin degradation products (most sensitive) • ↑ D-Dimer (most specific)' with a brace labelled '⎫ D/t fibrinolysis'. (Book p184)",
)

add(
    S12, 184, "oddoneout",
    "The DIC investigation list on page 184 contains all of the following EXCEPT:",
    "↑ fibrinogen",
    [
        "↓ platelet count",
        "↑ thrombin time (TT)",
        "Peripheral smear: fragmented RBC",
    ],
    "Page 184 prints '↓platelet count', '↑aPTT', '↑PT', '↑fibrin degradation products', '↑D-Dimer', 'Peripheral smear : Fragmented RBC', '↑thrombin time (TT)' and crucially '↓fibrinogen' — fibrinogen falls, it does not rise. (Book p184)",
)

add(
    S12, 184, "management",
    "Under 'MANAGEMENT' on page 184, which products does the cryoprecipitate line credit, and which two measures are marked 'Obsolete'?",
    "Cryoprecipitate supplies VIII, vWF, fibrinogen and XIII (with FFP/platelets transfusion); obsolete measures are drotrecogin alfa (recombinant protein-C) and heparin",
    [
        "Cryoprecipitate supplies II, VII, IX and X; obsolete measures are EACA and FFP",
        "Cryoprecipitate supplies VIII, vWF, fibrinogen and XIII; obsolete measures are EACA and platelets",
        "Cryoprecipitate supplies V, vWF, fibrinogen and XIII; obsolete measures are drotrecogin alfa and heparin",
    ],
    "Page 184 prints '• Treat the cause. • Cryoprecipitate (VIII, vWF, Fibrinogen, XIII)/FFP/platelets transfusion. • Epsilon amino caproic acid (EACA) can be used. • Obsolete : Drotrecogin alfa (Recombinant protein-C), heparin.' with a boxed 'Differential diagnosis : Liver disease.' (Book p184)",
)

GUIDES = {
    S1: (
        "Evaluation Protocol I: Platelet vs Coagulation Bleed Table, Lineage Chart, Count-Based Bleeding Risk & Drug-Induced Thrombocytopenia",
        "Protocol step 1 (p173): platelet bleed starts immediately after trauma whereas coagulation bleed is late; platelet type is mucosal (gum, epistaxis, menorrhagia, intra-operative) with petechiae <3 mm and purpura 3–10 mm; coagulation type is joint (haemarthrosis), muscle (m/c ilio psoas), hematoma and large solitary ecchymotic patch >10 mm; sex male = female vs male > female.\n"
        "Step 2 lineage: single lineage → 1° platelet bleeding; trilineage (leukemia, aplastic anemia, MDS) → platelet related bleeding. Platelet-count risk: >20,000/µL no bleeding, <20,000/µL bleeding +ve, <10,000/µL severe (GI, cerebral); red purpura in pharynx and retinal bleed indicate risk.\n"
        "Step 3 drug-induced thrombocytopenia: chemotherapy/alkylating agents dose related; procainamide and gold produce autoantibody; heparin → immune complex with PF4.",
    ),
    S2: (
        "Evaluation Protocol II: Anticonvulsant/Gp IIb-IIIa/NSAID/Quinine/Penicillin Table, Hypersplenism, Smear & ITP Summary Flowchart",
        "Step 3 table continues (p174): anticonvulsants (carbamazepine, phenytoin, valproate) and NSAIDs have no mechanism listed ('–'); Gp IIb/IIIa inhibitors act by drug-specific antibody (abciximab within 24 hours, plus eptifibatide and tirofiban); quinine induces antibody; penicillin acts as a hapten-dependent antibody.\n"
        "Step 4 hypersplenism: sequestration of platelets, seen in liver disease; of the three arms of ↓ platelet count, destruction of platelet is m/c; the marrow arm produces no platelets, RBC or WBC.\n"
        "Step 5 smear: schistocytes → rule out HUS/TTP; normal smear with a few giant platelets (rare) goes with ITP. The summary flowchart ends: platelet-type bleeding → single-lineage with normal RBC/WBC → not drug induced → no hypersplenism → normal smear → ITP.",
    ),
    S3: (
        "Immune Thrombocytopenic Purpura I: Causes, Gp IIb/IIIa & Ib/IX Antibody Pathogenesis, Clinical Signs & Investigations",
        "ITP basics (p175): AKA Werlhof's disease, not seen in elderly; primary or secondary (SLE, RA, H. pylori, HIV, HCV); IgG antibody-mediated destruction with antibodies against Gp IIb/IIIa and Ib/IX plus inhibition of platelet release from megakaryocytes.\n"
        "Clinical: mucocutaneous bleeding when the count is <20,000/µL (example gum bleed); petechiae and purpura are non-palpable and non-blanching, unlike palpable branching vascular purpura; photographs show petechiae/purpura, oral petechiae and ecchymosis.\n"
        "Investigations: normal smear with a few giant platelets; Coombs test only for Evans syndrome or CVID with AIHA plus thrombocytopenia; marrow shows increased megakaryocytes and precursors, done for atypical findings (splenomegaly), first episode >60 years, or failure to respond to steroids.",
    ),
    S4: (
        "ITP II: Features Inconsistent with ITP, Duration-Based Classification & First-Line Treatment (Steroids, IVIg/Anti-D)",
        "Features inconsistent with ITP (p176): fever, pallor, jaundice, subconjunctival haemorrhage, bleeding into joints, splenomegaly, lymphadenopathy, predominant giant platelets, red-cell morphological abnormality, WBC abnormality. Duration: <3 months newly diagnosed, 3–12 months persistent, >1 year chronic.\n"
        "Treatment aim: raise platelets to 30,000/µL; >30,000 wait and watch, <30,000 ± bleeding treat; children have a self-limiting course.\n"
        "Adults first line: oral prednisolone full dose × 2 weeks then taper, ± IVIg/anti-D (indications: surgery, life-threatening bleeding, platelets <10,000/µL, relapse). Anti-D binds Rh antigen and is taken up preferentially by the spleen sparing platelets; prerequisites are a spleen and Hb >10 mg/dL.",
    ),
    S5: (
        "ITP III: Second-Line Therapy, Follow-Up & Qualitative Platelet Disorders (Causes, Defect Types, PFA-100 & Aggregation Test)",
        "Second line in relapse (p177): rituximab + dexamethasone; thrombopoietin analogues eltrombopag (oral) and romiplostim (s/c); splenectomy; azathioprine. Follow-up: counts rise in 2–4 days.\n"
        "Qualitative platelet disorder = bleeding with a normal platelet count; acquired causes are uremic bleeding (m/c) and drugs, besides inherited causes. Defect types: adhesion (Gp Ib-IX → Bernard-Soulier, and vWD), granulation (α granule → grey platelet, δ granule → Hermansky-Pudlak), activation/aggregation (Gp IIb-IIIa → Glanzmann, and afibrinogenemia).\n"
        "Investigations: PFA-100 is a screening test with prolonged aperture closure time >80 sec; the aggregation test is the gold standard, weak agents (ADP, epinephrine) giving two waves and all other agents one wave; primary aggregation releases no granules, secondary aggregation releases thromboxane A2 or granular ADP.",
    ),
    S6: (
        "Aggregation Curves (Biphasic vs Monophasic), Ristocetin Agglutination Test + aPTT Logic, Bleeding Time & vWF Functions",
        "Normal aggregation curves (p178): biphasic with ADP and epinephrine (primary then secondary wave), monophasic with collagen, arachidonic acid and ristocetin.\n"
        "RAT checks adhesion: negative in Bernard-Soulier syndrome and vWD, positive means normal adhesion. A negative RAT is followed by aPTT (common and intrinsic defect): prolonged aPTT → vWD with low factor VIII, normal aPTT → BSS. Bleeding time is elevated and obsolete.\n"
        "vWF functions: platelet adhesion and transport of factor VIII. Aggregation interpretation strip: ADP primary wave, collagen deficient, ristocetin normal → granule defect (storage pool defect loses the second ADP/epinephrine wave).",
    ),
    S7: (
        "Optical Density Traces: Aggregation Defect vs BSS/vWD vs Storage Pool (Granule) Defect Interpretation",
        "Glanzmann curves on p179 show absent aggregation with all agonists except ristocetin and are labelled 'Aggregation defect'; 'Aggregation defect : No waves seen' while 'granule defect : Primary wave seen in ADP & epinephrine'.\n"
        "Optical density test: normal agglutination/adhesion lowers optical density (↓ optical density).\n"
        "Three interpretation panels: aggregation defect (A: RAT +ve, B: aggregation –ve), BSS or vWD (A: RAT –ve, B: agglutination wave +ve), and storage pool/granule defect (A: agglutination wave +ve in ADP).",
    ),
    S8: (
        "Glanzmann Thrombasthenia, Afibrinogenemia, Bernard-Soulier Syndrome, Megathrombocytosis & Drug-Induced Qualitative Bleeding",
        "Platelet disorders (p180), set against 'Fibrinogen —thrombin time→ Fibrin': Glanzmann thrombasthenia is autosomal recessive with normal thrombin time, GpIIb-IIIa defect (fibrinogen receptor lost), RAT +ve, normal platelet count, prolonged BT and recurrent bleeding or heavy menstrual bleeding.\n"
        "Afibrinogenemia has a prolonged thrombin time. Bernard-Soulier syndrome is autosomal recessive with Gp Ib-IX deficiency, RAT negative (adhesion defect) and a smear showing megathrombocytosis with mild thrombocytopenia.\n"
        "Drug-induced qualitative bleeding: aspirin, beta lactams, dipyridamole/theophylline, ticlopidine/clopidogrel and dextran.",
    ),
    S9: (
        "Von Willebrand Disease I: vWF Gene/Structure Domains, ADAMTS13 Processing, Functions & Types",
        "vWD is the m/c congenital bleeding disorder, gene on chromosome 12p (p181). Structure domains: A → adhesion (binds GpIb-IX), D3 → carries factor VIII, C → aggregation.\n"
        "Physiology: megakaryocyte-derived vWF monomers → dimers → HMW multimers which circulate and are degraded by ADAMTS 13; endothelial vWF is stored coiled in Weibel-Palade bodies and released uncoiled after endothelial injury. Functions: platelet adhesion and carriage of factor VIII (T½ 2 → 12 hours).\n"
        "Types: Type 1 (m/c), Type 2 (2A, 2B, 2M, 2N) and Type 3 (rare).",
    ),
    S10: (
        "Von Willebrand Disease II: Type 1 vs Type 3 Table, Type 2 Subtypes (2A/2B/2M/2N), Acquired vWF & Management",
        "Type 1 vs Type 3 (p182): Type 1 = 85% incidence, autosomal dominant, partial semiquantitative defect, platelet bleed without coagulation bleed (factor VIII unaffected) and ↑aPTT, 2nd decade; Type 3 incidence is not printed ('–'), autosomal recessive, complete quantitative, severe platelet and coagulation bleed, <5 years.\n"
        "Type 2: 2A AD with absent HMW multimers (platelet bleed); 2B AD gain of function at the A-site with platelet trapping (thrombocytopenia); 2M AD loss of function at the A-site (adhesion, platelet bleed); 2N AR loss of function at the D3 site (factor VIII carriage, pseudohemophilia, presentation in females). Pseudo-vWD = loss of function of GpIb-IX.\n"
        "Acquired vWF: aortic stenosis (shear stress, ↑ cleavage), myeloproliferative/PCRV (adherence, ↑ cleavage), IgG/IgM paraprotein (immune mediated), hypothyroidism (↓ synthesis). Management: vWF concentrate or desmopressin (best, v2 stimulation, contraindicated in 2B, IV or intranasal, tachyphylaxis and SIADH), used only on bleeding, with anti-fibrinolytic add-on.",
    ),
    S11: (
        "DIC I: Clinical Approach by aPTT/PT/Platelet Combinations (Factor XII/XI/Hemophilia A & B/vWD/LAC/Liver/Warfarin) & Etiology",
        "Clinical approach table (p183): prolonged aPTT with normal PT and platelets — no bleeding implies factor XII, HMW kininogen or prekallikrein deficiency, mild bleeding implies factor XI (hemophilia C), severe bleeding implies hemophilia A/B (clotting factor bleed, chronic proliferative synovitis, muscle symptoms) or vWD (platelet-type bleed, RAT negative); prolonged aPTT with reduced platelets implies antiphospholipid syndrome from lupus anticoagulant.\n"
        "Prolonged aPTT and PT with reduced platelets implies liver disease (all clotting factors except VIII, dysfibrinogenemia) or DIC; normal aPTT with prolonged INR implies warfarin (vitamin K epoxide reductase inhibition, gamma carboxylation of glutamic acid residues of II, VII with shortest t½ 6 hr, IX, X), factor III or factor VII deficiency.\n"
        "Etiology: sepsis (m/c), APML, placenta and amniotic fluid, adenocarcinoma (lung, colon, prostate), trauma, pancreatitis, burns, massive transfusion, Kasabach-Merritt syndrome.",
    ),
    S12: (
        "DIC II: Pathogenesis Chain, ICU Monitoring, Purpura Fulminans, Investigations (FDP vs D-Dimer) & Management",
        "Pathogenesis (p184): stimulus → endothelial activation → tissue factor release → continuous and excessive thrombin formation → consumption of platelets and clotting factors → bleeding plus secondary hyperfibrinolysis with fibrinogen trapping.\n"
        "ICU monitoring: ARDS (saturation, chest examination, X-ray), DIC with haemorrhagic spots, myocarditis (tachycardia, hypotension unresponsive to fluids, ↑ troponin I). Clinically bleeding exceeds thrombosis with reduced anticoagulant factors; oozing at venipuncture sites, petechiae, ecchymosis; fibrinolysis exceeds antifibrinolysis; purpura fulminans is severe DIC with microvascular thrombosis and skin necrosis.\n"
        "Investigations: ↓ platelets, ↑ aPTT, ↑ PT, ↑ FDP (most sensitive), ↑ D-dimer (most specific), fragmented RBCs, ↑ TT, ↓ fibrinogen. Management: treat the cause, cryoprecipitate (VIII, vWF, fibrinogen, XIII)/FFP/platelets, EACA; drotrecogin alfa and heparin are obsolete; liver disease is the differential diagnosis.",
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
