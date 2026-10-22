#!/usr/bin/env python3
"""Generate Chapter 42: Allergic Bronchopulmonary Aspergillosis (Book p253–256).

Every question is anchored to a printed line, flowchart arm or figure caption of
uploads/03.pdf sheets 6–9 (Book pages 253–256), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 42
TITLE = "Allergic Bronchopulmonary Aspergillosis"
PAGES = "253-256"

S1 = "Aspergillus Microbiology and Its Four Lung Manifestations, with the ABPA Colonisation-to-Bronchiectasis Pathogenesis Flowchart"
S2 = "Th2 Eosinophilic Inflammation, Central Proximal Bronchiectasis on Imaging, ABPA Clinical Features and the Upper-Lobe Fibrosis Causes (Rheumatology)"
S3 = "Upper-Lobe Fibrosis Causes Completed, ABPA Diagnostic Criteria with IgE, PFT Pattern and the Five Imaging Captions"
S4 = "X-Ray Findings Unlikely or Against ABPA, the Steroid–Itraconazole–Omalizumab Treatment Flowchart and IgE Monitoring"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(42000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(42100 + idx).shuffle(shuffled)
    final = list(shuffled)
    final.insert(target, correct)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in final) == 2, f"truefalse: {stem}"
        assert sum(o.startswith("False") for o in final) == 2, f"truefalse: {stem}"
    if fmt == "fillup":
        assert "______" in stem, f"fillup blank: {stem}"
    if fmt == "match":
        assert stem.count(" — 1) ") == 1 and stem.count(" … A) ") == 1, f"match grammar: {stem}"
    exp = explanation.rstrip()
    if not exp.endswith(f"(Book p{page})"):
        exp = f"{exp} (Book p{page})"
    RAW.append((sec, page, fmt, stem, final, final.index(correct), exp))


# ---------------------------------------------------------------- Unit 1: p253
add(
    S1, 253, "recall",
    "Which causative-organism hierarchy and identifying features open the microbiology on page 253?",
    "Aspergillus fumigatus, a saprophyte, ahead of niger, flavus and terreus; identified by conidiophore, septate hyphae and its saprophyte nature",
    [
        "Aspergillus niger ahead of fumigatus, flavus and terreus; identified by conidiophore, septate hyphae and its saprophyte nature",
        "Aspergillus fumigatus, a saprophyte, ahead of niger, flavus and terreus; identified by conidiophore, aseptate hyphae and its parasitic nature",
        "Aspergillus fumigatus ahead of clavatus, niger and flavus; identified by conidial heads only",
    ],
    "The page reads 'Causative organism: Aspergillus fumigatus (Saprophyte) > niger/flavus/terreus' and 'Identifying features: Conidiophore. Septate hyphae. Saprophyte.' A. clavatus is the hypersensitivity pneumonitis antigen of page 257, not in this hierarchy.",
)

add(
    S1, 253, "match",
    "Match each microbiology image on page 253 with its printed caption — 1) Green GMS-stained lung tissue image 2) Blue image on the right … A) Conidial head B) Fungal balls and hyphae of A. fumigatus in GMS stained lung tissue",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "The left micrograph is captioned 'Fungal balls & hyphae of A. fumigatus in GMS stained lung tissue' and the right one simply 'Conidial head', matching two of the three identifying features listed beside them.",
)

add(
    S1, 253, "recall",
    "Which four manifestations of Aspergillus in lung are drawn on page 253?",
    "ABPA; aspergilloma; chronic necrotising aspergillosis, also called chronic cavitating pulmonary aspergillosis; and angio invasive aspergillosis",
    [
        "ABPA; aspergilloma; acute necrotising aspergillosis; and allergic aspergillus sinusitis",
        "Aspergilloma; chronic necrotising aspergillosis, also called chronic cavitating pulmonary aspergillosis; angio invasive aspergillosis; and aspergillus tracheobronchitis with ABPA excluded",
        "ABPA; aspergilloma; chronic necrotising aspergillosis, also called chronic fibrosing pulmonary aspergillosis; and angio invasive aspergillosis",
    ],
    "The 'manifestations in lung' tree has four arms: ABPA, aspergilloma, 'Chronic necrotising aspergillosis/ Chronic cavitating pulmonary aspergillosis' and 'Angio invasive aspergillosis'.",
)

add(
    S1, 253, "match",
    "Match each non-ABPA manifestation with its printed descriptors — 1) Aspergilloma 2) Chronic necrotising or cavitating aspergillosis 3) Angio invasive aspergillosis … A) Bronchial wall invasion, typically in COPD, with thick walled cavities B) Common in neutropenic people and long term steroids, with blood stream infection and bone marrow transplant infections C) Underlying cavity mostly due to TB",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "Aspergilloma carries the single bullet 'underlying cavity mostly due to TB'; chronic necrotising disease carries bronchial wall invasion, typical COPD setting and thick walled cavities; angio invasive disease carries the neutropenic/long-term-steroid host with blood stream and bone marrow transplant infections.",
)

add(
    S1, 253, "recall",
    "Which opening steps does the ABPA pathogenesis flowchart print?",
    "In long standing bronchial Asthma or cystic fibrosis the organism colonises the airway, provoking a complex hypersensitivity reaction of Type I greater than Type III",
    [
        "In long standing COPD the organism invades the airway wall, provoking a complex hypersensitivity reaction of Type III greater than Type I",
        "In long standing bronchial Asthma or cystic fibrosis the organism colonises the airway, provoking a complex hypersensitivity reaction of Type IV greater than Type III",
        "In neutropenic patients the organism colonises the airway, provoking a complex hypersensitivity reaction of Type I greater than Type III",
    ],
    "The flowchart descends 'In patients with long standing bronchial asthma (BA) or cystic fibrosis (CF) → Organism colonises the airway → Complex hypersensitivity reaction + (Type I > Type III)'. Type IV greater than III is hypersensitivity pneumonitis on page 257.",
)

add(
    S1, 253, "match",
    "Match each numbered consequence in the pathogenesis flowchart with its printed downstream path — 1) First numbered arm 2) Eosinophilic inflammation 3) Mucus plugs containing septate hyphae in the bronchial wall … A) Cough with sputum yielding bronchial mucosal plugs with hyphae and eosinophils, and atelectasis B) Eosinophilia with raised IgE, with no further arrow C) Migratory lung infiltrates, and weakening of the bronchial wall due to inflammation leading to bronchiectasis",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-B, 2-C, 3-B"],
    "Arm 1 ends at 'Eosinophilia ↑ IgE'; arm 2, eosinophilic inflammation (also fed by an arrow back from arm 3), splits to migratory lung infiltrates and to weakening of bronchial wall ending in bronchiectasis; arm 3 splits to cough with sputum containing bronchial mucosal plugs (hyphae and eosinophils) and to atelectasis.",
)

add(
    S1, 253, "scenario",
    "A long-standing asthmatic coughs up plugs in which septate hyphae and eosinophils are found, has shifting infiltrates, and is developing bronchiectasis from a weakened bronchial wall. Which single printed mechanism drives all three?",
    "Airway colonisation by Aspergillus with a complex Type I greater than Type III hypersensitivity reaction",
    [
        "Angioinvasion by Aspergillus in a neutropenic host",
        "Colonisation of a TB cavity forming an aspergilloma",
        "Type IV greater than Type III hypersensitivity to inhaled organic dust",
    ],
    "Mucus plugs with hyphae and eosinophils, migratory infiltrates and wall-weakening bronchiectasis are arms 3 and 2 of the ABPA flowchart, all descending from colonisation plus Type I > Type III hypersensitivity in Asthma or CF.",
)

add(
    S1, 253, "truefalse",
    "TRUE or FALSE about the flowchart's bronchiectasis route on page 253.",
    "True — bronchiectasis is reached through eosinophilic inflammation weakening the bronchial wall, not through the mucus-plug arm, whose terminals are plugs in sputum and atelectasis",
    [
        "False — bronchiectasis is the direct terminal of the mucus-plug arm",
        "False — migratory infiltrates, not wall weakening, arrow into bronchiectasis",
        "True — bronchiectasis is reached through atelectasis in the third arm",
    ],
    "Only the 'weakening of bronchial wall due to inflammation' sub-arrow of eosinophilic inflammation descends to 'Bronchiectasis'; the mucus-plug arm ends at bronchial mucosal plugs in sputum and at atelectasis.",
)


# ---------------------------------------------------------------- Unit 2: p254
add(
    S2, 254, "recall",
    "Which immune note and which four bronchiectasis features open page 254?",
    "Eosinophilic inflammation is Th2 mediated through IL 4, IL 5 and IL 13; ABPA bronchiectasis, differentiating it from standard bronchiectasis, is bilateral, upper lobe, central and proximal",
    [
        "Eosinophilic inflammation is Th1 mediated through IL 4, IL 5 and IL 13; ABPA bronchiectasis is unilateral, lower lobe, central and proximal",
        "Eosinophilic inflammation is Th2 mediated through IL 4, IL 5 and IL 13; ABPA bronchiectasis is bilateral, upper lobe, peripheral and distal",
        "Eosinophilic inflammation is Th2 mediated through IL 1, IL 6 and TNF; ABPA bronchiectasis is bilateral, upper lobe, central and proximal",
    ],
    "The Note reads 'Eosinophilic inflammation: Th2 mediated (IL 4, IL 5, IL 13)' — the TH2 trio of page 244 — and 'Features of bronchiectasis in ABPA (To differentiate from standard bronchiectasis): Bilateral, upper lobe, Central, Proximal'. Standard bronchiectasis on page 238 was unilateral.",
)

add(
    S2, 254, "match",
    "Match each page 254 image with its printed labels and caption — 1) Top-left CT lung window 2) Top-right HRCT thorax 3) Bottom-left gross specimen 4) Bottom-right CT chest … A) Tree in bud appearance labelled, captioned central bronchiectasis B) Mucus plugs labelled, captioned hyperattenuated mucus C) Cystic bronchiectasis of central aspects labelled, soft tissue upper lobe nodules representing mucoid impaction with dilated bronchi D) Captioned bronchi distended with mucus in ABPA",
    "1-C, 2-A, 3-D, 4-B",
    ["1-A, 2-C, 3-D, 4-B", "1-C, 2-A, 3-B, 4-D", "1-C, 2-D, 3-A, 4-B"],
    "The four images are captioned 'CT (lung window): Soft tissue upper lobe nodules represent mucoid impaction with dilated bronchi' under the cystic central bronchiectasis label; 'HRCT thorax: Central bronchiectasis' under the tree in bud label; 'Bronchi distended with mucus (ABPA)'; and 'CT chest: Hyperattenuated mucus' under the mucus plugs label.",
)

add(
    S2, 254, "recall",
    "Which clinical presentation is printed for ABPA on page 254?",
    "Recurrent acute exacerbation in a patient with chronic, steroid dependent or refractory-to-treatment or acute bronchial Asthma, or with cystic fibrosis",
    [
        "A first acute exacerbation in a patient with newly diagnosed Asthma or COPD",
        "Recurrent acute exacerbation in a neutropenic patient on long term steroids",
        "Recurrent hemoptysis in a patient with a TB cavity",
    ],
    "Presentation reads 'Recurrent acute exacerbation in a patient with chronic/steroid dependent/refractory to treatment/acute BA or CF', returning to the Asthma-or-CF host of the pathogenesis chart.",
)

add(
    S2, 254, "numeric",
    "Which symptoms, sign frequency and course are printed for ABPA?",
    "Fever with cough and expectoration of a brownish thick mucosal plug; signs — crackles and clubbing — in only 15–20%; and a course that rarely causes upper lobe fibrosis",
    [
        "Fever with cough and expectoration of chocolate colored sputum; signs in only 15–20%; and a course that commonly causes upper lobe fibrosis",
        "Fever with cough and expectoration of a brownish thick mucosal plug; signs — crackles and clubbing — in 80–85%; and a course that rarely causes upper lobe fibrosis",
        "Afebrile cough with gelatinous sputum; signs in only 15–20%; and a course that rarely causes upper lobe fibrosis",
    ],
    "Symptoms read 'Fever + cough with expectoration (Brownish thick mucosal plug)', Signs 'Only in 15 – 20 %: Crackles, Clubbing', and Course 'Rarely cause upper lobe fibrosis'. Chocolate sputum belongs to lung fluke on page 250 and gelatinous sputum to PAP on page 242.",
)

add(
    S2, 254, "scenario",
    "A steroid-dependent asthmatic with recurrent exacerbations expectorates brownish thick plugs; most such patients, the page warns, will show neither of the two listed signs. What are those signs and their combined frequency?",
    "Crackles and clubbing, present in only 15–20% of patients",
    [
        "Wheeze and clubbing, present in only 15–20% of patients",
        "Crackles and fever, present in 80% of patients",
        "Clubbing and hemoptysis, present in only 5% of patients",
    ],
    "Under Signs the page gives only 'Crackles' and 'Clubbing' and heads them 'Only in 15 – 20 %', so their absence in a plug-producing refractory asthmatic argues nothing against ABPA.",
)

add(
    S2, 254, "fillup",
    "ABPA rarely causes upper lobe fibrosis, and the first cause-group in the closing Note is Rheumatology, naming ankylosing spondylitis and ______.",
    "sarcoidosis",
    ["rheumatoid arthritis", "systemic sclerosis", "Sjogren syndrome"],
    "The Note 'upper lobe fibrosis causes: 1. Rheumatology:' lists ankylosing spondylitis on the left and sarcoidosis on the right of the same line, the pair already braced as CTDs in the upper-lobe ILD list on page 242.",
)

add(
    S2, 254, "oddoneout",
    "Pick the ODD ONE OUT — three of these descriptors are printed for ABPA bronchiectasis on page 254, one describes standard bronchiectasis instead:",
    "Unilateral, left lower lobe predominant",
    [
        "Bilateral",
        "Central and proximal",
        "Upper lobe",
    ],
    "ABPA bronchiectasis is bilateral, upper lobe, central and proximal, expressly 'to differentiate from standard bronchiectasis', which on pages 218 and 238 is usually unilateral with a left lower lobe predominance.",
)


# ---------------------------------------------------------------- Unit 3: p255
add(
    S3, 255, "recall",
    "Which groups complete the upper lobe fibrosis causes at the top of page 255?",
    "Occupational exposure with silicosis, coal worker's pneumoconiosis and berylliosis; and lung conditions ABPA, Langerhans cell histiocytosis, hypersensitivity pneumonitis and TB",
    [
        "Occupational exposure with asbestosis, silicosis and berylliosis; and lung conditions ABPA, Langerhans cell histiocytosis, hypersensitivity pneumonitis and TB",
        "Occupational exposure with silicosis, coal worker's pneumoconiosis and berylliosis; and lung conditions ABPA, LAM, hypersensitivity pneumonitis and TB",
        "Drug exposure with bleomycin and amiodarone; and lung conditions ABPA, Langerhans cell histiocytosis, hypersensitivity pneumonitis and TB",
    ],
    "Groups 2 and 3 read 'Occupational exposure: Silicosis, Coal worker's pneumoconiosis, Berylliosis' and 'Lung conditions: ABPA, Langerhans cell histiocytosis, Hypersensitivity pneumonitis, TB', continuing group 1 from page 254 and matching the upper-lobe ILD page 242.",
)

add(
    S3, 255, "numeric",
    "Which obligatory criteria and thresholds does the ABPA evaluation print on page 255?",
    "After a predisposing Asthma or CF, both obligatory criteria are required: IgE above 1000 IU/ml, and a positive immediate skin test or increased IgE antibody to Aspergillus",
    [
        "After a predisposing Asthma or CF, either obligatory criterion suffices: IgE above 100 IU/ml, or a positive immediate skin test to Aspergillus",
        "After a predisposing Asthma or CF, both obligatory criteria are required: IgE above 1000 IU/ml, and precipitins against Aspergillus",
        "Obligatory criteria come first with IgE above 1000 IU/ml, and predisposing Asthma or CF is merely supportive",
    ],
    "Criteria run '1. Predisposing asthma or CF. 2. Obligatory criteria: a. IgE >1000 IU/ml. b. Positive immediate skin test or increased IgE antibody to Aspergillus.' Precipitins sit one tier down among the supportive criteria.",
)

add(
    S3, 255, "recall",
    "Which supportive criteria, and how many of them, does the diagnosis require?",
    "Any two of eosinophilia above 500/µL, precipitins or raised IgG antibody to Aspergillus, and consistent radiographic opacities",
    [
        "All three of eosinophilia above 500/µL, precipitins or raised IgG antibody to Aspergillus, and consistent radiographic opacities",
        "Any two of eosinophilia above 1500/µL, precipitins or raised IgE antibody to Aspergillus, and consistent radiographic opacities",
        "Any one of eosinophilia above 500/µL, precipitins or raised IgG antibody to Aspergillus, and consistent radiographic opacities",
    ],
    "Item 3 reads 'Supportive criteria: Any 2 — a. Eosinophilia >500 /µL. b. Precipitins/↑ IgG antibody to Aspergillus. c. Consistent radiographic opacities.' The antibody class here is IgG, where the obligatory tier used total and specific IgE.",
)

add(
    S3, 255, "match",
    "Match each evaluation bullet on page 255 with its printed statement — 1) Most useful test 2) Predominant PFT pattern 3) Stage 5 PFT pattern … A) Fibrosis with a restrictive pattern B) Obstructive pattern predominantly, attributed to bronchiectasis C) IgE levels, for both diagnosis and follow up",
    "1-C, 2-B, 3-A",
    ["1-B, 2-C, 3-A", "1-C, 2-A, 3-B", "1-A, 2-B, 3-C"],
    "The bullets read 'most useful test for diagnosis and follow up: IgE levels' and 'PFT pattern: Obstructive pattern predominantly (Bronchiectasis). Stage 5: Fibrosis (Restrictive).' The restrictive pattern is reserved for the fibrotic final stage.",
)

add(
    S3, 255, "match",
    "Match each imaging caption on page 255 with its printed expansion — 1) Fleeting infiltrates over the dated film series 2) Tram track shadows 3) Finger in glove 4) Trees in bud, as printed … A) Mucoid impaction in dilated bronchi B) Cylindrical and proximal bronchiectasis of the upper lobe with thickening of the bronchial wall, the nodules C) Parenchymal infiltrates which are irregular and transient D) Parallel linear shadows extending from the hilum in bronchial distribution",
    "1-C, 2-D, 3-A, 4-B",
    ["1-D, 2-C, 3-A, 4-B", "1-C, 2-D, 3-B, 4-A", "1-C, 2-A, 3-D, 4-B"],
    "Captions read 'Fleeting infiltrates: Parenchymal infiltrates which are irregular and transient' under the six dated films, 'Tram track shadows: Parallel linear shadows extending from hilum in bronchial distribution', 'Finger in glove: Mucoid impaction in dilated bronchi', and 'Trees in bud: Cylindrical and proximal bronchiectasis of upper lobe with thickening of bronchial wall (Nodules)', with a separate 'Saccular dilatation' label on the last scan.",
)

add(
    S3, 255, "scenario",
    "An asthmatic has IgE of 1400 IU/ml, a positive immediate skin test to Aspergillus, eosinophilia of 700/µL and consistent opacities, but negative precipitins. Does the page 255 scheme diagnose ABPA, and what will follow-up track?",
    "Yes — both obligatory criteria and two supportive criteria are met, and IgE levels are the most useful test for diagnosis and follow up",
    [
        "No — precipitins are obligatory, so the scheme fails despite the IgE and skin test",
        "Yes — but follow-up tracks the eosinophil count as the most useful test",
        "No — all three supportive criteria are required, and only two are present",
    ],
    "Predisposing Asthma, IgE above 1000 IU/ml and a positive immediate skin test satisfy tiers 1 and 2, and eosinophilia above 500/µL plus consistent radiographic opacities give the 'Any 2' supportive criteria; precipitins are supportive, not obligatory.",
)

add(
    S3, 255, "truefalse",
    "TRUE or FALSE about the ABPA PFT statements on page 255.",
    "True — the predominant pattern is obstructive because of bronchiectasis, while restriction appears only at Stage 5 with fibrosis",
    [
        "False — the predominant pattern is restrictive from the first stage",
        "False — Stage 5 fibrosis is printed with an obstructive pattern",
        "True — the predominant pattern is restrictive, turning obstructive at Stage 5",
    ],
    "The bullet reads 'PFT pattern: Obstructive pattern predominantly (Bronchiectasis). Stage 5: Fibrosis (Restrictive).' Airway disease obstructs until end-stage fibrosis restricts, echoing the pure-airway logic of page 243.",
)


# ---------------------------------------------------------------- Unit 4: p256
add(
    S4, 256, "recall",
    "Which two findings are graded merely 'Unlikely' against an ABPA diagnosis on page 256?",
    "Bronchial wall thickening, and small nodules, with the bracket that they occur only in tree in bud",
    [
        "Bronchial wall thickening, and consolidation",
        "Pleural involvement, and small nodules, with the bracket that they occur only in tree in bud",
        "Bronchial wall thickening, and an air fluid level",
    ],
    "Under 'X-Ray findings against diagnosis of ABPA' the 'Unlikely:' tier lists only bronchial wall thickening and 'Small nodules (Only in tree in bud)'. Wall thickening and nodules did appear inside the page 255 tree-in-bud caption, hence unlikely rather than against.",
)

add(
    S4, 256, "recall",
    "Which five findings are graded fully 'Against' the diagnosis?",
    "Pleural involvement, lymphadenopathy, consolidation, air fluid level and perihilar involvement",
    [
        "Pleural involvement, lymphadenopathy, consolidation, cavitation and perihilar involvement",
        "Pleural effusion, lymphadenopathy, consolidation, air fluid level and basal involvement",
        "Pleural involvement, lymphadenopathy, fleeting infiltrates, air fluid level and perihilar involvement",
    ],
    "The 'Against:' tier lists pleural involvement, lymphadenopathy and consolidation on the left and air fluid level with perihilar involvement on the right. Fleeting infiltrates argue for ABPA on page 255, not against it.",
)

add(
    S4, 256, "scenario",
    "A presumed ABPA film instead shows lymphadenopathy, pleural involvement and a perihilar consolidation with an air fluid level. How does page 256 grade this collection?",
    "Every one of these findings sits in the 'Against' tier, so the film argues against ABPA",
    [
        "These findings sit in the 'Unlikely' tier, so ABPA remains probable",
        "Only the air fluid level is against ABPA; the rest are consistent with it",
        "These are the classic fleeting infiltrates of ABPA and support the diagnosis",
    ],
    "Pleural involvement, lymphadenopathy, consolidation, air fluid level and perihilar involvement make up the complete 'Against' list. The merely unlikely tier holds only bronchial wall thickening and small nodules.",
)

add(
    S4, 256, "management",
    "Which first-line treatment and duration does the page 256 flowchart print, and with what adjunct?",
    "Twelve weeks of steroid, marked DOC, plus an airway clearance device or hypertonic saline",
    [
        "Sixteen weeks of itraconazole, marked DOC, plus an airway clearance device or hypertonic saline",
        "Twelve weeks of steroid, marked DOC, plus omalizumab from the start",
        "Four weeks of steroid, marked DOC, plus postural drainage alone",
    ],
    "Treatment opens '12 weeks steroid (DOC) + airway clearance device/hypertonic saline' — the hypertonic saline and clearance pairing carried over from bronchiectasis care on page 222.",
)

add(
    S4, 256, "management",
    "A patient relapses whenever steroids are tapered, then fails the next step too. Which printed ladder has she climbed?",
    "Steroid dependence or relapse leads to 16 weeks of itraconazole therapy, and no resolution on that leads to omalizumab",
    [
        "Steroid dependence or relapse leads to omalizumab, and no resolution leads to 16 weeks of itraconazole",
        "Steroid dependence or relapse leads to 12 further weeks of steroid, and no resolution leads to itraconazole",
        "Steroid dependence or relapse leads to 16 weeks of voriconazole, and no resolution leads to mepolizumab",
    ],
    "The arrows read 'Steroid dependent/relapse → 16 week Itraconazole therapy → No resolution → Omalizumab' — the anti-IgE biologic of page 247 reserved for the last printed step.",
)

add(
    S4, 256, "fillup",
    "The closing Note of the chapter instructs that ______ levels are to be monitored periodically.",
    "IgE",
    ["IgG precipitin", "eosinophil", "FeNO"],
    "The Note reads 'IgE levels to be monitored periodically', completing the arc from page 255, where IgE was the most useful test for diagnosis and follow up.",
)

add(
    S4, 256, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed steps or agents in the ABPA treatment flow on page 256, one is borrowed from another chapter:",
    "Whole lung lavage for non-resolution",
    [
        "Twelve weeks of steroid as DOC",
        "Sixteen weeks of itraconazole for steroid dependence or relapse",
        "Omalizumab for no resolution",
    ],
    "The ladder is steroid (DOC) with airway clearance or hypertonic saline, then itraconazole, then omalizumab. Whole lung lavage treats pulmonary alveolar proteinosis on page 242 and never enters ABPA care.",
)


GUIDES = {
    S1: (
        "Aspergillus Microbiology and Its Four Lung Manifestations, with the ABPA Colonisation-to-Bronchiectasis Pathogenesis Flowchart",
        "Aspergillus fumigatus, a saprophyte ahead of niger, flavus and terreus (p253), is identified by conidiophore and septate hyphae, illustrated by GMS-stained fungal balls and hyphae and a conidial head.\n"
        "Its lung manifestations are ABPA, aspergilloma in a cavity mostly due to TB, chronic necrotising/cavitating disease with bronchial wall invasion and thick walled cavities typically in COPD, and angio invasive disease of neutropenic and long-term-steroid hosts with bloodstream and transplant infections.\n"
        "In long-standing Asthma or CF, airway colonisation triggers a Type I > Type III complex hypersensitivity producing eosinophilia with raised IgE, eosinophilic inflammation with migratory infiltrates and wall-weakening bronchiectasis, and septate-hypha mucus plugs expectorated with eosinophils or causing atelectasis.",
    ),
    S2: (
        "Th2 Eosinophilic Inflammation, Central Proximal Bronchiectasis on Imaging, ABPA Clinical Features and the Upper-Lobe Fibrosis Causes (Rheumatology)",
        "The eosinophilic inflammation is Th2 mediated via IL-4, IL-5 and IL-13 (p254), and ABPA bronchiectasis differs from standard disease by being bilateral, upper lobe, central and proximal.\n"
        "Images show cystic central bronchiectasis with mucoid impaction, tree-in-bud central bronchiectasis, bronchi distended with mucus, and hyperattenuated mucus plugs on CT.\n"
        "Clinically, recurrent exacerbations strike chronic, steroid-dependent, refractory or acute Asthma or CF with fever and brownish thick mucosal plugs, crackles and clubbing in only 15–20%, and rarely upper lobe fibrosis — whose rheumatological causes are ankylosing spondylitis and sarcoidosis.",
    ),
    S3: (
        "Upper-Lobe Fibrosis Causes completed, ABPA Diagnostic Criteria with IgE, PFT Pattern and the Five Imaging Captions",
        "Upper lobe fibrosis (p255) is completed by occupational silicosis, coal-worker's pneumoconiosis and berylliosis, and by the lung conditions ABPA, Langerhans cell histiocytosis, hypersensitivity pneumonitis and TB.\n"
        "Diagnosis needs predisposing Asthma or CF, both obligatory criteria (IgE above 1000 IU/ml and a positive immediate skin test or raised Aspergillus-specific IgE), and any two supportive criteria (eosinophilia above 500/µL, precipitins or raised IgG to Aspergillus, consistent radiographic opacities), with IgE the most useful test for diagnosis and follow-up and PFT obstructive until Stage 5 fibrotic restriction.\n"
        "Imaging captions define fleeting irregular transient infiltrates, tram track parallel hilar shadows, finger-in-glove mucoid impaction, trees-in-bud proximal upper-lobe bronchiectasis with wall thickening, and saccular dilatation.",
    ),
    S4: (
        "X-Ray Findings Unlikely or Against ABPA, the Steroid–Itraconazole–Omalizumab Treatment Flowchart and IgE Monitoring",
        "On page 256, bronchial wall thickening and small nodules (only in tree in bud) are merely unlikely in ABPA.\n"
        "Pleural involvement, lymphadenopathy, consolidation, air fluid level and perihilar involvement are fully against the diagnosis.\n"
        "Treatment is 12 weeks of steroid (DOC) with airway clearance or hypertonic saline, escalating on steroid dependence or relapse to 16 weeks of itraconazole and on non-resolution to omalizumab, with IgE levels monitored periodically.",
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
            {"chapter": CHAPTER, "title": TITLE, "pageRange": PAGES,
             "questions": questions, "units": units},
            ensure_ascii=False, indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {out.name}: {len(questions)} questions / {len(units)} units")


if __name__ == "__main__":
    main()
