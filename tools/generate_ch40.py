#!/usr/bin/env python3
"""Generate Chapter 40: Bronchial Asthma (Book p243–248).

Every question is anchored to a printed line, table cell or flowchart terminal of
uploads/02.pdf sheets 126–130 and uploads/03.pdf sheet 1 (Book pages 243–248), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 40
TITLE = "Bronchial Asthma"
PAGES = "243-248"

S1 = "General Features of Asthma, the Bronchodilator Reversibility Box, GINA Features and Respiratory Symptoms with Triggers"
S2 = "Etiopathogenesis: Triggers, Hygiene Hypothesis and TH2 Cytokines, Early versus Late Phases, and Eosinophil Mediators and Granules"
S3 = "Histopathology of Asthma with Curschmann Spirals, the Extrinsic versus Intrinsic Table and Samter's Triad"
S4 = "Mild versus Moderate versus Severe Asthma Table and Acute Severe Exacerbation versus Impending Respiratory Failure"
S5 = "Management: Inhaled Corticosteroids as Mainstay, the ICS–Formoterol Step Protocol with Biologics, and Investigations"
S6 = "Management of Asthma Exacerbation in the ER and Brittle Asthma Types One and Two"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(40000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(40100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p243
add(
    S1, 243, "recall",
    "Which five features of Asthma head the chapter on page 243?",
    "Pure airway disease; no parenchymal involvement, so no hypercapnia, pulmonary HTN or cor-pulmonale; chronic; inflammatory (eosinophils); and reversible bronchoconstriction",
    [
        "Pure airway disease; parenchymal involvement, so hypercapnia and cor-pulmonale; chronic; inflammatory (eosinophils); and reversible bronchoconstriction",
        "Pure parenchymal disease; no parenchymal involvement, so no hypercapnia, pulmonary HTN or cor-pulmonale; acute; inflammatory (neutrophils); and reversible bronchoconstriction",
        "Pure airway disease; no parenchymal involvement, so no hypercapnia, pulmonary HTN or cor-pulmonale; chronic; inflammatory (eosinophils); and irreversible bronchoconstriction",
    ],
    "The bullets read 'Pure airway disease', 'No parenchymal involvement → No hypercapnia, pulmonary HTN, cor-pulmonale', 'Chronic', 'Inflammatory (Eosinophils)' and 'Reversible bronchoconstriction', echoing the asthma exception in the Type I table on page 230.",
)

add(
    S1, 243, "numeric",
    "Which numbers does the bronchodilator reversibility box print on page 243?",
    "Four puffs of SABA, reassessed at 30 minutes, with FEV1 rising by 12% plus a 200 ml rise in absolute value",
    [
        "Two puffs of SABA, reassessed at 15 minutes, with FEV1 rising by 12% plus a 200 ml rise in absolute value",
        "Four puffs of SABA, reassessed at 30 minutes, with FEV1 rising by 15% plus a 250 ml rise in absolute value",
        "Four puffs of LABA, reassessed at 30 minutes, with FEV1 rising by 12% plus a 200 ml rise in absolute value",
    ],
    "The box reads 'On bronchodilator reversibility testing: (4 puffs of SABA) — 30 mins — FEV1: ↑ by 12% + 200 ml ↑ in absolute value.' Both the percentage and the absolute rise must be met.",
)

add(
    S1, 243, "match",
    "Match each reversibility result in the page 243 box with its printed label — 1) Rise present, marked plus 2) Rise absent, marked minus … A) Irreversible, labelled COPD B) Reversible, labelled Asthma",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "The box splits into '+' leading to 'Reversible (Asthma)' and '−' leading to 'Irreversible (COPD)'. The same 12% and 200 ml rule separated asthma from COPD on page 199.",
)

add(
    S1, 243, "recall",
    "Which three components are stacked as the GINA features of Asthma on page 243?",
    "Chronic airway inflammation with reversible bronchoconstriction, plus variable expiratory air-flow obstruction, plus symptoms due to broncho-constriction",
    [
        "Chronic airway inflammation with irreversible bronchoconstriction, plus fixed expiratory air-flow obstruction, plus symptoms due to broncho-constriction",
        "Acute airway inflammation with reversible bronchoconstriction, plus variable inspiratory air-flow obstruction, plus symptoms due to broncho-constriction",
        "Chronic airway inflammation with reversible bronchoconstriction, plus variable expiratory air-flow obstruction, plus parenchymal destruction",
    ],
    "Under 'GINA (Global initiative for Asthma) features of asthma' the page stacks chronic airway inflammation with reversible bronchoconstriction, variable expiratory air-flow obstruction and symptoms due to broncho-constriction, joined by plus signs.",
)

add(
    S1, 243, "fillup",
    "The four symptoms printed as due to broncho-constriction are shortness of breath, chronic cough, wheeze and ______.",
    "chest tightness",
    ["chest pain", "hemoptysis", "stridor"],
    "The bracket reads '(Shortness of breath/chronic cough/wheeze/chest tightness)'. Chest tightness, not pleuritic chest pain, is the fourth GINA symptom printed here.",
)

add(
    S1, 243, "recall",
    "How do the respiratory symptoms of Asthma behave, according to the foot of page 243?",
    "They are variable in time and intensity, worse at night and with viral infections (RSV most common)",
    [
        "They are fixed in time and intensity, worse in the morning and with viral infections (RSV most common)",
        "They are variable in time and intensity, worse at night and with bacterial infections (pneumococcus most common)",
        "They are variable in time and intensity, worse at night and with viral infections (influenza most common as printed)",
    ],
    "The bullets read 'variable in time and intensity' and 'worse: At night. With viral infections (RSV: m/c).' RSV is the organism named in brackets.",
)

add(
    S1, 243, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed triggers of Asthma symptoms on page 243, one appears only in the next day's trigger list on page 244:",
    "Paint fumes",
    [
        "Exercise",
        "Laughter",
        "Cold air",
    ],
    "Page 243 closes with 'Triggers: Exercise, laughter, allergens, cold air.' Paint fumes belongs to the separate etiopathogenesis trigger list on page 244, alongside sulfur dioxide and beta blockers.",
)

add(
    S1, 243, "scenario",
    "A patient's FEV1 rises 14% and 240 ml thirty minutes after four puffs of SABA. Using the page 243 box alone, how is this labelled?",
    "Reversible — labelled Asthma",
    [
        "Irreversible — labelled COPD",
        "Reversible — labelled COPD",
        "Indeterminate, because only the percentage criterion is printed",
    ],
    "Both printed thresholds are exceeded (12% and 200 ml in absolute value at 30 minutes after 4 puffs of SABA), so the '+' arm applies: 'Reversible (Asthma)'. A sub-threshold rise would take the '−' arm to COPD.",
)


# ---------------------------------------------------------------- Unit 2: p244
add(
    S2, 244, "recall",
    "What etiology and trigger list open the etiopathogenesis on page 244?",
    "Etiology unknown; triggers upper respiratory infection (URI), aspirin, beta blockers, sulfur dioxide, paint fumes, obesity, diet, 5q polymorphism and hyperventilation",
    [
        "Etiology unknown; triggers upper respiratory infection (URI), aspirin, beta blockers, sulfur dioxide, paint fumes, obesity, diet, 17q polymorphism and hypoventilation",
        "Etiology allergic; triggers upper respiratory infection (URI), aspirin, beta agonists, sulfur dioxide, paint fumes, obesity, diet, 5q polymorphism and hyperventilation",
        "Etiology unknown; triggers lower respiratory infection, aspirin, beta blockers, carbon dioxide, paint fumes, obesity, diet, 5q polymorphism and hyperventilation",
    ],
    "The section reads 'Etiology: unknown' and lists triggers in two columns: URI, aspirin, beta blockers, sulfur dioxide, paint fumes, and obesity, diet, 5q polymorphism, hyperventilation. Beta blockers, not agonists, are the drug trigger.",
)

add(
    S2, 244, "recall",
    "Which chain states the hygiene hypothesis on page 244?",
    "Increased exposure to antigens in childhood promotes conversion of TH2 to TH1 cells, giving better immunity",
    [
        "Decreased exposure to antigens in childhood promotes conversion of TH2 to TH1 cells, giving better immunity",
        "Increased exposure to antigens in childhood promotes conversion of TH1 to TH2 cells, giving better immunity",
        "Increased exposure to antigens in adulthood promotes conversion of TH2 to TH1 cells, giving better immunity",
    ],
    "The bullet reads '↑ exposure to antigens in childhood → Promotes conversion of TH2 to TH1 cells → Better immunity.' The conversion runs away from the TH2 phenotype that drives Asthma.",
)

add(
    S2, 244, "match",
    "Match each TH2 product on page 244 with its printed action — 1) IL-4 2) IL-5 3) IL-13 … A) Listed with no action printed against it B) Recruits eosinophils via eotaxin C) Raises IgE",
    "1-C, 2-B, 3-A",
    ["1-B, 2-C, 3-A", "1-C, 2-A, 3-B", "1-A, 2-B, 3-C"],
    "Under 'TH2 produces' the page gives 'IL-4: ↑ IgE', 'IL-5: Recruits eosinophils via eotaxin' and 'IL-13' with no action printed. These are the same three cytokines named for eosinophilic inflammation in ABPA on page 254.",
)

add(
    S2, 244, "match",
    "Match each Asthma phase with its printed timing and mediators — 1) Early phase response 2) Late phase … A) After 4–6 hours, mediator listed as basophil B) Mediators histamine, tryptase and PGD2",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "The Phases block pairs the early phase response with mediators histamine, tryptase and PGD2, and the 'Late phase (After 4–6 hrs)' with basophil as its listed mediator entry.",
)

add(
    S2, 244, "truefalse",
    "TRUE or FALSE about the phases printed on page 244.",
    "True — the late phase is timed after 4–6 hours and its mediator entry is the basophil, while histamine, tryptase and PGD2 belong to the early phase",
    [
        "False — the late phase is timed after 24 hours on this page",
        "False — histamine and tryptase are printed as late-phase mediators",
        "True — the early phase mediator entry is the basophil and PGD2 is a late mediator",
    ],
    "The block is explicit: 'Late phase (After 4–6 hrs)' arrows down to 'Basophil', and the early phase column lists histamine, tryptase and PGD2. Swapping either column contradicts the print.",
)

add(
    S2, 244, "recall",
    "Which mediators form the eosinophil's newly synthesised membrane-derived set on page 244?",
    "Leukotriene B4, platelet activating factor, 15 HETE, prostaglandin E1 and E2, and thromboxane B2",
    [
        "Leukotriene B4, platelet activating factor, 15 HETE, prostaglandin D2, and thromboxane A2",
        "Leukotriene C4, platelet activating factor, 15 HETE, prostaglandin E1 and E2, and thromboxane B2",
        "Leukotriene B4, histamine, 15 HETE, prostaglandin E1 and E2, and thromboxane B2",
    ],
    "The upper arrow from the eosinophil diagram reads 'Newly synthesised membrane derived mediators: Leukotriene B4, Platelet activating factor, 15 HETE, Prostaglandin E1, E2, Thromboxane B2.' PGD2 was an early-phase mediator in the block above.",
)

add(
    S2, 244, "recall",
    "Which four granule-derived basic proteins are listed from the eosinophil diagram?",
    "Major basic protein (MBP), eosinophil cationic protein (ECP), eosinophil derived neurotoxin (EDN) and eosinophil peroxidase (EPO)",
    [
        "Major basic protein (MBP), eosinophil cationic protein (ECP), eosinophil derived neurotoxin (EDN) and Charcot Leyden protein",
        "Minor basic protein (MBP), eosinophil cationic protein (ECP), eosinophil derived neurotoxin (EDN) and eosinophil peroxidase (EPO)",
        "Major basic protein (MBP), eosinophil anionic protein (ECP), eosinophil derived neurotoxin (EDN) and eosinophil peroxidase (EPO)",
    ],
    "The lower arrow reads 'Granule derived basic proteins: major basic protein (MBP), Eosinophil cationic protein (ECP), Eosinophil derived neurotoxin (EDN), Eosinophil peroxidase (EPO).' Charcot Leyden material is handled separately as a granule type.",
)

add(
    S2, 244, "fillup",
    "Of the two granule types in eosinophils, the 1° (primary) granules give ______, while the 2° granules contain MBP, ECP and EDN.",
    "Charcot Leyden crystals",
    ["Curschmann spirals", "Masson's buds", "Birbeck granules"],
    "The side box reads '1° granules: Charcot Leyden crystals. 2° granules: MBP, ECP, EDN.' Curschmann spirals are a histopathology finding on the next page, not a granule product here.",
)


# ---------------------------------------------------------------- Unit 3: p245
add(
    S3, 245, "recall",
    "Which four numbered headings make up the histopathology of Asthma on page 245?",
    "Chronic airway inflammation; bronchial smooth muscle hypertrophy; submucosal glandular (goblet cell) hyperplasia; and patchy necrosis of epithelium",
    [
        "Chronic airway inflammation; bronchial smooth muscle atrophy; submucosal glandular (goblet cell) hyperplasia; and diffuse necrosis of epithelium",
        "Acute airway inflammation; bronchial smooth muscle hypertrophy; submucosal glandular (goblet cell) hypoplasia; and patchy necrosis of epithelium",
        "Chronic airway inflammation; bronchial cartilage hypertrophy; submucosal glandular (goblet cell) hyperplasia; and patchy necrosis of endothelium",
    ],
    "The numbered list reads '1. Chronic airway inflammation, 2. Bronchial smooth muscle hypertrophy, 3. Submucosal glandular (Goblet cell) hyperplasia, 4. Patchy necrosis of epithelium.' Muscle hypertrophies and glands hyperplase; the necrosis is patchy and epithelial.",
)

add(
    S3, 245, "recall",
    "Which five elements are listed inside chronic airway inflammation, and which one captions the micrograph?",
    "Eosinophils, mucus plugs, mast cells, Curschmann spirals and Charcot Leyden crystals — with the image captioned Curschmann spirals",
    [
        "Eosinophils, mucus plugs, mast cells, Curschmann spirals and Charcot Leyden crystals — with the image captioned Charcot Leyden crystals",
        "Neutrophils, mucus plugs, mast cells, Curschmann spirals and Charcot Leyden crystals — with the image captioned Curschmann spirals",
        "Eosinophils, mucus plugs, basophils, Masson's buds and Charcot Leyden crystals — with the image captioned Curschmann spirals",
    ],
    "Under chronic airway inflammation the bullets are eosinophils, mucus plugs, mast cells, Curschmann spirals and Charcot Leyden crystals, and the red micrograph beside them is captioned 'Curschmann spirals'.",
)

add(
    S3, 245, "match",
    "Match each row of the extrinsic versus intrinsic table with its printed pair — 1) Association with allergy and skin tests 2) Serum IgE 3) Family history 4) Prognosis … A) Extrinsic raised, intrinsic normal B) Extrinsic good with children growing out of Asthma, intrinsic poor C) Extrinsic positive, intrinsic negative D) Extrinsic present, intrinsic absent",
    "1-C, 2-A, 3-D, 4-B",
    ["1-A, 2-C, 3-D, 4-B", "1-C, 2-A, 3-B, 4-D", "1-C, 2-D, 3-A, 4-B"],
    "The table gives extrinsic/atopic Asthma '+' for allergy association and skin tests against '−' for intrinsic, S. IgE '↑' versus 'Normal', family history '+' versus 'Absent', and prognosis 'Good (Children grow out of asthma)' versus 'Poor'.",
)

add(
    S3, 245, "match",
    "Match each remaining table row with its printed extrinsic versus intrinsic pair — 1) Etiology 2) Age of onset 3) Gender predisposition 4) Degree and triggers … A) Childhood onset with peak age 3 years versus adult onset B) Dermatophagoids, the house dust mite, as most common organism versus staphylococcal enterotoxins C) Dashes for extrinsic versus severe persistent degree and respiratory infection triggers for intrinsic D) M equal to F versus M greater than F",
    "1-B, 2-A, 3-D, 4-C",
    ["1-A, 2-B, 3-D, 4-C", "1-B, 2-A, 3-C, 4-D", "1-B, 2-D, 3-A, 4-C"],
    "Etiology pairs 'm/c organism: Dermatophagoids (House dust mite)' with 'Staphylococcal enterotoxins'; onset pairs childhood (peak 3 yrs) with adult; gender pairs 'm = F' with 'm > F'; and the degree and trigger rows carry dashes for extrinsic against 'Severe, persistent' and 'Respiratory infections' for intrinsic.",
)

add(
    S3, 245, "numeric",
    "Which single age figure is printed anywhere in the extrinsic versus intrinsic table?",
    "Peak age 3 years, attached to childhood-onset extrinsic/atopic Asthma",
    [
        "Peak age 13 years, attached to childhood-onset extrinsic/atopic Asthma",
        "Peak age 3 years, attached to adult-onset intrinsic Asthma",
        "Peak age 30 years, attached to childhood-onset extrinsic/atopic Asthma",
    ],
    "The age-of-onset cell reads 'Childhood onset (Peak age: 3 yrs)' for extrinsic/atopic Asthma against 'Adult onset' for intrinsic Asthma. Three years is the table's only age.",
)

add(
    S3, 245, "scenario",
    "An adult man with no family history, normal serum IgE, negative skin tests and severe persistent Asthma triggered by respiratory infections is discussed. Which column of the page 245 table does he fill, and what prognosis does it carry?",
    "Intrinsic Asthma — prognosis poor",
    [
        "Extrinsic/atopic Asthma — prognosis good, as children grow out of Asthma",
        "Intrinsic Asthma — prognosis good, as children grow out of Asthma",
        "Extrinsic/atopic Asthma — prognosis poor",
    ],
    "Adult onset, absent family history, normal IgE, negative skin tests, male predominance, severe persistent degree and respiratory-infection triggers are the intrinsic column cell by cell, whose prognosis row reads 'Poor'.",
)

add(
    S3, 245, "oddoneout",
    "Pick the ODD ONE OUT — three of these form the captioned triangle at the foot of page 245, one does not:",
    "Childhood onset Asthma",
    [
        "Adult onset Asthma",
        "Aspirin sensitivity",
        "Nasal polyps",
    ],
    "The Note 'Samters triad' (as printed) draws a triangle of adult onset Asthma at the apex with aspirin sensitivity and nasal polyps at the base corners. Childhood onset belongs to extrinsic Asthma in the table above.",
)

add(
    S3, 245, "fillup",
    "The triangle of adult onset Asthma, aspirin sensitivity and nasal polyps is labelled ______ triad (spelling as printed).",
    "Samters",
    ["Kartagener's", "Widal's printed as Vidal's", "Virchow's"],
    "The Note is headed 'Samters triad', without an apostrophe, exactly as printed on page 245. Aspirin also appears as a trigger on page 244, tying the triad back to the etiopathogenesis list.",
)


# ---------------------------------------------------------------- Unit 4: p246
add(
    S4, 246, "recall",
    "Which symptom-pattern scheme introduces the severity grading on page 246?",
    "Asthma with intermittent symptoms stands apart, while Asthma with persistent symptoms grades into mild, moderate and severe",
    [
        "Asthma with persistent symptoms stands apart, while Asthma with intermittent symptoms grades into mild, moderate and severe",
        "Asthma with intermittent symptoms grades into mild and moderate only, while severe Asthma is separately defined",
        "Asthma with nocturnal symptoms grades into mild, moderate and severe",
    ],
    "Under 'B. mild v/s moderate v/s severe' the arrows read 'Asthma with → Intermittent symptoms' and '→ Persistent symptoms → mild, moderate, Severe'. The three grades subdivide persistent disease only.",
)

add(
    S4, 246, "numeric",
    "Reading the severity table by column position (mild, then moderate, then severe), which day-symptom and FEV1 ladder is printed?",
    "Day symptoms 2–6 days/week, then daily, then continuous; FEV1 above 80% predicted, then 60–80% predicted, then below 60% predicted",
    [
        "Day symptoms daily, then 2–6 days/week, then continuous; FEV1 above 80% predicted, then 60–80% predicted, then below 60% predicted",
        "Day symptoms 2–6 days/week, then daily, then continuous; FEV1 below 60% predicted, then 60–80% predicted, then above 80% predicted",
        "Day symptoms 2–6 days/week, then continuous, then daily; FEV1 above 80% predicted, then below 60% predicted, then 60–80% predicted",
    ],
    "The columns run '2–6 days/week, Daily, Continuous' for day symptoms and '>80% predicted, 60–80% predicted, <60% predicted' for FEV1. Note the print carries over the headers 'Extrinsic/atopic' and 'Intrinsic' from page 245 over the moderate and severe columns, so the grades are read by position under the 'mild v/s moderate v/s severe' heading.",
)

add(
    S4, 246, "numeric",
    "Which nocturnal-awakening and PEFR-variability cells complete that table?",
    "Nocturnal awakenings more than 2 monthly, then more than 1 per week, then 'Significantly ↓ activity' as printed in the third cell; PEFR variability below 30%, then above 30%, then above 30%",
    [
        "Nocturnal awakenings more than 2 weekly, then more than 1 monthly, then nightly; PEFR variability below 30%, then above 30%, then above 30%",
        "Nocturnal awakenings more than 2 monthly, then more than 1 per week, then 'Significantly ↓ activity' as printed in the third cell; PEFR variability above 30%, then below 30%, then below 30%",
        "Nocturnal awakenings more than 2 monthly, then more than 1 per week, then frequent; PEFR variability below 30%, then above 30%, then below 30%",
    ],
    "The rows read '>2 monthly, >1/week, Significantly ↓ activity' for nocturnal awakenings — the third cell describing activity rather than awakenings, preserved as printed — and '<30%, >30%, >30%' for PEFR variability.",
)

add(
    S4, 246, "match",
    "Match each bedside row with its acute-exacerbation versus impending-failure pair on page 246 — 1) Speech 2) Orientation 3) Position 4) Accessory muscle use and loud wheeze … A) Upright versus cannot recline B) Both marked ++ in exacerbation versus paradoxical breathing and a silent chest in impending failure C) Words versus absent D) Agitated versus confused",
    "1-C, 2-D, 3-A, 4-B",
    ["1-D, 2-C, 3-A, 4-B", "1-C, 2-D, 3-B, 4-A", "1-C, 2-A, 3-D, 4-B"],
    "In acute exacerbation speech is in 'Words', orientation 'Agitated', position 'upright', and accessory muscle use and loud wheeze are '++'; in impending respiratory failure speech is 'Absent', orientation 'Confused', position 'Cant recline', accessory use becomes 'Paradoxical breathing' and wheeze is '− (Silent chest)'. Breathlessness at rest and tachypnoea carry a merged '+' across both columns.",
)

add(
    S4, 246, "match",
    "Match each physiological row with its printed pair in the same table — 1) Heart rate 2) Pulsus paradoxus 3) PEFR 4) PaO2 and PaCO2 … A) 25–40 L/min as printed versus below 25 L/min B) Marked ++ versus absent C) Merged cells across both columns: PaO2 below 60 mmHg (saturation below 90%) and PaCO2 below 40 mmHg D) Tachycardia versus relative bradycardia",
    "1-D, 2-B, 3-A, 4-C",
    ["1-B, 2-D, 3-A, 4-C", "1-D, 2-B, 3-C, 4-A", "1-D, 2-A, 3-B, 4-C"],
    "Heart rate moves from tachycardia to relative bradycardia and pulsus paradoxus from '++' to absent as failure impends; PEFR falls from '25–40 L/min' to '<25 L/min' (units as printed), while PaO2 '<60 mmHg (<90%)' and PaCO2 '<40 mmHg' are merged across both columns.",
)

add(
    S4, 246, "scenario",
    "A breathless asthmatic can no longer speak, is confused, cannot recline, has paradoxical breathing, a silent chest, relative bradycardia and no pulsus paradoxus, with PEFR under the lower printed band. Which column has he crossed into?",
    "Impending respiratory failure",
    [
        "Acute exacerbation of Asthma",
        "Mild persistent Asthma",
        "Intermittent Asthma",
    ],
    "Absent speech, confusion, inability to recline, paradoxical breathing, silent chest, relative bradycardia, absent pulsus paradoxus and PEFR below 25 (printed L/min) are the impending respiratory failure column cell by cell.",
)

add(
    S4, 246, "truefalse",
    "TRUE or FALSE about the merged cells of the exacerbation table on page 246.",
    "True — breathlessness at rest and tachypnoea each carry a single '+' merged across both columns, as do the PaO2 and PaCO2 values",
    [
        "False — breathlessness at rest is printed only under impending respiratory failure",
        "False — PaCO2 is given as above 40 mmHg in impending failure",
        "True — loud wheeze is also merged across both columns with a single '++'",
    ],
    "The breathlessness-at-rest and tachypnoea rows show one '+' spanning exacerbation and impending failure, and the gas rows merge as PaO2 '<60 mmHg (<90%)' with PaCO2 '<40 mmHg'. Loud wheeze, by contrast, splits '++' against the silent chest.",
)


# ---------------------------------------------------------------- Unit 5: p247
add(
    S5, 247, "recall",
    "Which status, effects and examples are printed for inhaled corticosteroids on page 247?",
    "Mainstay of treatment; effects of reduced hospitalisations, exacerbations and symptoms with improved lung functions, early administration improving future lung function; examples beclomethasone, budesonide and fluticasone",
    [
        "Reliever of choice; effects of reduced hospitalisations, exacerbations and symptoms with improved lung functions; examples beclomethasone, budesonide and fluticasone",
        "Mainstay of treatment; effects of reduced hospitalisations and symptoms only; examples beclomethasone, budesonide and prednisolone",
        "Mainstay of treatment; effects of reduced hospitalisations, exacerbations and symptoms with improved lung functions, early administration improving future lung function; examples salmeterol, budesonide and fluticasone",
    ],
    "The ICS block reads 'mainstay of treatment' with effects '↓ Hospitalisations, ↓ exacerbations, ↓ symptoms, Improved lung functions, early ICS administration → Improved lung function in future' and examples beclomethasone, budesonide and fluticasone. 'ICS' is misprinted once as 'LCS' in the early-administration line, preserved in the caveat record.",
)

add(
    S5, 247, "fillup",
    "Complete the printed Note: Short acting β agonists (SABA) has ______ in persistent Asthma.",
    "no role",
    ["the mainstay role", "a reliever-only role", "an equal role with ICS"],
    "The Note reads 'Short acting β agonists (SABA) has no role in persistent asthma', which is why the protocol below is built entirely on ICS–formoterol combinations.",
)

add(
    S5, 247, "management",
    "Which opening steps does the page 247 protocol print before any dose escalation?",
    "As-and-when-needed ICS–formoterol combination first, then daily low-dose ICS plus formoterol, printed as better than daily low-dose ICS alone",
    [
        "Daily low-dose ICS alone first, then as-and-when-needed ICS–formoterol combination",
        "As-and-when-needed SABA first, then daily low-dose ICS plus formoterol, printed as better than daily low-dose ICS alone",
        "As-and-when-needed ICS–formoterol combination first, then daily low-dose ICS plus salmeterol",
    ],
    "The flowchart opens 'As and when needed ICS-Formoterol combo' and descends to 'Daily low-dose ICS + Formoterol > Daily low dose ICS', the inequality making the combination the preferred daily step.",
)

add(
    S5, 247, "management",
    "A patient remains uncontrolled on daily low-dose ICS–formoterol. Which printed sequence follows?",
    "Medium-dose ICS plus formoterol; if still not responding, high-dose ICS plus formoterol; then add tiotropium, the long-acting muscarinic antagonist",
    [
        "High-dose ICS plus formoterol at once; then add tiotropium, the short-acting muscarinic antagonist",
        "Medium-dose ICS alone; if still not responding, oral steroids; then add tiotropium",
        "Medium-dose ICS plus formoterol; if still not responding, high-dose ICS plus formoterol; then add ipratropium as the long-acting agent",
    ],
    "Two 'Not responding' arrows take the protocol through 'medium-dose ICS + Formoterol' to 'High-dose ICS + Formoterol', and the next step is 'Add Tiotropium (LAMA: Long-acting muscarinic antagonist)'. Ipratropium is the SAMA of the ER chart on page 248.",
)

add(
    S5, 247, "match",
    "Match each biologic at the foot of the protocol with its printed target — 1) Omalizumab 2) Mepolizumab 3) Dupilumab, spelling as printed … A) Anti IL-4 receptor antagonist B) Anti-IgE C) Anti IL-5 receptor antagonist, description as printed",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The biologics read 'Omalizumab (Anti-IgE)', 'mepolizumab (Anti IL-5 receptor antagonist)' and 'Dupilumab (Anti IL-4 receptor antagonist)', offered with a '+/−' after tiotropium. The IL-5-receptor description for mepolizumab and the 'Dupilumab' spelling are preserved as printed.",
)

add(
    S5, 247, "match",
    "Match each investigation on page 247 with its printed purpose and status — 1) Methacholine challenge test 2) Radioallergosorbent test, RAST 3) Fractional exhalation of NO … A) Measures IgE levels, braced as obsolete with its neighbour B) Assesses airway hyperresponsiveness, braced as obsolete with its neighbour C) Non-invasive test to measure airway inflammation",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "Methacholine challenge assesses airway hyperresponsiveness and RAST measures IgE levels, the two sharing the brace 'Obsolete', while fractional exhalation of NO stands below as the non-invasive test of airway inflammation. Methacholine also appeared as the challenge agent on page 191.",
)

add(
    S5, 247, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed ICS examples on page 247, one is a protocol partner drug instead:",
    "Formoterol",
    [
        "Beclomethasone",
        "Budesonide",
        "Fluticasone",
    ],
    "The examples line reads 'Beclomethasone, Budesonide, Fluticasone'. Formoterol is the long-acting bronchodilator combined with ICS in every protocol step, not itself an inhaled corticosteroid.",
)


# ---------------------------------------------------------------- Unit 6: p248
add(
    S6, 248, "recall",
    "Which opening moves does the ER flowchart print before it splits, and what awaits the right-hand arm?",
    "Confirm diagnosis, then determine status; the impending respiratory failure arm goes directly to intubation and ventilation",
    [
        "Determine status, then confirm diagnosis; the impending respiratory failure arm goes directly to intubation and ventilation",
        "Confirm diagnosis, then determine status; the acute severe Asthma arm goes directly to intubation and ventilation",
        "Confirm diagnosis, then give magnesium; the impending respiratory failure arm goes to non-invasive ventilation first",
    ],
    "The chart for 'management of asthma exacerbation in ER' runs 'Confirm diagnosis → Determine status' and forks to acute severe Asthma on the left and 'Impending respiratory failure → Intubation & ventilation' on the right.",
)

add(
    S6, 248, "numeric",
    "Which doses and targets make up the acute severe Asthma arm on page 248?",
    "Nasal O2 to keep SpO2 above 95%; albuterol nebulisations 2.5–5 mg every 20 minutes or 4–8 puffs by MDI every 20 minutes; SAMA ipratropium 500 mg as printed; and 100 mg hydrocortisone",
    [
        "Nasal O2 to keep SpO2 above 90%; albuterol nebulisations 2.5–5 mg every 20 minutes or 4–8 puffs by MDI every 20 minutes; SAMA ipratropium 500 mg as printed; and 100 mg hydrocortisone",
        "Nasal O2 to keep SpO2 above 95%; albuterol nebulisations 5–10 mg hourly; SAMA ipratropium 500 mg as printed; and 200 mg hydrocortisone",
        "Nasal O2 to keep SpO2 above 95%; albuterol nebulisations 2.5–5 mg every 20 minutes or 4–8 puffs by MDI every 20 minutes; LAMA tiotropium; and 100 mg hydrocortisone",
    ],
    "The bullets read 'Nasal O2 to maintain SpO2 >95%', 'Short acting β2 agonist: Albuterol nebulisations 2.5 mg – 5 mg every 20 minutes OR 4–8 puffs by MDI every 20 minutes', 'SAMA: Ipratropium 500 mg' (unit as printed) and '100 mg hydrocortisone'.",
)

add(
    S6, 248, "management",
    "After the first hour the patient is reassessed and is not improving. Which printed ladder follows?",
    "Reassessment uses PEFR and O2 saturation; if not improving, IV MgSO4 2 g over 20 minutes, then non-invasive mechanical ventilation, then intubation and ventilation",
    [
        "Reassessment uses PEFR and PaCO2; if not improving, IV MgSO4 2 g over 20 minutes, then intubation directly with no non-invasive step",
        "Reassessment uses PEFR and O2 saturation; if not improving, oral magnesium, then non-invasive mechanical ventilation, then intubation and ventilation",
        "Reassessment uses speech and orientation; if not improving, IV MgSO4 4 g over 20 minutes, then non-invasive mechanical ventilation, then intubation and ventilation",
    ],
    "The chart prints 'Reassess after 1 hr — PEFR, O2 saturation' and, under 'Not improving', the sequence 'IV MgSO4 2g over 20 mins → Non-invasive mechanical ventilation → Intubation & ventilation'.",
)

add(
    S6, 248, "fillup",
    "The Note under the ER chart defines brittle Asthma in two words as ______ Asthma.",
    "childhood",
    ["occupational", "intrinsic", "nocturnal"],
    "The Note reads 'Brittle asthma: Childhood asthma' before the Type 1 and Type 2 table. Intrinsic Asthma was the adult-onset column on page 245.",
)

add(
    S6, 248, "match",
    "Match each brittle Asthma type with its printed pattern and treatment — 1) Type 1 2) Type 2 … A) Well-controlled Asthma with sudden severe exacerbations, drawn as a single peak, treated with subcutaneous adrenaline B) Wide peak flow variation despite intense medication, drawn as repeated waves, treated with oral corticosteroids",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "Type 1 shows 'wide peak flow variation despite intense medication' over a multi-wave trace with treatment 'Oral corticosteroids', while Type 2 shows 'well-controlled asthma with sudden severe exacerbations' over a single peak with treatment 'S/C adrenaline'.",
)

add(
    S6, 248, "scenario",
    "A child whose Asthma is ordinarily well controlled suffers abrupt, severe attacks out of the blue. Using the page 248 table, which brittle type is she and what is its printed treatment?",
    "Type 2 brittle Asthma — subcutaneous adrenaline",
    [
        "Type 1 brittle Asthma — oral corticosteroids",
        "Type 2 brittle Asthma — oral corticosteroids",
        "Type 1 brittle Asthma — subcutaneous adrenaline",
    ],
    "'Well-controlled asthma with sudden severe exacerbations' is the Type 2 pattern, drawn as one isolated peak, and its treatment cell reads 'S/C adrenaline'. Wide variation despite intense medication would make her Type 1.",
)

add(
    S6, 248, "truefalse",
    "TRUE or FALSE about the ER chart printed on page 248.",
    "True — impending respiratory failure bypasses the drug arm entirely and goes straight to intubation and ventilation, which is also the final step of the not-improving ladder",
    [
        "False — impending respiratory failure first receives albuterol and hydrocortisone for one hour",
        "False — the not-improving ladder ends at non-invasive ventilation with no intubation step",
        "True — acute severe Asthma goes straight to intubation while impending failure receives the drug arm",
    ],
    "The right fork reads 'Impending respiratory failure → Intubation & ventilation' with no drug bullets, and the left arm's not-improving sequence ends at the same 'Intubation & ventilation' after magnesium and non-invasive ventilation.",
)


GUIDES = {
    S1: (
        "General Features of Asthma, the Bronchodilator Reversibility Box, GINA Features and Respiratory Symptoms with Triggers",
        "Asthma (p243) is a pure airway disease without parenchymal involvement — hence no hypercapnia, pulmonary HTN or cor-pulmonale — chronic, eosinophilic-inflammatory and reversibly bronchoconstricting.\n"
        "Reversibility is tested with 4 puffs of SABA read at 30 minutes: an FEV1 rise of 12% plus 200 ml in absolute value is reversible (Asthma), its absence irreversible (COPD).\n"
        "GINA features stack chronic airway inflammation with reversible bronchoconstriction, variable expiratory airflow obstruction and the symptoms shortness of breath, chronic cough, wheeze and chest tightness, which vary in time and intensity, worsen at night and with viral infections (RSV most common), and are triggered by exercise, laughter, allergens and cold air.",
    ),
    S2: (
        "Etiopathogenesis: Triggers, Hygiene Hypothesis and TH2 Cytokines, Early versus Late Phases, and Eosinophil Mediators and Granules",
        "Etiology is unknown (p244); triggers are URI, aspirin, beta blockers, sulfur dioxide, paint fumes, obesity, diet, 5q polymorphism and hyperventilation.\n"
        "The hygiene hypothesis holds that increased childhood antigen exposure converts TH2 to TH1 cells for better immunity; TH2 products are IL-4 (raises IgE), IL-5 (recruits eosinophils via eotaxin) and IL-13, the early phase runs on histamine, tryptase and PGD2, and the late phase after 4–6 hours lists the basophil.\n"
        "Eosinophils release newly synthesised membrane mediators (leukotriene B4, platelet activating factor, 15 HETE, prostaglandin E1/E2, thromboxane B2) and granule basic proteins MBP, ECP, EDN and EPO, with primary granules forming Charcot Leyden crystals and secondary granules holding MBP, ECP and EDN.",
    ),
    S3: (
        "Histopathology of Asthma with Curschmann Spirals, the Extrinsic versus Intrinsic Table and Samter's Triad",
        "Histopathology (p245) numbers chronic airway inflammation (eosinophils, mucus plugs, mast cells, Curschmann spirals — the captioned micrograph — and Charcot Leyden crystals), bronchial smooth muscle hypertrophy, submucosal glandular goblet-cell hyperplasia and patchy epithelial necrosis.\n"
        "Extrinsic/atopic Asthma is allergy-associated with positive skin tests, raised IgE, family history, house dust mite (Dermatophagoids) etiology, childhood onset peaking at 3 years, equal sex ratio and a good prognosis as children grow out of it, against intrinsic Asthma with staphylococcal enterotoxins, adult onset, male predominance, severe persistent disease triggered by respiratory infections and a poor prognosis.\n"
        "The closing Samters triad, as printed, triangles adult onset Asthma, aspirin sensitivity and nasal polyps.",
    ),
    S4: (
        "Mild versus Moderate versus Severe Asthma Table and Acute Severe Exacerbation versus Impending Respiratory Failure",
        "Intermittent Asthma stands apart while persistent Asthma grades mild, moderate and severe (p246): day symptoms 2–6 days/week → daily → continuous, nocturnal awakenings >2 monthly → >1/week → significantly reduced activity as printed, PEFR variability <30% → >30% → >30%, and FEV1 >80% → 60–80% → <60% predicted, under headers that carry over 'Extrinsic/atopic' and 'Intrinsic' from page 245.\n"
        "An acute exacerbation speaks in words, is agitated and upright with ++ accessory use, loud wheeze, tachycardia, ++ pulsus paradoxus and PEFR 25–40 as printed, whereas impending respiratory failure is speechless, confused, unable to recline, with paradoxical breathing, silent chest, relative bradycardia, absent pulsus paradoxus and PEFR below 25.\n"
        "Breathlessness at rest, tachypnoea, PaO2 below 60 mmHg (saturation below 90%) and PaCO2 below 40 mmHg are merged across both columns.",
    ),
    S5: (
        "Management: Inhaled Corticosteroids as Mainstay, the ICS–Formoterol Step Protocol with Biologics, and Investigations",
        "ICS are the mainstay (p247), cutting hospitalisations, exacerbations and symptoms while improving lung function — early use improving future function — with beclomethasone, budesonide and fluticasone as examples, and SABA has no role in persistent Asthma.\n"
        "The protocol steps from as-needed ICS–formoterol to daily low-dose ICS plus formoterol (preferred over ICS alone), then medium- and high-dose ICS plus formoterol for non-responders, then tiotropium (LAMA) with or without biologics omalizumab (anti-IgE), mepolizumab (printed anti-IL-5 receptor antagonist) and dupilumab (printed 'Dupilumab', anti-IL-4 receptor antagonist).\n"
        "Methacholine challenge (airway hyperresponsiveness) and RAST (IgE levels) are braced obsolete, leaving fractional exhaled NO as the non-invasive measure of airway inflammation.",
    ),
    S6: (
        "Management of Asthma Exacerbation in the ER and Brittle Asthma Types One and Two",
        "The ER chart (p248) confirms the diagnosis and determines status: impending respiratory failure goes straight to intubation and ventilation, while acute severe Asthma receives nasal oxygen to SpO2 above 95%, albuterol 2.5–5 mg nebulised or 4–8 MDI puffs every 20 minutes, ipratropium 500 mg as printed and hydrocortisone 100 mg.\n"
        "Reassessment at one hour by PEFR and oxygen saturation escalates the non-improver through IV MgSO4 2 g over 20 minutes and non-invasive ventilation to intubation.\n"
        "Brittle Asthma is childhood Asthma: Type 1 shows wide peak-flow variation despite intense medication (multi-wave trace, oral corticosteroids) and Type 2 sudden severe exacerbations in otherwise well-controlled Asthma (single peak, subcutaneous adrenaline).",
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
