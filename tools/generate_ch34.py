#!/usr/bin/env python3
"""Generate Chapter 34: Venous Thromboembolism (Book p206–212).

Every question is anchored to a specific line, brace, table cell or figure
caption of uploads/02.pdf sheets 89–95 (Book pages 206–212), in printed order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 34
TITLE = "Venous Thromboembolism"
PAGES = "206-212"

S1 = "VTE Definition, Mortality, Thrombo-Embolic Pathogenesis, Origin of Thrombi, Acute Cor Pulmonale, Calf DVT & Massive VTE Pathogenesis Chain"
S2 = "Presentation, D/d of Dyspnea with Clear Lung Fields, Golden 4 Assessment (Clinical, ECHO/McConnel Sign, Biomarkers, CTPA) & Submassive/Non-Massive VTE"
S3 = "Non-Massive VTE Investigations & Complications, Genetic and Acquired Risk-Factor Lists, Malignancy/Nephrotic/Surgery Risks & Ventilation-Perfusion Physiology"
S4 = "Dead-Space vs Shunt Physiology in PE, Symptoms/Signs, Vagal Bradycardia, Acute Cor Pulmonale Complications & Type I Respiratory Failure with A-a Gradient"
S5 = "CXR Signs (Atelectatic Bands, Hampton's Hump, Pallas, Westermark, Fleischner), PAH Films & ECG Significance and Patterns (S1Q3T3)"
S6 = "Pulmonary Angiography Gold Standard, V/Q Scan Indications, D-Dimer, ECHO, the Wells Score Table and CTPA Signs (Saddle Embolus, Polo Mint Sign)"
S7 = "Management: Heparin/LMWH Dosing, Severity Determination, Thrombolysis vs Catheter Therapy, Heparin Target Ranges, 3-Month Switch and IVC Filter"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(34000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(34100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p206
add(
    S1, 206, "recall",
    "The chapter opening names VTE by a second term and prints one mortality figure. Which pair is printed?",
    "AKA pulmonary thromboembolism (PTE); 60–80% mortality in massive PTE",
    [
        "AKA pulmonary arterial thrombosis; 30–40% mortality in submassive PTE",
        "AKA pulmonary thromboembolism (PTE); 20–30% mortality in massive PTE",
        "AKA pulmonary embolism syndrome; 60–80% mortality in submassive PTE",
    ],
    "The first two lines read 'AKA pulmonary thromboembolism (PTE).' and '60–80% mortality in massive PTE.' The 60–80% figure is attached to massive PTE specifically, not to submassive disease.",
)

add(
    S1, 206, "fillup",
    "Page 206 defines the pathogenesis of VTE as migration of thrombi/microthrombi from the systemic circulation to the ______.",
    "Pulmonary vasculature",
    ["Systemic arterial tree", "Portal circulation", "Lymphatic channels"],
    "Page 206 prints 'migration of thrombi/microthrombi : Systemic circulation → Pulmonary vasculature.' The embolus travels with venous blood through the right heart into the pulmonary arterial tree.",
)

add(
    S1, 206, "match",
    "Page 206 ranks the sites from which thrombi originate. Match each printed statement with its site — 1) Deep veins 2) Max risk 3) In pregnancy … A) Pelvic veins B) Lower limb > upper limb C) Supra-popliteal veins → femoral veins",
    "1-B, 2-C, 3-A",
    ["1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-C, 2-B, 3-A"],
    "The origin list reads 'Deep veins of lower limb > upper limb', then 'max risk : Supra-popliteal veins → Femoral veins' and 'Pelvic veins (In pregnancy)'. The pelvic site is tied specifically to pregnancy.",
)

add(
    S1, 206, "oddoneout",
    "Pick the ODD ONE OUT — three statements are printed under the page 206 'Note :', one is not:",
    "DVT in calf is the commonest source of clinically significant emboli",
    [
        "Acute cor pulmonale: RV dilatation/hypertrophy ± heart failure",
        "Most common cause of acute cor pulmonale: VTE",
        "DVT in calf: most common site, and it does not embolize",
    ],
    "The Note prints the calf as the 'm/c site' but immediately adds 'Do not embolize' — the calf is the commonest DVT site yet is not the commonest source of emboli. The other three statements follow the page wording.",
)

add(
    S1, 206, "recall",
    "How does page 206 define a MASSIVE VTE?",
    "Any pulmonary embolism with hypotension",
    [
        "Any pulmonary embolism with RV dilatation but no hypotension",
        "Any pulmonary embolism with more than 50% clot burden on CT",
        "Any pulmonary embolism with haemoptysis and pleuritic pain",
    ],
    "The first line under 'Types of VTE' reads 'MASSIVE VTE — Any pulmonary embolism with hypotension.' RV dilatation without hypotension belongs instead to the submassive group on page 207.",
)

add(
    S1, 206, "numeric",
    "The massive-VTE pathogenesis chain on page 206 carries three numbers. Which set is printed?",
    ">50–70% occlusion of the pulmonary circulation; SBP < 90 mmHg; hypotension lasting ≥ 15 mins",
    [
        ">30–40% occlusion of the pulmonary circulation; SBP < 100 mmHg; hypotension lasting ≥ 10 mins",
        ">50–70% occlusion of the pulmonary circulation; SBP < 90 mmHg; hypotension lasting ≥ 30 mins",
        ">70–90% occlusion of the pulmonary circulation; SBP < 90 mmHg; hypotension lasting ≥ 15 mins",
    ],
    "The chain starts 'Pulmonary circulation blocked by thrombus (>50–70% occlusion) → Hypoxemia' and ends at 'Hypotension : SBP < 90 mmHg' with the brace 'Lasting for ≥ 15 mins or Requires ionotropic support'. All three printed cut-offs must be kept together.",
)

add(
    S1, 206, "recall",
    "Which sequence is printed for the massive-VTE chain after the pulmonary circulation is blocked?",
    "RV & RA dilatation → septum pushed to left → ↓LV volume → ↓cardiac output → hypotension",
    [
        "LV dilatation → septum pushed to right → ↑RV volume → ↑cardiac output → hypertension",
        "RA dilatation → tricuspid stenosis → ↓RV filling → ↓cardiac output → hypotension",
        "RV & RA dilatation → ↑LV volume → ↑cardiac output → hypotension",
    ],
    "Page 206 draws 'RV & RA dilatation' → 'Pushes septum to left' → '↓ LV volume' → '↓ cardiac output → Hypotension'. The leftward septal shift reduces, not increases, LV volume.",
)

add(
    S1, 206, "scenario",
    "A 58-year-old with a saddle embolus is hypotensive and needs inotropes. Applying page 206, the diagnosis and the two alternative qualifying criteria for the hypotension limb are:",
    "Massive VTE — hypotension qualifies if it lasts ≥ 15 mins OR requires ionotropic support",
    [
        "Submassive VTE — hypotension qualifies only if it lasts ≥ 30 mins and needs inotropes",
        "Massive VTE — hypotension must last ≥ 15 mins AND require ionotropic support together",
        "Non-massive VTE — hypotension is not part of this classification at all",
    ],
    "The brace after 'SBP < 90 mmHg' reads 'Lasting for ≥ 15 mins' OR 'Requires ionotropic support' — either criterion suffices, and the presence of hypotension by itself makes the episode massive.",
)


# ---------------------------------------------------------------- Unit 2: p207
add(
    S2, 207, "recall",
    "Page 207 lists four presentations of PTE and names the most and second most common symptoms. Which pair is printed?",
    "Most common: unexplained dyspnea with clear lung fields; second most common symptom: chest pain",
    [
        "Most common: pleuritic chest pain; second most common symptom: unexplained dyspnea",
        "Most common: syncope; second most common symptom: sudden cardiac death",
        "Most common: haemoptysis; second most common symptom: unexplained dyspnea",
    ],
    "The presentation list gives 'unexplained dyspnea with clear lung fields (m/c)' and 'chest pain : 2nd m/c symptom of PTE', alongside sudden cardiac death and syncope. Clear lung fields with breathlessness is the signature presentation.",
)

add(
    S2, 207, "fillup",
    "The page 207 note gives only two entries in the D/d for dyspnea with clear lung fields: 1. VTE and 2. ______.",
    "Metabolic acidosis",
    ["Pulmonary oedema", "Pneumothorax", "Bronchial asthma"],
    "The boxed note reads 'D/d for dyspnea with clear lung fields : 1. VTE. 2. metabolic acidosis.' Pulmonary oedema and pneumothorax do not give clear lung fields, which is why they are absent from this short list.",
)

add(
    S2, 207, "recall",
    "The 'Golden 4' assessment on page 207 numbers four domains. Which four are printed, in order?",
    "1. Clinical (hypotension) 2. ECHO 3. Biomarkers 4. Imaging evidence",
    [
        "1. Clinical (tachycardia) 2. ECG 3. Biomarkers 4. Imaging evidence",
        "1. Clinical (hypotension) 2. Chest radiograph 3. D-dimer 4. CTPA",
        "1. Wells score 2. ECHO 3. D-dimer 4. Pulmonary angiography",
    ],
    "The page numbers '1. Clinical : Hypotension', '2. ECHO', '3. Biomarkers', '4. Imaging evidence'. The Wells score and pulmonary angiography appear later, on pages 211 and 212 respectively, not in the Golden 4.",
)

add(
    S2, 207, "match",
    "Match each ECHO entry of the Golden 4 with its printed description — 1) McConnel's sign 2) Septal push 3) LV contraction 4) R/o pericardial tamponade … A) Used as a negative check on the ECHO 2-D study B) Hypocontractile RV free wall with hypercontractile apex C) Septum displaced by the dilated right heart D) Listed simply as LV contraction",
    "1-B, 2-C, 3-D, 4-A",
    ["1-C, 2-B, 3-A, 4-D", "1-B, 2-C, 3-A, 4-D", "1-D, 2-A, 3-B, 4-C"],
    "The ECHO bracket joins 'McConnel's sign' to 'Hypocontractile RV free wall + Hypercontractile apex', with 'septal push', 'LV contraction' and 'R/o pericardial tamponade' listed as the other three entries. The sign is a regional wall-motion paradox, not global RV failure.",
)

add(
    S2, 207, "match",
    "Match each Golden-4 test with the process it is bracketed to on page 207 — 1) NT pro BNP 2) Troponin I 3) CTPA … A) RV ischemia B) IOC that visualises clot in PA C) RV dilatation",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "Page 207 brackets 'NT pro BNP : RV dilatation', 'Troponin I : RV ischemia' and, under imaging, 'CTPA (CT-Pulmonary angiogram) : IOC' with the bracket 'Clot in PA'. The two biomarkers are reused on the submassive block, where their elevation converts low risk into high risk.",
)

add(
    S2, 207, "recall",
    "CTPA is described on page 207 as the IOC and as visualising three findings. Which three are printed?",
    "Dilated pulmonary artery, clot in PA, large RV",
    [
        "Dilated pulmonary vein, clot in LA, small RV",
        "Dilated pulmonary artery, pleural effusion, normal RV",
        "Clot in PA, raised hemidiaphragm, large LV",
    ],
    "The bracket from 'IOC' and 'visualises' opens onto 'Dilated pulmonary artery (PA)', 'Clot in PA' and 'Large RV'. All three are direct embolic or right-heart consequences; pleural effusion is not among them.",
)

add(
    S2, 207, "scenario",
    "A normotensive patient with confirmed PE has RV dilatation on ECHO but normal NT pro BNP and troponin. Using the page 207 submassive block, this patient is:",
    "Submassive VTE at low risk — high risk needs the biomarker rise as well as RV dilatation/ischaemia",
    [
        "Massive VTE at high risk — any RV dilatation makes the episode massive",
        "Non-massive VTE — the block requires hypotension for submassive disease",
        "Submassive VTE at high risk — RV dilatation alone defines high risk",
    ],
    "The brace prints 'RV dilatation/ischemia : Low risk' plus the two biomarker arrows '(RV dilatation)' and '(RV ischaemia)' joining to 'High risk'. A single low-risk feature stays low risk; only the combination escalates.",
)

add(
    S2, 207, "numeric",
    "Non-massive VTE is given an incidence on page 207 and a mechanism. Which pair is printed?",
    "10–20% of cases of VTE; d/t peripheral lodging of emboli",
    [
        "30–40% of cases of VTE; d/t central lodging of emboli",
        "10–20% of cases of VTE; d/t central lodging of emboli",
        "60–80% of cases of VTE; d/t peripheral lodging of emboli",
    ],
    "The block reads 'Incidence : 10–20% cases of VTE' and 'd/t peripheral lodging of emboli', with clinical features of recurrent/non-resolving pneumonia, cough, pleuritic chest pain and haemoptysis. The 60–80% figure on page 206 is mortality, not incidence.",
)


add(
    S2, 207, "scenario",
    "A 45-year-old has three episodes of 'recurrent pneumonia' confined to one peripheral segment, with cough, pleuritic pain and one episode of haemoptysis; ECHO and biomarkers are normal. Which page 207 category fits, and why?",
    "Non-massive VTE — peripheral lodging of emboli gives recurrent/non-resolving pneumonia, cough, pleuritic chest pain and haemoptysis",
    [
        "Massive VTE — recurrent pneumonia and haemoptysis are presentations of massive disease",
        "Submassive VTE at high risk — the haemoptysis alone escalates the risk",
        "Not VTE — recurrent pneumonia with a normal ECHO rules out embolism",
    ],
    "The non-massive block reads 'Recurrent episodes of pneumonia/non-resolving pneumonia', 'Cough', 'Pleuritic chest pain' and 'Hemoptysis', with the mechanism 'd/t peripheral lodging of emboli'. A normal ECHO and normal biomarkers are exactly what page 208 prints for non-massive disease, not a reason to exclude VTE.",
)


# ---------------------------------------------------------------- Unit 3: p208
add(
    S3, 208, "recall",
    "What do the investigations show in non-massive VTE on page 208, and what single complication is listed?",
    "ECHO normal, BP normal, biomarkers normal; complication is pulmonary infarction",
    [
        "ECHO shows RV dilatation, BP low, biomarkers raised; complication is pulmonary abscess",
        "ECHO normal, BP normal, biomarkers normal; complication is pulmonary hypertension",
        "ECHO shows RV strain, BP normal, biomarkers normal; complication is pleural empyema",
    ],
    "Page 208 prints 'ECHO : Normal', 'BP : Normal', 'Biomarkers : Normal' and 'Complications : Pulmonary infarction'. This normality is exactly why non-massive VTE is easy to miss clinically.",
)

add(
    S3, 208, "recall",
    "Under 'Genetics' on page 208, which risk factor is marked as the most common?",
    "Factor-V Leiden mutation",
    ["Antithrombin III deficiency", "Protein C deficiency", "Protein S deficiency"],
    "The genetic bracket opens with 'Factor-v Leiden mutation : m/c', followed by antithrombin III, protein C and protein S deficiencies. The other three are rarer inherited thrombophilias.",
)

add(
    S3, 208, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed in the 'Acquired' bracket, one belongs to the genetic bracket:",
    "Antithrombin III deficiency",
    [
        "Antiphospholipid antibody syndrome",
        "Paroxysmal nocturnal hemoglobinuria",
        "Heparin-induced thrombocytopenia",
    ],
    "The acquired bracket lists antiphospholipid antibody syndrome, polycythemia rubra vera, primary myelofibrosis, heparin-induced thrombocytopenia and paroxysmal nocturnal hemoglobinuria. Antithrombin III deficiency sits in the genetics bracket immediately above it.",
)

add(
    S3, 208, "recall",
    "Page 208 names one malignancy and one nephrotic lesion with its mechanism. Which pair is printed?",
    "Malignancy: adenocarcinoma; nephrotic syndrome (membranous nephropathy) d/t loss of antithrombin-III in urine",
    [
        "Malignancy: squamous cell carcinoma; nephrotic syndrome (minimal change) d/t loss of protein C in urine",
        "Malignancy: adenocarcinoma; nephrotic syndrome (minimal change) d/t loss of antithrombin-III in urine",
        "Malignancy: small cell carcinoma; nephrotic syndrome (membranous nephropathy) d/t loss of protein S in urine",
    ],
    "Page 208 prints 'malignancy : Adenocarcinoma' and 'Nephrotic syndrome (membranous nephropathy) : D/t loss of antithrombin-III in urine'. The histology and the lost protein are both specific as printed.",
)

add(
    S3, 208, "numeric",
    "The surgery risk on page 208 is quantified for immobilisation. What threshold is printed?",
    "Immobilisation for > 4 days, with orthopedic surgeries carrying ↑ risk",
    [
        "Immobilisation for > 2 days, with orthopedic surgeries carrying ↑ risk",
        "Immobilisation for > 7 days, with abdominal surgeries carrying ↑ risk",
        "Immobilisation for > 4 days, with neurosurgery carrying ↑ risk",
    ],
    "The surgery bracket reads 'Requiring immobilization for > 4 days' and 'Orthopedic surgeries ↑ risk'. Both entries are printed as a brace under 'Surgery'.",
)

add(
    S3, 208, "recall",
    "The physiology block at the foot of page 208 gives the regional distribution of ventilation, perfusion and the V/P ratio. Which statement is printed?",
    "Ventilation max at base, perfusion max at base, V/P ratio max at apex because the fall in perfusion exceeds the fall in ventilation",
    [
        "Ventilation max at apex, perfusion max at base, V/P ratio max at apex",
        "Ventilation max at base, perfusion max at apex, V/P ratio max at base",
        "Ventilation max at apex, perfusion max at apex, V/P ratio max at base",
    ],
    "The three lines read 'Ventilation (V) : max at base', 'Perfusion (P) : max at base' and 'Ventilation-Perfusion ratio (V/P) : max at apex (Decrease in perfusion > Decrease in ventilation)'. Both absolute flows are basal; the ratio rises apically.",
)

add(
    S3, 208, "truefalse",
    "TRUE or FALSE about the page 208 risk-factor lists.",
    "True — HRT, OCPs, pregnancy and post-partum are all printed as separate risk entries",
    [
        "False — post-partum is printed only under the genetic bracket",
        "False — COPD is printed as protective against VTE",
        "True — heart failure with reduced ejection fraction is printed without any qualifier",
    ],
    "Page 208 lists 'OCPs', 'HRT' and an obstetric brace of 'Pregnancy' and 'Post-partum' as separate entries, while the cardiac entry is qualified as 'Congestive cardiac failure (Heart failure with ↓ ejection fraction)'. Post-partum belongs to the acquired obstetric block, not the genetic one.",
)


# ---------------------------------------------------------------- Unit 4: p209
add(
    S4, 209, "recall",
    "Page 209 gives dead-space physiology with the example of pulmonary embolism. Which set of values is printed?",
    "V = Normal, P = 0, V/P = ∞",
    ["V = 0, P = Normal, V/P = 0", "V = Normal, P = Normal, V/P = 1", "V = 0, P = 0, V/P = ∞"],
    "The dead-space block prints 'eg : in pulmonary embolism, V = Normal, P = 0, V/P = ∞'. A blocked vessel leaves the alveolus ventilated but unperfused, so the ratio tends to infinity.",
)

add(
    S4, 209, "match",
    "Match each physiology with its printed values — 1) Dead space 2) Shunt 3) Normal lung … A) V = 0, P = Normal, V/P = 0 B) V = Normal, P = Normal, V/P = 0.8 C) V = Normal, P = 0, V/P = ∞",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "Dead space is 'V = Normal, P = 0, V/P = ∞' and shunt is 'V = 0, P = Normal, V/P = 0'; normal lung keeps both flows with V/P of about 0.8 as printed on page 231. Dead space and shunt are mirror images of one another.",
)

add(
    S4, 209, "recall",
    "The symptom hierarchy printed on page 209 is:",
    "Dyspnea (within seconds) > pleuritic chest pain, the latter in small and more peripheral emboli",
    [
        "Pleuritic chest pain > dyspnea, the latter in small and more peripheral emboli",
        "Haemoptysis > dyspnea, the latter in large central emboli",
        "Syncope > dyspnea, the latter in small and more peripheral emboli",
    ],
    "Page 209 prints 'Dyspnea (within seconds) > Pleuritic chest pain (in small & more peripheral emboli)' and separately 'Cough + hemoptysis (10–20% cases)'. Dyspnea outranks pain, and pain is tied to peripheral emboli.",
)

add(
    S4, 209, "numeric",
    "Two separate findings on page 209 are each given the same 10–20% frequency. Which two are they?",
    "Cough with haemoptysis, and rales/↓ breath sounds",
    [
        "Cough with haemoptysis, and unexplained dyspnea",
        "Pleuritic chest pain, and rales/↓ breath sounds",
        "Syncope, and hypoxia-induced bradycardia",
    ],
    "The page prints 'Cough + hemoptysis (10–20% cases)' under symptoms and 'Tachypnea > Tachycardia > Rales/ ↓ breath sounds (10–20% cases)' under signs. Dyspnea, in contrast, carries no percentage because it is the most common symptom.",
)

add(
    S4, 209, "recall",
    "Page 209 explains one paradoxical sign of PE. Which mechanism is printed?",
    "Hypoxia induced intrapulmonary vagal stimulation → bradycardia",
    [
        "Hypoxia induced sympathetic stimulation → tachycardia",
        "Hypoxia induced carotid body stimulation → bradycardia",
        "Hypercarbia induced vagal stimulation → bradycardia",
    ],
    "The sign line ends 'Hypoxia induced intrapulmonary vagal stimulation → Bradycardia'. Tachycardia is listed separately in the tachypnea > tachycardia > rales hierarchy, so the two coexist as different mechanisms.",
)

add(
    S4, 209, "match",
    "Match each complication branch of acute cor pulmonale with its printed label — 1) Shock 2) S3 + hypotension 3) ↑ JVP … A) Acute RV failure B) Massive VTE C) Listed as a third consequence",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-C, 2-A, 3-B", "1-B, 2-C, 3-A"],
    "The cor pulmonale brace reads 'Shock (massive VTE)', 'S3 + hypotension (Acute RV failure)' and '↑ JVP'. Shock is attached to the massive group, S3 with hypotension to acute RV failure.",
)

add(
    S4, 209, "recall",
    "Which set of statements is printed under 'Type I respiratory failure' for PE on page 209?",
    "Hypoxia d/t ventilation-perfusion mismatch; PaCO2 normal (no parenchymal involvement) → respiratory alkalosis; ↓perfusion → ↓diffusion → widening of the alveolar-arterial O2 gradient",
    [
        "Hypoxia with hypercarbia d/t parenchymal involvement → respiratory acidosis; narrowing of the alveolar-arterial O2 gradient",
        "Hypoxia d/t shunt; PaCO2 raised d/t dead space → respiratory acidosis; normal alveolar-arterial O2 gradient",
        "Hypoxia d/t diffusion block; PaCO2 low d/t hyperventilation of unperfused alveoli → metabolic acidosis; normal gradient",
    ],
    "The three lines under type I failure are exactly the mismatch hypoxia, the normal PaCO2 with consequent respiratory alkalosis, and the widened (Alveolar O2 − Arterial O2) gradient via reduced perfusion and diffusion. The type 2 note on the same page requires parenchymal involvement.",
)

add(
    S4, 209, "truefalse",
    "TRUE or FALSE about the two respiratory-failure notes on page 209.",
    "True — type 2 failure is defined there as hypoxia plus hypercarbia and is seen in lung disease with parenchyma involved",
    [
        "False — type 2 failure is defined there as hypoxia with a normal PaCO2",
        "False — type 2 failure is said there to occur only in PE",
        "True — type 1 failure is said there to require a raised PaCO2",
    ],
    "The note reads 'Type 2 respiratory failure : Hypoxia + hypercarbia' and 'Seen in lung diseases with parenchyma involved', which is precisely why uncomplicated PE produces type 1 failure. Type 1 by definition has a normal or low PaCO2.",
)


# ---------------------------------------------------------------- Unit 5: p210
add(
    S5, 210, "match",
    "Match each chest-radiograph sign on page 210 with its printed description — 1) Hampton's hump 2) Pallas sign 3) Westermark's sign 4) Fleischner sign … A) Enlarged central pulmonary artery B) Pleural based wedge shaped opacities C) Enlarged Rt descending artery D) Oligemia of Rt upper lung",
    "1-B, 2-C, 3-D, 4-A",
    ["1-B, 2-D, 3-C, 4-A", "1-A, 2-C, 3-D, 4-B", "1-C, 2-B, 3-A, 4-D"],
    "The figure captions read 'Pleural based wedge shaped opacities (Hamptons hump)', 'Enlarged Rt descending artery (Pallas sign)', 'Oligemia of Rt upper lung (Westermark's sign)' and 'Enlarged central pulmonary artery (Fleischner sign)'.",
)

add(
    S5, 210, "recall",
    "Which CXR finding on page 210 is marked as the most common?",
    "Long linear bands of atelectasis",
    ["Pleural based wedge shaped opacities", "Oligemia of the right upper lung", "Enlarged right descending artery"],
    "The first film is captioned 'Long linear bands of atelectasis (m/c)'. Hampton's hump, Westermark's and Pallas signs are all printed without a frequency label.",
)

add(
    S5, 210, "fillup",
    "Westermark's sign on page 210 is the ______ of the right upper lung.",
    "Oligemia",
    ["Hyperaemia", "Consolidation", "Calcification"],
    "The caption reads 'Oligemia of Rt upper lung (Westermark's sign)' — a zone of reduced vascular markings beyond the obstructed vessel, not increased flow or consolidation.",
)

add(
    S5, 210, "recall",
    "The page 210 PAH film is captioned with four findings. Which set is printed?",
    "Large central pulmonary arteries, right ventricular hypertrophy, rapid attenuation of pulmonary vessels, clear lung fields",
    [
        "Large central pulmonary arteries, left ventricular hypertrophy, delayed attenuation of pulmonary vessels, clear lung fields",
        "Small central pulmonary arteries, right ventricular hypertrophy, rapid attenuation of pulmonary vessels, bilateral infiltrates",
        "Large central pulmonary veins, right atrial enlargement, rapid attenuation of pulmonary vessels, clear lung fields",
    ],
    "The labelled film lists 'Large central pulmonary arteries', 'Right ventricular hypertrophy', 'Rapid attenuation of pulmonary vessels' and 'Clear lung fields'. The rapid tapering plus clear fields is what distinguishes vascular from parenchymal disease.",
)

add(
    S5, 210, "recall",
    "Two clinical purposes of the ECG in suspected PE are printed on page 210. Which pair?",
    "To rule out MI, and to identify RV strain/hypertrophy",
    [
        "To rule out pericarditis, and to identify LV strain/hypertrophy",
        "To confirm the embolus, and to grade its size",
        "To rule out MI, and to measure the pulmonary capillary wedge pressure",
    ],
    "The block reads 'Clinical significance : To rule out MI. To identify RV strain/ hypertrophy.' The ECG is adjunctive, not diagnostic — a point reinforced by the S1Q3T3 line being labelled non-specific.",
)

add(
    S5, 210, "truefalse",
    "TRUE or FALSE about the ECG patterns printed on page 210.",
    "True — the most common pattern is a normal ECG, while the most common abnormality is sinus tachycardia",
    [
        "False — the most common pattern is sinus tachycardia, the most common abnormality S1Q3T3",
        "False — the most common abnormality is T inversion in V1–V4",
        "True — S1Q3T3 is printed as a specific sign of RV infarction",
    ],
    "The patterns block reads 'Normal ECG : m/c pattern', 'Sinus tachycardia : m/c abnormality', 'Deep S waves in lead I > T inversion in V1–V4' and 'S1Q3T3 pattern : Non specific'. S1Q3T3 is explicitly non-specific.",
)

add(
    S5, 210, "oddoneout",
    "Pick the ODD ONE OUT — three are CXR captions from page 210, one is not printed there:",
    "Candle dripping appearance",
    ["Hampton's hump", "Westermark's sign", "Fleischner sign"],
    "Page 210 carries Hampton's hump, Pallas sign, Westermark's sign, Fleischner sign and long linear bands of atelectasis. 'Candle dripping' is the asbestos pleural-plaque sign printed much later, on page 227.",
)


# ---------------------------------------------------------------- Unit 6: p211
add(
    S6, 211, "recall",
    "Which investigation does page 211 name as the gold standard, and what is its stated drawback?",
    "Pulmonary angiography — it is invasive, cannulating a vein to reach the pulmonary artery",
    [
        "CTPA — it requires contrast and cannot be used in pregnancy",
        "V/Q scan — it is only valid in patients with a normal chest radiograph",
        "D-dimer — it is invasive and requires cannulation of the pulmonary artery",
    ],
    "The block reads 'Pulmonary angiography : gold standard' and 'Invasive : Cannulates vein to reach pulmonary artery'. CTPA is described on page 207 as the IOC, a different label.",
)

add(
    S6, 211, "match",
    "Match the investigation with its printed indication or purpose — 1) V/Q scan 2) D Dimer 3) ECHO … A) In low risk cases B) Pregnancy and contrast allergy C) To r/o alternate diagnosis (pericardial effusion)",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "Page 211 lists 'V/Q scan — Indications : Pregnancy. contrast allergy', 'D Dimer — In low risk cases' and 'ECHO — To r/o alternate diagnosis (Pericardial effusion)'. The D-dimer is a rule-out tool in low-risk patients, not a confirmatory test.",
)

add(
    S6, 211, "fillup",
    "Page 211's note states that any unexplained dyspnea with normal CXR/ECG/clinical examination is ______ unless proven otherwise.",
    "VTE",
    ["Pneumonia", "Anxiety hyperventilation", "Pulmonary oedema"],
    "The note reads 'Any unexplained dyspnea with normal CXR/ECG/clinical examination is VTE unless proven otherwise.' This is the page's answer to the 'clear lung fields' presentation described on page 207.",
)

add(
    S6, 211, "numeric",
    "In the Wells score table on page 211, two features score 3 points. Which two are printed?",
    "Clinical signs of DVT, and alternative diagnosis less likely",
    [
        "Clinical signs of DVT, and heart rate > 100/min",
        "Haemoptysis, and malignancy",
        "Recent surgery, and previous history of DVT/PE",
    ],
    "The two 3-point rows are 'Clinical signs of DVT' and 'Alternative diagnosis less likely'; HR >100/min, recent surgery and previous DVT/PE each score 1.5, and haemoptysis and malignancy each score 1.",
)

add(
    S6, 211, "match",
    "Match each Wells-score total with the printed features that produce it — 1) 3 points 2) 1.5 points 3) 1 point … A) Haemoptysis and malignancy B) Clinical signs of DVT and alternative diagnosis less likely C) Heart rate > 100/min, recent surgery and previous DVT/PE",
    "1-B, 2-C, 3-A",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "The table scores clinical signs of DVT 3, alternative diagnosis less likely 3, HR >100/min 1.5, recent surgery 1.5, previous DVT/PE 1.5, haemoptysis 1 and malignancy 1. The three score bands therefore group the seven rows exactly as listed.",
)

add(
    S6, 211, "recall",
    "How is the Wells score used on page 211 to choose imaging?",
    "Low risk → D-dimer, and only if positive → CTPA; moderate and high risk → helical CTPA",
    [
        "Low risk → helical CTPA; moderate and high risk → D-dimer followed by CTPA",
        "Low risk → V/Q scan; moderate and high risk → pulmonary angiography",
        "All risk groups → D-dimer first, then CTPA only if the D-dimer is negative",
    ],
    "The flowchart reads 'Risk → Low → D Dimer + → CTPA' with a brace joining 'moderate' and 'High' to 'Helical CTPA'. The D-dimer is used to avoid imaging in low-risk patients, not to trigger it when negative.",
)

add(
    S6, 211, "recall",
    "The two CT captions on page 211 describe a saddle embolus and the 'polo mint sign'. What does the printed line above the polo-mint image say?",
    "A thin rim of contrast persists around a central filling defect",
    [
        "A thick rim of thrombus surrounds a central contrast column",
        "Contrast fills the vessel completely with no filling defect",
        "A thin rim of thrombus persists around a central contrast column",
    ],
    "The caption reads 'Thin rim of contrast persists around a central filling defect' — the ring of contrast around the clot is what produces the polo-mint appearance.",
)


# ---------------------------------------------------------------- Unit 7: p212
add(
    S7, 212, "numeric",
    "The first dose of anticoagulant on page 212 is weight-based. Which two doses are printed?",
    "80 units/kg heparin IV, or 1 mg/kg s/c LMWH",
    [
        "80 units/kg heparin s/c, or 1 mg/kg IV LMWH",
        "100 units/kg heparin IV, or 1.5 mg/kg s/c LMWH",
        "18 units/kg heparin IV, or 1 mg/kg s/c LMWH",
    ],
    "The block reads 'First dose of anticoagulant : 80 units/kg heparin IV or 1 mg/kg s/c LMWH (Low molecular weight heparin)'. The 18 units/kg/hr figure belongs to the later infusion step, not the first dose.",
)

add(
    S7, 212, "recall",
    "After the first dose, page 212 asks the clinician to 'determine severity'. Which three findings are listed?",
    "Massive VTE (hypotension +), submassive VTE (RV dilatation +), extensive clot burden",
    [
        "Massive VTE (RV dilatation +), submassive VTE (hypotension +), minimal clot burden",
        "Massive VTE (hypotension +), submassive VTE (RV dilatation +), isolated calf DVT",
        "Massive VTE (troponin +), submassive VTE (BNP +), extensive clot burden",
    ],
    "The severity list is 'massive VTE (Hypotension +)', 'Submassive VTE (RV dilatation +)' and 'Extensive clot burden'. The bracket that decides 'Present' versus 'Absent' hangs off this severity assessment.",
)

add(
    S7, 212, "scenario",
    "A hypotensive patient with PE is judged fit for thrombolysis. Which regimen and time window are printed on page 212?",
    "Alteplase 100 mg IV, over 2 hrs, within 14 days",
    [
        "Alteplase 100 mg IV, over 2 hrs, within 7 days",
        "Alteplase 50 mg IV, over 1 hr, within 14 days",
        "Streptokinase 1.5 million units IV, over 2 hrs, within 14 days",
    ],
    "The thrombolysis branch reads 'Thrombolysis with Alteplase — 100 mg IV. — Over 2 hrs. — within 14 days.' followed by 'Restart heparin & replace with warfarin'.",
)

add(
    S7, 212, "recall",
    "For a patient who is unfit for thrombolysis, what does page 212 recommend, and how is it labelled?",
    "Catheter-based thrombolysis/embolectomy, marked as '(Preferred)'",
    [
        "Catheter-based thrombolysis/embolectomy, marked as a last resort",
        "Inferior vena cava filter, marked as '(Preferred)'",
        "Continue heparin alone, marked as '(Preferred)'",
    ],
    "The unfit branch reads 'Catheter-based thrombolysis/ embolectomy (Preferred)'. The IVC filter is reserved for the end-of-3-months branch when oral anticoagulation is contraindicated.",
)

add(
    S7, 212, "numeric",
    "For the 'Absent' severity branch, page 212 prints an infusion rate and two target ranges. Which set is printed?",
    "18 units/kg/hr heparin; aPTT 1.5–2 times the upper limit; INR 2–3",
    [
        "18 units/kg/hr heparin; aPTT 2–3 times the upper limit; INR 1.5–2",
        "80 units/kg/hr heparin; aPTT 1.5–2 times the upper limit; INR 2–3",
        "18 units/kg/hr heparin; aPTT 1.5–2 times the upper limit; INR 1.5–2",
    ],
    "The branch reads 'Continue anticoagulation at 18 units/kg/hr Heparin' with 'Target — aPTT : 1.5 – 2 times the upper limit' and 'INR : 2 – 3'. The aPTT target is applied to heparin and the INR to warfarin.",
)

add(
    S7, 212, "management",
    "At the end of 3 months, page 212 gives one switch rule and one exception pathway. Which statement matches the page?",
    "Switch to oral anticoagulants (new oral anticoagulants > warfarin/vit K), lifelong if a genetic mutation is positive; if contraindicated, insert an inferior vena cava filter",
    [
        "Switch to warfarin in preference to new oral anticoagulants, lifelong in all patients; if contraindicated, insert an inferior vena cava filter",
        "Stop anticoagulation at 3 months in all patients; if a genetic mutation is positive, extend heparin for 6 months",
        "Switch to oral anticoagulants, lifelong only if a genetic mutation is negative; if contraindicated, perform catheter embolectomy",
    ],
    "The block reads 'B. At the end of 3 months : Oral anticoagulants (New oral anticoagulants > warfarin/vit K) : Lifelong if genetic mutation (+). If C/I → Inferior vena cava filter.' The preference arrow points to the new oral agents, and lifelong therapy follows a positive genetic result.",
)

add(
    S7, 212, "truefalse",
    "TRUE or FALSE about the post-thrombolysis sequence printed on page 212.",
    "True — after thrombolysis the page says to restart heparin and then replace it with warfarin",
    [
        "False — after thrombolysis the page says to stop all anticoagulation",
        "False — after thrombolysis the page says to give an IVC filter first",
        "True — after thrombolysis the page says to continue alteplase for 14 days",
    ],
    "The line beneath the alteplase block reads 'Restart heparin & replace with warfarin.' Alteplase is a finite 2-hour infusion, not a 14-day one; 14 days is the outer limit for starting it.",
)


GUIDES = {
    S1: (
        "VTE Definition, Mortality, Thrombo-Embolic Pathogenesis, Origin of Thrombi, Acute Cor Pulmonale, Calf DVT & Massive VTE Pathogenesis Chain",
        "Venous thromboembolism (p206) is AKA pulmonary thromboembolism (PTE), with 60–80% mortality when massive. Pathogenesis is migration of thrombi/microthrombi from the systemic circulation to the pulmonary vasculature, and the origin is deep veins of the lower limb > upper limb, maximal risk from supra-popliteal veins draining to femoral veins and from pelvic veins in pregnancy.\n"
        "Note: acute cor pulmonale is RV dilatation/hypertrophy ± heart failure and its most common cause is VTE; calf DVT is the most common site but does not embolize.\n"
        "Massive VTE is any PE with hypotension. Its chain: >50–70% occlusion → hypoxaemia → RV & RA dilatation → septum pushed left → ↓LV volume → ↓cardiac output → SBP < 90 mmHg lasting ≥ 15 mins or requiring ionotropic support.",
    ),
    S2: (
        "Presentation, D/d of Dyspnea with Clear Lung Fields, Golden 4 Assessment (Clinical, ECHO/McConnel Sign, Biomarkers, CTPA) & Submassive/Non-Massive VTE",
        "Presentation (p207): unexplained dyspnea with clear lung fields is most common, chest pain is the second most common symptom, and sudden cardiac death and syncope complete the list; the only printed D/d for dyspnea with clear lung fields is VTE and metabolic acidosis.\n"
        "Golden 4: clinical hypotension; ECHO with McConnel's sign (hypocontractile RV free wall plus hypercontractile apex), septal push, LV contraction and exclusion of tamponade; biomarkers NT pro BNP for RV dilatation and troponin I for RV ischaemia; imaging with CTPA as IOC showing dilated PA, clot in PA and large RV.\n"
        "Submassive VTE has no hypotension — RV dilatation/ischaemia alone is low risk, escalating to high risk when the biomarkers rise. Non-massive VTE is 10–20% of cases from peripheral lodging, with recurrent/non-resolving pneumonia, cough, pleuritic pain and haemoptysis.",
    ),
    S3: (
        "Non-Massive VTE Investigations & Complications, Genetic and Acquired Risk-Factor Lists, Malignancy/Nephrotic/Surgery Risks & Ventilation-Perfusion Physiology",
        "Non-massive VTE (p208) has a normal ECHO, BP and biomarkers, and its complication is pulmonary infarction. Genetic risks are factor-V Leiden (most common), antithrombin III, protein C and protein S deficiency; acquired risks are antiphospholipid antibody syndrome, polycythaemia rubra vera, primary myelofibrosis, heparin-induced thrombocytopenia and paroxysmal nocturnal haemoglobinuria.\n"
        "Further risks: adenocarcinoma; COPD; heart failure with reduced ejection fraction; membranous nephropathy losing antithrombin III in urine; OCPs; HRT; pregnancy and post-partum; surgery with immobilisation > 4 days, orthopaedic surgery being higher risk.\n"
        "Physiology: ventilation and perfusion both maximal at the base, while the V/P ratio is maximal at the apex because perfusion falls more than ventilation.",
    ),
    S4: (
        "Dead-Space vs Shunt Physiology in PE, Symptoms/Signs, Vagal Bradycardia, Acute Cor Pulmonale Complications & Type I Respiratory Failure with A-a Gradient",
        "Dead-space physiology (p209) as in PE is V normal, P 0, V/P ∞; shunt physiology is V 0, P normal, V/P 0.\n"
        "Symptoms depend on embolus size and location: dyspnea within seconds > pleuritic chest pain in small peripheral emboli, with cough and haemoptysis in 10–20%. Signs run tachypnea > tachycardia > rales/↓breath sounds (10–20%), and hypoxia-induced intrapulmonary vagal stimulation causes bradycardia.\n"
        "Complications: acute cor pulmonale with shock in massive VTE, S3 plus hypotension in acute RV failure, and raised JVP; type I respiratory failure from V/Q mismatch with a normal PaCO2 (no parenchymal involvement), producing respiratory alkalosis and a widened alveolar-arterial O2 gradient. Type 2 failure is hypoxia plus hypercarbia in parenchymal disease.",
    ),
    S5: (
        "CXR Signs (Atelectatic Bands, Hampton's Hump, Pallas, Westermark, Fleischner), PAH Films & ECG Significance and Patterns (S1Q3T3)",
        "CXR (p210): long linear bands of atelectasis are the commonest sign; Hampton's hump is a pleural-based wedge-shaped opacity; Pallas sign is an enlarged right descending artery; Westermark's sign is oligaemia of the right upper lung; Fleischner sign is an enlarged central pulmonary artery. The PAH film shows large central pulmonary arteries, RV hypertrophy, rapid attenuation of vessels and clear lung fields.\n"
        "ECG is done to rule out MI and to identify RV strain/hypertrophy. A normal ECG is the commonest pattern and sinus tachycardia the commonest abnormality, with deep S in lead I exceeding T inversion in V1–V4; the S1Q3T3 pattern is non-specific.",
    ),
    S6: (
        "Pulmonary Angiography Gold Standard, V/Q Scan Indications, D-Dimer, ECHO, the Wells Score Table and CTPA Signs (Saddle Embolus, Polo Mint Sign)",
        "Pulmonary angiography (p211) is the gold standard and is invasive, cannulating a vein to reach the pulmonary artery. V/Q scan is indicated in pregnancy and contrast allergy; D-dimer is for low-risk cases; ECHO excludes alternate diagnoses such as pericardial effusion. Any unexplained dyspnea with a normal CXR/ECG/examination is VTE unless proven otherwise.\n"
        "Wells score: clinical signs of DVT 3, alternative diagnosis less likely 3, HR > 100/min 1.5, recent surgery 1.5, previous DVT/PE 1.5, haemoptysis 1, malignancy 1. Low risk goes to D-dimer and, if positive, CTPA; moderate and high risk go straight to helical CTPA.\n"
        "CT signs: saddle pulmonary embolism and the polo-mint sign, described as a thin rim of contrast persisting around a central filling defect.",
    ),
    S7: (
        "Management: Heparin/LMWH Dosing, Severity Determination, Thrombolysis vs Catheter Therapy, Heparin Target Ranges, 3-Month Switch and IVC Filter",
        "Management (p212) starts anticoagulation at the earliest with unfractionated heparin or LMWH: first dose 80 units/kg heparin IV or 1 mg/kg s/c LMWH. Severity is then determined as massive VTE (hypotension +), submassive VTE (RV dilatation +) or extensive clot burden.\n"
        "When severity is present: if fit for thrombolysis give alteplase 100 mg IV over 2 hrs within 14 days, then restart heparin and replace with warfarin; if unfit, catheter-based thrombolysis/embolectomy (preferred). When absent: continue heparin at 18 units/kg/hr targeting aPTT 1.5–2 times the upper limit and INR 2–3.\n"
        "At the end of 3 months switch to oral anticoagulants (new oral anticoagulants preferred over warfarin/vitamin K), lifelong if a genetic mutation is positive; if contraindicated, insert an inferior vena cava filter.",
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
