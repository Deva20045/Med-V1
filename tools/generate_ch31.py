#!/usr/bin/env python3
"""Generate Chapter 31: Clinical Anatomy of Lungs (Book p185–192).

Every question is anchored to a specific labelled diagram, table cell, printed
list or Note in uploads/02.pdf (PDF pages 68–75 = Book pages 185–192) in strict
book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 31
TITLE = "Clinical Anatomy of Lungs"
PAGES = "185-192"

S1 = "Gross Anatomy: Lobes, Oblique/Horizontal Fissures, Lower-Lobe Auscultation, Azygos Fissure 'Tadpole' & Phantom Tumor"
S2 = "Phantom Tumor Resolution Films, Hilar Structures & Relations, Causes of Hilar Enlargement & Weibel's 23 Generations"
S3 = "Bronchi Types, Right vs Left Bronchus Dimensions, Foreign-Body Predilection, Calibre/Area Change, Secondary Pulmonary Lobule & BPS Definition"
S4 = "Bronchopulmonary Segments of Right and Left Lung (10 Each) & Position-Dependent Aspiration Segments"
S5 = "Acinus Parts, Centriacinar (Smokers) vs Panacinar (α1-Antitrypsin) Emphysema & Basal/Goblet Cells of Conducting Airways"
S6 = "Club (Clara) Cells, CGRP, Kulchitzky Cells, Cartilage/Smooth Muscle/Goblet Table, Epithelial Zonation & Airway Mediators"
S7 = "Role of Cilia, Primary Ciliary Dyskinesia/Kartagener Triad, Nasal Nitric Oxide Gold Standard & Cystic Fibrosis (F508, Ivacaftor)"
S8 = "Airway Resistance: Poiseuille/Ohm Laws, Generation 5–7 Resistance Peak, Reynolds Number Flow Table"
S9 = "Alveolar Type I vs Type II Cells, Bleomycin Effect, Surfactant Function/Components/Synthesis & GM-CSF"

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
# UNIT 1 — Page 185
# ==============================================================================

add(
    S1, 185, "numeric",
    "Under 'Lobes :' on page 185, how many lobes are printed for each lung, and which lobes are named?",
    "Right = 3 lobes (upper RUL, middle RML, lower RLL); left = 2 lobes (upper LUL, lower LLL)",
    [
        "Right = 3 lobes (upper RUL, middle RML, lower RLL); left = 3 lobes (upper LUL, lingular, lower LLL)",
        "Right = 2 lobes (upper RUL, lower RLL); left = 2 lobes (upper LUL, lower LLL)",
        "Right = 4 lobes (upper, middle, lower, azygos); left = 2 lobes (upper LUL, lower LLL)",
    ],
    "Page 185 prints 'Lobes : Right (3 lobes) → upper lobe (RUL), middle lobe (RML), Lower lobe (RLL)' and 'Left (2 lobes) → upper lobe (LUL), Lower lobe (LLL)'. (Book p185)",
)

add(
    S1, 185, "recall",
    "The lobar photograph on page 185 labels two fissures. Which fissure is called the 'major (oblique)' fissure and which the 'minor (horizontal)' fissure, in terms of laterality?",
    "Oblique/major fissure is bilateral; horizontal/minor fissure is on the right lung",
    [
        "Oblique/major fissure is on the right lung only; horizontal/minor fissure is bilateral",
        "Oblique/major fissure is bilateral; horizontal/minor fissure is on the left lung",
        "Both fissures are bilateral, but the minor fissure is called the azygos fissure",
    ],
    "The lung photograph is annotated '(major fissure) oblique fissure' across both lungs and 'horizontal fissure (minor fissure)' on the right lung, matching the printed 'Types :' list on the same page. (Book p185)",
)

add(
    S1, 185, "recall",
    "Under 'Lower/Inferior lobe :' on page 185, why is this lobe not seen on a normal X-ray, what imaging is required, and which two auscultation areas are printed?",
    "Because of its posterior position; lateral X-ray/CT is required; auscultation at infrascapular and infraaxillary areas",
    [
        "Because of its anterior position; lateral X-ray/CT is required; auscultation at supraclavicular and infraclavicular areas",
        "Because of its posterior position; only a PA film is required; auscultation at infrascapular and infraaxillary areas",
        "Because of its posterior position; lateral X-ray/CT is required; auscultation at interscapular and apical areas",
    ],
    "Page 185 prints 'Lower/Inferior lobe : • Not visualised on normal x-ray due to posterior position. • Requires lateral xray / CT for visualisation. • Areas for auscultation : – Infrascapular. – Infraaxillary.' (Book p185)",
)

add(
    S1, 185, "recall",
    "Page 185 defines fissures as depressions on the lung surface extending where, and which fissure is described as a 'Tadpole appearance' with the azygos vein forming the head?",
    "Fissures are depressions extending to the hila; the azygos fissure gives the tadpole appearance",
    [
        "Fissures are depressions extending to the carina; the azygos fissure gives the tadpole appearance",
        "Fissures are depressions extending to the hila; the horizontal fissure gives the tadpole appearance",
        "Fissures are depressions extending to the hila; the oblique fissure gives the tadpole appearance",
    ],
    "Page 185 prints 'Fissures : Depressions on the lung surface extending to the hila.' and, under type 3, 'Azygos fissure • Tadpole appearance. • Azygos vein : Forms head of the tadpole.' (Book p185)",
)

add(
    S1, 185, "numeric",
    "What prevalence is printed for the azygos fissure on page 185?",
    "1–2% of population",
    [
        "10–20% of population",
        "0.1–0.2% of population",
        "5–10% of population",
    ],
    "Page 185 prints under the azygos fissure '• 1–2% of population.' The radiograph is captioned 'Azygos fissure'. (Book p185)",
)

add(
    S1, 185, "scenario",
    "An elderly man with heart failure and a low ejection fraction has a chest radiograph showing a rounded opacity in the region of the horizontal fissure. What does page 185 call this, what mechanism is printed, and what is the expected response to treatment?",
    "Phantom tumor/pseudotumor due to fluid collection in the horizontal fissures; it resolves with diuretics",
    [
        "Phantom tumor/pseudotumor due to fluid in the oblique fissure; it resolves with antibiotics",
        "Azygos lobe due to fluid in the horizontal fissure; it resolves with diuretics",
        "Phantom tumor/pseudotumor due to azygos vein enlargement; it resolves spontaneously",
    ],
    "Page 185 prints 'Note : Phantom tumor/Pseudotumor • D/t fluid collection in the horizontal fissures. • Etiology : Heart failure with ↓ ejection fraction (Congestive Heart Failure). • Resolves with administration of diuretics.' (Book p185)",
)

# ==============================================================================
# UNIT 2 — Page 186
# ==============================================================================

add(
    S2, 186, "match",
    "Three chest radiographs at the top of page 186 document the phantom tumor course. Match each film with its printed caption — 1) Left film 2) Middle film 3) Right film … A) 'Phantom tumor' B) 'After 2 weeks of therapy' C) 'After 4 weeks of therapy'",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The three radiographs on page 186 are captioned, left to right, 'Phantom tumor', 'After 2 weeks of therapy' and 'After 4 weeks of therapy'. (Book p186)",
)

add(
    S2, 186, "match",
    "Match each structure listed under 'Structures at the hila :' on page 186 with the printed annotation used for it — 1) Pulmonary artery 2) Pulmonary vein 3) Bronchus 4) Lymphatics … A) Printed with the abbreviation 'PA' B) Printed with the abbreviation 'PV' C) Printed third, with no abbreviation D) Printed fourth, with no abbreviation",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-B, 3-D, 4-C",
        "1-C, 2-D, 3-A, 4-B",
    ],
    "Page 186 prints 'Structures at the hila : • Pulmonary artery (PA). • Pulmonary vein (PV). • Bronchus. • Lymphatics.' in that order. (Book p186)",
)

add(
    S2, 186, "recall",
    "The two hilar diagrams on page 186 make a point of the pulmonary artery's relation to the bronchus on each side. Which relation is printed for the right and for the left hilum?",
    "Right hilum: PA anterior to the bronchus; left hilum: PA above the bronchus",
    [
        "Right hilum: PA above the bronchus; left hilum: PA anterior to the bronchus",
        "Right hilum: PA posterior to the bronchus; left hilum: PA below the bronchus",
        "Right hilum: PA anterior to the bronchus; left hilum: PA below the bronchus",
    ],
    "The two diagrams are captioned 'Right hilum — PA anterior to the bronchus' and 'Left hilum — PA above the bronchus'. (Book p186)",
)

add(
    S2, 186, "oddoneout",
    "Four causes of hilar enlargement are printed on page 186, with a brace marking which two are 'more common'. All of the following are on that printed list EXCEPT:",
    "Bronchial carcinoid tumour",
    [
        "Hilar lymphadenopathy (TB, sarcoidosis)",
        "PA dilatation",
        "Mass in the bronchus",
    ],
    "Page 186 lists exactly '1. Hilar lymphadenopathy (TB, sarcoidosis) 2. PA dilatation. 3. mediastinal mass. 4. mass in the bronchus.' with 'more common' bracing items 1 and 2; the radiograph is captioned 'Hilar lymphadenopathy' with right and left hilar points marked. (Book p186)",
)

add(
    S2, 186, "recall",
    "In the 'WEIBEL'S GENERATION OF AIRWAYS' diagram on page 186, which generation numbers bound the conducting zone, and what is the anatomical dead space said to be?",
    "Conducting zone = generations 0–16; anatomical dead space is 'Air in the conducting zone (150 ml)'",
    [
        "Conducting zone = generations 0–17; anatomical dead space is 'Air in the conducting zone (150 ml)'",
        "Conducting zone = generations 0–16; anatomical dead space is 'Air in the transitional zone (150 ml)'",
        "Conducting zone = generations 0–23; anatomical dead space is 'Air in the conducting zone (50 ml)'",
    ],
    "The shaded 'Conducting zone' column extends from Trachea (0) to Terminal bronchioles (16), and the bracket reads 'Anatomical dead space : Air in the conducting zone (150 ml)'. (Book p186)",
)

add(
    S2, 186, "recall",
    "Which airway generations are grouped into the 'Transitional and respiratory zones', and what is bracketed at generation 23?",
    "Respiratory bronchioles (17–19), alveolar ducts (20–22) and alveolar sacs (23); generation 23 is bracketed 'Site of gas exchange (acinus)'",
    [
        "Respiratory bronchioles (17–20), alveolar ducts (21–22) and alveolar sacs (23); generation 23 is bracketed 'Site of gas exchange (acinus)'",
        "Respiratory bronchioles (16–18), alveolar ducts (19–22) and alveolar sacs (23); generation 17 is bracketed 'Site of gas exchange (acinus)'",
        "Alveolar ducts (17–19) and alveolar sacs (20–23); generation 20 is bracketed 'Site of gas exchange (acinus)'",
    ],
    "The lower band of the diagram reads 'Respiratory bronchioles 17, 18, 19', 'Alveolar ducts 20, 21, 22' and 'Alveolar sacs 23', with 'Site of gas exchange (acinus)' bracketed from generation 17 downwards. (Book p186)",
)

# ==============================================================================
# UNIT 3 — Page 187
# ==============================================================================

add(
    S3, 187, "match",
    "Match the three bronchial types on page 187 with their printed alternative names — 1) Primary bronchi 2) Secondary bronchi 3) Tertiary bronchi … A) Lobar bronchi B) Segmental bronchi C) Principal/main bronchi",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-B, 3-C",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "Page 187 prints 'Types → Primary/Principal/main bronchi, → Secondary/Lobar bronchi, → Tertiary/Segmental bronchi'. (Book p187)",
)

add(
    S3, 187, "match",
    "Page 187 gives four measurements for the two main bronchi. Match each measurement with the bronchus printed against it — 1) Right bronchus width 2) Left bronchus width 3) Right bronchus length 4) Left bronchus length … A) 1.5 cm B) 1.3 cm C) 2 cm D) 5 cm",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-B, 3-D, 4-C",
        "1-C, 2-D, 3-A, 4-B",
    ],
    "The 'Right bronchus' box prints '• Wider (1.5cm) • Shorter • Steeper • 2cm (45° angle with carina)', while the 'Left bronchus' box prints '• Narrower (1.3 cm) • Longer • More horizontal • 5cm'. (Book p187)",
)

add(
    S3, 187, "recall",
    "Which three adjectives complete the right bronchus list on page 187, and which level is marked for the carina?",
    "Shorter, steeper, with a 45° angle with the carina; the carina is marked at T4/5",
    [
        "Shorter, more horizontal, with a 45° angle with the carina; the carina is marked at C6",
        "Longer, steeper, with a 45° angle with the carina; the carina is marked at T4/5",
        "Shorter, steeper, with a 60° angle with the carina; the carina is marked at T4/5",
    ],
    "The right bronchus box reads 'Wider (1.5cm), Shorter, Steeper, 2cm (45° angle with carina)'; the trachea is labelled C6 above and the carina is labelled T4/5. (Book p187)",
)

add(
    S3, 187, "recall",
    "What single clinical consequence of the right bronchus anatomy is printed on page 187, and which expression is used?",
    "Inhaled foreign body impaction: R > L bronchus",
    [
        "Inhaled foreign body impaction: L > R bronchus",
        "Aspiration pneumonia: L > R bronchus",
        "Inhaled foreign body impaction: equal in both bronchi",
    ],
    "Page 187 prints 'Inhaled foreign body impaction : R > L bronchus.' (Book p187)",
)

add(
    S3, 187, "numeric",
    "The 'Note :' on page 187 gives tracheal and alveolar diameters and cross-sectional areas. Which four values are printed?",
    "Diameter: trachea 25 mm → alveoli 0.25–0.3 mm; cross-sectional area: trachea 5 cm² → alveoli 7,00,000 cm²",
    [
        "Diameter: trachea 25 mm → alveoli 0.25–0.3 mm; cross-sectional area: trachea 5 cm² → alveoli 70,000 cm²",
        "Diameter: trachea 20 mm → alveoli 0.3–0.5 mm; cross-sectional area: trachea 5 cm² → alveoli 7,00,000 cm²",
        "Diameter: trachea 25 mm → alveoli 2.5–3 mm; cross-sectional area: trachea 5 cm² → alveoli 7,00,000 cm²",
    ],
    "Page 187 prints a table with 'Trachea 25 mm' and 'Alveoli 0.25 – 0.3 mm' under '↓ Diameter of airway', and '5 cm²' vs '7,00,000 cm²' under '↑ Cross-sectional area'. (Book p187)",
)

add(
    S3, 187, "recall",
    "Page 187 defines the secondary pulmonary lobule. Which three statements are printed about it?",
    "Functional unit of lung; 3–5 terminal bronchioles enclosed in connective tissue septa; airflow terminal bronchiole → respiratory bronchioles → alveolar ducts → alveoli",
    [
        "Anatomical unit of lung; 3–5 respiratory bronchioles enclosed in connective tissue septa; airflow terminal bronchiole → alveolar ducts → alveoli",
        "Functional unit of lung; 3–5 terminal bronchioles enclosed in connective tissue septa; airflow respiratory bronchiole → alveolar duct → alveolar sac",
        "Functional unit of lung; 10 terminal bronchioles enclosed in connective tissue septa; airflow terminal bronchiole → respiratory bronchioles → alveolar ducts → alveoli",
    ],
    "Page 187 prints 'SECONDARY PULMONARY LOBULE • Functional unit of lung. • 3–5 terminal bronchioles enclosed in connective tissue septa. • Airflow : Terminal bronchiole → Respiratory bronchioles → Alveolar ducts → Alveoli.' The diagram labels the 'Pulmonary vein (Intersegmental)' and 'Pulmonary artery (Intrasegmental)'. (Book p187)",
)

add(
    S3, 187, "recall",
    "How does page 187 define a bronchopulmonary segment (BPS), and what vessel is said to lie within it?",
    "Anatomical unit of lung supplied by a tertiary/segmental bronchus, containing the PA within it (intrasegmental artery)",
    [
        "Functional unit of lung supplied by a secondary/lobar bronchus, containing the PV within it (intersegmental vein)",
        "Anatomical unit of lung supplied by a tertiary/segmental bronchus, containing the PV within it (intersegmental vein)",
        "Anatomical unit of lung drained by a tertiary/segmental bronchus, containing the bronchial artery within it",
    ],
    "Page 187 prints 'BRONCHOPULMONARY SEGMENTS (BPS) • Anatomical unit of lung supplied by a tertiary /segmental bronchi. • Contains PA within it (Intrasegmental artery).' This is contrasted with the PV, labelled '(Intersegmental)' on the lobule diagram. (Book p187)",
)

# ==============================================================================
# UNIT 4 — Page 188 (segments + aspiration)
# ==============================================================================

add(
    S4, 188, "numeric",
    "The segment maps on page 188 are captioned for each lung. How many bronchopulmonary segments are shown for the right lung and for the left lung?",
    "10 segments in the right lung and 10 segments in the left lung",
    [
        "10 segments in the right lung and 8 segments in the left lung",
        "8 segments in the right lung and 10 segments in the left lung",
        "12 segments in the right lung and 10 segments in the left lung",
    ],
    "The two medial-view diagrams on page 188 are captioned 'BPS of Right Lung (10 segments)' and 'BPS of Left Lung (10 segments)', with segments numbered 1–10 on each. (Book p188)",
)

add(
    S4, 188, "recall",
    "On the right lung diagrams, which segments are numbered 1, 2 and 3 in the upper lobe, and which two segments form the middle lobe?",
    "Upper lobe: apical (1), posterior (2), anterior (3); middle lobe: lateral (4) and medial (5)",
    [
        "Upper lobe: apical (1), posterior (2), anterior (3); middle lobe: superior lingular (4) and inferior lingular (5)",
        "Upper lobe: apicoposterior (1, 2) and anterior (3); middle lobe: lateral (4) and medial (5)",
        "Upper lobe: apical (1), anterior (2), posterior (3); middle lobe: medial (4) and lateral (5)",
    ],
    "The right-lung lateral-view map lists 'Upper lobe — Apical (1), Posterior (2), Anterior (3)' and 'Middle lobe — Lateral (4), Medial (5)'. (Book p188)",
)

add(
    S4, 188, "recall",
    "On the left lung diagrams, how are the upper-lobe segments numbered?",
    "Apicoposterior is numbered 1, 2 and anterior is 3",
    [
        "Apical is 1, posterior is 2 and anterior is 3",
        "Apicoposterior is 1 and anterior is 2, 3",
        "Apical is 1 and apicoposterior is 2, 3",
    ],
    "The left-lung map reads 'Upper lobe (1, 2) Apicoposterior, (3) Anterior' and 'Middle lobe → (4) Superior lingular, (5) Inferior lingular'. (Book p188)",
)

add(
    S4, 188, "match",
    "Match the right-lung lower-lobe segment numbers 6–10 with their printed names — 1) 6 2) 7 3) 8 4) 9 5) 10 … A) Superior B) Posterior basal C) Medial basal D) Lateral basal E) Anterior basal",
    "1-A, 2-B, 3-C, 4-D, 5-E",
    [
        "1-A, 2-B, 3-D, 4-C, 5-E",
        "1-B, 2-A, 3-C, 4-D, 5-E",
        "1-A, 2-C, 3-B, 4-E, 5-D",
    ],
    "The right lung medial-view map numbers the lower lobe 'Superior (6)', 'Posterior basal (7)', 'Medial basal (8)', 'Lateral basal (9)', 'Anterior basal (10)'. (Book p188)",
)

add(
    S4, 188, "scenario",
    "A patient aspirates while lying supine. According to page 188, which segment is most likely involved, and which segment is involved when the patient aspirates while standing?",
    "Supine: posterior segment of right upper lobe > superior segment of right lower lobe; standing: basal segment of the left lower lobe, with R > L",
    [
        "Supine: superior segment of right lower lobe > posterior segment of right upper lobe; standing: basal segment of left lower lobe",
        "Supine: posterior segment of left upper lobe > superior segment of left lower lobe; standing: basal segment of right lower lobe",
        "Supine: posterior segment of right upper lobe; standing: apical segment of right upper lobe (R > L)",
    ],
    "Page 188 prints 'BPS involved in aspiration : Depending on position of patient : • Supine : Posterior segment of Rt upper lobe > Superior segment of Rt lower lobe. • Standing : Basal segment of LL (R > L).' (Book p188)",
)

# ==============================================================================
# UNIT 5 — Page 188 (acinus + conducting airway cells)
# ==============================================================================

add(
    S5, 188, "match",
    "Match each of the three acinar drawings on page 188 with the parenthetical printed beneath it — 1) Normal acinus 2) Centriacinar emphysema 3) Panacinar emphysema … A) (Smokers) B) (α-1 antitrypsin deficiency) C) No parenthetical printed",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-B, 3-C",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "Page 188 captions the three acinar drawings 'Normal acinus', 'Centriacinar emphysema (Smokers)' and 'Panacinar emphysema (α-1 antitrypsin deficiency)'. (Book p188)",
)

add(
    S5, 188, "recall",
    "Which three structures are labelled as the 'Parts :' of the acinus on page 188?",
    "Respiratory bronchiole, alveolar duct and alveolus",
    [
        "Terminal bronchiole, respiratory bronchiole and alveolar sac",
        "Respiratory bronchiole, alveolar sac and alveolus",
        "Terminal bronchiole, alveolar duct and alveolus",
    ],
    "Under 'ACINUS · Parts :' the drawing labels 'Respiratory bronchiole', 'Alveolar duct' and 'Alveolus'. The terminal bronchiole is not part of the acinus as drawn. (Book p188)",
)

add(
    S5, 188, "scenario",
    "A young non-smoker with α-1 antitrypsin deficiency develops emphysema. Which acinar pattern on page 188 corresponds to this, and which smoking-related pattern is drawn beside it?",
    "Panacinar emphysema for α-1 antitrypsin deficiency; centriacinar emphysema for smokers",
    [
        "Centriacinar emphysema for α-1 antitrypsin deficiency; panacinar emphysema for smokers",
        "Panacinar emphysema for α-1 antitrypsin deficiency; paraseptal emphysema for smokers",
        "Centriacinar emphysema for α-1 antitrypsin deficiency; irregular emphysema for smokers",
    ],
    "The right-hand drawing is labelled 'Panacinar emphysema (α-1 antitrypsin deficiency)' and the middle one 'Centriacinar emphysema (Smokers)'. (Book p188)",
)

add(
    S5, 188, "recall",
    "The first two 'CELLS IN CONDUCTING AIRWAYS' at the bottom of page 188 are basal cells and goblet cells. What function is printed for each?",
    "Basal cells: stem cells/progenitor cells during lung injury; goblet cells: secrete mucus",
    [
        "Basal cells: secrete mucus; goblet cells: stem cells/progenitor cells during lung injury",
        "Basal cells: detoxify xenobiotics; goblet cells: secrete mucus",
        "Basal cells: stem cells/progenitor cells during lung injury; goblet cells: secrete surfactant",
    ],
    "Page 188 prints '• Basal cells : Stem cells/ progenitor cells during lung injury. • Goblet cells : Secrete mucus.' (Book p188)",
)

add(
    S5, 188, "truefalse",
    "Which statement about the acinus and conducting airways as presented on page 188 is accurate?",
    "True — The acinus is the site of gas exchange and its parts begin with the respiratory bronchiole, whereas the conducting airways begin with cells such as basal and goblet cells",
    [
        "True — The acinus begins with the terminal bronchiole and is therefore part of the conducting zone",
        "False — Panacinar emphysema is the pattern printed for smokers",
        "False — Basal cells are described as mucus-secreting cells on page 188",
    ],
    "Page 188 shows the acinus arising from the respiratory bronchiole with 'Normal acinus / Centriacinar emphysema (Smokers) / Panacinar emphysema (α-1 antitrypsin deficiency)', while the only two cell functions printed are basal (stem/progenitor) and goblet (mucus). (Book p188)",
)

# ==============================================================================
# UNIT 6 — Page 189
# ==============================================================================

add(
    S6, 189, "recall",
    "Where are club (Clara) cells located, and what two functions are printed on page 189?",
    "Non-ciliated cuboidal epithelial cells in terminal bronchioles; detoxification of xenobiotics and progenitor for bronchiolar cells",
    [
        "Non-ciliated columnar cells in respiratory bronchioles; detoxification of xenobiotics and surfactant production",
        "Ciliated cuboidal cells in terminal bronchioles; mucus secretion and progenitor for bronchiolar cells",
        "Non-ciliated cuboidal epithelial cells in bronchi; detoxification of xenobiotics and progenitor for bronchiolar cells",
    ],
    "Page 189 prints '• Club/clara cells : – Non-ciliated cuboidal epithelial cells in terminal bronchioles. – Function → Detoxification of xenobiotics → Progenitor for bronchiolar cells'. (Book p189)",
)

add(
    S6, 189, "fillup",
    "In the 'Note :' beside the club cells, page 189 expands CGRP as 'Calcitonin gene-Related Peptide' and describes it as the 'major neurotransmitter in ______.'",
    "Migraine",
    [
        "Asthma",
        "Pulmonary hypertension",
        "Cough",
    ],
    "Page 189 prints 'Note : CGRP : • Calcitonin gene-Related Peptide. • major neurotransmitter in migraine.' (Book p189)",
)

add(
    S6, 189, "recall",
    "What does page 189 print about Kulchitzky cells?",
    "Dense core vesicles with serotonin/calcitonin/CGRP",
    [
        "Dense core vesicles with histamine/heparin/proteases",
        "Lamellar bodies with surfactant proteins A–D",
        "Apical granules with vasoactive intestinal peptide only",
    ],
    "Page 189 prints '• Kulchitzky cells : Dense core vesicles with serotonin/calcitonin/CGRP.' The bronchiole column later adds 'Few neuroendocrine cells, Kulchitzky cells → Cluster : Neuroepithelial bodies'. (Book p189)",
)

add(
    S6, 189, "match",
    "Match the three rows of the structural table on page 189 with the pattern of +/– printed across trachea, bronchi and bronchiole — 1) Cartilage 2) Smooth muscles 3) Mucus producing cells (goblet cells) … A) + / + / – B) – / + / + (max in terminal bronchiole) C) – / + / –",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The table on page 189 reads: Cartilage '+ / + / –'; Smooth muscles '– / + / + (max in terminal bronchiole)'; mucus producing cells (Goblet cells) '– / + / –'. (Book p189)",
)

add(
    S6, 189, "recall",
    "Page 189 describes the bronchus epithelium in three parts. Which epithelial type is printed for the upper, middle and lower parts?",
    "Upper: pseudostratified ciliated columnar; middle: ciliated simple cuboidal; lower: simple cuboidal",
    [
        "Upper: pseudostratified ciliated columnar; middle: simple squamous; lower: simple cuboidal",
        "Upper: ciliated simple cuboidal; middle: pseudostratified ciliated columnar; lower: simple cuboidal",
        "Upper: pseudostratified ciliated columnar; middle: ciliated simple cuboidal; lower: stratified squamous",
    ],
    "Page 189 prints 'Bronchus : epithelium → Upper part : Pseudostratified ciliated columnar epithelium → middle part : Ciliated simple cuboidal epithelium → Lower part : Simple cuboidal epithelium'. (Book p189)",
)

add(
    S6, 189, "match",
    "Match the four features listed under 'Bronchiole :' on page 189 with the printed text — 1) Lining 2) Mucus glands 3) Goblet cells 4) Neuroendocrine cells … A) No mucus glands B) Simple cuboidal epithelium C) Occasional goblet cells (+) D) Few, clustered as neuroepithelial bodies",
    "1-B, 2-A, 3-C, 4-D",
    [
        "1-A, 2-B, 3-C, 4-D",
        "1-B, 2-A, 3-D, 4-C",
        "1-C, 2-A, 3-B, 4-D",
    ],
    "Page 189 prints under 'Bronchiole :' '• Lining : Simple cuboidal epithelium. • No mucus glands. • Occasional goblet cells (+). • Few neuroendocrine cells, Kulchitzky cells → Cluster : Neuroepithelial bodies • Clara cells (+).' (Book p189)",
)

add(
    S6, 189, "match",
    "Match each mediator in 'SUBSTANCES ACTING ON CONDUCTING AIRWAYS' on page 189 with the superlative printed for it — 1) Leukotriene 2) Vasoactive intestinal peptide 3) Cholinergics 4) Anticholinergics … A) Most potent dilator, a NANC peptide B) Most potent constrictor of bronchial smooth muscles C) Broncho-constrictor, tested by methacholine challenge D) Bronchodilators used in asthma (ipratropium, tiotropium)",
    "1-B, 2-A, 3-C, 4-D",
    [
        "1-A, 2-B, 3-C, 4-D",
        "1-B, 2-C, 3-A, 4-D",
        "1-D, 2-A, 3-C, 4-B",
    ],
    "Page 189 prints 'Leukotriene : most potent constrictor of bronchial smooth muscles.', 'vasoactive Intestinal Peptide (VIP) : • most potent dilator. • Non-adrenergic non-cholinergic (NANC) peptide.', 'Cholinergics : • Broncho-constrictor. • methacholine challenge test : To assess airway hyperresponsiveness.' and 'Anticholinergics : • Bronchodilators. • used in asthma. Eg : Ipratropium, tiotropium.' (Book p189)",
)

# ==============================================================================
# UNIT 7 — Page 190
# ==============================================================================

add(
    S7, 190, "recall",
    "Under 'ROLE OF CILIA' on page 190, up to which level are cilia present, where are they absent, and in which direction does the mucociliary escalator beat?",
    "Present up to the terminal bronchiole, absent in the respiratory zone; beats towards the nasopharynx",
    [
        "Present up to the respiratory bronchiole, absent in the alveolar ducts; beats towards the nasopharynx",
        "Present up to the terminal bronchiole, absent in the respiratory zone; beats towards the alveoli",
        "Present up to the bronchiole, absent in the bronchi; beats towards the nasopharynx",
    ],
    "Page 190 prints '• Present upto terminal bronchiole (Absent in respiratory zone). • mucociliary escalator mechanism : Beats towards nasopharynx.' (Book p190)",
)

add(
    S7, 190, "recall",
    "Which four features of immotile cilia syndrome / primary ciliary dyskinesia are printed on page 190?",
    "Autosomal recessive; defective dynein arm; median age of presentation 5 yrs; recurrent sinusitis and otitis media (plus neonatal respiratory distress)",
    [
        "Autosomal dominant; defective radial spoke; median age of presentation 15 yrs; recurrent sinusitis and otitis media",
        "Autosomal recessive; defective dynein arm; median age of presentation 5 yrs; recurrent pneumonia and bronchiectasis only",
        "X-linked; defective dynein arm; median age of presentation 5 yrs; recurrent sinusitis and otitis media",
    ],
    "Page 190 prints under 'Immotile Cilia syndrome/Primary Ciliary Dyskinesia :' '• Autosomal recessive. • Defective dynein arm. • median age of presentation : 5 yrs. • C/F : a. Recurrent episodes of Sinusitis, Otitis media. b. Neonatal respiratory distress. c. Kartagener's syndrome : Triad + male infertility'. (Book p190)",
)

add(
    S7, 190, "recall",
    "Page 190 explains why Kartagener's syndrome includes situs inversus. What mechanism is printed?",
    "Cilia are required for rotation of body organs, so defective cilia result in situs inversus",
    [
        "Cilia are required for left-right asymmetrical gene expression, so defective cilia result in situs inversus",
        "Cilia move the developing heart to the left, so defective cilia result in dextrocardia only",
        "Cilia are required for rotation of the gut, so defective cilia result in malrotation",
    ],
    "Under Kartagener's syndrome the book prints '– Cilia required for rotation of body organs → Results in situs inversus.' (Book p190)",
)

add(
    S7, 190, "match",
    "The Kartagener triad is drawn as a triangle on page 190. Match each triad component with the organ system it belongs to — 1) Situs inversus 2) Sinusitis 3) Bronchiectasis … A) Lower respiratory tract B) Upper respiratory tract C) Organ laterality",
    "1-C, 2-B, 3-A",
    [
        "1-A, 2-B, 3-C",
        "1-C, 2-A, 3-B",
        "1-B, 2-C, 3-A",
    ],
    "Page 190 draws a triangle with 'Situs inversus' at the apex, 'Sinusitis' at bottom left and 'Bronchiectasis' at bottom right — the classic triad completed by the printed line 'Kartagener's syndrome : Triad + male infertility'. (Book p190)",
)

add(
    S7, 190, "recall",
    "What investigation is printed as the gold standard for primary ciliary dyskinesia on page 190, and what value is always found?",
    "Nasal nitric oxide levels, which are always low",
    [
        "Saccharin clearance time, which is always prolonged",
        "Nasal nitric oxide levels, which are always high",
        "Bronchial biopsy electron microscopy, which always shows a 9+0 pattern",
    ],
    "Page 190 prints '• Gold standard investigation : Nasal nitric oxide levels (Always low).' (Book p190)",
)

add(
    S7, 190, "recall",
    "For cystic fibrosis, page 190 prints an inheritance, a gene/mutation and a chromosome, and an ion defect. Which set is printed?",
    "Autosomal recessive; CFTR gene mutation (F508 mutation) on chromosome 7q → Cl⁻ ion defect",
    [
        "Autosomal recessive; CFTR gene mutation (F508 mutation) on chromosome 7p → Na⁺ ion defect",
        "Autosomal dominant; CFTR gene mutation (F508 mutation) on chromosome 7q → Cl⁻ ion defect",
        "Autosomal recessive; CFTR gene mutation (G551D mutation) on chromosome 7q → Cl⁻ ion defect",
    ],
    "Page 190 prints '• Autosomal recessive. • Defect : CFTR gene mutation (F508 mutation) on chromosome 7q → Cl⁻ ion defect.' (Book p190)",
)

add(
    S7, 190, "oddoneout",
    "Page 190 lists 'Affected sites :' in cystic fibrosis and contrasts the cilia with those in primary ciliary dyskinesia. All of the following are printed EXCEPT:",
    "Skin (sweat glands)",
    [
        "Bronchi",
        "Biliary tract",
        "Reproductive system",
    ],
    "The affected sites printed are '– Bronchi. – Biliary tract. – Intestine. – Reproductive system.' and the C/F line explicitly reads 'b. Normal cilia' — sweat glands are not in this list. (Book p190)",
)

add(
    S7, 190, "fillup",
    "Page 190 gives the cystic fibrosis drug as 'Rx : ______ (Cl⁻ channel opener).'",
    "Ivacaftor",
    [
        "Lumacaftor",
        "Dornase alfa",
        "Hypertonic saline",
    ],
    "Page 190 prints '• Rx : Ivacaftor (Cl⁻ channel opener)'. (Book p190)",
)

# ==============================================================================
# UNIT 8 — Page 191
# ==============================================================================

add(
    S8, 191, "match",
    "Match the four changes printed under 'From trachea to alveoli :' on page 191 with their direction — 1) Airway diameter 2) Total cross sectional area 3) Velocity of airflow 4) Turbulence … A) ↑ B) ↓ C) ↑ (same arrow as total cross-sectional area) D) ↓ (same arrow as velocity)",
    "1-B, 2-A, 3-D, 4-C",
    [
        "1-A, 2-B, 3-C, 4-D",
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-B, 3-D, 4-C",
    ],
    "Page 191 prints 'From trachea to alveoli : • Airway diameter ↓ • Total cross sectional area ↑ • velocity of airflow ↓ • Turbulence ↓'. (Book p191)",
)

add(
    S8, 191, "recall",
    "Which two laws are printed as 'Determinants of airway resistance' on page 191, and what does each express?",
    "Ohm's law Q = ΔP/R and Poiseuille's law R = 8ηL/πr⁴",
    [
        "Ohm's law Q = ΔP/R and Fick's law R = 8ηL/πr²",
        "Poiseuille's law Q = ΔP/R and Ohm's law R = 8ηL/πr⁴",
        "Boyle's law Q = ΔP/R and Poiseuille's law R = 8ηL/πr⁴",
    ],
    "Page 191 prints 'Ohm's law : Q = ΔP/R' and 'Poiseuille's law : R = 8ηL/πr⁴', then 'Flow ∝ 1/R' and 'R ∝ 1/r⁴', with the legend R = Resistance, Q = Flow, r = Radius, η = viscosity, L = Length. (Book p191)",
)

add(
    S8, 191, "recall",
    "Page 191 draws a conclusion from the radius term about flow and gives tracheal and alveolar examples. Which statement and examples are printed?",
    "Max radius → least resistance → max flow; trachea (max radius) shows highest velocity/turbulence, alveoli (min radius) show laminar flow",
    [
        "Max radius → greatest resistance → max flow; trachea shows laminar flow, alveoli show turbulence",
        "Min radius → least resistance → max flow; trachea shows highest velocity, alveoli show laminar flow",
        "Max radius → least resistance → max flow; both trachea and alveoli show laminar flow",
    ],
    "Page 191 prints 'max radius → least resistance → max flow. Eg : Trachea : max radius → Highest velocity (Turbulence) of flow. Alveoli : min. radius → Laminar flow.' (Book p191)",
)

add(
    S8, 191, "numeric",
    "What is the printed 'Area of max resistance', and what explanation is given underneath it?",
    "Generation 5, 6, 7 (bronchi > terminal bronchioles), because of the parallel arrangement of small airways giving a maximum cross-sectional area and low resistance to airflow",
    [
        "Generation 1, 2, 3 (trachea > main bronchi), because of the parallel arrangement of large airways",
        "Generation 5, 6, 7 (bronchi > terminal bronchioles), because of the series arrangement of small airways",
        "Generation 16, 17, 18 (terminal and respiratory bronchioles), because of the parallel arrangement of small airways",
    ],
    "Page 191 prints 'Area of max resistance : • Generation 5, 6, 7 (Bronchi > terminal bronchioles) • Cause : D/t parallel arrangement of small airways → maximum cross-sectional area → Low resistance to airflow', with the resistance peak marked 'Gen 5, 6, 7' on the graph. (Book p191)",
)

add(
    S8, 191, "match",
    "Match each Reynolds' number band on page 191 with the printed type of flow and area — 1) >4000 2) 4000–2000 3) <2000 … A) Turbulent — trachea, bronchi B) Transitional — respiratory bronchioles C) Laminar — alveolar duct, alveoli",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The table at the foot of page 191 reads '>4000 Turbulent flow Trachea, Bronchi'; '4000–2000 Transitional flow Respiratory bronchioles'; '<2000 Laminar flow Alveolar duct, alveoli'. (Book p191)",
)

add(
    S8, 191, "truefalse",
    "Which statement about Reynolds' number and airway resistance as printed on page 191 is accurate?",
    "True — Reynolds' number is printed as proportional to velocity (Re ∝ v), and resistance is printed as inversely proportional to the fourth power of the radius",
    [
        "True — Reynolds' number is printed as proportional to viscosity only, and resistance is proportional to the square of the radius",
        "False — Reynolds' number above 4000 is printed as laminar flow in the alveolar ducts",
        "False — Resistance is printed as directly proportional to the fourth power of the radius",
    ],
    "Page 191 prints 'Re = 2rvd/η' with 'Re ∝ v', and under Poiseuille's law 'R ∝ 1/r⁴'; the table assigns Re >4000 to turbulent flow in the trachea and bronchi. (Book p191)",
)

# ==============================================================================
# UNIT 9 — Page 192
# ==============================================================================

add(
    S9, 192, "match",
    "Match each alveolar cell type on page 192 with its printed percentage and morphology — 1) Type I pneumocyte 2) Type II pneumocyte 3) Bleomycin effect on type I … A) 5%, cuboidal (rounded) B) 95%, non-dividing flat squamous cells C) Injury",
    "1-B, 2-A, 3-C",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B",
    ],
    "The table on page 192 reads 'Percentage of cells 95% | 5%' and 'Type of cell Non-dividing flat squamous cells | Cuboidal (Rounded)'. (Book p192)",
)

add(
    S9, 192, "recall",
    "In the same table, what is printed for 'Features' and for the 'Effect of bleomycin' on type I vs type II pneumocytes?",
    "Type I: prone to oxidative damage, injured by bleomycin; Type II: repair post-injury and surfactant production, hyperplastic with bleomycin",
    [
        "Type I: repair post-injury and surfactant production, hyperplastic with bleomycin; Type II: prone to oxidative damage, injured by bleomycin",
        "Type I: prone to oxidative damage, hyperplastic with bleomycin; Type II: repair post-injury, injured by bleomycin",
        "Type I: prone to oxidative damage, injured by bleomycin; Type II: surfactant production only, no response to bleomycin",
    ],
    "The table prints Features 'Prone to oxidative damage' vs '• Repair post-injury • Surfactant production', and 'Effect of bleomycin' → 'Injury' vs 'Hyperplasia'. (Book p192)",
)

add(
    S9, 192, "match",
    "Match each marker with the pneumocyte type on page 192 — 1) Aquaporin-5 2) Caveolin-1 3) Carboxypeptidase m 4) Surfactant proteins A, B, C, D … A) Type I B) Type I C) Type I D) Type II",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-D, 2-B, 3-C, 4-A",
        "1-A, 2-D, 3-C, 4-B",
        "1-C, 2-B, 3-A, 4-D",
    ],
    "Under 'markers' the Type I column lists 'Aquaporin – 5', 'Caveolin – 1', 'Carboxypeptidase m' while the Type II column lists 'Surfactant protiens A, B, C, D'. (Book p192)",
)

add(
    S9, 192, "recall",
    "Page 192's Note lists three lung-specific facts. Which three are printed?",
    "Substance P is a bronchoconstrictor; DPPC expands to dipalmitoyl phosphatidylcholine; maximally bronchoconstricted at 6 am and bronchodilated at 6 pm",
    [
        "Substance P is a bronchodilator; DPPC expands to dipalmitoyl phosphatidylcholine; bronchoconstricted at 6 pm and bronchodilated at 6 am",
        "Substance P is a bronchoconstrictor; DPPC expands to dipalmitoyl phosphatidylserine; bronchoconstricted at 6 am and bronchodilated at 6 pm",
        "Substance P is a bronchoconstrictor; DPPC expands to dipalmitoyl phosphatidylcholine; maximally bronchoconstricted at 10 am and bronchodilated at 10 pm",
    ],
    "Page 192 prints 'Note : • Substance P : Bronchoconstrictor. • DPPC : Dipalmitoyl Phosphatidylcholine. • Time of max → Bronchoconstriction : 6 am → Bronchodilatation : 6 pm'. (Book p192)",
)

add(
    S9, 192, "scenario",
    "A premature neonate develops hyaline membrane disease. Which agent is printed for its use on page 192, and which other disease name is given for the same condition?",
    "Beractant — used in hyaline membrane disease (HMD)/fetal respiratory distress syndrome",
    [
        "Ivacaftor — used in hyaline membrane disease (HMD)/fetal respiratory distress syndrome",
        "Beractant — used in acute respiratory distress syndrome (ARDS)/adult respiratory distress syndrome",
        "Surfactant protein A — used in hyaline membrane disease (HMD)/bronchopulmonary dysplasia",
    ],
    "Page 192 prints '• Beractant : used in Hyaline membrane disease (HMD)/Fetal Respiratory Distress syndrome.' (Book p192)",
)

add(
    S9, 192, "management",
    "A woman in preterm labour is managed for anticipated fetal hyaline membrane disease, and the team also reviews which drugs raise or lower surfactant. According to page 192, which plan matches the printed text?",
    "Give steroids (printed as used for treating HMD) and note thyroid hormone also raises surfactant production; insulin lowers it; beractant is the exogenous surfactant used in HMD/fetal respiratory distress syndrome",
    [
        "Give insulin, since it raises surfactant production, and avoid steroids because they reduce surfactant in HMD",
        "Give beractant only after birth, since no antenatal drug is printed as raising surfactant production, and note that thyroid hormone lowers surfactant",
        "Give thyroid hormone to lower surfactant production, and give GM-CSF antibodies to clear excess surfactant in HMD",
    ],
    "Page 192 prints under surfactant synthesis 'Substances that → ↑ Surfactant production → Steroids (used for treating HMD). → Thyroid hormone.' and '→ ↓ Surfactant production : insulin', and in the Note 'Beractant : used in Hyaline membrane disease (HMD)/Fetal Respiratory Distress syndrome.' GM-CSF clears excess surfactant, and its antibodies cause pulmonary alveolar proteinosis — not HMD. (Book p192)",
)

add(
    S9, 192, "recall",
    "Page 192 traces the function of surfactant as a three-step chain. Which sequence is printed?",
    "Reducing surface tension → prevents fluid accumulation (pulmonary edema) → ↑ compliance",
    [
        "Reducing surface tension → ↑ fluid accumulation (pulmonary edema) → ↓ compliance",
        "Increasing surface tension → prevents alveolar collapse → ↑ compliance",
        "Reducing surface tension → prevents fluid accumulation (pulmonary edema) → ↓ compliance",
    ],
    "Under 'SURFACTANT · Function :' the book prints 'Reducing surface tension → Prevents fluid accumulation (Pulmonary edema) → ↑ compliance'. (Book p192)",
)

add(
    S9, 192, "match",
    "Match the surfactant statements on page 192 with the printed text — 1) Lamellar bodies 2) Substances that ↑ surfactant production 3) Substance that ↓ surfactant production 4) GM-CSF … A) Steroids (used for treating HMD) and thyroid hormone B) Insulin C) Storage bodies in type 2 pneumocytes that produce surfactants D) Clears excess surfactant",
    "1-C, 2-A, 3-B, 4-D",
    [
        "1-A, 2-C, 3-B, 4-D",
        "1-C, 2-B, 3-A, 4-D",
        "1-D, 2-A, 3-B, 4-C",
    ],
    "Page 192 prints '• Lamellar bodies : – Storage bodies in type 2 pneumocytes. – Produces surfactants'; 'Substances that → ↑ Surfactant production → Steroids (used for treating HMD). → Thyroid hormone.'; '→ ↓ Surfactant production : insulin'; and 'GM-CSF : • Clears excess surfactant. • GM-CSF antibodies : In Pulmonary alveolar proteinosis.' (Book p192)",
)

add(
    S9, 192, "recall",
    "Which two components and which two proteins of surfactant are printed on page 192?",
    "Lipoprotein (major component, with lecithin/DPPC > sphingomyelin) and surfactant proteins A, B, C, D, of which A and D are involved in innate immunity",
    [
        "Glycoprotein (major component, with sphingomyelin > lecithin) and surfactant proteins A, B, C, D, of which B and C are involved in innate immunity",
        "Lipoprotein (major component, with lecithin/DPPC > sphingomyelin) and surfactant proteins A and D only, both involved in innate immunity",
        "Lipoprotein (major component, with lecithin/DPPC > sphingomyelin) and surfactant proteins A, B, C, D, of which B and C are involved in innate immunity",
    ],
    "Page 192 prints 'Components : 1. Lipoprotein : • major component. • Lecithin (DPPC) > Sphingomyelin. 2. Surfactant proteins : • A, B, C, D. • A, D : involved in innate immunity.' (Book p192)",
)

GUIDES = {
    S1: (
        "Gross Anatomy: Lobes, Oblique/Horizontal Fissures, Lower-Lobe Auscultation, Azygos Fissure 'Tadpole' & Phantom Tumor",
        "Lobes (p185): right has 3 (RUL, RML, RLL), left has 2 (LUL, LLL); the oblique/major fissure is bilateral and the horizontal/minor fissure is right-sided. The lower lobe is not seen on a normal film because of its posterior position, needs a lateral film or CT, and is auscultated at the infrascapular and infraaxillary areas.\n"
        "Fissures are depressions on the lung surface reaching the hila; type 3 is the azygos fissure, giving a tadpole appearance whose head is the azygos vein, present in 1–2% of people.\n"
        "Phantom tumor/pseudotumor: fluid in the horizontal fissure, from heart failure with reduced ejection fraction, resolving with diuretics.",
    ),
    S2: (
        "Phantom Tumor Resolution Films, Hilar Structures & Relations, Causes of Hilar Enlargement & Weibel's 23 Generations",
        "Radiograph series (p186): 'Phantom tumor' → 'After 2 weeks of therapy' → 'After 4 weeks of therapy'. Hilar structures: pulmonary artery (PA), pulmonary vein (PV), bronchus, lymphatics; the PA lies anterior to the bronchus on the right and above the bronchus on the left.\n"
        "Hilar enlargement: hilar lymphadenopathy (TB, sarcoidosis) and PA dilatation are bracketed 'more common'; a mediastinal mass and a mass in the bronchus complete the list.\n"
        "Weibel generations total 23: conducting zone 0–16 (trachea 0 to terminal bronchioles 16) equals the anatomical dead space, 'air in the conducting zone (150 ml)'; transitional and respiratory zones 17–23 run from respiratory bronchioles through alveolar ducts (20–22) to alveolar sacs (23), bracketed as the site of gas exchange (acinus).",
    ),
    S3: (
        "Bronchi Types, Right vs Left Bronchus Dimensions, Foreign-Body Predilection, Calibre/Area Change, Secondary Pulmonary Lobule & BPS Definition",
        "Bronchi (p187) are primary/principal/main, secondary/lobar and tertiary/segmental. Right bronchus: wider (1.5 cm), shorter, steeper, 2 cm, 45° to the carina (carina at T4/5); left: narrower (1.3 cm), longer, more horizontal, 5 cm. Inhaled foreign bodies lodge R > L.\n"
        "From trachea to alveoli the diameter falls from 25 mm to 0.25–0.3 mm while the cross-sectional area rises from 5 cm² to 7,00,000 cm².\n"
        "The secondary pulmonary lobule is the functional unit — 3–5 terminal bronchioles within connective tissue septa — with airflow through respiratory bronchioles and alveolar ducts to alveoli; the bronchopulmonary segment is the anatomical unit supplied by a tertiary/segmental bronchus and contains the intra-segmental pulmonary artery.",
    ),
    S4: (
        "Bronchopulmonary Segments of Right and Left Lung (10 Each) & Position-Dependent Aspiration Segments",
        "Segment maps (p188): both lungs have 10 segments. Right upper lobe = apical (1), posterior (2), anterior (3); middle lobe = lateral (4), medial (5); left upper lobe = apicoposterior (1, 2) and anterior (3), with the lingula as superior (4) and inferior (5) lingular. Right lower lobe = superior (6), posterior basal (7), medial basal (8), lateral basal (9), anterior basal (10).\n"
        "Aspiration depends on posture: supine the posterior segment of the right upper lobe exceeds the superior segment of the right lower lobe; standing, the basal segment of the left lower lobe is involved, with R > L.",
    ),
    S5: (
        "Acinus Parts, Centriacinar (Smokers) vs Panacinar (α1-Antitrypsin) Emphysema & Basal/Goblet Cells of Conducting Airways",
        "Acinus parts (p188): respiratory bronchiole, alveolar duct and alveolus. Clinical significance: normal acinus, centriacinar emphysema (smokers) and panacinar emphysema (α-1 antitrypsin deficiency).\n"
        "Cells in conducting airways begin with basal cells (stem/progenitor cells during lung injury) and goblet cells (secrete mucus).",
    ),
    S6: (
        "Club (Clara) Cells, CGRP, Kulchitzky Cells, Cartilage/Smooth Muscle/Goblet Table, Epithelial Zonation & Airway Mediators",
        "Club/Clara cells (p189) are non-ciliated cuboidal epithelial cells of terminal bronchioles that detoxify xenobiotics and act as progenitors for bronchiolar cells. CGRP = calcitonin gene-related peptide, a major neurotransmitter in migraine. Kulchitzky cells hold dense-core vesicles with serotonin, calcitonin and CGRP.\n"
        "Structural table: cartilage + / + / –; smooth muscle – / + / + (maximal in terminal bronchiole); goblet cells – / + / – across trachea, bronchi and bronchioles. Trachea has hyaline cartilage and a glandular plus pseudostratified ciliated columnar epithelial layer; bronchus epithelium is pseudostratified ciliated columnar above, ciliated simple cuboidal in the middle and simple cuboidal below; bronchiole is simple cuboidal with no mucus glands, occasional goblet cells, neuroendocrine cells clustered as neuroepithelial bodies, and Clara cells.\n"
        "Mediators: leukotriene is the most potent constrictor; VIP the most potent dilator, a NANC peptide; cholinergics constrict with the methacholine challenge used to assess hyperresponsiveness; anticholinergics (ipratropium, tiotropium) dilate and are used in asthma.",
    ),
    S7: (
        "Role of Cilia, Primary Ciliary Dyskinesia/Kartagener Triad, Nasal Nitric Oxide Gold Standard & Cystic Fibrosis (F508, Ivacaftor)",
        "Cilia (p190) are present up to the terminal bronchiole and absent in the respiratory zone; the mucociliary escalator beats towards the nasopharynx. Immotile cilia syndrome/primary ciliary dyskinesia is autosomal recessive with a defective dynein arm, median presentation at 5 years, recurrent sinusitis and otitis media, and neonatal respiratory distress.\n"
        "Kartagener's syndrome is the triad plus male infertility; cilia are needed for rotation of body organs, so their failure produces situs inversus — the triad triangle of situs inversus, sinusitis and bronchiectasis. Gold-standard investigation is nasal nitric oxide, which is always low.\n"
        "Cystic fibrosis is autosomal recessive with CFTR (F508) mutation on chromosome 7q and a chloride defect: thick secretions with normal cilia affecting bronchi, biliary tract, intestine and reproductive system; ivacaftor is a chloride channel opener.",
    ),
    S8: (
        "Airway Resistance: Poiseuille/Ohm Laws, Generation 5–7 Resistance Peak, Reynolds Number Flow Table",
        "From trachea to alveoli (p191) diameter, velocity and turbulence fall while total cross-sectional area rises. Ohm's law Q = ΔP/R and Poiseuille's law R = 8ηL/πr⁴, so flow ∝ 1/R and R ∝ 1/r⁴; maximal radius gives least resistance and maximal flow — hence turbulence in the trachea and laminar flow in alveoli.\n"
        "Maximum resistance is at generations 5, 6 and 7 (bronchi > terminal bronchioles) because the parallel arrangement of small airways gives a maximal cross-sectional area and low resistance.\n"
        "Reynolds number is proportional to velocity; >4000 is turbulent flow (trachea, bronchi), 4000–2000 transitional (respiratory bronchioles) and <2000 laminar (alveolar duct, alveoli).",
    ),
    S9: (
        "Alveolar Type I vs Type II Cells, Bleomycin Effect, Surfactant Function/Components/Synthesis & GM-CSF",
        "Alveolar cells (p192) are the pulmonary alveolar macrophage and the type I/II pneumocytes. Type I is 95%, a non-dividing flat squamous cell, prone to oxidative damage and injured by bleomycin, marked by aquaporin-5, caveolin-1 and carboxypeptidase m. Type II is 5%, cuboidal, repairs after injury and makes surfactant, becomes hyperplastic with bleomycin, and is marked by surfactant proteins A–D.\n"
        "Notes: substance P is a bronchoconstrictor; DPPC = dipalmitoyl phosphatidylcholine; bronchoconstriction peaks at 6 am and bronchodilatation at 6 pm; beractant is used in hyaline membrane disease/fetal respiratory distress syndrome.\n"
        "Surfactant lowers surface tension, preventing fluid accumulation (pulmonary edema) and raising compliance. Lamellar bodies in type 2 pneumocytes store and produce it; steroids (used for HMD) and thyroid hormone raise production while insulin lowers it. Lipoprotein is the major component with lecithin (DPPC) > sphingomyelin, plus proteins A–D (A and D in innate immunity); GM-CSF clears excess surfactant and its antibodies cause pulmonary alveolar proteinosis.",
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
