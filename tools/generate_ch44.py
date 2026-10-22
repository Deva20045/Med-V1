#!/usr/bin/env python3
"""Generate Chapter 44: Pleural Effusion (Book p260–263).

Every question is anchored to a printed line, table cell or figure caption of
uploads/03.pdf sheets 13–16 (Book pages 260–263), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 44
TITLE = "Pleural Effusion"
PAGES = "260-263"

S1 = "Pleural Anatomy and Fluid Composition, Detection Thresholds, and Light's Criteria with the Diuretic Disadvantage"
S2 = "Transudative and Exudative Causes, Drugs Causing Effusion, TB Effusion Presentation and General Examination Signs"
S3 = "Parapneumonic Effusion and Empyema, Low-pH Causes, and Chylothorax versus Pseudochylothorax"
S4 = "Pleural Fluid Glucose, ICD Indications, Eosinophils in Pleural Fluid, and Tuberculous and Neoplastic Effusion Diagnosis"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(44000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(44100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p260
add(
    S1, 260, "recall",
    "Which pleural cavity statements open the anatomy on page 260?",
    "The cavity is lined by mesothelial cells, which produce surfactant as printed; its pressure is negative due to pleural lymphatics and vacuum; and the pleura is the coupling organ between lungs and chest wall",
    [
        "The cavity is lined by endothelial cells; its pressure is negative due to pleural lymphatics and vacuum; and the pleura is the coupling organ between lungs and chest wall",
        "The cavity is lined by mesothelial cells, which produce surfactant as printed; its pressure is positive due to pleural lymphatics; and the pleura separates the lungs from each other",
        "The cavity is lined by mesothelial cells; its pressure is negative due to elastic recoil alone as printed; and the pleura is the coupling organ between lungs and chest wall",
    ],
    "The bullets read 'Lined by: mesothelial cells (produce surfactant)', 'Negative intrapleural pressure d/t → Pleural lymphatics, vacuum' and 'Coupling organ b/w lungs and chest wall' — the lymphatic-vacuum mechanism already drawn on page 193.",
)

add(
    S1, 260, "numeric",
    "Which normal volume and detection thresholds are printed for pleural fluid on page 260?",
    "Normal amount 10–20 ml; minimum to detect an effusion is 50 mL by USG and lateral X-ray, 200 mL by CXR PA view and 300 mL clinically",
    [
        "Normal amount 10–20 ml; minimum to detect an effusion is 50 mL clinically, 200 mL by USG and 300 mL by CXR PA view",
        "Normal amount 50 ml; minimum to detect an effusion is 100 mL by USG and lateral X-ray, 200 mL by CXR PA view and 300 mL clinically",
        "Normal amount 10–20 ml; minimum to detect an effusion is 50 mL by USG and lateral X-ray, 300 mL by CXR PA view and 200 mL clinically",
    ],
    "The page gives 'Normal amount of pleural fluid (PF): 10–20 ml' and 'minimum amount of pleural fluid needed to detect effusion by: USG and lateral X-Ray: 50mL. CXR PA view: 200 mL. Clinically: 300 mL.' Sensitivity falls from ultrasound to film to the bedside.",
)

add(
    S1, 260, "match",
    "Match each pleural layer with its printed origin and pain property — 1) Parietal pleura 2) Visceral pleura … A) Develops, printed 'Developes', from splanchnopleural mesoderm and is pain insensitive B) Develops, printed 'Developes', from somatopleuric mesoderm and is pain sensitive",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "Types of pleura read 'Parietal: Developes from somatopleuric mesoderm (pain sensitive)' and 'Visceral: Developes from splanchnopleural mesoderm (Pain insensitive)', the verb spelled 'Developes' in both lines.",
)

add(
    S1, 260, "numeric",
    "Which cellular percentages compose normal pleural fluid on page 260?",
    "Macrophages 70%, lymphocytes 25% and mesothelial cells 1–5%",
    [
        "Macrophages 25%, lymphocytes 70% and mesothelial cells 1–5%",
        "Macrophages 70%, lymphocytes 25% and neutrophils 1–5%",
        "Macrophages 70%, lymphocytes 25% and mesothelial cells 10–15%",
    ],
    "Composition reads 'macrophages: 70%. Lymphocytes: 25%. mesothelial cells: 1–5%.' The lining cell appears only as a small shed minority in its own fluid.",
)

add(
    S1, 260, "numeric",
    "Which chemical composition is printed for normal pleural fluid?",
    "Glucose approximately equal to blood glucose, protein 1–1.5 g/dL, and LDH below 50% of plasma LDH",
    [
        "Glucose half of blood glucose, protein 1–1.5 g/dL, and LDH below 50% of plasma LDH",
        "Glucose approximately equal to blood glucose, protein 3–5 g/dL, and LDH above 50% of plasma LDH",
        "Glucose approximately equal to blood glucose, protein 1–1.5 g/dL, and LDH equal to plasma LDH",
    ],
    "The right-hand composition bullets read 'Glucose ~ blood glucose', 'Protein: 1–1.5 g/dL' and 'LDH: < 50% of plasma LDH' — the low protein and LDH baseline that Light's criteria below are built to detect departures from.",
)

add(
    S1, 260, "recall",
    "What purpose is printed for Light's criteria on page 260?",
    "To distinguish between exudative and transudative pleural effusion",
    [
        "To distinguish tuberculous from malignant pleural effusion",
        "To distinguish pleural effusion from pleural thickening",
        "To decide which effusions need an intercostal drain",
    ],
    "Under 'LIGHT'S CRITERIA' the single bullet reads 'Distinguish between exudative and transudative pleural effusion', the gateway decision for the cause lists on page 261.",
)

add(
    S1, 260, "numeric",
    "Which three numbered ratios form Light's criteria as printed?",
    "Pleural fluid to serum protein at or above 0.5; pleural fluid to serum LDH at or above 0.6; and pleural fluid LDH above two-thirds of the upper limit of normal serum LDH",
    [
        "Pleural fluid to serum protein above 0.6; pleural fluid to serum LDH above 0.5; and pleural fluid LDH above two-thirds of the upper limit of normal serum LDH",
        "Pleural fluid to serum protein at or above 0.5; pleural fluid to serum LDH at or above 0.6; and serum LDH above two-thirds of the upper limit of pleural fluid LDH",
        "Pleural fluid to serum albumin at or above 0.5; pleural fluid to serum LDH at or above 0.6; and pleural fluid LDH above one-third of the upper limit of normal serum LDH",
    ],
    "The three criteria are printed as fractions: pleural fluid protein over serum protein '≥ 0.5', pleural fluid LDH over serum LDH '≥ 0.6', and 'Pleural fluid LDH > 2/3rd of upper limit of normal S. LDH'.",
)

add(
    S1, 260, "match",
    "Match each Light's-criteria outcome with its printed classification — 1) Any one criterion present 2) All three negative … A) Transudative B) Exudative",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "The brace beside the three criteria reads 'Any 1 present → exudative' and 'All 3 negative → transudative'. One positive ratio is enough to call the fluid an exudate.",
)

add(
    S1, 260, "scenario",
    "A CCF patient on diuretics has an effusion meeting one Light criterion. Which printed disadvantage and which substitute test apply?",
    "One-third of such patients are wrongly classified as exudate, so the serum–pleural fluid albumin gradient is used instead, a higher gradient indicating transudative fluid",
    [
        "One-third are wrongly classified as transudate, so pleural fluid NT pro BNP replaces Light's criteria",
        "All such patients are wrongly classified, so the serum–pleural fluid albumin gradient is used, a lower gradient indicating transudative fluid",
        "One-third of such patients are wrongly classified as exudate, so the criteria are simply repeated after stopping diuretics as printed",
    ],
    "Disadvantages read 'In patients with CCF on diuretics → 1/3rd wrongly classified as exudate' and 'Instead use: Serum pleural fluid albumin gradient (Higher → transudative)'. NT pro BNP enters only as a cause marker on pages 261 and 263.",
)


# ---------------------------------------------------------------- Unit 2: p261
add(
    S2, 261, "recall",
    "Which ten transudative causes are numbered on page 261?",
    "CCF (NT pro BNP in pleural fluid), cirrhosis, nephrotic syndrome, hypothyroidism, hypoalbuminemia, Budd-Chiari syndrome, chronic constrictive pericarditis, SVC obstruction as printed 'SVC obstructive', peritoneal dialysis and urinothorax",
    [
        "CCF (NT pro BNP in pleural fluid), cirrhosis, nephrotic syndrome, hypothyroidism, hypoalbuminemia, Budd-Chiari syndrome, chronic constrictive pericarditis, pulmonary embolism, peritoneal dialysis and urinothorax",
        "CCF, cirrhosis, nephrotic syndrome, hyperthyroidism, hypoalbuminemia, Budd-Chiari syndrome, chronic constrictive pericarditis, SVC obstruction, peritoneal dialysis and urinothorax, with no NT pro BNP bracket printed",
        "CCF (NT pro BNP in pleural fluid), cirrhosis, nephritic syndrome, hypothyroidism, hypoalbuminemia, Budd-Chiari syndrome, acute pericarditis, SVC obstruction, peritoneal dialysis and urinothorax",
    ],
    "The transudative column numbers CCF with '(NT pro BNP in PF)', cirrhosis, nephrotic syndrome, hypothyroidism, hypoalbuminemia, Budd-Chiari syndrome, chronic constrictive pericarditis, 'SVC obstructive', peritoneal dialysis and urinothorax. Pulmonary embolism is kept for the both-types note below.",
)

add(
    S2, 261, "fillup",
    "Urinothorax, the tenth transudative cause, is bracketed as low pH with high creatinine and an ______ odor.",
    "ammoniacal",
    ["sweet", "sulphurous", "fishy"],
    "The bracket reads '(low pH + high creatinine + ammoniacal odor)' — urine chemistry announcing itself in the pleural space.",
)

add(
    S2, 261, "recall",
    "Which six exudative causes are numbered opposite, and which braces qualify them?",
    "TB, pneumonia, malignancy, connective tissue disorders branching to RA and SLE, acute pancreatitis and esophageal rupture — the last two braced together as predominant left side pleural effusion",
    [
        "TB, pneumonia, malignancy, connective tissue disorders branching to RA and SLE, acute pancreatitis and esophageal rupture — braced as predominant right side pleural effusion",
        "TB, pneumonia, malignancy, connective tissue disorders branching to scleroderma and SLE, acute pancreatitis and esophageal rupture — the last two braced as predominant left side pleural effusion",
        "TB, pneumonia, malignancy, vasculitis, acute pancreatitis and esophageal rupture — the last two braced as predominant left side pleural effusion",
    ],
    "The exudative column numbers TB, pneumonia, malignancy, connective tissue disorders with arrows to RA and SLE, acute pancreatitis and esophageal rupture, with a brace over the last two reading 'Predominant left side PE'.",
)

add(
    S2, 261, "oddoneout",
    "Pick the ODD ONE OUT — three of these statements are printed under CAUSES on page 261, one reverses the page:",
    "Pulmonary embolism is numbered among the pure transudative causes",
    [
        "Pulmonary infarction and pulmonary embolism cause both exudative and transudative effusions",
        "Nitrofurantoin, dantrolene, methysergide and bromocriptine are the listed drugs causing pleural effusion",
        "Acute pancreatitis and esophageal rupture give predominantly left-sided effusions",
    ],
    "Pulmonary infarction and pulmonary embolism appear only under 'Diseases with both exudative & transudative PE', never in either numbered column. The drug list — nitrofurantoin, dantrolene, methysergide, bromocriptine — follows immediately below.",
)

add(
    S2, 261, "recall",
    "Which patients and pain story are printed for pleural effusion with TB?",
    "Twenty to thirty years old, females more than males, on first exposure to TB, with pleuritic pain initially — for example pain on inspiration — that then decreases due to the effusion itself",
    [
        "Twenty to thirty years old, males more than females, on reactivation TB, with pleuritic pain that increases as the effusion grows",
        "Fifty to seventy years old, females more than males, on first exposure to TB, with pain decreasing due to the effusion itself",
        "Twenty to thirty years old, females more than males, on first exposure to TB, with pain absent throughout",
    ],
    "PE with TB reads '20–30 yrs old', 'F > m' and 'First exposure to TB', braced to 'Pleuritic pain initially (E.g., pain on inspiration) → pain decreases d/t PE' as fluid separates the inflamed pleural surfaces.",
)

add(
    S2, 261, "numeric",
    "Which delayed outcome is arrowed for primary TB effusion on page 261?",
    "Over 5–10 years, 25–30% of patients with effusion due to primary TB develop pulmonary TB",
    [
        "Over 5–10 months, 25–30% develop pulmonary TB",
        "Over 5–10 years, 5–10% develop pulmonary TB",
        "Over 25–30 years, 5–10% develop miliary TB as printed",
    ],
    "The arrow reads 'Patients with PE d/t primary TB — 5–10 yrs → 25–30% develop pulmonary TB', making the effusion a marker of future parenchymal disease.",
)

add(
    S2, 261, "match",
    "Match each examination step with its printed effusion findings — 1) Inspection 2) Palpation 3) Percussion 4) Auscultation … A) Reduced breath sound and reduced vocal resonance B) Stony dullness C) Tracheal deviation to the opposite side D) Tracheal deviation confirmed, with reduced vocal fremitus and reduced chest movement",
    "1-C, 2-D, 3-B, 4-A",
    ["1-D, 2-C, 3-B, 4-A", "1-C, 2-D, 3-A, 4-B", "1-C, 2-B, 3-D, 4-A"],
    "General examination runs inspection showing tracheal deviation to the opposite side, palpation confirming that deviation with '↓ vocal fremitus' and '↓ Chest movement', percussion giving 'Stony dullness', and auscultation giving '↓ Breath sound' and '↓ vocal resonance'.",
)

add(
    S2, 261, "scenario",
    "A film beside the examination list shows a white-out left hemithorax. Which caption does it carry, tying image to examination?",
    "'Left sided PE showing tracheal deviation to right'",
    [
        "'Left sided PE showing tracheal deviation to left'",
        "'Right sided PE showing tracheal deviation to right'",
        "'Loculated PE on the right with a central trachea'",
    ],
    "The caption reads 'Left sided PE showing tracheal deviation to right', the radiographic counterpart of the inspection finding printed beside it. The loculated right effusion with a central trachea is the contrasting film on page 263.",
)


# ---------------------------------------------------------------- Unit 3: p262
add(
    S3, 262, "match",
    "Match each parapneumonic row with its uncomplicated versus complicated pair on page 262 — 1) Pathogenesis 2) Glucose and pH 3) LDH and protein 4) Gram stain … A) Normal glucose with pH 7.3–7.4 versus glucose below 60, printed g/L, with pH below 7.2 B) Negative versus positive C) Inflammation with exudative leak versus bacterial invasion with fibrin and septation D) High LDH and high protein versus very high LDH above 1000 and very high protein",
    "1-C, 2-A, 3-D, 4-B",
    ["1-A, 2-C, 3-D, 4-B", "1-C, 2-A, 3-B, 4-D", "1-C, 2-D, 3-A, 4-B"],
    "Uncomplicated or synpneumonic or simple parapneumonic effusion is an inflammatory exudative leak with normal glucose, pH 7.3–7.4, high LDH and protein and a negative Gram stain; the complicated effusion adds bacterial invasion with fibrin and septation, glucose '< 60 g/L' as printed, pH '< 7.2', 'very high' LDH above 1000 and protein, and a positive Gram stain.",
)

add(
    S3, 262, "recall",
    "Which five statements define empyema under the parapneumonic table?",
    "It is a complicated parapneumonic effusion with macroscopic pus, the common complication of parapneumonic effusion (grammar as printed), with pleural fluid protein above 8 g/dL, pleural fluid LDH above 1000 IU/L and a split pleura sign on CT",
    [
        "It is an uncomplicated parapneumonic effusion with microscopic pus, with pleural fluid protein above 8 g/dL, pleural fluid LDH above 1000 IU/L and a split pleura sign on CT",
        "It is a complicated parapneumonic effusion with macroscopic pus, with pleural fluid protein above 5 g/dL, pleural fluid LDH below 1000 IU/L and a split pleura sign on CT",
        "It is a complicated parapneumonic effusion with macroscopic pus, with pleural fluid protein above 8 g/dL, pleural fluid LDH above 1000 IU/L and an air bronchogram on CT",
    ],
    "Empyema bullets read 'Complicated parapneumonic effusion + macroscopic pus', 'Common complications of parapneumonic effusion', 'P.F. protein > 8 g/dL', 'P.F. LDH > 1000 IU/L' and 'CT: Split pleura sign'.",
)

add(
    S3, 262, "match",
    "Match each CT image under the empyema bullets with its printed caption — 1) Left scan, labelled C 2) Right scan, labelled D … A) Pulmonary abscess B) Empyema with split pleura sign",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "Scan C is captioned 'Empyema: Split pleura sign' and scan D 'Pulmonary abscess', setting the pleural collection against its parenchymal mimic.",
)

add(
    S3, 262, "recall",
    "Which three causes of low pleural fluid pH are numbered in the Note, and which carries a prognostic arrow?",
    "Rheumatoid arthritis, complicated parapneumonic effusion, and malignancy — with malignancy arrowed to poor prognosis",
    [
        "Rheumatoid arthritis, uncomplicated parapneumonic effusion, and malignancy — with rheumatoid arthritis arrowed to poor prognosis",
        "SLE, complicated parapneumonic effusion, and malignancy — with malignancy arrowed to poor prognosis",
        "Rheumatoid arthritis, complicated parapneumonic effusion, and TB — with TB arrowed to poor prognosis",
    ],
    "The Note 'Low pH of pleural fluid' numbers rheumatoid arthritis, complicated parapneumonic effusion and 'malignancy → poor prognosis'. The same rheumatoid fluid reappears with the lowest glucose on page 263.",
)

add(
    S3, 262, "match",
    "Match each row of the chylothorax versus pseudochylothorax table with its printed pair — 1) Appearance 2) Causes 3) Pathogenesis 4) Pleural fluid … A) Pleural thickening producing an exudative effusion enriched with cholesterol crystals in pseudochylothorax versus lymphatic rupture in chylothorax B) Trauma and lymphoma in chylothorax versus TB and RA in pseudochylothorax C) Raised triglyceride and raised cholesterol in chylothorax versus raised cholesterol crystals with cholesterol above 250 mg/dL in pseudochylothorax D) Milky white, merged across both columns",
    "1-D, 2-B, 3-A, 4-C",
    ["1-B, 2-D, 3-A, 4-C", "1-D, 2-B, 3-C, 4-A", "1-D, 2-A, 3-B, 4-C"],
    "Appearance 'milky white' spans both diseases; causes split trauma/lymphoma against TB/RA; pathogenesis splits lymphatic rupture against pleural thickening enriching an exudate with cholesterol crystals; and fluid splits raised triglyceride with raised cholesterol against cholesterol crystals quantified as cholesterol above 250 mg/dL.",
)

add(
    S3, 262, "scenario",
    "A pneumonia patient's effusion now yields macroscopic pus, a positive Gram stain, pH 7.0, LDH above 1000 and protein above 8 g/dL, and CT shows the pleura split around the collection. Which printed stage is this?",
    "Empyema complicating a parapneumonic effusion",
    [
        "Uncomplicated synpneumonic effusion",
        "Complicated parapneumonic effusion still short of empyema",
        "Pseudochylothorax from pleural thickening",
    ],
    "Macroscopic pus is the defining step beyond a complicated parapneumonic effusion, and the protein above 8 g/dL, LDH above 1000 IU/L and split pleura sign are empyema's three printed corroborations.",
)

add(
    S3, 262, "truefalse",
    "TRUE or FALSE about the two milky effusions on page 262.",
    "True — both look milky white, but chylothorax is a lymphatic rupture after trauma or lymphoma, while pseudochylothorax is a thickened-pleura exudate of TB or RA enriched with cholesterol crystals",
    [
        "False — only chylothorax is milky white; pseudochylothorax is straw coloured as printed",
        "False — chylothorax is caused by TB and RA and pseudochylothorax by trauma",
        "True — both are transudates from lymphatic rupture",
    ],
    "The merged appearance cell is 'milky white' for both, after which causes and pathogenesis diverge exactly as the correct option states, and pseudochylothorax is expressly an exudative effusion in its pathogenesis cell.",
)


# ---------------------------------------------------------------- Unit 4: p263
add(
    S4, 263, "numeric",
    "Which pleural fluid glucose tiers open page 263?",
    "Below 60 mg/dL in RA, empyema, malignancy and SLE, with SLE bracketed below 20% as printed; and below 30 mg/dL specifically in RA",
    [
        "Below 60 mg/dL in RA, empyema and malignancy only; and below 30 mg/dL in empyema",
        "Below 30 mg/dL in RA, empyema, malignancy and SLE; and below 60 mg/dL in RA",
        "Below 60 mg/dL in RA, empyema, malignancy and TB; and below 30 mg/dL specifically in RA",
    ],
    "Pleural fluid glucose lists '<60 mg/dL: RA, Empyema, malignancy, SLE (<20%)' across its two columns and then '<30 mg/dL: RA', leaving rheumatoid fluid the deepest glucose sink, matching its low pH on page 262.",
)

add(
    S4, 263, "fillup",
    "The line beneath the glucose tiers states that NT pro BNP in pleural fluid points to a ______ cause.",
    "cardiac",
    ["hepatic", "malignant", "tuberculous"],
    "The line reads 'NT pro BNP in PF: Cardiac cause', bookending the identical bracket after CCF at the head of the transudative column on page 261.",
)

add(
    S4, 263, "management",
    "Which four indications for an intercostal drain are numbered on page 263?",
    "'Calculated effusion' as printed, pleural fluid pH below 7.2, pleural fluid glucose below 60 mg/dL, and pus in the pleural space",
    [
        "Free-flowing effusion, pleural fluid pH below 7.2, pleural fluid glucose below 60 mg/dL, and pus in the pleural space",
        "'Calculated effusion' as printed, pleural fluid pH below 7.4, pleural fluid glucose below 30 mg/dL, and organisms on culture alone",
        "'Calculated effusion' as printed, pleural fluid pH below 7.2, pleural fluid glucose below 60 mg/dL, and a positive Light criterion",
    ],
    "Indications for ICD number '1. Calculated effusion. 2. PF pH <7.2. 3. PF Glucose <60 mg/dL. 4. Pus in pleural space.' The first item is preserved verbatim as printed; the film beside the list captions a loculated effusion, the concept the item evidently intends.",
)

add(
    S4, 263, "recall",
    "Which six causes of eosinophils in pleural fluid are numbered on page 263?",
    "Lung fluke, asbestosis, histoplasmosis, lung infarction, drugs causing pleural effusion, and hemo- or pneumothorax",
    [
        "Lung fluke, asbestosis, histoplasmosis, lung infarction, malignancy, and hemo- or pneumothorax",
        "Ascaris, asbestosis, histoplasmosis, lung infarction, drugs causing pleural effusion, and hemo- or pneumothorax",
        "Lung fluke, silicosis, histoplasmosis, lung infarction, drugs causing pleural effusion, and chylothorax",
    ],
    "The list runs lung fluke (the eosinophilic effusion of page 250), asbestosis (whose benign effusion carried a raised eosinophil count on page 228), histoplasmosis, lung infarction, 'Drugs causing PE' from page 261, and 'Hemo/pneumothorax'.",
)

add(
    S4, 263, "match",
    "Match each label on the page 263 chest film with its printed annotation — 1) The circled midline structure with a right-pointing arrow 2) The long arrow to the right basal opacity, the film lettered A … A) CXR showing loculated pleural effusion on the right B) Trachea central",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "The circled trachea is annotated 'Trachea central' — pointedly not deviated — while the lower arrow reads 'CXR: Loculated P.E on R', the contained collection that does not shift the mediastinum as the free left effusion of page 261 did.",
)

add(
    S4, 263, "numeric",
    "Which sensitivity ladder is printed for diagnosing tuberculous pleural effusion?",
    "Pleural fluid AFB stain 10–20%, AFB culture 25–50% and CBNAAT 45–50%, with pleural biopsy plus biopsy culture at 90%",
    [
        "Pleural fluid AFB stain 45–50%, AFB culture 25–50% and CBNAAT 10–20%, with pleural biopsy plus biopsy culture at 90%",
        "Pleural fluid AFB stain 10–20%, AFB culture 45–50% and CBNAAT 25–50%, with pleural biopsy plus biopsy culture at 90%",
        "Pleural fluid AFB stain 10–20%, AFB culture 25–50% and CBNAAT 45–50%, with pleural biopsy alone at 50%",
    ],
    "The sensitivity table climbs through fluid tests — AFB stain 10–20%, AFB culture 25–50%, CBNAAT 45–50% — to 'Pleural biopsy + biopsy culture' at 90%, printed in red as the decisive row.",
)

add(
    S4, 263, "recall",
    "Which causes head neoplastic exudative effusion at the foot of page 263?",
    "Most common cause mesothelioma as printed, and metastasis from carcinoma of the breast",
    [
        "Most common cause metastasis from carcinoma of the lung as printed, and mesothelioma",
        "Most common cause mesothelioma as printed, and metastasis from carcinoma of the ovary",
        "Lymphoma as the most common cause, and metastasis from carcinoma of the breast",
    ],
    "Cause arrows to 'm/c cause: mesothelioma' and 'metastasis from: CA breast', preserved as printed. Lymphoma enters only in the prognosis line as the exception.",
)

add(
    S4, 263, "scenario",
    "Cytology of a suspected malignant effusion is negative, as it will be in half of cases by this page. Which printed next investigation and overall prognosis apply?",
    "VAT, as printed, or CT-guided biopsy; prognosis poor except in lymphoma",
    [
        "Repeat cytology until positive; prognosis poor except in mesothelioma as printed",
        "Pleural fluid CBNAAT; prognosis poor except in lymphoma",
        "VAT, as printed, or CT-guided biopsy; prognosis good except in lymphoma",
    ],
    "Investigation arrows to 'Cytology: low sensitivity (50%)' and 'VAT or CT guided biopsy' — VAT preserved as printed for video-assisted thoracoscopy — and the chapter closes 'Prognosis: Poor (Except in Lymphoma)'. CBNAAT belongs to the tuberculous table above.",
)

add(
    S4, 263, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed indications or findings tied to draining or sampling fluid on page 263, one belongs to a different threshold on the same page:",
    "Pleural fluid glucose below 30 mg/dL as an indication for ICD",
    [
        "Pleural fluid pH below 7.2 as an indication for ICD",
        "Pus in the pleural space as an indication for ICD",
        "Pleural fluid glucose below 60 mg/dL as an indication for ICD",
    ],
    "The ICD list uses glucose below 60 mg/dL, not 30; the below-30 tier belongs to rheumatoid fluid in the glucose block at the top of the page. pH below 7.2 and pus in the pleural space are ICD items 2 and 4.",
)


GUIDES = {
    S1: (
        "Pleural Anatomy and Fluid Composition, Detection Thresholds, and Light's Criteria with the Diuretic Disadvantage",
        "The mesothelial-lined pleural cavity (p260) holds 10–20 ml of fluid at negative pressure from its lymphatics and vacuum, coupling lung to chest wall; parietal pleura from somatopleuric mesoderm is pain sensitive and visceral pleura from splanchnopleural mesoderm is pain insensitive ('Developes' as printed).\n"
        "Effusions need 50 mL for USG or a lateral film, 200 mL for a PA film and 300 mL clinically; normal fluid is 70% macrophages, 25% lymphocytes and 1–5% mesothelial cells, with blood-level glucose, protein 1–1.5 g/dL and LDH under half of plasma.\n"
        "Light's criteria separate exudate from transudate — protein ratio at least 0.5, LDH ratio at least 0.6, or pleural LDH above two-thirds of the serum upper limit, any one making an exudate — but misclassify a third of diuresed CCF effusions, where a higher serum–pleural albumin gradient instead indicates a transudate.",
    ),
    S2: (
        "Transudative and Exudative Causes, Drugs Causing Effusion, TB Effusion Presentation and General Examination Signs",
        "Transudates (p261) number CCF with NT pro BNP in fluid, cirrhosis, nephrotic syndrome, hypothyroidism, hypoalbuminemia, Budd-Chiari syndrome, chronic constrictive pericarditis, SVC obstruction as printed, peritoneal dialysis and urinothorax with low pH, high creatinine and ammoniacal odor; exudates number TB, pneumonia, malignancy, RA/SLE connective tissue disease and the left-sided pair acute pancreatitis and esophageal rupture, with pulmonary infarction and embolism causing both types and nitrofurantoin, dantrolene, methysergide and bromocriptine as drug causes.\n"
        "TB effusion strikes women of 20–30 years at first exposure, its pleuritic pain easing as fluid collects, and 25–30% develop pulmonary TB over 5–10 years.\n"
        "Examination shows contralateral tracheal deviation (the film: left effusion deviating the trachea right), confirmed on palpation with reduced fremitus and movement, stony dull percussion, and reduced breath sounds and vocal resonance.",
    ),
    S3: (
        "Parapneumonic Effusion and Empyema, Low-pH Causes, and Chylothorax versus Pseudochylothorax",
        "Uncomplicated parapneumonic effusion (p262) is a sterile inflammatory leak with normal glucose, pH 7.3–7.4 and high protein/LDH, while bacterial invasion with fibrin and septation makes it complicated — glucose below 60 (printed g/L), pH below 7.2, very high LDH above 1000 and protein, Gram stain positive.\n"
        "Empyema adds macroscopic pus, protein above 8 g/dL, LDH above 1000 IU/L and the CT split pleura sign against a pulmonary abscess; low fluid pH also marks rheumatoid arthritis and malignancy, the latter with poor prognosis.\n"
        "Milky fluid splits into chylothorax of lymphatic rupture from trauma or lymphoma, rich in triglyceride, and pseudochylothorax of pleural thickening in TB or RA, an exudate enriched with cholesterol crystals above 250 mg/dL.",
    ),
    S4: (
        "Pleural Fluid Glucose, ICD Indications, Eosinophils in Pleural Fluid, and Tuberculous and Neoplastic Effusion Diagnosis",
        "Fluid glucose (p263) falls below 60 mg/dL in RA, empyema, malignancy and SLE (under 20% as printed) and below 30 mg/dL in RA, while NT pro BNP in fluid means a cardiac cause.\n"
        "An intercostal drain is indicated for 'calculated effusion' as printed, pH below 7.2, glucose below 60 mg/dL or pus; fluid eosinophils suggest lung fluke, asbestosis, histoplasmosis, lung infarction, effusion-causing drugs or hemo/pneumothorax, and the loculated right effusion film keeps its trachea central.\n"
        "Tuberculous effusion is best proven by biopsy plus culture at 90% sensitivity over fluid CBNAAT 45–50%, culture 25–50% and stain 10–20%; neoplastic effusion is headed by mesothelioma as printed and breast metastasis, needs VAT (as printed) or CT-guided biopsy beyond 50%-sensitive cytology, and carries a poor prognosis except in lymphoma.",
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
