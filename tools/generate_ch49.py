#!/usr/bin/env python3
"""Generate Chapter 49: Cardiac Cycle With Heart Sounds (Book p296–302).

Every question is anchored to a printed line, table cell or figure caption of
uploads/03.pdf sheets 49–55 (Book pages 296–302), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 49
TITLE = "Cardiac Cycle With Heart Sounds"
PAGES = "296-302"

S1 = "Heart Sounds as Discrete Vibrations, Intensity in Decibels against Frequency in Hertz with Their Inverse Relation, the Six-Row High against Low Frequency Table and the Mixed ESM of Aortic Stenosis"
S2 = "The 0.8-Second Cycle, the 0.3-Second Systolic and 0.5-Second Diastolic Phase Lists, the 70 to 30 Per Cent Filling Split, and the S1 Valve Apparatus with Annular Contraction and Coaptation"
S3 = "The Six Determinants of S1 Intensity from Leaflet Integrity and Diastolic Position through Contraction Velocity, Closure Timing and dP/dt to Chest Wall Transmission"
S4 = "S1 in Aortic Stenosis, Regurgitation, Mitral Stenosis and Mitral Regurgitation, Loud T1 Causes, the Aortic Ejection Click, and Varying, Intermittent and Wide Split S1"
S5 = "Reverse Split S1, the S1 to S2 Sequence through Crossover Pressure, and the Hangout Interval with Its 30 and 80 Millisecond Aortic and Pulmonary Values"
S6 = "S2 as Aortic and Pulmonary Closure at 120–150 Hz, the Four Determinants of A2 and P2, Their Behaviour in Valve Disease, the Four-Column Table and the Six Causes of a Single S2"
S7 = "Wide Split S2 above 50 ms with Its Variable and Fixed Arms, and the Paradoxical Split with Early P2 and Delayed A2 Causes"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(49000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(49100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p296
add(
    S1, 296, "recall",
    "How are heart sounds defined in the opening line of the chapter?",
    "Brief, discrete auditory vibrations",
    [
        "Prolonged, continuous auditory murmurs",
        "Brief, discrete tactile thrills",
        "Low-pitched continuous rumbles",
    ],
    "The definition is 'Brief, discrete auditory vibrations', after which the chapter separates intensity from frequency and then turns to types.",
)

add(
    S1, 296, "match",
    "Match each identifying feature of a heart sound to its printed unit — 1) Intensity (loudness) 2) Frequency (pitch) … A) Hertz (Hz) B) Decibel (dB)",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The page reads 'Intensity (Loudness): measured in decibel (dB)' and 'Frequency (Pitch): measured in hertz (Hz)', and then prints frequency ∝ 1/amplitude.",
)

add(
    S1, 296, "fillup",
    "The printed relation between frequency and amplitude is frequency α 1/______.",
    "amplitude/intensity",
    ["wavelength", "velocity", "duration"],
    "The formula line reads 'Frequency α 1 / Amplitude/intensity', so a louder sound is a lower-pitched sound in this scheme.",
)

add(
    S1, 296, "match",
    "Match each feature to high or low frequency as printed — 1) Features 2) Pressure difference between chambers 3) Area heard 4) Thrill … A) Wide against low B) Soft musical/blowing against rough rumbling or thud-like C) Absent against present D) Wider against localised",
    "1-B, 2-A, 3-D, 4-C",
    ["1-B, 2-D, 3-A, 4-C", "1-A, 2-B, 3-D, 4-C", "1-B, 2-A, 3-C, 4-D"],
    "The table gives high frequency a soft musical or blowing quality, a wide pressure difference, a wider area, no thrill and the diaphragm, against the low-frequency column's rough rumbling or thud, low pressure difference, localised area, present thrill and bell.",
)

add(
    S1, 296, "recall",
    "Which sounds are printed as exceptions to the rule that low frequency is heard with the bell?",
    "S3, S4 and tumour plop among the sounds, with MS, TS and Austin Flint among the murmurs",
    [
        "S1, S2 and opening snap among the sounds, with AS, PS and Austin Flint among the murmurs",
        "S3, S4 and opening snap among the sounds, with MR, TR and Austin Flint among the murmurs",
        "S3, S4 and tumour plop among the sounds, with MR, AR and Austin Flint among the murmurs",
    ],
    "The low-frequency example cell reads 'Exceptions: Sounds S3, S4, tumor plop. murmur: MS, TS, Austin Flint', all heard with the bell.",
)

add(
    S1, 296, "fillup",
    "The only mixed frequency sound discussed on page 296 is the ejection systolic murmur of ______.",
    "aortic stenosis",
    ["mitral stenosis", "mitral regurgitation", "pulmonary stenosis"],
    "The line reads 'mixed frequency sound: ejection systolic murmur (ESM) in AS', followed by its harsh quality at the second right intercostal space and the Gallavardin phenomenon.",
)

add(
    S1, 296, "recall",
    "Which two components of the aortic stenosis murmur are printed, and where does each radiate?",
    "A low pitch component radiating to the carotid and a high pitch component radiating to the apex (Gallavardin phenomenon)",
    [
        "A low pitch component radiating to the apex and a high pitch component radiating to the carotid",
        "A low pitch component radiating to the axilla and a high pitch component radiating to the carotid",
        "A high pitch component radiating to the carotid and a low pitch component radiating to the left sternal border",
    ],
    "The two components read 'Low pitch → radiates to carotid' and 'High pitch → radiates to apex (Gallavardin phenomenon)', the murmur itself being harsh at the second right ICS.",
)

add(
    S1, 296, "numeric",
    "Where is the harsh component of the aortic stenosis murmur best heard?",
    "The second right intercostal space",
    [
        "The apex",
        "The second left intercostal space",
        "The lower left sternal border",
    ],
    "The bullet reads 'Harsh murmur • 2nd right ICS', before the two components split into a carotid low pitch and an apical high pitch.",
)

# ---------------------------------------------------------------- Unit 2: p297
add(
    S2, 297, "numeric",
    "How long is the cardiac cycle, and how is it divided between atria and ventricles?",
    "0.8 s, with atrial systole 0.1 s and atrial diastole 0.7 s",
    [
        "0.8 s, with atrial systole 0.3 s and atrial diastole 0.5 s",
        "0.6 s, with atrial systole 0.1 s and atrial diastole 0.5 s",
        "0.8 s, with atrial systole 0.2 s and atrial diastole 0.6 s",
    ],
    "The page prints 'Cardiac cycle: 0.8 seconds', 'Atria: 0.1 s systole' and '0.7 s diastole', while the ventricular phases split 0.3 s systolic against 0.5 s diastolic.",
)

add(
    S2, 297, "match",
    "Match the two ventricular phases to their printed durations — 1) Systole 2) Diastole … A) 0.5 s B) 0.3 s",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The column headings read systole (0.3 s) and diastole (0.5 s), while the atria are printed separately as 0.1 s systole and 0.7 s diastole.",
)

add(
    S2, 297, "recall",
    "Which five phases make up diastole in the printed column?",
    "Proto diastole, isovolumetric relaxation, rapid filling, reduced filling and atrial systole",
    [
        "Proto diastole, isovolumetric contraction, rapid filling, reduced filling and atrial systole",
        "Proto diastole, isovolumetric relaxation, rapid ejection, reduced filling and atrial systole",
        "Isovolumetric relaxation, rapid filling, reduced filling, atrial systole and rapid ejection",
    ],
    "The right column reads 1. Proto diastole, 2. Isovolumetric relaxation (IVR), 3. Rapid filling, 4. Reduced filling, 5. Atrial systole, under the heading Diastole (0.5 s).",
)

add(
    S2, 297, "numeric",
    "What percentage of ventricular filling occurs passively in reduced filling, and what does atrial systole add?",
    "70% passively, with atrial systole contributing 30%",
    [
        "30% passively, with atrial systole contributing 70%",
        "50% passively, with atrial systole contributing 50%",
        "70% passively, with atrial systole contributing 40%",
    ],
    "The reduced-filling branch prints '70% of ventricles filled' and 'Passive filling', and atrial systole is labelled '(30%) ventricular filling (Active)'.",
)

add(
    S2, 297, "recall",
    "Which three events close the AV valves and open isovolumetric contraction?",
    "AV valves are open with 70% passive filling, atrial systole adds 30%, then ventricular pressure exceeds atrial pressure and the AV valves close, producing S1",
    [
        "AV valves are closed with 70% passive filling, atrial systole adds 30%, then ventricular pressure exceeds atrial pressure and the AV valves open, producing S1",
        "AV valves are open with 70% passive filling, atrial systole adds 30%, then atrial pressure exceeds ventricular pressure and the AV valves close, producing S1",
        "AV valves are open with 70% passive filling, atrial systole adds 30%, then ventricular pressure exceeds atrial pressure and the semilunar valves close, producing S1",
    ],
    "The arrows read reduced filling → AV valves open, 70% filled, passive → atrial systole 30% active → ventricular pressure > atrial → AV valves close (S1) → isovolumetric contraction.",
)

add(
    S2, 297, "recall",
    "Which three parts make up the valve apparatus as printed?",
    "Leaflet (cusp), fibrous annulus and commissures",
    [
        "Leaflet (cusp), chordae tendineae and papillary muscle",
        "Leaflet (cusp), fibrous annulus and chordae tendineae",
        "Fibrous annulus, commissures and papillary muscle",
    ],
    "The valve apparatus list reads '1. Leaflet (cusp). 2. Fibrous annulus. 3. Commissures.', chordae and papillary muscles being handled later with secondary MR.",
)

add(
    S2, 297, "recall",
    "Which physiological sequence generates the first heart sound?",
    "Annular contraction → leaflets come close (coaptation zone) → sudden tensing of the leaflet → S1",
    [
        "Annular dilatation → leaflets separate (coaptation zone) → sudden tensing of the leaflet → S1",
        "Annular contraction → leaflets come close (coaptation zone) → gradual relaxation of the leaflet → S1",
        "Papillary contraction → chordae shorten → leaflets evert → S1",
    ],
    "The physiology column reads 'Annular contraction → Leaflet come close (Coaptation zone) → Sudden tensing of leaflet → S1'.",
)

add(
    S2, 297, "fillup",
    "The two components of S1 are M1 from closure of the mitral valve and T1 from closure of the tricuspid valve, separated by less than ______ ms and therefore not appreciated.",
    "30",
    ["10", "50", "80"],
    "The bracket beside M1 and T1 reads '<30 ms difference (not appreciated)', which is why S1 is heard as a single sound.",
)

# ---------------------------------------------------------------- Unit 3: p298
add(
    S3, 298, "recall",
    "Which three leaflet abnormalities make S1 soft according to the first factor on page 298?",
    "An incompetent leaky leaflet as in MR, a perforated leaflet as in infective endocarditis, and a calcific immobile leaflet as in calcific MS",
    [
        "A stenotic leaflet as in MS, a perforated leaflet as in infective endocarditis, and a calcific immobile leaflet as in calcific MS",
        "An incompetent leaky leaflet as in MR, a perforated leaflet as in rheumatic fever, and a calcific mobile leaflet as in calcific MS",
        "An incompetent leaky leaflet as in AR, a perforated leaflet as in infective endocarditis, and a calcific immobile leaflet as in calcific AS",
    ],
    "The integrity branch ends in 'soft S1' through a. incompetent valve leaflet (leaky) → regurgitation (MR), b. perforation of leaflet (infective endocarditis) and c. calcific for immobile leaflet (calcific MS).",
)

add(
    S3, 298, "recall",
    "How does the position of the leaflet at end diastole differ in a normal valve and in stenosis, and what does that do to S1?",
    "Normally the leaflet floats semiclosed in the filled LV, but stenosis reduces LV filling so the valve sits wide apart and closes from a distance, making S1 loud",
    [
        "Normally the leaflet floats wide open in the filled LV, but stenosis reduces LV filling so the valve sits semiclosed and closes from a short distance, making S1 soft",
        "Normally the leaflet floats semiclosed in the filled LV, but stenosis increases LV filling so the valve sits wide apart and closes from a distance, making S1 loud",
        "Normally the leaflet floats semiclosed in the empty LV, but stenosis reduces LV filling so the valve sits wide apart and closes from a distance, making S1 loud",
    ],
    "The block reads 'Normal: Semiclosed position floating in the filled LV', then stenosis → reduced LV filling → valve wide apart → close from a distance → loud S1, the example being MS.",
)

add(
    S3, 298, "match",
    "Match each heart rate state to its printed effect on S1 — 1) Bradycardia 2) Tachycardia … A) Loud S1 B) Soft S1",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "Bradycardia lengthens the PR interval, increases filling and brings the valves closer, so S1 is soft; tachycardia shortens the PR interval, reduces filling and makes the valves close from a distance, so S1 is loud.",
)

add(
    S3, 298, "recall",
    "Which two timing abnormalities are printed for closure, with their examples?",
    "Delayed closure gives a loud S1 as in MS, and premature closure gives a soft S1 as in AR",
    [
        "Delayed closure gives a soft S1 as in MS, and premature closure gives a loud S1 as in AR",
        "Delayed closure gives a loud S1 as in AR, and premature closure gives a soft S1 as in MS",
        "Delayed closure gives a loud S1 as in MR, and premature closure gives a soft S1 as in AS",
    ],
    "The timing block reads 'a. Delayed closure: Loud S1, e.g. MS → ↑LAP → more time for LVP > LAP' and 'b. Premature closure: soft S1, e.g. AR → LVP ↑ rapidly'.",
)

add(
    S3, 298, "recall",
    "Which dP/dt states are printed, and which examples accompany them?",
    "A leaky valve gives an ineffective isovolumetric contraction with loss of dP/dt and a soft S1 (MR, myocarditis), while exercise or high output raises contractility and dP/dt and gives a loud S1",
    [
        "A leaky valve preserves dP/dt and gives a loud S1 (MR, myocarditis), while exercise lowers contractility and gives a soft S1",
        "A leaky valve gives loss of dP/dt and a loud S1 (MR, myocarditis), while exercise raises dP/dt and gives a soft S1",
        "A stenotic valve gives loss of dP/dt and a soft S1 (AS, MS), while exercise raises dP/dt and gives a loud S1",
    ],
    "The factor reads 'dP/dt of isovolumetric contraction' with a. leaky valve → ineffective IVC → loss of dP/dt → ↓velocity → soft S1 (MR, myocarditis) and b. exercise/high output → ↑contractility → ↑dP/dt → loud S1.",
)

add(
    S3, 298, "recall",
    "How do thoracic transmission factors change S1 on page 298?",
    "Obesity, emphysema and pericardial effusion reduce the intensity of all auscultatory events giving a soft S1, while a thin chest wall raises intensity giving a loud S1",
    [
        "Obesity, emphysema and pericardial effusion raise the intensity of all auscultatory events giving a loud S1, while a thin chest wall lowers intensity",
        "Obesity, emphysema and pleural effusion reduce the intensity of all auscultatory events giving a soft S1, while a thin chest wall raises intensity",
        "Obesity, emphysema and pericardial effusion reduce the intensity of S1 alone, while a thin chest wall raises only the murmurs",
    ],
    "The sixth factor reads 'Obesity, emphysema, pericardial effusion → ↓intensity of all auscultatory events → soft S1' and 'Thin chest wall → ↑intensity → loud S1'.",
)

add(
    S3, 298, "scenario",
    "A young woman with a long PR interval on ECG has a strikingly soft first heart sound. Which printed mechanism explains it?",
    "Bradycardia lengthens diastole, so filling is greater, the valve leaflets sit closer and closure velocity falls",
    [
        "Bradycardia shortens diastole, so filling is less, the valve leaflets sit wide apart and closure velocity rises",
        "The long PR interval delays closure, so the leaflets travel further and S1 becomes loud",
        "The long PR interval perforates the leaflets, so S1 becomes soft",
    ],
    "The velocity-of-contraction block explicitly ties '↑ PR interval (diastole) → ↑ filling → valve are closer → ↓ velocity' to a soft S1 in bradycardia.",
)

# ---------------------------------------------------------------- Unit 4: p299
add(
    S4, 299, "match",
    "Match each valve lesion to its printed S1 — 1) Aortic stenosis 2) Aortic regurgitation 3) Mitral stenosis 4) Mitral regurgitation … A) Soft S1 unrelated to severity B) Normal C) Soft S1 D) Loud S1 unrelated to severity",
    "1-B, 2-C, 3-D, 4-A",
    ["1-B, 2-D, 3-C, 4-A", "1-C, 2-B, 3-D, 4-A", "1-B, 2-C, 3-A, 4-D"],
    "The table reads AS normal, AR soft S1, MS loud S1 (unrelated to severity) and MR soft S1 (unrelated to severity), in that column order.",
)

add(
    S4, 299, "match",
    "Match each lesion to the printed reason for its S1 — 1) Aortic regurgitation 2) Mitral stenosis 3) Mitral regurgitation … A) Loss of integrity and loss of dP/dt of isovolumetric contraction B) Position wide apart, increased velocity and delayed closure C) Premature closure (acute and chronic AR)",
    "1-C, 2-B, 3-A",
    ["1-B, 2-C, 3-A", "1-A, 2-B, 3-C", "1-C, 2-A, 3-B"],
    "The reason row gives AR premature closure in acute and chronic disease, MS position wide apart with ↑velocity and delayed closure, and MR loss of integrity with loss of dP/dt of isovolumetric contraction.",
)

add(
    S4, 299, "recall",
    "Which three conditions give a loud T1, and by what shared mechanism?",
    "TS, ASD and total anomalous pulmonary venous connection, all through increased tricuspid flow",
    [
        "TS, VSD and total anomalous pulmonary venous connection, all through increased tricuspid flow",
        "TS, ASD and Ebstein anomaly, all through increased tricuspid flow",
        "MS, ASD and total anomalous pulmonary venous connection, all through increased mitral flow",
    ],
    "The list reads 'TS', 'ASD' and 'Total Anomalous Pulmonary Venous Connection' with the brace '↑ tricuspid flow' — a tricuspid, not mitral, mechanism.",
)

add(
    S4, 299, "recall",
    "What produces the loud heart sound in aortic stenosis, and with what can it be confused?",
    "A bicuspid aortic valve producing an aortic ejection click, which can be confused for S1",
    [
        "A calcified aortic valve producing an opening snap, which can be confused for S2",
        "A bicuspid aortic valve producing an aortic ejection click, which can be confused for S2",
        "A bicuspid pulmonary valve producing a pulmonary ejection click, which can be confused for S1",
    ],
    "The line reads 'Loud heart sound in AS: d/t Bicuspid aortic valve → Aortic ejection click (Can be confused for S1)'.",
)

add(
    S4, 299, "recall",
    "How is S1 described in rheumatic mitral regurgitation with a preserved leaflet, and why?",
    "Soft S1, because of associated myocarditis",
    [
        "Loud S1, because of associated myocarditis",
        "Soft S1, because of calcific immobile leaflets",
        "Normal S1, because the leaflet is preserved",
    ],
    "The line reads 'Rheumatic fever MR with preserved leaflet: Soft S1 (d/t associated myocarditis)', a myocardial rather than valvular cause.",
)

add(
    S4, 299, "recall",
    "What determines S1 when mitral stenosis and mitral regurgitation coexist, and what does moderate MS do through the right heart?",
    "S1 depends on the predominant disease, and moderate MS causes pulmonary hypertension with RV hypertrophy and TR, giving a soft S1",
    [
        "S1 is always loud, and moderate MS causes pulmonary hypertension with LV hypertrophy and MR, giving a soft S1",
        "S1 depends on the predominant disease, and moderate MS causes pulmonary hypotension with RV hypertrophy and TR, giving a loud S1",
        "S1 depends on the predominant disease, and moderate MS causes pulmonary hypertension with RV hypertrophy and TR, giving a loud S1",
    ],
    "The lines read 'MS + MR: Depends on predominant disease' and 'TR in MS: moderate MS → pulmonary HTN → RV Hypertrophy → TR → soft S1'.",
)

add(
    S4, 299, "match",
    "Match each variable-S1 pattern to its printed causes — 1) Varying S1 2) Intermittent S1 … A) Complete heart block with AV dissociation giving cannon S1, and VT with AV dissociation B) Atrial fibrillation from varying cycle length and atrial flutter",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The varying branch lists atrial fibrillation from varying cycle length with varying force of contraction, plus atrial flutter; the intermittent branch lists complete heart block with AV dissociation giving cannon S1, and VT with AV dissociation.",
)

add(
    S4, 299, "match",
    "Match each wide split S1 cause to its printed side of the split — 1) Ectopic from LV and LV pacing 2) Ebstein anomaly 3) RBBB, TS and RA myxoma … A) Late T1 B) Early M1 (mechanical, with a sail sound from loud T1) C) Early M1 (electrical)",
    "1-C, 2-B, 3-A",
    ["1-B, 2-C, 3-A", "1-A, 2-C, 3-B", "1-C, 2-A, 3-B"],
    "The wide split S1 tree places ectopic from LV and LV pacing under early M1 electrical, Ebstein anomaly under early M1 mechanical with the sail sound from loud T1, and RBBB, TS and RA myxoma under late T1.",
)

add(
    S4, 299, "fillup",
    "In Ebstein anomaly the wide split S1 carries a ______ sound because T1 is loud.",
    "sail",
    ["cannon", "ejection click", "knock"],
    "The bracket under Ebstein anomaly reads '(Sail sound d/t loud T1)', the early M1 widening the split.",
)

# ---------------------------------------------------------------- Unit 5: p300
add(
    S5, 300, "match",
    "Match each reverse split S1 cause to its printed mechanism — 1) Right sided pacing or right sided ectopic 2) LBBB 3) MS or LA myxoma … A) Delayed M1 (mechanical) B) Early T1 (electrical) C) Delayed M1 (electrical)",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "Reverse split runs T1 before M1, with early T1 from right sided pacing or ectopic, delayed M1 electrical in LBBB, and delayed M1 mechanical in MS or LA myxoma.",
)

add(
    S5, 300, "recall",
    "After S1, which structures open and which sound is associated with their opening?",
    "The aortic and pulmonary valves open, and this is associated with ejection clicks",
    [
        "The aortic and pulmonary valves close, and this is associated with ejection clicks",
        "The mitral and tricuspid valves open, and this is associated with opening snaps",
        "The aortic and pulmonary valves open, and this is associated with the second heart sound",
    ],
    "The S1–S2 flow reads S1 → isovolumetric contraction → 'Aortic and pulmonary valves open: associated with ejection clicks' → rapid ejection → reduced ejection.",
)

add(
    S5, 300, "recall",
    "Which point in the printed cycle follows the rise of aortic and pulmonary artery pressures?",
    "The point of crossover pressure, where aortic pressure exceeds CVP and pulmonary pressure exceeds RVP, followed by the hangout interval and valve closure with S2",
    [
        "The point of dicrotic notch, where aortic pressure falls below CVP, followed by the hangout interval and valve closure with S2",
        "The point of crossover pressure, where aortic pressure falls below CVP and pulmonary pressure falls below RVP, followed by valve closure with S2",
        "The point of isovolumetric relaxation, where aortic pressure exceeds CVP, followed by the opening snap",
    ],
    "The chart prints 'Point of crossover pressure (Aortic pressure > CVP, Pulmonary pressure > RVP)' → 'Hangout interval (protodiastole)' → 'valve closure – S2'.",
)

add(
    S5, 300, "fillup",
    "The hangout interval is defined as the time between crossover pressure and ______.",
    "valve closure",
    ["peak ejection", "valve opening", "the dicrotic notch"],
    "The definition reads 'Time between crossover pressure & valve closure', with protodiastole in brackets beside it.",
)

add(
    S5, 300, "recall",
    "On which two determinants does the printed hangout interval depend?",
    "The pressure beyond the valve and the distensibility of the vessel",
    [
        "The pressure beyond the valve and the valve area",
        "The flow across the valve and the vessel length",
        "The ventricular contractility and the valve area",
    ],
    "The block reads 'Depends on: Pressure (beyond valve), Distensibility (of vessel)', before splitting into the aortic and pulmonary columns.",
)

add(
    S5, 300, "numeric",
    "Which hangout interval is printed for the aorta and which for the pulmonary artery?",
    "30 ms for the aorta and 80 ms for the pulmonary artery",
    [
        "80 ms for the aorta and 30 ms for the pulmonary artery",
        "30 ms for the aorta and 50 ms for the pulmonary artery",
        "50 ms for the aorta and 80 ms for the pulmonary artery",
    ],
    "The aortic column prints '↓ Hangout interval (30 ms)' and the pulmonary column prints '(80 ms)', with A2 first and P2 next; the arrow in the pulmonary column is printed downward even though 80 ms exceeds 30 ms, a slip preserved as printed.",
)

add(
    S5, 300, "recall",
    "What is printed about the gap between A2 and P2, at rest and during inspiration?",
    "The gap is 50 ms and is appreciable, and during inspiration it exceeds 50 ms because venous return rises",
    [
        "The gap is 50 ms and is not appreciable, and during inspiration it falls below 50 ms because venous return rises",
        "The gap is 80 ms and is appreciable, and during inspiration it exceeds 80 ms because venous return rises",
        "The gap is 30 ms and is appreciable, and during expiration it exceeds 50 ms because venous return rises",
    ],
    "The two closing bullets read 'Gap between A2 & P2: 50ms (appreciable)' and 'During inspiration: >50ms (d/t ↑ venous return)'.",
)

add(
    S5, 300, "scenario",
    "A patient has an audible split in the second sound during inspiration only, about 50 ms wide. What is the printed explanation?",
    "Inspiration increases venous return, widening the A2–P2 gap beyond the appreciable 50 ms",
    [
        "Expiration increases venous return, widening the A2–P2 gap beyond the appreciable 50 ms",
        "Inspiration reduces venous return, narrowing the A2–P2 gap below 50 ms",
        "Inspiration delays aortic valve closure, reversing the order to P2 then A2",
    ],
    "The page prints the resting gap as 50 ms and adds 'During inspiration: >50 ms (d/t ↑ venous return)', which is the physiological split of S2.",
)

# ---------------------------------------------------------------- Unit 6: p301
add(
    S6, 301, "recall",
    "With which event is the second heart sound associated, and at what frequency is it printed?",
    "Closure of the aortic and pulmonary valves, at a high frequency of 120–150 Hz",
    [
        "Opening of the aortic and pulmonary valves, at a high frequency of 120–150 Hz",
        "Closure of the mitral and tricuspid valves, at a high frequency of 120–150 Hz",
        "Closure of the aortic and pulmonary valves, at a low frequency of 20–40 Hz",
    ],
    "The introduction reads 'Associated with closure of aortic & pulmonary valve' and 'High frequency: 120–150 Hz', with A2 louder because aortic pressure exceeds pulmonary pressure.",
)

add(
    S6, 301, "match",
    "Match each determinant to its printed effect — 1) Systemic hypertension 2) Pulmonary hypertension 3) Hyperkinetic state 4) Pulmonary artery dilatation … A) Loud P2 from raised pressure beyond the valve B) Loud A2 C) Loud A2 and P2 together D) Loud P2 from the dilated vessel itself",
    "1-B, 2-A, 3-C, 4-D",
    ["1-A, 2-B, 3-C, 4-D", "1-B, 2-C, 3-A, 4-D", "1-B, 2-D, 3-C, 4-A"],
    "The factors read systemic HTN → loud A2, pulmonary HTN → loud P2, hyperkinetic state → loud A2/P2, and dilatation of the vessel beyond the valve (pulmonary HTN with pulmonary artery dilatation) → loud P2, the fourth factor being listed separately from pressure.",
)

add(
    S6, 301, "recall",
    "How is A2 affected in aortic stenosis from a bicuspid valve against a degenerative cause?",
    "A bicuspid aortic valve gives a loud A2, while a degenerative cause gives a soft A2",
    [
        "A bicuspid aortic valve gives a soft A2, while a degenerative cause gives a loud A2",
        "A bicuspid aortic valve gives a loud A2, while a degenerative cause gives a loud A2 as well",
        "A bicuspid aortic valve gives a soft A2, while a degenerative cause gives a soft A2 as well",
    ],
    "The AS bullets read 'd/t Bicuspid Aortic valve (BAV) → Loud A2' and 'd/t degenerative cause → Soft A2'.",
)

add(
    S6, 301, "recall",
    "Which A2 does aortic regurgitation produce from valve pathology, and which from root pathology?",
    "Soft A2 from rheumatic valve pathology, and loud A2 (tambour S2) from root pathology as in syphilis",
    [
        "Loud A2 from rheumatic valve pathology, and soft A2 from root pathology as in syphilis",
        "Soft A2 from rheumatic valve pathology, and soft A2 (tambour S2) from root pathology as in Marfan syndrome",
        "Soft A2 from rheumatic valve pathology, and loud A2 (tambour S2) from root pathology as in ankylosing spondylitis",
    ],
    "The AR block reads 'd/t value pathology (Rheumatic) → Soft A2' and 'd/t root pathology → Loud A2 (tambour S2) (syphilis)'.",
)

add(
    S6, 301, "recall",
    "What does moderate mitral stenosis do to P2, and what happens if pulmonary hypertension is joined by right ventricular failure?",
    "It produces a loud P2 through pulmonary hypertension, and the combination with RVF widens the split of S2",
    [
        "It produces a soft P2 through pulmonary hypertension, and the combination with RVF widens the split of S2",
        "It produces a loud P2 through pulmonary hypertension, and the combination with RVF narrows the split of S2",
        "It produces a loud P2 through systemic hypertension, and the combination with LVF widens the split of S2",
    ],
    "The MS bullet reads 'moderate MS → PHTN → Loud P2' with a sub-bullet 'If PHTN + RVF → wide split S2'; MR gives a loud P2 only if PHTN is positive.",
)

add(
    S6, 301, "match",
    "Match each four-column table entry to its printed group — 1) Loud A2 2) Loud P2 3) Soft A2 4) Soft P2 … A) Valvular PS B) Hyperkinetic state, HTN, aortic root dilatation and BAV C) Valvular AS (degenerative) and AR D) PHTN and ASD",
    "1-B, 2-D, 3-C, 4-A",
    ["1-D, 2-B, 3-C, 4-A", "1-B, 2-D, 3-A, 4-C", "1-C, 2-D, 3-B, 4-A"],
    "The table groups loud A2 as hyperkinetic state, HTN, aortic root dilatation and BAV; loud P2 as PHTN and ASD; soft A2 as valvular AS of degenerative type and AR; soft P2 as valvular PS.",
)

add(
    S6, 301, "recall",
    "Which five causes of a single S2 are printed on page 301?",
    "Severe pulmonary arterial hypertension giving a single loud P2, aging, atresia of a semilunar valve, severe AS or PS, and truncus arteriosus",
    [
        "Severe pulmonary arterial hypertension giving a single loud A2, aging, atresia of a semilunar valve, severe AS or PS, and truncus arteriosus",
        "Severe systemic hypertension giving a single loud P2, aging, atresia of an atrioventricular valve, severe AS or PS, and truncus arteriosus",
        "Severe pulmonary arterial hypertension giving a single loud P2, aging, Ebstein anomaly, severe AS or PS, and truncus arteriosus",
    ],
    "The single S2 list reads severe PAH → single-loud P2, aging, atresia of semilunar valve, severe AS or PS and truncus arteriosus.",
)

add(
    S6, 301, "numeric",
    "At what frequency band is S2 printed, and which component is louder and why?",
    "120–150 Hz, with A2 louder because aortic pressure exceeds pulmonary pressure",
    [
        "120–150 Hz, with P2 louder because pulmonary pressure exceeds aortic pressure",
        "80–120 Hz, with A2 louder because aortic pressure exceeds pulmonary pressure",
        "120–150 Hz, with A2 and P2 equal because both valves close together",
    ],
    "The introduction prints high frequency 120–150 Hz with 'A2 louder (higher pressure in aorta than P2)'.",
)

# ---------------------------------------------------------------- Unit 7: p302
add(
    S7, 302, "numeric",
    "Above which gap is an S2 split called wide, and what is the printed bedside consequence?",
    "Above 50 ms, and the split is then heard even in expiration",
    [
        "Above 30 ms, and the split is then heard only in inspiration",
        "Above 50 ms, and the split is then heard only in inspiration",
        "Above 80 ms, and the split is then heard even in expiration",
    ],
    "The heading reads 'Wide split S2 (>50 ms)' with the line 'Split heard even in expiration', the expiration audibility being the clinical marker.",
)

add(
    S7, 302, "match",
    "Match each wide variable split cause to its printed side — 1) LV pacing or LV ectopic 2) MR 3) RBBB or PS 4) PHTN with RVF as in MS … A) Late P2 from right ventricular pressure and failure B) Early A2, electrical C) Early A2, mechanical D) Late P2 from delayed right-sided activation or outflow obstruction",
    "1-B, 2-C, 3-D, 4-A",
    ["1-C, 2-B, 3-D, 4-A", "1-B, 2-C, 3-A, 4-D", "1-D, 2-C, 3-B, 4-A"],
    "The variable tree gives early A2 from LV pacing/ectopic electrically and MR mechanically, while late P2 covers RBBB, PS, VSD with a left-to-right shunt, cardiac tamponade and PHTN with RVF in MS.",
)

add(
    S7, 302, "recall",
    "Which two entries are printed under a fixed split of S2?",
    "Any cause of a wide variable split plus significant RV failure, and ASD where RV and LV filling change equally in expiration and inspiration",
    [
        "Any cause of a wide variable split plus significant LV failure, and ASD where RV and LV filling change equally",
        "Any cause of a wide variable split plus significant RV failure, and VSD where RV and LV filling change equally",
        "Any cause of a narrow split plus significant RV failure, and ASD where RV filling alone changes with respiration",
    ],
    "The fixed column reads 'Any cause of wide variable split + significant RV failure' and 'ASD (similar degree of alteration in RV & LV filling during expiration & inspiration)'.",
)

add(
    S7, 302, "recall",
    "How is a reverse or paradoxical split of S2 defined on page 302?",
    "A split heard in expiration and not in inspiration, with P2 before A2",
    [
        "A split heard in inspiration and not in expiration, with A2 before P2",
        "A split heard in both phases equally, with P2 before A2",
        "A split heard in expiration only, with A2 before P2",
    ],
    "The heading reads 'Reverse split (paradoxical split)' with 'Split heard in expiration are not in inspiration (P2 – A2)', the order inverted from normal.",
)

add(
    S7, 302, "match",
    "Match each reverse split cause to its printed side — 1) Right side pacing or ectopic, and WPW type B 2) TR 3) LBBB 4) AS, AR and hypertrophic cardiomyopathy … A) Delayed A2 from left bundle branch block B) Early P2, electrical C) Early P2, mechanical D) Delayed A2 from aortic valve or myocardial disease",
    "1-B, 2-C, 3-A, 4-D",
    ["1-C, 2-B, 3-A, 4-D", "1-B, 2-C, 3-D, 4-A", "1-D, 2-C, 3-B, 4-A"],
    "The reverse split tree gives early P2 electrically from right side pacing/ectopic and WPW type B, early P2 mechanically from TR, and delayed A2 in LBBB as against AS, AR and hypertrophic cardiomyopathy.",
)

add(
    S7, 302, "fillup",
    "The early P2 of a paradoxical split is printed for right side pacing or ectopic and for WPW syndrome type ______.",
    "B",
    ["A", "C", "D"],
    "The electrical branch reads 'WPW syndrome: Type B', the pre-excitation type that delays left-sided activation and so delays A2 into a reverse split.",
)

add(
    S7, 302, "oddoneout",
    "Pick the ODD ONE OUT — three are printed as causes of a delayed A2 in reverse split, one causes an early P2:",
    "Tricuspid regurgitation",
    ["LBBB", "Aortic stenosis", "Hypertrophic cardiomyopathy"],
    "The delayed A2 column reads LBBB, AS, AR and hypertrophic cardiomyopathy (HCM), while TR sits in the early P2 mechanical column.",
)

# ---------------------------------------------------------------- extra interactives
add(
    S1, 296, "scenario",
    "A harsh systolic murmur is best heard at the second right intercostal space and is audible over the carotid and the apex. Which printed description fits?",
    "A mixed frequency ejection systolic murmur of aortic stenosis, with the apical high-pitch element as the Gallavardin phenomenon",
    [
        "A pure low frequency murmur of mitral stenosis heard with the bell",
        "A pure high frequency murmur of mitral regurgitation heard with the diaphragm",
        "A continuous murmur of patent ductus arteriosus",
    ],
    "The mixed frequency sound is the ESM of AS, harsh at the 2nd right ICS, with low pitch radiating to the carotid and high pitch to the apex, the latter named the Gallavardin phenomenon.",
)

add(
    S2, 297, "scenario",
    "On an intracardiac recording M1 precedes T1 by 20 ms. How does that interval appear at the bedside?",
    "As a single S1, because a difference under 30 ms is not appreciated",
    [
        "As a wide split S1, because any measurable difference is audible",
        "As a fixed split S1 that widens with inspiration",
        "As a soft S1, because the components cancel each other",
    ],
    "The bracket beside M1 and T1 reads '<30 ms difference (not appreciated)', so the two components fuse into one heard sound.",
)

add(
    S3, 298, "scenario",
    "A patient with calcific mitral stenosis has a soft first heart sound. Which of the six printed factors explains it?",
    "Loss of leaflet integrity, because the calcific leaflet is immobile",
    [
        "The valve sits wide apart at end diastole and closes from a distance",
        "The PR interval is short, reducing filling before closure",
        "The chest wall is thin, dampening transmission",
    ],
    "Under integrity of the valve leaflet, 'c. Calcific for immobile leaflet (Calcific MS)' leads to a soft S1; the wide-apart position of MS would instead make S1 loud.",
)

add(
    S4, 299, "truefalse",
    "TRUE or FALSE about combined mitral stenosis and mitral regurgitation on page 299.",
    "True — S1 depends on the predominant disease",
    [
        "True — S1 is always loud regardless of the predominant lesion",
        "False — S1 is always soft because regurgitation dominates",
        "False — S1 cannot be assessed when both lesions coexist",
    ],
    "The line reads 'MS + MR: Depends on predominant disease', the single printed rule for the combination.",
)

add(
    S5, 300, "scenario",
    "At rest the A2–P2 gap measures 50 ms and during inspiration it widens further. What does page 300 call this?",
    "An appreciable physiological gap that exceeds 50 ms in inspiration because venous return rises",
    [
        "A fixed split, because the gap does not change with respiration",
        "A paradoxical split, because P2 precedes A2",
        "A single S2, because a 50 ms gap cannot be heard",
    ],
    "The page prints the resting gap as 50 ms and 'appreciable', with 'During inspiration: >50 ms (d/t ↑ venous return)'; a fixed or paradoxical split behaves differently.",
)

add(
    S7, 302, "scenario",
    "A patient's second sound is split in expiration and single in inspiration, with P2 preceding A2. What is the printed name and mechanism?",
    "A reverse or paradoxical split, from delayed A2 as in LBBB",
    [
        "A wide split, from early A2 as in LV pacing",
        "A fixed split, as in ASD",
        "A single S2, as in severe pulmonary hypertension",
    ],
    "A split heard in expiration rather than inspiration with P2 before A2 is the reverse (paradoxical) split, whose delayed A2 causes are LBBB, AS, AR and HCM.",
)

GUIDES = {
    S1: (
        "Heart sounds (p296) are brief, discrete auditory vibrations; intensity is measured in decibels and frequency in hertz, with frequency ∝ 1/amplitude.\n"
        "High frequency sounds are soft, musical or blowing, with a wide chamber pressure difference, a wider area, no thrill and the diaphragm; low frequency sounds are rough, rumbling or thud-like, with a low pressure difference, a localised area, a thrill and the bell, whose exceptions are S3, S4, tumour plop, MS, TS and Austin Flint.\n"
        "The mixed frequency sound is the ejection systolic murmur of AS — harsh at the 2nd right ICS, with low pitch radiating to the carotid and high pitch to the apex (Gallavardin).",
    ),
    S2: (
        "The cardiac cycle (p297) lasts 0.8 s, atrial systole 0.1 s against atrial diastole 0.7 s; systole 0.3 s holds isovolumetric contraction, rapid ejection and reduced ejection, and diastole 0.5 s holds protodiastole, isovolumetric relaxation, rapid filling, reduced filling and atrial systole.\n"
        "During reduced filling the AV valves are open and 70% of filling is passive, atrial systole adds 30%, then ventricular pressure exceeds atrial pressure, the AV valves close and S1 is born into isovolumetric contraction.\n"
        "The valve apparatus is leaflet, fibrous annulus and commissures; annular contraction → coaptation → sudden tensing gives S1, whose M1 and T1 lie <30 ms apart and are not appreciated separately.",
    ),
    S3: (
        "Six factors alter S1 intensity (p298): leaflet integrity (incompetent MR, perforated endocarditis and calcific MS all soften it); diastolic leaflet position (stenosis keeps the valve wide apart so it closes from a distance and is loud, as in MS); contraction velocity (bradycardia with a long PR softens, tachycardia with a short PR loudens).\n"
        "Closure timing decides too — delayed closure is loud in MS while premature closure is soft in AR — and dP/dt behaves the same way, a leaky valve losing dP/dt and softening as in MR or myocarditis while exercise and high output louden.\n"
        "Chest-wall transmission closes the list: obesity, emphysema and pericardial effusion soften all auscultatory events, whereas a thin chest wall loudens them.",
    ),
    S4: (
        "S1 is normal in AS, soft in AR from premature closure, loud and unrelated to severity in MS from wide-apart position, increased velocity and delayed closure, and soft and unrelated to severity in MR from loss of integrity and loss of dP/dt (p299).\n"
        "Loud T1 comes from TS, ASD and total anomalous pulmonary venous connection through increased tricuspid flow; the loud sound of AS is an aortic ejection click from a bicuspid valve that can be mistaken for S1; rheumatic MR with a preserved leaflet gives a soft S1 from myocarditis, MS with MR depends on the predominant lesion, and TR after pulmonary hypertension in moderate MS softens S1.\n"
        "Variable S1 varies in atrial fibrillation and flutter but is intermittent as cannon S1 in complete heart block and VT with AV dissociation; wide split S1 separates early M1 (LV ectopic or pacing, Ebstein with a sail sound) from late T1 (RBBB, TS, RA myxoma).",
    ),
    S5: (
        "Reverse split of S1 puts T1 before M1, from early T1 in right sided pacing or ectopic and from delayed M1 in LBBB or, mechanically, MS and LA myxoma (p300).\n"
        "After S1 the aortic and pulmonary valves open with ejection clicks, then rapid and reduced ejection raise aortic and pulmonary pressures to the crossover point, where aortic pressure exceeds CVP and pulmonary pressure exceeds RVP.\n"
        "The hangout interval runs from crossover pressure to valve closure and depends on pressure beyond the valve and vessel distensibility, printing 30 ms for the aorta and 80 ms for the pulmonary artery; the A2–P2 gap is 50 ms and appreciable, exceeding 50 ms in inspiration from increased venous return.",
    ),
    S6: (
        "S2 is aortic and pulmonary closure at a high frequency of 120–150 Hz, with A2 louder because aortic pressure exceeds pulmonary pressure (p301).\n"
        "A2 and P2 are governed by pressure beyond the valve (systemic HTN loudens A2, pulmonary HTN loudens P2), flow across the valve (hyperkinetic states louden both), valve mobility and vessel dilatation beyond the valve.\n"
        "AS from a bicuspid valve is loud but degenerative AS is soft, AR is soft from valve pathology and loud (tambour S2) from root disease such as syphilis, moderate MS loudens P2 and with RVF widens the split, and MR loudens P2 only with pulmonary hypertension; single S2 arises in severe PAH (single loud P2), aging, semilunar atresia, severe AS or PS and truncus arteriosus.",
    ),
    S7: (
        "A wide split of S2 exceeds 50 ms and is heard even in expiration (p302).\n"
        "Its variable causes are early A2 (LV pacing or ectopic electrically, MR mechanically) and late P2 (RBBB, pulmonary hypertension with RVF as in MS, PS, VSD with a left-to-right shunt, cardiac tamponade).\n"
        "Fixed splitting is any wide variable split with significant RV failure, or ASD where RV and LV filling change equally with respiration; the reverse or paradoxical split is heard in expiration with P2 before A2, from early P2 (right sided pacing/ectopic, WPW type B, TR) or delayed A2 (LBBB, AS, AR, HCM).",
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
