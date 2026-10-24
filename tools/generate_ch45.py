#!/usr/bin/env python3
"""Generate Chapter 45: Obstructive Sleep Apnea Syndrome (Book p264–266).

Every question is anchored to a printed line, table cell or figure caption of
uploads/03.pdf sheets 17–19 (Book pages 264–266), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 45
TITLE = "Obstructive Sleep Apnea Syndrome"
PAGES = "264-266"

S1 = "Obstructive Breathing Events in REM, the >10-second Apnea and Hypopnea Thresholds, the Apnea Hypopnea Index Bands and the Eight Risk Factors"
S2 = "Snoring and the Day-time Symptom List, the Suspect-OSAS Note, the Vagal Sudden-Death Chain, Complications, the Obsolete Epworth Scale and the Two Polysomnography Traces"
S3 = "Severe OSAS Treated with CPAP and the Nasal and Full-face Mask Captions"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(45000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(45100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p264
add(
    S1, 264, "recall",
    "Which pair of features defines obstructive sleep apnea syndrome in the Introduction on page 264?",
    "Obstructive breathing events (manifesting as snoring) plus excessive day time sleepiness/fatigue",
    [
        "Obstructive breathing events (manifesting as snoring) plus cor pulmonale",
        "Central apnoeic events plus excessive day time sleepiness/fatigue",
        "Obstructive breathing events plus morning headache as the only complaint",
    ],
    "The Introduction sentence reads 'Obstructive breathing events (manifesting as snoring) + excessive day time sleepiness/fatigue' — snoring is the event and day-time sleepiness the consequence.",
)

add(
    S1, 264, "truefalse",
    "TRUE or FALSE about the stage of sleep in which the obstructive breathing events occur, as printed on page 264.",
    "True — obstructive breathing events occur in the REM phase",
    [
        "True — obstructive breathing events occur equally in every sleep stage",
        "False — the events occur only in non-REM sleep",
        "False — the events occur only in slow-wave (deep) sleep",
    ],
    "The first bullet under 'Obstructive breathing events' is 'Occur in REM phase', before the apnea and hypopnea definitions.",
)

add(
    S1, 264, "numeric",
    "How long must breathing cease for the printed definition of apnea to be satisfied?",
    ">10 s",
    [">5 s", ">20 s", ">30 s"],
    "The page defines 'Apnea: Cessation of breathing > 10s', the same 10-second cut-off used for hypopnea on the next line.",
)

add(
    S1, 264, "fillup",
    "Hypopnea is reduced breathing >10 s in which the amplitude of breathing falls by more than ______ or there is an O₂ desaturation ≥4%.",
    "50%",
    ["25%", "30%", "75%"],
    "The bracket reads '(Amplitude of breathing falls >50% or O2 desaturation ≥4%)', so the amplitude half and the 4% desaturation are the two alternatives.",
)

add(
    S1, 264, "match",
    "Match the obstructive event to its printed threshold — 1) Apnea 2) Hypopnea … A) Reduced breathing >10 s (amplitude falls >50% or O₂ desaturation ≥4%) B) Cessation of breathing >10 s",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The two bullets read 'Apnea: Cessation of breathing >10s' and 'Hypopnea: Reduced breathing >10s (Amplitude of breathing falls >50% or O2 desaturation ≥4%)'.",
)

add(
    S1, 264, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed as signs of disturbed sleep on page 264, one is not:",
    "Nocturnal dyspnea",
    ["Snoring", "Grunting", "Choking"],
    "The line reads 'Signs of disturbed sleep: Snoring, grunting, choking.' Nocturnal dyspnea is not part of that list.",
)

add(
    S1, 264, "recall",
    "Which sequence describes obesity hypoventilation syndrome in the Note on page 264?",
    "Obesity → hypoventilation → ↑PaCO₂, and excessive day time sleepiness is not present usually",
    [
        "Obesity → hypoventilation → ↑PaCO₂, and excessive day time sleepiness is always present",
        "Obesity → hyperventilation → ↓PaCO₂, and excessive day time sleepiness is not present usually",
        "Obesity → airflow obstruction → ↓PaO₂, and excessive day time sleepiness is not present usually",
    ],
    "The note is 'Obesity hypoventilation syndrome: Obesity → hypoventilation → ↑PaCO2. Excessive day time sleepiness not present usually.' — the absent sleepiness is what separates it from OSAS.",
)

add(
    S1, 264, "fillup",
    "The Apnea Hypopnea Index divides the total number of apnea and hypopnea by the ______.",
    "total sleep time",
    ["total study time", "total REM time", "total awake time"],
    "The fraction is printed as 'Total number of apnea and hypopnea / Total sleep time' — hence an index per hour of sleep, not per hour in bed.",
)

add(
    S1, 264, "match",
    "Match each Apnea Hypopnea Index band to its printed label — 1) <5 2) 5–15 3) 15–30 4) >30 … A) Normal B) Mild OSAS C) Moderate OSAS D) Severe OSAS",
    "1-A, 2-B, 3-C, 4-D",
    ["1-B, 2-A, 3-C, 4-D", "1-A, 2-B, 3-D, 4-C", "1-A, 2-C, 3-B, 4-D"],
    "The ladder reads '<5: Normal. 5–15: mild OSAS. 15–30: moderate OSAS. >30: Severe OSAS', with the last line adding CPAP.",
)

add(
    S1, 264, "numeric",
    "Which bands are bracketed together as needing only lifestyle modification?",
    "5–15 mild and 15–30 moderate",
    ["<5 normal and 5–15 mild", "15–30 moderate and >30 severe", "All bands below 30, including the normal band"],
    "The brace joins '5–15: mild OSAS' and '15–30: moderate OSAS' to 'Needs only lifestyle modification'; only '>30: Severe OSAS' needs CPAP.",
)

add(
    S1, 264, "scenario",
    "A 54-year-old obese man has an Apnea Hypopnea Index of 32 on polysomnography. Using the printed bands, he falls in which group and needs what treatment?",
    "Severe OSAS (>30) needing CPAP",
    [
        "Moderate OSAS (15–30) needing only lifestyle modification",
        "Severe OSAS (>30) needing only lifestyle modification",
        "Mild OSAS (5–15) needing CPAP",
    ],
    "The severity ladder places >30 in 'Severe OSAS → Needs treatment using CPAP (Continuous positive airway pressure)'; 32 is therefore severe and CPAP-treated.",
)

add(
    S1, 264, "oddoneout",
    "Pick the ODD ONE OUT — three are printed risk factors for OSAS on page 264, one is not:",
    "Female sex with a M : F ratio of 1 : 3",
    ["Central fat distribution", "Age 50–60 yrs", "Postmenopausal state"],
    "The risk list prints 'male sex (M : F = 3 : 1)' with obesity, central fat, age 50–60, postmenopausal state, alcohol, sedatives and smoking — the sex ratio is inverted in the odd option.",
)

add(
    S1, 264, "fillup",
    "The risk factor line prints the sex distribution of OSAS as M : F = ______.",
    "3 : 1",
    ["1 : 3", "2 : 1", "1 : 1"],
    "The bullet is 'male sex (M : F = 3 : 1)', i.e. three men for every woman, before 'Age 50–60 yrs' and 'Postmenopausal state'.",
)

# ---------------------------------------------------------------- Unit 2: p265
add(
    S2, 265, "recall",
    "Which description of snoring is printed under Clinical features on page 265?",
    "Cardinal symptom, intermittent/waxing & waning with long periods of silence, and more in the supine position",
    [
        "Cardinal symptom, continuous and unvarying, and more in the lateral position",
        "A late symptom, intermittent/waxing & waning, and more in the upright position",
        "Cardinal symptom, intermittent/waxing & waning, and abolished in the supine position",
    ],
    "The snoring block reads 'Cardinal symptom', 'Intermittent/waxing & waning/long periods of silence' and 'more in supine position' — the silence is what distinguishes it from continuous snoring.",
)

add(
    S2, 265, "fillup",
    "Two night-time symptoms listed immediately after snoring are nocturia and ______.",
    "sudden waking up at night",
    ["night sweats", "nocturnal cough", "sleep paralysis"],
    "The list runs 'Snoring: ... • Nocturia. • sudden waking up at night.' before the day-time symptom block begins.",
)

add(
    S2, 265, "match",
    "Match each day-time symptom to its printed descriptor — 1) Morning headache/confusion 2) Cognitive defects 3) Sexual dysfunction … A) Poor concentration, personality & mood changes (depression & anxiety) B) Impotence & decreased libido C) Non-restorative sleep",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "The brackets print 'morning headache/confusion (Non-restorative sleep)', 'cognitive defects: Poor concentration, personality mood changes (Depression & anxiety)' and 'sexual dysfunction: impotence, & decreased libido'.",
)

add(
    S2, 265, "recall",
    "Which two situations does the Note box direct you to suspect OSAS in?",
    "Unexplained pulmonary hypertension and unexplained polycythemia",
    [
        "Unexplained systemic hypertension and unexplained thrombocytopenia",
        "Unexplained pulmonary hypertension and unexplained eosinophilia",
        "Unexplained cor pulmonale and unexplained anemia",
    ],
    "The boxed note reads 'Always suspect OSAS in: • unexplained pulmonary hypertension. • unexplained polycythemia.' — both qualified by 'unexplained'.",
)

add(
    S2, 265, "scenario",
    "A 46-year-old snorer is found to have a raised hemoglobin and hematocrit with no hematological disease, and echocardiography shows pulmonary hypertension without a cardiac cause. Which sleep diagnosis should be suspected from the printed note?",
    "OSAS",
    ["Obesity hypoventilation syndrome", "Central sleep apnea", "Narcolepsy"],
    "Both 'unexplained pulmonary hypertension' and 'unexplained polycythemia' sit inside the suspect-OSAS box, so the combination points to OSAS rather than to obesity hypoventilation, whose day-time sleepiness is usually absent.",
)

add(
    S2, 265, "recall",
    "Which chain is drawn under 'Risk of sudden cardiac death' in Complications on page 265?",
    "Vagal stimulation → bradycardia + hypoxia → cardiac rhythm abnormality (premature beat, asystole, VT, cardiac arrest)",
    [
        "Sympathetic stimulation → tachycardia + hypertension → cardiac rhythm abnormality (premature beat, asystole, VT, cardiac arrest)",
        "Vagal stimulation → bradycardia + hypoxia → left ventricular hypertrophy and diastolic failure",
        "Vagal stimulation → tachycardia + hypoxia → cardiac rhythm abnormality (premature beat, asystole, VT, cardiac arrest)",
    ],
    "The flow prints 'vagal stimulation → Bradycardia + Hypoxia' and then 'cardiac rhythm abnormality (Premature beat, asystole, VT, cardiac arrest)'.",
)

add(
    S2, 265, "match",
    "Match each complication group to its printed mechanism — 1) Stroke and congestive cardiac failure 2) Metabolic syndrome … A) No mechanism bracketed on the page B) Due to HTN",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The brace 'due to HTN' encloses stroke and congestive cardiac failure only, while metabolic syndrome stands alone with no bracket on the page.",
)

add(
    S2, 265, "oddoneout",
    "Pick the ODD ONE OUT — three of these arrhythmias are printed inside the complication chain, one is not:",
    "Atrial flutter",
    ["Premature beat", "Asystole", "Ventricular tachycardia"],
    "The bracket prints 'Premature beat, asystole, VT, cardiac arrest'. Atrial flutter is not anywhere in that printed list of rhythm abnormalities.",
)

add(
    S2, 265, "fillup",
    "The Epworth sleepiness scale questionnaire is dismissed on page 265 as ______.",
    "obsolete",
    ["specific", "sensitive", "mandatory"],
    "Under Investigations the page writes 'eps-worth sleepiness scale questionnaire: obsolete', leaving polysomnography as the investigation that follows.",
)

add(
    S2, 265, "recall",
    "What do the two polysomnography figures on page 265 demonstrate?",
    "Central apnea without respiratory effort and obstructive apnea with persistent respiratory effort",
    [
        "Central apnea with persistent respiratory effort and obstructive apnea without respiratory effort",
        "Obstructive apnea in REM and obstructive apnea in non-REM sleep",
        "Cheyne–Stokes respiration and obesity hypoventilation",
    ],
    "The two captions read 'Central apnea without respiratory effort' and 'Obstructive apnea with persistent respiratory effort' — effort is the discriminator between the two traces.",
)

add(
    S2, 265, "scenario",
    "A polysomnography trace shows repeated cessation of airflow with continued, increasing respiratory effort. Which caption from page 265 matches this trace?",
    "Obstructive apnea with persistent respiratory effort",
    [
        "Central apnea without respiratory effort",
        "Central apnea with persistent respiratory effort",
        "Obstructive apnea with absent respiratory effort",
    ],
    "Airflow stops while effort persists in the second trace, captioned 'Obstructive apnea with persistent respiratory effort'; loss of effort would make it central.",
)

add(
    S2, 265, "oddoneout",
    "Pick the ODD ONE OUT — three are day-time symptoms printed on page 265, one is a night-time symptom from the same page:",
    "Sudden waking up at night",
    ["Dry throat", "GERD", "Impotence and decreased libido"],
    "Morning headache, dry throat, day-time sleepiness, cognitive defects, sexual dysfunction and GERD sit in the day-time list, whereas 'sudden waking up at night' is printed with nocturia above it.",
)

# ---------------------------------------------------------------- Unit 3: p266
add(
    S3, 266, "recall",
    "What treatment is printed for severe OSAS on page 266?",
    "CPAP",
    ["Uvulopalatopharyngoplasty", "Mandibular advancement splint", "Nocturnal oxygen"],
    "The page states 'Treatment: Severe OSAS : CPAP', followed only by two mask photographs.",
)

add(
    S3, 266, "fillup",
    "CPAP, the treatment of severe OSAS, stands for ______ positive airway pressure.",
    "continuous",
    ["cyclic", "central", "constant"],
    "Page 264 had already expanded 'CPAP (Continuous positive airway pressure)' and page 266 repeats the acronym as the severe-OSAS treatment.",
)

add(
    S3, 266, "match",
    "Match each CPAP mask caption on page 266 to its printed picture — 1) Left photograph 2) Right photograph … A) A man wearing a full face mask B) A sleeping man with a nasal mask",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The left photograph is captioned 'Nasal mask' and the right 'Full face mask'; the page prints no third mask type.",
)

add(
    S3, 266, "truefalse",
    "TRUE or FALSE about treatment on page 266.",
    "True — severe OSAS is treated with CPAP, shown in nasal and full face mask forms",
    [
        "True — severe OSAS is treated with CPAP, and only a nasal mask is illustrated",
        "False — severe OSAS is treated with surgery",
        "False — CPAP is restricted to mild OSAS",
    ],
    "The single treatment line reads 'Severe OSAS : CPAP', and the two captions show both a nasal mask and a full face mask.",
)

add(
    S3, 266, "oddoneout",
    "Pick the ODD ONE OUT — three statements about the page 266 treatment block are true, one contradicts it:",
    "CPAP is reserved for mild OSAS, while severe disease needs lifestyle modification alone",
    [
        "The treatment named for severe OSAS is CPAP",
        "A nasal mask is illustrated as one way of delivering CPAP",
        "A full face mask is illustrated as another way of delivering CPAP",
    ],
    "Page 266 prints only 'Severe OSAS : CPAP' with the nasal and full face masks; lifestyle modification alone was the page 264 brace for mild and moderate disease, the exact reverse.",
)

GUIDES = {
    S1: (
        "OSAS (p264) = obstructive breathing events manifesting as snoring plus excessive day time sleepiness/fatigue; the events occur in the REM phase, apnea is cessation >10 s and hypopnea is reduced breathing >10 s with amplitude falling >50% or O₂ desaturation ≥4%.\n"
        "Signs of disturbed sleep are snoring, grunting and choking, and obesity hypoventilation instead gives obesity → hypoventilation → ↑PaCO₂ with day-time sleepiness usually absent.\n"
        "AHI = total number of apnea and hypopnea / total sleep time: <5 normal, 5–15 mild, 15–30 moderate (the two bracketed as needing only lifestyle modification) and >30 severe needing CPAP; risk factors are obesity, central fat, male 3:1, age 50–60, postmenopausal state, alcohol, sedatives and smoking.",
    ),
    S2: (
        "Snoring (p265) is the cardinal symptom, intermittent/waxing & waning with long periods of silence and worse supine; nocturia and sudden waking at night share the night list with morning headache/confusion (non-restorative sleep), dry throat, sleepiness, cognitive and mood change, sexual dysfunction and GERD.\n"
        "Always suspect OSAS in unexplained pulmonary hypertension and unexplained polycythemia; sudden cardiac death runs vagal stimulation → bradycardia + hypoxia → rhythm abnormality (premature beat, asystole, VT, arrest), while stroke and CCF are bracketed 'due to HTN' beside metabolic syndrome.\n"
        "The Epworth questionnaire is obsolete and polysomnography supplies the two captions — central apnea without respiratory effort against obstructive apnea with persistent respiratory effort.",
    ),
    S3: (
        "Page 266 has a single treatment line, 'Severe OSAS : CPAP', matching the >30 AHI rule on page 264.\n"
        "The only illustrations are the two delivery masks, captioned 'Nasal mask' and 'Full face mask'.\n"
        "Mild and moderate disease had already been bracketed as needing only lifestyle modification, so CPAP is not a mild-disease option.",
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
        title = sec
        guide = GUIDES[sec][0] if isinstance(GUIDES[sec], (list, tuple)) else GUIDES[sec]
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
