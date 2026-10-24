#!/usr/bin/env python3
"""Generate Chapter 48: Atypical Pneumonia and Pneumonia in Immunocompromised
(Book p286–295).

Every question is anchored to a printed line, table cell or figure caption of
uploads/03.pdf sheets 39–48 (Book pages 286–295), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 48
TITLE = "Atypical Pneumonia and Pneumonia in Immunocompromised"
PAGES = "286-295"

S1 = "Mycoplasma as the Smallest Free-Living Organism, Its Wall-Free Sterol Membrane, the Ten Percent Pneumonia Picture, Seven Extrapulmonary Manifestations, Radiology, PPLO Culture and Azithromycin"
S2 = "Chlamydia as an Obligate Intracellular Peptidoglycan-Free Bacterium with Its Elementary Body, Walking Pneumonia, HEp-2 Isolation and Micro-Immunofluorescence, plus the Legionella Phenotype"
S3 = "Legionella Microaspiration, BCYE Medium, the Sterile Gram Stain, Its Four Risk Factors, Typical against Atypical Disease, Pontiac against Legionnaires and DFAT Diagnosis"
S4 = "Necrotising Pneumonia and Aspiration as the Two Causes of Lung Abscess, the Five-Step Pathogenesis, the Posterior Right Upper Lobe Site and the Clinical Picture"
S5 = "The Chest Film and CT Captions, Metastatic Infection to AA Amyloidosis, the Tuberculosis and Malignancy Differentials and the Vancomycin-Piperacillin-Tazobactam-Clindamycin Regimen"
S6 = "The Three Severely Immunocompromised States, the Seven Organisms, and the Renal and Bone Marrow Transplant Infection Timelines with Onset-Based Infection"
S7 = "Invasive Aspergillosis from Conidia to Hyphae, Neutropenia as the Chief Risk, the Halo and Air Crescent Signs, the Reverse Halo and Monad Notes and the Fever-Hemoptysis-Pleuritic Triad"
S8 = "Aspergillus Diagnosis by BAL, VATS and Galactomannan, Beta-D-Glucan Cross-Reactivity, Voriconazole against Liposomal Amphotericin, the Mucormycosis Contrast and the Opening of Pneumocystis"
S9 = "Pneumocystis Diagnosis by GMS Cyst Stain, Fluorescein Antibody and PCR, Its Four HIV Records, the Cotrimoxazole Ladder, Steroids for Hypoxia and Three Prophylactic Drugs"
S10 = "Nocardia asteroides as an Aerobic Acid-Fast Filamentous Organism, Its Mandatory Host Defect, Brain and Lung Disease, the Crooked Beaded Filaments and the Sulfonamide Regimen"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(48000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(48100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p286
add(
    S1, 286, "fillup",
    "Mycoplasma is described as the smallest free living organism capable of ______.",
    "replication",
    ["motility", "sporulation", "photosynthesis"],
    "The opening line reads 'Smallest free living organism capable of replication', the superlative that anchors the whole mycoplasma section.",
)

add(
    S1, 286, "recall",
    "Which three structural facts explain why β-lactams fail in mycoplasma?",
    "There is no cell wall, β-lactams are therefore not effective, and sterols are present while flagella are absent",
    [
        "There is a thick cell wall, β-lactams are therefore effective, and sterols are absent",
        "There is no cell wall, β-lactams are therefore not effective, and sterols are absent with flagella present",
        "There is no cell wall, β-lactams are effective through porins, and sterols are present with flagella absent",
    ],
    "The block reads 'No cell wall: β-lactams not effective, Sterols present' and 'No flagella', so the missing wall both excludes β-lactams and requires sterols in the membrane.",
)

add(
    S1, 286, "recall",
    "Which two diseases are listed under mycoplasma, and how is it transmitted?",
    "Tracheobronchitis or pharyngitis and pneumonia in 10%, transmitted by droplet infection",
    [
        "Tracheobronchitis or pharyngitis and pneumonia in 50%, transmitted by the faecal–oral route",
        "Lobar pneumonia and empyema, transmitted by droplet infection",
        "Pharyngitis and bronchiolitis in 10%, transmitted by direct contact",
    ],
    "The disease list gives tracheobronchitis/pharyngitis and 'Pneumonia (10%)', followed by 'Transmission: Droplet infection'.",
)

add(
    S1, 286, "recall",
    "Which four features describe the pneumonia of mycoplasma on page 286?",
    "Low grade fever, cough, scanty sputum and a paucity of clinical signs",
    [
        "High grade fever, cough, copious purulent sputum and florid clinical signs",
        "Low grade fever, dry cough, hemoptysis and consolidation with bronchial breathing",
        "High spiking fever, pleuritic pain, scanty sputum and a paucity of clinical signs",
    ],
    "The four bullets under pneumonia read 'Low grade fever', 'Cough', 'Scanty sputum' and 'Paucity of clinical signs' — the dissociation between symptoms and signs is the point.",
)

add(
    S1, 286, "match",
    "Match each mycoplasma extrapulmonary manifestation to its printed wording — 1) Hematological 2) Dermatological 3) Neurological … A) Steven Johnson syndrome (SJS)/erythema multiforme B) Guillain Barre syndrome (GBS) C) Cold antibody autoimmune hemolytic anemia (IgM)",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "The list prints cold antibody autoimmune hemolytic anemia (IgM), SJS/erythema multiforme and GBS, before encephalitis, bullous myringitis, myocarditis/pericarditis and arthralgia with adenopathy.",
)

add(
    S1, 286, "recall",
    "Which four radiological patterns are printed for mycoplasma on page 286?",
    "Reticulonodular or patchy consolidation starting at the hilum, interstitial involvement, ground glass appearance and tree in bud appearance in endobronchial inflammation or obstruction",
    [
        "Reticulonodular or patchy consolidation starting at the base, interstitial involvement, ground glass appearance and honeycomb change",
        "Lobar consolidation with air bronchogram, interstitial involvement, ground glass appearance and tree in bud appearance",
        "Reticulonodular consolidation starting at the hilum, cavitation, ground glass appearance and tree in bud appearance",
    ],
    "The imaging bullets read reticulonodular/patchy consolidation starting at the hilum, interstitial involvement, ground glass appearance and tree in bud appearance in endobronchial inflammation/obstruction.",
)

add(
    S1, 286, "match",
    "Match each mycoplasma culture detail to its printed description — 1) Medium 2) Method 3) Appearance … A) Biphasic with fried egg appearance B) PPLO agar C) Diene's method",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The culture block reads 'PPLO agar: Diene's method' and 'Biphasic with fried egg appearance', the fried egg colony being the classic description.",
)

add(
    S1, 286, "recall",
    "Which diagnostic test is bracketed as rapid and most sensitive, and which drug is the printed drug of choice?",
    "PCR of respiratory secretion and serology are rapid and most sensitive, and azithromycin is the drug of choice",
    [
        "Culture and serology are rapid and most sensitive, and doxycycline is the drug of choice",
        "PCR of respiratory secretion and culture are rapid and most sensitive, and a respiratory quinolone is the drug of choice",
        "PCR of respiratory secretion and serology are rapid and most sensitive, and erythromycin is the drug of choice",
    ],
    "The bracket joins 'PCR of respiratory secretion' and 'Serology' under 'Rapid & most sensitive', and the treatment list starts 'Azithromycin (DOC)' followed by doxycycline and respiratory quinolones.",
)

add(
    S1, 286, "fillup",
    "Mycoplasma injures epithelium through hydrogen peroxide and ______ produced by the organism.",
    "superoxide",
    ["peroxynitrite", "hydroxyl radical", "nitric oxide"],
    "The pathogen line reads 'Hydrogen peroxide & superoxide produced by organism → Epithelial cell injury', with prognosis printed as good.",
)

# ---------------------------------------------------------------- Unit 2: p287
add(
    S2, 287, "recall",
    "Which four features define chlamydia as printed on page 287?",
    "Obligate intracellular bacterium, absence of peptidoglycan, human to human transmission and an elementary body that is extracellular, metabolically inactive and infective",
    [
        "Facultative intracellular bacterium, presence of peptidoglycan, human to human transmission and an elementary body that is metabolically active",
        "Obligate intracellular bacterium, absence of peptidoglycan, zoonotic transmission and a reticulate body that is the infective form",
        "Obligate intracellular bacterium, thick peptidoglycan, human to human transmission and an elementary body that is metabolically inactive",
    ],
    "The bullets read 'Obligate intracellular bacteria', 'Absence of peptidoglycan', 'Human to human transmission' and 'elementary body: Extracellular, metabolically inactive, infective form'.",
)

add(
    S2, 287, "fillup",
    "The chlamydial elementary body is extracellular, metabolically inactive and ______.",
    "infective",
    ["non-infective", "replicating", "adherent"],
    "The elementary body bullet reads 'Extracellular, metabolically inactive, infective form', the dormant but transmissible stage.",
)

add(
    S2, 287, "recall",
    "Which clinical features of chlamydia are printed on page 287?",
    "A prolonged asymptomatic condition of the upper respiratory tract, atypical pneumonia in 10% and walking pneumonia indistinguishable from mycoplasma, with low grade fever, minimal sputum and dry cough",
    [
        "A short symptomatic condition of the lower respiratory tract, atypical pneumonia in 50% and lobar pneumonia distinguishable from mycoplasma",
        "A prolonged asymptomatic condition of the upper respiratory tract, atypical pneumonia in 10% and lobar pneumonia with copious sputum",
        "A prolonged symptomatic condition of the upper respiratory tract, atypical pneumonia in 10% and walking pneumonia indistinguishable from legionella",
    ],
    "The block reads 'Prolonged asymptomatic condition of upper respiratory tract', 'Atypical pneumonia (10%)', 'Walking pneumonia (cannot differentiate from mycoplasma)' and the nonspecific trio of low grade fever, minimal sputum and dry cough.",
)

add(
    S2, 287, "recall",
    "Which investigation is the gold standard for chlamydia, and which finding is expressly denied?",
    "Micro immunofluorescence serology is the gold standard, and there is no lobar consolidation",
    [
        "Isolation by HEp-2 cells is the gold standard, and there is lobar consolidation",
        "Micro immunofluorescence serology is the gold standard, and there is lobar consolidation",
        "Culture on PPLO agar is the gold standard, and there is no lobar consolidation",
    ],
    "The investigation list reads isolation by HEp-2 cells, 'Serology: micro immuno fluorescence (Gold standard)' and 'No lobar consolidation'.",
)

add(
    S2, 287, "recall",
    "Which drug is chlamydia expressly resistant to, and which two drugs are printed for it?",
    "It is resistant to sulfonamide, and azithromycin and doxycycline are used",
    [
        "It is resistant to azithromycin, and sulfonamide and doxycycline are used",
        "It is resistant to doxycycline, and azithromycin and sulfonamide are used",
        "It is resistant to penicillin, and azithromycin and doxycycline are used",
    ],
    "The treatment block reads 'Resistant to sulfonamide' and 'Azithromycin, doxycycline', in deliberate contrast with mycoplasma's azithromycin, doxycycline and quinolones.",
)

add(
    S2, 287, "match",
    "Match each Legionella feature to its printed description — 1) Gram status 2) Oxygen requirement 3) Motility 4) Staining … A) Strict aerobes B) Gram negative, predominantly intracellular C) Partially acid fast D) Motile",
    "1-B, 2-A, 3-D, 4-C",
    ["1-B, 2-D, 3-A, 4-C", "1-A, 2-B, 3-D, 4-C", "1-B, 2-A, 3-C, 4-D"],
    "The Legionella bullets read gram negative and predominantly intracellular, strict aerobes, motile and partially acid fast, before the aquatic reservoir and biofilm lines.",
)

add(
    S2, 287, "fillup",
    "The most pathogenic Legionella serovar is type ______.",
    "1",
    ["2", "4", "6"],
    "The virulence bullet reads 'Type 1 serovar: most pathogenic', with 'Type 4 secretion system' given as the pathogenic factor.",
)

# ---------------------------------------------------------------- Unit 3: p288
add(
    S3, 288, "recall",
    "Which route of Legionella transmission is printed first, and which comes second?",
    "Microaspiration first, then aerosolization",
    [
        "Aerosolization first, then microaspiration",
        "Direct inoculation first, then microaspiration",
        "Faecal–oral first, then aerosolization",
    ],
    "The line reads 'Mode of transmission: microaspiration > Aerosolization', the greater-than sign ranking the two routes.",
)

add(
    S3, 288, "recall",
    "Which medium is specific for Legionella, and what does the abbreviation stand for?",
    "BCYE medium, buffered charcoal yeast extract medium",
    [
        "BCYE medium, blood charcoal yeast extract medium",
        "PPLO agar, pleuropneumonia-like organism agar",
        "BCYE medium, buffered cysteine yeast extract medium",
    ],
    "The culture line reads 'BCYE medium: Buffered charcoal yeast extract medium: Specific medium', the letters BCYE being the tested part.",
)

add(
    S3, 288, "recall",
    "What does Gram staining of respiratory secretions show in Legionella infection?",
    "Pus cells and neutrophils are present but no organisms are seen",
    [
        "Pus cells and neutrophils are present with abundant gram-negative bacilli",
        "No pus cells are seen but the organisms stain readily",
        "Gram-positive diplococci in chains with a background of pus cells",
    ],
    "The Gram staining findings read 'Pus cells, neutrophils +' and 'No organisms seen', the notorious sterile-looking Gram stain of legionellosis.",
)

add(
    S3, 288, "recall",
    "Which four risk factors are printed for Legionella?",
    "Poor CMI, cigarette smoking, immunosuppression and hairy cell leukemia",
    [
        "Poor CMI, cigarette smoking, immunosuppression and chronic kidney disease",
        "Diabetes, cigarette smoking, immunosuppression and hairy cell leukemia",
        "Poor CMI, alcohol use, immunosuppression and hairy cell leukemia",
    ],
    "The risk list reads 'Poor CMI', 'Cigarette smoking', 'Immunosuppression' and 'Hairy cell leukemia'.",
)

add(
    S3, 288, "match",
    "Match the typical and atypical Legionella pictures as printed — 1) Typical 2) Atypical … A) Non-productive cough, diarrhea, hyponatremia, elevated LFT, thrombocytopenia and hematuria B) Rapidly progressive, high grade fever, bilateral dense consolidation and leucocytosis",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The typical arm is rapidly progressive with high grade fever, bilateral dense consolidation and leucocytosis; the atypical arm carries non-productive cough, GI symptoms, hyponatremia, elevated LFT, thrombocytopenia and hematuria.",
)

add(
    S3, 288, "match",
    "Match each Legionella syndrome to its severity — 1) Mild 2) Severe … A) Legionnaires disease B) Pontiac fever",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The severity branch reads mild → Pontiac fever and severe → Legionnaires disease, in that order.",
)

add(
    S3, 288, "recall",
    "Which three diagnostic statements are printed for Legionella on page 288?",
    "DFAT and urinary antigen testing both have high specificity, while sputum and aspiration testing are not done",
    [
        "DFAT has low specificity, urinary antigen has high specificity, and sputum testing is the test of choice",
        "DFAT and urinary antigen testing both have high specificity, and sputum testing is the test of choice",
        "DFAT and urinary antigen testing both have low specificity, while sputum and aspiration testing are not done",
    ],
    "The diagnosis block reads 'DFAT: Direct fluorescence antibody test, High specificity', 'urinary antigen testing: High specificity' and 'Sputum/aspiration testing: Not done'.",
)

add(
    S3, 288, "fillup",
    "The treatment printed for Legionella is azithromycin, the drug of choice, combined with ______.",
    "rifampicin",
    ["clindamycin", "ceftriaxone", "cotrimoxazole"],
    "The treatment line reads 'Azithromycin (DOC) + Rifampicin', with quinolones as the alternative below it.",
)

# ---------------------------------------------------------------- Unit 4: p289
add(
    S4, 289, "match",
    "Match each cause of lung abscess to its printed organisms — 1) Necrotising pneumonia 2) Aspiration pneumonia … A) Anaerobes B) Staphylococcus and Klebsiella",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "Necrotising pneumonia is a complication of pneumonia caused by staphylococcus and klebsiella, while aspiration pneumonia is anaerobic and presents with chronic symptoms.",
)

add(
    S4, 289, "recall",
    "Which two organisms are printed as causes of necrotising pneumonia?",
    "Staphylococcus and Klebsiella",
    [
        "Pneumococcus and Klebsiella",
        "Staphylococcus and Pseudomonas",
        "Klebsiella and Burkholderia",
    ],
    "The necrotising pneumonia branch lists 'Staphylococcus' and 'Klebsiella' under organisms involved.",
)

add(
    S4, 289, "recall",
    "Which aspiration sites are printed, and in which order of frequency?",
    "Posterior segment of the upper lobe, more often than the superior segment of the lower lobe",
    [
        "Superior segment of the lower lobe, more often than the posterior segment of the upper lobe",
        "Posterior segment of the lower lobe, more often than the superior segment of the upper lobe",
        "Anterior segment of the upper lobe, more often than the basal segments of the lower lobe",
    ],
    "The aspiration branch reads 'Site: Posterior segment of upper lobe > Superior segment of lower lobe', the greater-than sign giving the order.",
)

add(
    S4, 289, "recall",
    "Which five-step pathogenesis sequence is printed for lung abscess?",
    "Consolidation plus suppuration plus necrosis → rupture of abscess → drains into bronchus → purulent expectoration → abscess with air fluid level",
    [
        "Consolidation plus suppuration plus necrosis → fibrosis → drains into bronchus → purulent expectoration → abscess with air fluid level",
        "Consolidation plus cavitation → rupture of abscess → drains into the pleural space → empyema → abscess with air fluid level",
        "Suppuration plus necrosis → rupture of abscess → drains into bronchus → hemoptysis → abscess with air fluid level",
    ],
    "The flow reads 'Consolidation + Suppuration + Necrosis → Rupture of abscess → Drains into bronchus → Purulent expectoration → Abscess with air fluid level'.",
)

add(
    S4, 289, "fillup",
    "The most common site of a lung abscess is the posterior segment of the right ______ lobe.",
    "upper",
    ["lower", "middle", "lingular"],
    "The site line reads 'Posterior segment of right upper lobe (m/c)', the segmental anatomy explaining why aspiration favours it.",
)

add(
    S4, 289, "recall",
    "How are the fever and chills of a lung abscess modified by drainage, and what does the patient expectorate?",
    "Toxicity decreases when the abscess drains into the bronchus, and the cough produces purulent sputum",
    [
        "Toxicity increases when the abscess drains into the bronchus, and the cough is dry",
        "Toxicity decreases when the abscess drains into the pleural space, and the cough produces blood",
        "Toxicity is unaffected by drainage, and the cough produces purulent sputum",
    ],
    "The clinical bullets read 'Fever, chills (Toxicity decreases on drainage into bronchus)' and 'Cough with purulent sputum'.",
)

add(
    S4, 289, "recall",
    "Which four examination findings are printed for a lung abscess?",
    "Tachypnea, impaired percussion, cavity-related bronchial breathing and clubbing in a chronic abscess",
    [
        "Bradypnea, impaired percussion, cavity-related bronchial breathing and clubbing in acute abscess",
        "Tachypnea, hyper-resonant percussion, cavity-related bronchial breathing and clubbing in chronic abscess",
        "Tachypnea, impaired percussion, absent breath sounds and peripheral edema",
    ],
    "The O/E list reads 'Tachypnea, impaired percussion', 'Cavity related bronchial breathing' and 'Clubbing: In chronic abscess'.",
)

add(
    S4, 289, "recall",
    "Which diagnostic sequence is printed under Diagnosis on page 289?",
    "Pneumonia with poor response to treatment over 2–3 days, then purulent sputum and toxicity, with a chest X-ray or CT showing an air fluid level",
    [
        "Pneumonia with poor response to treatment over 2–3 weeks, then purulent sputum and toxicity, with a chest X-ray showing consolidation only",
        "Pneumonia with rapid response to treatment, then hemoptysis, with a chest X-ray showing an air fluid level",
        "Pneumonia with poor response to treatment over 2–3 days, then dry cough, with CT showing a ground glass opacity",
    ],
    "The clinical line reads 'Pneumonia with poor response to Rx → 2-3 days → Purulent sputum → Toxicity', and the imaging line 'Chest X-ray/CT: Air fluid level'.",
)

# ---------------------------------------------------------------- Unit 5: p290
add(
    S5, 290, "match",
    "Match each caption in the upper strip of page 290 to its finding — 1) Lung window CT 2) Chest film 3) Second chest film … A) Thick walled cavity B) Ground glass opacity C) Pleural effusion",
    "1-B, 2-C, 3-A",
    ["1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-C, 2-B, 3-A"],
    "The three captions read 'Ground glass opacity', 'Pleural effusion' and 'Thick walled cavity' in that left-to-right order.",
)

add(
    S5, 290, "recall",
    "Which four complications of a lung abscess are printed on page 290?",
    "Metastatic infection, pyopneumothorax, bronchopleural fistula and AA (secondary) amyloidosis",
    [
        "Metastatic infection, empyema, bronchopleural fistula and AA (secondary) amyloidosis",
        "Metastatic infection, pyopneumothorax, bronchopleural fistula and AL amyloidosis",
        "Septicemia, pyopneumothorax, bronchopleural fistula and AA (secondary) amyloidosis",
    ],
    "The list reads metastatic infection, pyopneumothorax, bronchopleural fistula and 'AA amyloidosis (Secondary amyloidosis)'.",
)

add(
    S5, 290, "recall",
    "In which three diseases is AA amyloidosis seen according to the note on page 290?",
    "TB, bronchiectasis and lung abscess",
    [
        "TB, bronchiectasis and lymphoma",
        "TB, cystic fibrosis and lung abscess",
        "Sarcoidosis, bronchiectasis and lung abscess",
    ],
    "The note reads 'AA amyloidosis seen in: TB, bronchiectasis, lung abscess', a trio of chronic suppurative or granulomatous infections.",
)

add(
    S5, 290, "fillup",
    "The D/d list for a cavitating lung lesion prints TB, malignancy, Nocardia and ______.",
    "Actinomycetes",
    ["Aspergillus", "Actinomyces", "Rhodococcus"],
    "The four-item column reads 'TB', 'malignancy', 'Nocardia' and 'Actinomycetes' — the last spelled as printed, without a bracketed discriminator.",
)

add(
    S5, 290, "recall",
    "Which regimen and duration are printed for a lung abscess on page 290?",
    "Antibiotics with postural drainage using vancomycin, piperacillin–tazobactam and clindamycin for anaerobes, for 6–8 weeks",
    [
        "Antibiotics with postural drainage using vancomycin, meropenem and clindamycin for 2 weeks",
        "Antibiotics alone using vancomycin and clindamycin for 6–8 weeks",
        "Antibiotics with postural drainage using piperacillin–tazobactam and clindamycin for 10 days",
    ],
    "The treatment block reads 'Antibiotics with postural drainage: Vancomycin + Piptaz + Clindamycin (Anaerobes)', '6–8 weeks therapy', with response as fever resolution in 7–10 days and surgery only if unresponsive to MDR organisms.",
)

add(
    S5, 290, "numeric",
    "How quickly should fever resolve on treatment, and when is surgery considered?",
    "Fever resolves in 7–10 days, and surgery is for unresponsive disease with MDR organisms",
    [
        "Fever resolves in 48–72 hours, and surgery is for unresponsive disease with MDR organisms",
        "Fever resolves in 7–10 days, and surgery is routine after 2 weeks of antibiotics",
        "Fever resolves in 3 weeks, and surgery is for any residual cavity",
    ],
    "The response line reads 'Resolution of fever in 7-10 days', and the next bullet reads 'Surgery: If unresponsive (MDR organisms)'.",
)

add(
    S5, 290, "oddoneout",
    "Pick the ODD ONE OUT — three labels are printed around the CT panel at the foot of page 290, one is not:",
    "Bronchiectasis",
    ["Consolidation", "Air fluid levels", "CT images with air fluid levels"],
    "The CT strip is captioned 'CT images with air fluid levels', and the right-hand image is labelled both 'Consolidation' and 'Air fluid levels'; bronchiectasis is not labelled anywhere on the page.",
)

# ---------------------------------------------------------------- Unit 6: p291
add(
    S6, 291, "recall",
    "Which three states define the severely immunocompromised patient on page 291?",
    "Neutropenia from any cause, post transplant recipients of bone marrow or kidney, and high dose steroid above 30 mg for 3–4 weeks",
    [
        "Neutropenia from any cause, post transplant recipients of bone marrow or kidney, and high dose steroid above 10 mg for 3–4 weeks",
        "Lymphopenia from any cause, post transplant recipients of liver or kidney, and high dose steroid above 30 mg for 3–4 weeks",
        "Neutropenia from any cause, post transplant recipients of bone marrow or kidney, and low dose steroid for 3–4 months",
    ],
    "The bullets read 'Neutropenia (Any cause)', 'Post transplant recepients (Bone marrow, renal)' and 'High dose steroid (>30 mg for 3–4 weeks)'.",
)

add(
    S6, 291, "recall",
    "Which four organisms are bracketed as having predominant lung involvement in the immunocompromised?",
    "Aspergillus, Nocardia, Pneumocystis jirovecii and MDR gram-negative organisms, with toxoplasma, CMV and candida listed separately",
    [
        "Aspergillus, Nocardia, Pneumocystis jirovecii and Candida, with toxoplasma, CMV and MDR gram-negative organisms listed separately",
        "Aspergillus, Actinomyces, Pneumocystis jirovecii and MDR gram-negative organisms, with toxoplasma, CMV and candida listed separately",
        "Cryptococcus, Nocardia, Pneumocystis jirovecii and MDR gram-negative organisms, with toxoplasma, CMV and candida listed separately",
    ],
    "The organism block reads 'mainly MDR gram negative', then brackets Aspergillus, Nocardia and Pneumocystis jirovecii as 'Predominant lung involvement', with toxoplasma, CMV and candida in the right-hand column.",
)

add(
    S6, 291, "match",
    "Match each post-renal-transplant period to its printed infections — 1) <1 month 2) 1–6 months 3) >6 months … A) Drug induced neutropenia with BK polyoma virus, Nocardia and Aspergillus B) Wound, catheter site, drain site infection, UTI and herpes C) CMV, Pneumocystis jirovecii, Legionella, Listeria and hepatitis B and C",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The timeline reads <1 month for wound, catheter, drain, UTI and herpes; 1–6 months as the commonest period for CMV, PCP, Legionella, Listeria and hepatitis B/C; >6 months for drug-induced neutropenia with BK polyoma, Nocardia and Aspergillus.",
)

add(
    S6, 291, "fillup",
    "The commonest post-renal-transplant infection window is ______ months.",
    "1–6",
    ["0–1", "6–12", "12–24"],
    "The middle branch is labelled '1-6 months (m/c)', carrying CMV, Pneumocystis, Legionella, Listeria and hepatitis B and C.",
)

add(
    S6, 291, "recall",
    "Which drugs are printed as causing neutropenia beyond 6 months after renal transplant, and which infections follow?",
    "Mycophenolate mofetil and calcineurin inhibitors, followed by BK polyoma virus, Nocardia and Aspergillus",
    [
        "Mycophenolate mofetil and calcineurin inhibitors, followed by CMV, PCP and Legionella",
        "Azathioprine and calcineurin inhibitors, followed by BK polyoma virus, Nocardia and Aspergillus",
        "Mycophenolate mofetil and corticosteroids, followed by BK polyoma virus, Listeria and Aspergillus",
    ],
    "The >6 month branch reads 'Drug induced neutropenia (mycophenolate mofetil, calcineurin inhibitors) → ↓CMI → Infection by BK polyoma virus, Nocardia, Aspergillus'.",
)

add(
    S6, 291, "match",
    "Match each post-bone-marrow-transplant period to its printed pathogens — 1) <1 month (neutropenia positive) 2) 1–4 months … A) CMV, Pneumocystis jirovecii and Aspergillus B) Gram negative bacteria and Aspergillus",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The bone marrow timeline reads <1 month for gram negative bacteria and Aspergillus, then 1–4 months for CMV, PCP and Aspergillus.",
)

add(
    S6, 291, "recall",
    "Which organism is matched to each clinical clue printed at the foot of page 291?",
    "CMV to ocular involvement and organomegaly, Nocardia to neurological involvement and nodules, and Pseudomonas to ecthyma gangrenosum",
    [
        "CMV to neurological involvement and nodules, Nocardia to ocular involvement and organomegaly, and Pseudomonas to ecthyma gangrenosum",
        "CMV to ocular involvement and organomegaly, Nocardia to ecthyma gangrenosum, and Pseudomonas to neurological involvement",
        "HSV to ocular involvement and organomegaly, Nocardia to neurological involvement and nodules, and Pseudomonas to ecthyma gangrenosum",
    ],
    "The three lines read 'CMV: Ocular involvement, organomegaly', 'Nocardia: Neurological involvement, nodules' and 'Pseudomonas: Ecthyma gangrenosum', the last captioned in the photograph.",
)

add(
    S6, 291, "match",
    "Match each onset pattern to its printed organisms — 1) Acute onset at 24–48 hours 2) Subacute onset … A) Virus, TB and fungi B) Bacteria, gram negative",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The onset block reads 'Acute onset (24-48 hours): Bacteria (Gram negative)' against 'Subacute onset: Virus, TB, fungi'.",
)

# ---------------------------------------------------------------- Unit 7: p292
add(
    S7, 292, "recall",
    "Which three-step etiopathogenesis is printed for invasive aspergillosis?",
    "Conidia or conidiospores aerosolised from the mold form → reach tissues → form invasive filaments (hyphae)",
    [
        "Conidia or conidiospores aerosolised from the yeast form → reach tissues → form invasive filaments (hyphae)",
        "Hyphae aerosolised from the mold form → reach tissues → form conidia",
        "Conidia inhaled into the alveoli → germinate in macrophages → form a fungal ball",
    ],
    "The ladder reads 'Pathogen: Conidia/conidiospores (Aerosolised from the mold form)' → 'Reaches tissues' → 'Forms invasive filaments (Hyphae)', with neutropenia flagged as the most important risk factor.",
)

add(
    S7, 292, "fillup",
    "The most important risk factor for invasive aspergillosis printed on page 292 is ______.",
    "neutropenia",
    ["steroid use", "diabetes", "smoking"],
    "The risk factor box reads 'Neutropenia (most important)', which is why the disease is drawn in the neutropenic host.",
)

add(
    S7, 292, "recall",
    "How is the CT halo sign described, and what does it suggest?",
    "Consolidation surrounded by ground glass opacification, suggestive of invasive aspergillosis",
    [
        "Ground glass opacification surrounded by consolidation, seen in cryptogenic organizing pneumonia",
        "A crescent of air within consolidation, indicating recovery",
        "A cavity with an air fluid level, indicating abscess",
    ],
    "The halo sign bullet reads 'Consolidation surrounded by ground glass opacification (GGO)' and 'Suggestive of invasive aspergillosis'.",
)

add(
    S7, 292, "recall",
    "What does the air crescent sign indicate, and what is its printed appearance?",
    "It indicates recovery, appearing as a crescent in consolidation",
    [
        "It indicates active invasion, appearing as a crescent in a cavity",
        "It indicates recovery, appearing as a halo around consolidation",
        "It indicates fungal ball formation, appearing as a crescent in a bulla",
    ],
    "The air crescent sign bullets read 'Indicates recovery' and 'Crescent in consolidation', and the adjacent CT is captioned 'Air crescent sign'.",
)

add(
    S7, 292, "recall",
    "How is the reverse halo sign defined, and in which disease is it seen?",
    "Ground glass opacification surrounded by consolidation, seen in cryptogenic organizing pneumonia",
    [
        "Consolidation surrounded by ground glass opacification, seen in cryptogenic organizing pneumonia",
        "Ground glass opacification surrounded by consolidation, seen in invasive aspergillosis",
        "A crescent of air inside consolidation, seen in aspergilloma",
    ],
    "The note reads 'Reverse halo sign: GGO surrounded by consolidation. Seen in cryptogenic organizing pneumonia', the exact inversion of the aspergillus halo.",
)

add(
    S7, 292, "recall",
    "What does the printed monad sign describe?",
    "An air crescent around a fungal ball which moves with change in position, seen in aspergilloma in an old case of TB",
    [
        "An air crescent around a fungal ball which is fixed in position, seen in invasive aspergillosis",
        "A crescent of air within consolidation which indicates recovery, seen in neutropenic hosts",
        "Ground glass surrounding consolidation which changes with position, seen in organizing pneumonia",
    ],
    "The note reads 'monad sign in xray: Air crescent seen around fungal ball. moves with change in position. Seen in aspergilloma in old case of TB', the movement distinguishing it from a fixed crescent.",
)

add(
    S7, 292, "match",
    "Match each clinical manifestation of invasive aspergillosis to its printed description — 1) Classical presentation 2) CNS infection 3) Angioinvasion … A) 100% mortality B) Hemorrhagic infarction C) Fever, hemoptysis and pleuritic pain",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "The classical triad is fever, hemoptysis and pleuritic pain; CNS infection is printed with 100% mortality; and angioinvasion leads to hemorrhagic infarction, with sinus infection listed alongside.",
)

# ---------------------------------------------------------------- Unit 8: p293
add(
    S8, 293, "recall",
    "Which four diagnostic modalities are printed for invasive aspergillosis?",
    "BAL showing dichotomous branching septate hyphae, VATS biopsy from a nodule, the galactomannan test and the β-D-glucan test",
    [
        "BAL showing aseptate right-angle branching hyphae, VATS biopsy, the galactomannan test and the β-D-glucan test",
        "BAL showing dichotomous branching septate hyphae, sputum culture, the galactomannan test and the tuberculin test",
        "BAL showing dichotomous branching septate hyphae, VATS biopsy, the galactomannan test and the urinary antigen test",
    ],
    "The diagnosis block reads 'BAL: Dichotomous branching septate hyphae', 'Video assisted thoracoscopic surgery (VATS): biopsy from nodule', 'Galactomannan test: Specific for invasive aspergillosis' and the β-D-glucan test.",
)

add(
    S8, 293, "recall",
    "Which organisms give a positive β-D-glucan test according to the printed list?",
    "Mucor, cryptococcus, candida, aspergillosis and pneumocystis",
    [
        "Mucor, cryptococcus, candida, aspergillosis and nocardia",
        "Aspergillus, candida, pneumocystis, histoplasma and cryptococcus",
        "Mucor, aspergillosis, pneumocystis, blastomyces and coccidioides",
    ],
    "The line reads 'β-D-glucan test: Positive for mucor, cryptococcus, candida, aspergillosis, pneumocystis', which is why the test is useful but not specific.",
)

add(
    S8, 293, "match",
    "Match each antifungal to its printed role in aspergillosis — 1) Voriconazole 2) Liposomal amphotericin B … A) The alternative agent B) The drug of choice",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The treatment list reads 'voriconazole (DOC)' and 'Liposomal amphotericin B', making amphotericin the second agent for aspergillosis.",
)

add(
    S8, 293, "recall",
    "Which five findings distinguish mucormycosis from aspergillosis on page 293?",
    "Aseptate hyphae, right angle branching, a negative galactomannan test, no response to voriconazole, and treatment with liposomal amphotericin B plus posaconazole and surgical debridement",
    [
        "Septate hyphae, right angle branching, a negative galactomannan test, no response to voriconazole, and treatment with liposomal amphotericin B plus posaconazole and surgical debridement",
        "Aseptate hyphae, acute angle branching, a positive galactomannan test, no response to voriconazole, and treatment with voriconazole plus debridement",
        "Aseptate hyphae, right angle branching, a negative galactomannan test, response to voriconazole, and treatment with itraconazole alone",
    ],
    "The mucormycosis note reads aseptate hyphae, right angle branching, negative galactomannan, no response to voriconazole and 'Rx: Liposomal amphotericin B with posaconazole + surgical debridement of infected tissue'.",
)

add(
    S8, 293, "fillup",
    "The hyphae of mucormycosis are ______, in contrast with the septate hyphae of aspergillus.",
    "aseptate",
    ["septate", "branched", "pigmented"],
    "The mucormycosis list opens 'Aseptate hyphae' with a caption 'Aseptate hyphae', directly contrasting the septate hyphae of aspergillus on the BAL line above.",
)

add(
    S8, 293, "recall",
    "Which fungal infection opens the Pneumocystis section, and in which two host groups does it arise?",
    "A fungal infection seen in HIV when CD4 is <200/μL and in the immunocompromised",
    [
        "A fungal infection seen in HIV when CD4 is <500/μL and in the immunocompromised",
        "A bacterial infection seen in HIV when CD4 is <200/μL and in the immunocompromised",
        "A fungal infection seen in HIV when CD4 is <200/μL and in the immunocompetent",
    ],
    "The lines read 'Fungal infection' and 'Seen in HIV (CD4: <200/μL), immunocompromised', the CD4 threshold being the tested number.",
)

add(
    S8, 293, "recall",
    "Which sequence describes the clinical features of Pneumocystis jirovecii infection?",
    "Dyspnea and hypoxia, then fever and cough after 2–3 days",
    [
        "Fever and cough, then dyspnea and hypoxia after 2–3 days",
        "Dyspnea and hypoxia, then hemoptysis and chest pain after 2–3 days",
        "Dyspnea and cyanosis, then fever and purulent sputum after 7 days",
    ],
    "The clinical block reads 'Dyspnea', 'Hypoxia' with an arrow '2–3 days' down to 'Fever, cough' — a subacute hypoxia-first presentation.",
)

add(
    S8, 293, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed as giving a positive β-D-glucan test, one is not:",
    "Nocardia",
    ["Mucor", "Cryptococcus", "Pneumocystis"],
    "The printed list is 'mucor, cryptococcus, candida, aspergillosis, pneumocystis'; Nocardia appears on this page only as an organism of the immunocompromised lung, never in the β-D-glucan list.",
)

# ---------------------------------------------------------------- Unit 9: p294
add(
    S9, 294, "recall",
    "Which six diagnostic points are printed for Pneumocystis on page 294?",
    "1,3 β-D-glucan positive but non-specific, raised LDH, BAL microscopy as the best mode with GMS cyst staining, fluorescein conjugated monoclonal antibody, PCR as gold standard, and diffuse perihilar infiltrates on chest X-ray",
    [
        "1,3 β-D-glucan positive and specific, raised LDH, BAL microscopy with GMS trophozoite staining, fluorescein antibody, PCR as gold standard, and perihilar infiltrates",
        "1,3 β-D-glucan negative, raised LDH, BAL microscopy with GMS cyst staining, fluorescein antibody, culture as gold standard, and perihilar infiltrates",
        "1,3 β-D-glucan positive but non-specific, raised LDH, BAL microscopy with GMS cyst staining, fluorescein antibody, PCR as gold standard, and lobar consolidation",
    ],
    "The diagnosis block reads '1,3 β-D-glucan test positive (Non specific)', '↑LDH', 'BAL: microscopy — Best mode of diagnosis; methenamine silver stain (GMS): Cyst form', the fluorescein antibody, 'PCR: gold standard' and chest X-ray perihilar infiltrates.",
)

add(
    S9, 294, "fillup",
    "The best mode of diagnosis for Pneumocystis is BAL microscopy with methenamine silver stain, which demonstrates the ______ form.",
    "cyst",
    ["trophozoite", "sporozoite", "hyphal"],
    "The BAL block reads 'methenamine silver stain (GMS): Cyst form', the cyst being what silver stains in this infection.",
)

add(
    S9, 294, "recall",
    "Which four complications may the perihilar infiltrates of Pneumocystis show on imaging?",
    "Cavity, pneumothorax and pneumatocele, with the caption showing a cyst with bilateral infiltrates",
    [
        "Cavity, pneumothorax and pleural effusion, with the caption showing a cyst with bilateral infiltrates",
        "Cavity, pneumothorax and honeycomb change, with the caption showing a cyst with unilateral infiltrates",
        "Cavity, pleural effusion and pneumatocele, with the caption showing a bulla with bilateral infiltrates",
    ],
    "The arrow from the perihilar infiltrates reads 'Cavity, pneumothorax, Pneumatocele', and the second film is captioned 'Cyst with B/L infiltrates'.",
)

add(
    S9, 294, "recall",
    "Which four HIV records are bracketed for Pneumocystis on page 294?",
    "Most common fungal pneumonia, most common opportunistic infection, most common cause of pneumonia and most common cause of pleural effusion in HIV",
    [
        "Most common fungal pneumonia, most common opportunistic infection, most common cause of pneumothorax and most common cause of pleural effusion in HIV",
        "Most common bacterial pneumonia, most common opportunistic infection, most common cause of pneumonia and most common cause of pleural effusion in HIV",
        "Most common fungal pneumonia, rare opportunistic infection, most common cause of pneumonia and most common cause of pleural effusion in HIV",
    ],
    "The brace 'In HIV' encloses 'm/c: Fungal pneumonia, Opportunistic infection, Cause of pneumonia, Cause of pleural effusion'.",
)

add(
    S9, 294, "match",
    "Match each Pneumocystis treatment line to its printed description — 1) First line mild to moderate 2) First line severe 3) Second line … A) IV cotrimoxazole B) Clindamycin plus primaquine and IV pentamidine C) Oral cotrimoxazole",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "Mild to moderate disease takes oral cotrimoxazole, severe disease IV cotrimoxazole, and second line is clindamycin + primaquine or IV pentamidine with increased side effects.",
)

add(
    S9, 294, "numeric",
    "At which PaO₂ does the printed protocol add a steroid in Pneumocystis?",
    "<70 mm Hg, or a raised arterio-alveolar O₂ gradient",
    [
        "<55 mm Hg, or a raised arterio-alveolar O₂ gradient",
        "<70 mm Hg, or a raised arterial–venous O₂ difference",
        "<90 mm Hg, or any oxygen requirement",
    ],
    "The hypoxia bullet reads 'PaO2: <70 mm Hg or arterio-alveolar O2 gradient ↑' with 'Steroid' beneath it.",
)

add(
    S9, 294, "match",
    "Match each prophylactic agent to the printed list — 1) First 2) Second 3) Third … A) Dapsone B) Atovaquone C) Cotrimoxazole",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "The prophylaxis column reads cotrimoxazole, dapsone and atovaquone in that order.",
)

# ---------------------------------------------------------------- Unit 10: p295
add(
    S10, 295, "recall",
    "Which four microbiological features are printed for Nocardia asteroides?",
    "Gram positive filamentous fungi, aerobic, acid fast and with filamented mycelia",
    [
        "Gram negative filamentous fungi, anaerobic, acid fast and with filamented mycelia",
        "Gram positive filamentous fungi, aerobic, non-acid fast and with non-filamented mycelia",
        "Gram positive filamentous bacteria, aerobic, acid fast and with non-filamented mycelia",
    ],
    "The block reads 'Gram positive filamentous fungi', 'Aerobic', 'Acid fast' and 'Filamented mycelia' — the word 'fungi' being printed even for this bacterium.",
)

add(
    S10, 295, "match",
    "Match each organism to its printed staining character — 1) Actinomycetes 2) Rhodococci 3) Nocardia … A) Acid fast and non-filamentous B) Non-acid fast and non-aerobic C) Acid fast and filamentous",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "The note reads 'Actinomycetes: Non-acid fast, non-aerobic' and 'Rhodococci: Acid fast, non-filamentous', against the acid-fast filamentous Nocardia above them.",
)

add(
    S10, 295, "fillup",
    "For Nocardia, a host defence defect is printed as ______.",
    "mandatory",
    ["optional", "rare", "protective"],
    "The transmission block reads 'Host defence defect: mandatory', followed by inhalation or skin defect as the modes of entry.",
)

add(
    S10, 295, "recall",
    "Which two clinical patterns are printed for Nocardia in the lung and CNS?",
    "CNS: subacute brain abscess; lung: cavitating nodules and nocardial mycetoma",
    [
        "CNS: acute meningitis; lung: cavitating nodules and nocardial mycetoma",
        "CNS: subacute brain abscess; lung: lobar consolidation and pleural effusion",
        "CNS: subacute brain abscess; lung: miliary nodules and hilar lymphadenopathy",
    ],
    "The clinical section reads 'CNS: Subacute brain abscess' and under lung 'Cavitating nodules' and 'Nocardial mycetoma', with the CT and film captions below.",
)

add(
    S10, 295, "recall",
    "What does the sputum or pus examination show in nocardiosis, and why is culture not done?",
    "Crooked branching beaded filaments that are acid fast, with culture not done because of slow growth",
    [
        "Straight branching septate filaments that are acid fast, with culture not done because of slow growth",
        "Crooked branching beaded filaments that are non-acid fast, with culture not done because of fastidious growth",
        "Crooked branching beaded filaments that are acid fast, with culture the gold standard because of rapid growth",
    ],
    "The diagnosis block reads 'Crooked branching beaded filaments', 'Acid fast' and 'Culture not done d/t slow growth', with the Gram stain photograph beside it.",
)

add(
    S10, 295, "recall",
    "Which three drugs are printed for Nocardia, and which is the drug of choice?",
    "Sulfonamide as the drug of choice, with minocycline and parenteral amikacin",
    [
        "Cotrimoxazole as the drug of choice, with minocycline and parenteral amikacin",
        "Sulfonamide as the drug of choice, with doxycycline and parenteral amikacin",
        "Sulfonamide as the drug of choice, with minocycline and oral amikacin",
    ],
    "The treatment block reads 'Sulfonamide (DOC), minocycline' and 'Amikacin (Parenteral)'.",
)

add(
    S10, 295, "scenario",
    "A renal transplant recipient on high dose steroids develops a subacute brain abscess and cavitating lung nodules; pus shows acid-fast crooked beaded filaments. Which organism and drug of choice fit the page?",
    "Nocardia asteroides treated with a sulfonamide",
    [
        "Actinomyces treated with a sulfonamide",
        "Rhodococcus treated with a sulfonamide",
        "Nocardia asteroides treated with voriconazole",
    ],
    "Nocardia requires a host defence defect, gives a subacute brain abscess with cavitating lung nodules, shows acid-fast crooked beaded filaments and is treated with sulfonamide as DOC; actinomycetes are non-acid fast and rhodococci are non-filamentous.",
)

# ---------------------------------------------------------------- extra interactives
add(
    S1, 286, "scenario",
    "A 22-year-old student has a week of low grade fever and dry cough with scanty sputum and almost no chest signs; cold agglutinins are positive. Which organism and drug of choice does the page support?",
    "Mycoplasma, treated with azithromycin",
    [
        "Chlamydia, treated with azithromycin",
        "Legionella, treated with azithromycin and rifampicin",
        "Mycoplasma, treated with a sulfonamide",
    ],
    "Mycoplasma gives low grade fever, cough, scanty sputum and a paucity of signs with cold antibody autoimmune hemolysis, and azithromycin is printed as DOC.",
)

add(
    S1, 286, "oddoneout",
    "Pick the ODD ONE OUT — three are printed extrapulmonary manifestations of mycoplasma, one belongs to chlamydia:",
    "Atherosclerosis",
    ["Bullous myringitis", "Encephalitis", "Arthralgia with adenopathy"],
    "The mycoplasma list prints cold antibody hemolysis, SJS, GBS, encephalitis, bullous myringitis, myocarditis/pericarditis and arthralgia with adenopathy; atherosclerosis is the single extrapulmonary manifestation given for chlamydia.",
)

add(
    S2, 287, "truefalse",
    "TRUE or FALSE about chlamydia on page 287.",
    "True — it lacks peptidoglycan and is resistant to sulfonamide",
    [
        "True — it has a thick peptidoglycan wall and is resistant to sulfonamide",
        "False — it lacks peptidoglycan and is highly sensitive to sulfonamide",
        "False — it is an extracellular organism transmitted from animals",
    ],
    "The chlamydia bullets read 'Absence of peptidoglycan' and, under treatment, 'Resistant to sulfonamide' with azithromycin or doxycycline used instead.",
)

add(
    S3, 288, "scenario",
    "A returning cruise passenger has high fever, diarrhea and hyponatremia with bilateral dense consolidation. Which organism and regimen does page 288 suggest?",
    "Legionella, treated with azithromycin plus rifampicin",
    [
        "Mycoplasma, treated with azithromycin plus rifampicin",
        "Legionella, treated with a sulfonamide",
        "Chlamydia, treated with azithromycin plus rifampicin",
    ],
    "Cruise travel points to Legionella in the etiology table, the atypical picture prints diarrhea and hyponatremia, and treatment is 'Azithromycin (DOC) + Rifampicin'.",
)

add(
    S3, 288, "scenario",
    "A respiratory sample in a suspected Legionella case shows numerous pus cells and neutrophils but no organisms on Gram stain. How does the page explain this?",
    "The Gram stain is characteristically negative for organisms even with abundant pus cells",
    [
        "The sample must have been taken after antibiotics, which always sterilises the stain",
        "The finding excludes Legionella and points to mycoplasma",
        "The finding is diagnostic of Nocardia, which is not seen on Gram stain",
    ],
    "The Gram staining findings read 'Pus cells, neutrophils +' and 'No organisms seen', which is why DFAT and urinary antigen are used instead.",
)

add(
    S4, 289, "scenario",
    "A patient with poor dentition and episodes of reduced consciousness develops a chronic abscess in the posterior segment of the upper lobe. Which cause and organism does the page print?",
    "Aspiration pneumonia with anaerobes",
    [
        "Necrotising pneumonia with Staphylococcus",
        "Aspiration pneumonia with Klebsiella",
        "Necrotising pneumonia with anaerobes",
    ],
    "Aspiration pneumonia presents with chronic symptoms, anaerobes and a posterior upper lobe site that outranks the superior lower lobe segment; staphylococcus and klebsiella belong to necrotising pneumonia.",
)

add(
    S5, 290, "truefalse",
    "TRUE or FALSE about AA amyloidosis on page 290.",
    "True — it is seen in TB, bronchiectasis and lung abscess",
    [
        "True — it is seen in TB, bronchiectasis and lymphoma",
        "False — AA amyloidosis is not a complication of chronic lung infection",
        "False — it is seen only in multiple myeloma",
    ],
    "The note reads 'AA amyloidosis seen in: TB, bronchiectasis, lung abscess', and it is listed as a complication of lung abscess, AL type being the myeloma-associated form.",
)

add(
    S6, 291, "scenario",
    "A renal transplant recipient develops pneumonia four months after surgery. Which organisms does the printed timeline expect?",
    "CMV, Pneumocystis jirovecii, Legionella, Listeria and hepatitis B and C",
    [
        "Wound, catheter site and drain site infection with herpes",
        "BK polyoma virus, Nocardia and Aspergillus",
        "Gram negative bacteria and Aspergillus only",
    ],
    "The 1–6 month branch is the commonest and lists CMV, Pneumocystis jirovecii, Legionella, Listeria and hepatitis B and C; the wound and herpes group belongs to the first month.",
)

add(
    S6, 291, "scenario",
    "Eight months after renal transplant a patient on mycophenolate has neutropenia and a new pulmonary infiltrate. Which organisms does the >6 month branch list?",
    "BK polyoma virus, Nocardia and Aspergillus",
    [
        "CMV, Pneumocystis jirovecii and Legionella",
        "Wound infection, UTI and herpes",
        "Gram negative bacteria and Aspergillus only",
    ],
    "The >6 month branch runs drug-induced neutropenia from mycophenolate mofetil or calcineurin inhibitors → ↓CMI → BK polyoma virus, Nocardia and Aspergillus.",
)

add(
    S7, 292, "scenario",
    "A neutropenic patient with leukaemia has fever and hemoptysis, and CT shows consolidation ringed by ground glass. Which sign, diagnosis and drug of choice does the page give?",
    "The halo sign, invasive aspergillosis, treated with voriconazole",
    [
        "The air crescent sign, invasive aspergillosis, treated with voriconazole",
        "The reverse halo sign, cryptogenic organizing pneumonia, treated with steroids",
        "The monad sign, aspergilloma, treated with surgery",
    ],
    "The halo sign is consolidation surrounded by ground glass and is suggestive of invasive aspergillosis, for which voriconazole is DOC; the air crescent instead indicates recovery.",
)

add(
    S7, 292, "scenario",
    "Three weeks into treatment for invasive aspergillosis a repeat CT shows a crescent of air inside the consolidating lesion. How does the page read this?",
    "An air crescent sign, which indicates recovery",
    [
        "An air crescent sign, which indicates progressive invasion",
        "A reverse halo sign, which indicates organizing pneumonia",
        "A monad sign, which indicates a fungal ball",
    ],
    "The air crescent sign bullets read 'Indicates recovery' and 'Crescent in consolidation', in contrast with the reverse halo and the monad sign of an aspergilloma.",
)

add(
    S8, 293, "oddoneout",
    "Pick the ODD ONE OUT — three are printed for mucormycosis, one belongs to aspergillosis:",
    "Septate hyphae with dichotomous branching",
    ["Aseptate hyphae", "Right angle branching", "Negative galactomannan test"],
    "Mucormycosis shows aseptate hyphae, right angle branching, a negative galactomannan test and no response to voriconazole; septate dichotomously branching hyphae are the aspergillus finding on BAL.",
)

add(
    S9, 294, "scenario",
    "A patient with HIV and a CD4 count of 120/μL has dyspnea and hypoxia with a PaO₂ of 60 mm Hg and diffuse perihilar infiltrates. Which treatment does the printed protocol give?",
    "IV cotrimoxazole plus a steroid, because the PaO₂ is below 70 mm Hg",
    [
        "Oral cotrimoxazole alone, because the PaO₂ is above 55 mm Hg",
        "Clindamycin plus primaquine as first line",
        "IV pentamidine as first line because of the hypoxia",
    ],
    "Severe disease takes IV cotrimoxazole, and a PaO₂ below 70 mm Hg or a raised arterio-alveolar gradient adds a steroid; clindamycin with primaquine and IV pentamidine are second line.",
)

add(
    S10, 295, "truefalse",
    "TRUE or FALSE about the treatment of Nocardia on page 295.",
    "True — sulfonamide is the drug of choice, with minocycline and parenteral amikacin as alternatives",
    [
        "True — voriconazole is the drug of choice, with sulfonamide as an alternative",
        "False — sulfonamide is contraindicated and amikacin is the drug of choice",
        "False — no antibiotic is effective and surgery alone is used",
    ],
    "The treatment block reads 'Sulfonamide (DOC), minocycline' and 'Amikacin (Parenteral)', with no role for voriconazole on the page.",
)

GUIDES = {
    S1: (
        "Mycoplasma (p286) is the smallest free-living replicating organism, with no cell wall so β-lactams fail, sterols present and no flagella; it causes tracheobronchitis/pharyngitis and pneumonia in 10%, spread by droplets, with low grade fever, cough, scanty sputum and few signs.\n"
        "Extrapulmonary disease covers cold antibody autoimmune hemolysis (IgM), SJS/erythema multiforme, GBS, encephalitis, bullous myringitis, myocarditis/pericarditis and arthralgia with adenopathy; imaging gives reticulonodular or patchy consolidation from the hilum, interstitial and ground glass change and tree-in-bud.\n"
        "PCR of respiratory secretions and serology are rapid and most sensitive, culture is on PPLO agar by Diene's method with fried egg colonies, and azithromycin is DOC with doxycycline and respiratory quinolones as alternatives; hydrogen peroxide and superoxide injure the epithelium but prognosis is good.",
    ),
    S2: (
        "Chlamydia (p287) is an obligate intracellular bacterium without peptidoglycan, transmitted human to human, its elementary body being extracellular, metabolically inactive and infective.\n"
        "It gives a prolonged asymptomatic upper respiratory illness, atypical pneumonia in 10% and walking pneumonia indistinguishable from mycoplasma, with low grade fever, minimal sputum and dry cough, atherosclerosis being the extrapulmonary link; isolation is by HEp-2 cells and micro-immunofluorescence serology is the gold standard, with no lobar consolidation, resistance to sulfonamide and treatment by azithromycin or doxycycline.\n"
        "Legionella is gram negative and predominantly intracellular, a strict aerobe, motile, partially acid fast, living in aquatic bodies and biofilms, with type 1 serovar most pathogenic and a type 4 secretion system.",
    ),
    S3: (
        "Legionella spreads by microaspiration more than aerosolization and grows on BCYE (buffered charcoal yeast extract) medium; Gram stain shows pus cells and neutrophils but no organisms (p288).\n"
        "Risk factors are poor CMI, smoking, immunosuppression and hairy cell leukemia; typical disease is rapidly progressive with high grade fever, bilateral dense consolidation and leucocytosis, while atypical disease gives non-productive cough, diarrhea, hyponatremia, elevated LFT, thrombocytopenia and hematuria; mild disease is Pontiac fever and severe is Legionnaires disease.\n"
        "DFAT and urinary antigen both have high specificity, sputum/aspiration testing is not done, and treatment is azithromycin (DOC) with rifampicin or a quinolone.",
    ),
    S4: (
        "Lung abscess (p289) has two causes: necrotising pneumonia complicating pneumonia from staphylococcus or klebsiella, and aspiration pneumonia with chronic symptoms, anaerobes and a posterior upper lobe predilection over the superior lower lobe segment.\n"
        "Pathogenesis runs consolidation + suppuration + necrosis → rupture → drainage into the bronchus → purulent expectoration → abscess with an air fluid level, the commonest site being the posterior segment of the right upper lobe.\n"
        "Clinically fever and chills ease when the abscess drains, with cough and purulent sputum, tachypnea, impaired percussion, cavity-related bronchial breathing and clubbing in chronic disease; diagnosis is poor response over 2–3 days with purulent sputum and toxicity plus an air fluid level on film or CT.",
    ),
    S5: (
        "Captions on p290 run ground glass opacity, pleural effusion, thick walled cavity, consolidation and air fluid levels.\n"
        "Complications are metastatic infection, pyopneumothorax, bronchopleural fistula and AA (secondary) amyloidosis, the last seen in TB, bronchiectasis and lung abscess; the differential is TB, malignancy, Nocardia and Actinomycetes with no bracketed clue.\n"
        "Treatment is antibiotics with postural drainage — vancomycin, piperacillin–tazobactam and clindamycin for anaerobes — for 6–8 weeks, fever resolving in 7–10 days and surgery reserved for unresponsive MDR disease.",
    ),
    S6: (
        "The severely immunocompromised (p291) are neutropenic from any cause, transplant recipients of bone marrow or kidney, and those on >30 mg steroid for 3–4 weeks; organisms are mainly MDR gram-negative with Aspergillus, Nocardia and PCP predominant in the lung, plus toxoplasma, CMV and candida.\n"
        "Post renal transplant: <1 month wound, catheter, drain site, UTI and herpes; 1–6 months (m/c) CMV, PCP, Legionella, Listeria and hepatitis B/C; >6 months drug-induced neutropenia from mycophenolate or calcineurin inhibitors giving BK polyoma, Nocardia and Aspergillus.\n"
        "Post bone marrow transplant: <1 month gram-negative bacteria and Aspergillus, then 1–4 months CMV, PCP and Aspergillus; acute onset at 24–48 hours means bacteria, subacute means virus, TB or fungi, with CMV ocular/organomegaly, Nocardia neurological/nodules and Pseudomonas ecthyma gangrenosum.",
    ),
    S7: (
        "Invasive aspergillosis (p292) starts with conidia aerosolised from the mold, reaching tissue and forming invasive hyphae, with neutropenia the most important risk.\n"
        "The CT halo sign is consolidation surrounded by ground glass and suggests invasion, while the air crescent sign means recovery; the reverse halo is ground glass surrounded by consolidation in cryptogenic organizing pneumonia, and the monad sign is an air crescent around a fungal ball that moves with posture in an old TB aspergilloma.\n"
        "The classical triad is fever, hemoptysis and pleuritic pain, with sinus infection, CNS infection carrying 100% mortality and angioinvasion causing hemorrhagic infarction.",
    ),
    S8: (
        "Diagnosis of aspergillosis (p293) rests on BAL showing dichotomous branching septate hyphae, VATS biopsy of a nodule, the specific galactomannan test and β-D-glucan, which is positive in mucor, cryptococcus, candida, aspergillosis and pneumocystis.\n"
        "Voriconazole is DOC with liposomal amphotericin B as the alternative, and mucormycosis is separated by aseptate right-angle hyphae, negative galactomannan, no voriconazole response and treatment with liposomal amphotericin B plus posaconazole and surgical debridement.\n"
        "Pneumocystis is a fungal infection of HIV with CD4 <200/μL and the immunocompromised, giving dyspnea and hypoxia then fever and cough after 2–3 days.",
    ),
    S9: (
        "Pneumocystis diagnosis (p294) uses a positive but non-specific 1,3 β-D-glucan, raised LDH, BAL microscopy as the best mode with GMS cyst staining, fluorescein conjugated monoclonal antibody, PCR as gold standard and perihilar infiltrates that may cavitate, pneumothorax or pneumatocele.\n"
        "It is the most common fungal pneumonia, opportunistic infection, cause of pneumonia and cause of pleural effusion in HIV; treatment is oral cotrimoxazole for mild-moderate disease, IV cotrimoxazole for severe, and second line clindamycin + primaquine or IV pentamidine.\n"
        "Steroids are added for PaO₂ <70 mm Hg or a raised arterio-alveolar gradient, and prophylaxis is cotrimoxazole, dapsone or atovaquone.",
    ),
    S10: (
        "Nocardia asteroides (p295) is a gram positive filamentous 'fungus' that is aerobic, acid fast and filamented, unlike non-acid-fast non-aerobic actinomycetes and acid-fast non-filamentous rhodococci.\n"
        "A host defence defect is mandatory, entry is by inhalation or a skin defect, and disease is a subacute brain abscess or cavitating lung nodules with nocardial mycetoma.\n"
        "Sputum or pus shows acid-fast crooked branching beaded filaments and culture is avoided because of slow growth; treatment is sulfonamide as DOC with minocycline and parenteral amikacin.",
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
