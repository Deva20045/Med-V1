#!/usr/bin/env python3
"""Generate Chapter 47: Community Acquired Pneumonia (Book p274–285).

Every question is anchored to a printed line, table cell or figure caption of
uploads/03.pdf sheets 27–38 (Book pages 274–285), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 47
TITLE = "Community Acquired Pneumonia"
PAGES = "274-285"

S1 = "The Necrosis-Free Definition of Pneumonia, Its Five Parenchymal Sites, the Necrotising Note, the Six-Step Pathogenesis and the Three Protective Mechanisms"
S2 = "HAP, VAP and CAP by Source with Their 48-hour Rules, the Lobar and Interstitial Anatomy, the Typical and Atypical Split, and the Four-Part CAP Criteria with Auscultation"
S3 = "The Lobular and Interstitial Organism Columns, the MRSA-in-India Note and the Seven-Row Typical against Atypical Table"
S4 = "Community Acquired MRSA, the Outpatient to ICU Organism Shift, MRSA and MDR Risk within Three Months, and Pneumococcal Morphology, Culture and Haemolysis Chart"
S5 = "Pneumococcus against Viridans, the Four Toxins, the Quellung Reaction, Type 3 Invasiveness and the CAP Risk and Poor-Prognosis Notes"
S6 = "Type 2 Alveolar Binding, the Lobar Pneumonia Cardinal and Abdominal Symptoms, the Older-Patient Caveat, Resolution Timing and the Four-Column Chest Film Table"
S7 = "Sputum and Blood Culture Yields, BAL, and the Fourteen-Row Etiology Table from Bacteraemia to Atherosclerosis"
S8 = "Extrapulmonary Mycoplasma, and the Air Bronchogram, Silhouette, Golden S and Mediastinal Shift Captions"
S9 = "Mycoplasma against Legionella Films, the Fibrocalcific Scar, Necrotising Klebsiella and the Pneumatocele Cascade with Its 4 mm Rule"
S10 = "The CURB-65 Score with Its BUN and Blood Urea Equivalents, the BTS Outpatient Algorithm and the Non-Severe against Severe Inpatient Antibiotic Table"
S11 = "MRSA Cover and the 48–72-hour Response Rule, Empyema, Lung Abscess and ARDS, the Empyema against Abscess Table and the Definition of a Lung Cavity"
S12 = "The Bulla, Cyst and Thin-Walled Cavity Captions, the Four Thick-Walled Causes and the Seven-Letter CAVITY Mnemonic"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(47000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(47100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p274
add(
    S1, 274, "fillup",
    "Pneumonia is defined as acute infection of lung parenchyma without ______.",
    "necrosis",
    ["cavitation", "effusion", "fibrosis"],
    "The definition line reads 'Definition: Acute infection of lung parenchyma without necrosis', and the note below makes necrosis the dividing line to necrotising pneumonia and lung abscess.",
)

add(
    S1, 274, "recall",
    "Which five structures does the page list as the seat of pneumonia?",
    "Alveoli, alveolar interstitium, vascular interstitium, respiratory bronchioles and alveolar ducts",
    [
        "Alveoli, visceral pleura, vascular interstitium, respiratory bronchioles and alveolar ducts",
        "Alveoli, alveolar interstitium, conducting bronchi, respiratory bronchioles and alveolar ducts",
        "Alveoli, alveolar interstitium, vascular interstitium, terminal bronchioles and secondary lobules",
    ],
    "The arrow from the definition opens into 'Alveoli, alveolar interstitium, vascular interstitium, respiratory bronchioles, alveolar ducts', and the pleura and conducting bronchi are not included.",
)

add(
    S1, 274, "match",
    "Match the parenchymal event to its printed outcome — 1) Necrosis 2) Destruction of parenchyma … A) Lung abscess B) Necrotizing pneumonia",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The note branches 'Necrosis / destruction of parenchyma' into 'Necrotizing pneumonia' and 'Lung abscess' in that order.",
)

add(
    S1, 274, "recall",
    "In which order does the printed pathogenesis flowchart run?",
    "Defective cell-mediated immunity with viral infection → disruption of lung microbiota → alveolar epithelial barrier disruption → bacterial entry through microaspiration → alveoli",
    [
        "Disruption of lung microbiota → defective cell-mediated immunity → bacterial entry through microaspiration → alveolar epithelial barrier disruption → alveoli",
        "Defective cell-mediated immunity with viral infection → alveolar epithelial barrier disruption → disruption of lung microbiota → bacterial entry through microaspiration → alveoli",
        "Bacterial entry through microaspiration → defective cell-mediated immunity → disruption of lung microbiota → alveolar epithelial barrier disruption → alveoli",
    ],
    "The ladder reads defective cell mediated immunity with 'Infection by virus', disruption of lung microbiota, alveolar epithelial barrier disruption, entry of bacteria through microaspiration and then alveoli.",
)

add(
    S1, 274, "match",
    "Match each cytokine to its printed effect — 1) IL-1, IL-6 and TNFα 2) IL-8 … A) Recruitment of neutrophils B) Fever",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The cytokine bracket groups IL-1, IL-6 and TNFα under 'Fever', while IL-8 alone points to 'Recruitment of neutrophils'.",
)

add(
    S1, 274, "recall",
    "Which three protective mechanisms of the lung are printed on page 274?",
    "Pulmonary alveolar macrophage, gag reflex and mucociliary clearance",
    [
        "Pulmonary alveolar macrophage, cough reflex and surfactant",
        "Neutrophilic phagocytosis, gag reflex and mucociliary clearance",
        "Pulmonary alveolar macrophage, IgA secretion and mucociliary clearance",
    ],
    "The note lists 'Pulmonary alveolar macrophage', 'Gag reflex' and 'mucociliary clearance' as the protective mechanisms.",
)

add(
    S1, 274, "fillup",
    "The easiest and most common access to the lower respiratory tract is the ______ via aspiration.",
    "oropharynx",
    ["nasopharynx", "stomach", "trachea"],
    "The line reads 'Easiest / m/c access to lower respiratory tract: Oropharynx via aspiration', which explains why microaspiration dominates the pathogenesis.",
)

add(
    S1, 274, "recall",
    "Which sequence follows the cytokine release in the pathogenesis chart?",
    "Recruitment of neutrophils → capillary leak → alveolo-capillary exudate → impaired diffusion → hypoxia → dyspnea",
    [
        "Recruitment of neutrophils → capillary leak → alveolo-capillary exudate → improved diffusion → hyperoxia → dyspnea",
        "Recruitment of neutrophils → vasoconstriction → interstitial fibrosis → impaired diffusion → hypoxia → dyspnea",
        "Recruitment of macrophages → capillary leak → pleural effusion → impaired diffusion → hypoxia → dyspnea",
    ],
    "The right-hand column runs 'Recruitment of neutrophils → Capillary leak → Alveolo-capillary exudate → Impairs diffusion → Hypoxia → Dyspnea'.",
)

# ---------------------------------------------------------------- Unit 2: p275
add(
    S2, 275, "match",
    "Match each pneumonia to its printed source rule — 1) Hospital acquired pneumonia 2) Ventilator associated pneumonia 3) Community acquired pneumonia … A) No timing rule printed B) Occurs >48 hrs after admission (not present at admission) C) Occurs >48 hrs after endotracheal intubation",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "HAP is defined as occurring >48 hrs after admission and not present at admission, VAP as occurring >48 hrs after endotracheal intubation, while CAP carries no timing rule in this tree.",
)

add(
    S2, 275, "numeric",
    "Which single interval governs both hospital acquired and ventilator associated pneumonia on page 275?",
    "48 hours",
    ["24 hours", "72 hours", "7 days"],
    "Both brackets print 48 hrs — one after admission for HAP and one after endotracheal intubation for VAP.",
)

add(
    S2, 275, "match",
    "Match each classification axis to its printed branches — 1) Anatomical classification 2) Based on organism … A) Typical and atypical B) Lobar and interstitial",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The second tree splits anatomy into lobar and interstitial, while the third splits organisms into typical and atypical.",
)

add(
    S2, 275, "recall",
    "Which four-part sequence defines community acquired pneumonia on page 275?",
    "Acute infection <1 week with cardinal features plus radiological infiltrates on chest X-ray or CT, with no other explanation for the illness",
    [
        "Acute infection <2 weeks with cardinal features plus radiological infiltrates, with no other explanation for the illness",
        "Acute infection <1 week with cardinal features alone, radiology being optional",
        "Chronic infection >4 weeks with cardinal features plus radiological infiltrates",
    ],
    "The tree prints '1) Acute infection: <1 week with' the cardinal features, '3) Radiological finding: Infiltrates in chest x-ray/CT' and '+ 4) No other explanation for illness'.",
)

add(
    S2, 275, "recall",
    "Which five cardinal features are listed for CAP on page 275?",
    "Fever, dyspnea/tachypnea/tachycardia, cough (± sputum), pleuritic chest pain and hemoptysis",
    [
        "Fever, dyspnea/tachypnea/tachycardia, cough (± sputum), pleuritic chest pain and cyanosis",
        "Fever, bradycardia, cough (± sputum), pleuritic chest pain and hemoptysis",
        "Fever, dyspnea/tachypnea/tachycardia, cough with purulent sputum, dull chest pain and clubbing",
    ],
    "The cardinal list reads fever; dyspnea/tachypnea/tachycardia; cough (± sputum); pleuritic chest pain; hemoptysis — cyanosis and clubbing are not part of it.",
)

add(
    S2, 275, "numeric",
    "How long may the acute infection have lasted for the printed CAP criteria to apply?",
    "<1 week",
    ["<48 hours", "<2 weeks", "<4 weeks"],
    "Criterion 1 is 'Acute infection: <1 week with' the cardinal features, a tighter window than the <2-week and >4-week definitions used elsewhere in the book.",
)

add(
    S2, 275, "fillup",
    "The auscultation findings printed for CAP are bronchial breath sounds and crackles, which the page labels ______.",
    "subjective",
    ["diagnostic", "specific", "pathognomonic"],
    "The line reads 'Auscultation findings: Bronchial breath sounds, crackles; Subjective', which is why radiology rather than auscultation sits in the criteria.",
)

add(
    S2, 275, "truefalse",
    "TRUE or FALSE about the radiological criterion of CAP on page 275.",
    "True — infiltrates must be shown in a chest X-ray or CT",
    [
        "True — infiltrates must be shown in a chest X-ray only, CT being excluded",
        "False — radiology is not part of the CAP criteria",
        "False — the radiological criterion requires cavitation rather than infiltrates",
    ],
    "Criterion 3 reads 'Radiological finding: Infiltrates in chest x-ray/CT', accepting either modality before the final 'no other explanation' clause.",
)

# ---------------------------------------------------------------- Unit 3: p276
add(
    S3, 276, "recall",
    "Which organisms are printed under lobar pneumonia on page 276?",
    "Streptococcus pneumoniae (m/c), Staph. aureus (MRSA sp), Klebsiella pneumoniae, Hemophilus influenza and Moraxella catarrhalis",
    [
        "Streptococcus pneumoniae (m/c), Staph. aureus (MRSA sp), Klebsiella pneumoniae, Mycoplasma and Chlamydia",
        "Mycoplasma, Chlamydia, Legionella, Aspergillus and Pneumocystis jirovecii",
        "Streptococcus pneumoniae (m/c), Klebsiella pneumoniae, Hemophilus influenza, Moraxella catarrhalis and Nocardia",
    ],
    "The bacteria column reads 'Streptococcus pneumoniae (m/c)', 'Staph. aureus (MRSA sp)', 'Klebsiella pneumonia', 'Hemophilus influenza' and 'moraxella catarrhalis'; mycoplasma and chlamydia sit in the interstitial column.",
)

add(
    S3, 276, "recall",
    "Which organisms fill the interstitial (atypical) column on page 276?",
    "Virus (m/c), then mycoplasma, chlamydia and Legionella with features of both, then Aspergillus, Pneumocystis jirovecii in HIV and Nocardia in the immunocompromised",
    [
        "Virus (m/c), then pneumococcus, staphylococcus and klebsiella, then Aspergillus and Candida",
        "Mycoplasma (m/c), then chlamydia, Legionella and Moraxella, then Aspergillus and Nocardia",
        "Virus (m/c), then mycoplasma, chlamydia and Legionella, then Candida, Histoplasma and Coccidioides",
    ],
    "The right-hand column opens with 'virus (m/c)' under a merged cell, lists mycoplasma, chlamydia and Legionella with features of both, then fungi as Aspergillus, PCP in HIV and Nocardia in the immunocompromised.",
)

add(
    S3, 276, "fillup",
    "The note beneath the organism table states that MRSA is not common in ______.",
    "India",
    ["Europe", "Africa", "Japan"],
    "The line reads 'Note: MRSA is not common in India', qualifying the MRSA entry in the lobar column and the ICU list on the next page.",
)

add(
    S3, 276, "match",
    "Match each feature to typical or atypical pneumonia as printed — 1) Organism site 2) Onset 3) Pathology … A) Abrupt against insidious B) Extracellular against intracellular C) Alveolar capillary exudates against interstitial infiltrates",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "The table rows read extracellular vs intracellular, abrupt vs insidious, and alveolar capillary exudates vs interstitial infiltrates for typical against atypical disease.",
)

add(
    S3, 276, "match",
    "Match each atypical clinical feature to its printed description — 1) Course 2) Fever 3) Sputum … A) Low grade B) Mild upper respiratory infection → dry cough, dyspnea → ARDS C) Scanty",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "The atypical cell prints 'mild URI → Dry cough, dyspnea → ARDS', 'Low grade fever' and 'Scanty sputum', closing with extrapulmonary involvement.",
)

add(
    S3, 276, "match",
    "Match typical against atypical for laboratory detection as printed — 1) Culture/gram stain 2) Inflammatory parameters … A) CRP ↑, procalcitonin ↑ and leucocytosis B) Cannot be detected, with no inflammatory marker change",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The typical column says culture/gram stain 'Can be detected' with raised CRP, procalcitonin and leucocytosis; the atypical column says 'Cannot be detected' and prints only a dash for inflammatory parameters.",
)

add(
    S3, 276, "match",
    "Match each radiological pattern to its pneumonia type — 1) Large area of consolidation with lobar involvement 2) Bilateral patchy or diffuse interstitial involvement … A) Atypical pneumonia B) Typical pneumonia",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The last row reads 'Large area of consolidation (Lobar involvement)' for typical and 'Bilateral patchy / diffuse (Interstitial involvement)' for atypical pneumonia.",
)

# ---------------------------------------------------------------- Unit 4: p277
add(
    S4, 277, "recall",
    "Which two settings raise the possibility of community acquired MRSA on page 277?",
    "Concurrent influenza infection, and cavity with hemoptysis and pneumatocele",
    [
        "Concurrent tuberculosis, and cavity with hemoptysis and pneumatocele",
        "Concurrent influenza infection, and bilateral hilar lymphadenopathy",
        "Recent hospitalization, and a simple parapneumonic effusion",
    ],
    "The two bullets are 'concurrent influenza infection' and 'cavity + hemoptysis + pneumatocele', the classic triad of necrotising community MRSA.",
)

add(
    S4, 277, "match",
    "Match each care setting to its printed organisms — 1) Outpatient 2) Inpatient non-ICU 3) Inpatient ICU … A) Strep pneumoniae, MRSA and multidrug resistant gram-negative B) Strep pneumoniae, virus, mycoplasma, chlamydia and H. influenza C) Strep pneumoniae from ↓CMI, respiratory viruses and Legionella",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The care-set-up tree gives outpatients strep pneumoniae, virus, mycoplasma, chlamydia and H. influenza; non-ICU inpatients strep pneumoniae (d/t ↓CMI), respiratory viruses and Legionella; ICU patients strep pneumoniae, MRSA and MDR gram-negative with high mortality.",
)

add(
    S4, 277, "recall",
    "Which five risk factors are printed for MRSA and MDR gram-negative infection?",
    "Congestive heart failure, hemodialysis, antibiotic use and hospitalization within the last 3 months, and structural lung disease",
    [
        "Congestive heart failure, hemodialysis, antibiotic use and hospitalization within the last 12 months, and structural lung disease",
        "Diabetes, hemodialysis, antibiotic use within the last 3 months, and pleural effusion",
        "Congestive heart failure, neutropenia, recent surgery, and structural lung disease",
    ],
    "The list reads congestive heart failure, hemodialysis, antibiotic use, hospitalization and structural lung disease, with the brace 'within the last 3 months' covering the antibiotic and admission items.",
)

add(
    S4, 277, "fillup",
    "Antibiotic use and hospitalization count as MRSA/MDR risks only when they occurred within the last ______ months.",
    "3",
    ["1", "6", "12"],
    "The brace beside 'Antibiotic use' and 'Hospitalization' is labelled 'within the last 3 months', which is the time window the question tests.",
)

add(
    S4, 277, "recall",
    "How are pneumococci described morphologically on page 277?",
    "Gram-positive diplococci in chains, flame shaped or lanceolate",
    [
        "Gram-negative diplococci in chains, flame shaped or lanceolate",
        "Gram-positive cocci in clusters, spherical and non-capsulated",
        "Gram-positive diplococci in pairs only, without a capsule",
    ],
    "The morphology block reads 'gram-positive diplococci in chains', and the micrograph is captioned 'Flame shaped / Lanceolate diplococci'.",
)

add(
    S4, 277, "recall",
    "Which culture characteristics of pneumococci are printed beside the blood agar photograph?",
    "Alpha hemolytic, partial hemolysis in 5% blood agar, with green colour and a draughtsman or carrom coin appearance",
    [
        "Beta hemolytic, complete hemolysis in 5% blood agar, with a clear zone and a swarming appearance",
        "Gamma hemolytic, no hemolysis on blood agar, with a grey colony and a mucoid appearance",
        "Alpha hemolytic, partial hemolysis in 5% blood agar, with a golden pigment and a comet-tail appearance",
    ],
    "The culture block reads 'Alpha hemolytic (Partial hemolysis in 5% blood agar)', with arrows to 'green colour on blood agar' and the 'Draughtsman/carrom coin appearance' photograph.",
)

add(
    S4, 277, "match",
    "Match each hemolysis pattern to its printed organisms — 1) Complete 2) Partial 3) No hemolysis … A) Enterococci B) Streptococcus C) Strep. pneumoniae and Strep. viridans",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The note tree reads Complete → Streptococcus, Partial → Strep. pneumoniae and Strep. viridans, and No → Enterococci.",
)

# ---------------------------------------------------------------- Unit 5: p278
add(
    S5, 278, "match",
    "Match the two streptococci to their printed results across the whole biochemical table — 1) Strep pneumoniae 2) Strep viridans … A) Negative for bile soluble, optochin susceptible and inulin fermentation B) Positive for bile soluble, optochin susceptible and inulin fermentation",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The two-column table gives a plus to Strep pneumoniae and a minus to Strep viridans in all three rows — bile soluble, optochin susceptible and inulin fermentation.",
)

add(
    S5, 278, "recall",
    "Which four toxins or antigens are listed for the pneumococcus on page 278?",
    "Capsular polysaccharide, pneumolysin, IgA1 and pneumococcal somatic C antigen",
    [
        "Capsular polysaccharide, pneumolysin, streptolysin O and pneumococcal somatic C antigen",
        "Capsular polysaccharide, pneumolysin, IgA protease and M protein",
        "Capsular polysaccharide, exotoxin A, IgA1 and pneumococcal somatic C antigen",
    ],
    "The toxin list reads capsular polysaccharide, pneumolysin ('Cytolytic toxin → Pores in cell membrane'), IgA1 and pneumococcal somatic C antigen, which precipitates C reactive protein.",
)

add(
    S5, 278, "fillup",
    "The Quellung reaction shown beside the toxin list demonstrates ______ of the capsule.",
    "swelling",
    ["rupture", "staining", "dissolution"],
    "The arrow on the diagram points to 'swelling of capsule' with the caption 'Quellung reaction' beneath it.",
)

add(
    S5, 278, "truefalse",
    "TRUE or FALSE about the invasiveness of S. pneumoniae as printed on page 278.",
    "True — S. pneumoniae is non invasive except for type 3",
    [
        "True — every serotype of S. pneumoniae is invasive",
        "False — S. pneumoniae is invasive except for type 3",
        "False — S. pneumoniae is never invasive",
    ],
    "The note under the Quellung diagram reads 'S pneumoniae is non invasive (Except type 3)', making type 3 the exception.",
)

add(
    S5, 278, "recall",
    "Which six conditions define deficient cell-mediated immunity as a CAP risk on page 278?",
    "Diabetes, chronic kidney disease, hemodialysis, COPD with bronchiectasis, cardiac failure and age >65 years",
    [
        "Diabetes, chronic kidney disease, hemodialysis, COPD with bronchiectasis, cardiac failure and age >50 years",
        "Diabetes, nephrotic syndrome, hemodialysis, COPD with bronchiectasis, cardiac failure and age >65 years",
        "Diabetes, chronic kidney disease, peritoneal dialysis, asthma, cardiac failure and age >65 years",
    ],
    "The list reads diabetes, chronic kidney disease, hemodialysis, 'chronic obstructive pulmonary disease, bronchiectasis', cardiac failure and 'Age >65 yrs'.",
)

add(
    S5, 278, "recall",
    "Which four items are listed under the immunocompromised heading?",
    "Steroid or monoclonal antibody consumption, transplant and neutropenia",
    [
        "Steroid consumption, splenectomy, transplant and neutrophilia",
        "Monoclonal antibody consumption, transplant, neutropenia and chemotherapy",
        "Steroid consumption, transplant, neutropenia and HIV",
    ],
    "The immunocompromised block reads 'Steroid, monoclonal antibody consumption', 'Transplant' and 'Neutropenia' — four drug/state entries across three bullets.",
)

add(
    S5, 278, "recall",
    "Which two findings are printed as markers of a poor prognosis in CAP?",
    "Hypothermia and leukopenia, the latter usually with atypical organisms",
    [
        "Hyperthermia and leukocytosis, the latter usually with typical organisms",
        "Hypothermia and leukocytosis, the latter usually with typical organisms",
        "Hypotension and thrombocytosis, the latter usually with atypical organisms",
    ],
    "The note reads 'Poor prognosis of CAP: Hypothermia. Leukopenia (usually atypical organisms)', both being paradoxical findings in an infection.",
)

# ---------------------------------------------------------------- Unit 6: p279
add(
    S6, 279, "fillup",
    "The clinical pattern section opens by stating that bacteria bind to type ______ alveolar epithelial cells.",
    "2",
    ["1", "3", "4"],
    "The first line under Clinical Pattern reads 'Bacteria bind to type 2 alveolar epithelial cells', the same type II cell that makes surfactant in the earlier pulmonary chapter.",
)

add(
    S6, 279, "recall",
    "Which five symptoms are bracketed as cardinal symptoms of lobar pneumonia?",
    "High spiking fever, pleuritic chest pain, cough, hemoptysis and dyspnea",
    [
        "High spiking fever, pleuritic chest pain, cough, hemoptysis and abdominal pain",
        "Low grade fever, pleuritic chest pain, cough, hemoptysis and dyspnea",
        "High spiking fever, dull chest pain, cough with scanty sputum, hemoptysis and dyspnea",
    ],
    "The brace 'Cardinal symptoms' encloses exactly high spiking fever, pleuritic chest pain, cough, hemoptysis and dyspnea; abdominal symptoms and confusion sit outside it.",
)

add(
    S6, 279, "oddoneout",
    "Pick the ODD ONE OUT — three are printed under lobar pneumonia on page 279, one details belongs elsewhere:",
    "Recurrent hiccups with diffuse abdominal pain as the only presentation in older patients",
    ["Confusion", "Abdominal symptoms with diffuse abdominal pain", "Recurrent hiccups"],
    "Abdominal symptoms include diffuse abdominal pain and recurrent hiccups, and confusion is a separate bullet; in older patients confusion may be the only symptom, not the abdominal pair.",
)

add(
    S6, 279, "recall",
    "What is printed about lobar pneumonia in older patients?",
    "Confusion might be the only symptom, and classical signs may not be present",
    [
        "Fever is always the only symptom, and classical signs are exaggerated",
        "Abdominal pain is the only symptom, and classical signs are always present",
        "Cough is the only symptom, and classical signs may not be present",
    ],
    "The two lines read 'In older patients: Confusion might be the only symptom' and 'Classical signs may not be present', which is why the criteria lean on radiology.",
)

add(
    S6, 279, "numeric",
    "How long after antibiotics do fever and leukocytosis resolve in the printed progression line?",
    "4–5 days",
    ["24–48 hours", "7–10 days", "2 weeks"],
    "The line reads 'Progression: Fever & leukocytosis resolve 4-5 days after antibiotics', a useful clock for judging treatment failure.",
)

add(
    S6, 279, "match",
    "Match each pneumonia to its printed blood picture — 1) Lobar pneumonia 2) Interstitial bronchopneumonia … A) Normal CBC, CRP and procalcitonin B) Leucocytosis with raised CRP and procalcitonin",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The table gives lobar disease leucocytosis, raised CRP and raised procalcitonin, while the interstitial column reads normal for all three.",
)

add(
    S6, 279, "recall",
    "Which four signs are printed for the lobar pneumonia chest film?",
    "Homogeneous consolidation, silhouette sign, air bronchogram and sharply marginated fissure",
    [
        "Heterogeneous patchy infiltrates, silhouette sign, air bronchogram and sharply marginated fissure",
        "Homogeneous consolidation, silhouette sign, air bronchogram and bilateral diffuse fine reticular opacity",
        "Homogeneous consolidation, cavity formation, air bronchogram and sharply marginated fissure",
    ],
    "The lobar column lists '1. Homogeneous consolidation, 2. Silhouette sign, 3. Air bronchogram, 4. Sharply marginated fissure', with Strep pneumoniae as the usual cause.",
)

add(
    S6, 279, "recall",
    "Which signs and usual cause are printed for bronchopneumonia?",
    "Poorly defined heterogeneous patchy infiltrates scattered through the lung with an air bronchogram, usually staphylococcal aureus giving multilobar disease with cavitation, pneumatoceles and abscess",
    [
        "Homogeneous consolidation with a silhouette sign, usually Strep pneumoniae giving a single lobe",
        "Bilateral diffuse fine reticular opacity, usually Pneumocystis jirovecii",
        "Airspace opacification in a lobar distribution, usually after a stroke or seizure",
    ],
    "The bronchopneumonia column prints 'Poorly defined heterogenous patchy infiltrates scattered throughout the lung', an air bronchogram, and 'Staphylococcal aureus → multilobar + Cavitation + pneumatoceles + abscess'.",
)

add(
    S6, 279, "match",
    "Match each film pattern to its printed usual cause — 1) Interstitial pneumonia with bilateral diffuse fine reticular opacity 2) Aspiration with airspace opacification in a lobar or segmental distribution … A) Stroke or seizure B) Pneumocystis jirovecii pneumonia",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The interstitial column names Pneumocystis (jiroveci) pneumonia and the aspiration column names stroke or seizure, with gravity-dependent predilection.",
)

# ---------------------------------------------------------------- Unit 7: p280
add(
    S7, 280, "recall",
    "Which specimen work-up is described at the top of page 280?",
    "Sputum microscopy and sputum culture done in atypical pneumonia, blood culture with poor yield, and BAL",
    [
        "Sputum microscopy and culture done in typical pneumonia, blood culture with high yield, and BAL",
        "Sputum microscopy only, blood culture with poor yield, and pleural biopsy",
        "Sputum culture done in atypical pneumonia, blood culture with poor yield, and lung biopsy",
    ],
    "The bracket joins sputum microscopy and sputum culture as 'Done in atypical pneumonia', with blood culture noted for 'poor yield' and BAL listed last.",
)

add(
    S7, 280, "match",
    "Match each history to its printed organism — 1) Bacteremia or diabetes 2) Alcoholism with upper lobe involvement 3) COPD, smoking or bronchiectasis 4) Cystic fibrosis … A) Pseudomonas B) Klebsiella C) Streptococcus pneumoniae D) Burkholderia cepacia",
    "1-C, 2-B, 3-A, 4-D",
    ["1-C, 2-A, 3-B, 4-D", "1-B, 2-C, 3-A, 4-D", "1-C, 2-B, 3-D, 4-A"],
    "The table pairs bacteremia/diabetes with S. pneumoniae, the alcoholism cluster with Klebsiella, COPD/smoking/bronchiectasis with Pseudomonas and cystic fibrosis with Burkholderia cepacia.",
)

add(
    S7, 280, "match",
    "Match each lesion to its printed organism — 1) Lung abscess 2) Cavity 3) Pneumatocele … A) Klebsiella B) MRSA and anaerobes C) MRSA",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The rows read lung abscess → MRSA and anaerobes, cavity → MRSA (printed in colour) and pneumatocele → Klebsiella.",
)

add(
    S7, 280, "match",
    "Match each exposure to its printed organism — 1) Sheep, cats and goats 2) Rabbits 3) Bats … A) Histoplasma B) Coxiella burnetii C) Francisella tularensis",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The exposure rows read sheep/cats/goats → Coxiella burnetii, rabbits → Francisella tularensis and bats → Histoplasma.",
)

add(
    S7, 280, "fillup",
    "Travel to the Ohio and St. Lawrence river valley points to ______.",
    "Histoplasma capsulatum",
    ["Coccidioides immitis", "Blastomyces dermatitidis", "Cryptococcus neoformans"],
    "The row reads 'Travel to Ohio & St. Lawrence river valley → Histoplasma capsulatum', distinct from the bat exposure row that names Histoplasma alone.",
)

add(
    S7, 280, "fillup",
    "The final row of the etiology table links atherosclerosis to ______.",
    "Chlamydia pneumoniae",
    ["Mycoplasma pneumoniae", "Legionella pneumophila", "Coxiella burnetii"],
    "The last row pairs 'Atherosclerosis' with 'Chlamydia pneumoniae', the chronic-infection hypothesis printed in colour.",
)

add(
    S7, 280, "match",
    "Match each setting to its printed organism — 1) Alzheimer-type dementia or decreased level of consciousness 2) Travel on a cruise ship … A) Legionella B) Anaerobes",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "Dementia and a decreased level of consciousness point to anaerobes from aspiration, while cruise-ship travel points to Legionella.",
)

# ---------------------------------------------------------------- Unit 8: p281
add(
    S8, 281, "recall",
    "Which three extrapulmonary manifestations of mycoplasma are printed on page 281?",
    "Cold antibody autoimmune hemolysis, Steven Johnson's syndrome and Guillain Barre syndrome",
    [
        "Cold antibody autoimmune hemolysis, erythema nodosum and Guillain Barre syndrome",
        "Warm antibody autoimmune hemolysis, Steven Johnson's syndrome and myasthenia gravis",
        "Cold antibody autoimmune hemolysis, Steven Johnson's syndrome and transverse myelitis",
    ],
    "The list reads 'Cold antibody autoimmune hemolysis', 'Steven Johnson's syndrome' and 'Guillain Barre syndrome' beneath the heading extrapulmonary manifestations of mycoplasma.",
)

add(
    S8, 281, "recall",
    "How is the air bronchogram described in the radiological findings block?",
    "Air filled spaces within consolidation, which is not specific to consolidation and also appears in cardiogenic pulmonary edema",
    [
        "Air filled spaces within consolidation, which is specific to lobar pneumonia and never appears in edema",
        "Air filled spaces within a cavity, which is specific to tuberculosis",
        "Air filled spaces tracking along the pleura, which is specific to empyema",
    ],
    "The two bullets read 'Air filled spaces within consolidation' and 'Not specific to consolidation', with a captioned example 'Air bronchogram in a cardiogenic pulmonary edema'.",
)

add(
    S8, 281, "recall",
    "What does consolidation of the left lower lobe do to the silhouettes?",
    "It loses the left heart silhouette while the diaphragm silhouette stays intact",
    [
        "It loses the diaphragm silhouette while the left heart silhouette stays intact",
        "It loses both the left heart and the diaphragm silhouettes",
        "It loses the ascending aorta silhouette with the diaphragm intact",
    ],
    "The two bullets under the left lower lobe film read 'Loss of left heart silhouette' and 'Diaphragm silhouette is intact', a classic silhouette-sign exercise.",
)

add(
    S8, 281, "recall",
    "Which silhouette is lost with consolidation of the right upper lobe, and which signs are bracketed to Klebsiella?",
    "Loss of the ascending aorta silhouette, with golden S or reverse S sign and bulging fissure sign belonging to Klebsiella infection",
    [
        "Loss of the right heart silhouette, with golden S and bulging fissure sign belonging to pneumococcal infection",
        "Loss of the ascending aorta silhouette, with golden S and bulging fissure sign belonging to staphylococcal infection",
        "Loss of the descending aorta silhouette, with golden S and bulging fissure sign belonging to Pseudomonas infection",
    ],
    "The upper lobe film is captioned with 'Loss of ascending aorta silhouette', and the brace ties golden S/reverse S and bulging fissure to 'Klebsiella infection'.",
)

add(
    S8, 281, "match",
    "Match each chest film finding to its printed meaning — 1) Golden S sign or reverse S sign 2) Bulging fissure sign … A) Klebsiella infection alongside the golden S B) Collapse with mediastinum shifted to the same side",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The collapse panel lists '1. Shifting of mediastinum to same side' and '2. Golden S sign / Reverse S sign', while the bulging fissure sign is bracketed with Klebsiella infection.",
)

add(
    S8, 281, "scenario",
    "A chest film shows right upper lobe consolidation, a bulging fissure and a reverse S curve, and the trachea is shifted to the right. Which combination does the page support?",
    "Collapse of the right upper lobe, with Klebsiella as the suggested organism",
    [
        "Consolidation without collapse, with pneumococcus as the suggested organism",
        "Collapse of the left upper lobe, with Klebsiella as the suggested organism",
        "Pleural effusion, with Klebsiella as the suggested organism",
    ],
    "The collapse panel pairs mediastinal shift to the same side with golden S/reverse S, and the adjacent brace attributes golden S and bulging fissure to Klebsiella; the last caption is 'Collapse of right upper lobe'.",
)

# ---------------------------------------------------------------- Unit 9: p282
add(
    S9, 282, "match",
    "Match each photograph caption on page 282 to its printed message — 1) Mycoplasma/Chlamydia 2) Legionella 3) Bronchopneumonia 4) Fibrocalcific scar post TB … A) Bilateral dense consolidation B) Minimal interstitial infiltrates misdiagnosed as a normal study C) Air space opacification/consolidation D) Fibrosis",
    "1-B, 2-A, 3-C, 4-D",
    ["1-A, 2-B, 3-C, 4-D", "1-B, 2-A, 3-D, 4-C", "1-C, 2-A, 3-B, 4-D"],
    "The four captions read 'mycoplasma/Chlamydia minimal interstitial infiltrates misdiagnosed as normal study', 'Legionella bilateral dense consolidation', 'Bronchopneumonia air space opacification: consolidation' and 'Fibrocalcific scar post TB' with an arrow to fibrosis.",
)

add(
    S9, 282, "recall",
    "Which two features are printed under the necrotising Klebsiella film?",
    "Upper lobe involvement and bulging fissure sign",
    [
        "Lower lobe involvement and air bronchogram",
        "Upper lobe involvement and golden S sign only",
        "Bilateral diffuse infiltrates and pneumatocele",
    ],
    "The caption bullets read 'upper lobe involvement' and 'bulging fissure sign' beneath the circled necrotising area.",
)

add(
    S9, 282, "recall",
    "Which sequence describes the pathogenesis of pneumonia with multiple pneumatocele on page 282?",
    "Dense white opacity → focal suppurative lung abscess → necrosis and destruction of parenchyma → bursts into bronchus → air entry into abscess → gas within consolidation surrounded by a wall → air-fluid levels → cavity",
    [
        "Dense white opacity → focal suppurative lung abscess → fibrosis and scarring → air entry into abscess → gas within consolidation → air-fluid levels → cavity",
        "Dense white opacity → cavity → air-fluid level → abscess → necrosis → air entry → resolution",
        "Dense white opacity → air entry into abscess → necrosis of parenchyma → bursts into bronchus → gas within consolidation → cavity",
    ],
    "The flow begins with 'Dense white opacity: mass, consolidation, nodule' and runs through suppurative abscess, necrosis and destruction, rupture into the bronchus, air entry, gas within consolidation, air-fluid levels and finally cavity.",
)

add(
    S9, 282, "fillup",
    "Gas within consolidation counts as a pneumatocele when surrounded by a wall of minimum ______ mm.",
    "4",
    ["2", "6", "10"],
    "The flow cell reads 'Gas within consolidation surrounded by a wall (min. 4mm)', and the adjacent note uses the same 4 mm to separate a bulla.",
)

add(
    S9, 282, "recall",
    "In which four settings is the pneumatocele, cyst or bulla caption said to occur?",
    "IV drug abusers and post viral infection, with progression to cavity, an association with MRSA and a size under 4 mm",
    [
        "IV drug abusers and post viral infection, with progression to cavity, an association with Klebsiella and a size over 4 mm",
        "Alcoholics and post viral infection, with progression to pneumothorax, an association with MRSA and a size under 4 mm",
        "IV drug abusers and post tubercular scarring, with progression to cavity, an association with MRSA and a size under 4 mm",
    ],
    "The list reads 'IV drug abusers', 'Post viral infection', 'Progresses to cavity', 'Associated with MRSA' and 'Size <4mm'.",
)

add(
    S9, 282, "fillup",
    "The note at the foot of page 282 reserves the term bulla for a cavity larger than ______ mm.",
    "4",
    ["2", "6", "10"],
    "The boxed note reads 'Bulla: Cavity >4 mm', pairing with the 4 mm minimum wall thickness in the pneumatocele cascade above it.",
)

add(
    S9, 282, "oddoneout",
    "Pick the ODD ONE OUT — three are printed for the pneumatocele/ cyst/ bulla caption on page 282, one reverses the print:",
    "Associated with Klebsiella rather than MRSA",
    ["Seen in IV drug abusers", "Progresses to cavity", "Size <4 mm"],
    "The caption asserts an association with MRSA, seen in IV drug abusers and post viral infection, progressing to cavity with size <4 mm; Klebsiella is the pneumatocele organism in the page 280 table, not this caption.",
)

# ---------------------------------------------------------------- Unit 10: p283
add(
    S10, 283, "match",
    "Match each CURB-65 letter to its printed criterion — 1) C 2) U 3) R 4) B … A) Respiratory rate >30/min B) Confusion C) Blood pressure <90 mmHg systolic or <60 mmHg diastolic D) Urea >7 mmol/L",
    "1-B, 2-D, 3-A, 4-C",
    ["1-B, 2-A, 3-D, 4-C", "1-D, 2-B, 3-A, 4-C", "1-B, 2-D, 3-C, 4-A"],
    "The stem lists C confusion, U urea >7 mmol/L, R respiratory rate >30/min, B blood pressure <90 systolic or <60 diastolic and 65 age ≥65.",
)

add(
    S10, 283, "numeric",
    "Which urea value in mmol/L defines the U of CURB-65, and what are its printed BUN and blood urea equivalents?",
    ">7 mmol/L, with BUN ≈21 mg/dL and blood urea ≈42 mg/dL",
    [
        ">7 mmol/L, with BUN ≈42 mg/dL and blood urea ≈21 mg/dL",
        ">10 mmol/L, with BUN ≈21 mg/dL and blood urea ≈42 mg/dL",
        ">7 mmol/L, with BUN ≈7 mg/dL and blood urea ≈14 mg/dL",
    ],
    "The bracket reads 'U: urea >7 mmol/L (BUN ≈ 21 mg/dL, Blood urea ≈ 42 mg/dL)', the two conversions serving readers who work in mg/dL.",
)

add(
    S10, 283, "match",
    "Match each CURB-65 score to its printed management — 1) 0 2) 1 to 2 3) ≥3 … A) ICU management B) Outpatient management C) Inpatient management",
    "1-B, 2-C, 3-A",
    ["1-B, 2-A, 3-C", "1-C, 2-B, 3-A", "1-A, 2-C, 3-B"],
    "The interpretation table gives score 0 outpatient management, 1 and 2 inpatient management and ≥3 ICU management.",
)

add(
    S10, 283, "recall",
    "In the BTS outpatient algorithm, which combination is printed when antibiotic resistance risk is absent?",
    "Amoxicillin 1 g TDS plus azithromycin 500 mg on day 1 then 250 mg on days 2–5, or clarithromycin 500 mg BD, or amoxicillin plus doxycycline",
    [
        "Amoxyclav 625 mg TDS plus azithromycin or doxycycline",
        "Amoxicillin 500 mg TDS plus azithromycin 500 mg for five days",
        "Levofloxacin 750 mg once daily alone",
    ],
    "The 'Absent' arm prints amoxicillin 1g TDS with azithromycin 500 mg D1 and 250 mg D2–D5 or clarithromycin 500 mg BD, or amoxicillin plus doxycycline; amoxyclav 625 mg TDS belongs to the 'Present' arm.",
)

add(
    S10, 283, "recall",
    "Which regimen is printed when the risk of antibiotic resistance is present in outpatients?",
    "Amoxyclav 625 mg TDS plus azithromycin or doxycycline",
    [
        "Amoxicillin 1 g TDS plus azithromycin 500 mg",
        "Piperacillin–tazobactam 4.5 g QID IV plus a macrolide",
        "Amoxicillin 1 g TDS plus doxycycline only",
    ],
    "The 'Present' arm prints 'Amoxyclav 625mg TDS + Azithromycin/Doxycycline', with the note that cephalosporins are an alternative to amoxyclav.",
)

add(
    S10, 283, "fillup",
    "The note beneath the outpatient algorithm states that ______ are an alternative to amoxyclav.",
    "cephalosporins",
    ["macrolides", "fluoroquinolones", "aminoglycosides"],
    "The line reads 'Note: Cephalosporins are an alternative to amoxyclav', placed under the resistance-present arm.",
)

add(
    S10, 283, "recall",
    "Which first-line inpatient regimen is printed for non-severe CAP?",
    "A β-lactam (ampicillin + sulbactam 1.5 g QID IV or piperacillin + tazobactam 4.5 g QID IV) plus a macrolide (azithromycin or clarithromycin 500 mg BD)",
    [
        "A β-lactam (ampicillin + sulbactam 1.5 g QID IV or piperacillin + tazobactam 4.5 g QID IV) plus levofloxacin 750 mg/day",
        "Levofloxacin 750 mg/day as monotherapy",
        "Azithromycin 500 mg BD alone",
    ],
    "The non-severe first line is β-lactam with a macrolide, the β-lactam bracket giving ampicillin + sulbactam 1.5 g QID IV or piperacillin + tazobactam 4.5g QID IV, and the macrolide 500 mg BD.",
)

add(
    S10, 283, "recall",
    "What is printed for second-line and severe CAP in the inpatient table?",
    "Second line is a respiratory fluoroquinolone (levofloxacin 750 mg/day), and severe ICU disease takes a β-lactam plus levofloxacin, with fluoroquinolone monotherapy not recommended",
    [
        "Second line is a macrolide alone, and severe ICU disease takes levofloxacin monotherapy",
        "Second line is levofloxacin 500 mg/day, and severe ICU disease takes a β-lactam alone",
        "Second line is amoxyclav, and severe ICU disease takes a β-lactam plus azithromycin",
    ],
    "The second-line row reads 'Respiratory fluoroquinolone: Levofloxacin 750mg/day', and the severe column reads 'β-lactam + Levofloxacin (monotherapy with fluoroquinolone not recommended)'.",
)

# ---------------------------------------------------------------- Unit 11: p284
add(
    S11, 284, "recall",
    "Which three historical items trigger consideration of MRSA cover on page 284?",
    "History of isolation, recent hospitalization and prior MRSA",
    [
        "History of isolation, recent hospitalization and prior influenza",
        "History of intubation, recent hospitalization and prior MRSA",
        "History of isolation, diabetes and prior MRSA",
    ],
    "The line reads 'H/o isolation, recent hospitalization, prior MRSA → MRSA cover considered', before the response-to-therapy rule.",
)

add(
    S11, 284, "numeric",
    "At what interval is response to therapy judged, and what follows if there is no response?",
    "At 48–72 hours, and no response means a complication with CT as the next step",
    [
        "At 24 hours, and no response means a complication with a repeat chest X-ray",
        "At 48–72 hours, and no response means changing the antibiotic without imaging",
        "At 7 days, and no response means a complication with CT as the next step",
    ],
    "The line reads 'Response to Therapy: 48 – 72hrs → No response: Complication → CT', a strict three-step rule.",
)

add(
    S11, 284, "recall",
    "Which findings diagnose empyema, and what is its treatment?",
    "Macroscopic pus with a complicated parapneumonic effusion; CT split pleura sign with thickened parietal and visceral pleura, raised protein and LDH with low glucose, treated by intercostal drainage",
    [
        "Macroscopic pus with a simple parapneumonic effusion; CT split pleura sign with raised glucose, treated by antibiotics alone",
        "Microscopic pus with a complicated parapneumonic effusion; ultrasound septation with low protein, treated by thoracocentesis",
        "Macroscopic pus with a complicated parapneumonic effusion; CT split pleura sign with raised protein and LDH, treated by decortication",
    ],
    "Empyema is macroscopic pus plus a complicated parapneumonic effusion (m/c); diagnosis uses the CT split pleura sign with thickened pleura and ↑protein, ↑LDH, ↓glucose, and treatment is intercostal drainage.",
)

add(
    S11, 284, "recall",
    "Which antibiotic triple and duration are printed for a lung abscess?",
    "Vancomycin plus meropenem plus clindamycin for 6–8 weeks",
    [
        "Vancomycin plus piperacillin–tazobactam plus clindamycin for 6–8 weeks",
        "Vancomycin plus meropenem plus clindamycin for 2 weeks",
        "Meropenem plus clindamycin for 6–8 weeks",
    ],
    "The abscess line reads 'Rx: vancomycin + meropenem + Clindamycin × 6-8 wks', under the heading 'Destruction & cavity'.",
)

add(
    S11, 284, "oddoneout",
    "Pick the ODD ONE OUT — three are printed complications of CAP on page 284, one is not:",
    "Pleural plaque",
    ["Empyema", "Lung abscess", "ARDS with MDR organisms"],
    "The complication list is empyema, lung abscess, ARDS with MDR and metastatic infection (rare); pleural plaque is not on it.",
)

add(
    S11, 284, "match",
    "Match empyema against abscess on the four printed rows — 1) Wall 2) Angle 3) X-ray 4) CT split pleura sign … A) Lentiform against rounded B) Smooth against irregular C) Positive against negative D) Obtuse against acute",
    "1-B, 2-D, 3-A, 4-C",
    ["1-B, 2-A, 3-D, 4-C", "1-D, 2-B, 3-A, 4-C", "1-B, 2-D, 3-C, 4-A"],
    "The table gives empyema against abscess as wall smooth vs irregular, angle obtuse vs acute, X-ray lentiform vs rounded, and split pleura sign positive vs negative.",
)

add(
    S11, 284, "fillup",
    "The note beside the empyema/abscess table states that a simple and synpneumonic effusion is ______.",
    "sterile",
    ["purulent", "loculated", "fibrinous"],
    "The note reads 'Simple & synpneumonic effusion: Sterile', which is why empyema requires macroscopic pus rather than an effusion alone.",
)

add(
    S11, 284, "recall",
    "How is a lung cavity defined on page 284, and which two organisms are printed?",
    "A gas filled space within consolidation, mass or nodule, due to expulsion of necrotic debris via the bronchial tree, seen in staphylococcus and klebsiella",
    [
        "A gas filled space within normal lung, due to expulsion of necrotic debris via the bronchial tree, seen in staphylococcus and klebsiella",
        "A gas filled space within consolidation, due to bronchial obstruction, seen in pneumococcus and klebsiella",
        "A fluid filled space within consolidation, due to expulsion of necrotic debris, seen in staphylococcus and pseudomonas",
    ],
    "The definition is 'Gas filled space within consolidation, mass, nodule' with 'D/t expulsion of necrotic debris via bronchial tree', and the cavity arrow to necrotising pneumonia names staphylococcus and klebsiella.",
)

# ---------------------------------------------------------------- Unit 12: p285
add(
    S12, 285, "match",
    "Match each three-figure caption strip on page 285 to what it shows — 1) First strip 2) Second strip … A) Thick walled cavities B) Bulla, cyst and thin walled cavity",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The upper strip shows three generous air spaces captioned Bulla, Cyst and Thin walled cavity; the lower strip shows 'Thick walled cavities'.",
)

add(
    S12, 285, "recall",
    "Which four causes of thick walled cavities are printed on page 285?",
    "Abscess, necrotising SCC, Wegener's granulomatosis and blastomycosis",
    [
        "Abscess, carcinoid tumour, Wegener's granulomatosis and histoplasmosis",
        "Abscess, necrotising SCC, sarcoidosis and blastomycosis",
        "Bulla, necrotising SCC, Wegener's granulomatosis and aspergilloma",
    ],
    "The thick walled cavity list reads 'Abscess', 'Necrotising SCC', 'wegener's granulomatosis' and 'Blastomycosis'.",
)

add(
    S12, 285, "match",
    "Match each letter of the CAVITY mnemonic to its printed causes — 1) C 2) A 3) V 4) I 5) T 6) Y … A) Aspergillosis, autoimmune (Wegener's granulomatosis) and abscess B) Cancer, SCC being most common C) Vascular emboli D) Young patients with congenital abnormality E) TB F) Infection with Staphylococcus aureus and Klebsiella",
    "1-B, 2-A, 3-C, 4-F, 5-E, 6-D",
    ["1-B, 2-A, 3-F, 4-C, 5-E, 6-D", "1-B, 2-C, 3-A, 4-F, 5-E, 6-D", "1-A, 2-B, 3-C, 4-F, 5-D, 6-E"],
    "The mnemonic runs C cancer with SCC as m/c, A aspergillosis/autoimmune/abscess, V vascular emboli, I infection with staph and klebsiella, T TB, Y young patients with congenital abnormality.",
)

add(
    S12, 285, "fillup",
    "In the CAVITY mnemonic the letter C stands for cancer, with ______ printed as the most common histological type.",
    "SCC",
    ["adenocarcinoma", "small cell carcinoma", "carcinoid"],
    "The first line of the mnemonic reads 'C – cancer (SCC: m/c)', placing squamous cell carcinoma first among cavitating cancers.",
)

add(
    S12, 285, "recall",
    "Which three fungi are printed as causes of lung cavities at the end of the mnemonic?",
    "Cryptococcus, Aspergillus and Coccidioidomycosis",
    [
        "Cryptococcus, Candida and Coccidioidomycosis",
        "Histoplasma, Aspergillus and Coccidioidomycosis",
        "Cryptococcus, Aspergillus and Blastomyces",
    ],
    "The seventh line reads 'Fungus: Cryptococcus, Aspergillus, Coccidioidomycosis', following the six mnemonic letters.",
)

add(
    S12, 285, "scenario",
    "A 62-year-old smoker has a 3 cm thick-walled upper lobe cavity with an irregular inner margin. Using the page 285 lists, which diagnosis heads the differential and which benign mimic is named in the thick-walled group?",
    "Necrotising squamous cell carcinoma, with Wegener's granulomatosis among the thick-walled mimics",
    [
        "Necrotising squamous cell carcinoma, with a simple cyst among the thick-walled mimics",
        "Pneumococcal pneumonia, with Wegener's granulomatosis among the thick-walled mimics",
        "Tuberculosis, with a bulla among the thick-walled mimics",
    ],
    "Thick walled cavities are abscess, necrotising SCC, Wegener's granulomatosis and blastomycosis, and the CAVITY mnemonic puts SCC as the commonest cancer; a bulla and a cyst are thin-walled structures in the strip above.",
)

# ---------------------------------------------------------------- extra interactives
add(
    S1, 274, "truefalse",
    "TRUE or FALSE about the definition of pneumonia on page 274.",
    "True — pneumonia is an acute infection of lung parenchyma without necrosis",
    [
        "True — pneumonia is an acute infection of lung parenchyma with necrosis",
        "False — pneumonia is a chronic infection of the pleura without necrosis",
        "False — necrosis is required before the term pneumonia can be used",
    ],
    "The definition is 'Acute infection of lung parenchyma without necrosis', and the note makes necrosis the step to necrotising pneumonia or lung abscess.",
)

add(
    S2, 275, "scenario",
    "A 34-year-old has three days of fever, cough with sputum and pleuritic pain, with a right lower zone infiltrate on chest X-ray and no other explanation. How many of the printed CAP criteria does he satisfy?",
    "All four — acute infection under a week, cardinal features, radiological infiltrate and no alternative explanation",
    [
        "Only three — the radiological criterion needs CT rather than a chest X-ray",
        "Only two — fever and cough are enough for the diagnosis",
        "All four, but only if the sputum culture is positive",
    ],
    "The four criteria read acute infection <1 week with cardinal features, radiological infiltrate on chest X-ray/CT and no other explanation, and a three-day history fits the first.",
)

add(
    S3, 276, "oddoneout",
    "Pick the ODD ONE OUT — three are printed in the lobar pneumonia organism column, one belongs to the interstitial column:",
    "Mycoplasma",
    ["Streptococcus pneumoniae", "Klebsiella pneumonia", "Moraxella catarrhalis"],
    "The lobar column prints S. pneumoniae (m/c), Staph aureus including MRSA, Klebsiella, H. influenzae and Moraxella; mycoplasma sits in the interstitial (atypical) column.",
)

add(
    S4, 277, "scenario",
    "A patient with severe CAP is admitted to the ICU. Which organisms does the printed care-set-up tree expect, and what does it say about mortality?",
    "Strep pneumoniae, MRSA and multidrug resistant gram-negative organisms, with high mortality",
    [
        "Strep pneumoniae, respiratory viruses and Legionella, with low mortality",
        "Virus, mycoplasma and chlamydia, with high mortality",
        "Strep pneumoniae, MRSA and Legionella, with high mortality",
    ],
    "The ICU arm reads 'Inpatient (ICU): (High mortality) Strep. pneumoniae, MRSA, multidrug resistant gram-negative (MDR)', distinct from the non-ICU arm.",
)

add(
    S5, 278, "scenario",
    "A diabetic patient with pneumococcal bacteremia is treated on the ward. Which organism does the printed etiology pairing predict, and what does the immunity list say about diabetes?",
    "Streptococcus pneumoniae, and diabetes sits under deficient cell-mediated immunity",
    [
        "Klebsiella, and diabetes sits under deficient cell-mediated immunity",
        "Streptococcus pneumoniae, and diabetes sits under immunocompromised states only",
        "Pseudomonas, and diabetes sits under the structural lung disease list",
    ],
    "The p280 pairing links bacteremia/diabetes to S. pneumoniae, and the p278 risk list places diabetes first under deficient cell-mediated immunity.",
)

add(
    S6, 279, "scenario",
    "An 82-year-old presents with confusion alone and no classical signs of pneumonia. What does page 279 advise?",
    "Confusion may be the only symptom in older patients and classical signs may be absent, so radiology is needed",
    [
        "Confusion excludes pneumonia and points to a metabolic cause",
        "Classical signs are always present in older patients, so confusion can be ignored",
        "Confusion in the elderly always means a lung abscess rather than pneumonia",
    ],
    "The two lines read 'In older patients: Confusion might be the only symptom' and 'Classical signs may not be present', which is why the CAP criteria include radiology.",
)

add(
    S7, 280, "scenario",
    "A patient with fever and a cavitating pneumonia reports exposure to bats. Which organism does the printed table suggest?",
    "Histoplasma",
    [
        "Coxiella burnetii",
        "Francisella tularensis",
        "Chlamydia pneumoniae",
    ],
    "The exposure rows read sheep, cats and goats → Coxiella burnetii, rabbits → Francisella tularensis and bats → Histoplasma.",
)

add(
    S9, 282, "scenario",
    "An IV drug user develops a pneumatocele that progresses to a cavity. Which organism does the printed caption associate with this, and what size cut-off is given?",
    "MRSA, with a size under 4 mm",
    [
        "Klebsiella, with a size under 4 mm",
        "MRSA, with a size over 4 mm",
        "Pseudomonas, with a size under 4 mm",
    ],
    "The caption reads 'Associated with MRSA' and 'Size <4mm', while the note reserves 'Bulla' for a cavity larger than 4 mm.",
)

add(
    S10, 283, "scenario",
    "A patient with CAP is confused, has a urea of 9 mmol/L, a respiratory rate of 32/min, a blood pressure of 100/70 mmHg and is 70 years old. What CURB-65 score and disposal does the page give?",
    "A score of 3 from confusion, urea and respiratory rate, requiring ICU management",
    [
        "A score of 3, requiring inpatient ward management",
        "A score of 4, requiring ICU management",
        "A score of 2, requiring outpatient management",
    ],
    "Confusion, urea >7 mmol/L and respiratory rate >30/min give three points; blood pressure 100/70 and age 70 add none, and a score ≥3 means ICU management.",
)

add(
    S11, 284, "scenario",
    "A patient with CAP has had no response after 72 hours of appropriate antibiotics. What does the printed rule say to do?",
    "Suspect a complication and obtain a CT scan",
    [
        "Repeat the same antibiotics for another 72 hours",
        "Change to a macrolide and repeat the chest X-ray in a week",
        "Proceed directly to surgery",
    ],
    "The line reads 'Response to Therapy: 48 – 72hrs → No response: Complication → CT', so a CT follows the failed response.",
)

add(
    S12, 285, "oddoneout",
    "Pick the ODD ONE OUT — three are printed as causes of thick walled cavities, one belongs to the thin walled group above:",
    "Bulla",
    ["Abscess", "Necrotising SCC", "Wegener's granulomatosis"],
    "The thick walled list is abscess, necrotising SCC, Wegener's granulomatosis and blastomycosis, while a bulla is captioned in the thin walled strip above it.",
)

GUIDES = {
    S1: (
        "Pneumonia (p274) is acute infection of lung parenchyma without necrosis, seated in alveoli, alveolar and vascular interstitium, respiratory bronchioles and alveolar ducts; necrosis or destruction of parenchyma turns it into necrotising pneumonia or lung abscess.\n"
        "Pathogenesis runs defective cell-mediated immunity with viral infection → disrupted lung microbiota → alveolar epithelial barrier disruption → bacterial microaspiration → alveoli → IL-1/IL-6/TNFα for fever and IL-8 for neutrophil recruitment → capillary leak → alveolo-capillary exudate → impaired diffusion → hypoxia → dyspnea.\n"
        "Protective mechanisms are the alveolar macrophage, gag reflex and mucociliary clearance, and the commonest access is the oropharynx via aspiration.",
    ),
    S2: (
        "HAP occurs >48 hrs after admission and is not present at admission, VAP >48 hrs after endotracheal intubation, and CAP has no timing rule; anatomy splits into lobar and interstitial and organisms into typical and atypical (p275).\n"
        "CAP requires an acute infection <1 week with cardinal features — fever, dyspnea/tachypnea/tachycardia, cough ± sputum, pleuritic chest pain and hemoptysis — plus infiltrates on CXR or CT and no other explanation.\n"
        "Auscultation gives bronchial breath sounds and crackles, which the page labels subjective.",
    ),
    S3: (
        "Lobar pneumonia (p276) is restricted to one lobe with Strep pneumoniae most common, Staph aureus including MRSA, Klebsiella, H. influenzae and Moraxella; the interstitial column opens with virus as most common, then mycoplasma, chlamydia and Legionella with features of both, then Aspergillus, PCP in HIV and Nocardia in the immunocompromised.\n"
        "The note states MRSA is not common in India.\n"
        "Typical against atypical runs extracellular vs intracellular, abrupt vs insidious, alveolar capillary exudates vs interstitial infiltrates, neutrophilic vs lymphocytic, detectable vs undetectable on culture, raised CRP/procalcitonin/leucocytosis vs none, and large lobar consolidation vs bilateral patchy interstitial change.",
    ),
    S4: (
        "Community acquired MRSA (p277) is suggested by concurrent influenza or by cavity with hemoptysis and pneumatocele.\n"
        "Outpatients carry strep pneumoniae, virus, mycoplasma, chlamydia and H. influenzae; non-ICU inpatients strep pneumoniae from low CMI, respiratory viruses and Legionella; ICU patients strep pneumoniae, MRSA and MDR gram-negative with high mortality — MRSA and MDR risk being CCF, hemodialysis, antibiotics and hospitalization within the last 3 months, and structural lung disease.\n"
        "Pneumococci are gram-positive diplococci in chains, flame-shaped or lanceolate, alpha hemolytic with partial hemolysis on 5% blood agar, green colour and a draughtsman/carrom coin colony; complete hemolysis means streptococcus, partial means pneumoniae or viridans, and none means enterococci.",
    ),
    S5: (
        "Strep pneumoniae is bile soluble, optochin susceptible and inulin fermenting while viridans is negative in all three (p278).\n"
        "The toxins are capsular polysaccharide, pneumolysin (cytolytic, punching pores in the membrane), IgA1 and pneumococcal somatic C antigen, which precipitates C reactive protein; the Quellung reaction shows swelling of the capsule, and S. pneumoniae is non-invasive except type 3.\n"
        "CAP risk comes from deficient CMI — diabetes, chronic kidney disease, hemodialysis, COPD, bronchiectasis, cardiac failure and age >65 — or from immunocompromise by steroids/monoclonals, transplant and neutropenia, and poor prognosis is marked by hypothermia and leukopenia with atypical organisms.",
    ),
    S6: (
        "Bacteria bind type 2 alveolar epithelial cells (p279); lobar pneumonia has cardinal high spiking fever, pleuritic chest pain, cough, hemoptysis and dyspnea, with abdominal pain and hiccups or confusion added, and in the elderly confusion may be the only symptom while classical signs are absent.\n"
        "Fever and leukocytosis resolve 4–5 days after antibiotics; blood shows leucocytosis, raised CRP and procalcitonin in lobar disease against normal values in interstitial bronchopneumonia.\n"
        "Films separate into lobar (homogeneous consolidation, silhouette sign, air bronchogram, sharply marginated fissure, usually pneumococcus), bronchopneumonia (poorly defined heterogeneous patchy infiltrates with air bronchogram, staph giving multilobar disease with cavitation, pneumatoceles and abscess), interstitial (bilateral diffuse fine reticular opacity, PCP) and aspiration (airspace opacification, gravity dependent, after stroke or seizure).",
    ),
    S7: (
        "Sputum microscopy and culture are done in atypical pneumonia, blood culture has poor yield and BAL is listed last (p280).\n"
        "The etiology table pairs bacteremia/diabetes with S. pneumoniae; alcoholism, upper lobe involvement, bulging fissure, cavitation and golden S with Klebsiella; COPD/smoking/bronchiectasis with Pseudomonas; cystic fibrosis with Burkholderia cepacia; lung abscess with MRSA and anaerobes; cavity with MRSA; pneumatocele with Klebsiella; dementia or low consciousness with anaerobes.\n"
        "Exposures pair sheep, cats and goats with Coxiella, rabbits with Francisella, bats with Histoplasma, cruise ships with Legionella, the Ohio and St. Lawrence valleys with Histoplasma capsulatum and atherosclerosis with Chlamydia pneumoniae.",
    ),
    S8: (
        "Mycoplasma adds cold antibody autoimmune hemolysis, Steven Johnson's syndrome and Guillain Barre syndrome (p281).\n"
        "An air bronchogram is air-filled space within consolidation, not specific and also seen in cardiogenic pulmonary edema; left lower lobe consolidation loses the left heart silhouette with an intact diaphragm, while right upper lobe disease loses the ascending aorta silhouette.\n"
        "Golden S/reverse S and the bulging fissure sign are bracketed to Klebsiella, and collapse shifts the mediastinum to the same side.",
    ),
    S9: (
        "Captions on p282 read mycoplasma/chlamydia minimal interstitial infiltrates misdiagnosed as a normal study, Legionella bilateral dense consolidation, bronchopneumonia air space opacification, and a fibrocalcific scar post TB with fibrosis; necrotising Klebsiella shows upper lobe involvement and a bulging fissure.\n"
        "The pneumatocele cascade runs dense white opacity → focal suppurative abscess → necrosis and destruction → rupture into bronchus → air entry → gas within consolidation inside a wall of minimum 4 mm → air-fluid levels → cavity.\n"
        "Pneumatoceles occur in IV drug abusers and after viral infection, progress to cavity, associate with MRSA and measure <4 mm, while a bulla is a cavity >4 mm.",
    ),
    S10: (
        "CURB-65 (p283) is confusion, urea >7 mmol/L (BUN ≈21 mg/dL, blood urea ≈42 mg/dL), respiratory rate >30/min, blood pressure <90 systolic or <60 diastolic and age ≥65, scoring 0 for outpatient, 1–2 for inpatient and ≥3 for ICU care.\n"
        "The BTS outpatient arm without resistance risk gives amoxicillin 1 g TDS plus azithromycin 500 mg day 1 then 250 mg days 2–5 or clarithromycin 500 mg BD, or amoxicillin plus doxycycline; with resistance risk it gives amoxyclav 625 mg TDS plus azithromycin or doxycycline, cephalosporins being an alternative.\n"
        "Inpatients take a β-lactam (ampicillin + sulbactam 1.5 g QID IV or piperacillin–tazobactam 4.5 g QID IV) plus a macrolide 500 mg BD, second line levofloxacin 750 mg/day, and severe ICU disease a β-lactam plus levofloxacin without fluoroquinolone monotherapy.",
    ),
    S11: (
        "MRSA cover follows isolation, recent hospitalization or prior MRSA, and response is judged at 48–72 hours, with no response meaning a complication and CT (p284).\n"
        "Empyema is macroscopic pus with a complicated parapneumonic effusion, diagnosed by the CT split pleura sign with thickened pleura and ↑protein, ↑LDH, ↓glucose and treated by intercostal drainage; lung abscess is destruction with cavity and takes vancomycin + meropenem + clindamycin for 6–8 weeks; ARDS with MDR and metastatic infection complete the list.\n"
        "Empyema against abscess is smooth vs irregular wall, obtuse vs acute angle, lentiform vs rounded on X-ray and positive vs negative split pleura sign, a simple synpneumonic effusion being sterile; a cavity is a gas-filled space within consolidation, mass or nodule from expectorated necrotic debris, seen in staphylococcus and klebsiella.",
    ),
    S12: (
        "The caption strip on p285 shows a bulla, a cyst and a thin walled cavity, then thick walled cavities.\n"
        "Thick walled cavities are abscess, necrotising SCC, Wegener's granulomatosis and blastomycosis.\n"
        "The CAVITY mnemonic gives C cancer with SCC most common, A aspergillosis/autoimmune (Wegener's)/abscess, V vascular emboli, I infection with Staphylococcus aureus and Klebsiella, T TB, Y young patients with congenital abnormality, and fungus as Cryptococcus, Aspergillus and Coccidioidomycosis.",
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
