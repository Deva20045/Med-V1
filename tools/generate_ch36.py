#!/usr/bin/env python3
"""Generate Chapter 36: Bronchiectasis (Book p218–222).

Every question is anchored to a specific printed line, figure caption or
histology panel of uploads/02.pdf sheets 101–105 (Book pages 218–222), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 36
TITLE = "Bronchiectasis"
PAGES = "218-222"

S1 = "Definition (Irreversible Dilatation Plus Obliterative Bronchiolar Fibrosis), Pseudobronchiectasis, the Obstructive-Disease List, Pathogenesis Flowchart and the Normal-vs-Bronchiectasis Diagram"
S2 = "Types of Dilatation (Cylindrical/Varicose/Cystic), Traction Bronchiectasis, Lobe/Sex/Age Distribution and the Four Histological Features"
S3 = "Paediatric Aetiology (Post-Infective, Mounier-Kuhn, William Campbell, Kartagener, Young, Yellow Nail, α1-Antitrypsin), Impaired Mucociliary Clearance, McLeod, IgA Deficiency and Adult Aetiology"
S4 = "Clinical Features (Three-Layered Sputum, Postural Cough, Haemoptysis Mechanism), Examination Findings, Sicca/ABPA Notes, Plain-Film Signs and the Three CT Criteria"
S5 = "Complications (Cor Pulmonale, Massive Haemoptysis, Empyema, Amyloidosis, Abscess), Airway Clearance and CF Therapies, Surgery, Antibiotic Rationale, Macrolide Duration and the Infecting-Organism Hierarchy"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(36000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(36100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p218
add(
    S1, 218, "fillup",
    "Page 218 defines bronchiectasis as abnormal and irreversible dilatation of bronchi (initially medium sized, later the entire bronchial tree) plus ______ fibrosis of bronchioles.",
    "Obliterative",
    ["Interstitial", "Subpleural", "Peribronchial"],
    "The definition joins 'Abnormal and irreversible dilatation of bronchi (Initially medium sized → entire bronchial tree)' with 'Obliterative fibrosis of bronchioles → Obstructive lung disease (can have restrictive component)'. The bronchiolar fibrosis explains the mixed obstructive-restrictive physiology.",
)

add(
    S1, 218, "recall",
    "How does the page 218 note define pseudobronchiectasis, and which two infections are named?",
    "Reversible dilatation of bronchi following infection — influenza and COVID",
    [
        "Irreversible dilatation of bronchioles following infection — influenza and COVID",
        "Reversible dilatation of bronchioles following obstruction — tuberculosis and measles",
        "Reversible dilatation of bronchi following fibrosis — influenza and tuberculosis",
    ],
    "The note reads 'Pseudobronchiectasis : Reversible dilatation of bronchi following infection (Influenza, COVID).' Reversibility is what separates it from the irreversible disease defined in the opening line.",
)

add(
    S1, 218, "truefalse",
    "TRUE or FALSE about how bronchiectasis is classified on page 218.",
    "True — it is listed among the obstructive lung diseases and the definition adds that it can have a restrictive component",
    [
        "False — it is listed among the restrictive lung diseases with no obstructive component",
        "False — it is listed as a purely vascular lung disease",
        "True — it is listed among the obstructive diseases but can never have a restrictive component",
    ],
    "The definition ends '→ Obstructive lung disease (can have restrictive component)', and the list of obstructive diseases places bronchiectasis at item d, after COPD, bronchial asthma and bronchiolitis. Both the obstructive label and the possible restrictive component are printed.",
)

add(
    S1, 218, "recall",
    "Which sequence does the page 218 pathogenesis flowchart print after the initial infective insult?",
    "Infection (mostly TB)/idiopathic → inflammation → loss of smooth muscle and elastic tissue in bronchi → abnormal and irreversible dilatation of bronchi",
    [
        "Infection (mostly TB)/idiopathic → inflammation → goblet cell hyperplasia → loss of smooth muscle → abnormal dilatation",
        "Infection (mostly TB)/idiopathic → fibrosis → loss of cilia → abnormal and irreversible dilatation of bronchioles",
        "Infection (mostly TB)/idiopathic → inflammation → cartilage hypertrophy → abnormal and reversible dilatation of bronchi",
    ],
    "The flowchart runs 'Initial insult : Infection (mostly TB)/idiopathic' → 'Inflammation' → 'Loss of smooth muscle and elastic tissue in bronchi (Bronchi & bronchiole both have smooth muscle)' → 'Abnormal & irreversible dilatation of bronchi'. Goblet cell hyperplasia sits on the separate mucus limb of the chart.",
)

add(
    S1, 218, "recall",
    "The flowchart parenthesises a fact about smooth muscle in the airways. Which statement is printed?",
    "Bronchi and bronchioles both have smooth muscle",
    [
        "Only bronchi have smooth muscle, bronchioles do not",
        "Only bronchioles have smooth muscle, bronchi do not",
        "Neither bronchi nor bronchioles have smooth muscle; only the trachea does",
    ],
    "The bracket after 'Loss of smooth muscle and elastic tissue in bronchi' reads '(Bronchi & bronchiole both have smooth muscle)'. This contrasts with cartilage, which is lost at bronchiolar level and is discussed later in the chapter's treatment rationale.",
)

add(
    S1, 218, "recall",
    "The mucus limb of the page 218 flowchart runs through three steps. Which sequence is printed?",
    "Goblet cell hyperplasia → mucus hypersecretion → obstruction of airway",
    [
        "Goblet cell atrophy → mucus inspissation → dilatation of airway",
        "Goblet cell hyperplasia → mucus hypersecretion → loss of cilia",
        "Mucous gland hyperplasia → serous secretion → bronchospasm",
    ],
    "One arrow of the chart reads '3. Goblet cell hyperplasia → mucus hypersecretion → Obstruction of airway.' Loss of cilia is a separate numbered step (1) with its own downstream consequence, pooling of secretion.",
)

add(
    S1, 218, "recall",
    "Which chain is printed as step 1 on the left of the page 218 flowchart?",
    "Loss of cilia → loss of mucociliary escalator mechanism → pooling of secretion in airway",
    [
        "Loss of cilia → mucus hypersecretion → obstruction of airway",
        "Loss of goblet cells → loss of mucociliary escalator → pooling of secretion",
        "Loss of cartilage → airway collapse → pooling of secretion in airway",
    ],
    "Step 1 reads 'Loss of cilia → loss of micro ciliary escalator mechanism → pooling of secretion in airway', and the pooled secretion loops back into 'microbial colonisation leading to infusion' and inflammation. Cartilage loss is not part of this first step.",
)

add(
    S1, 218, "match",
    "Match each numbered or arrowed step of the page 218 flowchart with its printed text — 1) Step 1 2) Step 2 3) Step 3 4) Arrow back into inflammation … A) Weakening & inflammation of bronchial wall B) Loss of cilia → loss of mucociliary escalator → pooling of secretion C) Microbial colonisation leading to infusion D) Goblet cell hyperplasia → mucus hypersecretion → obstruction of airway",
    "1-B, 2-A, 3-D, 4-C",
    ["1-B, 2-D, 3-A, 4-C", "1-A, 2-B, 3-D, 4-C", "1-C, 2-A, 3-B, 4-D"],
    "The flowchart numbers '1. Loss of cilia → loss of micro ciliary escalator mechanism → pooling of secretion in airway', '2. weakening & inflammation of bronchial wall' and '3. Goblet cell hyperplasia → mucus hypersecretion → Obstruction of airway', and the closed arrow returning to inflammation reads 'microbial colonisation leading to infusion'.",
)


# ---------------------------------------------------------------- Unit 2: p219
add(
    S2, 219, "match",
    "Match each morphological type with the letter used in the page 219 grades figure — 1) Cylindrical/tubular 2) Varicose 3) Saccular/cystic … A) S B) C C) V",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The caption reads 'A normal bronchus (N) compared with the three grades of severity of bronchiectasis: cylindrical (C), varicose (V), and saccular (cystic) (S)'. The letters C, V and S follow the severity order shown.",
)

add(
    S2, 219, "recall",
    "The page 219 note on traction bronchiectasis links it to fibrosis and to a classification. Which statement is printed?",
    "Traction bronchiectasis → fibrosis (restrictive type: classified under ILD)",
    [
        "Traction bronchiectasis → fibrosis (obstructive type: classified under COPD)",
        "Traction bronchiectasis → elastolysis (restrictive type: classified under ILD)",
        "Traction bronchiectasis → atelectasis (mixed type: classified under bronchiectasis)",
    ],
    "The note reads 'Traction bronchiectasis → Fibrosis (Restrictive type : Classified under ILD).' The dilatation is pulled open by surrounding fibrotic contraction, so the physiology is restrictive rather than obstructive.",
)

add(
    S2, 219, "numeric",
    "Which epidemiological details are printed in the page 219 note?",
    "Usually unilateral, most common lobe the left lower lobe, F > M, 50–70 yrs",
    [
        "Usually bilateral, most common lobe the right middle lobe, M > F, 20–40 yrs",
        "Usually unilateral, most common lobe the left upper lobe, M > F, 50–70 yrs",
        "Usually unilateral, most common lobe the left lower lobe, F > M, 20–40 yrs",
    ],
    "The note reads 'Bronchiectasis : usually unilateral (can become bilateral)', 'm/c lobe involved : Left lower lobe', 'F > m' and '50 – 70 yrs'. The right middle lobe is the site of Brock's syndrome on page 220, not the overall commonest lobe.",
)

add(
    S2, 219, "truefalse",
    "TRUE or FALSE about the laterality of bronchiectasis printed on page 219.",
    "True — it is usually unilateral but can become bilateral",
    [
        "False — it is always bilateral by definition",
        "False — it is always unilateral and never becomes bilateral",
        "True — the left lower lobe is spared because of its longer bronchus",
    ],
    "The note says 'usually unilateral (can become bilateral)'. It also names the left lower lobe as the commonest lobe involved, so the left lower lobe is the most, not the least, affected site.",
)

add(
    S2, 219, "match",
    "Match each histological panel caption with its letter on page 219 — 1) Fibrosis and cartilage destruction 2) Mucosal and mucous gland hyperplasia 3) Excessive mucus and exudate 4) Inflammatory cell infiltrate … A) b B) d C) a D) c",
    "1-C, 2-A, 3-D, 4-B",
    ["1-A, 2-C, 3-D, 4-B", "1-C, 2-D, 3-A, 4-B", "1-B, 2-A, 3-D, 4-C"],
    "The four panels are captioned 'a. Fibrosis and cartilage destruction', 'b. mucosal and mucous gland hyperplasia', 'c. Excessive mucus and exudate' and 'd. Inflammatory cell infiltrate'. Cartilage destruction is what allows the airway to dilate irreversibly.",
)

add(
    S2, 219, "scenario",
    "A patient with pulmonary fibrosis has dilated bronchi within the fibrotic zone on CT. How does page 219 classify this?",
    "Traction bronchiectasis, a restrictive type classified under ILD",
    [
        "Traction bronchiectasis, an obstructive type classified under COPD",
        "Pseudobronchiectasis, a reversible post-infective dilatation",
        "Saccular bronchiectasis, a cystic type requiring resection",
    ],
    "Page 219 prints 'Traction bronchiectasis → Fibrosis (Restrictive type : Classified under ILD)'. The dilatation is part of the fibrotic process rather than a primary infective airway disease, which is why it is filed under ILD.",
)

add(
    S2, 219, "recall",
    "Three morphological types of dilatation are shown on page 219. Which list is printed?",
    "Cylindrical/tubular, varicose and cystic",
    [
        "Cylindrical/tubular, saccular and fusiform",
        "Varicose, saccular and beaded",
        "Tubular, moniliform and cystic",
    ],
    "The three labelled drawings read 'Cylindrical / tubular', 'Varicose' and 'Cystic', with the figure caption adding 'saccular (cystic) (S)'. Fusiform, beaded and moniliform are not printed here.",
)


# ---------------------------------------------------------------- Unit 3: p220
add(
    S3, 220, "match",
    "Match each named paediatric syndrome with its printed abnormality — 1) Mounier-Kuhn 2) William Campbell 3) Kartagener's syndrome 4) Young's syndrome … A) Azoospermia causing infertility B) Tracheobronchomegaly C) Primary ciliary dyskinesia D) Absence of cartilage",
    "1-B, 2-D, 3-C, 4-A",
    ["1-D, 2-B, 3-C, 4-A", "1-B, 2-C, 3-D, 4-A", "1-C, 2-D, 3-A, 4-B"],
    "The list reads 'Mounier Kuhn : Tracheobronchomegaly', 'William Campbell : Absence of cartilage', 'Kartagener's syndrome : Primary ciliary dyskinesia' and 'Young's syndrome : Azoospermia → Infertility'. Mounier-Kuhn enlarges the airway while William Campbell weakens it through missing cartilage.",
)

add(
    S3, 220, "recall",
    "Which triad does page 220 print for Kartagener's syndrome?",
    "Bronchiectasis, sinusitis and situs inversus",
    ["Bronchiectasis, sinusitis and azoospermia", "Bronchiectasis, situs inversus and azoospermia", "Sinusitis, situs inversus and yellow nails"],
    "The page reads 'Kartagener's syndrome : Primary ciliary dyskinesia (bronchiectasis, sinusitis & situs inversus)'. Azoospermia belongs to Young's syndrome, which sits immediately below it on the same list.",
)

add(
    S3, 220, "recall",
    "Three conditions are bracketed on page 220 as causing impaired mucociliary clearance. Which three are printed?",
    "Kartagener's syndrome, cystic fibrosis and Young's syndrome",
    [
        "Kartagener's syndrome, cystic fibrosis and yellow nail syndrome",
        "Kartagener's syndrome, Young's syndrome and α1-antitrypsin deficiency",
        "Cystic fibrosis, Young's syndrome and isolated IgA deficiency",
    ],
    "The note reads 'Impaired mucociliary clearance : Kartageners syndrome. Cystic fibrosis. Young's syndrome.' Yellow nail syndrome and α1-antitrypsin deficiency appear in the paediatric list above but not in the clearance bracket.",
)

add(
    S3, 220, "recall",
    "What does page 220 say about isolated IgA deficiency?",
    "It is the most common primary immunodeficiency",
    [
        "It is the least common primary immunodeficiency",
        "It is the most common secondary immunodeficiency",
        "It is the commonest cause of bronchiectasis in adults",
    ],
    "The note reads 'Isolated IgA deficiency : m/c primary immunodeficiency', and the adult list repeats 'Immunodeficiency (Also seen in childhood) : IgA deficiency (m/c)'. It is a predisposing cause, not the commonest overall cause of adult bronchiectasis.",
)

add(
    S3, 220, "fillup",
    "Obliterative bronchiectasis due to infection in childhood is called ______ syndrome on page 220.",
    "McLeod",
    ["Brock", "Kartagener", "Swyer-James"],
    "The note reads 'Obliterative bronchiectasis d/t infection in childhood : mcleod's syndrome.' Brock's syndrome, printed lower on the same page, is a different entity — secondary lymphadenopathy causing right middle lobe bronchiectasis.",
)

add(
    S3, 220, "numeric",
    "The adult aetiology list gives two percentages. Which pair is printed?",
    "Idiopathic 30%, post-infection mostly TB 40%",
    [
        "Idiopathic 40%, post-infection mostly TB 30%",
        "Idiopathic 30%, post-infection mostly pertussis 40%",
        "Idiopathic 60%, post-infection mostly TB 20%",
    ],
    "The adult list reads 'Idiopathic : 30%' and 'Post-infection : mostly TB (40%)', with mechanical obstruction, immunodeficiency and autoimmune causes below them. TB dominates the adult post-infective group even though pertussis and measles dominate the paediatric one.",
)

add(
    S3, 220, "scenario",
    "A patient with right middle lobe bronchiectasis is found to have enlarged hilar nodes compressing the lobar bronchus. Which eponym does page 220 print?",
    "Brock's syndrome — secondary lymphadenopathy causing right middle lobe bronchiectasis",
    [
        "McLeod's syndrome — obliterative bronchiectasis after childhood infection",
        "Mounier-Kuhn syndrome — tracheobronchomegaly",
        "William Campbell syndrome — absence of cartilage",
    ],
    "The adult mechanical-obstruction line reads 'Brock's syndrome : Secondary lymphadenopathy → Right middle lobe bronchiectasis'. The obstruction is extrinsic compression, not a primary airway wall defect.",
)

add(
    S3, 220, "oddoneout",
    "Pick the ODD ONE OUT — three of these appear in the paediatric aetiology list of page 220, one does not:",
    "Sjögren syndrome",
    ["Yellow nail syndrome", "α1-antitrypsin deficiency", "Cystic fibrosis"],
    "The paediatric list contains pertussis/measles, the syndromes, cystic fibrosis, yellow nail syndrome and α1-antitrypsin deficiency. Sjögren syndrome is the autoimmune entry in the ADULT list at the foot of the page.",
)


# ---------------------------------------------------------------- Unit 4: p221
add(
    S4, 221, "recall",
    "Which description of sputum is printed under the symptoms on page 221?",
    "Copious, foul smelling, three layered (mucus, mucopurulent, pus) with early morning exacerbation",
    [
        "Scanty, odourless, two layered (mucus, pus) with evening exacerbation",
        "Copious, foul smelling, three layered (mucus, mucopurulent, pus) with evening exacerbation",
        "Copious, odourless, four layered (mucus, mucopurulent, pus, blood) with early morning exacerbation",
    ],
    "The sputum sub-list reads 'Copius', 'Foul smelling', '3 layered : mucus, mucopurulent, pus' and 'early morning exacerbation'. The layering reflects the settling of different densities of secretions overnight.",
)

add(
    S4, 221, "recall",
    "How does page 221 explain haemoptysis in bronchiectasis?",
    "Due to rupture of a thin walled vein on the bronchial wall",
    [
        "Due to rupture of a thin walled artery on the bronchial wall",
        "Due to erosion of granulation tissue into the pulmonary artery",
        "Due to bronchial artery hypertrophy from chronic inflammation",
    ],
    "The line reads 'Hemoptysis : d/t rupture of thin walled vein on bronchial wall.' The vessel named is a vein, not an artery or granulation tissue.",
)

add(
    S4, 221, "recall",
    "Which auscultatory findings are printed, and in which type is clubbing described?",
    "Early and mid inspiratory coarse crackles with diffuse rhonchi; clubbing in children, seen in the cystic type",
    [
        "Late inspiratory fine crackles with a pleural rub; clubbing in adults, seen in the varicose type",
        "Early and mid inspiratory coarse crackles with diffuse rhonchi; clubbing in adults, seen in the cylindrical type",
        "Expiratory wheeze with diffuse rhonchi; clubbing in children, seen in the varicose type",
    ],
    "The findings read 'Clubbing in children (seen in cystic type)', then 'Early and mid inspiratory coarse crackles' and 'Diffuse rhonchi'. Coarse early-mid inspiratory crackles differ from the fine bibasal inspiratory crackles of fibrosis.",
)

add(
    S4, 221, "recall",
    "The page 221 note ties allergic bronchopulmonary aspergillosis to a specific bronchiectasis pattern. Which description is printed?",
    "Central, proximal, upper lobe bronchiectasis (usually b/l), which can go with interstitial lung disease",
    [
        "Peripheral, distal, lower lobe bronchiectasis (usually unilateral), which can go with COPD",
        "Central, proximal, lower lobe bronchiectasis (usually b/l), which can go with emphysema",
        "Central, distal, upper lobe bronchiectasis (usually unilateral), which can go with asthma only",
    ],
    "The note reads 'Allergic bronchopulmonary aspergillius : Central, proximal, upperlobe bronchiectasis (usually b/l); Can go with interstitial lung disease (ILD).' The central-proximal distribution follows the larger airways colonised by Aspergillus.",
)

add(
    S4, 221, "fillup",
    "The clinical-features section advises: 'always rule out bronchiectasis in recurrent ______.'",
    "Pneumonia",
    ["Asthma", "Sinusitis", "Haemoptysis"],
    "The line reads 'Acute exacerbation d/t infection : Always rule out bronchiectasis in recurrent pneumonia.' Recurrent infection in the same segment is the clinical clue to an underlying dilated, poorly cleared airway.",
)

add(
    S4, 221, "match",
    "Match each plain-film sign with its printed description — 1) Tram track sign 2) Bunch of grape appearance 3) Finger in glove appearance … A) Due to mucus inside B) Dilated airways with lack of tapering C) Clustered cystic spaces",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The film is captioned 'Tram track sign (Dilated airways with lack of tapering)', 'Bunch of grape appearance' and 'Finger in glove appearance (d/t mucus inside)'. Loss of tapering is the radiographic signature of the dilated airway.",
)

add(
    S4, 221, "recall",
    "Which three criteria for the CT diagnosis are printed under 'Volumetric multidetector helical CT scan : IOC'?",
    "Airway dilatation (1–1.5 times the adjacent vessels), lack of bronchial tapering, and tree-in-bud opacity (non-specific) from endobronchial obstruction giving nodules plus signet ring",
    [
        "Airway dilatation (2–3 times the adjacent vessels), preserved bronchial tapering, and tree-in-bud opacity",
        "Airway dilatation (1–1.5 times the adjacent vessels), lack of bronchial tapering, and honeycombing with traction Bronchiectasis",
        "Airway narrowing (less than the adjacent vessels), lack of bronchial tapering, and tree-in-bud opacity",
    ],
    "The three CT criteria read '1. Airway dilatation (1–1.5 times than adjacent vessels). 2. Lack of bronchial tapering. 3. Tree in bud opacity (Non-specific) : endobronchial obstruction → nodules + signet ring.' The ratio compares the airway with its adjacent vessel, not with a fixed diameter.",
)


add(
    S4, 221, "scenario",
    "A young asthmatic with poorly controlled disease has central, proximal, upper lobe bronchiectasis on CT, and a background of interstitial lung disease is suspected. Which page 221 note applies?",
    "Allergic bronchopulmonary aspergillosis — central, proximal, upper lobe bronchiectasis (usually b/l), which can go with ILD",
    [
        "Sicca bronchiectasis — central, proximal, upper lobe bronchiectasis seen with haemoptysis and cough",
        "Brock's syndrome — central, proximal, upper lobe bronchiectasis from secondary lymphadenopathy",
        "Traction bronchiectasis — central, proximal, upper lobe bronchiectasis classified under ILD",
    ],
    "The note reads 'Allergic bronchopulmonary aspergillius : Central, proximal, upperlobe bronchiectasis (usually b/l)' and 'Can go with interstitial lung disease (ILD)'. Sicca bronchiectasis, printed just above, is the TB-associated pattern with haemoptysis and cough.",
)


add(
    S4, 221, "fillup",
    "The chest X-ray in bronchiectasis is introduced on page 221 with a single qualifier: 'X-Ray : ______ sensitivity'.",
    "Low",
    ["High", "Intermediate", "Variable"],
    "The line reads 'X-Ray : Low sensitivity', which is why the volumetric multidetector helical CT scan is designated the IOC on the same page despite the classic tram track, bunch of grape and finger-in-glove signs.",
)


# ---------------------------------------------------------------- Unit 5: p222
add(
    S5, 222, "match",
    "Match each complication with its printed qualifier — 1) Massive haemoptysis 2) Empyema 3) Secondary amyloidosis 4) Lung abscess … A) With bronchopleural fistula B) AA type C) Especially in dry bronchiectasis D) Listed without a qualifier",
    "1-C, 2-A, 3-B, 4-D",
    ["1-C, 2-B, 3-A, 4-D", "1-D, 2-A, 3-B, 4-C", "1-A, 2-C, 3-B, 4-D"],
    "The complication list reads '1. Cor pulmonale. 2. massive hemoptysis : especially in dry bronchiectasis. 3. Empyema with bronchopleural fistula. 4. Secondary Amyloidosis (AA). 5. Lung Abscess.' Dry bronchiectasis is the variant that bleeds rather than expectorates.",
)

add(
    S5, 222, "recall",
    "Cor pulmonale is split on page 222 into acute and chronic types. Which two causes are printed?",
    "Acute: most common cause thromboembolism; chronic: due to lung parenchymal disease such as ILD, chronic bronchitis and bronchiectasis",
    [
        "Acute: most common cause lung parenchymal disease; chronic: due to thromboembolism",
        "Acute: most common cause pneumonia; chronic: due to ILD, chronic bronchitis and bronchiectasis",
        "Acute: most common cause thromboembolism; chronic: due to left heart disease",
    ],
    "The note reads 'Cor pulmonale : RV dilatation/hypertrophy +/− RV Failure' and then 'Types → Acute (m/c cause : thromboembolism)' and '→ Chronic (d/t lung parenchymal disease : ILD, chronic bronchitis, bronchiectasis)'. Acute cor pulmonale is embolic; chronic is parenchymal.",
)

add(
    S5, 222, "numeric",
    "Which concentration of nebulised hypertonic saline is printed under airway clearance on page 222?",
    "7% hypertonic saline",
    ["3% hypertonic saline", "0.9% normal saline", "7% sodium bicarbonate"],
    "The airway-clearance line reads 'Nebulized 7% hypertonic saline, Steam inhalation, flutter valves', together with postural drainage. Hypertonic saline is used to osmotically draw water into secretions and make them easier to clear.",
)

add(
    S5, 222, "match",
    "Match each therapy with the role printed against it on page 222 — 1) Recombinant human DNase 2) Nebulized gentamycin 3) Nebulized 7% hypertonic saline … A) As prophylaxis B) Airway clearance agent C) Listed first among CF-associated therapies",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-C, 2-B, 3-A"],
    "Under 'CF associated bronchiectasis' the page prints 'Recombinant human DNase' then 'Nebulized gentamycin as prophylaxis'. The 7% hypertonic saline belongs to the mainstay airway-clearance list above. The DNase thins DNA-rich secretions while the aminoglycoside suppresses chronic Pseudomonas.",
)

add(
    S5, 222, "numeric",
    "Macrolides have two roles in the page 222 treatment block. Which statement is printed?",
    "They reach effective concentration within lung and bronchial mucosa, and have an immunomodulatory action recommended for 6–9 months",
    [
        "They reach effective concentration within lung and bronchial mucosa, and have an immunomodulatory action recommended for 3–6 months",
        "They do not reach effective lung concentrations, but have an immunomodulatory action recommended for 6–9 months",
        "They reach effective concentration only in serum, and have an immunomodulatory action recommended for 6–9 months",
    ],
    "The antibiotic block reads 'macrolides & penicillin (Beta-lactams) : Reach effective concentration within lung and bronchial mucosa' and 'macrolides : immunomodulatory action - recommended for 6–9 months'. Both the penetration and the 6–9 month duration are printed.",
)

add(
    S5, 222, "recall",
    "Which organism hierarchy is printed in the closing note on page 222?",
    "Pseudomonas >> H. influenzae > S. pneumoniae",
    [
        "H. influenzae >> Pseudomonas > S. pneumoniae",
        "S. pneumoniae >> H. influenzae > Pseudomonas",
        "Pseudomonas > S. pneumoniae >> H. influenzae",
    ],
    "The note reads 'Organism infecting & weakening bronchial wall → Pseudomonas >> H. influenzae > S. pneumoniae.' The double arrow marks Pseudomonas as the dominant organism in damaged airways.",
)

add(
    S5, 222, "scenario",
    "A patient with long-standing bronchiectasis develops nephrotic-range proteinuria and a tissue biopsy shows AA deposits. Which page 222 complication does this represent?",
    "Secondary amyloidosis (AA), the fourth listed complication",
    [
        "Secondary amyloidosis (AL), the fourth listed complication",
        "Cor pulmonale, the first listed complication",
        "Empyema with bronchopleural fistula, the third listed complication",
    ],
    "The complication list includes '4. Secondary Amyloidosis (AA)'. Chronic infection drives serum amyloid A production, which is why the type is AA rather than AL.",
)

add(
    S5, 222, "management",
    "Which surgical and antibiotic strategy is printed for bronchiectasis on page 222?",
    "Localized resection for localized bronchiectasis, and antibiotics chosen because macrolides and beta-lactams reach effective concentrations in lung and bronchial mucosa",
    [
        "Bilateral resection for bilateral bronchiectasis, and antibiotics chosen because aminoglycosides reach effective concentrations in lung and bronchial mucosa",
        "Localized resection for diffuse bronchiectasis, and inhaled antibiotics as the only route",
        "Bilateral lung transplant for localized disease, and oral antibiotics avoided because they do not reach the airway",
    ],
    "The block reads 'Surgery : localized resection for localized bronchiectasis' and, under antibiotics, 'macrolides & penicillin (Beta-lactams) : Reach effective concentration within lung and bronchial mucosa'. Surgery is offered only when the disease is localised enough to remove completely.",
)


GUIDES = {
    S1: (
        "Definition (Irreversible Dilatation Plus Obliterative Bronchiolar Fibrosis), Pseudobronchiectasis, the Obstructive-Disease List, Pathogenesis Flowchart and the Normal-vs-Bronchiectasis Diagram",
        "Bronchiectasis (p218) is abnormal and irreversible dilatation of bronchi — initially medium sized, later the entire bronchial tree — plus obliterative fibrosis of bronchioles, producing obstructive lung disease that can have a restrictive component. Pseudobronchiectasis is the reversible dilatation that follows influenza or COVID.\n"
        "It is listed among the obstructive diseases with COPD (emphysema, bronchitis, small airway disease), bronchial asthma, bronchiolitis and cystic fibrosis.\n"
        "Pathogenesis: infection (mostly TB)/idiopathic → inflammation → loss of smooth muscle and elastic tissue in bronchi (bronchi and bronchioles both have smooth muscle) → abnormal and irreversible dilatation; the mucus limb runs goblet cell hyperplasia → mucus hypersecretion → airway obstruction, while loss of cilia removes the mucociliary escalator and pools secretions, feeding microbial colonisation and further inflammation. The diagram contrasts a normal bronchus (outer wall, cilia, mucus, mucous gland) with loss of cilia, increased mucus and destruction of the wall.",
    ),
    S2: (
        "Types of Dilatation (Cylindrical/Varicose/Cystic), Traction Bronchiectasis, Lobe/Sex/Age Distribution and the Four Histological Features",
        "Types of dilatation (p219) are cylindrical/tubular, varicose and cystic, drawn against a normal bronchus (N) as grades C, V and S, with a CT showing cystic changes at the upper lobe. Traction bronchiectasis follows fibrosis and is a restrictive type classified under ILD.\n"
        "Distribution: usually unilateral though it can become bilateral, most common lobe the left lower lobe, F > M, age 50–70 years.\n"
        "Histology: fibrosis and cartilage destruction; mucosal and mucous gland hyperplasia; excessive mucus and exudate; inflammatory cell infiltrate.",
    ),
    S3: (
        "Paediatric Aetiology (Post-Infective, Mounier-Kuhn, William Campbell, Kartagener, Young, Yellow Nail, α1-Antitrypsin), Impaired Mucociliary Clearance, McLeod, IgA Deficiency and Adult Aetiology",
        "Paediatric aetiology (p220): post-infective pertussis and measles; syndromes usually cystic in the upper to mid fields — Mounier-Kuhn (tracheobronchomegaly), William Campbell (absence of cartilage), Kartagener's (primary ciliary dyskinesia with bronchiectasis, sinusitis and situs inversus), Young's (azoospermia causing infertility); cystic fibrosis; yellow nail syndrome; α1-antitrypsin deficiency.\n"
        "Impaired mucociliary clearance is bracketed for Kartagener's, cystic fibrosis and Young's syndrome. Obliterative bronchiectasis after childhood infection is McLeod's syndrome, and isolated IgA deficiency is the commonest primary immunodeficiency.\n"
        "Adult causes: idiopathic 30%, post-infection mostly TB 40%, mechanical obstruction such as Brock's syndrome (secondary lymphadenopathy causing right middle lobe bronchiectasis), immunodeficiency (IgA deficiency commonest) and autoimmune disease such as Sjögren syndrome.",
    ),
    S4: (
        "Clinical Features (Three-Layered Sputum, Postural Cough, Haemoptysis Mechanism), Examination Findings, Sicca/ABPA Notes, Plain-Film Signs and the Three CT Criteria",
        "Clinical features (p221): chronic cough with postural variation; copious foul-smelling sputum in three layers — mucus, mucopurulent, pus — with early morning exacerbation; haemoptysis from rupture of a thin-walled vein on the bronchial wall; exacerbations from infection, and bronchiectasis must always be excluded in recurrent pneumonia.\n"
        "Findings: clubbing in children, seen in the cystic type; early and mid inspiratory coarse crackles with diffuse rhonchi. Note sicca bronchiectasis with haemoptysis and cough points to TB, and ABPA gives central, proximal, upper lobe bronchiectasis, usually bilateral, which can accompany ILD.\n"
        "X-ray has low sensitivity but shows the tram track sign (dilated airways with lack of tapering), bunch of grape appearance and finger-in-glove appearance from mucus inside. Volumetric multidetector helical CT is the IOC: airway dilatation 1–1.5 times the adjacent vessels, lack of bronchial tapering, and tree-in-bud opacity (non-specific) from endobronchial obstruction giving nodules plus signet ring.",
    ),
    S5: (
        "Complications (Cor Pulmonale, Massive Haemoptysis, Empyema, Amyloidosis, Abscess), Airway Clearance and CF Therapies, Surgery, Antibiotic Rationale, Macrolide Duration and the Infecting-Organism Hierarchy",
        "Complications (p222): cor pulmonale; massive haemoptysis, especially in dry bronchiectasis; empyema with bronchopleural fistula; secondary amyloidosis (AA); lung abscess. Cor pulmonale is RV dilatation/hypertrophy ± failure, acute from thromboembolism and chronic from parenchymal disease such as ILD, chronic bronchitis and bronchiectasis.\n"
        "Treatment: mainstay is airway clearance with nebulised 7% hypertonic saline, steam inhalation, flutter valves and postural drainage; CF-associated disease gets recombinant human DNase and nebulised gentamycin as prophylaxis; surgery is localized resection for localized disease.\n"
        "Antibiotics: macrolides and penicillin (beta-lactams) reach effective concentration within lung and bronchial mucosa, and macrolides have an immunomodulatory action recommended for 6–9 months. The organism hierarchy that infects and weakens the bronchial wall is Pseudomonas >> H. influenzae > S. pneumoniae.",
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
