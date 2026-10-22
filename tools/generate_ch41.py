#!/usr/bin/env python3
"""Generate Chapter 41: Pulmonary Eosinophilia (Book p249–252).

Every question is anchored to a printed line, table cell or figure caption of
uploads/03.pdf sheets 2–5 (Book pages 249–252), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 41
TITLE = "Pulmonary Eosinophilia"
PAGES = "249-252"

S1 = "Eosinophilic Lung Disease Defined, Its Three Defining Features, Known versus Unknown Causes and Diseases Not Classified under ELD"
S2 = "Parasite-Related ELD (Loeffler Syndrome versus Lung Fluke Invasion), Drugs and Toxins, and Tropical Pulmonary Eosinophilia Pathogenesis"
S3 = "Tropical Pulmonary Eosinophilia: Acute-on-Chronic Symptoms, Laboratory and Radiological Findings, DEC Treatment, and the Unknown-Cause Table Histories and Presentations"
S4 = "Unknown Causes of ELD: Investigations in AEP, CEP and Idiopathic Hypereosinophilic Syndrome with Their Steroid Responses"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(41000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(41100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p249
add(
    S1, 249, "recall",
    "Which opening statements define pulmonary eosinophilia on page 249?",
    "AKA eosinophilic lung disease (ELD), with increased eosinophils within the pulmonary airway more than the parenchyma, the role of eosinophils in eosinophilic pneumonia pathogenesis not clear, and peripheral counts not elevated in every type of ELD",
    [
        "AKA eosinophilic lung disease (ELD), with increased eosinophils within the pulmonary parenchyma more than the airway, the role of eosinophils fully established, and peripheral counts elevated in every type of ELD",
        "AKA eosinophilic lung disease (ELD), with increased eosinophils within the pulmonary airway more than the parenchyma, the role of eosinophils in eosinophilic pneumonia pathogenesis not clear, and peripheral counts diagnostic in every type of ELD",
        "AKA eosinophilic airway disease, with increased eosinophils confined to blood, the role of eosinophils not clear, and peripheral counts not elevated in every type of ELD",
    ],
    "The head of the page reads 'AKA eosinophilic lung disease (ELD)', 'Increased number of eosinophils within pulmonary airway > parenchyma', 'Role of eosinophils in pathogenesis of eosinophilic pneumonia not clear' and 'Peripheral blood eosinophil counts: Not elevated in all type of ELD'.",
)

add(
    S1, 249, "recall",
    "Which three defining features of ELD are numbered on page 249?",
    "Increased eosinophils on bronchoalveolar lavage (BAL); lung tissue eosinophilia; and peripheral blood eosinophilia with a lung-infiltrate abnormality on imaging",
    [
        "Increased eosinophils in sputum; lung tissue eosinophilia; and peripheral blood eosinophilia with a lung-infiltrate abnormality on imaging",
        "Increased eosinophils on BAL; pleural fluid eosinophilia; and peripheral blood eosinophilia alone",
        "Increased eosinophils on BAL; lung tissue eosinophilia; and a raised serum IgE with a normal image",
    ],
    "The Defining features are '1. ↑ eosinophils on Broncho Alveolar Lavage (BAL). 2. Lung tissue eosinophilia. 3. Peripheral blood eosinophilia + abnormality (Lung infiltrate) on imaging.' Any one route — lavage, tissue, or blood plus imaging — defines the group.",
)

add(
    S1, 249, "match",
    "Match each known cause in the page 249 etiology tree with its printed mechanism or member — 1) Parasite-related hypersensitivity 2) Parasite-related lung invasion 3) The remaining two known causes … A) Lung fluke B) Drug and toxin, tropical pulmonary eosinophilia, and ABPA counted within the four known heads C) Loeffler syndrome",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "The 'Known (4)' arm branches parasite-related disease into hypersensitivity causing Loeffler syndrome and lung invasion by lung fluke, and completes the four heads with drug & toxin, tropical pulmonary eosinophilia (TPE) and allergic bronchopulmonary aspergillosis (ABPA) as the bulleted known causes.",
)

add(
    S1, 249, "recall",
    "Which four diseases form the 'Unknown (4)' arm of the etiology tree?",
    "Acute eosinophilic pneumonia (AEP), chronic eosinophilic pneumonia (CEP), allergic granulomatosis with polyangiitis (AGPA) / eosinophilic GPA (EGPA) / Churg-Strauss syndrome, and idiopathic hypereosinophilic syndrome",
    [
        "Acute eosinophilic pneumonia (AEP), chronic eosinophilic pneumonia (CEP), granulomatosis with polyangiitis (GPA), and idiopathic hypereosinophilic syndrome",
        "Acute eosinophilic pneumonia (AEP), Loeffler syndrome, allergic granulomatosis with polyangiitis (AGPA) / eosinophilic GPA (EGPA) / Churg-Strauss syndrome, and idiopathic hypereosinophilic syndrome",
        "Acute eosinophilic pneumonia (AEP), chronic eosinophilic pneumonia (CEP), allergic granulomatosis with polyangiitis (AGPA) / eosinophilic GPA (EGPA) / Churg-Strauss syndrome, and tropical pulmonary eosinophilia",
    ],
    "The Unknown arm lists AEP, CEP, 'Allergic granulomatosis with polyangiitis (AGPA) / Eosinophilic GPA (EGPA)/Churg Strauss syndrome' under its three printed names, and idiopathic hypereosinophilic syndrome. Loeffler syndrome and TPE sit on the known side.",
)

add(
    S1, 249, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed on page 249 as diseases with eosinophilia but not classified under ELD, one is a true ELD cause:",
    "Allergic bronchopulmonary aspergillosis (ABPA)",
    [
        "Bronchial Asthma",
        "Langerhans cell histiocytosis",
        "IgG4 related connective tissue disorder",
    ],
    "The Note lists bronchial Asthma, 'Cytogenic organising pneumonia' as printed, Langerhans cell histiocytosis and IgG4 related connective tissue disorder as eosinophilic diseases outside ELD. ABPA is one of the four known ELD heads in the tree above.",
)

add(
    S1, 249, "recall",
    "Which two not-classified diseases share an arrow on page 249, and where does it send them?",
    "'Cytogenic organising pneumonia' as printed and Langerhans cell histiocytosis are braced together and arrowed to ILD",
    [
        "Bronchial Asthma and IgG4 related connective tissue disorder are braced together and arrowed to ILD",
        "'Cytogenic organising pneumonia' as printed and bronchial Asthma are braced together and arrowed to ELD",
        "Langerhans cell histiocytosis and IgG4 related connective tissue disorder are braced together and arrowed to ILD",
    ],
    "In the Note, 'Cytogenic organising pneumonia' (printed spelling, for cryptogenic organizing pneumonia) and Langerhans cell histiocytosis share one brace arrowed '→ ILD', returning both to the Chapter 39 grouping; the same Note adds that hypersensitivity pneumonitis is not grouped under ELD.",
)

add(
    S1, 249, "numeric",
    "Which BAL threshold and which two diseases close page 249?",
    "BAL at or above 40%, in 'TEP' as printed (for TPE) and CEP",
    [
        "BAL at or above 25%, in TPE and AEP",
        "BAL at or above 40%, in ABPA and CEP",
        "BAL above 60%, in 'TEP' as printed (for TPE) and CEP",
    ],
    "The last bullet reads 'ELD with BAL ≥40%: TEP. CEP.' — TEP being the page's transposed printing of TPE, whose own BAL figure of at least 40% recurs on page 251.",
)

add(
    S1, 249, "truefalse",
    "TRUE or FALSE about the page 249 classification boundaries.",
    "True — hypersensitivity pneumonitis is stated to be not grouped under ELD, even though it is an eosinophil-associated hypersensitivity disease in neighbouring chapters",
    [
        "False — hypersensitivity pneumonitis heads the list of unknown ELD causes",
        "False — bronchial Asthma is classified under ELD because its inflammation is eosinophilic",
        "True — hypersensitivity pneumonitis is grouped under ELD as a known cause",
    ],
    "The Note is explicit: 'Hypersensitivity pneumonitis not grouped under ELD', and bronchial Asthma leads the 'diseases with eosinophilia but not classified under ELD' list despite the eosinophilic inflammation of page 243.",
)


# ---------------------------------------------------------------- Unit 2: p250
add(
    S2, 250, "match",
    "Match each parasite-related table row with its Loeffler versus lung-invasion pair on page 250 — 1) Organism 2) Mechanism 3) Symptoms 4) Treatment … A) Type 1 hypersensitivity to larvae versus metacercaria reaching lung and maturing to adult worm larvae as printed B) Ascaris lumbricoides most common, ahead of Ancylostoma, Necator and Strongyloides, versus the lung fluke Paragonimus westermani C) Self-limiting, resolving in 1–2 weeks, versus praziquantel as DOC D) Asthma mimic with cough, substernal discomfort and wheeze plus low grade fever, versus a dash",
    "1-B, 2-A, 3-D, 4-C",
    ["1-A, 2-B, 3-D, 4-C", "1-B, 2-A, 3-C, 4-D", "1-B, 2-D, 3-A, 4-C"],
    "The Loeffler column gives Ascaris (m/c) > Ancylostoma/Necator/Strongyloides, type 1 hypersensitivity to larvae, an Asthma-mimicking symptom set with low grade fever, and self-limited resolution in 1–2 weeks; the invasion column gives Paragonimus westermani maturing from metacercaria in lung, a dash for symptoms, and praziquantel as drug of choice.",
)

add(
    S2, 250, "recall",
    "Which findings fill the Loeffler syndrome column on page 250?",
    "Peripheral eosinophilia, raised IgE and migratory eosinophilic lung infiltrates",
    [
        "Peripheral eosinophilia, normal IgE and fixed eosinophilic lung infiltrates",
        "BAL eosinophilia only, raised IgE and cavitating nodules",
        "Peripheral eosinophilia, raised IgE and chocolate colored sputum",
    ],
    "The Findings cell reads 'Peripheral eosinophilia, ↑ IgE, migratory eosinophilic lung infiltrates'. Migratory infiltrates are the type 1 signature that hypersensitivity pneumonitis on page 257 is defined against.",
)

add(
    S2, 250, "recall",
    "Which pleural, lung and diagnostic findings fill the lung-invasion column?",
    "Pleura: eosinophilic pleural effusion; lung: cavitating nodules, ground glass opacification and chocolate colored sputum, with eosinophilia positive; diagnosis by eggs in sputum or ELISA",
    [
        "Pleura: eosinophilic pleural effusion; lung: migratory infiltrates and chocolate colored sputum; diagnosis by eggs in stool or ELISA",
        "Pleura: chylous effusion; lung: cavitating nodules, ground glass opacification and chocolate colored sputum; diagnosis by eggs in sputum or ELISA",
        "Pleura: eosinophilic pleural effusion; lung: cavitating nodules, ground glass opacification and brownish mucosal plugs; diagnosis by skin test",
    ],
    "The invasion cell reads 'Pleura: Eosinophilic pleural effusion. Lung: Cavitating nodules, ground glass opacification, chocolate colored sputum. Eosinophilia +ve. Diagnosis: Eggs in sputum or ELISA.' Lung fluke reappears as the first cause of eosinophils in pleural fluid on page 263.",
)

add(
    S2, 250, "scenario",
    "A child with Ascaris develops cough, substernal discomfort, wheeze and low grade fever; blood shows eosinophilia with raised IgE and the film shows shifting infiltrates that clear within a fortnight untreated. Which table column and mechanism is this?",
    "Loeffler syndrome — type 1 hypersensitivity to larvae, self limiting in 1–2 weeks",
    [
        "Lung invasion by Paragonimus — metacercaria maturing in lung, treated with praziquantel",
        "Loeffler syndrome — type 4 hypersensitivity to adults, treated with praziquantel",
        "Tropical pulmonary eosinophilia — hypersensitivity to microfilariae, treated with DEC",
    ],
    "Ascaris lumbricoides heads the Loeffler organisms, its mechanism is type 1 hypersensitivity to larvae, its symptoms mimic Asthma with low grade fever, its findings are migratory infiltrates, and it is 'Self limiting and resolve in 1–2 weeks'.",
)

add(
    S2, 250, "recall",
    "Which drug and toxin list is printed under known causes of ELD on page 250, and which entry leads it?",
    "NSAIDs, marked most common, then L-tryptophan, rapeseed oil, nitrofurantoin, minocycline and ampicillin",
    [
        "Nitrofurantoin, marked most common, then NSAIDs, L-tryptophan, rapeseed oil, minocycline and ampicillin",
        "NSAIDs, marked most common, then L-tryptophan, rapeseed oil, nitrofurantoin, methotrexate and ampicillin",
        "NSAIDs, marked most common, then L-tryptophan, mustard oil, nitrofurantoin, minocycline and amoxicillin",
    ],
    "Under 'Drug & Toxin' the bullets read 'NSAIDs (m/c)', L-Tryptophan, rapeseed oil, nitrofurantoin, minocycline and ampicillin. Rapeseed oil echoes the toxic rapeseed oil of pulmonary hypertension on page 214.",
)

add(
    S2, 250, "recall",
    "Which sex ratio, organisms and pathogenesis open tropical pulmonary eosinophilia on page 250?",
    "Males more than females; Wuchereria bancrofti and Brugia malayi; hypersensitivity to microfilarial larvae",
    [
        "Females more than males; Wuchereria bancrofti and Brugia malayi; direct invasion by adult filariae",
        "Males more than females; Ascaris lumbricoides and Strongyloides; hypersensitivity to microfilarial larvae",
        "Males equal to females; Wuchereria bancrofti and Brugia malayi; hypersensitivity to microfilarial larvae",
    ],
    "The TPE block reads 'm > F', 'Organism: Wuchereria bancrofti, Brugia malayi' and 'Pathogenesis: Hypersensitivity to microfilarial larvae'. The hypersensitivity — not the worm burden — is the mechanism, as in Loeffler syndrome above it.",
)

add(
    S2, 250, "oddoneout",
    "Pick the ODD ONE OUT — three of these bullets are printed on page 250 as jointly suggesting the microfilarial association in TPE, one is not:",
    "Eggs demonstrated in sputum",
    [
        "Microfilariae demonstrated in lung, liver and lymph node",
        "High antifilarial antibody titres that diminish after cure",
        "Dramatic response to anti-filarial treatment",
    ],
    "The brace collects microfilariae in lung/liver/LN, high antifilarial antibody titres falling after cure, and dramatic response to anti-filarial treatment as together suggesting 'association with microfilariae'. Eggs in sputum diagnose the lung fluke in the table above.",
)

add(
    S2, 250, "fillup",
    "In TPE the three evidence bullets are braced to the conclusion: 'Suggest association with ______'.",
    "microfilariae",
    ["adult filariae", "metacercariae", "Ascaris larvae"],
    "The brace reads 'Suggest association with microfilariae', matching the pathogenesis line 'Hypersensitivity to microfilarial larvae'. Metacercariae belong to Paragonimus in the same page's table.",
)


# ---------------------------------------------------------------- Unit 3: p251
add(
    S3, 251, "match",
    "Match each TPE symptom component on page 251 with its printed contents — 1) Chronic component 2) Acute component … A) Paroxysmal dry cough with dyspnoea and wheeze worse at night, stimulating status asthmaticus as printed B) Malaise, anorexia and weight loss with or without hepatosplenomegaly and lymphadenopathy",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "As an 'Acute on chronic disease', TPE couples a chronic component of malaise, anorexia and weight loss ± hepatosplenomegaly/lymphadenopathy with an acute component of paroxysmal dry cough and nocturnal dyspnoea/wheeze that '(stimulate status asthmaticus)' as printed, for simulate.",
)

add(
    S3, 251, "numeric",
    "Which three laboratory numbers are printed for TPE investigations?",
    "Marked peripheral eosinophilia above 3000 cells/mm³, BAL intense eosinophilic alveolitis at or above 40%, and serum IgE above 1000 u/ml as printed",
    [
        "Marked peripheral eosinophilia above 1500 cells/mm³, BAL intense eosinophilic alveolitis at or above 40%, and serum IgE above 1000 u/ml as printed",
        "Marked peripheral eosinophilia above 3000 cells/mm³, BAL eosinophils at or above 25%, and serum IgE above 500 u/ml as printed",
        "Marked peripheral eosinophilia above 3000 cells/mm³, BAL intense eosinophilic alveolitis at or above 40%, and serum IgE above 100 u/ml as printed",
    ],
    "Laboratory findings read 'marked peripheral eosinophilia (> 3000 cells/mm³)', 'BAL: Intense eosinophilic alveolitis (≥ 40 %)' and '↑ S. IgE (> 1000 u/ml)'. The 1500 figure belongs to idiopathic hypereosinophilic syndrome on page 252.",
)

add(
    S3, 251, "recall",
    "Which radiological findings and caption are printed for TPE?",
    "Bilateral indefinite mottling uniformly in both lung fields (middle and lower), increased bronchovascular markings, and cavitation with pleural effusion — the film captioned 'mottling pattern in x ray'",
    [
        "Bilateral indefinite mottling uniformly in both lung fields (upper and middle), increased bronchovascular markings, and cavitation with pleural effusion — the film captioned 'mottling pattern in x ray'",
        "Unilateral definite mottling, decreased bronchovascular markings, and honeycombing — the film captioned 'mottling pattern in x ray'",
        "Bilateral indefinite mottling uniformly in both lung fields (middle and lower), increased bronchovascular markings, and pleural effusion without cavitation — the film captioned 'reverse bat wing'",
    ],
    "Radiological findings read 'B/L indefinite mottling uniformly in both lung fields (middle & lower)', '↑ bronchovascular markings' and 'Cavitation and pleural effusion', and the chest film is captioned 'mottling pattern in x ray'.",
)

add(
    S3, 251, "management",
    "Which TPE treatment statement, dose and course bullets are printed on page 251?",
    "DOC diethylcarbamazine (DEC) 2 mg/kg orally three times daily for 14–21 days / 4 weeks as printed, directly filaricidal to adult worms and microfilariae, with clinical improvement in 7 days and acute relapse in up to 20% requiring higher doses",
    [
        "DOC praziquantel for 14–21 days, directly filaricidal to adult worms and microfilariae, with clinical improvement in 7 days and acute relapse in up to 20% requiring higher doses",
        "DOC diethylcarbamazine (DEC) 2 mg/kg orally three times daily for 14–21 days / 4 weeks as printed, active only against microfilariae, with clinical improvement in 7 days and no relapses",
        "DOC diethylcarbamazine (DEC) 6 mg/kg single dose, directly filaricidal to adult worms and microfilariae, with clinical improvement in 7 days and acute relapse in up to 20% requiring higher doses",
    ],
    "Treatment reads 'DOC: Diethylcarbamazine (DEC) 2 mg/kg orally TID for 14 – 21 days / 4 weeks', 'Directly filaricidal to both adult & microfilariae', 'Clinical improvement in 7 days' and 'Acute relapse in upto 20% require higher doses'. Praziquantel was the lung-fluke DOC on page 250.",
)

add(
    S3, 251, "match",
    "Match each unknown-cause column with its printed History and Pathogenesis rows on page 251 — 1) AEP 2) CEP 3) Idiopathic hypereosinophilic syndrome … A) History atopy in 33–50%, pathogenesis a dash B) History a dash, pathogenesis a myeloproliferative disorder with JAK2/PDGFRα mutation C) History restarted smoking, pathogenesis a dash",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "History gives 'Restarted smoking' for AEP, 'Atopy (33 – 50 %)' for CEP and a dash for the hypereosinophilic syndrome, while Pathogenesis is dashed for both pneumonias and names a 'myeloproliferative disorder: JAK2/PDGFRα mutation' only for the syndrome.",
)

add(
    S3, 251, "recall",
    "Which presentation timeline is drawn for acute eosinophilic pneumonia on page 251?",
    "Viral fever-like symptoms of fever and cough progressing over 2–3 days to dyspnea, tachypnea and hypoxia in an ARDS-like presentation, lasting 3–4 weeks",
    [
        "Viral fever-like symptoms of fever and cough progressing over 2–3 weeks to dyspnea, tachypnea and hypoxia in an ARDS-like presentation, lasting 3–4 days",
        "Subacute low grade fever, wheeze and night sweats over 2–3 days, lasting 3–4 weeks",
        "Viral fever-like symptoms progressing over 2–3 days to hemoptysis and cavitation, lasting 3–4 weeks",
    ],
    "The AEP cell arrows 'viral fever like symptoms (fever, cough) — 2–3 days — Dyspnea, tachypnea, hypoxia (ARDS like presentation)' and adds 'Lasts 3–4 weeks'. ARDS and crazy-pavement AEP were already cross-referenced on page 225.",
)

add(
    S3, 251, "recall",
    "Which presentation fills the chronic eosinophilic pneumonia column?",
    "A 30–40 year old with females more than males, subacute presentation, low grade fever, wheeze, night sweats and weight loss, plus cough, dyspnea and ARDS",
    [
        "A 30–40 year old with males more than females, acute presentation, high grade fever and weight gain, plus cough and dyspnea",
        "A 50–70 year old with females more than males, subacute presentation, low grade fever, wheeze, night sweats and weight loss, plus cough, dyspnea and ARDS",
        "A 30–40 year old with females more than males, subacute presentation, low grade fever, wheeze, night sweats and weight loss, without any ARDS mention",
    ],
    "The CEP cell reads '30 – 40 yr (F > M)', 'Subacute presentation', 'Low grade fever, wheeze, night sweats, weight loss' and 'Cough, dyspnea, ARDS'. Both eosinophilic pneumonias can thus reach an ARDS picture by this table.",
)

add(
    S3, 251, "recall",
    "Which multisystem presentation is printed for idiopathic hypereosinophilic syndrome?",
    "End-organ damage across respiratory system, CNS, CVS and peripheral nerves: RS in 40% with TB-like disease, ARDS and pulmonary HTN; CNS neuropsychiatric dysfunction in 60%; CVS eosinophilic myocarditis and endomyocardial fibrosis",
    [
        "End-organ damage across respiratory system, CNS, CVS and peripheral nerves: RS in 60% with TB-like disease, ARDS and pulmonary HTN; CNS neuropsychiatric dysfunction in 40%; CVS eosinophilic myocarditis and endomyocardial fibrosis",
        "Lung-limited disease: RS in 40% with TB-like disease, ARDS and pulmonary HTN, and no cardiac involvement printed",
        "End-organ damage across respiratory system, CNS, CVS and peripheral nerves: RS in 40% with TB-like disease, ARDS and pulmonary HTN; CNS neuropsychiatric dysfunction in 60%; CVS valvular regurgitation only",
    ],
    "The cell lists 'multisystem involvement: End organ damage', 'RS + CNS + CVS + peripheral neuropathy', 'RS (40%): TB like, ARDS, pulm HTN', 'CNS: Neuropsychiatric dysfunction (60 %)' and 'CVS: Eosinophilic myocarditis, endomyocardial fibrosis'. The percentages belong to RS 40 and CNS 60 in that order.",
)

add(
    S3, 251, "scenario",
    "A man who has just restarted smoking develops fever and cough, then within three days is tachypneic and hypoxic with an ARDS-like picture that settles over a month. Which unknown-cause column is he in?",
    "Acute eosinophilic pneumonia",
    [
        "Chronic eosinophilic pneumonia",
        "Idiopathic hypereosinophilic syndrome",
        "Tropical pulmonary eosinophilia",
    ],
    "Restarted smoking is the AEP history cell, and its 2–3 day progression from viral-like symptoms to ARDS-like hypoxia lasting 3–4 weeks is drawn only in that column. CEP is the subacute disease of atopic women aged 30–40.",
)


# ---------------------------------------------------------------- Unit 4: p252
add(
    S4, 252, "recall",
    "Which investigations are printed for AEP on page 252, with their captions?",
    "Peripheral blood leukocytosis; BAL with increased eosinophils and increased IgE; X-ray diffuse bilateral infiltrates like ARDS captioned 'X ray in AEP'; and CT diffuse parenchymal ground glass opacity with consolidation captioned 'CT in AEP'",
    [
        "Peripheral blood eosinophilia above 3000; BAL at or above 40% eosinophils; X-ray peripheral infiltrates captioned 'X ray in AEP'; and CT honeycombing",
        "Peripheral blood leukocytosis; BAL with increased eosinophils and increased IgE; X-ray diffuse bilateral infiltrates like ARDS captioned 'X ray in AEP'; and CT reverse bat wing appearance",
        "Peripheral blood leukocytosis; BAL lymphocytosis; X-ray diffuse bilateral infiltrates like ARDS captioned 'X ray in AEP'; and CT diffuse parenchymal ground glass opacity with consolidation captioned 'CT in AEP'",
    ],
    "The AEP investigations cell reads 'Peripheral blood: leukocytosis. BAL: ↑ eosinophil, ↑ IgE. X-ray: diffuse b/l infiltrates (like ARDS)' over the films captioned 'X ray in AEP', and 'CT: Diffuse parenchymal ground glass opacity, consolidation' over the scans captioned 'CT in AEP'.",
)

add(
    S4, 252, "recall",
    "Which imaging signature defines CEP investigations on page 252?",
    "Reverse bat wing appearance, also called the photographic negative of pulmonary edema, with perihilar sparing present and peripheral opacities",
    [
        "Batwing appearance without perihilar sparing, with central opacities",
        "Reverse bat wing appearance, also called the photographic negative of pulmonary edema, with perihilar infiltrates and peripheral sparing",
        "Photographic negative of pulmonary edema with diffuse bilateral infiltrates like ARDS",
    ],
    "The CEP cell reads 'BAL ≥40 % eosinophils. Imaging: Reverse bat wing appearance/ photographic negative of pulmonary edema. Perihilar sparing +. Peripheral opacities.' The plain batwing belongs to PAP on page 242; CEP reverses it.",
)

add(
    S4, 252, "match",
    "Match each CEP image on page 252 with its printed caption — 1) The chest film labelled A 2) The CT beside it … A) CT: peripheral pulmonary opacities, predominantly right B) X ray: peripheral pulmonary infiltrate, predominantly right",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "The film is captioned 'X ray: Peripheral pulmonary infiltrate (predominantly right)' and the scan 'CT: Peripheral pulmonary opacities (predominantly right)'. Both captions stress the same right-sided peripheral pattern.",
)

add(
    S4, 252, "numeric",
    "Which blood criterion and X-ray description are printed for idiopathic hypereosinophilic syndrome on page 252?",
    "Peripheral eosinophilia above 1500/µL for more than 6 months, with X-ray showing transient focal or diffuse pulmonary infiltrates",
    [
        "Peripheral eosinophilia above 3000/µL for more than 6 weeks, with X-ray showing transient focal or diffuse pulmonary infiltrates",
        "Peripheral eosinophilia above 1500/µL for more than 6 months, with X-ray showing fixed peripheral infiltrates",
        "BAL eosinophilia at or above 40% for more than 6 months, with X-ray showing transient focal or diffuse pulmonary infiltrates",
    ],
    "The syndrome cell reads 'Peripheral eosinophilia > 1500 /µl for > 6 months. X ray: Transient focal or diffuse pulmonary infiltrates.' The 3000 threshold and the 40% BAL figure belong to TPE on page 251.",
)

add(
    S4, 252, "truefalse",
    "TRUE or FALSE about the Treatment row that closes the unknown-causes table.",
    "True — 'Steroid' is printed across the AEP and CEP columns while idiopathic hypereosinophilic syndrome is 'unresponsive to steroid'",
    [
        "False — all three unknown causes are printed as steroid responsive",
        "False — AEP is unresponsive to steroid while the hypereosinophilic syndrome responds",
        "True — 'Steroid' is printed only under CEP, with AEP left untreated in the row",
    ],
    "The merged treatment cell reads 'Steroid' spanning the AEP and CEP columns, against 'unresponsive to steroid' for idiopathic hypereosinophilic syndrome — the myeloproliferative biology of page 251 made visible as drug resistance.",
)

add(
    S4, 252, "scenario",
    "A 35-year-old atopic woman with weeks of low grade fever, night sweats and weight loss has BAL eosinophils of 45% and a film showing peripheral opacities sparing the perihilar lung, predominantly on the right. Which diagnosis and printed sign-name fit?",
    "Chronic eosinophilic pneumonia — reverse bat wing, the photographic negative of pulmonary edema",
    [
        "Acute eosinophilic pneumonia — diffuse infiltrates like ARDS",
        "Chronic eosinophilic pneumonia — batwing appearance of pulmonary edema itself",
        "Idiopathic hypereosinophilic syndrome — transient focal infiltrates, steroid unresponsive",
    ],
    "Age 30–40 with female predominance, atopy in 33–50%, the subacute constitutional presentation, BAL at or above 40% and perihilar-sparing peripheral opacities are the CEP column from pages 251–252, whose sign is the reverse bat wing or photographic negative of pulmonary edema.",
)

add(
    S4, 252, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed investigation findings of the unknown ELD causes on page 252, one belongs to a known cause on an earlier page:",
    "Eggs in sputum as the diagnostic test",
    [
        "BAL at or above 40% eosinophils in CEP",
        "Diffuse parenchymal ground glass opacity with consolidation on CT in AEP",
        "Peripheral eosinophilia above 1500/µL for over 6 months in the hypereosinophilic syndrome",
    ],
    "Eggs in sputum diagnose Paragonimus lung invasion, a known parasite cause on page 250. The other three findings sit in the AEP, CEP and hypereosinophilic-syndrome investigation cells of page 252.",
)

add(
    S4, 252, "fillup",
    "In the CEP investigations cell, perihilar ______ is marked present alongside the peripheral opacities.",
    "sparing",
    ["infiltration", "consolidation", "honeycombing"],
    "The bullet reads 'Perihilar sparing +', the negative space at the lung centres that makes the image the photographic negative of cardiogenic pulmonary edema, whose batwing is perihilar instead.",
)


GUIDES = {
    S1: (
        "Eosinophilic Lung Disease Defined, Its Three Defining Features, Known versus Unknown Causes and Diseases Not Classified under ELD",
        "Pulmonary eosinophilia (p249), AKA eosinophilic lung disease, increases eosinophils in airway over parenchyma with an unclear pathogenic role and peripheral counts not elevated in every type; it is defined by raised BAL eosinophils, lung tissue eosinophilia, or peripheral eosinophilia with a lung infiltrate on imaging.\n"
        "Known causes (four heads) are parasite-related disease (hypersensitivity in Loeffler syndrome, lung invasion by lung fluke), drugs and toxins, tropical pulmonary eosinophilia and ABPA; unknown causes (four) are AEP, CEP, EGPA/Churg-Strauss under its three printed names, and idiopathic hypereosinophilic syndrome.\n"
        "Bronchial Asthma, 'cytogenic organising pneumonia' as printed and Langerhans cell histiocytosis (the last two arrowed to ILD), IgG4 related connective tissue disorder and hypersensitivity pneumonitis all sit outside ELD, and BAL of at least 40% marks 'TEP' as printed and CEP.",
    ),
    S2: (
        "Parasite-Related ELD (Loeffler Syndrome versus Lung Fluke Invasion), Drugs and Toxins, and Tropical Pulmonary Eosinophilia Pathogenesis",
        "Loeffler syndrome (p250) is type 1 hypersensitivity to larvae of Ascaris (most common) ahead of Ancylostoma, Necator and Strongyloides, mimicking Asthma with low grade fever, peripheral eosinophilia, raised IgE and migratory infiltrates, and resolving untreated in 1–2 weeks.\n"
        "True lung invasion by Paragonimus westermani maturing from metacercaria gives eosinophilic pleural effusion, cavitating nodules, ground glass and chocolate colored sputum, is diagnosed by eggs in sputum or ELISA, and takes praziquantel as DOC; drug and toxin causes are led by NSAIDs (most common) with L-tryptophan, rapeseed oil, nitrofurantoin, minocycline and ampicillin.\n"
        "TPE affects males more than females through hypersensitivity to microfilarial larvae of Wuchereria bancrofti and Brugia malayi, an association suggested by microfilariae in lung, liver and lymph nodes, antifilarial titres falling after cure, and dramatic anti-filarial response.",
    ),
    S3: (
        "Tropical Pulmonary Eosinophilia: Acute-on-Chronic Symptoms, Laboratory and Radiological Findings, DEC Treatment, and the Unknown-Cause Table Histories and Presentations",
        "TPE (p251) is acute on chronic: malaise, anorexia and weight loss with or without hepatosplenomegaly and lymphadenopathy, under paroxysmal nocturnal dry cough and wheeze that stimulate — as printed — status asthmaticus.\n"
        "Investigations show eosinophils above 3000 cells/mm³, BAL eosinophilic alveolitis at or above 40%, IgE above 1000 u/ml as printed, and bilateral indefinite middle-and-lower mottling with raised bronchovascular markings, cavitation and effusion; DOC DEC 2 mg/kg thrice daily for 14–21 days / 4 weeks kills adults and microfilariae, improves symptoms in 7 days, and relapses in up to 20%.\n"
        "Of the unknown causes, AEP follows restarted smoking into an ARDS-like illness over 2–3 days lasting 3–4 weeks, CEP is the subacute disease of atopic women aged 30–40, and the hypereosinophilic syndrome is a JAK2/PDGFRα myeloproliferative disorder damaging lung (40%), CNS (60%), heart and nerves.",
    ),
    S4: (
        "Unknown Causes of ELD: Investigations in AEP, CEP and Idiopathic Hypereosinophilic Syndrome with Their Steroid Responses",
        "AEP (p252) shows peripheral leukocytosis with BAL eosinophilia and raised IgE, diffuse bilateral ARDS-like infiltrates captioned 'X ray in AEP', and diffuse ground glass with consolidation captioned 'CT in AEP'.\n"
        "CEP shows BAL at or above 40% eosinophils and the reverse bat wing — photographic negative of pulmonary edema — with perihilar sparing and peripheral, predominantly right, infiltrates and opacities on film and CT.\n"
        "Idiopathic hypereosinophilic syndrome requires eosinophils above 1500/µL for over 6 months with transient focal or diffuse infiltrates, and alone among the three is unresponsive to the steroid printed across AEP and CEP.",
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
