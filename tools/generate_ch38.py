#!/usr/bin/env python3
"""Generate Chapter 38: Respiratory Failure and Acute Respiratory Distress Syndrome (Book p230–235).

Every question is anchored to a printed line, table cell or flowchart terminal of
uploads/02.pdf sheets 113–118 (Book pages 230–235), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 38
TITLE = "Respiratory Failure and Acute Respiratory Distress Syndrome"
PAGES = "230-235"

S1 = "Definition of Respiratory Failure, Hypoxemic/Hypercapnic Thresholds, the Partial-Pressure Abbreviation Box and the Type I Table (Diffusion Failure, CO Diffusion Potential, Etiology List Including the Asthma Exception)"
S2 = "Type III (Parenchymal Damage) and Type IV (Shock) Rows, the Anaesthesiology 'Type-3' FRC Note, the V/Q Ratio Zones and the Dead-Space-vs-Shunt Table"
S3 = "The Two Flowcharts: Hypoxemic Failure Branches (V/Q Mismatch, Shunt, Dead Space, Type II vs Type III, Oxygen-Responsiveness, High Altitude) and Hypercapnic Failure Branches"
S4 = "ARDS Synonyms, the 1992 AECC Criteria, Limitations and Mortality, the Berlin 2012 Definition with PEEP and Severity Table and the Factors Preventing Pulmonary Edema"
S5 = "ARDS Etiology (Primary and Secondary), the Toxin-to-Hyaline-Membrane Pathogenesis Chain, Alveolar Consequences and the Three Pathological Phases"
S6 = "ARDS Clinical Features, Mechanical Ventilation Strategies, the VILI Table (Volume, Baro and Atelecto Trauma) and the Differential of Acute Breathlessness"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(38000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(38100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p230
add(
    S1, 230, "numeric",
    "Which thresholds define respiratory failure on page 230?",
    "Hypoxemic: PaO2 < 60 mmHg on room air with SpO2 < 90%; hypercapnic: PaCO2 > 50 mmHg on room air",
    [
        "Hypoxemic: PaO2 < 80 mmHg on room air with SpO2 < 90%; hypercapnic: PaCO2 > 45 mmHg on room air",
        "Hypoxemic: PaO2 < 60 mmHg on room air with SpO2 < 80%; hypercapnic: PaCO2 > 50 mmHg on room air",
        "Hypoxemic: PaO2 < 60 mmHg on oxygen; hypercapnic: PaCO2 > 50 mmHg on oxygen",
    ],
    "The definition box reads 'Hypoxemic : PaO2 <60 mmHg on room air, SpO2 <90%' and 'Hypercapnic : PaCO2 >50 mmHg on room air'. Both thresholds are specified on room air.",
)

add(
    S1, 230, "match",
    "Match each abbreviation in the page 230 box with its printed meaning — 1) PAO2 2) PaO2 3) PaCO2 4) PAO2 − PaO2 … A) Partial pressure of carbon dioxide in artery (normal ~40 mmHg) B) Partial pressure of oxygen in alveoli C) Alveolocapillary oxygen gradient D) Partial pressure of oxygen in artery (normal ~97 mmHg)",
    "1-B, 2-D, 3-A, 4-C",
    ["1-D, 2-B, 3-A, 4-C", "1-B, 2-D, 3-C, 4-A", "1-C, 2-D, 3-A, 4-B"],
    "The box reads 'PAO2 : Partial pressure of oxygen in alveoli', 'PaO2 : Partial pressure of oxygen in artery (Normal ~97mmHg)', 'PaCO2 : Partial pressure of carbon dioxide in artery (Normal ~40mmHg)' and 'PAO2 − PaO2 : Alveolocapillary oxygen gradient'. The capital-A subscript is alveolar and the lower-case-a subscript arterial.",
)

add(
    S1, 230, "recall",
    "Which pathology chain is printed in the Type I column on page 230?",
    "Impaired diffusion → oxygenation failure, with the high (150 times) diffusion potential of CO and no hypercapnia",
    [
        "Hypoventilation → oxygenation failure, with the high (150 times) diffusion potential of CO and hypercapnia",
        "Impaired diffusion → ventilatory failure, with the low (15 times) diffusion potential of CO and no hypercapnia",
        "Impaired perfusion → oxygenation failure, with the high (150 times) diffusion potential of CO and no hypercapnia",
    ],
    "The Type I pathology cell reads 'Impaired diffusion → Oxygenation failure', then 'High (150 times) diffusion potential of CO' and 'No hypercapnia', with an alveolus-capillary diagram beneath. The 150-fold figure explains why CO transfer is used to measure diffusion.",
)

add(
    S1, 230, "recall",
    "Which set of partial pressures belongs to Type I respiratory failure on page 230?",
    "↓PaO2, normal PaCO2, ↑PAO2 − PaO2",
    [
        "↓PaO2, ↑PaCO2, normal PAO2 − PaO2",
        "↓PaO2, ↑PaCO2, ↑PAO2 − PaO2",
        "Normal PaO2, ↓PaCO2, ↑PAO2 − PaO2",
    ],
    "The partial-pressure column of Type I reads '↓PaO2', 'Normal PaCO2' and '↑PAO2 − PaO2'. A raised CO2 with a normal gradient is the Type II pattern, and a raised CO2 with a raised gradient the Type III pattern, both on the next page.",
)

add(
    S1, 230, "recall",
    "Which aetiological groups are listed in the Type I column besides ILD, pulmonary oedema/ARDS and pneumonia?",
    "Emphysema (↓surface area/volume), vascular causes such as thromboembolism and pulmonary HTN, pneumothorax, granulomatous lung disease, cystic congenital heart disease and bronchiectasis",
    [
        "Emphysema (↑surface area/volume), vascular causes such as thromboembolism and pulmonary HTN, pneumothorax, granulomatous lung disease, cystic congenital heart disease and bronchiectasis",
        "Emphysema (↓surface area/volume), vascular causes such as thromboembolism and pulmonary HTN, pneumothorax, granulomatous lung disease, cystic fibrosis and bronchiectasis",
        "Pleural effusion, vascular causes such as thromboembolism and pulmonary HTN, pneumothorax, granulomatous lung disease, cystic congenital heart disease and bronchiectasis",
    ],
    "The Type I aetiology cell reads 'Fibrosis of interstitium : ILD', 'Fluid in interstitium, Pulmonary edema, ARDS', 'Exudate, Consolidation (Pneumonia)', 'Impaired alveolocapillary membrane unit ↓ surface area : Emphysema volume', then vascular causes, pneumothorax, granulomatous lung disease, cystic congenital heart disease and bronchiectasis.",
)

add(
    S1, 230, "recall",
    "Bronchial asthma appears as a special Type I entry with a bracketed explanation. Which statements are printed?",
    "Airway disease with normal parenchyma → absent CO2 retention, and ↓PaO2 with (N)PaCO2 but ↑DLCO (normal diffusion)",
    [
        "Airway disease with abnormal parenchyma → present CO2 retention, and ↓PaO2 with ↑PaCO2 but ↓DLCO",
        "Airway disease with normal parenchyma → absent CO2 retention, and ↓PaO2 with (N)PaCO2 but ↓DLCO (impaired diffusion)",
        "Interstitial disease with normal airways → absent CO2 retention, and ↓PaO2 with (N)PaCO2 but ↑DLCO",
    ],
    "The asthma entry reads 'Airway disease (Normal parenchyma, → Absent CO2 retention)' and '↓PaO2, (N) PaCO2, ↑DLCO (normal diffusion)'. Because the alveolo-capillary membrane is spared, diffusion is preserved and CO2 is not retained.",
)

add(
    S1, 230, "truefalse",
    "TRUE or FALSE about the Type I definition printed on page 230.",
    "True — Type I failure is an oxygenation failure with a normal PaCO2, and the CO diffusion potential is quoted as 150 times",
    [
        "False — Type I failure is a ventilatory failure with a raised PaCO2",
        "False — the CO diffusion potential is quoted as 15 times on this page",
        "True — Type I failure always requires a raised PAO2 − PaO2 with a raised PaCO2",
    ],
    "The Type I column reads 'Oxygenation failure', 'No hypercapnia' and 'High (150 times) diffusion potential of CO', with 'Normal PaCO2' in the pressure column. A raised CO2 would make it Type II or III.",
)


add(
    S1, 230, "scenario",
    "A patient with severe asthma has PaO2 55 mmHg, a normal PaCO2 and normal diffusion. Using the page 230 asthma entry, why is CO2 not retained?",
    "Airway disease with normal parenchyma means absent CO2 retention, so PaO2 falls with (N)PaCO2 and ↑DLCO",
    [
        "Airway disease with abnormal parenchyma means present CO2 retention, so PaO2 falls with ↑PaCO2 and ↓DLCO",
        "Airway disease with normal parenchyma means present CO2 retention, so PaO2 falls with ↑PaCO2 and ↑DLCO",
        "Interstitial disease with normal airways means absent CO2 retention, so PaO2 falls with (N)PaCO2 and ↓DLCO",
    ],
    "The asthma rows read 'Airway disease (Normal parenchyma, → Absent CO2 retention)' and '↓PaO2, (N)PaCO2, ↑DLCO (normal diffusion)'. Because the alveolo-capillary membrane is intact, CO2 diffuses freely and the DLCO is preserved.",
)


# ---------------------------------------------------------------- Unit 2: p231
add(
    S2, 231, "recall",
    "Which Type III chain and aetiology pair are printed on page 231?",
    "Oxygenation failure → parenchymal damage → ventilatory failure, with ILD acting through ↓diffusion and ARDS through ↓lung compliance",
    [
        "Hypoventilation → parenchymal damage → oxygenation failure, with ILD acting through ↓compliance and ARDS through ↓diffusion",
        "Oxygenation failure → parenchymal damage → ventilatory failure, with ILD acting through ↓compliance and ARDS through ↓diffusion",
        "Ventilatory failure → parenchymal damage → oxygenation failure, with ILD acting through ↓diffusion and ARDS through ↑lung compliance",
    ],
    "The Type III row reads 'Oxygenation failure → Parenchymal damage → ventilatory failure', and the aetiology cell brackets 'ILD : ↓Diffusion' and 'ARDS : ↓Lung compliance' to 'Type 1 → Type 3 as disease progresses'. Type III therefore carries both a low PaO2 and a high PaCO2 with a raised gradient.",
)

add(
    S2, 231, "recall",
    "Which Type IV mechanism and causes are printed on page 231?",
    "Hypotension → ↓perfusion of respiratory muscles, with cardiogenic, hypovolemic and septic shock as causes",
    [
        "Hypertension → ↑perfusion of respiratory muscles, with cardiogenic, hypovolemic and septic shock as causes",
        "Hypotension → ↓diffusion across the membrane, with cardiogenic, hypovolemic and septic shock as causes",
        "Hypotension → ↓perfusion of respiratory muscles, with obstructive, neurogenic and anaphylactic shock as causes",
    ],
    "The Type IV row reads 'Hypotension → ↓Perfusion of respiratory muscles' with the partial-pressure cell printed as a dash, and aetiology 'Cardiogenic shock, Hypovolemic shock, Septic shock'. The failure is of the respiratory pump, so pressures are not characteristic.",
)

add(
    S2, 231, "recall",
    "The 'Type-3 respiratory failure' note on page 231 is set in anaesthesiology. Which mechanism is printed?",
    "↓Functional residual capacity (residual volume + expiratory reserve volume) → collapse (post-op atelectasis)",
    [
        "↑Functional residual capacity (residual volume + expiratory reserve volume) → collapse (post-op atelectasis)",
        "↓Functional residual capacity (tidal volume + inspiratory reserve volume) → collapse (post-op atelectasis)",
        "↓Vital capacity (residual volume + expiratory reserve volume) → collapse (post-op pneumonia)",
    ],
    "The note reads 'Type-3 Respiratory Failure : in Anesthesiology' with 'Pathology : ↓ Functional Residual Capacity (Residual Volume + Expiratory Reserve Volume)' leading to 'Collapse (Post op Atelectasis)'. Note the page uses 'Type-3' here for a perioperative mechanism distinct from the Type III parenchymal row above it (recorded in the caveat file).",
)

add(
    S2, 231, "recall",
    "Which four causes of the anaesthesiology type-3 failure are printed?",
    "Supine position/obese/ascites, residual effects of anaesthesia, upper abdominal incision and airway secretions",
    [
        "Prone position/obese/ascites, residual effects of anaesthesia, lower abdominal incision and airway secretions",
        "Supine position/obese/ascites, residual effects of anaesthesia, upper abdominal incision and pulmonary embolism",
        "Supine position/cachexia/ascites, muscle relaxants, upper abdominal incision and airway secretions",
    ],
    "The aetiology list reads 'supine position, Obese, Ascites', 'Residual effects of Anesthesia', 'upper abdominal incision' and 'Airway secretions'. All four reduce FRC or impede its restoration after surgery.",
)

add(
    S2, 231, "numeric",
    "Which V/Q ratio values are printed under the hypoxemic-failure clinical approach?",
    "Normal 0.8; upper zone > 1 (non-dependent, ↓↓V and ↓↓Q); lower zone < 1 (dependent area)",
    [
        "Normal 1.0; upper zone > 1 (non-dependent, ↓↓V and ↓↓Q); lower zone < 1 (dependent area)",
        "Normal 0.8; upper zone < 1 (non-dependent, ↓↓V and ↓↓Q); lower zone > 1 (dependent area)",
        "Normal 0.8; upper zone > 1 (dependent area); lower zone < 1 (non-dependent area)",
    ],
    "The page prints 'Normal : 0.8', 'upper zone : >1 (Non-dependent area → ↓↓V, ↓↓Q)' and 'Lower zone : <1 (Dependent area)', adding that the ratio 'Indicates overall respiratory functional status of lung' and plays a role in type 1 failure.",
)

add(
    S2, 231, "match",
    "Match each physiology with its printed row in the ventilation table — 1) Dead space physiology 2) Shunt physiology 3) Normal matching … A) Ventilation absent, perfusion present, V/Q zero B) V/Q 0.8 C) Ventilation present, perfusion absent, V/Q infinite",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "The table reads: dead space — ventilation present, perfusion absent, V/Q ∞, aetiology pulmonary embolism and pulmonary vascular disease; shunt — ventilation absent, perfusion present, V/Q zero, aetiology intracardiac/vascular shunts. Normal matching carries the V/Q of 0.8 printed above the table.",
)

add(
    S2, 231, "truefalse",
    "TRUE or FALSE about the Type III and Type IV rows on page 231.",
    "True — Type III has ↓PaO2 with ↑PaCO2 and ↑PAO2 − PaO2, while the Type IV partial-pressure cell is printed as a dash",
    [
        "False — Type III has ↓PaO2 with normal PaCO2 and a normal gradient",
        "False — Type IV is printed with a full set of partial pressures",
        "True — Type IV is caused by parenchymal damage rather than by shock",
    ],
    "The Type III pressure cell reads '↓PaO2, ↑PaCO2, ↑PAO2 − PaO2', whereas the Type IV cell contains only a dash, consistent with a perfusion failure of the respiratory muscles rather than a gas-exchange defect.",
)


# ---------------------------------------------------------------- Unit 3: p232
add(
    S3, 232, "recall",
    "The hypoxemic-failure flowchart begins with ↓PaO2 and three first-level branches. Which three are printed?",
    "V/Q mismatch (Type I respiratory failure, diffusion abnormality), V/Q = 0 shunt and V/Q = ∞ dead space",
    [
        "V/Q mismatch (Type I respiratory failure, diffusion abnormality), V/Q = 0 dead space and V/Q = ∞ shunt",
        "V/Q mismatch (Type II respiratory failure), V/Q = 1 shunt and V/Q = 0 dead space",
        "Diffusion abnormality (Type III), V/Q = 0 shunt and V/Q = ∞ dead space",
    ],
    "The three arrows from ↓PaO2 read 'V/Q mismatch : Type-I respiratory failure (Diffusion abnormality)', 'V/Q = 0 Shunt' and 'V/Q = ∞ Dead space'. The shunt and dead space branches reproduce page 209's definitions exactly.",
)

add(
    S3, 232, "match",
    "Match each flowchart terminal with its printed label — 1) Raised CO2 with a normal gradient 2) Raised CO2 with a raised gradient 3) Normal CO2 with a raised gradient not corrected by oxygen 4) Normal CO2 with a normal gradient … A) Shunt B) Hypoventilation (Type II) C) High altitude D) Hypoventilation plus another mechanism (Type III)",
    "1-B, 2-D, 3-A, 4-C",
    ["1-B, 2-D, 3-C, 4-A", "1-D, 2-B, 3-A, 4-C", "1-B, 2-A, 3-D, 4-C"],
    "The chart prints 'Hypoventilation (Type II)', 'Hypoventilation + Another mechanism (Type III)', then under Type I the oxygen-response test ends at 'v/Q : mismatch' (corrects) or 'Shunt' (does not correct), and 'High Altitude' sits on the branch with no gradient.",
)

add(
    S3, 232, "recall",
    "According to the page 232 flowchart, how is a Type I hypoxaemia separated into V/Q mismatch versus shunt?",
    "Give oxygen: if the low PaO2 is corrected it is V/Q mismatch; if it is not corrected it is shunt",
    [
        "Give oxygen: if the low PaO2 is corrected it is shunt; if it is not corrected it is V/Q mismatch",
        "Measure the A-a gradient: if raised it is shunt; if normal it is V/Q mismatch",
        "Measure the PaCO2: if raised it is shunt; if normal it is V/Q mismatch",
    ],
    "The Type I branch runs 'Low PO2 Corrected with O2 → Yes → v/Q : mismatch' and '→ No → Shunt'. Shunted blood never contacts ventilated alveoli, so added oxygen cannot reach it.",
)

add(
    S3, 232, "fillup",
    "On the page 232 flowchart, a low PaO2 with a normal gradient and no CO2 retention leads to the terminal labelled ______.",
    "High altitude",
    ["Shunt", "Dead space", "Hypoventilation"],
    "The far-right branch of the Type I limb ends at 'High Altitude'. There the inspired oxygen pressure itself is low, so the gradient stays normal — unlike shunt or V/Q mismatch.",
)

add(
    S3, 232, "recall",
    "The hypercapnic-failure flowchart at the foot of page 232 begins with ↑PaCO2 and splits on the A-a gradient. Which two terminals are printed?",
    "Normal gradient → hypoventilation → generator, pumps, effector organ; increased gradient → V/Q mismatch, eg ARDS and ILD",
    [
        "Increased gradient → hypoventilation → generator, pumps, effector organ; normal gradient → V/Q mismatch, eg ARDS and ILD",
        "Normal gradient → shunt; increased gradient → dead space, eg ARDS and ILD",
        "Normal gradient → hypoventilation → generator and pumps only; increased gradient → diffusion defect, eg pulmonary embolism",
    ],
    "The chart reads '↑PaCO2 → PAO2 − PaO2', then 'Normal → Hypoventilation → Generator, Pumps, Effector organ' and 'Increased → v/Q mismatch eg : ARDS ILD'. The generator/pump/effector trio matches the Type II aetiology list on page 230.",
)

add(
    S3, 232, "scenario",
    "A patient has PaO2 50 mmHg, a normal PaCO2 and a raised A-a gradient; the PaO2 does not improve on 100% oxygen. Where does the page 232 algorithm place this?",
    "Type I respiratory failure with a shunt",
    [
        "Type I respiratory failure with V/Q mismatch",
        "Type II respiratory failure from hypoventilation",
        "Type III respiratory failure with a high altitude mechanism",
    ],
    "The Type I limb splits on oxygen responsiveness: corrected PaO2 means V/Q mismatch, uncorrected means 'Shunt'. A normal PaCO2 keeps the case out of the Type II and III Hypoventilation terminals.",
)


# ---------------------------------------------------------------- Unit 4: p233
add(
    S4, 233, "recall",
    "Which synonyms for ARDS are printed at the top of page 233?",
    "Shock lung, acute lung injury, DAD, blast lung and acute alveolar injury",
    [
        "Shock lung, acute lung injury, DAD, blast lung and acute interstitial pneumonia",
        "Stiff lung, acute lung injury, DAD, blast lung and acute alveolar injury",
        "Shock lung, chronic lung injury, DAD, blast lung and acute alveolar injury",
    ],
    "The line reads 'AKA shock lung/acute lung injury/DAD/blast lung/acute alveolar injury.' Acute interstitial pneumonia is a separate idiopathic interstitial pneumonia listed on page 236, not a synonym for ARDS.",
)

add(
    S4, 233, "numeric",
    "Which three 1992 AECC criteria carry numbers on page 233?",
    "PCWP < 18 mmHg (measuring left atrial pressure), bilateral alveolar and interstitial infiltrates, and PaO2/FiO2 < 200",
    [
        "PCWP < 18 mmHg, unilateral alveolar infiltrates, and PaO2/FiO2 < 300",
        "PCWP > 18 mmHg, bilateral alveolar and interstitial infiltrates, and PaO2/FiO2 < 200",
        "PCWP < 15 mmHg, bilateral alveolar and interstitial infiltrates, and PaO2/FiO2 < 200",
    ],
    "The AECC block reads 'Non cardiogenic pulmonary edema' with 'PCWP : <18 mm Hg (Suggestive of no cardiac abnormality)', then 'Bilateral alveolar and interstitial lung infiltrates on x-ray' and 'PaO2/FiO2 < 200'. The wedge pressure must be low, confirming a non-cardiogenic cause.",
)

add(
    S4, 233, "numeric",
    "What limitation and mortality figures are printed for ARDS on page 233?",
    "Only 20% of patients meet the ARDS criteria; mortality 70–75% with post-ARDS residual disability",
    [
        "Only 20% of patients meet the ARDS criteria; mortality 30–40% with post-ARDS residual disability",
        "Only 50% of patients meet the ARDS criteria; mortality 70–75% with post-ARDS residual disability",
        "Only 20% of patients meet the ARDS criteria; mortality 70–75% with no residual disability",
    ],
    "The limitations line reads 'Only 20% patients meet ARDS criteria', and the note gives 'mortality : 70–75%' plus 'Post ARDS residual disability present'. Survivors are left with functional impairment, not a full recovery.",
)

add(
    S4, 233, "recall",
    "Which four Berlin 2012 criteria are numbered on page 233?",
    "Acute onset within 1 week of the insult, bilateral infiltrates not explained by effusion/collapse/nodules, non-cardiogenic with a normal ECHO, and oxygenation measured when PEEP ≥ 5 cm of H2O",
    [
        "Acute onset within 1 month of the insult, bilateral infiltrates not explained by effusion/collapse/nodules, non-cardiogenic with a normal ECHO, and oxygenation measured when PEEP ≥ 5 cm of H2O",
        "Acute onset within 1 week of the insult, unilateral infiltrates not explained by effusion/collapse/nodules, cardiogenic with an abnormal ECHO, and oxygenation measured when PEEP ≥ 10 cm of H2O",
        "Acute onset within 1 week of the insult, bilateral infiltrates, non-cardiogenic with a normal ECHO, and oxygenation measured on room air without PEEP",
    ],
    "The Berlin block reads '1. Acute onset : within 1 week of clinical insult/worsening respiratory symptoms', '2. Chest x-ray : Bilateral alveolar/Interstitial infiltrates not explained by effusion/collapse/nodules', '3. Non cardiogenic : Normal ECHO' and '4. Oxygenation :' with the brace 'when PEEP ≥ 5 cm of H2O'. The timing is one week, not one month.",
)

add(
    S4, 233, "match",
    "Match each Berlin severity grade with its printed PaO2/FiO2 range — 1) Mild 2) Moderate 3) Severe … A) < 100 B) 100–200 C) 200–300",
    "1-C, 2-B, 3-A",
    ["1-A, 2-B, 3-C", "1-C, 2-A, 3-B", "1-B, 2-C, 3-A"],
    "The severity table reads 'mild — 200 – 300', 'moderate — 100 – 200' and 'severe — < 100'. Lower ratios indicate more severe disease, so the grades run from the highest range to the lowest.",
)

add(
    S4, 233, "recall",
    "Which three factors preventing pulmonary edema are printed at the foot of page 233?",
    "Retained intravascular protein, interstitial lymphatics draining fluid, and tight junctions between epithelial cells",
    [
        "Lost intravascular protein, interstitial lymphatics draining fluid, and tight junctions between epithelial cells",
        "Retained intravascular protein, blocked interstitial lymphatics, and tight junctions between endothelial cells",
        "Retained intravascular protein, interstitial lymphatics draining fluid, and loose junctions between epithelial cells",
    ],
    "The three bullets read 'Retained intravascular protein', 'Interstitial lymphatics drains fluid' and 'Tight junctions between epithelial cells'. ARDS breaks all three, which is why protein-rich fluid floods the alveolus.",
)


add(
    S4, 233, "scenario",
    "A ventilated patient has ARDS onset three days after a urinary tract infection, bilateral infiltrates, a normal ECHO and PaO2/FiO2 of 150 on PEEP 8 cm H2O. Using the Berlin table, how is this graded and which AECC threshold has changed?",
    "Moderate ARDS (100–200); the Berlin definition replaces the single AECC PaO2/FiO2 < 200 cut-off with three graded ranges measured on PEEP ≥ 5 cm H2O",
    [
        "Mild ARDS (200–300); the Berlin definition raises the AECC cut-off from 200 to 300 without grading",
        "Severe ARDS (< 100); the Berlin definition is identical to the AECC cut-off of 200",
        "Moderate ARDS (100–200); the Berlin definition removes the PEEP requirement entirely",
    ],
    "The Berlin severity table reads 'mild 200 – 300', 'moderate 100 – 200' and 'severe < 100', with the brace 'when PEEP ≥ 5 cm of H2O'. The AECC instead used a single 'PaO2/FiO2 < 200' threshold, which is why it captured only about 20% of patients.",
)

add(
    S4, 233, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed as factors preventing pulmonary edema on page 233, one is not:",
    "Leaky junctions between epithelial cells",
    [
        "Retained intravascular protein",
        "Interstitial lymphatics draining fluid",
        "Tight junctions between epithelial cells",
    ],
    "The three protective factors are retained intravascular protein, interstitial lymphatics draining fluid, and tight junctions between epithelial cells. Leaky junctions are the pathological change of ARDS, not a protective mechanism.",
)


# ---------------------------------------------------------------- Unit 5: p234
add(
    S5, 234, "recall",
    "Which primary ARDS causes are printed on page 234?",
    "Pulmonary sepsis, massive blood transfusion, acute pancreatitis, TRALI, smoke inhalation, drowning and post surgery",
    [
        "Non-pulmonary sepsis, massive blood transfusion, acute pancreatitis, TRALI, smoke inhalation, drowning and post surgery",
        "Pulmonary sepsis, massive blood transfusion, acute pancreatitis, TRALI, smoke inhalation, drowning and major burns",
        "Pulmonary sepsis, minor blood transfusion, chronic pancreatitis, TRALI, smoke inhalation, drowning and post surgery",
    ],
    "The primary list reads 'Pulmonary sepsis', 'massive blood transfusion', 'Acute pancreatitis', 'Transfusion associated lung injury (TRALI)', 'Smoke inhalation', 'Drowning' and 'Post surgery'. Non-pulmonary sepsis and major trauma/burns are the secondary causes printed below it.",
)

add(
    S5, 234, "recall",
    "Which secondary ARDS causes are printed on page 234?",
    "Non pulmonary sepsis (UTI, surgical site infection) and major trauma/burns",
    [
        "Pulmonary sepsis and minor trauma/burns",
        "Non pulmonary sepsis and acute pancreatitis",
        "Non pulmonary sepsis and massive blood transfusion",
    ],
    "The secondary block reads 'Non pulmonary sepsis (UTI, surgical site infection)' and 'major trauma/burns'. Acute pancreatitis and massive transfusion sit in the primary block above.",
)

add(
    S5, 234, "recall",
    "Which mediator sequence does the page 234 pathogenesis diagram print after alveolar epithelial injury?",
    "Inflammatory mediators (IL-1, IL-6, TNF α), cytokines → neutrophil recruitment",
    [
        "Inflammatory mediators (IL-2, IL-4, TNF β), cytokines → eosinophil recruitment",
        "Inflammatory mediators (IL-1, IL-6, TNF α), cytokines → macrophage recruitment only",
        "Inflammatory mediators (IL-10, IL-6, TNF α), cytokines → neutrophil recruitment",
    ],
    "The vertical chain reads 'Toxin, sepsis → Alveolar epithelial injury → Inflammatory mediators (IL 1, IL 6, TNF α), cytokines → Neutrophil recruitment', alongside a capillary endothelial injury limb feeding exudation. The interleukins are 1 and 6 with TNF alpha.",
)

add(
    S5, 234, "match",
    "Match each consequence of proteinaceous alveolar fluid with its printed label — 1) Loss of surfactant 2) ↓Compliance 3) Impaired gas exchange … A) Collapse B) Impaired gas exchange itself C) Reduced compliance itself",
    "1-A, 2-C, 3-B",
    ["1-B, 2-C, 3-A", "1-A, 2-B, 3-C", "1-C, 2-A, 3-B"],
    "The three arrows from 'Alveolar space proteinaceous fluid + debris' read 'Loss of surfactant → Collapse', '↓Compliance' and 'Impaired gas exchange'. Surfactant loss is the only one with a further downstream arrow, to collapse.",
)

add(
    S5, 234, "numeric",
    "Which day ranges are printed for the three pathological phases of ARDS?",
    "Acute exudative phase 7 days, fibroproliferative phase 7–14 days, fibrotic vasoconstriction 14–21 days",
    [
        "Acute exudative phase 14 days, fibroproliferative phase 7–14 days, fibrotic vasoconstriction 21–28 days",
        "Acute exudative phase 7 days, fibroproliferative phase 14–21 days, fibrotic vasoconstriction 21–28 days",
        "Acute exudative phase 3 days, fibroproliferative phase 7–14 days, fibrotic vasoconstriction 14–21 days",
    ],
    "The phase list reads '1. Acute exudative phase (7 days)', '2. Fibroproliferative phase (7–14 days)' and '3. Fibrotic vasoconstriction (14–21 days)'. The phases overlap rather than following one another cleanly.",
)

add(
    S5, 234, "recall",
    "Which finding is called the hallmark of the acute exudative phase, and what alternative name is given?",
    "Eosinophilic hyaline membrane deposition — AKA hyaline membrane disease",
    [
        "Eosinophilic hyaline membrane deposition — AKA hyaline arteriolosclerosis",
        "Neutrophilic hyaline membrane deposition — AKA hyaline membrane disease",
        "Eosinophilic hyaline membrane deposition — AKA diffuse alveolar haemorrhage",
    ],
    "The phase 1 entry reads 'Diffuse alveolar damage (DAD) : Interstitial + alveolar edema', then 'Eosinophilic hyaline membrane deposition — Hallmark — a.k.a. hyaline membrane disease.' The membrane is eosinophilic, not neutrophilic.",
)

add(
    S5, 234, "truefalse",
    "TRUE or FALSE about the respiratory-failure type printed in the ARDS note on page 234.",
    "True — the note says type 1 (most common) or type 3 respiratory failure is seen",
    [
        "False — the note says only type 2 respiratory failure is seen",
        "False — the note says type 4 respiratory failure is the most common",
        "True — the note says type 2 failure is the most common pattern in ARDS",
    ],
    "The note reads 'Type 1 (m/c) or Type 3 respiratory failure seen.' This matches the Type I table on page 230 and the Type III parenchymal row on page 231, where ARDS acts through reduced compliance.",
)


# ---------------------------------------------------------------- Unit 6: p235
add(
    S6, 235, "recall",
    "Which clinical features of ARDS are printed on page 235?",
    "Rapid onset dyspnea, hypoxemia, bilateral crackles with diffuse pulmonary infiltrates, tachypnea/tachycardia/diaphoresis, and pulmonary hypertension from hypoxemic vasoconstriction",
    [
        "Gradual onset dyspnea, hypoxemia, unilateral crackles with a focal infiltrate, bradycardia and systemic hypotension",
        "Rapid onset dyspnea, hypoxemia, bilateral crackles with diffuse pulmonary infiltrates, tachypnea/tachycardia/diaphoresis, and pulmonary hypotension from hypoxemic vasodilatation",
        "Rapid onset pleuritic pain, hypercarbia, bilateral crackles, bradycardia and pulmonary hypertension",
    ],
    "The list reads 'Rapid onset dyspnoea', 'Hypoxemia', 'Bilateral crackles : Diffuse pulmonary infiltrates', 'Tachypnoea, tachycardia, diaphoresis' and 'Pulmonary hypertension : D/t hypoxemic vasoconstriction'. The vascular response to hypoxia is vasoconstriction, not vasodilatation.",
)

add(
    S6, 235, "recall",
    "Which four mechanical-ventilation strategies are printed as the mainstay of ARDS treatment?",
    "Inverse ratio ventilation with inspiration, prone ventilation, permissive hypercapnia, and mechanical ventilation itself as the mainstay",
    [
        "Inverse ratio ventilation with expiration, supine ventilation, permissive hypercapnia, and mechanical ventilation itself as the mainstay",
        "Inverse ratio ventilation with inspiration, prone ventilation, permissive hypocapnia, and mechanical ventilation itself as the mainstay",
        "Conventional ratio ventilation, prone ventilation, permissive hypercapnia, and high tidal volume as the mainstay",
    ],
    "The block reads 'mechanical ventilation : mainstay of treatment', 'Inverse ratio ventilation with inspiration', 'Prone ventilation' and 'Permissive hypercapnia'. Permissive hypercapnia accepts a raised CO2 in exchange for protecting the lung from over-distension.",
)

add(
    S6, 235, "match",
    "Match each form of VILI with its printed pathogenesis — 1) Volume trauma 2) Baro trauma 3) Atelecto trauma … A) Collapse and decollapse during tidal breathing B) ↑Transpulmonary pressure C) ↑Lung volume causing alveolar injury",
    "1-C, 2-B, 3-A",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "The table reads 'volume trauma — ↑lung volume → alveolar injury', 'Baro trauma — ↑transpulmonary pressure' and 'Atelecto trauma — Collapse and decollapse during tidal breathing'. Each has its own protective strategy in the next column.",
)

add(
    S6, 235, "match",
    "Match each form of VILI with the protective strategy printed against it — 1) Volume trauma 2) Baro trauma 3) Atelecto trauma … A) High positive end expiratory pressure B) Low tidal volume ventilation (high frequency ventilation) C) Low plateau pressure (low driving pressure)",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The treatment column reads 'Low tidal volume ventilation (High frequency ventilation)' for volume trauma, 'Low plateau pressure (low driving pressure)' for baro trauma and 'High positive end expiratory pressure (PEEP)' for atelecto trauma. Each strategy neutralises the specific mechanical stress named beside it.",
)

add(
    S6, 235, "management",
    "Which ventilation settings would the page 235 VILI table pair with a patient showing cyclical alveolar collapse?",
    "High positive end expiratory pressure, because the mechanism is atelecto trauma — collapse and decollapse during tidal breathing",
    [
        "Low plateau pressure, because the mechanism is baro trauma from a raised transpulmonary pressure",
        "Low tidal volume ventilation, because the mechanism is volume trauma from a raised lung volume",
        "Permissive hypercapnia alone, with no change in PEEP",
    ],
    "The third row pairs 'Atelecto trauma — Collapse and decollapse during tidal breathing' with 'High positive end expiratory pressure (PEEP)'. PEEP splints open the recruited alveoli and prevents repeated derecruitment.",
)

add(
    S6, 235, "recall",
    "Which six-item differential of acute breathlessness closes page 235, and which is marked as the default?",
    "Pulmonary edema (unless proven otherwise), pulmonary embolism, pneumothorax, acute exacerbation of asthma, aortic dissection and myocardial infarction",
    [
        "Pulmonary edema (unless proven otherwise), pulmonary embolism, pneumothorax, acute exacerbation of COPD, aortic stenosis and myocardial infarction",
        "Pneumonia (unless proven otherwise), pulmonary embolism, pneumothorax, acute exacerbation of asthma, aortic dissection and pericarditis",
        "Pulmonary edema (unless proven otherwise), pulmonary embolism, pleural effusion, acute exacerbation of asthma, aortic dissection and myocardial infarction",
    ],
    "The note reads 'D/d of acute breathlessness : Pulmonary edema (Unless proven otherwise), Pulmonary embolism, Pneumothorax, Acute exacerbation of asthma, Aortic dissection, myocardial infarction.' Pulmonary oedema heads the list as the default diagnosis, mirroring the ARDS content of the chapter.",
)


GUIDES = {
    S1: (
        "Definition of Respiratory Failure, Hypoxemic/Hypercapnic Thresholds, the Partial-Pressure Abbreviation Box and the Type I Table (Diffusion Failure, CO Diffusion Potential, Etiology List Including the Asthma Exception)",
        "Respiratory failure (p230) is the pulmonary system's inability to meet the body's demands: hypoxemic when PaO2 < 60 mmHg on room air with SpO2 < 90%, hypercapnic when PaCO2 > 50 mmHg on room air. The box defines PAO2 as alveolar oxygen, PaO2 as arterial oxygen (normal ~97 mmHg), PaCO2 as arterial carbon dioxide (normal ~40 mmHg) and PAO2 − PaO2 as the alveolocapillary oxygen gradient.\n"
        "Type I is impaired diffusion causing oxygenation failure, with the high (150 times) diffusion potential of CO and no hypercapnia; pressures are ↓PaO2, normal PaCO2 and ↑PAO2 − PaO2. Causes are interstitial fibrosis/ILD, fluid in the interstitium with pulmonary edema or ARDS, exudate/consolidation in pneumonia, the reduced surface area/volume of emphysema, vascular disease such as thromboembolism and pulmonary HTN, pneumothorax, granulomatous lung disease, cystic congenital heart disease and bronchiectasis.\n"
        "Bronchial asthma is entered separately: airway disease with normal parenchyma means absent CO2 retention, so ↓PaO2 with (N)PaCO2 but ↑DLCO, reflecting normal diffusion.",
    ),
    S2: (
        "Type III (Parenchymal Damage) and Type IV (Shock) Rows, the Anaesthesiology 'Type-3' FRC Note, the V/Q Ratio Zones and the Dead-Space-vs-Shunt Table",
        "Type III (p231) runs oxygenation failure → parenchymal damage → ventilatory failure with ↓PaO2, ↑PaCO2 and ↑PAO2 − PaO2; ILD acts by ↓diffusion and ARDS by ↓lung compliance, with the brace showing type 1 becoming type 3 as disease progresses. Type IV is hypotension → ↓perfusion of respiratory muscles with a dash for partial pressures, caused by cardiogenic, hypovolemic or septic shock.\n"
        "The anaesthesiology 'Type-3' note describes ↓functional residual capacity (residual volume + expiratory reserve volume) causing collapse and post-op atelectasis, with causes of supine position/obesity/ascites, residual anaesthesia, upper abdominal incision and airway secretions.\n"
        "The hypoxemic approach uses V/Q matching: normal 0.8, upper zone > 1 (non-dependent, ↓↓V and ↓↓Q) and lower zone < 1 (dependent). Dead space physiology has ventilation present, perfusion absent and V/Q ∞ (pulmonary embolism, pulmonary vascular disease); shunt physiology has ventilation absent, perfusion present and V/Q zero (intracardiac/vascular shunts).",
    ),
    S3: (
        "The Two Flowcharts: Hypoxemic Failure Branches (V/Q Mismatch, Shunt, Dead Space, Type II vs Type III, Oxygen-Responsiveness, High Altitude) and Hypercapnic Failure Branches",
        "The hypoxemic flowchart (p232) starts from ↓PaO2 and branches to V/Q mismatch (Type I, diffusion abnormality), V/Q = 0 shunt and V/Q = ∞ dead space.\n"
        "It then splits on PaCO2: a raised CO2 with a normal gradient ends in hypoventilation (Type II), and with a raised gradient in hypoventilation plus another mechanism (Type III). Without CO2 retention, a raised gradient with oxygen-correctable hypoxaemia means V/Q mismatch and uncorrectable hypoxaemia means shunt, while a normal gradient leads to high altitude.\n"
        "The hypercapnic flowchart starts from ↑PaCO2 and splits on the A-a gradient: normal → hypoventilation → generator, pumps, effector organ; increased → V/Q mismatch, eg ARDS and ILD.",
    ),
    S4: (
        "ARDS Synonyms, the 1992 AECC Criteria, Limitations and Mortality, the Berlin 2012 Definition with PEEP and Severity Table and the Factors Preventing Pulmonary Edema",
        "ARDS (p233) is AKA shock lung, acute lung injury, DAD, blast lung and acute alveolar injury. The 1992 AECC criteria are non-cardiogenic pulmonary edema with PCWP < 18 mmHg (the wedge measures left atrial pressure and suggests no cardiac abnormality), bilateral alveolar and interstitial infiltrates on X-ray, and PaO2/FiO2 < 200; only 20% of patients meet them, mortality is 70–75% and post-ARDS residual disability is present.\n"
        "The Berlin 2012 definition requires acute onset within 1 week of the insult, bilateral infiltrates not explained by effusion/collapse/nodules, a non-cardiogenic cause with normal ECHO, and oxygenation measured when PEEP ≥ 5 cm of H2O — mild 200–300, moderate 100–200, severe < 100.\n"
        "Pulmonary edema is prevented by retained intravascular protein, interstitial lymphatics draining fluid, and tight junctions between epithelial cells.",
    ),
    S5: (
        "ARDS Etiology (Primary and Secondary), the Toxin-to-Hyaline-Membrane Pathogenesis Chain, Alveolar Consequences and the Three Pathological Phases",
        "Primary ARDS (p234) follows pulmonary sepsis, massive blood transfusion, acute pancreatitis, TRALI, smoke inhalation, drowning or post surgery; secondary ARDS follows non-pulmonary sepsis (UTI, surgical site infection) or major trauma/burns.\n"
        "Pathogenesis: toxin/sepsis → alveolar epithelial injury → inflammatory mediators (IL-1, IL-6, TNF α) and cytokines → neutrophil recruitment, with capillary endothelial injury causing exudation of fluid and protein; the alveolar space fills with proteinaceous fluid and debris, causing loss of surfactant → collapse, ↓compliance and impaired gas exchange. Type 1 (most common) or type 3 respiratory failure is seen.\n"
        "Phases: acute exudative phase (7 days) with diffuse alveolar damage, interstitial and alveolar edema and eosinophilic hyaline membrane deposition as the hallmark (AKA hyaline membrane disease); fibroproliferative phase (7–14 days); fibrotic vasoconstriction (14–21 days).",
    ),
    S6: (
        "ARDS Clinical Features, Mechanical Ventilation Strategies, the VILI Table (Volume, Baro and Atelecto Trauma) and the Differential of Acute Breathlessness",
        "Clinical features (p235): rapid onset dyspnea, hypoxemia, bilateral crackles with diffuse pulmonary infiltrates, tachypnea, tachycardia, diaphoresis, and pulmonary hypertension from hypoxemic vasoconstriction.\n"
        "Management is mechanical ventilation as the mainstay, with inverse ratio ventilation with inspiration, prone ventilation and permissive hypercapnia.\n"
        "VILI: volume trauma (↑lung volume → alveolar injury) is treated with low tidal volume ventilation (high frequency ventilation); baro trauma (↑transpulmonary pressure) with low plateau pressure (low driving pressure); atelecto trauma (collapse and decollapse during tidal breathing) with high PEEP.\n"
        "The differential of acute breathlessness is pulmonary edema (unless proven otherwise), pulmonary embolism, pneumothorax, acute exacerbation of asthma, aortic dissection and myocardial infarction.",
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
