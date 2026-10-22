#!/usr/bin/env python3
"""Generate Chapter 32: Clinical Physiology of Lungs (Book p193–196).

Every question is anchored to a specific printed line, pressure value on the
labelled traces, or table cell in uploads/02.pdf (PDF pages 76–79 = Book pages
193–196) in strict book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 32
TITLE = "Clinical Physiology of Lungs"
PAGES = "193-196"

S1 = "Tidal Volume, Boyle's Law, Three Pressures, Intrapleural Negativity & Intra-Alveolar Pressure Changes"
S2 = "Transpulmonary Pressure Equations, TPP Trace Values, Intrapleural Fluid Cohesiveness, Pneumothorax Note & Static Compliance"
S3 = "Hysteresis Loop, Surface Tension vs Elastic Recoil, Elastin/Collagen & Obstructive vs Restrictive Compliance Curves"
S4 = "Dynamic Compliance (Only-Dynamic vs Static-and-Dynamic Falls) & Elastic Recoil Pressure of the Respiratory System at RV/FRC/TLC"

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
# UNIT 1 — Page 193
# ==============================================================================

add(
    S1, 193, "numeric",
    "At the start of 'Pressures In Respiratory Physiology' on page 193, tidal volume (VT) is defined and a normal value printed. Which definition and value are given?",
    "Volume of air moving in & out of lungs; normal 500 mL",
    [
        "Volume of air moving in & out of lungs; normal 5000 mL",
        "Amount of air remaining after maximum expiration; normal 500 mL",
        "Amount of air inspired with maximum force after tidal inspiration; normal 500 mL",
    ],
    "Page 193 prints 'Tidal volume (V_T) : • volume of air moving in & out of lungs. • Normal : 500 mL.' (Book p193)",
)

add(
    S1, 193, "fillup",
    "Page 193 states Boyle's law as 'Tidal volume α ______' and uses the relation to link volume with transpulmonary pressure.",
    "1/TPP",
    [
        "TPP",
        "1/IAP",
        "1/intrapleural pressure",
    ],
    "Page 193 prints 'Boyle's law : Tidal volume α 1/T_PP' — i.e. tidal volume is inversely related to transpulmonary pressure. (Book p193)",
)

add(
    S1, 193, "match",
    "Match the three pressures listed under 'TYPES' on page 193 with their printed definition or location — 1) Intrapleural pressure 2) Intraalveolar pressure (IAP) 3) Transpulmonary pressure (TPP) … A) Intraalveolar/intrapulmonary pressure − intrapleural pressure B) Pressure in pleura C) Listed second, abbreviated IAP",
    "1-B, 2-C, 3-A",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-A, 3-C",
        "1-C, 2-B, 3-A",
    ],
    "Page 193 prints 'TYPES 1. Intrapleural pressure. 2. Intraalveolar pressure (IAP). 3. Transpulmonary pressure (TPP) : Intraalveolar/intrapulmonary pressure – Intrapleural pressure.' (Book p193)",
)

add(
    S1, 193, "recall",
    "Under 'Intrapleural pressure :' on page 193, two properties of the pleura are printed in parentheses. Which two are given?",
    "The pleura has lymphatics, and it has a vacuum so that the lung collapses while the chest expands",
    [
        "The pleura has lymphatics, and it has a positive pressure so that the lung expands with the chest",
        "The pleura lacks lymphatics, and it has a vacuum so that the lung collapses while the chest expands",
        "The pleura has blood vessels, and it has a vacuum so that both lung and chest collapse",
    ],
    "Page 193 prints '• Pleura. a. Has lymphatics. b. Has vacuum (Lung collapses, chest expands).' followed by '• Intrapleural pressure : Negative. – Positive in forceful expiration.' (Book p193)",
)

add(
    S1, 193, "recall",
    "Page 193 characterises inspiration and expiration. Which pair of statements is printed, and what chain follows inspiration?",
    "Inspiration is an active process and expiration a passive process; contraction of respiratory muscles and diaphragm → chest wall expands → pleural pressure ↓",
    [
        "Inspiration is a passive process and expiration an active process; contraction of respiratory muscles and diaphragm → chest wall expands → pleural pressure ↓",
        "Inspiration is an active process and expiration a passive process; contraction of respiratory muscles and diaphragm → chest wall contracts → pleural pressure ↑",
        "Both inspiration and expiration are active processes; relaxation of respiratory muscles → chest wall expands → pleural pressure ↓",
    ],
    "Page 193 prints 'Inspiration : Active process. Contraction of respiratory muscles & diaphragm → Chest wall expands → Pleural pressure ↓' and 'Expiration : Passive process.' (Book p193)",
)

add(
    S1, 193, "numeric",
    "Under 'Intra alveolar pressure :' on page 193, three values are printed for rest, inspiration and expiration. Which set is printed?",
    "At rest: zero; inspiration: −1 mmHg; expiration: +1 mmHg",
    [
        "At rest: −1 mmHg; inspiration: −3 mmHg; expiration: +3 mmHg",
        "At rest: zero; inspiration: −2 to −3 mmHg; expiration: +2 to +3 mmHg",
        "At rest: zero; inspiration: +1 mmHg; expiration: −1 mmHg",
    ],
    "Page 193 prints 'Intra alveolar pressure : a. At rest : Zero. b. Inspiration : Negative (−1 mmHg). c. Expiration : Positive (+1 mmHg).' (Book p193)",
)

add(
    S1, 193, "numeric",
    "On the intrapleural pressure trace at the right of page 193, two values are arrowed. What is printed at the start of inspiration and at the end of inspiration?",
    "Start of inspiration: −2 to −3 mmHg; end of inspiration: −7 to −8 mmHg",
    [
        "Start of inspiration: −5 to −6 mmHg; end of inspiration: −7 to −8 mmHg",
        "Start of inspiration: −2 to −3 mmHg; end of inspiration: −5 to −6 mmHg",
        "Start of inspiration: 0 mmHg; end of inspiration: −4 to −5 mmHg",
    ],
    "The labelled trace reads 'Start of inspiration : −2 to −3 mmHg' and 'End of inspiration : −7 to −8 mmHg', with intrapleural pressure printed as negative and positive only in forceful expiration. (Book p193)",
)

# ==============================================================================
# UNIT 2 — Page 194
# ==============================================================================

add(
    S2, 194, "match",
    "Page 194 gives three equations for transpulmonary pressure. Match each statement with the right-hand side printed for it — 1) Total TPP 2) TPP of chest wall 3) Total TPP (second printed form) … A) TPP of lung + TPP of chest wall B) Intra pleural pressure − atmospheric pressure C) IAP − atmospheric pressure",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 194 prints '• Total TPP = TPP of lung + TPP of chest wall • TPP of chest wall = Intra pleural pressure – atmospheric pressure. • Total TPP = IAP – atmospheric pressure.' (Book p194)",
)

add(
    S2, 194, "numeric",
    "The large pressure trace in the middle of page 194 marks the intra-alveolar and intrapleural pressures against an atmospheric pressure line. Which atmospheric value is printed, and what alveolar value appears during expiration?",
    "Atmospheric pressure 760 mmHg; intra-alveolar +1 mmHg during expiration",
    [
        "Atmospheric pressure 760 mmHg; intra-alveolar −1 mmHg during expiration",
        "Atmospheric pressure 756 mmHg; intra-alveolar +1 mmHg during expiration",
        "Atmospheric pressure 760 mmHg; intra-alveolar +7 to +8 mmHg during expiration",
    ],
    "The trace is scaled around 'Atmospheric pressure 760' and labels 'Intra-alveolar pressure' with '+1 mmHg' in expiration and '−1 mmHg' in inspiration; intrapleural pressure falls from '−2 to −3 mmHg' to '−7 to −8 mmHg'. (Book p194)",
)

add(
    S2, 194, "numeric",
    "At the lower right of the same figure, a bracketed TPP value is printed for the end of inspiration. What is it?",
    "TPP : 7–8 mmHg (end of inspiration)",
    [
        "TPP : 2–3 mmHg (end of inspiration)",
        "TPP : 1 mmHg (end of inspiration)",
        "TPP : 760 mmHg (end of inspiration)",
    ],
    "The right-hand arrow of the pressure trace is labelled 'TPP : 7–8 mmHg (end of inspiration)', and the vertical annotation reads 'TPP lung at start of inspiration : −2 to −3 mmHg' with a 'Transmural pressure gradient across the lung wall'. (Book p194)",
)

add(
    S2, 194, "recall",
    "Under 'LINKAGE OF LUNGS TO THORAX' on page 194, which two mechanisms are bracketed as the 'Forces that hold thoracic wall & lungs in close opposition'?",
    "Intrapleural fluid cohesiveness (water molecules attracted to each other, resisting being pulled apart) and negative intrapleural pressure",
    [
        "Intrapleural fluid cohesiveness and positive intrapleural pressure",
        "Surfactant activity and negative intrapleural pressure",
        "Elastic recoil of the lung and elastic recoil of the chest wall",
    ],
    "Page 194 prints 'Intrapleural fluid cohesiveness : • water molecules attracted to each other. • Resists being pulled apart' and 'Negative intrapleural pressure.' with a brace labelled 'Forces that hold thoracic wall & lungs in close opposition.' (Book p194)",
)

add(
    S2, 194, "recall",
    "The pneumothorax Note on page 194 lists three statements. Which three are printed?",
    "Intrapleural = intrapulmonary; TPP = 0; lung not inflated",
    [
        "Intrapleural = intrapulmonary; TPP = 7–8 mmHg; lung not inflated",
        "Intrapleural > intrapulmonary; TPP = 0; lung hyperinflated",
        "Intrapleural = intrapulmonary; TPP = 0; lung still inflated by surfactant",
    ],
    "Page 194 prints 'Note : Pneumothorax • Intrapleural = Intrapulmonary. • TPP = 0. • Lung not inflated.' (Book p194)",
)

add(
    S2, 194, "numeric",
    "What static compliance value is printed on page 194, and at what part of the pressure range is compliance maximal?",
    "Static compliance = 200 mL/cm of H2O; maximal at mid-range pressure",
    [
        "Static compliance = 200 mL/cm of H2O; maximal at low pressure",
        "Static compliance = 20 mL/cm of H2O; maximal at mid-range pressure",
        "Static compliance = 500 mL/cm of H2O; maximal at high pressure",
    ],
    "Page 194 prints 'Static compliance : 200 mL/cm of H₂O.' and 'max compliance : mid range pressure.' (Book p194)",
)

add(
    S2, 194, "recall",
    "Page 194 defines static compliance at tidal volume. Which three statements are printed?",
    "Inflation of lung per unit change in pressure; static compliance = ΔV/ΔP; ΔP = TPP",
    [
        "Inflation of lung per unit change in pressure; static compliance = ΔP/ΔV; ΔP = TPP",
        "Inflation of lung per unit change in pressure; static compliance = ΔV/ΔP; ΔP = IAP",
        "Deflation of lung per unit change in pressure; static compliance = ΔV/ΔP; ΔP = TPP",
    ],
    "Page 194 prints 'Static compliance at tidal volume : • Inflation of lung per unit change in pressure. • Static compliance = ΔV/ΔP • ΔP = TPP.' (Book p194)",
)

add(
    S2, 194, "numeric",
    "Two further annotations on the page 194 pressure figure give the TPP of the lung at the start of inspiration and name the driving gradient. Which pair is printed?",
    "TPP lung at start of inspiration: 2–3 mmHg (printed as −2 to −3 mmHg on the intrapleural scale), with a 'Transmural pressure gradient across the lung wall'",
    [
        "TPP lung at start of inspiration: 7–8 mmHg, with a 'Transmural pressure gradient across the lung wall'",
        "TPP lung at start of inspiration: 0 mmHg, with a 'Transmural pressure gradient across the chest wall'",
        "TPP lung at start of inspiration: 2–3 mmHg, with a 'Hydrostatic pressure gradient across the pleura'",
    ],
    "The figure is annotated 'TPP lung at start of inspiration : −2 to −3 mmHg' (the same magnitude as the intrapleural value at that instant) and the vertical brace is labelled 'Transmural pressure gradient across the lung wall'; the end-inspiratory value on the same figure is 'TPP : 7–8 mmHg'. (Book p194)",
)

# ==============================================================================
# UNIT 3 — Page 195
# ==============================================================================

add(
    S3, 195, "recall",
    "What does page 195 print under 'HYSTERESIS LOOP', and how is the loop's existence explained?",
    "The ΔV/ΔP curve differs for inspiration and expiration, because inspiration occurs against resistance whereas expiration is passive and requires no extra force",
    [
        "The ΔV/ΔP curve differs for inspiration and expiration, because expiration occurs against resistance whereas inspiration is passive",
        "The ΔV/ΔP curve is identical for inspiration and expiration, because both are passive processes",
        "The ΔV/ΔP curve differs for inspiration and expiration, because of surfactant degradation between breaths",
    ],
    "Page 195 prints 'ΔV/ΔP curve is different for inspiration & expiration.' with 'Reason' splitting into 'Inspiration : Occurs against resistance' and 'Expiration : • Passive process • Does not require extra force'. (Book p195)",
)

add(
    S3, 195, "match",
    "Under the inspiration limb on page 195, two resistances are bracketed and 'Overcome by' is applied to them. Match each with the printed text — 1) Surface tension 2) Surface tension, overcome by 3) Elastic recoil pressure (ERP of lung) … A) Marked '(more important)' B) Surfactant C) Listed third, with no 'overcome by' entry",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 195 brackets 'Surface tension (more important)' with 'Overcome by surfactant' beneath it, and lists 'Elastic recoil pressure (ERP of lung)' as the second bracket with no 'overcome by' entry. (Book p195)",
)

add(
    S3, 195, "match",
    "Match the two structural proteins named under 'elastic recoil pressure :' on page 195 with the property printed against each — 1) Elastin 2) Collagen 3) Structure whose change is listed next … A) Elastic force B) Tensile strength C) 'Changes in airway diseases'",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 195 prints 'elastic recoil pressure : • D/t → Elastin (elastic force) → Collagen (Tensile strength)'. (Book p195)",
)

add(
    S3, 195, "match",
    "For obstructive airway disease, page 195 lists three changes plus a consequence. Match each step of the chain with the printed text — 1) Static compliance 2) Shift of the curve 3) Structural change 4) Consequence … A) ↑ static compliance B) Curve shifts up & left C) Loss of elastin D) ↓ ERP, so easier to inflate lung",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-A, 2-C, 3-B, 4-D",
        "1-B, 2-A, 3-C, 4-D",
        "1-D, 2-B, 3-C, 4-A",
    ],
    "Under 'a. Obstructive diseases (eg : COPD, emphysema)' page 195 prints '• ↑ static compliance • Curve shifts up & left • Loss of elastin → ↓ ERP → Easier to inflate lung'. (Book p195)",
)

add(
    S3, 195, "match",
    "For restrictive disease, match each step of the chain on page 195 with the printed text — 1) Static compliance 2) Shift of the curve 3) Structural change 4) Consequence … A) ↓ static compliance B) Curve shifts down & right C) Fibrosis with ↑ collagen D) ↑ ERP, so difficult to inflate lung",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-B, 3-D, 4-C",
        "1-A, 2-C, 3-B, 4-D",
    ],
    "Under 'b. Restrictive diseases (eg : ILD)' page 195 prints '• ↓ static compliance • Curve shifts down & right • Fibrosis → ↑ Collagen → ↑ ERP → Difficult to inflate lung'. (Book p195)",
)

add(
    S3, 195, "oddoneout",
    "Page 195 labels three of the plotted pressure–volume curves in the bottom graph. Which label is NOT used there?",
    "Low compliance (pulmonary emphysema)",
    [
        "High compliance (Emphysema)",
        "Normal",
        "Low compliance (Pulmonary fibrosis)",
    ],
    "The bottom graph of page 195 is labelled 'High compliance (Emphysema)', 'Normal' and 'Low compliance (Pulmonary fibrosis)'. The accompanying legend in the upper chart also prints 'Interstitial fibrosis'. (Book p195)",
)

add(
    S3, 195, "recall",
    "The pressure–volume graph on page 195 is captioned and its two limbs are arrowed. What is printed for the caption and for the direction of each limb?",
    "'Pressure-volume curves of the lung during inspiration and expiration', with the expiration limb lying above the inspiration limb",
    [
        "'Pressure-volume curves of the lung during inspiration and expiration', with the inspiration limb lying above the expiration limb",
        "'Pressure-volume curves of the respiratory system and its components', with the expiration limb lying above the inspiration limb",
        "'Static compliance of lung', with identical inspiration and expiration limbs",
    ],
    "The graph on page 195 is captioned 'Pressure-volume curves of the lung during inspiration and expiration', and the arrows place 'Expiration' on the upper limb and 'Inspiration' on the lower limb, which is what makes the loop hysteretic. (Book p195)",
)

# ==============================================================================
# UNIT 4 — Page 196
# ==============================================================================

add(
    S4, 196, "recall",
    "How is dynamic compliance defined on page 196, and what relation to static compliance is printed?",
    "Static compliance + resistance; static and dynamic compliance will ↑/↓ together",
    [
        "Static compliance × resistance; static and dynamic compliance move in opposite directions",
        "Static compliance − resistance; static and dynamic compliance will ↑/↓ together",
        "Static compliance + elastance; dynamic compliance is independent of static compliance",
    ],
    "Page 196 prints '• Static compliance + resistance. • Static and dynamic compliance will ↑/↓ together.' (Book p196)",
)

add(
    S4, 196, "match",
    "Page 196 groups the causes of a fall in dynamic compliance into two brackets. Match each entry with the effect printed against it — 1) Foreign body, kink in ET tube, intrathoracic obstruction 2) Kink in ET tube, individually 3) Pulmonary edema, consolidation, atelectasis, pneumothorax … A) Only dynamic compliance ↓ B) Listed as the second cause of an isolated dynamic fall C) Static & dynamic compliance ↓",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 196 prints 'eg : Fall in dynamic compliance • Foreign body • Kink in ET tube • Intrathoracic obstruction } Only dynamic compliance ↓' and '• Pulmonary edema • Consolidation • Atelectasis • Pneumothorax } Static & dynamic compliance ↓'. (Book p196)",
)

add(
    S4, 196, "recall",
    "Which four causes are printed in the 'Static & dynamic compliance ↓' bracket on page 196?",
    "Pulmonary edema, consolidation, atelectasis and pneumothorax",
    [
        "Pulmonary edema, consolidation, atelectasis and foreign body",
        "Pulmonary fibrosis, consolidation, atelectasis and pneumothorax",
        "Pulmonary edema, emphysema, atelectasis and pneumothorax",
    ],
    "The second bracket on page 196 lists exactly 'Pulmonary edema, Consolidation, Atelectasis, Pneumothorax' and the first bracket lists foreign body, kink in ET tube and intrathoracic obstruction. (Book p196)",
)

add(
    S4, 196, "recall",
    "Under 'ERP of respiratory system' on page 196, how is total ERP expressed?",
    "Total ERP = ERP (Lung) + ERP (Chest wall)",
    [
        "Total ERP = ERP (Lung) − ERP (Chest wall)",
        "Total ERP = ERP (Lung) × ERP (Chest wall)",
        "Total ERP = ERP (Chest wall) only, since the lung contributes no recoil",
    ],
    "Page 196 prints 'Total ERP = ERP (Lung) + ERP (Chest wall)'. (Book p196)",
)

add(
    S4, 196, "match",
    "Match each lung volume in the 'Changes in ERP' table on page 196 with the contributor and sign printed for it — 1) At residual volume 2) At functional residual capacity 3) At total lung capacity … A) Chest wall only, ERP −ve (directed outwards) B) Chest wall + lung, ERP zero C) Chest wall + lung, ERP +ve (both forces directed downwards)",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The table on page 196 reads: at residual volume, ERP contributed by 'Chest wall', ERP '−ve (Directed outwards)', inflation 'Easy'; at FRC, 'Chest wall + lung', 'Zero (Tendency of collapse of lung counter balanced by chest wall expansion)', 'Easy'; at TLC, 'Chest wall + lung', '+ve (Both forces directed downwards)', 'Difficult'. (Book p196)",
)

add(
    S4, 196, "numeric",
    "The same table gives three printed facts about residual volume and FRC. Which set is printed?",
    "Residual volume = air left after forceful expiration, normal 1.2 L; FRC is AKA equilibrium/relaxation volume, holds air left after normal expiration, and FRC = RV + ERV",
    [
        "Residual volume = air left after normal expiration, normal 1.2 L; FRC = RV + IRV",
        "Residual volume = air left after forceful expiration, normal 2.1 L; FRC is AKA equilibrium volume and FRC = RV + ERV",
        "Residual volume = air left after forceful expiration, normal 1.2 L; FRC is AKA equilibrium volume and FRC = ERV + IC",
    ],
    "Page 196 prints under 'At residual volume': '• Air left after forceful expiration • Normal : 1.2 L'; under FRC: '• AKA Equilibrium volume, relaxation volume • Air left after normal expiration • FRC = RV + ERV'. (Book p196)",
)

add(
    S4, 196, "truefalse",
    "Which statement about elastic recoil pressure across lung volumes as printed on page 196 is accurate?",
    "True — At residual volume the chest wall alone contributes the recoil, which is negative and directed outwards, making inflation easy",
    [
        "True — At total lung capacity the recoil is zero because lung collapse and chest wall expansion balance",
        "False — At FRC the ERP is positive with both forces directed downwards",
        "False — At residual volume the recoil is contributed by the lung alone and is positive",
    ],
    "The table on page 196 assigns the −ve, outward, 'easy' state to residual volume (chest wall), zero to FRC ('chest wall + lung'), and +ve, downward, 'difficult' to TLC. (Book p196)",
)

add(
    S4, 196, "fillup",
    "On the dynamic-compliance graph on page 196, the slope of the loop is labelled as the quantity being measured: 'slope = ______'.",
    "dynamic compliance",
    [
        "static compliance",
        "airway resistance",
        "elastic recoil pressure",
    ],
    "The small loop plotted between expiration and inspiration on page 196 is annotated 'slope = dynamic complian[ce]' and captioned 'Dynamic compliance', contrasting with the static-compliance curve of page 194. (Book p196)",
)

GUIDES = {
    S1: (
        "Tidal Volume, Boyle's Law, Three Pressures, Intrapleural Negativity & Intra-Alveolar Pressure Changes",
        "Pressures in respiratory physiology (p193): tidal volume is the air moving in and out of the lungs, normal 500 mL; Boyle's law gives tidal volume α 1/TPP. Three pressures are intrapleural, intra-alveolar (IAP) and transpulmonary (TPP = intra-alveolar/intrapulmonary − intrapleural).\n"
        "Intrapleural pressure is the pressure in the pleura, which has lymphatics and a vacuum (lung collapses, chest expands); it is negative except in forceful expiration, where it becomes positive. Inspiration is active — respiratory muscles and diaphragm contract, the chest wall expands and pleural pressure falls; expiration is passive.\n"
        "Intra-alveolar pressure is zero at rest, −1 mmHg in inspiration and +1 mmHg in expiration; the printed intrapleural trace runs from −2 to −3 mmHg at the start of inspiration to −7 to −8 mmHg at the end.",
    ),
    S2: (
        "Transpulmonary Pressure Equations, TPP Trace Values, Intrapleural Fluid Cohesiveness, Pneumothorax Note & Static Compliance",
        "Transpulmonary pressure (p194): total TPP = TPP of lung + TPP of chest wall; TPP of chest wall = intrapleural − atmospheric pressure; total TPP = IAP − atmospheric pressure. The trace is drawn around an atmospheric pressure of 760 mmHg, with intra-alveolar +1 mmHg in expiration and a TPP of 7–8 mmHg at end-inspiration.\n"
        "Lungs are held to the thorax by intrapleural fluid cohesiveness (water molecules attracting one another and resisting being pulled apart) and by negative intrapleural pressure. In pneumothorax, intrapleural equals intrapulmonary pressure, TPP is 0 and the lung is not inflated.\n"
        "Static compliance is 200 mL/cm H2O, maximal at mid-range pressure, and equals ΔV/ΔP with ΔP = TPP; at tidal volume it is the inflation of lung per unit change in pressure.",
    ),
    S3: (
        "Hysteresis Loop, Surface Tension vs Elastic Recoil, Elastin/Collagen & Obstructive vs Restrictive Compliance Curves",
        "Hysteresis (p195): the ΔV/ΔP curve differs between inspiration and expiration because inspiration occurs against resistance while expiration is passive and needs no extra force. The resistances are surface tension (more important, overcome by surfactant) and elastic recoil pressure of the lung, which arises from elastin (elastic force) and collagen (tensile strength).\n"
        "Obstructive disease (COPD, emphysema): ↑ static compliance, curve shifted up and left, loss of elastin → ↓ ERP → easier to inflate. Restrictive disease (ILD): ↓ static compliance, curve shifted down and right, fibrosis → ↑ collagen → ↑ ERP → difficult to inflate.\n"
        "The plotted curves are labelled high compliance (emphysema), normal, and low compliance (pulmonary fibrosis).",
    ),
    S4: (
        "Dynamic Compliance (Only-Dynamic vs Static-and-Dynamic Falls) & Elastic Recoil Pressure of the Respiratory System at RV/FRC/TLC",
        "Dynamic compliance (p196) equals static compliance plus resistance, and static and dynamic compliance move together. Foreign body, kink in the ET tube and intrathoracic obstruction lower only dynamic compliance, whereas pulmonary edema, consolidation, atelectasis and pneumothorax lower both.\n"
        "ERP of the respiratory system: total ERP = ERP of lung + ERP of chest wall. At residual volume the chest wall alone contributes a negative, outward ERP and inflation is easy; at FRC (equilibrium/relaxation volume, RV + ERV) chest wall and lung together give zero ERP and inflation is easy; at TLC both forces act downwards giving a positive ERP and inflation is difficult. Residual volume is the air left after forceful expiration, normally 1.2 L.",
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
