#!/usr/bin/env python3
"""Generate Chapter 39: Interstitial Lung Disease (Book p236–242).

Every question is anchored to a printed line, table cell, brace or figure caption of
uploads/02.pdf sheets 119–125 (Book pages 236–242), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 39
TITLE = "Interstitial Lung Disease"
PAGES = "236-242"

S1 = "Interstitium and Its Types, Lung Parenchyma, TGF-β/PDGF Fibrosis, ILD Classification and the Seven Idiopathic Interstitial Pneumonias"
S2 = "Autoimmune and Miscellaneous ILD (Occupational Lobes, Vasculitis, Inherited, Drug-Induced, LCH, LAM) with the UIP/NSIP/COP/LIP Important Points"
S3 = "Clinical Features of ILD: Cardinal Symptoms, the Crackles-and-Clubbing Table versus Bronchiectasis, Skin Signs, Pulmonary HTN Prognosis and CXR"
S4 = "PFT in Initial versus Advanced ILD, HRCT as Investigation of Choice and the UIP Pattern with Its Image Captions and New Antifibrotic Drugs"
S5 = "NSIP Pattern and Its Treatment, Drugs Causing ILD, COP/BOOP with Halo Signs, and Cysts on HRCT (LAM, LCH, LIP)"
S6 = "HRCT Finding–Disease Table, Nodular Shadows and Tree-in-Bud Notes with the Mosaic Attenuation and Lower-Lobe Infiltrate Captions"
S7 = "Conditions with Upper-Lobe ILD, the LL Reticular Caption in IPF, and Pulmonary Alveolar Proteinosis (PAP)"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(39000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(39100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p236
add(
    S1, 236, "recall",
    "Which interstitium scheme opens the chapter on page 236?",
    "Interstitium is connective tissue that holds the lungs together; alveolar interstitium splits into subpleural and lobar, vascular interstitium surrounds vessels, and axial interstitium connects lung to chest wall",
    [
        "Interstitium is connective tissue that holds the lungs together; alveolar interstitium surrounds vessels, vascular interstitium splits into subpleural and lobar, and axial interstitium connects lung to chest wall",
        "Interstitium is the air space within alveoli; alveolar interstitium splits into subpleural and lobar, vascular interstitium surrounds vessels, and axial interstitium connects lung to chest wall",
        "Interstitium is connective tissue that holds the lungs together; alveolar interstitium splits into subpleural and segmental, vascular interstitium surrounds airways, and axial interstitium connects the two lungs",
    ],
    "The page reads 'Interstitium: Connective tissue that holds the lungs together', with types 'Alveolar → Subpleural, Lobar', 'Vascular: Surrounds vessels' and 'Axial: Connects lung to chest wall'.",
)

add(
    S1, 236, "fillup",
    "Complete the printed definition: Lung parenchyma = Alveoli + alveolar interstitium + ______ interstitium.",
    "vascular",
    ["axial", "subpleural", "lobar"],
    "The line reads 'Lung parenchyma: Alveoli + alveolar interstitium + vascular interstitium'. The axial interstitium, defined just above as connecting lung to chest wall, is deliberately left out of the parenchyma.",
)

add(
    S1, 236, "recall",
    "How is interstitial lung disease itself defined and driven on page 236?",
    "It is 'Diffuse parenchymal lung fibrosis', a TGF-β > PDGF mediated parenchymal fibrosis, with TGF-β boxed as the most potent pathogenic fibrogenic cytokine",
    [
        "It is 'Diffuse parenchymal lung fibrosis', a PDGF > TGF-β mediated parenchymal fibrosis, with PDGF boxed as the most potent pathogenic fibrogenic cytokine",
        "It is 'Focal parenchymal lung fibrosis', a TGF-β > PDGF mediated parenchymal fibrosis, with TGF-β boxed as the most potent pathogenic fibrogenic cytokine",
        "It is 'Diffuse parenchymal lung inflammation', a TGF-β > VEGF mediated parenchymal fibrosis, with VEGF boxed as the most potent pathogenic fibrogenic cytokine",
    ],
    "The bullets read 'Diffuse parenchymal lung fibrosis' and 'TGF-β > PDGF mediated parenchymal fibrosis', and the side box states 'Note: TGF-β most potent pathogenic fibrogenic cytokine.' The inequality runs TGF-β first.",
)

add(
    S1, 236, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed arms of the page 236 ILD classification tree, one is not:",
    "Pulmonary alveolar proteinosis",
    [
        "Idiopathic interstitial pneumonia (m/c)",
        "Hypersensitivity pneumonitis",
        "Sarcoidosis",
    ],
    "The tree reads 'ILD → Idiopathic Interstitial pneumonia (m/c), Autoimmune ILD, Hypersensitivity pneumonitis, Sarcoidosis, miscellaneous'. PAP is not an arm of this tree; it appears separately at the end of the chapter on page 242.",
)

add(
    S1, 236, "match",
    "Match each idiopathic interstitial pneumonia with its printed rank on page 236 — 1) Idiopathic pulmonary fibrosis / usual interstitial pneumonia 2) Idiopathic nonspecific interstitial pneumonia 3) Cryptogenic organizing pneumonia … A) 3rd most common B) Most common C) 2nd most common",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The numbered list reads '1. Idiopathic pulmonary fibrosis/usual interstitial pneumonia (UIP): m/c', '2. Idiopathic nonspecific interstitial pneumonia (NSIP): 2nd m/c' and '3. Cryptogenic organizing pneumonia (COP): 3rd m/c'.",
)

add(
    S1, 236, "truefalse",
    "TRUE or FALSE about the smoking brace in the idiopathic interstitial pneumonia list on page 236.",
    "True — respiratory bronchiolitis interstitial lung disease (RB-ILD) and desquamative interstitial pneumonia (DIP) are bracketed together as 'Associated with smoking'",
    [
        "False — only desquamative interstitial pneumonia is bracketed as associated with smoking",
        "False — the brace covers acute interstitial pneumonia and lymphocytic interstitial pneumonia",
        "True — all seven idiopathic interstitial pneumonias are bracketed as associated with smoking",
    ],
    "Items 4 and 5, 'Respiratory bronchiolitis interstitial lung disease (RB-ILD)' and 'Desquamative interstitial pneumonia (DIP)', share one brace labelled 'Associated with smoking'. The brace covers exactly these two.",
)

add(
    S1, 236, "recall",
    "Which three bullets are printed under acute interstitial pneumonia, the sixth idiopathic interstitial pneumonia?",
    "ARDS associated with diffuse alveolar damage; seen following COVID infection and viral infections; very poor prognosis",
    [
        "ARDS associated with diffuse alveolar damage; seen following bacterial sepsis; very poor prognosis",
        "COP associated with diffuse alveolar damage; seen following COVID infection and viral infections; good prognosis",
        "ARDS associated with diffuse alveolar damage; seen following COVID infection and viral infections; prognosis better than UIP",
    ],
    "Item 6 reads 'Acute interstitial pneumonia' with bullets 'ARDS associated with diffuse alveolar damage', 'Seen following COVID infection, viral infections' and 'very poor prognosis', before item 7, lymphocytic interstitial pneumonia (LIP).",
)

add(
    S1, 236, "scenario",
    "Weeks after a COVID infection a patient develops an ARDS picture, and the team discusses diffuse alveolar damage with a very poor prognosis. Which entry in the page 236 list does this reproduce?",
    "Acute interstitial pneumonia",
    [
        "Cryptogenic organizing pneumonia",
        "Lymphocytic interstitial pneumonia",
        "Desquamative interstitial pneumonia",
    ],
    "Only acute interstitial pneumonia carries the bullets 'ARDS associated with diffuse alveolar damage', 'Seen following COVID infection, viral infections' and 'very poor prognosis'. COP is the 3rd most common type and DIP sits in the smoking brace.",
)


# ---------------------------------------------------------------- Unit 2: p237
add(
    S2, 237, "recall",
    "Which six conditions are listed as prone to develop autoimmune ILD on page 237?",
    "Rheumatoid arthritis, diffuse systemic sclerosis, polymyositis/dermatomyositis (inflammatory muscle disease), mixed connective tissue disease (MCTD), Sjogren's syndrome and ankylosing spondylitis",
    [
        "Rheumatoid arthritis, limited systemic sclerosis, polymyositis/dermatomyositis (inflammatory muscle disease), mixed connective tissue disease (MCTD), Sjogren's syndrome and ankylosing spondylitis",
        "Rheumatoid arthritis, diffuse systemic sclerosis, polymyositis/dermatomyositis (inflammatory muscle disease), systemic lupus erythematosus, Sjogren's syndrome and ankylosing spondylitis",
        "Rheumatoid arthritis, diffuse systemic sclerosis, inclusion body myositis, mixed connective tissue disease (MCTD), Sjogren's syndrome and reactive arthritis",
    ],
    "Under 'Conditions prone to develop ILD' the page lists rheumatoid arthritis, diffuse systemic sclerosis, polymyositis/dermatomyositis as inflammatory muscle disease, MCTD, Sjogren's syndrome and ankylosing spondylitis. The sclerosis entry is the diffuse form.",
)

add(
    S2, 237, "match",
    "Match each occupational ILD with the lobe printed against it on page 237 — 1) Asbestosis 2) Silicosis 3) Berylliosis 4) Coal-worker's pneumoconiosis … A) Upper lobe ILD B) Lower lobe ILD C) Upper lobe ILD (same brace) D) Upper lobe ILD (same brace)",
    "1-B, 2-A, 3-C, 4-D",
    ["1-A, 2-B, 3-C, 4-D", "1-B, 2-C, 3-D, 4-A", "1-C, 2-A, 3-B, 4-D"],
    "The miscellaneous list reads 'Asbestosis (Lower lobe ILD)' on its own, while silicosis, berylliosis and coal-worker's pneumoconiosis share one brace labelled 'Upper lobe ILD'. Asbestosis is the lone lower-lobe entry.",
)

add(
    S2, 237, "recall",
    "Which vasculitis-related, inherited and drug-induced entries complete the miscellaneous ILD list on page 237?",
    "Vasculitis-related: eosinophilic granulomatosis polyangiitis (EGPA)/Churg-Strauss syndrome; inherited: neurofibromatosis and tuberous sclerosis; drug-induced: bleomycin",
    [
        "Vasculitis-related: granulomatosis with polyangiitis (GPA); inherited: neurofibromatosis and tuberous sclerosis; drug-induced: bleomycin",
        "Vasculitis-related: eosinophilic granulomatosis polyangiitis (EGPA)/Churg-Strauss syndrome; inherited: neurofibromatosis and cystic fibrosis; drug-induced: amiodarone",
        "Vasculitis-related: eosinophilic granulomatosis polyangiitis (EGPA)/Churg-Strauss syndrome; inherited: tuberous sclerosis only; drug-induced: bleomycin",
    ],
    "Items 2 to 4 read 'vasculitis-related ILD — Eosinophilic granulomatosis polyangiitis (EGPA)/Churg-Strauss syndrome', 'Inherited forms of ILD — Neurofibromatosis, Tuberous sclerosis' and 'Drug-induced forms of ILD: Bleomycin'.",
)

add(
    S2, 237, "fillup",
    "In the miscellaneous list, Langerhan's cell histiocytosis (LCH), as printed, carries the arrow annotation 'Associated with ______', and the final miscellaneous entry is lymphangio myomatosis (LAM).",
    "smoking",
    ["asbestos", "tuberous sclerosis", "viral infection"],
    "Item 5 reads 'Langerhan's cell histiocytosis (LCH) → Associated with smoking' (printed spelling 'Langerhan's'), and item 6 is 'Lymphangio myomatosis (LAM)', printed as two words. Tuberous sclerosis is an inherited-ILD entry two items above, not the LCH annotation.",
)

add(
    S2, 237, "recall",
    "Which 'Important points' are printed for UIP/IPF on page 237?",
    "Idiopathic UIP/IPF is the most common; rheumatoid arthritis ILD occurs in males > females aged 50–70 years and is associated with smoking",
    [
        "Idiopathic UIP/IPF is the most common; rheumatoid arthritis ILD occurs in females > males aged 30–40 years and is associated with smoking",
        "Idiopathic UIP/IPF is the second most common; rheumatoid arthritis ILD occurs in males > females aged 50–70 years and is associated with smoking",
        "Idiopathic UIP/IPF is the most common; rheumatoid arthritis ILD occurs in males > females aged 50–70 years with no smoking association printed",
    ],
    "The box reads 'UIP/IPF: Idiopathic: m/c' and 'Rheumatoid arthritis ILD — males > females, 50–70 years, Associated with smoking'. The demographic triad belongs to the RA entry, not to idiopathic disease.",
)

add(
    S2, 237, "match",
    "Match each pattern with its page 237 'Important points' association — 1) NSIP 2) COP 3) LIP … A) Sjogren syndrome and HIV B) Young females with a subacute restrictive process, associated with drugs and connective tissue disease C) Most common pattern in inflammatory muscle disease (polymyositis and dermatomyositis)",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "NSIP is described as young females with a subacute restrictive process and associations of drug and connective tissue disease; COP is 'm/c in inflammatory muscle disease' branching to polymyositis and dermatomyositis; LIP lists Sjogren syndrome and HIV.",
)

add(
    S2, 237, "truefalse",
    "TRUE or FALSE about the closing Note on page 237.",
    "True — the most common pattern of ILD is UIP in rheumatoid arthritis and NSIP in other conditions",
    [
        "False — the most common pattern is NSIP in rheumatoid arthritis and UIP in other conditions",
        "False — the Note names COP as the most common pattern in rheumatoid arthritis",
        "True — the most common pattern is UIP in every condition including the non-RA group",
    ],
    "The Note reads 'm/c pattern of ILD → RA: UIP; Other conditions: NSIP'. Rheumatoid arthritis is the exception that keeps the UIP pattern.",
)

add(
    S2, 237, "scenario",
    "A young woman with a connective tissue disease develops a subacute restrictive lung process. Using only the page 237 boxes, which pattern and which two associations fit her best?",
    "NSIP — young females, subacute restrictive process, associated with drugs and connective tissue disease",
    [
        "UIP — males over 50 years, associated with smoking",
        "COP — most common in inflammatory muscle disease such as dermatomyositis",
        "LIP — associated with Sjogren syndrome and HIV",
    ],
    "The NSIP box reads 'Young females', 'Subacute restrictive process' and 'Associations → Drug, Connective tissue disease', matching all three elements of the vignette.",
)


# ---------------------------------------------------------------- Unit 3: p238
add(
    S3, 238, "recall",
    "Which two cardinal symptoms of ILD are printed on page 238, and what happens to them diagnostically?",
    "Dry non-productive cough and dyspnea on exertion — together misdiagnosed as bronchitis",
    [
        "Productive cough and dyspnea at rest — together misdiagnosed as bronchitis",
        "Dry non-productive cough and dyspnea on exertion — together misdiagnosed as bronchial Asthma",
        "Dry non-productive cough and hemoptysis — together misdiagnosed as bronchitis",
    ],
    "The Symptoms block reads '2 cardinal symptoms → Dry non-productive cough, Dyspnea on exertion' with a brace to 'misdiagnosed as bronchitis'. Hemoptysis appears lower down as a rare additional symptom.",
)

add(
    S3, 238, "match",
    "Match each additional symptom on page 238 with the condition printed against it — 1) Fever with arthralgia 2) Wheeze 3) Pleuritic pain 4) Hemoptysis … A) Asbestosis B) Sarcoidosis C) Rare, with no single condition attached D) Specific to bronchiectasis, ABPA and hypersensitivity pneumonitis",
    "1-B, 2-D, 3-A, 4-C",
    ["1-D, 2-B, 3-A, 4-C", "1-B, 2-D, 3-C, 4-A", "1-B, 2-A, 3-D, 4-C"],
    "The list reads 'Fever + arthralgia (Sarcoidosis)', 'Wheeze: Specific to → Bronchiectasis, ABPA, Hypersensitivity pneumonitis', 'Pleuritic pain (Asbestosis)' and 'Hemoptysis (Rare)'.",
)

add(
    S3, 238, "scenario",
    "On auscultation a patient has bilateral bibasal fine 'velcro' crackles, timed end to early expiratory as printed, with no variation on coughing or posture change. Which column of the page 238 table is this, and what does the other column show?",
    "ILD — the bronchiectasis column instead shows unilateral, coarse, early to mid inspiratory crackles",
    [
        "Bronchiectasis — the ILD column instead shows unilateral, coarse, early to mid inspiratory crackles",
        "ILD — the bronchiectasis column instead shows bilateral bibasal, fine crackles with variation on coughing",
        "Bronchiectasis — the ILD column instead shows absent crackles with clubbing only",
    ],
    "The table gives ILD crackles as bilateral bibasal in site, 'End to early expiratory' in timing (as printed on p238), fine 'velcro crackles' in type and 'Absent' variation with cough/posture, against unilateral, early to mid inspiratory, coarse crackles in bronchiectasis, whose variation cell is left blank.",
)

add(
    S3, 238, "recall",
    "What does the clubbing row of the page 238 table state for each disease?",
    "Clubbing is present (+) in ILD and absent (−) in bronchiectasis, with the single exception of childhood cystic bronchiectasis",
    [
        "Clubbing is absent in ILD and present in bronchiectasis, with the single exception of childhood cystic bronchiectasis",
        "Clubbing is present (+) in ILD and absent (−) in bronchiectasis, with the single exception of adult cystic bronchiectasis",
        "Clubbing is present in both diseases, but coarser in bronchiectasis",
    ],
    "The row reads 'Clubbing: ILD +' versus bronchiectasis '− (Exception: Childhood cystic bronchiectasis)'. The exception is specified as childhood disease.",
)

add(
    S3, 238, "oddoneout",
    "Pick the ODD ONE OUT — three of these examination signs are printed under ILD on page 238 with their parent conditions, one pairing is not:",
    "Erythema nodosum (neurofibromatosis)",
    [
        "Cafe-au-lait spots (neurofibromatosis)",
        "Erythema nodosum (sarcoidosis)",
        "Raynaud's phenomenon (scleroderma)",
    ],
    "The three bullets read 'Cafe-au-lait spots (Neurofibromatosis)', 'Erythema nodosum (Sarcoidosis)' and 'Raynaud's phenomenon (Scleroderma)'. Attaching erythema nodosum to neurofibromatosis swaps the printed parent condition.",
)

add(
    S3, 238, "recall",
    "Which chain closes the signs section on page 238, and why does it matter?",
    "Hypoxia → pulmonary vasoconstriction → pulmonary HTN, bracketed as the most significant factor for prognosis of ILD",
    [
        "Hypoxia → pulmonary vasodilatation → pulmonary HTN, bracketed as the most significant factor for prognosis of ILD",
        "Hypercapnia → pulmonary vasoconstriction → pulmonary HTN, bracketed as the most common presenting feature of ILD",
        "Hypoxia → pulmonary vasoconstriction → pulmonary HTN, bracketed as the most significant factor for diagnosis of ILD",
    ],
    "The bullet reads 'Hypoxia → Pulmonary vasoconstriction → Pulmonary HTN (most significant factor for prognosis of ILD)'. The pulmonary vascular response to hypoxia is constriction, in line with the boxed note on page 214.",
)

add(
    S3, 238, "match",
    "Match each condition that 'presents directly with pulmonary HTN' with the test printed to rule it out — 1) Obstructive sleep apnea syndrome 2) ILD … A) CT scan B) Sleep study",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "The Note reads 'Conditions that present directly with pulmonary HTN: 1. Obstructive sleep apnea syndrome (R/o with sleep study). 2. ILD (R/o with CT scan).' Each condition carries its own exclusion test.",
)

add(
    S3, 238, "fillup",
    "Under Investigations, the CXR in ILD shows bilateral bibasal subpleural ______ infiltrates.",
    "reticular / reticulo-nodular",
    ["nodular / cavitating", "alveolar / consolidative", "miliary / interstitial-nodular"],
    "The CXR line reads 'Bilateral bibasal subpleural reticular/ reticulo-nodular infiltrates', shown on the chest film beside it. The distribution words bibasal and subpleural are given in the stem; the pattern words are reticular and reticulo-nodular.",
)


# ---------------------------------------------------------------- Unit 4: p239
add(
    S4, 239, "match",
    "Match each PFT stage on page 239 with its printed findings — 1) Initial phase 2) Advanced disease … A) Type 3 respiration failure with ventilation impaired, FVC reduced three arrows down, FEV1/FVC normal or raised B) Type 1 respiratory failure with only diffusion impaired, impaired DLCO with normal FEV1 and FVC",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "The table reads 'Initial phase: Type 1 respiratory failure (Only diffusion impaired) — Impaired DLCO, Normal FEV1, FVC' and 'Advanced disease: Type 3 respiration failure (Ventilation impaired) — ↓↓↓ FVC, (N)/↑ FEV1/FVC' ('respiration' as printed).",
)

add(
    S4, 239, "recall",
    "What status and purpose are given to HRCT at the head of the HRCT section?",
    "Investigation of choice, used to determine pattern and prognosis",
    [
        "Investigation of choice, used to determine etiology and infectivity",
        "Gold standard, used to replace lung biopsy in every pattern",
        "Screening test, used only when the CXR is normal",
    ],
    "The line reads 'Investigation of choice: To determine pattern and prognosis.' HRCT sorts the UIP and NSIP patterns that follow on pages 239–240 and thereby the outlook.",
)

add(
    S4, 239, "recall",
    "Which two HRCT shadows are bracketed as 'suggestive of UIP' on page 239, with their parenthetical meanings?",
    "Linear shadows (intralobular septal thickening) and reticular shadows (net of linear opacities)",
    [
        "Linear shadows (interlobular septal thickening) and nodular shadows (net of linear opacities)",
        "Reticular shadows (intralobular septal thickening) and linear shadows (net of linear opacities)",
        "Linear shadows (intralobular septal thickening) and ground-glass shadows (net of linear opacities)",
    ],
    "The first two UIP bullets read 'Linear shadows (Intralobular septal thickening)' and 'Reticular shadows (Net of linear opacities)', sharing the small brace 'suggestive of UIP'. Nodules and ground glass are instead listed as absent in UIP.",
)

add(
    S4, 239, "recall",
    "Which subpleural, basal predominant features complete the 'Specific for UIP' brace?",
    "Honeycombing (small, polyhedral cystic spaces), loss of lung architecture and traction bronchiectasis",
    [
        "Honeycombing (large, round cystic spaces), loss of lung architecture and cylindrical bronchiectasis",
        "Honeycombing (small, polyhedral cystic spaces), preserved lung architecture and traction bronchiectasis",
        "Consolidation, loss of lung architecture and traction bronchiectasis",
    ],
    "The third UIP bullet, 'Subpleural, basal predominant', arrows to 'Honeycombing (Small, polyhedral cystic spaces)', 'Loss of lung architecture' and 'Traction bronchiectasis', and the large brace over the whole UIP set is labelled 'Specific for UIP'.",
)

add(
    S4, 239, "oddoneout",
    "Pick the ODD ONE OUT — three of these belong to the printed UIP picture on page 239, one is listed as absent in UIP:",
    "Ground glass opacification",
    [
        "Reticular shadows",
        "Honeycombing",
        "Traction bronchiectasis",
    ],
    "Under 'Features absent in UIP' the page lists only 'Nodules' and 'Ground glass opacification'. Reticular shadows, honeycombing and traction bronchiectasis are core UIP features on the same page.",
)

add(
    S4, 239, "match",
    "Match each captioned HRCT image on page 239 with its printed caption position — 1) Image captioned beneath the top-row scans 2) Bottom-left image with red circles 3) Bottom-middle image 4) Bottom-right image … A) Linear shadows B) Honeycombing C) Traction bronchiectasis D) Reticular shadows",
    "1-B, 2-C, 3-D, 4-A",
    ["1-D, 2-C, 3-B, 4-A", "1-B, 2-D, 3-C, 4-A", "1-B, 2-C, 3-A, 4-D"],
    "The six scans carry the captions 'Honeycombing' under the top row and, left to right below, 'Traction bronchiectasis' (with red circles), 'Reticular shadows' and 'Linear shadows'.",
)

add(
    S4, 239, "management",
    "Which new drugs for UIP-ILD close page 239, with their printed targets?",
    "Pirfenidone (Anti-TGF) and nintedanib (Anti-FDGF as printed, anti VEGF, anti PDGFR)",
    [
        "Pirfenidone (Anti-PDGF) and nintedanib (Anti-TGF, anti VEGF, anti PDGFR)",
        "Nintedanib (Anti-TGF) and pirfenidone (Anti-FDGF as printed, anti VEGF, anti PDGFR)",
        "Pirfenidone (Anti-TGF) and everolimus, an mTOR inhibitor",
    ],
    "The Note reads 'New drugs for treatment of UIP-ILD: Pirfenidone (Anti-TGF). Nintedanib (Anti-FDGF, anti VEGF, anti PDGFR).' 'FDGF' is preserved as printed; everolimus belongs to LAM on the next page.",
)

add(
    S4, 239, "truefalse",
    "TRUE or FALSE about the UIP pattern assembled on page 239.",
    "True — UIP is subpleural and basal predominant, and ground glass opacification is printed as absent in UIP",
    [
        "False — UIP is perihilar and apical predominant on this page",
        "False — ground glass opacification is listed as a specific feature of UIP",
        "True — UIP is subpleural and basal predominant, and nodules are its specific feature",
    ],
    "The bullets give 'Subpleural, basal predominant' distribution, while 'Features absent in UIP' lists nodules and ground glass opacification. Both halves of the False options invert the page.",
)


# ---------------------------------------------------------------- Unit 5: p240
add(
    S5, 240, "recall",
    "Which five HRCT statements define the NSIP pattern on page 240?",
    "Bilateral postero-basal ground-glass appearance, no destruction of lung parenchyma, no honeycombing, no cystic spaces, and prognosis NSIP > UIP",
    [
        "Bilateral postero-basal ground-glass appearance, destruction of lung parenchyma present, no honeycombing, no cystic spaces, and prognosis NSIP > UIP",
        "Unilateral postero-basal ground-glass appearance, no destruction of lung parenchyma, honeycombing present, no cystic spaces, and prognosis UIP > NSIP",
        "Bilateral postero-basal reticular appearance, no destruction of lung parenchyma, no honeycombing, cystic spaces present, and prognosis NSIP > UIP",
    ],
    "The NSIP bullets read 'B/L postero-basal ground-glass appearance', 'No destruction of lung parenchyma', 'No honeycombing', 'No cystic spaces' and 'Prognosis: NSIP > UIP', beside its CT image.",
)

add(
    S5, 240, "management",
    "Which treatment ranking is printed in the Note beside the NSIP pattern?",
    "MMF is best (printed 'MMF (Best)'), followed in the list by steroids and azathioprine",
    [
        "Steroids are best, followed in the list by MMF and azathioprine",
        "Azathioprine is best, followed in the list by steroids and MMF",
        "Pirfenidone is best, followed in the list by nintedanib and steroids",
    ],
    "The Note reads 'Rx: MMF (Best). Steroids. Azathioprine.' The antifibrotics pirfenidone and nintedanib belong to UIP-ILD on page 239, not to NSIP.",
)

add(
    S5, 240, "recall",
    "Which ten drugs are listed as causing ILD with an NSIP pattern on page 240?",
    "Amiodarone, bleomycin, busulfan, bromocriptine, nitrofurantoin, cyclophosphamide, methotrexate, anti-TNF, carmustine and mitomycin",
    [
        "Amiodarone, bleomycin, busulfan, bromocriptine, nitrofurantoin, cyclophosphamide, methotrexate, anti-TNF, cisplatin and mitomycin",
        "Amiodarone, bleomycin, busulfan, bromocriptine, minocycline, cyclophosphamide, methotrexate, anti-TNF, carmustine and mitomycin",
        "Amiodarone, bleomycin, busulfan, dantrolene, nitrofurantoin, cyclophosphamide, methotrexate, anti-TNF, carmustine and mitomycin",
    ],
    "Under 'Drugs causing ILD (NSIP pattern)' the two columns read amiodarone, bleomycin, busulfan, bromocriptine, nitrofurantoin, and cyclophosphamide, methotrexate, anti-TNF, carmustine, mitomycin. Minocycline and dantrolene appear in other chapters' drug lists, not this one.",
)

add(
    S5, 240, "fillup",
    "In that drug list, cyclophosphamide and methotrexate alone share a brace pointing to a different disease: ______.",
    "Hypersensitivity pneumonitis",
    ["Acute eosinophilic pneumonia", "Usual interstitial pneumonia", "Pulmonary alveolar proteinosis"],
    "Cyclophosphamide and methotrexate are bracketed together to 'Hypersensitivity pneumonitis', while the whole list is headed 'Drugs causing ILD (NSIP pattern)'. No other drug in the list carries this side brace.",
)

add(
    S5, 240, "recall",
    "Which COP/BOOP profile opens its section on page 240?",
    "Elderly males (>60–70 years as printed) with polypoid plugs (Masson's buds) in bronchioles, a pneumonia-like presentation, and associations of polymyositis/dermatomyositis",
    [
        "Young females (30–40 years) with polypoid plugs (Masson's buds) in bronchioles, a pneumonia-like presentation, and associations of polymyositis/dermatomyositis",
        "Elderly males (>60–70 years as printed) with polypoid plugs (Masson's buds) in alveoli, an Asthma-like presentation, and associations of Sjogren syndrome",
        "Elderly males (>60–70 years as printed) with caseating granulomas in bronchioles, a pneumonia-like presentation, and associations of polymyositis/dermatomyositis",
    ],
    "Under 'COP/BOOP (Bronchiolitis Obliterans Organising Pneumonia)' the bullets read 'Elderly males (>60–70 years)', 'Polypoid plugs (masson's buds) in bronchioles', 'Pneumonia like presentation' and 'Associations: Polymyositis/Dermatomyositis'.",
)

add(
    S5, 240, "match",
    "Match each COP feature on page 240 with its printed partner — 1) Restrictive type 2) Constrictive type with obstructive pattern 3) Reverse-halo sign 4) Halo sign … A) Consolidation surrounded by GGO, in invasive aspergillosis B) Most common type, responds to steroids C) GGO surrounded by consolidation, the caption on the COP scan D) No response to steroids",
    "1-B, 2-D, 3-C, 4-A",
    ["1-D, 2-B, 3-C, 4-A", "1-B, 2-D, 3-A, 4-C", "1-B, 2-C, 3-D, 4-A"],
    "HRCT in COP gives consolidations (peribronchial, perilobar opacities) and ground-glass opacities; types split into 'Restrictive (m/c): Responds to steroids' and 'Constrictive (Obstructive pattern): No response to steroids'. The scan is captioned 'Reverse-halo sign (GGO surrounded by consolidation)', and the Note contrasts 'Halo sign (Consolidation surrounded by GGO) in invasive aspergillosis'.",
)

add(
    S5, 240, "scenario",
    "A young woman with tuberous sclerosis and an angiomyolipoma presents with a spontaneous pneumothorax and a chylous effusion, and her HRCT shows cysts. Which labelled cyst panel and which printed drug apply?",
    "LAM — treated with everolimus, an mTOR inhibitor",
    [
        "LCH — treated with everolimus, an mTOR inhibitor",
        "LAM — treated with pirfenidone, an anti-TGF drug",
        "LIP — treated with MMF as best therapy",
    ],
    "The LAM panel reads 'Young females', associations of tuberous sclerosis and angiomyolipoma, complications of spontaneous pneumothorax and chylous effusion, and 'Rx: Everolimus (mTOR inhibitor)'. Every element of the vignette is in that one panel.",
)

add(
    S5, 240, "recall",
    "Which pathology markers and associations are printed under the LCH cyst panel?",
    "A young male with upper lobe fibrosis and spontaneous pneumothorax as complication; pathology CD1a positive and Birbeck granules positive; associations smoking, lytic lesions and diabetes insipidus",
    [
        "A young female with lower lobe fibrosis and chylous effusion as complication; pathology CD1a positive and Birbeck granules positive; associations smoking, lytic lesions and diabetes insipidus",
        "A young male with upper lobe fibrosis and spontaneous pneumothorax as complication; pathology CD20 positive and Birbeck granules negative; associations smoking, lytic lesions and diabetes insipidus",
        "A young male with upper lobe fibrosis and spontaneous pneumothorax as complication; pathology CD1a positive and Birbeck granules positive; associations tuberous sclerosis and angiomyolipoma",
    ],
    "The LCH panel reads 'Young male', 'Upper lobe fibrosis', 'Complication: Spontaneous pneumothorax', 'Pathology: CD1A (+), Birbeck granules (+)' and 'Associations: Smoking, Lytic lesions, Diabetes insipidus'. The tuberous sclerosis pair belongs to the LAM panel beside it.",
)

add(
    S5, 240, "oddoneout",
    "Pick the ODD ONE OUT — three of these statements are printed on page 240, one reverses the page:",
    "LIP is associated with tuberous sclerosis and angiomyolipoma",
    [
        "NSIP has a better prognosis than UIP",
        "COP of restrictive type responds to steroids",
        "LIP is associated with Sjogren's syndrome and HIV",
    ],
    "The LIP panel lists only 'Sjogren's' and 'HIV' as associations, exactly as on page 237. Tuberous sclerosis and angiomyolipoma are the LAM associations in the neighbouring panel.",
)


# ---------------------------------------------------------------- Unit 6: p241
add(
    S6, 241, "match",
    "Match each HRCT finding with the disease in the page 241 table — 1) Reticular and linear shadows 2) Ground glass opacities 3) Consolidations 4) Mosaic attenuation with air trapping … A) HP B) UIP C) COP D) NSIP",
    "1-B, 2-D, 3-C, 4-A",
    ["1-B, 2-C, 3-D, 4-A", "1-D, 2-B, 3-C, 4-A", "1-B, 2-D, 3-A, 4-C"],
    "The table pairs reticular & linear shadows with UIP, ground glass opacities with NSIP, consolidations with COP, and mosaic attenuation/air trapping with HP.",
)

add(
    S6, 241, "match",
    "Match each remaining HRCT finding with its table disease — 1) Nodular shadows 2) Cysts 3) Traction bronchiectasis 4) Honeycombing … A) UIP B) LCH/LAM/LIP C) LCH/LAM D) UIP again",
    "1-C, 2-B, 3-A, 4-D",
    ["1-B, 2-C, 3-A, 4-D", "1-C, 2-B, 3-D, 4-A", "1-C, 2-A, 3-B, 4-D"],
    "The table pairs nodular shadows with LCH/LAM, cysts with the wider trio LCH/LAM/LIP, and both traction bronchiectasis and honeycombing with UIP — so UIP appears against three findings in this table (reticular/linear, traction, honeycombing).",
)

add(
    S6, 241, "recall",
    "Which four causes are listed for nodular shadows on HRCT in the page 241 Note?",
    "LAM, LCH, LIP and RB-ILD",
    [
        "LAM, LCH, UIP and RB-ILD",
        "LAM, LCH, LIP and COP",
        "LCH, LIP, RB-ILD and NSIP",
    ],
    "Note 1 reads 'Nodular shadows on HRCT: Non-specific feature; Causes: LAM, LCH, LIP, RB-ILD', beside the four scans captioned 'HRCT findings in ILD: Nodular shadows'. The Note list is wider than the table row above it, which names only LCH/LAM.",
)

add(
    S6, 241, "truefalse",
    "TRUE or FALSE about nodular shadows as printed on page 241.",
    "True — nodular shadows are called a non-specific feature, and their cause list in the Note adds LIP and RB-ILD to the table's LCH/LAM",
    [
        "False — nodular shadows are called specific for UIP on this page",
        "False — the Note and the table give identical cause lists for nodular shadows",
        "True — nodular shadows are specific for LCH and exclude LAM",
    ],
    "The Note explicitly calls nodular shadows a 'Non-specific feature' and lists LAM, LCH, LIP and RB-ILD, whereas the summary table pairs nodular shadows only with LCH/LAM. Specificity on page 239 belonged to the UIP set, not to nodules.",
)

add(
    S6, 241, "recall",
    "What mechanism and association are printed for the tree-in-bud appearance on HRCT?",
    "It arises due to endobronchial obstruction and is associated with infections",
    [
        "It arises due to endobronchial dilatation and is associated with fibrosis",
        "It arises due to vascular occlusion and is associated with infections",
        "It arises due to endobronchial obstruction and is associated with malignancy",
    ],
    "Note 2 reads 'Tree in bud appearance on HRCT: D/t endobronchial obstruction. Associated with infections.' The same appearance is labelled on the ABPA scan on page 254.",
)

add(
    S6, 241, "fillup",
    "The four lower-right scans on page 241 are captioned 'mosaic attenuation in ILD', and the disease named in brackets beneath is ______.",
    "Hypersensitivity pneumonitis",
    ["Cryptogenic organizing pneumonia", "Usual interstitial pneumonia", "Nonspecific interstitial pneumonia"],
    "The caption reads 'mosaic attenuation in ILD (Hypersensitivity pneumonitis)', matching the table row that pairs mosaic attenuation and air trapping with HP.",
)

add(
    S6, 241, "oddoneout",
    "Pick the ODD ONE OUT — three of these captions or pairings are printed on page 241, one is not:",
    "'Ill-defined infiltrates in upper lobe' beneath the lower-left scan",
    [
        "'HRCT findings in ILD: Nodular shadows' beneath the upper scans",
        "Cysts paired with LCH/LAM/LIP in the table",
        "Honeycombing paired with UIP in the table",
    ],
    "The lower-left scan is captioned 'Ill-defined infiltrates in lower lobe', not upper lobe. The nodular-shadows caption and the cyst and honeycombing pairings are printed exactly as the other options state.",
)


# ---------------------------------------------------------------- Unit 7: p242
add(
    S7, 242, "match",
    "Match each upper-lobe ILD group on page 242 with its printed members — 1) Occupational lung disorders 2) CTDs … A) Sarcoidosis and ankylosing spondylitis B) Silicosis, berylliosis and coal-worker's pneumoconiosis",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "Under '3. Conditions with upper-lobe ILD' the occupational bullet arrows to silicosis, berylliosis and coal-worker's pneumoconiosis, while the CTDs bullet arrows to sarcoidosis and ankylosing spondylitis — sarcoidosis sits inside the CTD brace as printed.",
)

add(
    S7, 242, "recall",
    "Which single-line entries complete the upper-lobe ILD list after the occupational and CTD groups?",
    "ABPA, hypersensitivity pneumonitis, TB (fibrosis of UL) and LCH",
    [
        "ABPA, hypersensitivity pneumonitis, TB (fibrosis of LL) and LAM",
        "Asbestosis, hypersensitivity pneumonitis, TB (fibrosis of UL) and LCH",
        "ABPA, hypersensitivity pneumonitis, sarcoidosis and LCH",
    ],
    "The remaining bullets read 'ABPA', 'Hypersensitivity pneumonitis', 'TB (Fibrosis of UL)' and 'LCH'. Asbestosis was the lower-lobe occupational exception on page 237 and does not reappear here.",
)

add(
    S7, 242, "recall",
    "What caption is printed beneath the chest film that illustrates this upper-lobe page?",
    "'LL reticular shadows in IPF', as printed",
    [
        "'UL reticular shadows in IPF'",
        "'LL nodular shadows in IPF', as printed",
        "'Bilateral reticular shadows in NSIP'",
    ],
    "Despite heading a page about upper-lobe disease, the film is captioned 'LL reticular shadows in IPF' — preserved verbatim, since IPF/UIP is the basal-predominant pattern of page 239.",
)

add(
    S7, 242, "numeric",
    "Which demographic line opens the PAP section on page 242?",
    "30–50, male (printed without a years unit)",
    [
        "20–30, female",
        "30–50, female",
        "50–70, male (printed without a years unit)",
    ],
    "Under 'PAP (Pulmonary Alveolar Proteinosis)' the first bullet reads '30–50 male', with no age unit printed. The 50–70 span belongs to rheumatoid arthritis ILD on page 237.",
)

add(
    S7, 242, "match",
    "Match each PAP type with its printed mechanism — 1) Congenital 2) Acquired … A) Antibodies against GM-CSF causing reduced surfactant clearance, and marked most common B) Surfactant protein SP-B mutation",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "The Types brace reads 'Congenital: Surfactant Protein (SP)-B mutation' and 'Acquired (m/c): Antibodies against GM-CSF → ↓ surfactant clearance'. Only the acquired arm carries the m/c tag and the clearance arrow.",
)

add(
    S7, 242, "fillup",
    "In PAP the reduced surfactant clearance produces the clinical feature of chunky gelatinous sputum that is ______ positive.",
    "PAS",
    ["GMS", "AFB", "Gram"],
    "The arrow from '↓ surfactant clearance' ends at 'C/F: Chunky gelatinous sputum (PAS +)'. GMS staining belongs to the Aspergillus tissue image on page 253.",
)

add(
    S7, 242, "management",
    "Which X-ray appearance, differential and treatment close the PAP section?",
    "X-ray batwing appearance, differential diagnosis silicosis, and treatment by whole lung lavage",
    [
        "X-ray reverse batwing appearance, differential diagnosis asbestosis, and treatment by whole lung lavage",
        "X-ray batwing appearance, differential diagnosis silicosis, and treatment by GM-CSF antibodies",
        "X-ray batwing appearance, differential diagnosis berylliosis, and treatment by lung transplantation",
    ],
    "The closing bullets read 'X-ray: Batwing appearance', 'D/d: Silicosis' and 'Rx: Whole lung lavage'. Reverse bat wing is the chronic eosinophilic pneumonia image on page 252, not PAP.",
)


GUIDES = {
    S1: (
        "Interstitium and Its Types, Lung Parenchyma, TGF-β/PDGF Fibrosis, ILD Classification and the Seven Idiopathic Interstitial Pneumonias",
        "The interstitium (p236) is connective tissue holding the lungs together: alveolar (subpleural and lobar), vascular (surrounds vessels) and axial (connects lung to chest wall); lung parenchyma is alveoli plus alveolar and vascular interstitium.\n"
        "ILD is 'diffuse parenchymal lung fibrosis', TGF-β > PDGF mediated, with TGF-β boxed as the most potent pathogenic fibrogenic cytokine, and classifies into idiopathic interstitial pneumonia (most common), autoimmune ILD, hypersensitivity pneumonitis, sarcoidosis and miscellaneous.\n"
        "The seven idiopathic interstitial pneumonias run IPF/UIP (most common), NSIP (2nd), COP (3rd), RB-ILD and DIP bracketed as smoking-associated, acute interstitial pneumonia (ARDS with diffuse alveolar damage after COVID/viral infection, very poor prognosis), and LIP.",
    ),
    S2: (
        "Autoimmune and Miscellaneous ILD (Occupational Lobes, Vasculitis, Inherited, Drug-Induced, LCH, LAM) with the UIP/NSIP/COP/LIP Important Points",
        "Autoimmune ILD (p237) complicates rheumatoid arthritis, diffuse systemic sclerosis, polymyositis/dermatomyositis, MCTD, Sjogren's syndrome and ankylosing spondylitis.\n"
        "Miscellaneous ILD covers occupational disease (asbestosis lower lobe; silicosis, berylliosis and coal-worker's pneumoconiosis upper lobe), EGPA/Churg-Strauss vasculitis, inherited neurofibromatosis and tuberous sclerosis, bleomycin, smoking-associated LCH (printed 'Langerhan's') and LAM.\n"
        "Important points: idiopathic UIP/IPF is most common and RA-ILD affects smoking males of 50–70 years; NSIP affects young females as a subacute restrictive process linked to drugs and connective tissue disease; COP is most common in inflammatory muscle disease; LIP links to Sjogren syndrome and HIV; and the commonest pattern is UIP in RA but NSIP in other conditions.",
    ),
    S3: (
        "Clinical Features of ILD: Cardinal Symptoms, the Crackles-and-Clubbing Table versus Bronchiectasis, Skin Signs, Pulmonary HTN Prognosis and CXR",
        "ILD (p238) presents with two cardinal symptoms, dry non-productive cough and dyspnea on exertion, often misdiagnosed as bronchitis; fever with arthralgia suggests sarcoidosis, wheeze is specific to bronchiectasis/ABPA/hypersensitivity pneumonitis, pleuritic pain to asbestosis, and hemoptysis is rare.\n"
        "Crackles in ILD are bilateral bibasal, fine 'velcro', end to early expiratory as printed, without cough/posture variation, against unilateral coarse early-to-mid inspiratory crackles in bronchiectasis; clubbing is present in ILD and absent in bronchiectasis except childhood cystic bronchiectasis, with cafe-au-lait spots, erythema nodosum and Raynaud's pointing to neurofibromatosis, sarcoidosis and scleroderma.\n"
        "Hypoxia drives pulmonary vasoconstriction to pulmonary HTN, the most significant prognostic factor; OSAS (ruled out by sleep study) and ILD (by CT scan) present directly with pulmonary HTN, and the CXR shows bilateral bibasal subpleural reticular/reticulo-nodular infiltrates.",
    ),
    S4: (
        "PFT in Initial versus Advanced ILD, HRCT as Investigation of Choice and the UIP Pattern with Its Image Captions and New Antifibrotic Drugs",
        "Initially (p239) ILD is a type 1 respiratory failure with only diffusion impaired — impaired DLCO with normal FEV1 and FVC — advancing to type 3 failure with ventilation impaired, FVC falling sharply and FEV1/FVC normal or raised.\n"
        "HRCT is the investigation of choice to determine pattern and prognosis: in UIP, linear shadows (intralobular septal thickening) and reticular shadows (net of linear opacities) are suggestive, while subpleural basal-predominant honeycombing (small polyhedral cystic spaces), loss of lung architecture and traction bronchiectasis complete the set bracketed specific for UIP, and nodules with ground glass opacification are absent.\n"
        "The six scans are captioned honeycombing, traction bronchiectasis, reticular shadows and linear shadows, and the new UIP-ILD drugs are pirfenidone (anti-TGF) and nintedanib (anti-FDGF as printed, anti-VEGF, anti-PDGFR).",
    ),
    S5: (
        "NSIP Pattern and Its Treatment, Drugs Causing ILD, COP/BOOP with Halo Signs, and Cysts on HRCT (LAM, LCH, LIP)",
        "NSIP (p240) shows bilateral postero-basal ground glass without parenchymal destruction, honeycombing or cystic spaces and a prognosis better than UIP; MMF is printed best, ahead of steroids and azathioprine.\n"
        "Ten drugs cause NSIP-pattern ILD — amiodarone, bleomycin, busulfan, bromocriptine, nitrofurantoin, cyclophosphamide, methotrexate, anti-TNF, carmustine and mitomycin — with cyclophosphamide and methotrexate braced to hypersensitivity pneumonitis.\n"
        "COP/BOOP affects elderly males (>60–70 years as printed) with Masson's buds, a pneumonia-like presentation and polymyositis/dermatomyositis associations; its restrictive type responds to steroids while the constrictive obstructive type does not, the reverse-halo sign (GGO inside consolidation) contrasts with the halo sign of invasive aspergillosis, and HRCT cysts split into LAM (young females, tuberous sclerosis/angiomyolipoma, pneumothorax and chylous effusion, everolimus), LCH (young male, upper lobe fibrosis, CD1a and Birbeck granules positive, smoking, lytic lesions, diabetes insipidus) and LIP (Sjogren's, HIV).",
    ),
    S6: (
        "HRCT Finding–Disease Table, Nodular Shadows and Tree-in-Bud Notes with the Mosaic Attenuation and Lower-Lobe Infiltrate Captions",
        "The HRCT table (p241) maps reticular/linear shadows, traction bronchiectasis and honeycombing to UIP; nodular shadows to LCH/LAM; ground glass to NSIP; consolidations to COP; mosaic attenuation/air trapping to HP; and cysts to LCH/LAM/LIP.\n"
        "Nodular shadows are a non-specific feature caused by LAM, LCH, LIP and RB-ILD, and tree-in-bud reflects endobronchial obstruction associated with infections.\n"
        "The page's scans are captioned 'HRCT findings in ILD: Nodular shadows', 'mosaic attenuation in ILD (Hypersensitivity pneumonitis)' and 'Ill-defined infiltrates in lower lobe'.",
    ),
    S7: (
        "Conditions with Upper-Lobe ILD, the LL Reticular Caption in IPF, and Pulmonary Alveolar Proteinosis (PAP)",
        "Upper-lobe ILD (p242) groups the occupational trio silicosis, berylliosis and coal-worker's pneumoconiosis, the CTD pair sarcoidosis and ankylosing spondylitis as printed, and ABPA, hypersensitivity pneumonitis, TB with upper-lobe fibrosis and LCH; the illustrating film is nonetheless captioned 'LL reticular shadows in IPF'.\n"
        "PAP affects 30–50-year males as printed without a unit: congenital disease from SP-B mutation, and acquired most-common disease from anti-GM-CSF antibodies reducing surfactant clearance.\n"
        "Its clinical feature is chunky gelatinous PAS-positive sputum, the X-ray shows a batwing appearance with silicosis as differential, and treatment is whole lung lavage.",
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
