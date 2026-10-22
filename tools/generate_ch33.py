#!/usr/bin/env python3
"""Generate Chapter 33: Pulmonary Function Tests (Book p197–205).

Every question is anchored to a specific table cell, formula, flowchart branch,
graph caption or Note in uploads/02.pdf (PDF pages 80–88 = Book pages 197–205)
in strict book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 33
TITLE = "Pulmonary Function Tests"
PAGES = "197-205"

S1 = "Lung Volumes and Capacities Tables (TV/IRV/ERV/RV with Male-Female Split; IC/FVC/FRC/TLC Formulas) & Volume-Time Graph"
S2 = "Residual Volume Measurement (Plethysmography vs Obsolete Gas Methods), Spirometry Procedure/Disadvantage, FEV1/FVC & Obstructive-Restrictive-Vascular Disease Tree"
S3 = "Obstructive Disease (Emphysema): Hyperinflation Phase I vs Air Trapping Phase II Table & Bronchodilator Reversibility Testing"
S4 = "Restrictive Lung Disease: Diffusion vs Ventilation Indices, Intraparenchymal vs Extraparenchymal Types & Vascular Lung Disease"
S5 = "Small Airway Disease (mmEFR, Closing Volume/Fowler) & Flow-Volume Curve Patterns (Normal, Mild, Severe Obstruction, Restriction)"
S6 = "Upper Airway Obstruction Patterns (Extrathoracic/Intrathoracic/Fixed), Neuromuscular & Parenchymal Loops, and GOLD Staging"
S7 = "DLCO: Definition, Normal Values, Alveolo-Capillary Membrane Layers, Advantages of CO, Procedure & Blood Volume Determinant"
S8 = "Conditions Raising/Lowering DLCO, False-Low DLCO Causes, Diffuse Alveolar Hemorrhage & DLCO Across Respiratory Disorders"
S9 = "Coefficient of Diffusion (Kco) & the Stepwise Approach to Evaluation of Lung Diseases Flowchart"

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
# UNIT 1 — Page 197
# ==============================================================================

add(
    S1, 197, "numeric",
    "The lung volumes table on page 197 gives tidal volume in millilitres and also weight-normalised. Which values are printed?",
    "500 ml (5–7 mL/kg)",
    [
        "500 ml (10–15 mL/kg)",
        "250 ml (5–7 mL/kg)",
        "500 ml (3–5 mL/kg)",
    ],
    "Page 197 prints 'Tidal volume (TV) 500 ml (5–7 mL/kg)' defined as the 'Amount of air flowing in and out of lungs during normal quiet breathing.' (Book p197)",
)

add(
    S1, 197, "match",
    "The lung volumes table on page 197 splits two volumes by sex. Match each value with the volume and sex printed against it — 1) 3.3 L 2) 1.8 L 3) 1.3 L 4) 0.8 L … A) IRV male B) IRV female C) ERV male D) ERV female",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-B, 3-D, 4-C",
        "1-C, 2-D, 3-A, 4-B",
    ],
    "Page 197 reads 'Inspiratory Reserve volume (IRV) M : 3.3 L, F : 1.8 L' and 'expiratory Reserve volume (ERV) M : 1.3 L, F : 0.8 L'. (Book p197)",
)

add(
    S1, 197, "recall",
    "How is residual volume (RV) defined on page 197, and what single value is printed for it?",
    "Amount of air remaining in lungs at the end of forceful maximum expiration; 1.2 L",
    [
        "Amount of air remaining in lungs after a normal expiration; 1.2 L",
        "Amount of air remaining in lungs at the end of forceful maximum expiration; 2.2 L",
        "Amount of air expired with maximum force after tidal expiration; 1.2 L",
    ],
    "Page 197 prints 'Residual volume (RV) 1.2 L — Amount of air remaining in lungs at the end of forceful maximum expiration.' (Book p197)",
)

add(
    S1, 197, "numeric",
    "The lung capacities table on page 197 prints each capacity with both a formula and a numeric expansion. Which pair is printed for inspiratory capacity (IC) and for total lung capacity (TLC)?",
    "IC 3.5 L = TV + IRV (0.5 L + 3 L); TLC 5.7 L = FVC + RV (4.5 L + 1.2 L)",
    [
        "IC 3.5 L = TV + IRV (0.5 L + 3 L); TLC 5.7 L = FRC + IC (2.2 L + 3.5 L)",
        "IC 4.5 L = TV + IRV (0.5 L + 4 L); TLC 5.7 L = FVC + RV (4.5 L + 1.2 L)",
        "IC 3.5 L = TV + ERV (0.5 L + 3 L); TLC 5.7 L = FVC + RV (4.5 L + 1.2 L)",
    ],
    "Page 197 prints 'Inspiratory Capacity (IC) 3.5 L — TV + IRV — 0.5 L + 3 L' and 'Total Lung Capacity (TLC) 5.7 L — FVC + RV — 4.5 L + 1.2 L'. (Book p197)",
)

add(
    S1, 197, "numeric",
    "For functional residual capacity (FRC) the table gives three entries in the formula cell. Which three are printed?",
    "ERV + RV; 1 L + 1.2 L; 1/2 FVC — with FRC given as 2.2 L",
    [
        "ERV + RV; 1 L + 1.2 L; 1/2 FVC — with FRC given as 3.2 L",
        "IRV + RV; 1 L + 1.2 L; 1/2 FVC — with FRC given as 2.2 L",
        "ERV + RV; 1 L + 1.2 L; 1/3 FVC — with FRC given as 2.2 L",
    ],
    "Page 197 prints 'Functional Residual Capacity (FRC) 2.2 L' with formula entries 'ERV + RV', '1 L + 1.2 L' and '1/2 FVC', and the definition 'Amount of air remaining in lung after a normal expiration'. (Book p197)",
)

add(
    S1, 197, "recall",
    "Which definition is printed for forced vital capacity (FVC) in the page 197 table?",
    "Amount of air expired with maximum force after forceful maximal inspiration",
    [
        "Amount of air expired with maximum force after a tidal expiration",
        "Amount of air inspired with maximum force after a tidal inspiration",
        "Amount of air remaining in lung after a normal expiration",
    ],
    "The FVC row reads 'TV + IRV + ERV / 0.5 L + 3 L + 1 L' with the definition 'Amount of air expired with maximum force after forceful maximal inspiration.' (Book p197)",
)

add(
    S1, 197, "recall",
    "Two statements close page 197 under 'Note :'. Which pair is printed?",
    "Elastic recoil pressure on the system is zero, and the elastic recoil pressure of the lung is counter-balanced by expansion of the chest wall",
    [
        "Elastic recoil pressure on the system is zero, and the elastic recoil pressure of the lung is counter-balanced by contraction of the chest wall",
        "Elastic recoil pressure on the system is 7–8 mmHg, and the elastic recoil pressure of the lung is counter-balanced by expansion of the chest wall",
        "Elastic recoil pressure on the system equals that of the chest wall, and the lung's recoil adds to it",
    ],
    "Page 197 prints 'Note : Elastic recoil pressure on the system : Zero. Elastic recoil pressure of lung = Counter-balanced by expansion of chest wall.' (Book p197)",
)

# ==============================================================================
# UNIT 2 — Page 198
# ==============================================================================

add(
    S2, 198, "recall",
    "Under 'RV :' on page 198, which two measurements are said to be impossible with a spirometer, and for what reason?",
    "RV cannot be measured with a spirometer, and hence FRC and TLC cannot be measured",
    [
        "TLC cannot be measured with a spirometer, and hence RV and FRC cannot be measured",
        "RV cannot be measured with a spirometer, and hence FVC and TLC cannot be measured",
        "FRC cannot be measured with a spirometer, and hence RV and IC cannot be measured",
    ],
    "Page 198 prints 'RV : • Cannot be measured with spirometer. • Hence FRC & TLC cannot be measured.' (Book p198)",
)

add(
    S2, 198, "match",
    "Three methods for measuring RV are listed on page 198, one of which avoids the printed drawback. Match each method with the page's annotation — 1) Total body plethysmography 2) Closed-circuit helium method 3) Open-circuit nitrogen washout method … A) Photographed as 'Total body plethysmography' in the panel B) Bracketed as obsolete C) Bracketed as obsolete for the same reason",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 198 lists 'measured using : 1. Total body plethysmography. 2. Closed-circuit helium method. 3. Open-circuit nitrogen washout method.' with a brace marked 'Obsolete (doesn't include trapped gas in closed airways/pneumothorax)' spanning the helium and nitrogen-washout methods; the accompanying photograph is captioned 'Total body plethysmography'. (Book p198)",
)

add(
    S2, 198, "fillup",
    "The brace beside the helium and nitrogen-washout methods on page 198 is labelled 'Obsolete' because these methods do not include ______.",
    "Trapped gas in closed airways/pneumothorax",
    [
        "Alveolar dead space",
        "Anatomical dead space",
        "Residual volume above FRC",
    ],
    "Page 198 prints 'Obsolete (doesn't include trapped gas in closed airways/pneumothorax)'. (Book p198)",
)

add(
    S2, 198, "recall",
    "Under 'Spirometry' on page 198, what two graphs is the test used to plot, and what single disadvantage is printed?",
    "Volume–time graph and flow–volume graph; the disadvantage is that it is physically demanding, so it is not done after MI/stroke/strenuous physical activity/smoking",
    [
        "Volume–time graph and pressure–volume graph; the disadvantage is radiation exposure",
        "Flow–volume graph and pressure–volume graph; the disadvantage is that it is physically demanding",
        "Volume–time graph and flow–volume graph; the disadvantage is that it cannot measure flow",
    ],
    "Page 198 prints 'uses : measuring 'volume' and 'flow' to plot 1. volume–Time graph. 2. Flow–volume graph.' and 'Disadvantage : Physically demanding → Not done after MI/stroke/strenuous physical activity/smoking.' (Book p198)",
)

add(
    S2, 198, "recall",
    "The printed spirometry procedure on page 198 has three steps. Which sequence and durations are given?",
    "Maximal inspiration → blast of expiration (continuous exhalation for 15 s or minimum 6 s) → maximum inhalation",
    [
        "Maximal inspiration → blast of expiration (continuous exhalation for 6 s or minimum 3 s) → maximum inhalation",
        "Tidal inspiration → blast of expiration (continuous exhalation for 15 s) → tidal inhalation",
        "Maximal inspiration → blast of expiration (continuous exhalation for 15 s) → maximum exhalation",
    ],
    "Page 198 prints 'Procedure : Maximal inspiration → Blast of expiration (continuous exhalation for 15s or minimum 6s) → maximum inhalation'. (Book p198)",
)

add(
    S2, 198, "numeric",
    "On the volume–time graph of page 198, what is printed for FVC in litres and for the normal FEV1/FVC ratio with its absolute volume?",
    "FVC 4.5 L normally expired in 5–6 s; FEV1/FVC ≥ 80% (4 L)",
    [
        "FVC 5.7 L normally expired in 5–6 s; FEV1/FVC ≥ 80% (4 L)",
        "FVC 4.5 L normally expired in 1 s; FEV1/FVC ≥ 70% (4 L)",
        "FVC 4.5 L normally expired in 5–6 s; FEV1/FVC ≥ 80% (3 L)",
    ],
    "Page 198 prints 'FVC : 4.5 L normally expired in 5–6 s.' and 'In normal individuals : FEV1/FVC ≥ 80% (4 L).' (Book p198)",
)

add(
    S2, 198, "match",
    "Match each arm of the 'LUNG DISEASES' tree on page 198 with the examples printed under it — 1) Obstructive 2) Restrictive 3) Vascular … A) Pulmonary HTN and pulmonary thromboembolism B) COPD (chronic bronchitis, emphysema, small airway disease), asthma, cystic fibrosis, bronchiolitis, bronchiectasis C) Intraparenchymal (ILD) and extraparenchymal (neuromuscular, chest wall)",
    "1-B, 2-C, 3-A",
    [
        "1-A, 2-C, 3-B",
        "1-B, 2-A, 3-C",
        "1-C, 2-B, 3-A",
    ],
    "The tree on page 198 splits into 'Obstructive' (COPD with chronic bronchitis, emphysema and small airway disease; bronchial asthma; cystic fibrosis; bronchiolitis; bronchiectasis), 'Restrictive' (intraparenchymal → ILD; extraparenchymal → neuromuscular: myasthenia gravis, Guillain-Barré syndrome, and chest wall disorders: kyphoscoliosis, obesity, ankylosing spondylitis) and 'Vascular' (pulmonary HTN, pulmonary thromboembolism). (Book p198)",
)

# ==============================================================================
# UNIT 3 — Page 199
# ==============================================================================

add(
    S3, 199, "recall",
    "Page 199 begins with the normal physiology of forceful expiration. Which chain and which driving pressure are printed?",
    "Driving pressure (elastic recoil pressure + intrapleural pressure) > airway pressure → opens up alveoli → air exhaled out",
    [
        "Driving pressure (elastic recoil pressure − intrapleural pressure) > airway pressure → opens up alveoli → air exhaled out",
        "Driving pressure (elastic recoil pressure + intrapleural pressure) < airway pressure → alveoli collapse → air exhaled out",
        "Airway pressure > driving pressure → opens up alveoli → air exhaled out",
    ],
    "Page 199 prints 'Normally : On forceful expiration → driving pressure (Elastic recoil pressure + intrapleural pressure) > airway pressure → Opens up alveoli → Air exhaled out', with the side note 'Post exhalation → Positive intrapleural pressure'. (Book p199)",
)

add(
    S3, 199, "match",
    "Page 199 traces COPD as a five-step failure chain. Match each step with the printed text — 1) Low elastic recoil pressure 2) Driving pressure vs airway pressure 3) Collapse of bronchioles 4) Dynamic compression of airways … A) Easy to inflate, giving a hyperinflated lung (Phase 1) B) Driving pressure < airway pressure C) Due to absence of cartilage D) Leads to air trapping (Phase 2)",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-B, 2-A, 3-C, 4-D",
        "1-A, 2-C, 3-B, 4-D",
        "1-A, 2-B, 3-D, 4-C",
    ],
    "Page 199 prints 'In COPD : Low elastic recoil pressure → easy to inflate → hyperinflated lung (Phase 1) → driving pressure < airway pressure → Collapse of bronchioles (D/t absence of cartilage) → Dynamic compression of airways → Cannot exhale air out → Air trapping (Phase 2)'. (Book p199)",
)

add(
    S3, 199, "match",
    "Match each entry of the two-phase table on page 199 with its printed pattern — 1) Phase of hyperinflation 2) Phase of air trapping 3) TLC in the phase of air trapping … A) FVC normal, FEV1 ↓↓, FEV1/FVC ↓↓, RV ↑↑, TLC ↑↑, reversibility (−) B) FVC ↓↓, FEV1 ↓↓↓, FEV1/FVC ↓↓, RV ↑↑, reversibility (−) C) Normal",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The table on page 199 reads 'I. Phase of hyperinflation: FVC Normal, FEV1 ↓↓, FEV1/FVC ↓↓, RV ↑↑, TLC ↑↑, Reversibility (−)' and 'II. Phase of air trapping: FVC ↓↓, FEV1 ↓↓↓, FEV1/FVC ↓↓, RV ↑↑, TLC Normal, Reversibility (−)'. (Book p199)",
)

add(
    S3, 199, "recall",
    "On which spirometric criterion does page 199 branch to bronchodilator reversibility testing, and what exact value is printed?",
    "FEV1/FVC < 0.7",
    [
        "FEV1/FVC > 0.7",
        "FEV1 < 80% predicted",
        "FVC < 80% predicted",
    ],
    "Page 199 prints 'On spirometry : FEV1/FVC < 0.7' with an arrow into 'bronchodilator reversibility testing'. (Book p199)",
)

add(
    S3, 199, "recall",
    "Which two bronchodilators and doses are printed for reversibility testing on page 199, and when is the test repeated?",
    "Salbutamol (short-acting bronchodilator) 100 mg × 4 puffs or ipratropium (short-acting anticholinergic) 40 mg × 4 puffs; repeat after 30 mins",
    [
        "Salbutamol 100 µg × 4 puffs or ipratropium 40 µg × 4 puffs; repeat after 15 mins",
        "Salbutamol 100 mg × 4 puffs or ipratropium 40 mg × 4 puffs; repeat after 15 mins",
        "Salmeterol 100 mg × 4 puffs or tiotropium 40 mg × 4 puffs; repeat after 30 mins",
    ],
    "Page 199 prints 'Patient given → Salbutamol (Short-acting bronchodilator) : 100 mg × 4 puffs or → Ipratropium (Short-acting anticholinergic) : 40 mg × 4 puffs' then 'Repeat the test after 30 mins' — note the mass units are printed as mg on this page. (Book p199)",
)

add(
    S3, 199, "recall",
    "What two criteria are printed together as indicating reversibility on page 199, and which diagnosis is that arrowed to?",
    "FEV1 increase by 200 mL plus FEV1 increases by >12%, calculated as (post FEV1 − repetition pre FEV1)/pre FEV1 → bronchial asthma",
    [
        "FEV1 increase by 200 mL plus FEV1 increases by >12% → COPD",
        "FEV1 increase by 100 mL plus FEV1 increases by >20% → bronchial asthma",
        "FEV1 increase by 200 mL plus FEV1 increases by >12%, with a residual FEV1/FVC < 0.7 → COPD",
    ],
    "Page 199 prints 'FEV1 increase by 200 mL + FEV1 increases by >12% : ((Post FEV1 − repetition pre FEV1)/pre FEV1) → Indicates reversibility → Bronchial asthma', while the alternative branch 'FEV1/FVC < 0.7 → COPD'. (Book p199)",
)

add(
    S3, 199, "truefalse",
    "Which statement about the two COPD phases on page 199 is accurate?",
    "True — Reversibility is printed as negative ('−') in both phases, and total lung capacity is raised only in the phase of hyperinflation",
    [
        "True — Total lung capacity is raised in both phases while FVC is reduced only in hyperinflation",
        "False — Reversibility is printed as positive in the phase of air trapping",
        "False — FEV1 falls less than FVC in the phase of air trapping",
    ],
    "The page 199 table gives 'Reversibility (−)' for both phases, TLC ↑↑ in phase I and 'Normal' in phase II, and FVC 'Normal' then '↓↓' while FEV1 is '↓↓' then '↓↓↓'. (Book p199)",
)

# ==============================================================================
# UNIT 4 — Page 200
# ==============================================================================

add(
    S4, 200, "recall",
    "Page 200 opens the restrictive (ILD) section with a statement of the underlying derangement. Which is printed?",
    "Derangement in diffusion and ventilation due to fibrosis, initially defective diffusion from alveoli into capillary",
    [
        "Derangement in diffusion only, due to fibrosis, initially defective ventilation",
        "Derangement in diffusion and ventilation due to elastin loss, initially defective diffusion from capillary into alveoli",
        "Derangement in perfusion and ventilation due to fibrosis, initially defective diffusion",
    ],
    "Page 200 prints 'Derangement in diffusion and ventilation → D/t fibrosis → Initially : defective diffusion from alveoli into capillary → ↓ DLCO (Diffusion lung capacity of carbon monoxide) → Normal FVC'. (Book p200)",
)

add(
    S4, 200, "match",
    "Match each index in the progressed-ILD list on page 200 with the arrow printed against it — 1) FVC 2) FEV1 3) FEV1/FVC 4) RV 5) TLC 6) DLCO … A) ↓↓↓ B) ↓ C) N/↑ D) ↓↓ E) ↓↓ F) ↓↓",
    "1-A, 2-B, 3-C, 4-D, 5-E, 6-F",
    [
        "1-D, 2-B, 3-C, 4-A, 5-E, 6-F",
        "1-A, 2-D, 3-C, 4-B, 5-E, 6-F",
        "1-A, 2-B, 3-E, 4-D, 5-C, 6-F",
    ],
    "Page 200 prints, as disease progresses: '• FVC : ↓↓↓ • FEV1 : ↓ • FEV1/FVC : N/↑ • RV : ↓↓ • TLC : ↓↓ • DLCO ↓↓'. Note RV, TLC and DLCO all carry the same '↓↓' arrow. (Book p200)",
)

add(
    S4, 200, "match",
    "Match the three patterns printed across pages 200 with their findings — 1) Intraparenchymal restrictive disease 2) Extraparenchymal restrictive disease 3) Vascular lung disease … A) Diffusion disorder (eg ILD) with ↓↓↓ DLCO B) Ventilation disorder (↓↓↓ FVC) with normal diffusion (normal DLCO) and normal RV C) Normal FEV1, FVC and FEV1/FVC with abnormal DLCO",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "The 'Types :' tree on page 200 splits 'Intraparenchymal : • Diffusion disorder. • e.g, ILD. • ↓↓↓ DLCO.' from 'Extraparenchymal : • ventilation disorder (↓↓↓ FVC). • Normal diffusion (Normal DLCO). • Normal RV.' (Book p200)",
)

add(
    S4, 200, "match",
    "Match the extraparenchymal sub-branches on page 200 with their examples and RV/TLC entries — 1) Pure inspiratory (neuromuscular) disorders 2) Inspiratory + expiratory disorder 3) TLC in the pure inspiratory group … A) Eg. myasthenia gravis, with ↑↑ RV/TLC B) Eg. kyphoscoliosis, with normal RV/TLC C) ↓TLC",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 200 prints 'Pure inspiratory (Neuromuscular) disorders : Eg. myasthenia Gravis — ↑↑ RV/TLC, ↓TLC' and 'Inspiratory + Expiratory disorder : Eg. Kyphoscoliosis — Normal RV/TLC'. (Book p200)",
)

add(
    S4, 200, "recall",
    "Under 'Vascular Lung Disease :' on page 200, which three spirometric indices are normal and which single measurement is abnormal?",
    "Normal FEV1, FVC and FEV1/FVC; abnormal DLCO",
    [
        "Normal FEV1, FVC and DLCO; abnormal FEV1/FVC",
        "Normal FEV1/FVC and DLCO; abnormal FVC",
        "Normal FEV1 and FEV1/FVC; abnormal FVC and DLCO",
    ],
    "Page 200 prints 'Vascular Lung Disease : • Normal FEV1, FVC, FEV1/FVC. • Abnormal DLCO.' (Book p200)",
)

add(
    S4, 200, "scenario",
    "A patient with ILD has a falling DLCO but a preserved FVC early in the illness. Which two lines on page 200 explain this discordance?",
    "Initially there is defective diffusion from alveoli into the capillary with a ↓DLCO and normal FVC; only as the disease progresses do diffusion and ventilation both fall",
    [
        "Initially there is defective ventilation with a normal DLCO and ↓FVC; later diffusion falls",
        "Initially there is a ventilation disorder with ↓↓↓FVC and normal DLCO, as printed for extraparenchymal disease",
        "Initially the FEV1/FVC ratio rises with a normal DLCO, and later the FVC falls",
    ],
    "Page 200 prints 'Initially : defective diffusion from alveoli into capillary → ↓ DLCO → Normal FVC' and 'As disease progresses : ↓↓ diffusion + ↓↓ ventilation' followed by the full index list. (Book p200)",
)

# ==============================================================================
# UNIT 5 — Page 201
# ==============================================================================

add(
    S5, 201, "recall",
    "Small airway disease is described on page 201 by four numbered points, the last of which is a raised closing volume. Which first two points explain that it 'cannot be diagnosed with a spirometer'?",
    "Normal FEV1/FVC and normal FVC",
    [
        "Reduced FEV1/FVC and normal FVC",
        "Normal FEV1/FVC and reduced FVC",
        "Normal FEV1 and raised TLC",
    ],
    "Page 201 prints '1. Normal FEV1/FVC 2. Normal FVC } cannot be diagnosed with a spirometer.' (Book p201)",
)

add(
    S5, 201, "recall",
    "Which third abnormality is printed for small airway disease on page 201, and what two alternative names are given for it?",
    "↓↓ maximal mid expiratory flow rate (mmEFR), AKA forced expiratory flow (FEF) 25–75 and forced expiratory flow rate in the mid half of the maneuver",
    [
        "↓↓ FEV1, AKA forced expiratory flow (FEF) 25–75 and forced expiratory flow rate in the mid half of the maneuver",
        "↓↓ maximal mid expiratory flow rate (mmEFR), AKA FEF 75–85 and peak expiratory flow rate",
        "↓↓ maximal mid expiratory flow rate (mmEFR), AKA FEF 25–75 and forced vital capacity",
    ],
    "Page 201 prints '3. ↓↓ maximal mid Expiratory Flow Rate (mmEFR). • AKA Forced expiratory flow (FEF) 25–75. • Forced expiratory flow rate in the mid half of the maneuver.' (Book p201)",
)

add(
    S5, 201, "numeric",
    "For closing volume, page 201 gives the measuring technique, the phase in which nitrogen is measured, and a normal value. Which set is printed?",
    "Single breath nitrogen/Fowler's technique (obsolete); nitrogen measured in phase 4; normal 10% of VC",
    [
        "Single breath helium technique; nitrogen measured in phase 3; normal 20% of VC",
        "Single breath nitrogen/Fowler's technique; nitrogen measured in phase 2; normal 10% of FVC",
        "Single breath nitrogen/Fowler's technique; nitrogen measured in phase 4; normal 30% of VC",
    ],
    "Page 201 prints '4. ↑↑ closing volume • measured using single Breath Nitrogen/Fowler's technique (Obsolete) → 100% O₂ administered → nitrogen in expired air measured in phase 4 (only upper alveoli open) • Normal : 10% of VC.' (Book p201)",
)

add(
    S5, 201, "match",
    "On the flow–volume curve, page 201 marks regions and one derived quantity. Match each with the printed text — 1) Effort dependent 2) Effort independent 3) FVC … A) Trachea, large airways B) The remainder of the curve, so labelled to the right of the peak C) Area under curve",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 201 labels the rising/peak portion 'effort dependent (Trachea, large airways)' and the descending limb 'effort independent'; the caption adds 'FVC : Area under curve'. (Book p201)",
)

add(
    S5, 201, "match",
    "Match each of the four flow-volume patterns on page 201 with its printed panel text — 1) Normal 2) Mild obstruction 3) Severe obstruction 4) Restriction … A) Late plateau, FVC preserved, PEFR mildly reduced, coving/scooping/dog-tail appearance B) PEFR, no coving C) No plateau, FVC reduced, PEFR severely reduced, coving D) Normal plateau, FVC reduced, PEFR normal or mildly reduced, no coving",
    "1-B, 2-A, 3-C, 4-D",
    [
        "1-A, 2-B, 3-C, 4-D",
        "1-B, 2-A, 3-D, 4-C",
        "1-D, 2-A, 3-C, 4-B",
    ],
    "The four columns of page 201 read: 'Normal — PEFR (no plateau label), no coving'; 'mild Obstruction — Late plateau, FVC preserved, PEFR mildly reduced, Coving/scooping/dog-tail appearance'; 'Severe Obstruction — No plateau, FVC reduced, PEFR severely reduced, Coving'; 'Restriction — Normal plateau, FVC reduced, PEFR normal or mildly reduced, No Coving'. (Book p201)",
)

add(
    S5, 201, "scenario",
    "A patient's flow-volume loop shows a late plateau with preserved FVC, a mildly reduced PEFR and a concave 'dog-tail' expiratory limb. Which page-201 pattern is this, and what is the named shape?",
    "Mild obstruction, with a coving/scooping/dog-tail appearance",
    [
        "Severe obstruction, with a coving appearance",
        "Restriction, with no coving",
        "Normal, with no coving",
    ],
    "Page 201's 'mild Obstruction' column prints 'Late plateau, FVC preserved, PEFR mildly reduced, Coving/scooping/dog-tail appearence' against the corresponding loop. (Book p201)",
)

# ==============================================================================
# UNIT 6 — Page 202
# ==============================================================================

add(
    S6, 202, "match",
    "Match each upper airway obstruction pattern on page 202 with the flattening printed for it — 1) Variable extrathoracic UAO 2) Variable intrathoracic UAO 3) Fixed upper airway obstruction … A) Flattening of inspiration B) Flattening of expiration C) Flattening of both expiration (high pleural pressure) and inspiration (negative intrathoracic pressure)",
    "1-A, 2-B, 3-C",
    [
        "1-C, 2-B, 3-A",
        "1-A, 2-C, 3-B",
        "1-B, 2-A, 3-C",
    ],
    "Page 202 captions the three loops 'variable extrathoracic uao — Flattening of inspiration', 'variable intrathoracic uao — Flattening of expiration' and 'Fixed upper Airway Obstruction (uAO) — Flattening of expiration (d/t high pleural pressure) + Flattening of inspiration (d/t negative intrathoracic pressure)'. (Book p202)",
)

add(
    S6, 202, "match",
    "Match each UAO type on page 202 with the examples printed beneath it — 1) Variable extrathoracic UAO 2) Variable intrathoracic UAO 3) Fixed upper airway obstruction … A) FB, tracheomalacia B) Vocal cord palsy, laryngeal tumor, goitre, obstructive sleep apnea syndrome C) Tracheal stenosis",
    "1-B, 2-A, 3-C",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B",
    ],
    "Page 202 prints examples: extrathoracic — 'vocal cord palsy, Laryngeal tumor, Goitre, Obstructive sleep apnea syndrome'; intrathoracic — 'FB, Tracheomalacia'; fixed — 'Eg : Tracheal stenosis'. (Book p202)",
)

add(
    S6, 202, "oddoneout",
    "Page 202 draws two further loops labelled outside the UAO group. All of the following are printed there EXCEPT:",
    "Obesity hypoventilation",
    [
        "Neuromuscular weakness",
        "Restrictive parenchymal lung disease",
        "Restrictive parenchymal lung disease with a small loop",
    ],
    "The two extra loops at the foot of the UAO group on page 202 are captioned 'Neuromuscular weakness' and 'Restrictive parenchymal lung disease', both drawn as small loops within the predicted envelope. (Book p202)",
)

add(
    S6, 202, "numeric",
    "The GOLD staging table on page 202 stages COPD by post-bronchodilator FEV1. Which four bands are printed?",
    "Stage I ≥80%; Stage II <80% to 50%; Stage III <50% to 30%; Stage IV <30",
    [
        "Stage I ≥70%; Stage II <70% to 50%; Stage III <50% to 30%; Stage IV <30",
        "Stage I ≥80%; Stage II <80% to 60%; Stage III <60% to 40%; Stage IV <40",
        "Stage I ≥80%; Stage II <80% to 50%; Stage III <50% to 25%; Stage IV <25",
    ],
    "The table reads 'Stage I ≥ 80%', 'II < 80% to 50%', 'III < 50% to 30%', 'IV < 30'. (Book p202)",
)

add(
    S6, 202, "recall",
    "On what measurement is the GOLD staging on page 202 explicitly based?",
    "Post-bronchodilator FEV1",
    [
        "Pre-bronchodilator FEV1",
        "Post-bronchodilator FEV1/FVC ratio",
        "DLCO percent predicted",
    ],
    "Page 202 prints 'Note : Staging of COPD based on post-bronchodilator FEV1 : Gold staging'. (Book p202)",
)

# ==============================================================================
# UNIT 7 — Page 203
# ==============================================================================

add(
    S7, 203, "recall",
    "How is DLCO expanded and defined at the top of page 203, and what does the test measure?",
    "Diffusing capacity of lungs for carbon monoxide; it measures the lung's ability to transfer gases across the respiratory membrane",
    [
        "Diffusing capacity of lungs for carbon dioxide; it measures the lung's ability to transfer gases across the respiratory membrane",
        "Diffusing capacity of lungs for carbon monoxide; it measures alveolar ventilation per unit time",
        "Diffusing capacity of lungs for carbon monoxide; it measures pulmonary capillary blood flow",
    ],
    "Page 203 prints 'DLCO/Transfer Factor — Diffusing capacity of lungs for Carbon monoxide. measurement of lung's ability to transfer gases across the respiratory membrane.' (Book p203)",
)

add(
    S7, 203, "numeric",
    "Page 203 gives a normal DLCO value together with two percentage bands. Which set is printed?",
    "Normal 20–30 mL per minute/mmHg; 70–140% of predicted value is normal physiology; in severe disease <40%",
    [
        "Normal 20–30 mL per minute/mmHg; 80–120% of predicted value; in severe disease <30%",
        "Normal 70–140 mL per minute/mmHg; 70–140% of predicted value; in severe disease <40%",
        "Normal 20–30 mL per minute/mmHg; 70–140% of predicted value; in severe disease <60%",
    ],
    "Page 203 prints 'values : Normal : 20–30 mL per minute/mmHg.' and 'Findings normal physiology : • 70–140% of predicted value, • In severe disease : <40%.' (Book p203)",
)

add(
    S7, 203, "numeric",
    "For the respiratory membrane, page 203 gives a surface area and a thickness. Which values are printed?",
    "Surface area 70 m²; thickness 0.2–0.5 µm",
    [
        "Surface area 70 m²; thickness 2–5 µm",
        "Surface area 50 m²; thickness 0.2–0.5 µm",
        "Surface area 100 m²; thickness 0.5–1 µm",
    ],
    "Page 203 prints 'respiratory membrane : • AKA alveolo-capillary membrane. • Surface area : 70 m². • Thickness : 0.2–0.5 µm.' (Book p203)",
)

add(
    S7, 203, "match",
    "Six layers of the respiratory membrane are printed on page 203. Match each numbered layer with its printed name — 1) I 2) II 3) III 4) IV 5) V 6) VI … A) Fluid and surfactants B) Interstitial space C) Alveolar epithelial layer D) Capillary basement membrane E) Epithelial basement layer F) Capillary endothelial layer",
    "1-A, 2-C, 3-E, 4-B, 5-D, 6-F",
    [
        "1-A, 2-C, 3-B, 4-E, 5-D, 6-F",
        "1-A, 2-D, 3-E, 4-B, 5-C, 6-F",
        "1-E, 2-C, 3-A, 4-B, 5-D, 6-F",
    ],
    "Page 203 numbers the layers 'I. Fluid and surfactants. II. Alveolar epithelial layer. III. Epithelial basement layer.' in the left column and 'IV. Interstitial space. V. Capillary basement membrane. VI. Capillary endothelial layer.' in the right column. (Book p203)",
)

add(
    S7, 203, "recall",
    "Three 'Advantages of CO' are printed on page 203. Which three are given?",
    "210 times higher affinity of Hb for CO than O2; negligible levels in blood; a diffusion-limited (not perfusion-limited) gas",
    [
        "210 times higher affinity of Hb for CO than O2; negligible levels in blood; a perfusion-limited (not diffusion-limited) gas",
        "21 times higher affinity of Hb for CO than O2; negligible levels in blood; a diffusion-limited gas",
        "210 times higher affinity of Hb for CO than O2; high baseline blood levels; a diffusion-limited gas",
    ],
    "Page 203 prints 'Advantages of CO : • 210 times higher affinity of Hb to CO than O2. • Negligible levels in blood. • Diffusion limited gas, not perfusion limited.' (Book p203)",
)

add(
    S7, 203, "recall",
    "The DLCO procedure on page 203 has three timed steps. Which timings and gas concentration are printed?",
    "Forceful deep inspiration (4 sec) of gas with 0.3% CO → hold breath (10 s) → maximal forced expiration",
    [
        "Forceful deep inspiration (10 sec) of gas with 0.3% CO → hold breath (4 s) → maximal forced expiration",
        "Forceful deep inspiration (4 sec) of gas with 3% CO → hold breath (10 s) → maximal forced expiration",
        "Tidal inspiration of gas with 0.3% CO → hold breath (10 s) → maximal forced expiration",
    ],
    "Page 203 prints 'Procedure : Forceful deep inspiration (4 sec) of gas with 0.3% CO → hold breath (10s) → maximal forced expiration.' (Book p203)",
)

add(
    S7, 203, "recall",
    "What is printed on page 203 as the most important determinant of DLCO, and what chain explains its effect?",
    "Blood volume — ↑ blood volume → ↑ Hb → ↑ CO binding to Hb → ↑ DLCO",
    [
        "Membrane thickness — ↑ thickness → ↑ diffusion distance → ↑ DLCO",
        "Blood volume — ↑ blood volume → ↓ Hb → ↓ CO binding to Hb → ↓ DLCO",
        "Alveolar surface area — ↑ area → ↑ CO binding → ↑ DLCO",
    ],
    "Page 203 prints 'FACTORS AFFECTING DLCO • Blood volume – most important determinant of DLCO. – ↑ Blood volume → ↑ Hb → ↑ CO binding to Hb → ↑ DLCO.' (Book p203)",
)

# ==============================================================================
# UNIT 8 — Page 204
# ==============================================================================

add(
    S8, 204, "match",
    "Match each condition in the '↑DLCO' column on page 204 with the parenthetical printed for it — 1) Diffuse alveolar hemorrhage 2) Polycythemia 3) Supine 4) Exercise … A) No parenthetical B) No parenthetical C) (↑ venous return) D) No parenthetical",
    "1-A, 2-B, 3-C, 4-D",
    [
        "1-C, 2-B, 3-A, 4-D",
        "1-A, 2-C, 3-B, 4-D",
        "1-D, 2-B, 3-C, 4-A",
    ],
    "The ↑DLCO column on page 204 lists 'Diffuse alveolar hemorrhage, Polycythemia, Supine (↑ venous return), Exercise, L→R shunting, Obesity, Pregnancy (↑ blood volume), mild congestive HF' — only supine and pregnancy carry parentheticals. (Book p204)",
)

add(
    S8, 204, "oddoneout",
    "The ↓DLCO column on page 204 contains only two entries. All of the following are also printed as causes of an ↑DLCO EXCEPT:",
    "Pulmonary edema (thick interstitium)",
    [
        "L→R shunting",
        "Obesity",
        "Mild congestive HF",
    ],
    "The ↓DLCO column on page 204 prints just 'Anemia (↓ blood volume)' and 'Pulmonary edema (thick interstitium)'; L→R shunting, obesity and mild congestive HF sit in the ↑DLCO column. (Book p204)",
)

add(
    S8, 204, "recall",
    "Which two 'Factors causing false low DLCO' are printed on page 204, with their explanations?",
    "High-flow O2 (high levels of oxyhemoglobin) and smoking (high carboxy hemoglobin → ↓ Hb binding to CO)",
    [
        "High-flow O2 (high levels of carboxyhemoglobin) and smoking (high levels of oxyhemoglobin → ↓ Hb binding to CO)",
        "Low-flow O2 (high levels of oxyhemoglobin) and smoking (high carboxy hemoglobin → ↑ Hb binding to CO)",
        "High-flow O2 (high levels of oxyhemoglobin) and anemia (↓ blood volume)",
    ],
    "Page 204 prints 'Factors causing false low DLCO : 1. High-flow O2 (high levels of oxyhemoglobin). 2. Smoking (High carboxy hemoglobin → ↓ Hb binding to CO).' (Book p204)",
)

add(
    S8, 204, "recall",
    "Under the diffuse alveolar hemorrhage note on page 204, what is the mechanism and what single example is printed?",
    "Due to bleeding within the lungs; example given is Goodpasture syndrome",
    [
        "Due to bleeding within the lungs; example given is polycythemia",
        "Due to capillary leak without bleeding; example given is Goodpasture syndrome",
        "Due to bleeding within the lungs; example given is pulmonary alveolar proteinosis",
    ],
    "Page 204 prints 'Diffuse Alveolar Hemorrhage • D/t bleeding within lungs • Eg : in goodpasture syndrome', beside a list of conditions for which 'DLCO used for diagnosis of : • Bleomycin toxicity • Pulmonary vasculitis • early ILD'. (Book p204)",
)

add(
    S8, 204, "match",
    "Match each respiratory disorder in the page 204 table with the DLCO change printed against it — 1) Asthma 2) Emphysema 3) Chronic bronchitis 4) Intraparenchymal restrictive lung disease (ILD) 5) Extraparenchymal restrictive lung disease 6) Vascular lung disease … A) ↑↑ B) ↓ C) Normal D) ↓↓↓ E) Normal F) ↓",
    "1-A, 2-B, 3-C, 4-D, 5-E, 6-F",
    [
        "1-B, 2-A, 3-C, 4-D, 5-E, 6-F",
        "1-A, 2-C, 3-B, 4-D, 5-E, 6-F",
        "1-A, 2-B, 3-C, 4-E, 5-D, 6-F",
    ],
    "The table on page 204 reads: Asthma ↑↑; Emphysema ↓; Chronic Bronchitis Normal; Intraparenchymal restrictive lung disease (ILD) ↓↓↓; Extraparenchymal restrictive lung disease Normal; Vascular lung disease ↓. (Book p204)",
)

add(
    S8, 204, "recall",
    "Which pathology explanations does page 204 print for the asthma, emphysema and vascular rows of the DLCO table?",
    "Asthma: pulmonary hyperemia with preferential perfusion; emphysema: ↑ volume/surface area ratio in alveoli; vascular: ↓ blood reaching lungs (normal FEV1, normal FVC)",
    [
        "Asthma: ↑ volume/surface area ratio in alveoli; emphysema: pulmonary hyperemia; vascular: ↓ blood reaching lungs",
        "Asthma: pulmonary hyperemia with preferential perfusion; emphysema: thickened respiratory membrane; vascular: ↓ blood reaching lungs",
        "Asthma: pulmonary hyperemia; emphysema: ↑ volume/surface area ratio in alveoli; vascular: thickened respiratory membrane",
    ],
    "The pathology column on page 204 reads: Asthma — 'Pulmonary hyperemia, Preferential perfusion'; Emphysema — '↑ volume/surface area ratio in alveoli'; ILD — 'Thickened respiratory membrane'; Vascular lung disease — '↓ Blood reaching lungs (Normal FEV1, Normal FVC)'. (Book p204)",
)

# ==============================================================================
# UNIT 9 — Page 205
# ==============================================================================

add(
    S9, 205, "fillup",
    "Page 205 opens with the coefficient of diffusion, written 'Kco = ______'.",
    "DLCO / Lung volume",
    [
        "DLCO × Lung volume",
        "Lung volume / DLCO",
        "DLCO / RV",
    ],
    "Page 205 prints 'COEFFICIENT OF DIFFUSION (Kco) — Kco = DLCO / Lung volume'. (Book p205)",
)

add(
    S9, 205, "management",
    "A patient has a restrictive spirometric pattern with a reduced lung volume. Using page 205, which Kco result would you use to separate an intraparenchymal from an extraparenchymal cause, and what management-pathway step follows?",
    "A normal Kco with a low DLCO indicates intraparenchymal disease, whereas a raised Kco with a normal DLCO indicates extraparenchymal disease, in which case RV/TLC is used to separate neuromuscular (raised) from chest wall (normal) disorders",
    [
        "A raised Kco with a low DLCO indicates intraparenchymal disease, whereas a normal Kco with a normal DLCO indicates extraparenchymal disease, in which case DLCO separates the two groups",
        "A normal Kco with a normal DLCO indicates intraparenchymal disease, whereas a low Kco with a low DLCO indicates extraparenchymal disease, in which case FEV1/FVC separates the two groups",
        "Kco cannot be used here; the flowchart uses post-bronchodilator FEV1 to separate intraparenchymal from extraparenchymal disease",
    ],
    "Page 205 prints 'Restrictive lung disease → Intraparenchymal : ↓DLCO, ↓ lung volume → (N) Kco' and '→ Extraparenchymal : N DLCO, ↓ lung volume → ↑ Kco'. (Book p205)",
)

add(
    S9, 205, "recall",
    "At the first branch of the 'Approach to Evaluation of Lung Diseases' flowchart on page 205, which two spirometric findings lead to 'obstructive lung disease', and what comes next in that column?",
    "FEV1/FVC = 0.7 with a normal FVC; next is post-bronchodilator FEV1 to distinguish asthma vs COPD",
    [
        "FEV1/FVC = 0.7 with a reduced FVC; next is DLCO to distinguish asthma vs COPD",
        "Normal FEV1/FVC with a normal FVC; next is post-bronchodilator FEV1 to distinguish asthma vs COPD",
        "FEV1/FVC = 0.7 with a normal FVC; next is RV/TLC to distinguish asthma vs COPD",
    ],
    "Page 205 prints the left column '• FEV1/FVC = 0.7 • Normal FVC → Obstructive lung disease → Post-bronchodilator FEV1 (Asthma vs COPD)'. (Book p205)",
)

add(
    S9, 205, "match",
    "Match each branch of the restrictive arm of the page 205 flowchart with the printed text — 1) FEV1/FVC normal/↑ with ↓FVC 2) ↓DLCO 3) Normal DLCO … A) Restrictive lung disease, then DLCO B) Intraparenchymal restrictive lung disease (ILD: (N) Kco) C) Extraparenchymal (↑Kco), then RV/TLC",
    "1-A, 2-B, 3-C",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "Page 205 prints the middle column '• FEV1/FVC : Normal/↑ • ↓FVC → Restrictive lung disease → DLCO' then splits '↓DLCO → Intraparenchymal Restrictive Lung Disease (ILD : (N) Kco)' and 'Normal DLCO → Extraparenchymal (↑Kco) → RV/TLC'. (Book p205)",
)

add(
    S9, 205, "recall",
    "At the bottom of the restrictive arm, how does the RV/TLC ratio separate neuromuscular from chest wall disorders on page 205?",
    "Raised RV/TLC → neuromuscular disorders; normal RV/TLC → chest wall disorders",
    [
        "Normal RV/TLC → neuromuscular disorders; raised RV/TLC → chest wall disorders",
        "Raised RV/TLC → chest wall disorders; reduced RV/TLC → neuromuscular disorders",
        "RV/TLC is not used; Kco separates the two groups",
    ],
    "Page 205 prints, after 'RV/TLC', two arrows: '↑ → Neuromuscular disorders' and 'Normal → Chest wall disorders'. (Book p205)",
)

add(
    S9, 205, "match",
    "Three parts of the page 205 flowchart use different labels. Match each with the printed text — 1) Right-hand column 2) Boxed note for small airway diseases 3) Middle column after restrictive disease … A) Normal FEV1/FVC, normal FVC, ↓DLCO → vascular lung disease and early ILD B) FEF 25–75 and closing volume C) DLCO",
    "1-A, 2-B, 3-C",
    [
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
    ],
    "Page 205's right column reads '• Normal FEV1/FVC • Normal FVC • ↓DLCO → vascular lung disease, early ILD', and the boxed note reads 'For small airway diseases : • FEF 25–75. • Closing volume.' (Book p205)",
)

GUIDES = {
    S1: (
        "Lung Volumes and Capacities Tables (TV/IRV/ERV/RV with Male-Female Split; IC/FVC/FRC/TLC Formulas) & Volume-Time Graph",
        "Lung volumes (p197): tidal volume 500 ml (5–7 mL/kg) is the air moving in and out during quiet breathing; IRV is M 3.3 L / F 1.8 L (maximum inspired after tidal inspiration); ERV is M 1.3 L / F 0.8 L (maximum expired after tidal expiration); RV is 1.2 L (remaining after forceful maximum expiration).\n"
        "Lung capacities: IC 3.5 L = TV + IRV (0.5 + 3 L); FVC 4.5 L = TV + IRV + ERV (0.5 + 3 + 1 L), the air expired with maximum force after forceful maximal inspiration; FRC 2.2 L = ERV + RV (1 + 1.2 L) = 1/2 FVC, the air remaining after a normal expiration; TLC 5.7 L = FVC + RV (4.5 + 1.2 L).\n"
        "Closing note: elastic recoil pressure of the system is zero, and the lung's elastic recoil is counter-balanced by expansion of the chest wall. The volume–time spirogram on the same page labels TV, IRV, ERV, RV, IC, FRC, VC and TLC.",
    ),
    S2: (
        "Residual Volume Measurement (Plethysmography vs Obsolete Gas Methods), Spirometry Procedure/Disadvantage, FEV1/FVC & Obstructive-Restrictive-Vascular Disease Tree",
        "RV (p198) cannot be measured with a spirometer, and therefore neither can FRC or TLC. It is measured by total body plethysmography (photographed), closed-circuit helium dilution or open-circuit nitrogen washout — the last two are bracketed 'Obsolete (doesn't include trapped gas in closed airways/pneumothorax)'.\n"
        "Spirometry measures volume and flow to plot volume–time and flow–volume graphs; it is physically demanding, so it is avoided after MI, stroke, strenuous activity or smoking. The procedure is maximal inspiration → blast of expiration (continuous exhalation for 15 s or minimum 6 s) → maximum inhalation. FVC is 4.5 L normally expired in 5–6 s and FEV1/FVC is ≥80% (4 L).\n"
        "The disease tree splits into obstructive (COPD with chronic bronchitis, emphysema and small airway disease; asthma; cystic fibrosis; bronchiolitis; bronchiectasis), restrictive (intraparenchymal ILD; extraparenchymal neuromuscular — myasthenia gravis, Guillain-Barré — and chest wall — kyphoscoliosis, obesity, ankylosing spondylitis) and vascular (pulmonary HTN, pulmonary thromboembolism).",
    ),
    S3: (
        "Obstructive Disease (Emphysema): Hyperinflation Phase I vs Air Trapping Phase II Table & Bronchodilator Reversibility Testing",
        "Normal forceful expiration (p199) depends on a driving pressure (elastic recoil plus intrapleural pressure) exceeding airway pressure. In COPD the elastic recoil is low, so the lung inflates easily and becomes hyperinflated (Phase 1); driving pressure then falls below airway pressure, bronchioles collapse because they lack cartilage, airways are dynamically compressed and air is trapped (Phase 2).\n"
        "Phase I: FVC normal, FEV1 ↓↓, FEV1/FVC ↓↓, RV ↑↑, TLC ↑↑, reversibility (−). Phase II: FVC ↓↓, FEV1 ↓↓↓, FEV1/FVC ↓↓, RV ↑↑, TLC normal, reversibility (−).\n"
        "If FEV1/FVC < 0.7, bronchodilator reversibility is tested with salbutamol 100 mg × 4 puffs or ipratropium 40 mg × 4 puffs (as printed), repeating after 30 minutes; a rise of 200 mL plus >12% ((post FEV1 − pre FEV1)/pre FEV1) indicates reversibility and bronchial asthma, whereas FEV1/FVC < 0.7 indicates COPD.",
    ),
    S4: (
        "Restrictive Lung Disease: Diffusion vs Ventilation Indices, Intraparenchymal vs Extraparenchymal Types & Vascular Lung Disease",
        "Restrictive/ILD physiology (p200): fibrosis deranges diffusion and ventilation; initially diffusion from alveolus to capillary fails, giving ↓DLCO with a normal FVC, and as disease progresses diffusion and ventilation both fall — FVC ↓↓↓, FEV1 ↓, FEV1/FVC normal or ↑, RV ↓↓, TLC ↓↓, DLCO ↓↓.\n"
        "Intraparenchymal disease is a diffusion disorder (eg ILD) with ↓↓↓ DLCO; extraparenchymal disease is a ventilation disorder (↓↓↓ FVC) with normal diffusion, normal DLCO and normal RV. Pure inspiratory (neuromuscular) disorders such as myasthenia gravis give ↑↑ RV/TLC with ↓TLC; combined inspiratory and expiratory disorders such as kyphoscoliosis give a normal RV/TLC.\n"
        "Vascular lung disease has normal FEV1, FVC and FEV1/FVC with an abnormal DLCO.",
    ),
    S5: (
        "Small Airway Disease (mmEFR, Closing Volume/Fowler) & Flow-Volume Curve Patterns (Normal, Mild, Severe Obstruction, Restriction)",
        "Small airway disease (p201) has normal FEV1/FVC and normal FVC, so it cannot be diagnosed with a spirometer; the diagnostic abnormalities are ↓↓ maximal mid-expiratory flow rate (mmEFR, also FEF 25–75, the flow in the mid half of the manoeuvre) and ↑↑ closing volume, measured by the single-breath nitrogen/Fowler technique (obsolete) with nitrogen read in phase 4 and normally 10% of VC.\n"
        "On the flow–volume curve the early portion is effort dependent (trachea, large airways) and the rest effort independent; FVC is the area under the curve.\n"
        "Patterns: normal — PEFR with no coving; mild obstruction — late plateau, FVC preserved, PEFR mildly reduced, coving/scooping/dog-tail; severe obstruction — no plateau, FVC reduced, PEFR severely reduced, coving; restriction — normal plateau, FVC reduced, PEFR normal or mildly reduced, no coving.",
    ),
    S6: (
        "Upper Airway Obstruction Patterns (Extrathoracic/Intrathoracic/Fixed), Neuromuscular & Parenchymal Loops, and GOLD Staging",
        "Upper airway obstruction (p202): variable extrathoracic obstruction flattens inspiration (vocal cord palsy, laryngeal tumour, goitre, obstructive sleep apnoea); variable intrathoracic obstruction flattens expiration (foreign body, tracheomalacia); fixed obstruction flattens both, expiration from high pleural pressure and inspiration from negative intrathoracic pressure (tracheal stenosis). Small loops are also drawn for neuromuscular weakness and restrictive parenchymal lung disease.\n"
        "GOLD staging uses post-bronchodilator FEV1: stage I ≥80%, II <80% to 50%, III <50% to 30%, IV <30%.",
    ),
    S7: (
        "DLCO: Definition, Normal Values, Alveolo-Capillary Membrane Layers, Advantages of CO, Procedure & Blood Volume Determinant",
        "DLCO or transfer factor (p203) is the diffusing capacity of the lung for carbon monoxide — a measure of the lung's ability to transfer gas across the respiratory membrane. Normal is 20–30 mL/min/mmHg; 70–140% of predicted is normal physiology and severe disease is <40%.\n"
        "The respiratory (alveolo-capillary) membrane has a surface area of 70 m² and thickness 0.2–0.5 µm, with six layers: I fluid and surfactants, II alveolar epithelium, III epithelial basement layer, IV interstitial space, V capillary basement membrane, VI capillary endothelium.\n"
        "CO is advantageous because its affinity for Hb is 210 times that of oxygen, blood levels are negligible and it is diffusion- rather than perfusion-limited. The manoeuvre is a 4-second deep inspiration of 0.3% CO, a 10-second breath hold, then maximal forced expiration. Blood volume is the most important determinant: ↑ blood volume → ↑ Hb → ↑ CO binding → ↑ DLCO.",
    ),
    S8: (
        "Conditions Raising/Lowering DLCO, False-Low DLCO Causes, Diffuse Alveolar Hemorrhage & DLCO Across Respiratory Disorders",
        "Raised DLCO (p204): diffuse alveolar haemorrhage, polycythaemia, supine posture (↑ venous return), exercise, left-to-right shunting, obesity, pregnancy (↑ blood volume) and mild congestive heart failure. Lowered DLCO: anaemia (↓ blood volume) and pulmonary oedema (thick interstitium).\n"
        "False-low DLCO is produced by high-flow oxygen (high oxyhaemoglobin) and by smoking (high carboxyhaemoglobin reducing Hb binding of CO). Diffuse alveolar haemorrhage from bleeding within the lungs, as in Goodpasture syndrome, raises DLCO; DLCO is used to diagnose bleomycin toxicity, pulmonary vasculitis and early ILD.\n"
        "DLCO by disorder: asthma ↑↑ (pulmonary hyperaemia with preferential perfusion), emphysema ↓ (printed as ↑ volume/surface area ratio in alveoli), chronic bronchitis normal, intraparenchymal restrictive disease ↓↓↓ (thickened respiratory membrane), extraparenchymal restrictive disease normal, vascular disease ↓ (↓ blood reaching lungs with normal FEV1 and FVC).",
    ),
    S9: (
        "Coefficient of Diffusion (Kco) & the Stepwise Approach to Evaluation of Lung Diseases Flowchart",
        "Kco (p205) = DLCO / lung volume. In restrictive disease the intraparenchymal pattern is ↓DLCO with ↓ lung volume giving a normal Kco, whereas the extraparenchymal pattern is normal DLCO with ↓ lung volume giving ↑Kco.\n"
        "Approach flowchart: FEV1/FVC = 0.7 with normal FVC → obstructive disease → post-bronchodilator FEV1 (asthma vs COPD); FEV1/FVC normal or ↑ with ↓FVC → restrictive disease → DLCO, where ↓DLCO means intraparenchymal disease (ILD, normal Kco) and normal DLCO means extraparenchymal disease (↑Kco) → RV/TLC, raised indicating neuromuscular and normal indicating chest-wall disorders; normal FEV1/FVC, normal FVC and ↓DLCO indicate vascular lung disease or early ILD, with FEF 25–75 and closing volume boxed for small airway disease.",
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
