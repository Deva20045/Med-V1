#!/usr/bin/env python3
"""Generate Chapter 50: Added Heart Sounds (Book p303–306).

Every question is anchored to a printed line, table cell or figure caption of
uploads/03.pdf sheets 56–59 (Book pages 303–306), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 50
TITLE = "Added Heart Sounds"
PAGES = "303-306"

S1 = "The Diastolic Continuation from Protodiastole to Atrial Systole, the O-P-Time-S3-S4 Sequence, Early, Mid and Late Diastolic Position, and S3 with Its Three Mechanisms and Four Valve Lesions"
S2 = "S3 Features with Left Lateral Position, Leg Raising and the Heart-Failure Caveat, the Pericardial Knock of Constrictive Pericarditis, and S4 with Its Four Prerequisites and Its Valve-Disease Table"
S3 = "The Three S4 Settings, the Opening Snap in Mitral Stenosis with Its S2-OS Interval Ladder and Auscultation Rules, and the Low Pitched Tumour Plop of Atrial Myxoma"
S4 = "Systolic Added Sounds as Clicks, the Valvular and Vascular Ejection Clicks with Their S2 and S1 Rules, and the Non-Ejection Click of Mitral Valve Prolapse with Dynamic Auscultation"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(50000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(50100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p303
add(
    S1, 303, "recall",
    "Which sequence continues the cardiac cycle at the top of page 303?",
    "Protodiastole → semilunar valves closed → isovolumetric relaxation → AV valves open → rapid filling → reduced filling → atrial systole",
    [
        "Protodiastole → semilunar valves open → isovolumetric contraction → AV valves open → rapid filling → reduced filling → atrial systole",
        "Protodiastole → semilunar valves closed → isovolumetric relaxation → AV valves closed → rapid filling → reduced filling → atrial systole",
        "Protodiastole → AV valves closed → isovolumetric relaxation → semilunar valves open → rapid filling → reduced filling → atrial systole",
    ],
    "The row reads protodiastole, semilunar valves closed, isovolumetric relaxation, AV valves open, rapid filling, reduced filling and atrial systole, with 70% passive and 30% active filling bracketed beneath.",
)

add(
    S1, 303, "numeric",
    "Which filling percentages are printed beneath the rapid and atrial phases on page 303?",
    "70% filling (passive) and 30% filling (active)",
    [
        "30% filling (passive) and 70% filling (active)",
        "50% filling (passive) and 50% filling (active)",
        "70% filling (passive) and 40% filling (active)",
    ],
    "The brackets read '70% filling (Passive)' under rapid and reduced filling and '30% filling (Active)' under atrial systole.",
)

add(
    S1, 303, "match",
    "Match each diastolic sound to its printed position — 1) Opening snap, pericardial knock and tumour plop 2) S3 3) S4 … A) Late diastolic B) Early diastolic sounds C) Mid diastolic",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The sequence line places opening snap (O), pericardial knock (P) and tumour plop together as early diastolic sounds, S3 as mid diastolic and S4 as late diastolic.",
)

add(
    S1, 303, "fillup",
    "The three low pitched added sounds printed on page 303 are S3, S4 and ______.",
    "tumor plop",
    ["opening snap", "ejection click", "pericardial knock"],
    "The line reads 'Low pitched sounds: S3, S4 & tumor plop', separating them from the higher-pitched opening snap and knock discussed later.",
)

add(
    S1, 303, "recall",
    "Which other names are printed for S3, and in which phase is it seen?",
    "Ventricular or protodiastolic gallop rhythm, seen in the rapid filling phase",
    [
        "Atrial or presystolic gallop rhythm, seen in atrial systole",
        "Ventricular or presystolic gallop rhythm, seen in the reduced filling phase",
        "Atrial or protodiastolic gallop rhythm, seen in the rapid filling phase",
    ],
    "The S3 block reads 'AKA ventricular/protodiastolic gallop rhythm' and 'Seen in rapid filling phase', with the pre-requisite of a non-stenosed AV valve.",
)

add(
    S1, 303, "recall",
    "What is the pre-requisite for S3, and which two valve lesions are therefore excluded?",
    "A non-stenosed AV valve, excluding MS and TS",
    [
        "A stenosed AV valve, excluding MR and AR",
        "A non-stenosed semilunar valve, excluding AS and PS",
        "A non-stenosed AV valve, excluding MR and AR",
    ],
    "The line reads 'Pre-requisite: Non-stenosed AV valve (Not seen in MS & TS)', the stenotic valve preventing the rapid filling that generates S3.",
)

add(
    S1, 303, "match",
    "Match each S3 mechanism to its printed setting — 1) Physiological 2) Increased end systolic volume 3) Less than normal filling … A) LVH, RVH and RCMP B) Young people, athletes and hyperkinetic states C) LV or RV failure",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "The three arms read physiological excessive rapid filling into a hypercompliant ventricle across a normal AV valve in the young, athletes and hyperkinetic states; increased end systolic volume seen in LV/RV failure, the commonest setting; and less than normal filling of a hypertrophic non-compliant ventricle in LVH, RVH and RCMP.",
)

add(
    S1, 303, "recall",
    "How does the timing of a pathological S3 compare with a physiological S3, and which valve lesions produce S3?",
    "Pathological S3 occurs earlier than physiological S3; it is heard in MR with or without LVF and in severe AS from LVH, but not in MS or AR with LVF",
    [
        "Pathological S3 occurs later than physiological S3; it is heard in MR with or without LVF and in severe AS from LVH, but not in MS or AR with LVF",
        "Pathological S3 occurs earlier than physiological S3; it is heard in MS and AR, but not in MR or AS",
        "Pathological S3 occurs earlier than physiological S3; it is heard only in MS and TS",
    ],
    "The line reads 'Pathological S3 occurs earlier than physiological S3', and the valvular diagram prints MR heard with or without LVF, AS seen in severe AS, MS not seen and AR not seen except with LVF.",
)

add(
    S1, 303, "oddoneout",
    "Pick the ODD ONE OUT — three statements about S3 on page 303 are printed, one contradicts the page:",
    "S3 is a high pitched early systolic sound heard with the diaphragm",
    [
        "S3 is also called the ventricular or protodiastolic gallop",
        "S3 is seen in the rapid filling phase",
        "S3 is not seen in mitral stenosis or tricuspid stenosis",
    ],
    "S3 is a low pitched sound (the page lists it with S4 and tumour plop), occurs in the rapid filling phase, is a protodiastolic gallop and is excluded by a stenosed AV valve; nothing on the page makes it high pitched or systolic.",
)

# ---------------------------------------------------------------- Unit 2: p304
add(
    S2, 304, "recall",
    "How and where is S3 auscultated, and how does posture change it?",
    "In the left lateral position at the apex; it does not vary with respiration, and a physiological S3 disappears in the upright position",
    [
        "In the supine position at the apex; it varies with respiration, and a physiological S3 appears only in the upright position",
        "In the left lateral position at the apex; it varies with inspiration, and a physiological S3 disappears in the upright position",
        "In the left lateral position at the lower left sternal border; it does not vary with respiration, and a pathological S3 disappears upright",
    ],
    "The features read 'Auscultated in: Left lateral position; At the apex', 'Does not vary with respiration' and 'Physiological S3 disappears in upright position'.",
)

add(
    S2, 304, "recall",
    "What does passive leg raising do, and why is it performed?",
    "It augments venous return so that S3 is heard even if it was not heard in the left lateral position",
    [
        "It reduces venous return so that S3 disappears even if it was heard in the left lateral position",
        "It augments venous return so that a pericardial knock appears in constrictive pericarditis",
        "It increases heart rate so that a fourth sound appears in sinus rhythm",
    ],
    "The arrow reads 'Passive leg raising: Augments venous return → S3 heard even if not heard in left lateral', a bedside trick to unmask the sound.",
)

add(
    S2, 304, "recall",
    "Which three conditions are printed as heart failure without S3?",
    "MS, TS and pericardial tamponade",
    [
        "MS, MR and pericardial tamponade",
        "MS, TS and constrictive pericarditis",
        "AS, AR and pericardial tamponade",
    ],
    "The note reads 'Heart failure without S3 → MS, TS, pericardial tamponade', the same stenotic-pair logic that excludes S3 at the valve.",
)

add(
    S2, 304, "recall",
    "Which disease produces a pericardial knock, and what is its printed mechanism?",
    "Chronic constrictive pericarditis, where the rock-like pericardium structurally restricts diastolic filling by the pericardial shell",
    [
        "Acute pericarditis, where the inflamed pericardium structurally restricts diastolic filling by the pericardial shell",
        "Chronic constrictive pericarditis, where the pericardium is thin and offers no resistance to filling",
        "Pericardial tamponade, where the pericardial fluid restricts systolic ejection",
    ],
    "The knock block reads 'Seen in chronic constrictive pericarditis', with the mechanism 'Constrictive pericarditis → Rock-like pericarditis → Structural restriction of diastolic filling by pericardial shell'.",
)

add(
    S2, 304, "match",
    "Match each pericardial knock feature to what it is printed to do — 1) High pitched and louder with inspiration 2) Early diastolic timing 3) Disappears after pericardiectomy … A) Distinguishes it from S3 B) Confirms the pericardial origin C) Places it in early diastole",
    "1-A, 2-C, 3-B",
    ["1-B, 2-C, 3-A", "1-A, 2-B, 3-C", "1-C, 2-A, 3-B"],
    "The knock features are high pitched and louder with inspiration, bracketed 'To differentiate from S3'; early diastolic sound; and 'Disappears following pericardiectomy', which proves the pericardial source.",
)

add(
    S2, 304, "recall",
    "Which other name and phase are printed for S4, and with which venous wave does it correlate?",
    "Atrial or presystolic gallop, seen in atrial systole and correlating with the A-wave in the JVP",
    [
        "Ventricular or presystolic gallop, seen in atrial systole and correlating with the V-wave in the JVP",
        "Atrial or protodiastolic gallop, seen in rapid filling and correlating with the A-wave in the JVP",
        "Atrial or presystolic gallop, seen in atrial systole and correlating with the C-wave in the JVP",
    ],
    "The S4 block reads 'AKA atrial/presystolic gallop', 'Seen in atrial systole' and 'Correlates with A-wave in JVP'.",
)

add(
    S2, 304, "match",
    "Match each S4 prerequisite to its printed wording — 1) Atrium 2) Contraction 3) AV valve 4) Ventricle … A) Across a non stenosed A-V valve B) Healthy atria in sinus rhythm C) Into a non-dilated ± hypertrophic and non-compliant ventricle D) Contracting vigorously",
    "1-B, 2-D, 3-A, 4-C",
    ["1-B, 2-A, 3-D, 4-C", "1-D, 2-B, 3-A, 4-C", "1-B, 2-D, 3-C, 4-A"],
    "The prerequisites read healthy atria in sinus rhythm, contracting vigorously, across a non stenosed A-V valve, into a non-dilated ± hypertrophic and non-compliant ventricle.",
)

add(
    S2, 304, "recall",
    "Which mechanism is printed for S4, and which valve lesions make it disappear or appear?",
    "Atrial contraction increases LV end-diastolic fibre length; it is not seen in MS, MR or AR, but is heard in AS",
    [
        "Atrial contraction decreases LV end-diastolic fibre length; it is not seen in MS, MR or AR, but is heard in AS",
        "Atrial contraction increases LV end-diastolic fibre length; it is not seen in AS, MR or AR, but is heard in MS",
        "Ventricular contraction increases LV end-diastolic fibre length; it is not seen in MS, MR or AR, but is heard in AS",
    ],
    "The mechanism arrow reads 'Atrial contraction → ↑ LV end-diastolic fibre length', and the valvular list prints MS, MR and AR as not seen with AS heard, adding that it is heard in acute MR and AR.",
)

add(
    S2, 304, "match",
    "Match each valve lesion to its printed S3 and S4 cells — 1) AS 2) AR 3) MS 4) MR … A) S3 absent and S4 absent B) S3 present and S4 present C) S3 present in failure and S4 absent D) S3 present and S4 absent",
    "1-B, 2-C, 3-A, 4-D",
    ["1-B, 2-D, 3-A, 4-C", "1-A, 2-C, 3-B, 4-D", "1-B, 2-C, 3-D, 4-A"],
    "The table reads AS +/+, AR in failure/–, MS –/– and MR +/– for S3 and S4 respectively.",
)

add(
    S2, 304, "fillup",
    "The note beneath the S3/S4 table states that both added sounds are heard in acute ______.",
    "MR and AR",
    ["MS and TS", "AS and PS", "MR and MS"],
    "The note reads 'Note: Heard in acute MR & AR', a caveat that overrides the chronic valve-disease cells in the table above.",
)

# ---------------------------------------------------------------- Unit 3: p305
add(
    S3, 305, "match",
    "Match each setting of S4 to its printed examples — 1) Concentric LVH 2) Concentric RVH 3) RV ischaemia … A) Coronary artery disease B) Pulmonary stenosis, PAH and RCM C) Systemic HTN and HCM",
    "1-C, 2-B, 3-A",
    ["1-B, 2-C, 3-A", "1-C, 2-A, 3-B", "1-A, 2-B, 3-C"],
    "The three arms read concentric LVH with systemic HTN and HCM, concentric RVH with pulmonary stenosis, PAH and RCM, and RV ischaemia from coronary artery disease.",
)

add(
    S3, 305, "recall",
    "What does the opening snap represent, and which valve event produces it?",
    "It is produced by opening of the AV valve and represents isovolumetric relaxation",
    [
        "It is produced by closure of the AV valve and represents isovolumetric contraction",
        "It is produced by opening of the semilunar valve and represents rapid ejection",
        "It is produced by closure of the semilunar valve and represents protodiastole",
    ],
    "The opening snap block reads 'Sound produced by opening of the A-V valve' and 'Represents isovolumetric relaxation'.",
)

add(
    S3, 305, "recall",
    "How is the opening snap auscultated, and what are its printed prerequisites?",
    "With the bell at the apex in expiration, requiring mobile leaflets, good LV function, primary organic MS and MS as the predominant lesion",
    [
        "With the diaphragm at the apex in inspiration, requiring calcified leaflets, poor LV function and MS as the predominant lesion",
        "With the bell at the lower left sternal border in expiration, requiring mobile leaflets, poor LV function and any degree of MS",
        "With the bell at the apex in expiration, requiring mobile leaflets, good LV function and any degree of MS even if another lesion predominates",
    ],
    "The auscultation block reads bell, apex and expiration; the prerequisites read mobile leaflets, good LV function, 1° MS (organic) and 'ms should be pre-dominant lesion'.",
)

add(
    S3, 305, "recall",
    "Which mechanism produces the opening snap in mitral stenosis?",
    "A raised left atrial pressure with thickened leaflets causes a sudden doming motion of the valves into the LV",
    [
        "A raised left atrial pressure with thinned leaflets causes a gradual doming motion of the valves into the LV",
        "A raised left ventricular pressure with thickened leaflets causes a sudden doming motion of the valves into the LA",
        "A low left atrial pressure with thickened leaflets causes a sudden doming motion of the valves into the LV",
    ],
    "The mechanism reads '↑ LAP + thickened leaflets → Sudden doming motion of valves into LV → Opening snap', with the opening snap proportional to LAP.",
)

add(
    S3, 305, "recall",
    "How does a rising left atrial pressure change the S2–OS interval in mitral stenosis?",
    "It opens the AV valves earlier, so the opening snap comes earlier and the S2–OS interval shortens; S2–OS is inversely proportional to LAP",
    [
        "It opens the AV valves later, so the opening snap comes later and the S2–OS interval lengthens; S2–OS is directly proportional to LAP",
        "It opens the AV valves earlier, so the opening snap comes earlier and the S2–OS interval lengthens; S2–OS is directly proportional to LAP",
        "It does not change the timing of valve opening, so the S2–OS interval is independent of LAP",
    ],
    "The pathophysiology chain reads '↑ LAP → Early opening of AV valves → Early OS → ↓ S2-OS interval', and the next line 'S2-OS α 1/LAP'.",
)

add(
    S3, 305, "match",
    "Match each severity of mitral stenosis to its printed intervals and pressures — 1) Mild MS 2) Severe MS … A) S2–OS 40–60 mmHg with LAP >15 mmHg B) S2–OS >120 mmHg with LAP <5 mmHg",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The mild column prints S2–OS >120 mmHg with LAP <5 mmHg and the severe column S2–OS 40–60 mmHg with LAP >15 mmHg; the units are printed as mmHg against what should be milliseconds, a slip preserved verbatim.",
)

add(
    S3, 305, "fillup",
    "The opening snap is auscultated with the patient standing, midway between the apex and the lower left sternal border, and it does not vary with ______.",
    "respiration",
    ["posture", "exercise", "heart rate"],
    "The features read auscultation done standing midway between apex and lower left sternal border, and 'Does not vary with respiration'.",
)

add(
    S3, 305, "recall",
    "Which three descriptors are printed inside the ovals for tumour plop?",
    "Low pitched, atrial myxoma and early diastolic sound",
    [
        "High pitched, atrial myxoma and early diastolic sound",
        "Low pitched, ventricular myxoma and mid diastolic sound",
        "Low pitched, atrial myxoma and late diastolic sound",
    ],
    "The three ovals read 'Low pitched', 'Atrial myxoma' and 'Early diastolic sound', matching the early diastolic grouping on page 303.",
)

# ---------------------------------------------------------------- Unit 4: p306
add(
    S4, 306, "recall",
    "What are systolic added sounds called, and how are they classified?",
    "Clicks, classified into ejection clicks and non-ejection clicks, with ejection clicks divided into valvular and vascular",
    [
        "Snaps, classified into ejection snaps and non-ejection snaps, with ejection snaps divided into valvular and vascular",
        "Clicks, classified into valvular and vascular only, without a non-ejection group",
        "Knocks, classified into ejection knocks and non-ejection knocks, with ejection knocks divided into valvular and vascular",
    ],
    "The heading reads 'Systolic Added Sounds AKA clicks', with the tree splitting ejection clicks (valvular and vascular) from non ejection clicks.",
)

add(
    S4, 306, "recall",
    "Which event produces an ejection click, and which lesions are printed for the valvular type?",
    "Opening of the semilunar valves; the valvular type occurs in AS, PS and bicuspid aortic valve through a doming motion halted abruptly",
    [
        "Closure of the semilunar valves; the valvular type occurs in AS, PS and bicuspid aortic valve through a doming motion halted abruptly",
        "Opening of the atrioventricular valves; the valvular type occurs in MS, TS and bicuspid aortic valve through a doming motion halted abruptly",
        "Opening of the semilunar valves; the valvular type occurs in AR, PR and bicuspid aortic valve through a doming motion halted abruptly",
    ],
    "The block reads 'Sound produced by opening of semilunar valves', and the valvular mechanism 'Stenosis of valve → Doming motion of valve coming to an abrupt halt' with 'Heard in AS, PS & BAV'.",
)

add(
    S4, 306, "recall",
    "What causes a vascular ejection click, and in which lesion is it seen?",
    "Sudden distension of the valve beyond the vessel, seen in aneurysm of the vessel",
    [
        "Sudden distension of the valve beyond the vessel, seen in stenosis of the vessel",
        "Gradual distension of the vessel itself, seen in aneurysm of the vessel",
        "Sudden collapse of the vessel beyond the valve, seen in coarctation of the aorta",
    ],
    "The vascular branch reads 'D/t sudden distension of the valve beyond the vessel' and 'Seen in aneurysm of vessel'.",
)

add(
    S4, 306, "match",
    "Match each pathology to its printed S1 or S2 behaviour — 1) Vascular (root) pathologies 2) Valvular pathologies 3) Fever … A) Tachycardia with a loud S1 B) Soft S2 C) Loud S2",
    "1-C, 2-B, 3-A",
    ["1-B, 2-C, 3-A", "1-C, 2-A, 3-B", "1-A, 2-B, 3-C"],
    "The note reads vascular (root) pathologies → loud S2, valvular pathologies → soft S2 and fever → tachycardia → loud S1.",
)

add(
    S4, 306, "recall",
    "Which five features of ejection clicks are printed on page 306?",
    "Absent in severe stenosis from calcification, heard best in the aortic area, often confused with a loud S1, not varying with respiration, and the pulmonary click heard better in expiration",
    [
        "Present in severe stenosis despite calcification, heard best in the pulmonary area, often confused with a loud S2, varying with respiration, and the pulmonary click heard better in inspiration",
        "Absent in severe stenosis from calcification, heard best in the aortic area, often confused with a loud S2, not varying with respiration, and the pulmonary click heard better in inspiration",
        "Absent in mild stenosis, heard best in the aortic area, often confused with a loud S1, varying with expiration, and the pulmonary click heard better in inspiration",
    ],
    "The features list reads absent in severe stenosis (d/t calcification), heard best in the aortic area, often confused with loud S1, does not vary with respiration, and 'Pulmonary ejection click → Heard better in expiration'.",
)

add(
    S4, 306, "recall",
    "With which valve lesion are non-ejection clicks associated, and what does dynamic auscultation do?",
    "Mitral valve prolapse, where dynamic auscultation causes a long duration murmur",
    [
        "Mitral stenosis, where dynamic auscultation causes a long duration murmur",
        "Mitral valve prolapse, where dynamic auscultation abolishes the murmur",
        "Aortic stenosis, where dynamic auscultation causes a long duration murmur",
    ],
    "The non-ejection section reads 'Associated with mitral valve prolapse' and, under features, 'Dynamic auscultation: Causes long duration murmur'.",
)

add(
    S4, 306, "recall",
    "Which chain is printed for the mitral valve prolapse click during standing or Valsalva?",
    "↓ preload → ↓ ventricular cavity size → ↓ stretching of chordae → ↑ prolapse → click moves closer to S1",
    [
        "↑ preload → ↑ ventricular cavity size → ↑ stretching of chordae → ↑ prolapse → click moves closer to S1",
        "↓ preload → ↓ ventricular cavity size → ↑ stretching of chordae → ↓ prolapse → click moves away from S1",
        "↓ afterload → ↑ ventricular cavity size → ↓ stretching of chordae → ↑ prolapse → click moves closer to S2",
    ],
    "The loop reads standing/Valsalva → ↓ preload → ↓ ventricular cavity size → ↓ stretching of chordae → ↑ prolapse → 'Click moves closer to S1'.",
)

add(
    S4, 306, "scenario",
    "A young woman has a mid-systolic click and late systolic murmur that move earlier in standing and later on squatting. Which printed mechanism explains the movement?",
    "Standing lowers preload, reducing ventricular cavity size and chordal stretch, so prolapse occurs earlier and the click approaches S1",
    [
        "Standing raises preload, increasing ventricular cavity size and chordal stretch, so prolapse occurs later and the click approaches S2",
        "Standing lowers afterload, increasing ventricular cavity size and chordal stretch, so prolapse occurs earlier and the click approaches S1",
        "Standing lowers preload, reducing ventricular cavity size and chordal stretch, so prolapse occurs later and the click approaches S2",
    ],
    "The printed loop is ↓ preload → ↓ ventricular cavity size → ↓ stretching of chordae → ↑ prolapse → click closer to S1, the behaviour that marks a non-ejection click of mitral valve prolapse.",
)

add(
    S4, 306, "truefalse",
    "TRUE or FALSE about ejection clicks on page 306.",
    "True — they are often confused with a loud S1 and do not vary with respiration",
    [
        "True — they are often confused with a loud S2 and do vary with respiration",
        "False — they are never confused with a heart sound and vary widely with respiration",
        "False — they are absent in mild stenosis because of calcification",
    ],
    "The features print 'Often confused with loud S1' and 'Does not vary with respiration', while calcification abolishes the click only in severe stenosis.",
)

# ---------------------------------------------------------------- extra interactives
add(
    S1, 303, "scenario",
    "A lean 20-year-old athlete has a third heart sound at the apex, with excessive rapid filling of a hypercompliant ventricle and no cardiac disease. Which of the three printed mechanisms does he represent?",
    "Physiological — excessive rapid filling into a hypercompliant ventricle",
    [
        "Pathological — increased end systolic volume in a dilated ventricle",
        "Pathological — less than normal filling of a hypertrophic non-compliant ventricle",
        "Pathological — rapid filling across a stenosed AV valve",
    ],
    "The three mechanisms are physiological excessive rapid filling into a hypercompliant ventricle in the young or athletic, increased end systolic volume in a dilated ventricle (LVF, MR, AR) and less than normal filling of a hypertrophic non-compliant ventricle (LVH, RVH, RCMP); a stenosed AV valve precludes S3. (Book p303)",
)

add(
    S1, 303, "truefalse",
    "TRUE or FALSE about the valve lesions in which S3 is seen, as printed on page 303.",
    "True — S3 is not seen in mitral stenosis or tricuspid stenosis",
    [
        "True — S3 is a constant finding in mitral stenosis",
        "False — S3 is always seen in aortic regurgitation with LVF",
        "False — S3 requires a stenosed AV valve",
    ],
    "The pre-requisite is a non-stenosed AV valve, printed as 'Not seen in MS & TS'; AR is also printed as not seen except with LVF.",
)

add(
    S2, 304, "scenario",
    "A patient with chronic constrictive pericarditis has an early diastolic sound that disappears after pericardiectomy. Which sound is this, and which feature separates it from S3?",
    "A pericardial knock, separated from S3 by its high pitch and inspiratory increase",
    [
        "A pericardial knock, separated from S3 by its low pitch and expiratory increase",
        "An opening snap, separated from S3 by its early timing",
        "A tumour plop, separated from S3 by its late diastolic timing",
    ],
    "The knock is high pitched and louder with inspiration, bracketed 'To differentiate from S3', and 'Disappears following pericardiectomy'.",
)

add(
    S2, 304, "scenario",
    "A patient in atrial fibrillation has no fourth heart sound despite LVH. Which printed prerequisite explains the absence?",
    "S4 needs healthy atria in sinus rhythm contracting vigorously",
    [
        "S4 needs a stenosed AV valve, which is absent here",
        "S4 needs a dilated, compliant ventricle, which is absent here",
        "S4 needs a rapid filling phase, which fibrillation enhances",
    ],
    "The prerequisites begin 'Healthy atria in sinus rhythm' and 'Contracting vigorously', both lost in atrial fibrillation.",
)

add(
    S3, 305, "scenario",
    "A patient with mitral stenosis has an S2–OS interval of 50 ms and a left atrial pressure of 18 mm Hg. Which severity does the printed ladder indicate?",
    "Severe MS, since S2–OS is 40–60 and LAP exceeds 15 mmHg",
    [
        "Mild MS, since S2–OS is above 120 and LAP is below 5 mmHg",
        "Mild MS, since any measurable S2–OS indicates mild disease",
        "Severe MS, since S2–OS is above 120 mmHg",
    ],
    "The severe column prints S2–OS 40–60 mmHg with LAP >15 mmHg, against mild disease at >120 mmHg and LAP <5 mmHg; the units are printed as mmHg and preserved verbatim.",
)

add(
    S3, 305, "truefalse",
    "TRUE or FALSE about the relation of the opening snap to left atrial pressure on page 305.",
    "True — the opening snap amplitude is proportional to LAP, while the S2–OS interval is inversely proportional to LAP",
    [
        "True — both the opening snap amplitude and the S2–OS interval are directly proportional to LAP",
        "False — the opening snap amplitude is inversely proportional to LAP and the interval is directly proportional",
        "False — the opening snap bears no relation to LAP",
    ],
    "The two printed lines are 'Opening snap (OS) α LAP' and 'S2-OS α 1/LAP', which is why severe disease has a short interval and a loud snap.",
)

add(
    S4, 306, "scenario",
    "A patient with severe calcific aortic stenosis has no ejection click. What does page 306 say about that?",
    "The click is absent in severe stenosis because of calcification",
    [
        "The click is loudest in severe stenosis because of calcification",
        "The click is absent because vascular rather than valvular pathology is present",
        "The absence of a click excludes aortic stenosis",
    ],
    "Under features, 'Absent in severe stenosis (d/t calcification)' is printed first, so a missing click does not exclude severe disease.",
)

add(
    S4, 306, "oddoneout",
    "Pick the ODD ONE OUT — three are printed features of ejection clicks, one belongs to the non-ejection click of mitral valve prolapse:",
    "It moves closer to S1 on standing because of reduced preload",
    ["It is often confused with a loud S1", "It does not vary with respiration", "It is heard best in the aortic area"],
    "Movement with standing is the dynamic auscultation of the non-ejection click of mitral valve prolapse; ejection clicks are confused with loud S1, do not vary with respiration and are best heard in the aortic area.",
)

GUIDES = {
    S1: (
        "The cycle continues (p303) from protodiastole through closed semilunar valves, isovolumetric relaxation, opening AV valves, rapid and reduced filling (70% passive) to atrial systole (30% active).\n"
        "Diastolic sounds run opening snap, pericardial knock and tumour plop as early diastolic, S3 mid diastolic and S4 late diastolic, with S3, S4 and tumour plop the low pitched ones.\n"
        "S3 is the ventricular or protodiastolic gallop of rapid filling, requiring a non-stenosed AV valve and so absent in MS and TS; its mechanisms are physiological hypercompliant filling in the young, increased end systolic volume in LV/RV failure, and reduced filling of a hypertrophic non-compliant ventricle in LVH, RVH and RCMP, with pathological S3 earlier than physiological; it is heard in MR and severe AS but not MS or AR.",
    ),
    S2: (
        "S3 is heard in the left lateral position at the apex, does not vary with respiration, disappears upright when physiological, and appears with passive leg raising; heart failure without S3 means MS, TS or pericardial tamponade (p304).\n"
        "The pericardial knock of chronic constrictive pericarditis is high pitched, louder with inspiration and early diastolic, increasing with cardiac output and disappearing after pericardiectomy.\n"
        "S4 is the atrial or presystolic gallop of atrial systole correlating with the JVP A-wave, needing healthy atria in sinus rhythm contracting vigorously across a non-stenosed AV valve into a non-dilated ± hypertrophic non-compliant ventricle; its mechanism is a rise in LV end-diastolic fibre length, and it is not seen in MS, MR or AR but is heard in AS, and in acute MR and AR; the table gives AS +/+, AR in failure/–, MS –/– and MR +/–.",
    ),
    S3: (
        "S4 also appears with concentric LVH from systemic HTN or HCM, concentric RVH from PS, PAH or RCM, and RV ischaemia from coronary disease (p305).\n"
        "The opening snap is AV valve opening representing isovolumetric relaxation, heard with the bell at the apex in expiration, requiring mobile leaflets, good LV function and organic MS as the predominant lesion; raised LAP with thickened leaflets causes sudden doming, so OS α LAP and S2–OS α 1/LAP, printing S2–OS >120 mmHg with LAP <5 mmHg in mild disease and 40–60 mmHg with LAP >15 mmHg in severe disease.\n"
        "It is heard standing midway between apex and lower left sternal border and does not vary with respiration; tumour plop is low pitched, from atrial myxoma, and early diastolic.",
    ),
    S4: (
        "Systolic added sounds are clicks, split into ejection clicks (valvular and vascular) and non-ejection clicks (p306).\n"
        "Ejection clicks come from semilunar valve opening: valvular clicks from a doming valve halted abruptly in AS, PS and bicuspid aortic valve, and vascular clicks from sudden distension beyond the valve in aneurysm; root pathology loudens S2 while valvular pathology softens it, fever with tachycardia loudens S1.\n"
        "Ejection clicks disappear in severe calcific stenosis, are best heard in the aortic area, are often confused with a loud S1, do not vary with respiration, and a pulmonary click is better heard in expiration; non-ejection clicks belong to mitral valve prolapse, where standing or Valsalva lowers preload, shrinks the cavity, reduces chordal stretch, increases prolapse and moves the click toward S1.",
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
