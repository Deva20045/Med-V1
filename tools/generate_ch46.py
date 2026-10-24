#!/usr/bin/env python3
"""Generate Chapter 46: Chronic Obstructive Pulmonary Disease (Book p267–273).

Every question is anchored to a printed line, table cell or figure caption of
uploads/03.pdf sheets 20–26 (Book pages 267–273), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 46
TITLE = "Chronic Obstructive Airway Disease"
PAGES = "267-273"

S1 = "GOLD 2023 Definition, the Clinical and Pathological Type Trees, the Spirometry Diagnosis Rule, the Eight Risk Factors and the Four Clinical Features"
S2 = "Chronic Bronchitis against Emphysema across Definition, Pathology, Age, Blue Bloater and Pink Puffer, Chest X-ray and PFT, with the Lobule and Respiratory Unit Notes and Centriacinar Disease"
S3 = "Panacinar, Paraseptal and Blank Irregular Emphysema, the Protease-Antiprotease Theory, the SERPINA-1 Alleles with PiMM and PiZZ, and the Spontaneous Pneumothorax Note"
S4 = "Large Airway Disease of Chronic Bronchitis against Asthma, Small Airway Disease of Emphysema, and the Driving-Pressure Physiology of Forced Exhalation"
S5 = "The Alveolar DLCO Split, the Hypoxia to Cor Pulmonale Chain, Emphysematous PFT with Reversibility Testing, the GOLD Grades and the ABE Tool"
S6 = "Inhaled Corticosteroid Indications and Contraindications, Group E against Groups A and B, LABA and LAMA Examples, and the Follow-up Treatment Flowchart"
S7 = "Long Term Oxygen Therapy, LVRS and the BODE Index, the Exacerbation Definition, its Three Causes and the Printed Treatment Bundle"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(46000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(46100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p267
add(
    S1, 267, "recall",
    "Which GOLD 2023 definition opens the chapter on page 267?",
    "Chronic persistent respiratory symptoms due to abnormalities of airway/alveoli resulting in progressive airflow limitation",
    [
        "Chronic persistent respiratory symptoms due to abnormalities of airway/alveoli resulting in reversible airflow limitation",
        "Acute respiratory symptoms due to infection of the airway/alveoli resulting in progressive airflow limitation",
        "Chronic intermittent respiratory symptoms due to pulmonary vascular disease resulting in progressive airflow limitation",
    ],
    "The two bullets read 'global initiative for COPD' and 'chronic persistent respiratory symptoms d/t abnormalities of airway/alveoli resulting in progressive airflow limitation'.",
)

add(
    S1, 267, "fillup",
    "The definition heading names GOLD 2023, in which GOLD stands for ______ initiative for COPD.",
    "global",
    ["graded", "guideline", "general"],
    "The first bullet expands the acronym as 'global initiative for COPD', lower-case 'g' as printed, before the definition itself.",
)

add(
    S1, 267, "match",
    "Match each COPD classification tree to its printed branches — 1) Based on clinical presentation 2) Based on pathology … A) Large airway, small airway (diameter <2 mm), alveoli, pulmonary vasculature B) Chronic bronchitis, emphysema",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The upper tree splits clinical presentation into chronic bronchitis and emphysema, while the lower tree splits pathology into large airway, small airway (diameter <2 mm), alveoli and pulmonary vasculature.",
)

add(
    S1, 267, "numeric",
    "At which diameter does the printed pathology tree define a small airway?",
    "<2 mm",
    ["<1 mm", "<3 mm", "<4 mm"],
    "The small airway branch carries the bracket '(Diameter <2 mm)', sitting between large airway and alveoli in the pathology tree.",
)

add(
    S1, 267, "recall",
    "How is the diagnosis of COPD made on page 267?",
    "Symptoms (dyspnea) plus spirometry for confirmation",
    [
        "Symptoms (dyspnea) plus chest X-ray for confirmation",
        "Symptoms (cough) plus CT for confirmation",
        "Spirometry alone, without symptoms",
    ],
    "The line reads 'Diagnosis: Symptoms (Dyspnea) + Spirometry (For confirmation)' — symptoms raise it and spirometry confirms it.",
)

add(
    S1, 267, "oddoneout",
    "Pick the ODD ONE OUT — three are printed risk factors for COPD on page 267, one reverses a printed word:",
    "High birth weight (post-term)",
    ["Smoke from cooking, fuels", "Occupational dust", "Low birth weight (Pre terms)"],
    "The risk list prints 'Low birth weight (Pre terms)' with tobacco smoking, cooking-fuel smoke, occupational dust, vapours, fumes and other chemicals; high birth weight is not on it.",
)

add(
    S1, 267, "recall",
    "Which four clinical features are listed for COPD on page 267?",
    "Dyspnea, chronic cough, recurrent lower respiratory tract infection and wheeze",
    [
        "Dyspnea, hemoptysis, recurrent lower respiratory tract infection and wheeze",
        "Dyspnea, chronic cough, clubbing and wheeze",
        "Fever, chronic cough, recurrent lower respiratory tract infection and wheeze",
    ],
    "The list is 'Dyspnea', 'Chronic cough', 'Recurrent lower respiratory tract infection (LRTI)' and 'wheeze'; hemoptysis and clubbing are not part of it.",
)

add(
    S1, 267, "fillup",
    "The dyspnea of COPD is persistent and progressive, and its printed aggravating factor is ______.",
    "exertion",
    ["cold air", "lying flat", "inspiration"],
    "Under dyspnea the page writes 'Persistent progressive' and 'Aggravating factor: Exertion', while the cough is described as intermittent with ± sputum production.",
)

add(
    S1, 267, "truefalse",
    "TRUE or FALSE about the chronic cough of COPD as printed on page 267.",
    "True — the cough is intermittent and may or may not produce sputum",
    [
        "True — the cough is continuous and always productive of copious sputum",
        "False — the cough is paroxysmal and always dry",
        "False — cough is not listed among the clinical features of COPD",
    ],
    "The cough bullets are 'Intermittent' and '± sputum production', the ± sign carrying the optional sputum.",
)

# ---------------------------------------------------------------- Unit 2: p268
add(
    S2, 268, "recall",
    "Which definition of chronic bronchitis is printed in the comparison table on page 268?",
    "A clinical disease defined by cough with sputum ≥3 months/year for ≥2 years",
    [
        "A pathological disease defined by dilatation of airway distal to the terminal bronchiole",
        "A clinical disease defined by cough with sputum ≥2 months/year for ≥3 years",
        "A physiological disease defined by reduced FEV1/FVC with hyperinflation",
    ],
    "The definition cell reads 'Clinical disease: Cough with sputum ≥3 months/year for ≥2 years' — the mirror image of the emphysema cell, which is pathological.",
)

add(
    S2, 268, "numeric",
    "Which duration pair defines chronic bronchitis in the table?",
    "≥3 months per year for ≥2 years",
    ["≥2 months per year for ≥3 years", "≥3 months per year for ≥3 years", "≥6 months per year for ≥2 years"],
    "The cell prints 'Cough with sputum ≥3 months/year for ≥2 years', the standard clinical definition placed under the 'Clinical disease' heading.",
)

add(
    S2, 268, "recall",
    "Which definition of emphysema is printed beside chronic bronchitis on page 268?",
    "A pathological disease: dilatation of airway distal to the terminal bronchiole followed by destruction of wall and air spaces",
    [
        "A pathological disease: dilatation of airway proximal to the terminal bronchiole with intact alveolar walls",
        "A clinical disease: cough with sputum for ≥3 months/year for ≥2 years",
        "A pathological disease: fibrosis of the alveolar interstitium with honeycomb change",
    ],
    "The emphysema cell is 'Pathological disease: Dilatation of airway distal to terminal bronchiole followed by destruction of wall & air spaces' — destruction is the operative word.",
)

add(
    S2, 268, "match",
    "Match each disease to its printed pathology — 1) Chronic bronchitis 2) Emphysema … A) Small airway disease of the abnormal alveolo-capillary unit, minimal parenchymal damage, exhale CO₂ and ↓ elastic recoil B) Large airway disease plus parenchymal destruction",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The pathology row gives chronic bronchitis 'Large airway disease + parenchymal destruction' and emphysema 'Small airway disease: Abnormal alveolo-capillary unit (Affects diffusion)', minimal parenchymal damage with CO₂ exhalation and reduced elastic recoil.",
)

add(
    S2, 268, "match",
    "Match each disease to its printed age band — 1) Chronic bronchitis 2) Emphysema … A) 50–75 years (elderly) B) 40–45 years",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The age row reads 40–45 years for chronic bronchitis and 50–75 years (elderly) for emphysema.",
)

add(
    S2, 268, "recall",
    "Which chain produces the blue bloater picture in the chronic bronchitis column?",
    "Cough with copious sputum, hypoxia → cyanosis, right ventricle failure → edema, type II respiratory failure with ↓PaO₂ and ↑PaCO₂, and cor pulmonale with RV hypertrophy/dilatation ± failure",
    [
        "Severe dyspnea with ↑ work of breathing → ↓PCO₂, cachexia, Hoover sign and type I respiratory failure",
        "Cough with copious sputum, hyperinflation with ↑AP diameter and a small heart",
        "Cough with copious sputum, type I respiratory failure with ↓PaO₂ and ↓PaCO₂, and left ventricular failure",
    ],
    "The blue bloater branch prints hypoxia → cyanosis and RV failure → edema, then type II failure '↓PaO2 ↑PaCO2' and cor pulmonale 'RV hypertrophy/dilatation ± failure', with infections listed as well.",
)

add(
    S2, 268, "recall",
    "Which cluster belongs to the pink puffer column of the table?",
    "Severe dyspnea, ↑ work of breathing → ↓PCO₂, cachectic, Hoover sign, hyper resonance, pursed lips and type I respiratory failure",
    [
        "Cough with copious sputum, cyanosis, edema and type II respiratory failure",
        "Severe dyspnea, ↑ work of breathing → ↑PCO₂, obesity and type II respiratory failure",
        "Mild dyspnea, hyper resonance, cor pulmonale and type II respiratory failure",
    ],
    "The emphysema column lists severe dyspnea, ↑ work of breathing → ↓PCO₂, cachectic, Hoover sign, hyper resonance, pursed lips and type I respiratory failure — the mirror image of the blue bloater.",
)

add(
    S2, 268, "match",
    "Match each disease to its printed chest X-ray — 1) Chronic bronchitis 2) Emphysema … A) Hyperinflation of lung (AP diameter ↑) and small heart B) Prominent vessels and large heart",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The CXR row gives prominent vessels and a large heart for chronic bronchitis against hyperinflation with increased AP diameter and a small heart for emphysema.",
)

add(
    S2, 268, "match",
    "Match each disease to its printed pulmonary function — 1) Chronic bronchitis 2) Emphysema … A) TLC and RV increased with DLCO decreased B) TLC normal with DLCO normal",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The PFT row reads TLC normal and DLCO normal for chronic bronchitis, while emphysema raises TLC and RV and lowers DLCO.",
)

add(
    S2, 268, "fillup",
    "The note beneath the table names the functional unit of the lung as the ______ pulmonary lobule.",
    "secondary",
    ["primary", "tertiary", "respiratory"],
    "The note bullet reads 'Functional unit of lung: Secondary pulmonary lobule', the next bullet defining the respiratory unit separately.",
)

add(
    S2, 268, "recall",
    "Which structures make up the respiratory unit of the lung in the printed note?",
    "Everything distal to the terminal bronchiole — respiratory bronchiole → alveolar duct → alveoli",
    [
        "Everything distal to the secondary pulmonary lobule — alveolar duct → alveoli only",
        "The terminal bronchiole with its cartilage and the alveoli",
        "The respiratory bronchiole and the pulmonary capillary bed, without alveoli",
    ],
    "The note reads 'Respiratory unit of lung: Distal to terminal bronchiole (Respiratory bronchiole → Alveolar duct → Alveoli)', the arrow sequence being the tested part.",
)

add(
    S2, 268, "recall",
    "Which three characteristics are printed for centriacinar emphysema?",
    "Most common, seen in smokers, and involves the upper lobe of lung",
    [
        "Second most common, seen in non-smokers, and involves the lower lobe of lung",
        "Most common, seen in non-smokers, and involves the lower lobe of lung",
        "Rare, seen in young male smokers, and associated with spontaneous pneumothorax",
    ],
    "The centriacinar row lists 'most common', 'seen in smokers' and 'involve upper lobe of lung' beside the diagram of respiratory bronchiole involvement.",
)

# ---------------------------------------------------------------- Unit 3: p269
add(
    S3, 269, "recall",
    "Which four features are printed for panacinar (entire acinus) emphysema?",
    "Age <45 years, seen in non-smokers, involves the lower lobe (basilar), and is associated with vasculitis, liver disease and bronchiectasis from α-1 antitrypsin deficiency",
    [
        "Age >45 years, seen in smokers, involves the upper lobe, and is associated with spontaneous pneumothorax",
        "Age <45 years, seen in smokers, involves the upper lobe, and is associated with α-1 antitrypsin deficiency",
        "Young male smoker, involves the lower lobe, and is associated with spontaneous pneumothorax",
    ],
    "The panacinar row reads 'Age <45 years', 'Seen in non-smokers', 'Involve lower lobe of lung (Basilar)' and 'Associated with vasculitis, liver disease, bronchiectasis (α-1 antitrypsin deficiency)'.",
)

add(
    S3, 269, "recall",
    "Which two features are printed for paraseptal emphysema?",
    "Young male smoker and associated with spontaneous pneumothorax",
    [
        "Elderly female non-smoker and associated with vasculitis",
        "Young male smoker and associated with α-1 antitrypsin deficiency",
        "Non-smoker below 45 years and involves the basilar lower lobe",
    ],
    "The paraseptal row has only two cells filled — 'Young male smoker' and 'Associated with spontaneous pneumothorax' — with the diagram showing subpleural alveolar ducts and alveoli.",
)

add(
    S3, 269, "fillup",
    "The third row of the classification table, irregular emphysema, is printed with a characteristics cell containing only ______.",
    "a dash",
    ["upper lobe involvement", "smoker status", "α-1 antitrypsin deficiency"],
    "The irregular row shows the diagram of terminal bronchiole with alveolar ducts and alveoli but the characteristics column contains just '–', a blank the reader is expected to notice.",
)

add(
    S3, 269, "recall",
    "Which protease-antiprotease pathway is drawn on page 269?",
    "α-1 antitrypsin inhibits neutrophil elastase, which otherwise destroys extracellular matrix, and the protein is encoded by the SERPINA-1 gene",
    [
        "α-1 antitrypsin activates neutrophil elastase, which then destroys extracellular matrix, and the protein is encoded by the SERPINA-1 gene",
        "Neutrophil elastase inhibits α-1 antitrypsin, which otherwise destroys extracellular matrix, and the protein is encoded by the SERPINA-1 gene",
        "α-1 antitrypsin inhibits neutrophil elastase, which otherwise destroys extracellular matrix, and the protein is encoded by the alpha-1 globulin gene",
    ],
    "The flow reads 'α-1 antitrypsin ↓Inhibit Neutrophil elastase' over the arrow 'SERPINA-1 gene → Extracellular matrix destruction', i.e. antitrypsin restrains elastase.",
)

add(
    S3, 269, "fillup",
    "α-1 antitrypsin, the inhibitor of neutrophil elastase, is encoded by the ______ gene.",
    "SERPINA-1",
    ["SERPINB-1", "SERPINC-1", "SERPINE-1"],
    "The label under the enzyme in the flow diagram reads 'SERPINA-1 gene', naming the gene before the arrow to extracellular matrix destruction.",
)

add(
    S3, 269, "recall",
    "Which statement of the protease-antiprotease theory is printed on page 269?",
    "Deficiency of α-1 antitrypsin raises neutrophil elastase activity",
    [
        "Deficiency of α-1 antitrypsin lowers neutrophil elastase activity",
        "Excess of α-1 antitrypsin raises neutrophil elastase activity",
        "Deficiency of neutrophil elastase raises α-1 antitrypsin activity",
    ],
    "The theory bullet reads 'Deficiency of α-1 antitrypsin: ↑ neutrophil elastase activity', from which the matrix destruction and panacinar pattern follow.",
)

add(
    S3, 269, "match",
    "Match each genotype to its printed meaning — 1) PiMM 2) PiZZ … A) Disease (+) and the most common form of α-1 antitrypsin deficiency B) Normal",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The genetics block lists the m, Z and Null alleles, then 'PiMM: Normal' and 'PiZZ: Disease (+) (m/c form of α-1 antitrypsin deficiency)'.",
)

add(
    S3, 269, "oddoneout",
    "Pick the ODD ONE OUT — three are printed under spontaneous pneumothorax on page 269, one is not:",
    "Centriacinar emphysema",
    ["Paraseptal emphysema", "Langerhans cell histiocytosis", "Lymphangioma hematosis"],
    "The note lists paraseptal change, Langerhans cell histiocytosis and 'Lymphangioma hematosis' as printed. Centriacinar disease belongs to the smoker's upper-lobe pattern, not this list.",
)

# ---------------------------------------------------------------- Unit 4: p270
add(
    S4, 270, "recall",
    "Which set of large-airway changes is printed for chronic bronchitis on page 270?",
    "Neutrophils in sputum, squamous metaplasia of epithelium, no basement membrane thickening, ↑ macrophages, ↑ CD8+ lymphocytes, goblet cell hyperplasia with mucous hypersecretion, and little increase in airway smooth muscle giving no hyperresponsive symptoms",
    [
        "Neutrophils in sputum, squamous metaplasia of epithelium, basement membrane thickening, and a severe increase in airway smooth muscle giving hyperresponsive symptoms",
        "Eosinophils in sputum, epithelial necrosis, basement membrane thickening and severe bronchospasm",
        "Neutrophils in sputum, goblet cell hyperplasia, and loss of cartilage with airway collapse",
    ],
    "The diagram labels all of those large-airway features and ends 'Little increase in airway smooth muscle → No hyperresponsive symptoms', which is the point separating it from asthma.",
)

add(
    S4, 270, "match",
    "Match each feature to the asthma column of the note table — 1) Bronchospasm 2) Necrosis of epithelium 3) Squamous metaplasia 4) Mucus secretion … A) Severe (↑ airway smooth muscle) B) Present C) Absent D) Increased",
    "1-A, 2-B, 3-C, 4-D",
    ["1-A, 2-C, 3-B, 4-D", "1-B, 2-A, 3-C, 4-D", "1-A, 2-B, 3-D, 4-C"],
    "The table gives asthma severe bronchospasm, present epithelial necrosis, absent squamous metaplasia and increased mucus secretion, exactly inverting the chronic bronchitis column for the first three.",
)

add(
    S4, 270, "fillup",
    "In the note table, necrosis of epithelium is ______ in chronic bronchitis and present in asthma.",
    "absent",
    ["mild", "severe", "focal"],
    "The chronic bronchitis column reads bronchospasm mild, mucus secretion increased, necrosis of epithelium absent and squamous metaplasia present.",
)

add(
    S4, 270, "recall",
    "Which changes are labelled in the small airway diagram of emphysema?",
    "Inflammatory exudate in the lumen, a wall thickened by inflammatory cells, macrophages, CD8+ cells and fibroblasts, peribronchial fibrosis, a lymphoid follicle and disrupted alveolar attachments",
    [
        "Squamous metaplasia, goblet cell hyperplasia and neutrophils in the sputum",
        "Inflammatory exudate in the lumen with an intact alveolar attachment and no fibrosis",
        "Basement membrane thickening, eosinophils and severe bronchospasm",
    ],
    "The small airway diagram labels inflammatory exudate in the lumen, thickened wall with inflammatory cells, macrophages, CD8+ cells and fibroblast, peribronchial fibrosis, lymphoid follicle and disrupted alveolar attachments; squamous metaplasia and goblet hyperplasia belong to the large airway panel.",
)

add(
    S4, 270, "recall",
    "Which consequence follows the disrupted alveolar attachments in emphysema?",
    "↓ ERP → alveoli are easily inflatable → hyperinflated lung with ↑ TLC and ↑ RV",
    [
        "↑ ERP → alveoli are stiff → restrictive lung with ↓ TLC and ↓ RV",
        "↓ ERP → alveoli collapse → reduced lung volumes with ↓ TLC and ↓ RV",
        "↑ ERP → airway collapse → air trapping with normal TLC and RV",
    ],
    "The arrows read 'Disrupted alveolar attachments → ↓ ERP → Alveoli are easily inflatable → Hyperinflated lung (↑ TLC, ↑ RV)'.",
)

add(
    S4, 270, "fillup",
    "The driving pressure of exhalation is printed as DP = intrapleural pressure (IPP) + ______ pressure (ERP).",
    "elastic recoil",
    ["airway", "alveolar", "transpulmonary"],
    "The physiology line reads 'DP = Intrapleural pressure (IPP) + elastic recoil pressure (ERP)', and forceful exhalation then raises IPP while lowering ERP.",
)

add(
    S4, 270, "recall",
    "What happens to driving pressure during forceful exhalation, and why?",
    "It falls below airway pressure because IPP rises and ERP falls",
    [
        "It rises above airway pressure because IPP rises and ERP falls",
        "It falls below airway pressure because IPP falls and ERP rises",
        "It stays equal to airway pressure because IPP and ERP change in parallel",
    ],
    "The page writes 'Forceful exhalation: ↑ IPP, ↓ ERP → DP < AP', the fall in driving pressure being the mechanism of dynamic airway compression.",
)

add(
    S4, 270, "recall",
    "Why do the bronchi but not the distal airways resist collapse in emphysema?",
    "Cartilage is present at the bronchi and prevents collapse, whereas airways collapse, trap air and raise the work of breathing",
    [
        "Cartilage is present at the bronchi, and the distal airways are held open by surfactant",
        "The bronchi have no cartilage and collapse, whereas the distal airways are held open by elastic recoil",
        "Both bronchi and distal airways are cartilaginous, but only the distal airways trap air",
    ],
    "The two bullets read 'At bronchi → Cartilage present (Prevents collapse)' and 'At airways → Collapse → Air trapping → ↑ work of breathing → Dyspnea'.",
)

add(
    S4, 270, "oddoneout",
    "Pick the ODD ONE OUT — three are large-airway features of chronic bronchitis on page 270, one belongs to asthma:",
    "Severe increase in airway smooth muscle",
    ["Goblet cell hyperplasia", "Squamous metaplasia of epithelium", "Neutrophils in sputum"],
    "Chronic bronchitis has only a little increase in airway smooth muscle; severe increase with hyperresponsive symptoms is the asthma side of the note table.",
)

# ---------------------------------------------------------------- Unit 5: p271
add(
    S5, 271, "match",
    "Match each structure and disease pair to its printed DLCO — 1) Parenchyma — chronic bronchitis 2) Alveolo-capillary unit — emphysema … A) Reduced B) Normal",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The alveoli table lists parenchyma with chronic bronchitis and a normal DLCO, against the alveolo-capillary unit with emphysema and a reduced DLCO.",
)

add(
    S5, 271, "recall",
    "Which chain is drawn under pulmonary vasculature on page 271?",
    "Parenchyma damage → chronic hypoxia (↓PaO₂, ↑PaCO₂) → pulmonary vasoconstriction → pulmonary hypertension → cor pulmonale → edema and death",
    [
        "Parenchyma damage → chronic hypoxia (↑PaO₂, ↓PaCO₂) → pulmonary vasodilatation → pulmonary hypertension → cor pulmonale → edema and death",
        "Parenchyma damage → chronic hypercapnia → systemic vasoconstriction → systemic hypertension → left ventricular failure → death",
        "Parenchyma damage → chronic hypoxia → pulmonary vasoconstriction → pulmonary hypotension → cor pulmonale → edema and death",
    ],
    "The flow runs through chronic hypoxia with ↓PaO2 and ↑PaCO2, pulmonary vasoconstriction, pulmonary hypertension, cor pulmonale and then edema or death.",
)

add(
    S5, 271, "recall",
    "Which spirometry pattern is printed for emphysema?",
    "FEV₁ reduced, FVC normal and FEV₁/FVC reduced",
    [
        "FEV₁ reduced, FVC reduced and FEV₁/FVC normal",
        "FEV₁ normal, FVC reduced and FEV₁/FVC increased",
        "FEV₁ reduced, FVC normal and FEV₁/FVC increased",
    ],
    "The three bullets are 'FEV1: Reduced', 'FVC: Normal' and 'FEV1/FVC: Reduced', which then triggers the bronchodilator reversibility step.",
)

add(
    S5, 271, "numeric",
    "Below which FEV₁/FVC ratio does the page send the patient for bronchodilator reversibility testing?",
    "0.7",
    ["0.5", "0.6", "0.8"],
    "The arrow reads 'If FEV1/FVC: <0.7 → Bronchodilator reversibility testing', the same threshold that confirms COPD after bronchodilator later on the page.",
)

add(
    S5, 271, "recall",
    "How does the reversibility branch divide asthma from COPD?",
    "A positive test (FEV₁ rising by 200 mL or 12%) means asthma, and a negative test means COPD",
    [
        "A positive test (FEV₁ rising by 200 mL or 12%) means COPD, and a negative test means asthma",
        "A positive test (FEV₁ rising by 100 mL or 10%) means asthma, and a negative test means COPD",
        "A positive test (FEV₁ falling by 200 mL or 12%) means asthma, and a negative test means COPD",
    ],
    "The tree marks 'Positive → Asthma (FEV₁ ↑ by 200 mL or 12%)' and 'Negative → COPD', the magnitude and percentage both required as printed.",
)

add(
    S5, 271, "match",
    "Match each GOLD grade to its printed post-bronchodilator FEV₁ — 1) GOLD 1 2) GOLD 2 3) GOLD 3 4) GOLD 4 … A) <30% B) ≥80% C) <50% D) <80%",
    "1-B, 2-D, 3-C, 4-A",
    ["1-B, 2-C, 3-D, 4-A", "1-D, 2-B, 3-C, 4-A", "1-B, 2-D, 3-A, 4-C"],
    "The grade table reads GOLD 1 ≥80%, GOLD 2 <80%, GOLD 3 <50% and GOLD 4 <30% of predicted FEV₁.",
)

add(
    S5, 271, "recall",
    "What defines group E in the GOLD ABE assessment tool, and what does the tool otherwise ask you to assess?",
    "≥2 exacerbations or 1 hospitalization/year, alongside symptom and risk assessment after spirometry has confirmed airflow obstruction",
    [
        "0–1 moderate exacerbation, alongside symptom assessment only",
        "≥2 exacerbations or 1 hospitalization/year, assessed without spirometry",
        "A single mild exacerbation with stable dyspnea, alongside risk assessment only",
    ],
    "The right-hand box prints '≥ 2 exacerbations or 1 hospitalization/year' over groups A and B, while the flow runs spirometry → assess airflow obstruction → assess symptoms/risks.",
)

add(
    S5, 271, "fillup",
    "COPD is confirmed when the post-bronchodilator FEV₁/FVC is <______.",
    "0.7",
    ["0.5", "0.6", "0.8"],
    "Under 'Diagnosis confirmed' the tool prints 'Post bronchodilator FEV1/FVC : <0.7', the same cut-off used to enter reversibility testing.",
)

add(
    S5, 271, "recall",
    "What does page 271 say about oral glucocorticoids in COPD?",
    "They carry increased side effects and reduced benefits",
    [
        "They carry reduced side effects and increased benefits",
        "They carry increased side effects but are the first-line maintenance drug",
        "They carry no side effects and replace inhaled corticosteroids",
    ],
    "The single steroid line is 'Oral glucocorticoids: ↑ side effects, ↓ benefits', which sets up the inhaled corticosteroid indications overleaf.",
)

# ---------------------------------------------------------------- Unit 6: p272
add(
    S6, 272, "match",
    "Match each inhaled corticosteroid indication on page 272 to its printed threshold — 1) Blood eosinophils 2) Exacerbation frequency 3) History … A) ≥2 moderate exacerbations/year B) ≥300 cells/μL C) Concomitant asthma",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "The indications list blood eosinophils ≥300 cells/μL, ≥2 moderate exacerbations/year, a history of concomitant asthma and a history of hospitalisation for an asthma exacerbation.",
)

add(
    S6, 272, "oddoneout",
    "Pick the ODD ONE OUT — three are printed contraindications to inhaled corticosteroids on page 272, one is an indication:",
    "Blood eosinophils ≥300 cells/μL",
    ["Repeated pneumonia", "Blood eosinophils <100 cells/μL", "History of tuberculosis"],
    "The contraindication list is repeated pneumonia (with increased risk in COPD), blood eosinophils <100 cells/μL and a history of tuberculosis; ≥300 cells/μL is the indication at the top of the page.",
)

add(
    S6, 272, "numeric",
    "Which pair of blood eosinophil cut-offs separates the indication from the contraindication on page 272?",
    "≥300 cells/μL for the indication and <100 cells/μL for the contraindication",
    [
        "≥100 cells/μL for the indication and <300 cells/μL for the contraindication",
        "≥200 cells/μL for the indication and <50 cells/μL for the contraindication",
        "≥300 cells/μL for both the indication and the contraindication",
    ],
    "The indications begin 'Blood eosinophils ≥300 cells/μL' and the contraindications include 'Blood eosinophils <100 cells/μL', leaving a grey zone between them.",
)

add(
    S6, 272, "fillup",
    "According to the 2019 guidelines printed on page 272, the use of steroids in COPD should be ______.",
    "reduced",
    ["increased", "continued unchanged", "restricted to oral only"],
    "The line under the contraindications reads 'According to 2019 guidelines: Reduce usage of steroids', explaining why the indications are written as a short list.",
)

add(
    S6, 272, "recall",
    "What does the Note box beside medical management say about asthma?",
    "In asthma the combination is ICS + formoterol",
    [
        "In asthma the combination is ICS + salmeterol only",
        "In asthma inhaled corticosteroids are contraindicated",
        "In asthma the combination is LABA + LAMA without ICS",
    ],
    "The box reads 'Note: In asthma: ICS + Formoterol', distinguishing the asthma strategy from the group-based COPD algorithm beside it.",
)

add(
    S6, 272, "recall",
    "Which initial treatment is printed for a COPD patient with ≥2 moderate exacerbations or ≥1 hospitalization?",
    "Group E: LABA + LAMA ± ICS if blood eosinophils are ≥300",
    [
        "Group A: LABA/LAMA bronchodilator only",
        "Group B: LABA + LAMA with ICS for everyone",
        "Group E: ICS alone, with no bronchodilator",
    ],
    "The first row of the initial-treatment table prints group E with 'LABA + LAMA ± ICS (If blood eosinophils ≥300)' against that exacerbation criterion.",
)

add(
    S6, 272, "match",
    "Match each drug class to its printed example — 1) LABA 2) LAMA … A) Tiotropium B) Formoterol and indacaterol",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The page writes 'LABA (Long acting β agonist): Formoterol, Indacaterol' and 'LAMA (Long acting muscarinic agonist): Tiotropium'.",
)

add(
    S6, 272, "recall",
    "In the follow-up flowchart, what happens after blood eosinophils are checked in a patient with continuing exacerbations?",
    "Below 300 the patient moves to LAMA + LABA, above 300 to LAMA + LABA + ICS",
    [
        "Below 300 the patient moves to LAMA + LABA + ICS, above 300 to LAMA + LABA",
        "Below 300 the patient moves to ICS alone, above 300 to triple therapy with roflumilast",
        "Eosinophils do not change treatment; both arms receive LABA/LAMA",
    ],
    "The two arms read '<300 → LAMA + LABA' and '>300 → LAMA + LABA + ICS', after the entry LABA/LAMA for exacerbation.",
)

add(
    S6, 272, "recall",
    "Which drug is added for a patient unresponsive to treatment who has chronic bronchitis with FEV₁ <50%, and which for one with a history of smoking or emphysema?",
    "Roflumilast (a phosphodiesterase-4 inhibitor) for the first, and azithromycin for the second",
    [
        "Azithromycin for the first, and roflumilast for the second",
        "Roflumilast for both, at different doses",
        "Tiotropium for the first, and formoterol for the second",
    ],
    "The bottom of the flowchart pairs 'Chronic bronchitis with FEV1 <50% → Roflumilast (Phosphodiesterase-4 inhibitor)' with 'H/o smoking/emphysema → Azithromycin'.",
)

# ---------------------------------------------------------------- Unit 7: p273
add(
    S7, 273, "numeric",
    "For how many hours a day are oxygen concentrators used in long term oxygen therapy as printed?",
    "15–16 hours/day",
    ["8–10 hours/day", "12–14 hours/day", "20–24 hours/day"],
    "The line reads 'O2 concentrators: 15–16 hours/day', above the two indications for LTOT.",
)

add(
    S7, 273, "recall",
    "Which two indications for long term oxygen therapy are printed on page 273?",
    "PaO₂ <55 mm Hg, and PaO₂ 55–60 mm Hg associated with polycythemia or right heart failure",
    [
        "PaO₂ <60 mm Hg, and PaO₂ 60–70 mm Hg associated with polycythemia or right heart failure",
        "PaO₂ <55 mm Hg, and PaO₂ 55–60 mm Hg associated with any breathlessness",
        "PaO₂ <50 mm Hg, and PaCO₂ 55–60 mm Hg associated with polycythemia",
    ],
    "The list reads 'PaO2 <55 mm Hg' and 'PaO2: 55–60 mm Hg associated with polycythemia or right heart failure', the qualifier being what licenses oxygen in the upper band.",
)

add(
    S7, 273, "fillup",
    "Lung volume reduction surgery is contraindicated if FEV₁ is <______.",
    "20%",
    ["30%", "40%", "50%"],
    "The surgical line reads 'Lung volume reduction surgery (LVRS): contraindicated if FEV₁ <20%'.",
)

add(
    S7, 273, "match",
    "Match each letter of the BODE index to its printed component — 1) B 2) O 3) D 4) E … A) Dyspnea B) BMI C) Exercise capacity D) Obstructive ventilatory defect",
    "1-B, 2-D, 3-A, 4-C",
    ["1-B, 2-A, 3-D, 4-C", "1-D, 2-B, 3-A, 4-C", "1-B, 2-D, 3-C, 4-A"],
    "The note lists 'B: BMI', 'O: Obstructive ventilatory defect', 'D: Dyspnoea' and 'E: Exercise capacity' — the multidimensional index behind the four letters.",
)

add(
    S7, 273, "numeric",
    "An exacerbation event is defined by dyspnea and/or cough with sputum lasting less than how long?",
    "14 days",
    ["7 days", "10 days", "21 days"],
    "The line reads 'Exacerbation event: Characterized by dyspnea &/or cough with sputum <14 days associated with systemic inflammation'.",
)

add(
    S7, 273, "match",
    "Match each cause of exacerbation to its printed clue — 1) Pulmonary embolism 2) Heart failure 3) Pneumonia … A) X-ray, ECHO and NT-pro BNP B) History of surgery, fracture or DVT C) No clue bracketed",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "The causes list reads pneumonia with no bracket, 'Pulmonary embolism (H/o surgery, fracture, DVT)' and 'Heart failure (X-ray, ECHO, NT-pro BNP)'.",
)

add(
    S7, 273, "recall",
    "Which drug pair is printed for the acute exacerbation, below nebulization and IV hydrocortisone 100 mg?",
    "A short acting β-agonist (salbutamol) plus a short acting anticholinergic (ipratropium bromide)",
    [
        "A long acting β-agonist (formoterol) plus a long acting anticholinergic (tiotropium)",
        "A short acting β-agonist (salbutamol) plus IV magnesium sulphate only",
        "Inhaled corticosteroid plus oral azithromycin only",
    ],
    "The treatment list runs nebulization, IV hydrocortisone 100 mg, then 'Short acting β-agonist (Salbutamol) + Short acting anticholinergic (Ipratropium bromide)', then MgSO₄.",
)

add(
    S7, 273, "fillup",
    "In the exacerbation bundle, antibiotics are given for ______ days and oral steroids for 7 days.",
    "5",
    ["3", "7", "10"],
    "The two lines read 'Antibiotics × 5 days (For pneumonia)' and 'Short course oral steroids × 7 days', with ICS added only for recurrent exacerbations.",
)

add(
    S7, 273, "truefalse",
    "TRUE or FALSE about methylxanthines in the exacerbation treatment printed on page 273.",
    "False — the note states there is no role for methylxanthines",
    [
        "True — methylxanthines are added after magnesium sulphate",
        "True — methylxanthines replace nebulized bronchodilators",
        "False — methylxanthines are the first-line agent before nebulization",
    ],
    "The closing note reads 'Note: No role for methylxanthines', so they are neither first line nor an add-on in this bundle.",
)

add(
    S7, 273, "recall",
    "Which step follows magnesium sulphate in the printed exacerbation sequence?",
    "Ventilation, non invasive → invasive",
    [
        "Intravenous antibiotics",
        "Oral steroids for 7 days",
        "Inhaled corticosteroids for recurrent exacerbations",
    ],
    "The arrow after 'mgSO₄' drops to 'ventilation: Non invasive → Invasive', with antibiotics, steroids and ICS listed beneath it.",
)

# ---------------------------------------------------------------- extra interactives
add(
    S1, 267, "scenario",
    "A 62-year-old smoker has two years of progressive exertional dyspnea and intermittent cough; spirometry after bronchodilator shows FEV₁/FVC 0.62. What does page 267 require for the diagnosis of COPD?",
    "Symptoms of dyspnea plus spirometry for confirmation, with post-bronchodilator FEV₁/FVC below 0.7",
    [
        "Symptoms of dyspnea alone, spirometry being supportive only",
        "Chest X-ray hyperinflation plus symptoms, spirometry being optional",
        "A normal FEV₁/FVC but a reduced DLCO",
    ],
    "The diagnosis line is 'Symptoms (Dyspnea) + Spirometry (For confirmation)', and page 271 adds the post-bronchodilator FEV₁/FVC <0.7 that confirms airflow obstruction.",
)

add(
    S2, 268, "truefalse",
    "TRUE or FALSE about the clinical definition of chronic bronchitis on page 268.",
    "True — cough with sputum for at least 3 months a year for 2 consecutive years defines it clinically",
    [
        "True — cough with sputum for at least 2 months a year for 3 consecutive years defines it clinically",
        "False — chronic bronchitis is defined pathologically by airspace destruction",
        "False — chronic bronchitis requires a reduced DLCO for diagnosis",
    ],
    "The definition cell reads 'Clinical disease: Cough with sputum ≥3 months/year for ≥2 years', while DLCO is normal in chronic bronchitis and destruction of airspaces defines emphysema.",
)

add(
    S3, 269, "scenario",
    "A 38-year-old non-smoker has basilar emphysema with a history of liver disease and bronchiectasis. Which printed emphysema type and enzyme defect fit?",
    "Panacinar emphysema with α-1 antitrypsin deficiency",
    [
        "Centriacinar emphysema with α-1 antitrypsin deficiency",
        "Paraseptal emphysema with α-1 antitrypsin deficiency",
        "Irregular emphysema with neutrophil elastase excess",
    ],
    "Panacinar disease occurs below 45 years in non-smokers, in the basilar lower lobe, and is 'Associated with vasculitis, liver disease, bronchiectasis (α-1 antitrypsin deficiency)'.",
)

add(
    S4, 270, "oddoneout",
    "Pick the ODD ONE OUT — three are printed as small airway changes of emphysema on page 270, one belongs to the large airway panel:",
    "Goblet cell hyperplasia with mucous hypersecretion",
    ["Inflammatory exudate in the lumen", "Peribronchial fibrosis", "Lymphoid follicle"],
    "The small airway diagram labels luminal exudate, peribronchial fibrosis and a lymphoid follicle; goblet cell hyperplasia with mucous hypersecretion is drawn in the large airway (chronic bronchitis) panel.",
)

add(
    S5, 271, "scenario",
    "A patient with COPD has a post-bronchodilator FEV₁ of 45% predicted. Which GOLD grade and which ABE history would place him in group E?",
    "GOLD 3, with ≥2 exacerbations or 1 hospitalization a year",
    [
        "GOLD 2, with 0–1 moderate exacerbation a year",
        "GOLD 4, with ≥2 exacerbations or 1 hospitalization a year",
        "GOLD 3, with no exacerbations in the past year",
    ],
    "The grade table puts <50% in GOLD 3, and group E is defined by '≥ 2 exacerbations or 1 hospitalization/year' on the same page.",
)

add(
    S6, 272, "scenario",
    "A COPD patient has had three moderate exacerbations in a year and a blood eosinophil count of 350 cells/μL. Which initial regimen does the printed table give?",
    "Group E: LABA + LAMA + ICS, because eosinophils are ≥300",
    [
        "Group E: LABA + LAMA without ICS, because exacerbations alone do not allow ICS",
        "Group A: LABA/LAMA only",
        "Group B: LABA + LAMA with ICS only if eosinophils are <100",
    ],
    "The group E row reads 'LABA + LAMA ± ICS (If blood eosinophils ≥300)', and 350 cells/μL satisfies the printed indication for ICS.",
)

add(
    S7, 273, "scenario",
    "A COPD patient has a PaO₂ of 58 mm Hg with polycythemia. Does he qualify for long term oxygen therapy, and for how long each day?",
    "Yes — PaO₂ 55–60 mm Hg with polycythemia qualifies, for 15–16 hours a day",
    [
        "No — oxygen requires PaO₂ below 55 mm Hg irrespective of polycythemia",
        "Yes — PaO₂ 55–60 mm Hg with polycythemia qualifies, for 8–10 hours a day",
        "Yes — any PaO₂ below 60 mm Hg qualifies, for 20–24 hours a day",
    ],
    "The indications read 'PaO2 <55 mm Hg' and 'PaO2: 55–60 mm Hg associated with polycythemia or right heart failure', with concentrators used '15–16 hours/day'.",
)

add(
    S7, 273, "truefalse",
    "TRUE or FALSE about lung volume reduction surgery on page 273.",
    "True — it is contraindicated when FEV₁ is below 20%",
    [
        "True — it is contraindicated when FEV₁ is below 50%",
        "False — it is indicated when FEV₁ is below 20%",
        "False — no FEV₁ limit is printed for the operation",
    ],
    "The surgical line reads 'Lung volume reduction surgery (LVRS): contraindicated if FEV₁ <20%', a hard cut-off rather than a target.",
)

GUIDES = {
    S1: (
        "COPD (p267) is defined by GOLD 2023 as chronic persistent respiratory symptoms from airway/alveolar abnormalities giving progressive airflow limitation, with diagnosis by symptoms plus spirometry and a clinical/pathological split into chronic bronchitis and emphysema against large airway, small airway (<2 mm), alveoli and vasculature.\n"
        "Risk factors are tobacco, cooking-fuel smoke, occupational dust, vapours, fumes, other chemicals and low birth weight in preterms.\n"
        "Clinical features are persistent progressive dyspnea worse on exertion, intermittent chronic cough ± sputum, recurrent LRTI and wheeze.",
    ),
    S2: (
        "Chronic bronchitis (p268) is the clinical disease of cough with sputum ≥3 months/year for ≥2 years, aged 40–45, with copious sputum, hypoxia → cyanosis and RV failure → edema (blue bloater), type II failure, cor pulmonale, prominent vessels and a large heart, and normal TLC and DLCO.\n"
        "Emphysema is the pathological disease of dilatation distal to the terminal bronchiole with wall destruction, aged 50–75, with severe dyspnea, ↓PCO₂, cachexia, Hoover sign, hyper resonance, pursed lips (pink puffer), type I failure, hyperinflation with a small heart, and raised TLC/RV with reduced DLCO.\n"
        "The functional unit is the secondary pulmonary lobule and the respiratory unit is everything distal to the terminal bronchiole; centriacinar disease is the most common, in smokers, upper lobe.",
    ),
    S3: (
        "Panacinar emphysema (p269) affects the entire acinus below 45 years in non-smokers, in the basilar lower lobe, with vasculitis, liver disease and bronchiectasis from α-1 antitrypsin deficiency; paraseptal disease affects the young male smoker and gives spontaneous pneumothorax; irregular disease is printed with a blank characteristics cell.\n"
        "The protease-antiprotease flow has α-1 antitrypsin (SERPINA-1 gene) inhibiting neutrophil elastase, so deficiency raises elastase activity and destroys extracellular matrix; the alleles are m, Z and Null, with PiMM normal and PiZZ the commonest disease form.\n"
        "The pneumothorax note lists paraseptal change, Langerhans cell histiocytosis and 'lymphangioma hematosis'.",
    ),
    S4: (
        "Chronic bronchitis (p270) is large airway disease with neutrophils in sputum, squamous metaplasia, no basement membrane thickening, ↑macrophages and CD8 cells, goblet hyperplasia and mucous hypersecretion, with only a little smooth muscle increase and so no hyperresponsive symptoms.\n"
        "Against asthma the note table gives mild vs severe bronchospasm, increased mucus in both, epithelial necrosis absent vs present and squamous metaplasia present vs absent.\n"
        "Emphysema is small airway disease with exudate, a thickened inflammatory wall, peribronchial fibrosis, lymphoid follicles and disrupted alveolar attachments → ↓ERP → easily inflatable alveoli → ↑TLC and ↑RV; DP = IPP + ERP, and forceful exhalation raises IPP with falling ERP so DP < AP, collapsing airways and trapping air.",
    ),
    S5: (
        "DLCO is normal with parenchymal chronic bronchitis and reduced with the emphysematous alveolo-capillary unit (p271), and parenchymal damage drives chronic hypoxia (↓PaO₂, ↑PaCO₂) → pulmonary vasoconstriction → pulmonary hypertension → cor pulmonale → edema or death.\n"
        "Emphysema gives FEV₁ reduced with normal FVC and a reduced ratio; a ratio <0.7 sends the patient to reversibility testing, where FEV₁ rising 200 mL or 12% means asthma and no response means COPD, and post-bronchodilator FEV₁/FVC <0.7 confirms the diagnosis.\n"
        "GOLD 1 is ≥80%, GOLD 2 <80%, GOLD 3 <50% and GOLD 4 <30%; ≥2 exacerbations or 1 hospitalization a year defines group E; oral glucocorticoids raise side effects and lower benefits.",
    ),
    S6: (
        "Inhaled corticosteroids (p272) are indicated for blood eosinophils ≥300 cells/μL, ≥2 moderate exacerbations a year, concomitant asthma or asthma hospitalisation, and contraindicated by repeated pneumonia, eosinophils <100 cells/μL or a history of tuberculosis, with 2019 guidance to reduce steroid use; in asthma the pair is ICS + formoterol.\n"
        "Initial treatment gives group E LABA + LAMA ± ICS when eosinophils are ≥300, group A LABA/LAMA and group B LABA + LAMA, with LABA as formoterol or indacaterol and LAMA as tiotropium.\n"
        "Follow-up moves dyspnea from LABA/LAMA to LABA + LAMA, and exacerbations through eosinophils <300 to LAMA + LABA or >300 to LAMA + LABA + ICS, then roflumilast for chronic bronchitis with FEV₁ <50% or azithromycin for smoking/emphysema.",
    ),
    S7: (
        "Long term oxygen therapy (p273) runs 15–16 hours a day for PaO₂ <55 mm Hg, or 55–60 mm Hg with polycythemia or right heart failure, and LVRS is contraindicated below FEV₁ 20%.\n"
        "The BODE index is BMI, obstructive ventilatory defect, dyspnea and exercise capacity; an exacerbation is dyspnea and/or cough with sputum for <14 days with systemic inflammation, caused by pneumonia, pulmonary embolism or heart failure.\n"
        "Treatment is nebulization, IV hydrocortisone 100 mg, salbutamol plus ipratropium, MgSO₄, non-invasive then invasive ventilation, antibiotics for 5 days, oral steroids for 7 days and ICS for recurrent exacerbations, with no role for methylxanthines.",
    ),
}


def main() -> None:
    RAW.sort(key=lambda row: row[1])
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
        units.append({
            "id": f"MED-U{CHAPTER}-{n}",
            "ch": CHAPTER,
            "n": n,
            "title": sec,
            "sec": sec,
            "guide": (GUIDES[sec][0] if isinstance(GUIDES[sec], (list, tuple)) else GUIDES[sec]),
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
