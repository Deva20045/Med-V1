#!/usr/bin/env python3
"""Generate Chapter 35: Pulmonary Hypertension (Book p213–217).

Every question is anchored to a specific line, table cell, murmur description or
figure label of uploads/02.pdf sheets 96–100 (Book pages 213–217), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 35
TITLE = "Pulmonary Hypertension"
PAGES = "213-217"

S1 = "Ohm's Law Applied to the Pulmonary Circulation (PAP − LAP = CO × PVR), the Five WHO Classes, Class 1 PAH Features and the Class-to-Affected-Vessel Figure"
S2 = "PAH vs Systemic HTN Mortality Logic, Definition (Mean PAP > 20 mmHg), Cor Pulmonale, Wood-Unit PVR Split, Plexiform Arteriolopathy & Secondary Causes (BMPR2 to Appetite Suppressants)"
S3 = "Pathology Triad, Endothelin/NO/Prostacyclin Pathway Treatment Table, Clinical Presentation and the RV Dilatation and RV Failure Sign Chains"
S4 = "PA Catheterisation Gold Standard, the Three PAH Murmurs (Carvallo, Ejection Systolic, Graham Steell), CXR Findings, PA Aneurysm Causes and ECG RVH Criteria"
S5 = "Investigations to Exclude Other Causes (PFT, ECHO, V/Q, Sleep Study, HRCT, 6MWT), the Vaso-Reactivity Test, General Treatment and the NYHA-Stratified Drug and Surgical Table"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(35000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(35100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p213
add(
    S1, 213, "match",
    "Page 213 maps Ohm's law onto the pulmonary circulation. Match each electrical term with its printed pulmonary equivalent — 1) Voltage 2) Current 3) Resistance … A) Cardiac output B) Pulmonary vascular resistance C) Pressure difference between pulmonary artery and left atrium",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "The page reads 'V : Voltage → Pressure difference between pulmonary artery (PAP) & left atrium (LAP)', 'I : Current → Cardiac Output (CO)' and 'R : Resistance → Pulmonary vascular resistance (PVR)'.",
)

add(
    S1, 213, "numeric",
    "Which pair of equations is printed on page 213?",
    "PAP − LAP = CO × PVR, therefore PAP = (CO × PVR) + LAP",
    [
        "PAP + LAP = CO × PVR, therefore PAP = (CO × PVR) − LAP",
        "PAP − LAP = CO ÷ PVR, therefore PAP = (CO ÷ PVR) + LAP",
        "LAP − PAP = CO × PVR, therefore PAP = (CO × PVR) − LAP",
    ],
    "Page 213 prints 'Therefore, PAP-LAP = CO x PVR' and beneath it 'PAP = (CO x PVR) + LAP'. The pulmonary artery pressure is the flow times resistance plus the downstream left atrial pressure.",
)

add(
    S1, 213, "recall",
    "Page 213 splits the causes of a raised PAP along the equation. Which split is printed?",
    "↑PVR causes class 1/3/4 pulmonary HTN; ↑LAP causes class 2 pulmonary HTN, the commonest cardiac cause being mitral stenosis",
    [
        "↑PVR causes class 2 pulmonary HTN; ↑LAP causes class 1/3/4 pulmonary HTN, the commonest cardiac cause being aortic stenosis",
        "↑PVR causes class 1/2/3 pulmonary HTN; ↑LAP causes class 4 pulmonary HTN, the commonest cardiac cause being mitral regurgitation",
        "↑CO causes class 1/3/4 pulmonary HTN; ↑LAP causes class 2 pulmonary HTN, the commonest cardiac cause being left ventricular hypertrophy",
    ],
    "The brace from 'For ↑PAP' reads '↑ PVR : Class 1/3/4 pulmonary HTN' and '↑ LAP : Cardiac cause (m/c : mitral stenosis) → Class 2 pulmonary HTN'. Resistance disease and downstream pressure disease occupy different classes.",
)

add(
    S1, 213, "recall",
    "Under Class 1 pulmonary artery hypertension, which three features are printed?",
    "Most common cause is idiopathic (hence idiopathic pulmonary HTN), very poor prognosis with median survival < 9 months, young females",
    [
        "Most common cause is hereditary, very poor prognosis with median survival < 19 months, elderly males",
        "Most common cause is idiopathic, good prognosis with median survival > 9 years, young females",
        "Most common cause is drug-induced, very poor prognosis with median survival < 9 months, elderly females",
    ],
    "Class 1 reads 'm/c cause : Idiopathic (Hence k/a Idiopathic pulmonary HTN)', 'very poor prognosis (median survival : <9 months)' and 'Young females'. The chronic thrombo-embolic class, not class 1, is the surgically responsive one.",
)

add(
    S1, 213, "match",
    "The figure at the foot of page 213 labels each class by the vessel affected. Match the class with the affected structure — 1) Class 1 PAH 2) Class 2 PVH 3) Class 3 PH 4) Class 4 CTEPH … A) Capillary affected B) Arterioles affected C) Pulmonary artery affected D) Pulmonary vein affected",
    "1-B, 2-D, 3-A, 4-C",
    ["1-B, 2-C, 3-A, 4-D", "1-D, 2-B, 3-A, 4-C", "1-A, 2-D, 3-C, 4-B"],
    "The figure labels read 'Class 1: PAH — Arterioles affected', 'Class 2: PVH (Pulmonary vein affected)', 'Class 3: PH (Capillary affected)' and 'Class 4: CTEPH (Pulmonary artery affected)'. Class 5 is labelled multifactorial.",
)

add(
    S1, 213, "recall",
    "Which description of Class 3 pulmonary hypertension is printed on page 213?",
    "Pulmonary HTN secondary to chronic lung disease, with hypoxia related pulmonary vasoconstriction, very poor prognosis and chronic bronchitis as the example",
    [
        "Pulmonary HTN secondary to left heart disease, with hypoxia related vasodilatation, good prognosis and mitral stenosis as the example",
        "Pulmonary HTN due to chronic thromboembolic disease, responsive to surgery, with chronic bronchitis as the example",
        "Pulmonary HTN secondary to chronic lung disease, with hypercarbia related vasoconstriction, very poor prognosis and emphysema as the example",
    ],
    "Class 3 reads 'Pulmonary HTN secondary to chronic lung disease', 'Hypoxia related pulmonary vasoconstriction', 'very poor prognosis' and 'eg : In chronic bronchitis'. Class 4 carries the 'responsive to surgery' label.",
)

add(
    S1, 213, "fillup",
    "The boxed note on page 213 states: hypoxia causes vasodilatation ______ in pulmonary vessels.",
    "Except",
    ["Including", "Only", "Especially"],
    "The box reads 'Hypoxia : vasodilatation except in pulmonary vessels.' Hypoxic pulmonary vasoconstriction is the exception that drives class 3 disease, and it explains why the page links chronic lung disease to a raised PVR.",
)

add(
    S1, 213, "recall",
    "Which two remaining classes complete the page 213 classification, with their printed descriptors?",
    "Class 4: chronic thrombo-embolic pulmonary HTN (responsive to surgery); Class 5: miscellaneous (multifactorial)",
    [
        "Class 4: miscellaneous (multifactorial); Class 5: chronic thrombo-embolic pulmonary HTN (responsive to surgery)",
        "Class 4: chronic thrombo-embolic pulmonary HTN (not responsive to surgery); Class 5: miscellaneous (unifactorial)",
        "Class 4: pulmonary HTN of unclear cause (responsive to surgery); Class 5: mixed connective tissue disease",
    ],
    "The last two lines read 'Class 4 : Chronic thrombo-embolic pulmonary HTN (Responsive to surgery)' and 'Class 5 : miscellaneous (Multifactorial)'. The figure adds that class 4 affects the pulmonary artery and class 5 is multifactorial.",
)


# ---------------------------------------------------------------- Unit 2: p214
add(
    S2, 214, "numeric",
    "What definition of pulmonary hypertension is printed on page 214?",
    "Mean PAP > 20 mmHg at rest with right heart catheterisation",
    [
        "Mean PAP > 25 mmHg at rest with right heart catheterisation",
        "Mean PAP > 20 mmHg on echocardiography at rest",
        "Systolic PAP > 20 mmHg at rest with right heart catheterisation",
    ],
    "The definition line reads 'mean PAP > 20 mmHg at rest with right heart catheterisation'. The measurement is a mean pressure, the threshold is 20, and the technique is right heart catheterisation, not echocardiography.",
)

add(
    S2, 214, "recall",
    "How does page 214 define cor pulmonale, and which three causes are printed?",
    "RV hypertrophy/dilatation ± RV failure; causes are COPD, pulmonary HTN and thromboembolism (the last giving acute cor pulmonale)",
    [
        "LV hypertrophy/dilatation ± LV failure; causes are systemic HTN, aortic stenosis and myocardial infarction",
        "RV hypertrophy/dilatation ± RV failure; causes are COPD, pulmonary HTN and pulmonary stenosis",
        "RA dilatation ± RA failure; causes are COPD, mitral stenosis and thromboembolism",
    ],
    "The note reads 'Cor pulmonale : RV hypertrophy/dilatation ± RV failure', with causes 'COPD', 'Pulmonary HTN' and 'Thromboembolism → Acute cor pulmonale'. Cor pulmonale is right-heart disease from a pulmonary cause.",
)

add(
    S2, 214, "numeric",
    "Page 214 splits the classes by pulmonary vascular resistance in wood units. Which split is printed?",
    "PVR > 3 wood units → class I, III, IV; PVR < 3 wood units → class II, where PCWP (LAP) > 15 mmHg",
    [
        "PVR > 3 wood units → class II; PVR < 3 wood units → class I, III, IV, where PCWP (LAP) > 15 mmHg",
        "PVR > 5 wood units → class I, III, IV; PVR < 5 wood units → class II, where PCWP (LAP) > 15 mmHg",
        "PVR > 3 wood units → class I, III, IV; PVR < 3 wood units → class II, where PCWP (LAP) > 20 mmHg",
    ],
    "The brace reads '> 3 wood units → Class I, III, IV' and '< 3 wood units → Class II : PCWP (LAP) >15 mmHg'. The class II threshold is a wedge pressure of 15 mmHg, matching the upstream left-heart mechanism.",
)

add(
    S2, 214, "recall",
    "The pathology of PAH is summarised on page 214 by a single term for the arterial lesion. Which term is printed, and which vessels are affected?",
    "Plexiform arteriolopathy, with the arterioles affected",
    [
        "Plexiform arteriopathy, with the pulmonary veins affected",
        "Intimal fibroelastosis, with the arterioles affected",
        "Medial hypertrophy, with the pulmonary artery affected",
    ],
    "Page 214 prints 'Plexiform arteriolopathy (Arterioles affected)' under the PAH heading, consistent with class 1 being an arteriolar disease in the page 213 figure.",
)

add(
    S2, 214, "match",
    "Match each secondary cause of PAH with its printed detail — 1) Hereditary 2) Acquired 3) Infection 4) Drugs … A) HIV B) Bone morphogenic protein receptor-2 (BMPR2) mutation C) Serotonin (appetite suppressants) D) Limited systemic sclerosis",
    "1-B, 2-D, 3-A, 4-C",
    ["1-B, 2-A, 3-D, 4-C", "1-C, 2-D, 3-A, 4-B", "1-D, 2-B, 3-C, 4-A"],
    "The list reads 'Hereditary : Bone morphogenic protein receptor-2 (BMPR2) mutation', 'Acquired : Limited systemic sclerosis', 'HIV' and 'Drugs : Serotonin (Appetite suppressants)'. HIV is listed as its own infective cause rather than under acquired autoimmune disease.",
)

add(
    S2, 214, "scenario",
    "A patient with cirrhosis develops pulmonary hypertension. Which mechanism does page 214 print for portal HTN?",
    "Splanchnic vasodilatation → hyperdynamic circulation → ↑CO → pulmonary HTN",
    [
        "Splanchnic vasoconstriction → low-output circulation → ↓CO → pulmonary HTN",
        "Portosystemic shunting → ↓LAP → class 2 pulmonary HTN",
        "Splanchnic vasodilatation → ↓CO → ↑PVR → pulmonary HTN",
    ],
    "The page prints 'Portal HTN : Splanchnic vasodilatation → Hyperdynamic circulation → ↑CO → Pulmonary HTN'. This is a high-flow mechanism acting through the CO term of the equation on page 213, not a resistance or wedge mechanism.",
)

add(
    S2, 214, "recall",
    "Which drug list is printed under the drug cause of PAH?",
    "Fenfluramine, dexfenfluramine, benfluorex, aminorex and toxic rapeseed oil",
    [
        "Fenfluramine, dexfenfluramine, benfluorex, amiodarone and toxic rapeseed oil",
        "Fenfluramine, dexfenfluramine, bosentan, aminorex and toxic rapeseed oil",
        "Fenfluramine, dexfenfluramine, benfluorex, aminorex and ergotamine",
    ],
    "The drug block prints 'Serotonin (Appetite suppressants)' — Fenfluramine, Dexfenfluramine, Benfluorex, Aminorex — and 'Toxic rapeseed oil'. Amiodarone, bosentan and ergotamine are not on this list.",
)

add(
    S2, 214, "truefalse",
    "TRUE or FALSE about the haemodynamic comparisons on page 214.",
    "True — PAP is far below systemic arterial pressure and PVR far below systemic vascular resistance, because the lungs are a low-resistance, high-compliance system",
    [
        "False — PAP exceeds systemic arterial pressure because the lungs receive the whole cardiac output",
        "False — PVR exceeds systemic vascular resistance because the pulmonary circuit is in series",
        "True — systemic hypertension causes RV hypertrophy while pulmonary hypertension causes LV dilatation",
    ],
    "The block reads 'PAP <<< SAP', 'PVR <<< SAR' and 'Lungs : Low resistance high compliance system', then 'Systemic HTN → LV hypertrophy' and 'Pulmonary HTN → RV dilatation → RV failure → ↑mortality'. The ventricular responses are the reverse of the option offered.",
)


add(
    S2, 214, "recall",
    "A boxed equation on page 214 restates how systemic arterial pressure is generated. Which form is printed there?",
    "Systemic arterial pressure = CO × systemic vascular resistance + right atrial pressure",
    [
        "Systemic arterial pressure = CO × pulmonary vascular resistance + right atrial pressure",
        "Systemic arterial pressure = CO × systemic vascular resistance + left atrial pressure",
        "Systemic arterial pressure = CO × systemic vascular resistance − right atrial pressure",
    ],
    "The box reads 'Systemic arterial pressure = CO x systemic vascular resistance + Right atrial pressure'. Note the addend printed is the RIGHT atrial pressure, not the left — the same structural form as the pulmonary equation PAP = (CO × PVR) + LAP on page 213.",
)


# ---------------------------------------------------------------- Unit 3: p215
add(
    S3, 215, "recall",
    "The three processes grouped under 'PATHOLOGY' on page 215 are:",
    "Vasoconstriction, remodeling and thrombosis",
    [
        "Vasodilatation, remodeling and haemorrhage",
        "Vasoconstriction, fibrosis and calcification",
        "Remodeling, thrombosis and amyloid deposition",
    ],
    "The bracket over the three arrows reads 'vasoconstriction', 'Remodeling' and 'Thrombosis'. All three converge on the raised PVR that defines the disease.",
)

add(
    S3, 215, "match",
    "Match each pathway with its printed effect in PAH — 1) Endothelin pathway 2) Nitric oxide pathway 3) Prostacyclin pathway … A) Inhibited, with NO → ↑cGMP B) Promoted C) Inhibited, with prostacyclin → ↑cAMP",
    "1-B, 2-A, 3-C",
    ["1-B, 2-C, 3-A", "1-A, 2-B, 3-C", "1-C, 2-A, 3-B"],
    "The table rows read 'Endothelin pathway — Promoted', 'Nitric oxide pathway : NO → ↑cGMP — Inhibited' and 'Prostacyclin pathway : Prostacyclin → ↑cAMP — Inhibited'. Only the endothelin pathway is upregulated.",
)

add(
    S3, 215, "match",
    "Match each pathway with the treatment class printed against it — 1) Endothelin pathway 2) Nitric oxide pathway 3) Prostacyclin pathway … A) Phosphodiesterase inhibitors B) Antagonists of endothelin receptors C) Prostacyclin analogues",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "The treatment column reads 'Antagonists of endothelin receptors', 'Phosphodiesterase inhibitors' and 'Prostacyclin analogues' in that order. The logic is to block the promoted pathway and to replace the inhibited ones.",
)

add(
    S3, 215, "recall",
    "Which two symptoms are bracketed on page 215 as occurring 'without overt signs of heart & lung disease'?",
    "Breathlessness and fatigue",
    [
        "Chest pain and syncope",
        "Haemoptysis and palpitations",
        "Ascites and pedal oedema",
    ],
    "The presentation bracket joins 'Breathlessness' and 'Fatigue' to 'without overt signs of heart & lung disease'. Chest pain and syncope appear only later, once the right ventricle is under strain.",
)

add(
    S3, 215, "recall",
    "Which chain is printed on page 215 for RV dilatation in pulmonary hypertension?",
    "RV dilatation → septal push → ↑LV volume → ↓CO → breathlessness, fatigue, syncope",
    [
        "RV dilatation → septal push → ↓LV volume → ↓CO → breathlessness, fatigue, syncope",
        "RV dilatation → tricuspid stenosis → ↓RV filling → ↓CO → breathlessness, fatigue, syncope",
        "LV dilatation → septal push → ↓RV volume → ↓CO → breathlessness, fatigue, syncope",
    ],
    "The arrow chain reads 'RV dilatation → septal push → ↑ LV volume → ↓ CO' and then brackets the three consequences 'Breathlessness, Fatigue, Syncope'. Note the printed direction: LV volume rises here, the reverse of the massive-VTE chain on page 206.",
)

add(
    S3, 215, "recall",
    "How does page 215 explain chest pain in pulmonary hypertension?",
    "↓RV filling + ↑RV afterload → RV ischemia → chest pain",
    [
        "↑RV filling + ↓RV afterload → RV ischemia → chest pain",
        "↓LV filling + ↑LV afterload → LV ischemia → chest pain",
        "RV dilatation → pericardial stretch → pericarditis → chest pain",
    ],
    "The line reads '↓ RV filling + ↑ RV afterload → RV ischemia → Chest pain'. Reduced filling reduces coronary perfusion while the raised afterload increases oxygen demand — a supply-demand mismatch in the right ventricle.",
)

add(
    S3, 215, "recall",
    "Which four findings are grouped under RV failure on page 215, and what happens to the apex?",
    "Ascites, edema, hepatomegaly, and the apex shifts outwards",
    [
        "Ascites, edema, hepatomegaly, and the apex shifts inwards",
        "Pleural effusion, pulmonary edema, splenomegaly, and the apex shifts outwards",
        "Ascites, peripheral cyanosis, hepatomegaly, and the apex remains normal",
    ],
    "The last bullet reads 'RV failure : Ascites, edema, hepatomegaly, apex shifts outwards.' The outward (leftward) apex shift accompanies the right ventricular enlargement.",
)

add(
    S3, 215, "match",
    "Match each bedside sign with its printed explanation — 1) Loud P2 2) Wide splitting of P2 3) S3 4) JVP … A) 'a' waves B) Listed as an auscultatory sign in RV failure C) Pulmonary HTN → RA-RV dilatation → ↑diastolic filling pressure D) Listed as an auscultatory finding without a bracketed mechanism",
    "1-D, 2-B, 3-C, 4-A",
    ["1-D, 2-C, 3-B, 4-A", "1-A, 2-B, 3-C, 4-D", "1-B, 2-D, 3-C, 4-A"],
    "Under auscultation the page prints 'Loud P2' then, 'In RV failure', 'wide splitting of P2' and 'S3 (Pulmonary HTN → RA-RV dilatation → ↑Diastolic filling pressure)'; the JVP line reads 'a waves'. Only the S3 carries an explicit mechanism on the page.",
)


add(
    S3, 215, "scenario",
    "A patient with long-standing pulmonary hypertension now has ascites, pedal oedema, a pulsatile liver and an apex beat displaced outwards. Which printed signs belong to this stage, and which finding is described as rare?",
    "RV failure with ascites, edema, hepatomegaly and an outward apex shift; clubbing is described as rare in the figure",
    [
        "LV failure with ascites, edema, hepatomegaly and an inward apex shift; clubbing is described as common",
        "RV failure with ascites, edema, hepatomegaly and an outward apex shift; clubbing is described as universal",
        "RV failure with clear lungs, a fixed split S2 and an inward apex shift; clubbing is described as rare",
    ],
    "The RV failure bullet reads 'Ascites, edema, hepatomegaly, apex shifts outwards', and the figure labels 'Clubbing rare' alongside 'Cold extremities', 'Peripheral edema' and a 'Large pulsatile liver'. The lungs are separately labelled clear.",
)


# ---------------------------------------------------------------- Unit 4: p216
add(
    S4, 216, "recall",
    "Which investigation is named the gold standard for diagnosis on page 216?",
    "PA catheterisation",
    ["Echocardiography", "CT pulmonary angiography", "Right-sided ECG criteria"],
    "Page 216 opens with 'PA catheterisation : Gold standard for diagnosis.' This matches the page 214 definition, which required a mean PAP measured at right heart catheterisation.",
)

add(
    S4, 216, "recall",
    "Carvallo's sign on page 216 is attached to which murmur, and what does it describe?",
    "The pan systolic murmur, which increases on inspiration; it is lower left sternal border, high pitched and blowing",
    [
        "The early diastolic murmur, which increases on inspiration; it is lower left sternal border, low pitched and rumbling",
        "The ejection systolic murmur, which decreases on inspiration; it is upper right sternal border, high pitched and blowing",
        "The pan systolic murmur, which increases on expiration; it is at the apex, low pitched and rumbling",
    ],
    "Under '1. Pan systolic murmur' the page prints '↑ on inspiration : Carvallo's sign', 'Lower left sternal border' and 'High pitched, blowing'. The inspiratory increase is the right-sided (tricuspid regurgitation) manoeuvre.",
)

add(
    S4, 216, "recall",
    "Which description of Graham Steell's murmur is printed on page 216?",
    "Early diastolic murmur from PA dilatation in severe PAH, heard sitting up, leaning forward and in fixed expiration, indicating pulmonary regurgitation",
    [
        "Early diastolic murmur from LV dilatation in severe systemic HTN, heard sitting up, leaning forward and in fixed inspiration, indicating aortic regurgitation",
        "Mid diastolic murmur from PA dilatation in mild PAH, heard in expiration, indicating pulmonary stenosis",
        "Early systolic murmur from PA dilatation in severe PAH, heard leaning forward, indicating tricuspid regurgitation",
    ],
    "The third murmur reads 'Early diastolic murmur : Graham Steells murmur. D/t PA dilatation (Severe PAH). Sitting up, leaning forward and fixed expiration. Indicates pulmonary regurgitation +.' The murmur is diastolic because it is regurgitant flow back into the right ventricle.",
)

add(
    S4, 216, "oddoneout",
    "Pick the ODD ONE OUT — three murmurs are printed on page 216, one is not:",
    "Mid-diastolic rumble of mitral stenosis",
    ["Pan systolic murmur", "Ejection systolic murmur d/t pulmonary stenosis", "Early diastolic Graham Steell's murmur"],
    "Page 216 lists exactly three murmurs in PAH: pan systolic, ejection systolic from pulmonary stenosis, and the early diastolic Graham Steell's murmur. Mitral stenosis is mentioned on page 213 only as a cause of class 2 disease, not as a PAH murmur.",
)

add(
    S4, 216, "recall",
    "Which four findings are labelled on the PAH chest radiograph on page 216?",
    "Large central pulmonary arteries, right ventricular hypertrophy, rapid attenuation of pulmonary vessels and clear lung fields",
    [
        "Large central pulmonary arteries, left ventricular hypertrophy, rapid attenuation of pulmonary vessels and clear lung fields",
        "Small central pulmonary arteries, right ventricular hypertrophy, rapid attenuation of pulmonary vessels and bilateral infiltrates",
        "Large central pulmonary veins, right atrial enlargement, delayed attenuation of pulmonary vessels and clear lung fields",
    ],
    "The labelled film reads from top to bottom 'Large central pulmonary arteries', 'Right ventricular hypertrophy', 'Rapid attenuation of pulmonary vessels' and 'Clear lung fields'. Rapid tapering with clear fields separates vascular from parenchymal disease.",
)

add(
    S4, 216, "fillup",
    "The page 216 figure caption names two diseases causing a pulmonary artery aneurysm: Behçet's and ______.",
    "Takayasu",
    ["Marfan syndrome", "Giant cell arteritis", "Polyarteritis nodosa"],
    "The caption reads 'Pulmonary artery aneurysm : Behçet's, Takayasu'. Both are large-vessel arteritides, which is why the aneurysm appears in the PA rather than in the left-sided circulation alone.",
)

add(
    S4, 216, "numeric",
    "Which ECG criterion for right ventricular hypertrophy is printed with the strip on page 216?",
    "r/s ratio > 1 in V1",
    ["r/s ratio > 1 in V6", "r/s ratio < 1 in V1", "R wave > 26 mm in V5"],
    "The line beside the ECG reads 'r/s ratio > 1 in V1 (Indicates RVH)'. The accompanying note flips the normal pattern: 'Large S wave in V1' and 'Large r wave in V6' are the normal findings.",
)

add(
    S4, 216, "truefalse",
    "TRUE or FALSE about the ECG note on page 216.",
    "True — in a normal ECG there is a large S wave in V1 and a large r wave in V6",
    [
        "False — in a normal ECG there is a large r wave in V1 and a large S wave in V6",
        "False — the note says a normal ECG always shows an r/s ratio > 1 in V1",
        "True — the note says PAH abolishes the r wave in V6 while preserving the S wave in V1",
    ],
    "The note reads 'Normal ECG : Large S wave in V1. Large r wave in V6.' RV hypertrophy reverses this dominance, which is exactly why 'r/s ratio > 1 in V1' is used as the criterion on the same page.",
)


# ---------------------------------------------------------------- Unit 5: p217
add(
    S5, 217, "recall",
    "Which pulmonary function pattern is printed for pulmonary hypertension on page 217?",
    "FEV1/FVC normal, FVC normal, DLCO ↓",
    [
        "FEV1/FVC low, FVC normal, DLCO normal",
        "FEV1/FVC normal, FVC low, DLCO ↓",
        "FEV1/FVC low, FVC low, DLCO ↓",
    ],
    "The PFT block reads 'FEV/FVC : Normal', 'FVC : Normal' and 'DLCO ↓'. A purely vascular disease leaves spirometry intact but reduces gas transfer, mirroring the vascular pattern of chapter 33.",
)

add(
    S5, 217, "match",
    "Match each investigation with the reason printed beside it on page 217 — 1) ECHO 2) V/Q scan 3) Sleep study 4) HRCT … A) To r/o interstitial lung disease B) To r/o chronic thromboembolic PAH C) To assess RV function and TR D) To r/o obstructive sleep apnea",
    "1-C, 2-B, 3-D, 4-A",
    ["1-C, 2-B, 3-A, 4-D", "1-B, 2-C, 3-D, 4-A", "1-D, 2-A, 3-B, 4-C"],
    "The lines read 'ECHO : To assess RV function, TR', 'V/Q scan : To r/o chronic thromboembolic PAH', 'Sleep study : To r/o obstructive sleep apnea' and 'HRCT : To r/o interstitial lung disease'. Each test is screening out a competing class of pulmonary hypertension.",
)

add(
    S5, 217, "recall",
    "The 6-minute walk test on page 217 is done for which stated purpose?",
    "To determine prognosis",
    ["To diagnose pulmonary hypertension", "To exclude interstitial lung disease", "To titrate nifedipine"],
    "The line reads '6-minute walk test : To determine prognosis.' It is a functional and prognostic measure, not a diagnostic test — diagnosis rests on PA catheterisation per page 216.",
)

add(
    S5, 217, "numeric",
    "Which response defines a positive vaso-reactivity test on page 217?",
    "PAP decreases by 10 mmHg or PAP < 40 mmHg, with BP and CO unchanged; seen in 10% of cases",
    [
        "PAP decreases by 20 mmHg or PAP < 40 mmHg, with BP and CO unchanged; seen in 10% of cases",
        "PAP decreases by 10 mmHg or PAP < 40 mmHg, with BP falling and CO rising; seen in 30% of cases",
        "PAP decreases by 10 mmHg or PAP < 25 mmHg, with BP and CO unchanged; seen in 10% of cases",
    ],
    "The block reads 'Patient given nitric oxide (Potent PA vasodilator) → PAP measured', 'Positive test (10% cases) → PAP decreases by 10 mmHg/PAP < 40 mmHg' and a brace stating that BP and CO 'Remains the same'. The fall must be selective for the pulmonary circulation.",
)

add(
    S5, 217, "recall",
    "What inference follows a positive vaso-reactivity test, and which drug and dose are printed?",
    "Pulmonary HTN responds to high dose CCBs — nifedipine 240 mg",
    [
        "Pulmonary HTN responds to low dose CCBs — nifedipine 60 mg",
        "Pulmonary HTN responds to high dose CCBs — diltiazem 240 mg",
        "Pulmonary HTN responds to phosphodiesterase inhibitors — sildenafil 240 mg",
    ],
    "The inference line reads 'Positive test → Pulmonary HTN responds to high dose CCBs (Nifedipine 240 mg)'. The same 240 mg nifedipine figure is repeated in the specific-treatment table's first row.",
)

add(
    S5, 217, "recall",
    "Which four general treatment measures are listed at the start of page 217, including one contraindication?",
    "Oral anticoagulants, long term O2 therapy, diuretics for right heart failure, and pregnancy contraindicated",
    [
        "Oral anticoagulants, long term O2 therapy, beta blockers for right heart failure, and pregnancy permitted",
        "Oral anticoagulants, inhaled nitric oxide, diuretics for left heart failure, and pregnancy contraindicated",
        "Oral anticoagulants, long term O2 therapy, diuretics for right heart failure, and pregnancy permitted",
    ],
    "The measures read 'Oral anticoagulants (To prevent thrombosis & thromboembolism)', 'Long term O2 therapy', 'Diuretics for right heart failure' and 'Pregnancy contraindicated'. Anticoagulation here is prophylaxis against in-situ thrombosis, not treatment of embolism.",
)

add(
    S5, 217, "recall",
    "For NYHA I–3 disease, which drug pair is printed in the specific-treatment table?",
    "Tadalafil (phosphodiesterase-5 inhibitor) + ambrisentan (endothelin receptor antagonist)",
    [
        "Tadalafil (endothelin receptor antagonist) + ambrisentan (phosphodiesterase-5 inhibitor)",
        "Epoprostenol + treprostinil",
        "Nifedipine + selexipag",
    ],
    "The NYHA I–3 row reads 'Tadalafil (Phosphodiesterase -5 inhibitor) + Ambrisentan (Endothelin receptor antagonist)'. Epoprostenol and treprostinil belong to the NYHA class-4 row, and nifedipine to the positive vaso-reactivity row above.",
)

add(
    S5, 217, "scenario",
    "A patient with PAH has symptoms at rest. Using the page 217 table, which prostanoid details are printed?",
    "Epoprostenol (most common) via a permanent tunnel catheter in the IJV, treprostinil via a microinfusion pump, and selexipag as a chemically stable oral prostacyclin derivative not yet available",
    [
        "Epoprostenol (most common) via a microinfusion pump, treprostinil via a permanent tunnel catheter in the IJV, and selexipag as an oral endothelin antagonist",
        "Iloprost (most common) via a permanent tunnel catheter in the IJV, treprostinil via a microinfusion pump, and selexipag as a chemically stable oral prostacyclin derivative",
        "Epoprostenol (most common) via a permanent tunnel catheter in the IJV, treprostinil orally, and selexipag as an inhaled prostacyclin analogue already available",
    ],
    "The class-4 row reads 'Prostanoids : Epoprostenol (m/c) via permanent tunnel catheter in IJV; Trepostinil (via microinfusion pump); Selexipag : Chemically stable, Orally active prostacyclin derivative, Not available yet.' The drug name is printed 'Trepostinil'.",
)


GUIDES = {
    S1: (
        "Ohm's Law Applied to the Pulmonary Circulation (PAP − LAP = CO × PVR), the Five WHO Classes, Class 1 PAH Features and the Class-to-Affected-Vessel Figure",
        "Page 213 applies Ohm's law: V is the PAP−LAP gradient, I is cardiac output and R is pulmonary vascular resistance, so PAP − LAP = CO × PVR and PAP = (CO × PVR) + LAP. A raised PAP therefore comes from a raised PVR (classes 1, 3 and 4) or a raised LAP (class 2, commonest cardiac cause mitral stenosis).\n"
        "Class 1 PAH is mostly idiopathic (hence idiopathic pulmonary HTN), has a very poor prognosis with median survival < 9 months and affects young females. Class 2 is left heart disease with ↑LAP; class 3 follows chronic lung disease via hypoxia-related pulmonary vasoconstriction, with chronic bronchitis as the example and a very poor prognosis; class 4 is chronic thrombo-embolic disease responsive to surgery; class 5 is miscellaneous and multifactorial.\n"
        "The figure labels the affected structure: class 1 arterioles, class 2 pulmonary vein, class 3 capillary, class 4 pulmonary artery and class 5 multifactorial. A boxed note adds that hypoxia causes vasodilatation everywhere except in pulmonary vessels.",
    ),
    S2: (
        "PAH vs Systemic HTN Mortality Logic, Definition (Mean PAP > 20 mmHg), Cor Pulmonale, Wood-Unit PVR Split, Plexiform Arteriolopathy & Secondary Causes (BMPR2 to Appetite Suppressants)",
        "Pulmonary hypertension (p214) kills more than systemic hypertension: PAP <<< SAP and PVR <<< SAR because the lungs are a low-resistance, high-compliance system, so systemic HTN causes LV hypertrophy whereas pulmonary HTN causes RV dilatation, RV failure and ↑mortality.\n"
        "The definition is a mean PAP > 20 mmHg at rest on right heart catheterisation. Cor pulmonale is RV hypertrophy/dilatation ± RV failure from COPD, pulmonary HTN or thromboembolism (the last being acute cor pulmonale). PVR > 3 wood units places disease in class I/III/IV, while PVR < 3 wood units with PCWP (LAP) > 15 mmHg places it in class II. The PAH lesion is plexiform arteriolopathy affecting the arterioles.\n"
        "Secondary causes: hereditary BMPR2 mutation; acquired limited systemic sclerosis; HIV; schistosomiasis; portal HTN via splanchnic vasodilatation → hyperdynamic circulation → ↑CO; and drugs — the serotonin appetite suppressants fenfluramine, dexfenfluramine, benfluorex and aminorex, plus toxic rapeseed oil.",
    ),
    S3: (
        "Pathology Triad, Endothelin/NO/Prostacyclin Pathway Treatment Table, Clinical Presentation and the RV Dilatation and RV Failure Sign Chains",
        "Pathology (p215) is vasoconstriction, remodeling and thrombosis. The pathway table reads: endothelin pathway promoted → endothelin receptor antagonists; nitric oxide pathway (NO → ↑cGMP) inhibited → phosphodiesterase inhibitors; prostacyclin pathway (prostacyclin → ↑cAMP) inhibited → prostacyclin analogues.\n"
        "Presentation is breathlessness and fatigue without overt signs of heart and lung disease. RV dilatation → septal push → ↑LV volume → ↓CO gives breathlessness, fatigue and syncope; ↓RV filling plus ↑RV afterload → RV ischaemia → chest pain; RV failure gives ascites, edema, hepatomegaly and an apex that shifts outwards.\n"
        "Signs: loud P2; in RV failure wide splitting of P2 and S3 (from RA-RV dilatation raising diastolic filling pressure); palpable P2, parasternal heave and palpable epigastric impulse; JVP shows 'a' waves. The figure adds a prominent V wave if tricuspid regurgitation is present, clear lungs, fixed splitting of S2, left parasternal lift, large pulsatile liver, cold extremities, rare clubbing and peripheral edema.",
    ),
    S4: (
        "PA Catheterisation Gold Standard, the Three PAH Murmurs (Carvallo, Ejection Systolic, Graham Steell), CXR Findings, PA Aneurysm Causes and ECG RVH Criteria",
        "PA catheterisation (p216) is the gold standard for diagnosis. Three murmurs occur in PAH: a pan systolic murmur that ↑ on inspiration (Carvallo's sign), lower left sternal border, high pitched and blowing; an ejection systolic murmur from pulmonary stenosis; and an early diastolic murmur — Graham Steell's — from PA dilatation in severe PAH, heard sitting up leaning forward in fixed expiration and indicating pulmonary regurgitation.\n"
        "CXR: large central pulmonary arteries, right ventricular hypertrophy, rapid attenuation of pulmonary vessels and clear lung fields; the PA aneurysm caption names Behçet's and Takayasu. ECG: r/s ratio > 1 in V1 indicates RVH, whereas a normal ECG has a large S wave in V1 and a large r wave in V6.",
    ),
    S5: (
        "Investigations to Exclude Other Causes (PFT, ECHO, V/Q, Sleep Study, HRCT, 6MWT), the Vaso-Reactivity Test, General Treatment and the NYHA-Stratified Drug and Surgical Table",
        "PFT (p217) shows normal FEV1/FVC and FVC with ↓DLCO. ECHO assesses RV function and TR; V/Q scan excludes chronic thromboembolic PAH; sleep study excludes obstructive sleep apnea; HRCT excludes interstitial lung disease; the 6-minute walk test determines prognosis.\n"
        "Vaso-reactivity testing gives nitric oxide and measures PAP: a positive test (10% of cases) lowers PAP by 10 mmHg or to < 40 mmHg with BP and CO unchanged, implying response to high dose calcium channel blockers — nifedipine 240 mg.\n"
        "General treatment: oral anticoagulants, long term O2, diuretics for right heart failure and contraindication of pregnancy. Specific treatment by finding: vaso-reactivity + → nifedipine 240 mg; NYHA I–3 → tadalafil + ambrisentan; NYHA class-4 (symptoms at rest) → prostanoids — epoprostenol (m/c) by permanent tunnel catheter in the IJV, treprostinil by microinfusion pump, and selexipag, a chemically stable oral prostacyclin derivative not yet available. Surgical options if not responding to drugs are atrial septostomy and lung transplant.",
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
