#!/usr/bin/env python3
"""Generate Chapter 43: Hypersensitivity Pneumonitis (Book p257–259).

Every question is anchored to a printed line, table cell or figure caption of
uploads/03.pdf sheets 10–12 (Book pages 257–259), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 43
TITLE = "Hypersensitivity Pneumonitis"
PAGES = "257-259"

S1 = "Extrinsic Allergic Alveolitis: Type IV over III Pathogenesis, Absent Type I Features, and the Twelve-Disease Etiology Table"
S2 = "Acute, Subacute and Chronic Presentations, Complications, Non-Caseating Granuloma and Emphysema Notes, Precipitins and BAL CD8/CD4"
S3 = "PFT, CXR and CT in HP with the Head Cheese Pattern, Steroid Response versus Irreversible Fibrosis, and the HP versus ABPA Difference Table"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(43000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(43100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p257
add(
    S1, 257, "recall",
    "Which synonym and host line open hypersensitivity pneumonitis on page 257?",
    "AKA extrinsic allergic alveolitis, occurring usually in non smokers",
    [
        "AKA intrinsic allergic alveolitis, occurring usually in non smokers",
        "AKA extrinsic allergic alveolitis, occurring usually in smokers",
        "AKA extrinsic allergic bronchiolitis, occurring usually in non smokers",
    ],
    "The head of the chapter reads 'AKA extrinsic allergic alveolitis' and 'usually in non smokers' — a useful counterweight to the smoking-associated cystic and interstitial diseases of pages 236–240.",
)

add(
    S1, 257, "recall",
    "Which pathogenesis chain is printed for HP on page 257?",
    "Repeated organic dust inhalation causes hypersensitivity of Type IV greater than III, producing predominantly lymphocytic inflammation of terminal airways, alveoli and interstitium",
    [
        "Repeated inorganic dust inhalation causes hypersensitivity of Type I greater than III, producing predominantly eosinophilic inflammation of terminal airways, alveoli and interstitium",
        "Single organic dust inhalation causes hypersensitivity of Type IV greater than III, producing predominantly lymphocytic inflammation of large airways only",
        "Repeated organic dust inhalation causes hypersensitivity of Type III greater than IV, producing predominantly neutrophilic inflammation of terminal airways, alveoli and interstitium",
    ],
    "The chain reads 'Repeated organic dust inhalation → Hypersensitivity (Type IV > III) → Inflammation (Predominantly lymphocytic) of terminal airways, alveoli & interstitium'. Repetition, the IV-over-III order and the lymphocyte all matter.",
)

add(
    S1, 257, "recall",
    "Because there is no type 1 hypersensitivity in HP, which three absences does the pathology block print?",
    "No eosinophilia, no raised IgE and no migratory lung infiltrates",
    [
        "No lymphocytosis, no raised IgE and no diffuse infiltrates",
        "No eosinophilia, no precipitins and no migratory lung infiltrates",
        "No eosinophilia, no raised IgE and no granulomas",
    ],
    "The block reads 'No type 1 hypersensitivity → No: Eosinophilia, ↑ IgE, migratory lung infiltrates' — precisely the type 1 triad that Loeffler syndrome displayed on page 250.",
)

add(
    S1, 257, "recall",
    "Which infiltrate evolution and granuloma statement complete the pathology on page 257?",
    "Pulmonary infiltrates are diffuse initially and become a reticulo-nodular pattern, and non caseating granulomas are present",
    [
        "Pulmonary infiltrates are migratory initially and become reticular, and caseating granulomas are present",
        "Pulmonary infiltrates are diffuse initially and become a reticulo-nodular pattern, and granulomas are absent",
        "Pulmonary infiltrates are peripheral initially and become diffuse, and non caseating granulomas are present",
    ],
    "The bullets read 'Pulmonary infiltrates: Diffuse (Initially) → Reticulo-nodular pattern' and 'Non caseating granulomas present', the same evolution the CXR line repeats on page 259.",
)

add(
    S1, 257, "match",
    "Match each thermophilic-actinomycete Disease in the etiology table with its printed source — 1) Farmer's lung, marked most common 2) Bagassosis, marked second most common 3) Mushroom worker's lung … A) Moldy compost or mushroom B) Moldy hay C) Moldy sugarcane",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "Farmer's lung (m/c) comes from moldy hay, bagassosis (2nd m/c) from moldy sugarcane and mushroom worker's lung from moldy compost/mushroom, all three sharing the merged antigen cell 'Thermophilic actinomycete: Thermoactinomyces vulgaris (m/c antigen)'.",
)

add(
    S1, 257, "recall",
    "Which antigen cell is shared by the next four rows of the etiology table, and which sources accompany them?",
    "Aspergillus clavatus covers compost lung (compost), tobacco worker's lung (mold on tobacco), malt worker's lung (barley) and cheese washer's lung, whose source cell is blank",
    [
        "Thermoactinomyces vulgaris covers compost lung, tobacco worker's lung, malt worker's lung and cheese washer's lung from cheese washings",
        "Aspergillus fumigatus covers compost lung (compost), tobacco worker's lung (mold on tobacco), malt worker's lung (barley) and cheese washer's lung",
        "Aspergillus clavatus covers compost lung (compost), tobacco worker's lung (barley), malt worker's lung (mold on tobacco) and cheese washer's lung, whose source cell is blank",
    ],
    "The second merged antigen cell, 'Aspergillus clavatus', spans compost lung, tobacco worker's lung, malt worker's lung and cheese washer's lung, with sources compost, mold on tobacco and barley printed for the first three and the cheese washer source left blank.",
)

add(
    S1, 257, "match",
    "Match each remaining etiology-table Disease with its printed source and antigen pairing — 1) Hot tub, humidifier or air conditioner lung 2) Bird fancier's lung 3) Wood trimmer's lung 4) Familial HP and chemical worker's lung … A) Source pigeon, parrot or chicken with avian droppings as antigen B) Familial HP from wood pulp with Bacillus subtilis, and chemical worker's lung from polyurethane foams (isocyanate) with its antigen cell blank C) Source cell blank with Cladosporium and MAC as antigens D) Source cell blank with Rhizopus as antigen",
    "1-C, 2-A, 3-D, 4-B",
    ["1-A, 2-C, 3-D, 4-B", "1-C, 2-A, 3-B, 4-D", "1-C, 2-D, 3-A, 4-B"],
    "Hot tub/humidifier/air conditioner lung pairs a blank source with Cladosporium and MAC; bird fancier's lung pairs pigeon/parrot/chicken with avian droppings; wood trimmer's lung pairs a blank source with Rhizopus; familial HP pairs wood pulp with Bacillus subtilis; and chemical worker's lung prints polyurethane foams (isocyanate) with a blank antigen cell.",
)

add(
    S1, 257, "scenario",
    "A non-smoking pigeon keeper develops lymphocytic alveolitis with non caseating granulomas, no eosinophilia and a normal IgE. Which Disease, source and antigen does the page 257 table assign him?",
    "Bird fancier's lung — pigeon source, avian droppings antigen",
    [
        "Farmer's lung — moldy hay source, Thermoactinomyces vulgaris antigen",
        "Bird fancier's lung — pigeon source, Aspergillus clavatus antigen",
        "Mushroom worker's lung — moldy compost source, Thermoactinomyces antigen",
    ],
    "Bird fancier's lung is the only row sourced to 'Pigeon/ parrot/ chicken' with antigen 'Avian droppings', and the absent eosinophilia and IgE rise are the no-type-1 signature printed above the table.",
)

add(
    S1, 257, "truefalse",
    "TRUE or FALSE about the superlatives printed inside the etiology table.",
    "True — farmer's lung is marked the most common Disease and Thermoactinomyces vulgaris the most common antigen, while bagassosis is marked second most common",
    [
        "False — bagassosis is marked most common and farmer's lung second most common",
        "False — Aspergillus clavatus is marked the most common antigen",
        "True — bird fancier's lung is marked most common because its row is printed in red",
    ],
    "The table tags 'Farmer's lung (m/c)', 'Bagassosis (2nd m/c)' and, in the merged cell, 'Thermoactinomyces vulgaris (m/c antigen)'. Bird fancier's lung is highlighted in red ink but carries no frequency tag.",
)


# ---------------------------------------------------------------- Unit 2: p258
add(
    S2, 258, "match",
    "Match each HP presentation tempo on page 258 with its printed fate — 1) Acute 2) Subacute 3) Chronic … A) Marked most common B) Can cause fibrosis, that is ILD C) Self resolving",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "Presentation reads 'Acute: Self resolving', 'Subacute: m/c' and 'Chronic: Can cause fibrosis (ILD)', returning HP to the ILD classification of page 236 in its chronic form.",
)

add(
    S2, 258, "numeric",
    "Which clinical features and timescale define the acute form of HP?",
    "Fever, chills and cough with a raised ESR, resolving in 2–4 days",
    [
        "Fever, chills and cough with a raised IgE, resolving in 2–4 weeks",
        "Gradually progressive dyspnea and cough, resolving in 2–4 days",
        "Fever, chills and cough with a raised ESR, resolving in 2–4 hours as printed",
    ],
    "The acute form reads 'Fever, chills, cough (↑ ESR)' with 'Resolves in 2–4 days' beneath it. The raised marker is ESR, not the IgE that type 1 disease would raise.",
)

add(
    S2, 258, "recall",
    "Which three statements define the subacute form of HP?",
    "Gradually progressive dyspnea and cough with fatiguability, no systemic features, and upper lobe involvement",
    [
        "Gradually progressive dyspnea and cough with fatiguability, prominent systemic features, and lower lobe involvement",
        "Abrupt dyspnea and cough with fever and chills, and upper lobe involvement",
        "Gradually progressive dyspnea and cough with fatiguability, no systemic features, and diffuse involvement without lobar preference as printed",
    ],
    "The subacute form reads 'Gradually progressive dyspnea & cough + fatiguability', 'No systemic features' and 'Upper lobe involvement' — the lobar preference that placed HP in the upper-lobe lists on pages 242 and 255.",
)

add(
    S2, 258, "match",
    "Match each named HP Disease with its printed complication on page 258 — 1) Bird fancier's lung 2) Farmer's lung … A) Emphysematous changes B) Rarely causes fibrosis or ILD",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "Complications read 'Bird fancier's lung: Rarely cause fibrosis/ ILD' and 'Farmer's lung: Emphysematous changes'. The commonest HP thus ends in emphysema rather than the fibrosis the chronic form threatens.",
)

add(
    S2, 258, "recall",
    "Which seven causes of non caseating granulomas are listed in the page 258 Note?",
    "HP, 30% of TB as printed, lymphoma, sarcoidosis, cat scratch disease, Crohn's disease and berylliosis",
    [
        "HP, TB without any percentage, lymphoma, sarcoidosis, cat scratch disease, ulcerative colitis and berylliosis",
        "HP, 30% of TB as printed, lymphoma, sarcoidosis, cat scratch disease, Crohn's disease and silicosis",
        "Sarcoidosis, 30% of TB as printed, lymphoma, cat scratch disease, Crohn's disease, berylliosis and ABPA",
    ],
    "The Note lists HP itself, '30 % TB', lymphoma, sarcoidosis, cat scratch disease, Crohn's disease and berylliosis — berylliosis having been introduced as the sarcoid mimic on pages 228–229. HP heads its own granuloma list.",
)

add(
    S2, 258, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed on page 258 as diseases causing emphysematous changes apart from COPD, one is not:",
    "Bird fancier's lung",
    [
        "Farmer's lung",
        "Cryptogenic organising pneumonia",
        "Coal worker's pneumoconiosis, marked rare",
    ],
    "The second Note lists farmer's lung, cryptogenic organising pneumonia and coal worker's pneumoconiosis (rare) as non-COPD emphysema causes. Bird fancier's lung, in the complications block above, rarely causes fibrosis instead.",
)

add(
    S2, 258, "recall",
    "What does the Management section print about serum precipitin in HP?",
    "It can be positive but is non-specific, arising due to type III hypersensitivity",
    [
        "It is always negative because HP has no type III component",
        "It is specific and diagnostic, arising due to type I hypersensitivity",
        "It can be positive but is non-specific, arising due to type IV hypersensitivity",
    ],
    "Investigations read 'S. precipitin: Can be positive (Non specific): D/t type III hypersensitivity' — the junior partner in the Type IV > III mechanism leaving a serological trace that cannot confirm the diagnosis.",
)

add(
    S2, 258, "fillup",
    "BAL in HP shows lymphocytosis with the printed fraction CD8/CD4 greater than ______.",
    "2",
    ["1", "3.5", "0.5"],
    "The BAL line reads 'Lymphocytosis: CD 8 / CD 4 > 2', a CD8-dominant lavage. The inverted ratio for sarcoidosis is given as a mirror note on the next page.",
)

add(
    S2, 258, "scenario",
    "Four days after shovelling moldy hay a farmer's fever, chills and cough with raised ESR settle on their own, but over the following seasons he develops emphysematous change rather than fibrosis. Which tempo and which complication has he shown, in the page's terms?",
    "The acute self-resolving form of farmer's lung, whose printed complication is emphysematous change",
    [
        "The subacute form of bird fancier's lung, which rarely causes fibrosis",
        "The chronic form of farmer's lung, whose printed complication is fibrosis in every case",
        "The acute form of bagassosis, whose printed complication is emphysematous change",
    ],
    "Fever, chills, cough and raised ESR resolving in 2–4 days is the acute form, moldy hay makes it farmer's lung, and farmer's lung alone carries 'Emphysematous changes' as its complication on this page.",
)


# ---------------------------------------------------------------- Unit 3: p259
add(
    S3, 259, "recall",
    "Which PFT and CXR statements open page 259, and what captions the chest film?",
    "In chronic ILD/fibrosis the PFT is restrictive; CXR moves from diffuse opacities to reticulonodular shadows; and the film, labelled A, is captioned 'CXR infiltrates in acute HP'",
    [
        "In chronic ILD/fibrosis the PFT is obstructive; CXR moves from diffuse opacities to reticulonodular shadows; and the film is captioned 'CXR infiltrates in acute HP'",
        "In chronic ILD/fibrosis the PFT is restrictive; CXR moves from reticulonodular shadows to diffuse opacities; and the film is captioned 'CXR infiltrates in chronic HP'",
        "The PFT is restrictive in acute HP; CXR moves from diffuse opacities to reticulonodular shadows; and the film is captioned 'mosaic tiles attenuation'",
    ],
    "The page opens 'PFT: In chronic form (ILD/ fibrosis): Restrictive pattern' and 'CXR: Diffuse opacities → Reticulonodular shadows', with film A captioned 'CXR infiltrates in acute HP' — the evolution already stated in the pathology on page 257.",
)

add(
    S3, 259, "recall",
    "Which three CT findings are printed for HP on page 259?",
    "Centrilobular nodules, bilateral ground glass opacities, and mosaic attenuation or head cheese pattern of varying densities on the same CT",
    [
        "Centrilobular nodules, unilateral ground glass opacities, and honeycombing",
        "Perilobular nodules, bilateral ground glass opacities, and crazy pavement pattern",
        "Centrilobular nodules, bilateral consolidations, and mosaic attenuation or head cheese pattern of uniform density",
    ],
    "CT lists 'Centrilobular nodules', 'B/L ground glass opacities (GGO)' and 'mosaic attenuation/ Head cheese pattern (varying densities on same CT)'. Mosaic attenuation was the HP row of the HRCT table on page 241.",
)

add(
    S3, 259, "match",
    "Match each CT image on page 259 with its printed label and caption — 1) Left scan marked B with red arrows 2) Right scan … A) Captioned mosaic tiles attenuation B) Nodular opacity arrows, captioned bilateral GGO and nodular opacity, the pair jointly captioned CT in HP",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "Scan B carries 'Nodular opacity' arrows over the caption 'B/L GGO & nodular opacity', the right scan is captioned 'mosaic tiles attenuation', and both together are labelled 'CT: HP'.",
)

add(
    S3, 259, "recall",
    "Which mirror-image BAL Note is printed for sarcoidosis on page 259?",
    "BAL lymphocytosis with CD4/CD8 greater than 2 indicates sarcoidosis — the inverse of HP's CD8/CD4 dominance",
    [
        "BAL lymphocytosis with CD8/CD4 greater than 2 indicates sarcoidosis, identical to HP",
        "BAL eosinophilia above 40% indicates sarcoidosis",
        "BAL lymphocytosis with CD4/CD8 less than 1 indicates sarcoidosis",
    ],
    "The Note reads 'BAL lymphocytosis with CD 4 / CD 8 > 2: Sarcoidosis', deliberately inverting the CD8/CD4 > 2 of HP on page 258 so the two granulomatous diseases separate on lavage.",
)

add(
    S3, 259, "management",
    "Which two treatment statements are printed for HP on page 259?",
    "The subacute form responds to steroids, but once fibrosis is present the Disease is irreversible",
    [
        "The acute form requires steroids, and fibrosis reverses with prolonged therapy",
        "The subacute form responds to antifungals, but once fibrosis is present the Disease is irreversible",
        "All forms respond to steroids including established fibrosis",
    ],
    "Treatment reads 'Subacute form: Respond to steroids' and 'If fibrosis (+): Irreversible' — placing the therapeutic window in the most common, subacute, presentation before chronic fibrosis supervenes.",
)

add(
    S3, 259, "match",
    "Match each row of the HP versus ABPA table with its printed pair — 1) Pathology 2) Radiographic features 3) Skin test reaction 4) Blood markers … A) ABPA migratory infiltrates with bronchiectatic changes versus HP diffuse infiltrates becoming reticulonodular opacities B) ABPA positive to A. fumigatus versus HP positive to A. clavatus C) ABPA eosinophilia positive, IgG precipitins positive and serum IgE markedly raised versus HP eosinophilia negative, precipitins positive and serum IgE normal D) ABPA airway colonisation with eosinophilic inflammation and hypersensitivity I plus III versus HP non caseating granulomas with lymphocytic inflammation and hypersensitivity IV over III",
    "1-D, 2-A, 3-B, 4-C",
    ["1-A, 2-D, 3-B, 4-C", "1-D, 2-A, 3-C, 4-B", "1-D, 2-B, 3-A, 4-C"],
    "Pathology contrasts colonisation and eosinophilic (I + III) inflammation in ABPA with granulomas and lymphocytic (IV > III) inflammation in HP; radiology contrasts migratory bronchiectatic change with diffuse-to-reticulonodular infiltrates; skin tests are positive to fumigatus in ABPA and clavatus in HP; and blood work separates only on eosinophilia and IgE, since IgG Aspergillus precipitins of type III hypersensitivity are positive in both.",
)

add(
    S3, 259, "scenario",
    "Two patients are skin-test positive to an Aspergillus species with positive IgG precipitins. One has eosinophilia, a markedly raised IgE and migratory infiltrates with bronchiectasis; the other has no eosinophilia, a normal IgE and reticulonodular opacities. Using the page 259 table, name each.",
    "The first is ABPA reacting to A. fumigatus; the second is HP reacting to A. clavatus",
    [
        "The first is HP reacting to A. clavatus; the second is ABPA reacting to A. fumigatus",
        "Both are ABPA, separated only by Disease stage",
        "The first is ABPA reacting to A. clavatus; the second is HP reacting to A. fumigatus",
    ],
    "Shared precipitins cannot separate them, but eosinophilia with ↑↑ IgE and migratory bronchiectatic infiltrates fill the ABPA column (fumigatus), while absent eosinophilia, normal IgE and reticulonodular opacities fill the HP column (clavatus).",
)

add(
    S3, 259, "truefalse",
    "TRUE or FALSE about the shared row of the HP versus ABPA table.",
    "True — IgG Aspergillus precipitins, labelled type III hypersensitivity, are the one test printed positive in both diseases",
    [
        "False — precipitins are positive in ABPA but negative in HP",
        "False — serum IgE, not precipitins, is the shared positive row",
        "True — peripheral eosinophilia is also printed positive in both diseases",
    ],
    "The row 'IgG Aspergillus precipitins (Type III hypersensitivity)' reads '+ve' under both ABPA and HP, reflecting the type III component each mechanism carries; eosinophilia and IgE split the columns instead.",
)

add(
    S3, 259, "fillup",
    "The varying densities coexisting on one HP CT are given the alternative name of the ______ pattern.",
    "head cheese",
    ["crazy pavement", "tree in bud", "reverse halo"],
    "The CT bullet reads 'mosaic attenuation/ Head cheese pattern (varying densities on same CT)'. Crazy pavement belonged to silicosis and PAP on page 225, and reverse halo to COP on page 240.",
)


GUIDES = {
    S1: (
        "Extrinsic Allergic Alveolitis: Type IV over III Pathogenesis, Absent Type I Features, and the Twelve-Disease Etiology Table",
        "HP (p257), AKA extrinsic allergic alveolitis and usually a disease of non-smokers, follows repeated organic dust inhalation through Type IV > III hypersensitivity into lymphocytic inflammation of terminal airways, alveoli and interstitium.\n"
        "Without type 1 hypersensitivity there is no eosinophilia, no raised IgE and no migratory infiltrates; infiltrates run diffuse then reticulo-nodular, with non caseating granulomas.\n"
        "The etiology table ranks farmer's lung (most common, moldy hay), bagassosis (second, moldy sugarcane) and mushroom worker's lung under Thermoactinomyces vulgaris (most common antigen); compost, tobacco worker's, malt worker's and cheese washer's lung under Aspergillus clavatus; hot tub/humidifier lung under Cladosporium and MAC; bird fancier's lung under avian droppings; wood trimmer's under Rhizopus; familial HP under Bacillus subtilis from wood pulp; and chemical worker's lung to polyurethane isocyanate, with the table's blank source and antigen cells preserved.",
    ),
    S2: (
        "Acute, Subacute and Chronic Presentations, Complications, Non-Caseating Granuloma and Emphysema Notes, Precipitins and BAL CD8/CD4",
        "Acute HP (p258) is self-resolving fever, chills and cough with raised ESR settling in 2–4 days; subacute HP is the most common tempo, with gradually progressive dyspnea, cough and fatiguability, no systemic features and upper lobe involvement; chronic HP can fibrose into ILD.\n"
        "Bird fancier's lung rarely fibroses while farmer's lung turns emphysematous, and the notes list non-caseating granulomas in HP, 30% of TB as printed, lymphoma, sarcoidosis, cat scratch disease, Crohn's disease and berylliosis, and non-COPD emphysema in farmer's lung, COP and rarely coal worker's pneumoconiosis.\n"
        "Serum precipitins may be positive non-specifically through the type III component, and BAL shows lymphocytosis with CD8/CD4 above 2.",
    ),
    S3: (
        "PFT, CXR and CT in HP with the Head Cheese Pattern, Steroid Response versus Irreversible Fibrosis, and the HP versus ABPA Difference Table",
        "Chronic HP restricts on PFT (p259), the CXR evolves from diffuse opacities to reticulonodular shadows ('CXR infiltrates in acute HP'), and CT shows centrilobular nodules, bilateral GGO and mosaic or head-cheese attenuation of varying densities, captioned as bilateral GGO with nodular opacity and mosaic tiles in HP.\n"
        "Sarcoidosis mirrors the lavage with CD4/CD8 above 2, subacute HP responds to steroids, and established fibrosis is irreversible.\n"
        "Against ABPA, HP shows granulomatous lymphocytic (IV > III) pathology, reticulonodular radiology, clavatus skin positivity, no eosinophilia and normal IgE, sharing only the type III IgG precipitins — ABPA instead colonises airways eosinophilically (I + III) with migratory bronchiectatic infiltrates, fumigatus positivity, eosinophilia and markedly raised IgE.",
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
