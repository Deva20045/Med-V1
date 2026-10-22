#!/usr/bin/env python3
"""Generate Chapter 37: Occupational Lung Diseases (Book p223–229).

Every question is anchored to a printed line, table row or figure caption of
uploads/02.pdf sheets 106–112 (Book pages 223–229), in order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHAPTER = 37
TITLE = "Occupational Lung Diseases"
PAGES = "223-229"

S1 = "Disease Types, Pneumoconiosis Definition, the Dust-Particle Size/Site Table, the Four Pneumoconioses and Byssinosis (Organic Dust, Monday Fever)"
S2 = "Silicosis: Industries, Crystalline vs Amorphous Silica, Parenchymal-Only Involvement, Malignancy/COPD Risk and the Acute-vs-Chronic Table (Exposure, Pathogenesis, Clinical Triangle, BAL, PFT, Prognosis)"
S3 = "Radiology of Silicosis: Acute Crazy-Pavement CT Pattern and the Chronic Nodule-to-PMF Sequence with Egg-Shell Calcification and Upper Lobe ILD"
S4 = "Crazy-Pavement Differential (DAH, AEP, PAP with Anti-GM-CSF), Coal Workers Pneumoconiosis, the CWP-vs-Silicosis Table and Caplan Syndrome"
S5 = "Chronic Asbestosis: Fibre Types, Industries, Pleural Plaques (Candle Dripping, Holly Leaf), BAPE Fluid Criteria, Crow Feet Sign, Shaggy Heart Sign and Parenchymal Fibrosis"
S6 = "Asbestos Malignancy: Lung Cancer vs Mesothelioma Table, Ferruginous Body, Berylliosis as Delayed Hypersensitivity with Non-Caseating Granulomas and the Granuloma Differential"
S7 = "Berylliosis: Sarcoidosis Features That Are Absent, Industries, Upper Lobe ILD to PMF, Lymphocyte Proliferation Test, X-ray in 50% and the HRCT Triad"

RAW: list[tuple] = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: need four distinct options: {stem}")
    idx = len(RAW)
    block = [0, 1, 2, 3]
    random.Random(37000 + (idx // 4)).shuffle(block)
    target = block[idx % 4]
    shuffled = list(distractors)
    random.Random(37100 + idx).shuffle(shuffled)
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


# ---------------------------------------------------------------- Unit 1: p223
add(
    S1, 223, "recall",
    "Which three disease groups are listed under 'Types' at the start of page 223?",
    "Pneumoconiosis, occupational asthma and hypersensitivity pneumonitis",
    [
        "Pneumoconiosis, occupational asthma and byssinosis",
        "Pneumoconiosis, silicosis and asbestosis",
        "Occupational asthma, hypersensitivity pneumonitis and Caplan syndrome",
    ],
    "The opening list reads 'Types : Pneumoconiosis. occupational asthma. Hypersensitive pneumonitis.' Silicosis and asbestosis are subtypes of pneumoconiosis listed further down the page, not parallel categories.",
)

add(
    S1, 223, "recall",
    "How is pneumoconiosis defined on page 223?",
    "Accumulation of dust in lung and tissue reactions to its presence",
    [
        "Accumulation of dust in lung without any tissue reaction",
        "Accumulation of organic dust in the alveoli with granuloma formation",
        "Accumulation of silica in the pleura with plaque formation",
    ],
    "The definition reads 'accumulation of dust in lung & tissue reactions to its presence'. The tissue reaction is part of the definition, which is why the chapter separates the dusts by the pattern of reaction they provoke.",
)

add(
    S1, 223, "match",
    "Match each dust-particle size with its printed deposition site — 1) >3 µm 2) 0.5–3 µm 3) <0.5 µm … A) Alveoli B) Bronchiole C) Secondary bronchi",
    "1-C, 2-B, 3-A",
    ["1-A, 2-B, 3-C", "1-C, 2-A, 3-B", "1-B, 2-C, 3-A"],
    "The table reads '>3 µm — Secondary bronchi', '0.5–3 µm — Bronchiole' and '<0.5 µm — Alveoli'. The finest particles penetrate furthest, which is why alveolar dusts cause the pneumoconioses.",
)

add(
    S1, 223, "recall",
    "Which pneumoconiosis is marked as the most common on page 223?",
    "Silicosis",
    ["Asbestosis", "Coal worker pneumoconiosis", "Berylliosis"],
    "The list reads '1. Silicosis : most common. 2. Asbestosis. 3. Coal worker pneumoconiosis (CWP). 4. Berylliosis.' The following page devotes a full risk-factor and table section to silicosis accordingly.",
)

add(
    S1, 223, "recall",
    "What does the page 223 note say about byssinosis?",
    "It is hypersensitivity to organic dust exposure, with recurrent Monday fever as its clinical feature",
    [
        "It is hypersensitivity to inorganic dust exposure, with recurrent Monday fever as its clinical feature",
        "It is a pneumoconiosis from cotton dust, with progressive massive fibrosis as its clinical feature",
        "It is hypersensitivity to organic dust exposure, with egg-shell calcification as its clinical feature",
    ],
    "The note reads 'Byssinosis : Hypersensitivity to organic dust exposure' and 'Clinical features : Recurrent monday fever.' Monday fever describes the symptoms recurring on the first day back at work after the weekend.",
)

add(
    S1, 223, "oddoneout",
    "Pick the ODD ONE OUT — three are printed as types of pneumoconiosis on page 223, one is listed separately as organic-dust hypersensitivity:",
    "Byssinosis",
    ["Silicosis", "Asbestosis", "Berylliosis"],
    "The numbered pneumoconiosis list is silicosis, asbestosis, coal worker pneumoconiosis and berylliosis. Byssinosis appears only in the Note as hypersensitivity to organic dust — a different mechanism from dust accumulation with fibrosis.",
)

add(
    S1, 223, "fillup",
    "Particles larger than 3 µm are deposited in the ______, according to the page 223 table.",
    "Secondary bronchi",
    ["Bronchioles", "Alveoli", "Pleura"],
    "The table pairs '>3 µm' with 'Secondary bronchi'. Particles of 0.5–3 µm reach the bronchiole and those below 0.5 µm reach the alveoli, which is where the interstitial reactions begin.",
)


# ---------------------------------------------------------------- Unit 2: p224
add(
    S2, 224, "recall",
    "Which industries are listed as silicosis risk factors on page 224?",
    "Mining industry, quarries, blast furnaces, slate industry, sand stone industry, ceramics and rock cutting",
    [
        "Textile industry, cement industry, ship building work and automobile industry",
        "Ceramic industry, battery manufacturing and alloy industry",
        "Mining industry, battery manufacturing and textile industry",
    ],
    "The risk-factor list reads 'mining industry, Quarries, Blast furnaces, Slate industry, Sand stone industry, Ceramics, Rock cutting'. The textile/cement/shipbuilding list belongs to asbestosis on page 227 and the ceramic/battery/alloy list to berylliosis on page 229.",
)

add(
    S2, 224, "recall",
    "Which type of silica is most common, what is its composition, and which carries the higher occupational hazard?",
    "Crystalline silica (quartz); SiO2 (free silica); higher risk of occupational hazard",
    [
        "Amorphous silica; SiO2 bound in silicates; higher risk of occupational hazard",
        "Crystalline silica (quartz); SiO2 (free silica); lower risk of occupational hazard",
        "Crystalline silica (cristobalite); SiO2 (combined silica); higher risk of occupational hazard",
    ],
    "The block reads '1. Crystalline silica (Quartz) : m/c', 'Composition : SiO2 (Free silica)' and 'Higher risk of occupational hazard', with '2. Amorphous silica' as the second, lesser type.",
)

add(
    S2, 224, "fillup",
    "Two features are printed for silicosis under 'FEATURES': lung parenchymal involvement with ______ pleural involvement, and a risk of malignancy and COPD.",
    "No",
    ["Extensive", "Bilateral", "Unilateral"],
    "The line reads 'Lung parenchymal involvement (No pleural involvement)' and the next 'Risk of malignancy and COPD.' The absence of pleural disease is a printed point of contrast with asbestosis, which is dominated by pleural plaques.",
)

add(
    S2, 224, "numeric",
    "The acute-versus-chronic silicosis table gives two exposure durations. Which pair is printed?",
    "Large quantity for 2 years (acute) versus 10–30 years (chronic)",
    [
        "Large quantity for 5 years (acute) versus 20–40 years (chronic)",
        "Large quantity for 2 years (acute) versus 5–10 years (chronic)",
        "Small quantity for 2 years (acute) versus 10–30 years (chronic)",
    ],
    "The exposure row reads 'Large quantity for 2 years' for acute silicosis and 'For 10–30 years' for chronic silicosis. The acute form needs an intense exposure over a short period, not a small one.",
)

add(
    S2, 224, "recall",
    "Which pathogenesis chain is printed for chronic silicosis in the table?",
    "Injury to pulmonary alveolar macrophages → silicotuberculosis (reactivation of latent TB) and autoimmune illness (SLE, RA)",
    [
        "Injury to pulmonary alveolar macrophages → silicotuberculosis (primary TB) and immune deficiency (HIV)",
        "Injury to type II pneumocytes → progressive massive fibrosis and bronchogenic carcinoma",
        "Injury to capillary endothelium → alveolar haemorrhage and autoimmune illness (SLE, RA)",
    ],
    "The chronic pathogenesis cell reads 'Injury to pulmonary alveolar macrophages', with a double-headed arrow to 'Silicotuberculosis (Reactivation of latent TB)' on one side and 'Autoimmune illness (SLE, RA)' on the other. The acute cell in the same row is printed as a dash.",
)

add(
    S2, 224, "numeric",
    "In chronic silicosis, what frequency of chest signs is printed?",
    "25% of cases",
    ["15% of cases", "45% of cases", "50% of cases"],
    "The chronic clinical cell reads 'Chornic dry cough', 'Dyspnea on exertion' and 'Chest signs in 25% cases'. Most patients therefore have no chest signs despite established radiological disease.",
)

add(
    S2, 224, "match",
    "Match each table row with its acute-silicosis entry — 1) Clinical features 2) Investigations 3) Prognosis … A) PAS positive milky white BAL B) Very poor C) Acute onset with severe dyspnea, hypoxia and weight loss",
    "1-C, 2-A, 3-B",
    ["1-A, 2-B, 3-C", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "Acute silicosis gives 'Acute onset : severe dyspnea, hypoxia, weight loss', 'PAS positive milky white BAL (Bronchoalveolar lavage)' and 'very poor' prognosis. The chronic column instead reads PFT with a mixed pattern and a dash for prognosis.",
)

add(
    S2, 224, "scenario",
    "A sandblaster develops breathlessness, hypoxia and weight loss within two years, and lavage returns milky white PAS-positive fluid. Which diagnosis and prognostic statement match the page 224 table?",
    "Acute silicosis, with a very poor prognosis",
    [
        "Chronic silicosis, with a mixed pattern on spirometry",
        "Pulmonary alveolar proteinosis, with a very poor prognosis",
        "Byssinosis, with recurrent Monday fever",
    ],
    "The acute column combines 'Large quantity for 2 years', the dyspnea-hypoxia-weight loss triangle, 'PAS positive milky white BAL' and 'very poor' prognosis. Milky white PAS-positive lavage also appears under PAP on page 226, but the two-year heavy exposure and clinical triangle here are the printed acute-silicosis set.",
)


# ---------------------------------------------------------------- Unit 3: p225
add(
    S3, 225, "recall",
    "Which three components make up the 'crazy pavement appearance' printed for acute silicosis on CT?",
    "Ground glass opacifications with intact structure of lung, thickened septa and multiple centrilobular small nodules in parenchyma",
    [
        "Ground glass opacifications with destroyed lung structure, thin septa and multiple large nodules in pleura",
        "Consolidation with air bronchograms, thickened pleura and multiple centrilobular nodules",
        "Ground glass opacifications with intact structure of lung, thickened septa and multiple subpleural bullae",
    ],
    "The CT panel is labelled 'Crazy pavement appearance : Ground glass opacifications (Intact structure of lung); Thickened septa; multiple centrilobular small nodules in parenchyma.' The preserved lung architecture distinguishes it from destructive fibrosis.",
)

add(
    S3, 225, "recall",
    "Which radiological progression is printed for chronic silicosis on page 225?",
    "Small bilateral symmetric centrilobular parenchymal nodules → large conglomerate nodules (angel wing appearance) ± cavitations + hilar lymphadenopathy with egg shell calcification → progressive massive fibrosis (PMF), plus upper lobe interstitial lung disease",
    [
        "Large bilateral asymmetric nodules → small centrilobular nodules with angel wing appearance + hilar lymphadenopathy with egg shell calcification → PMF, plus lower lobe interstitial lung disease",
        "Small bilateral symmetric centrilobular nodules → large conglomerate nodules (angel wing appearance) ± cavitations + hilar lymphadenopathy with egg shell calcification → PMF, plus lower lobe interstitial lung disease",
        "Small unilateral asymmetric nodules → large conglomerate nodules (holly leaf appearance) + hilar lymphadenopathy with popcorn calcification → PMF, plus upper lobe interstitial lung disease",
    ],
    "The film sequence on page 225 reads exactly from 'Small bilateral symmetric centrilobular parenchymal nodule' to 'Large conglomerate nodules (Angel wing appearance)' to '± Cavitations + Hilar lymphadenopathy with egg shell calcification' to 'Progressive massive fibrosis (PMF)', ending with 'upper lobe interstitial lung disease'.",
)

add(
    S3, 225, "fillup",
    "The hilar node calcification of chronic silicosis on page 225 is described as ______ calcification.",
    "Egg shell",
    ["Popcorn", "Holly leaf", "Candle dripping"],
    "The label reads 'Hilar lymphadenopathy with egg shell calcification'. The hilar nodes calcify peripherally, giving a thin shell rather than a solid or popcorn density.",
)

add(
    S3, 225, "recall",
    "The large conglomerate nodules of chronic silicosis are described by which appearance on page 225?",
    "Angel wing appearance",
    ["Holly leaf appearance", "Shaggy heart appearance", "Crazy pavement appearance"],
    "The caption reads 'Large conglomerate nodules (Angel wing appearance)'. Holly leaf and shaggy heart are the asbestos signs printed on page 227, and crazy pavement is the acute silicosis CT pattern.",
)

add(
    S3, 225, "truefalse",
    "TRUE or FALSE about the two silicosis patterns on page 225.",
    "True — the acute pattern is a CT crazy-pavement appearance, whereas the chronic pattern progresses through nodules to PMF",
    [
        "False — the acute pattern is nodular progression to PMF, whereas the chronic pattern is crazy pavement",
        "False — both patterns are described as crazy pavement on CT",
        "True — the chronic pattern is confined to the lower lobes",
    ],
    "The acute column holds the single CT image captioned 'Crazy pavement appearance', while the chronic column holds the full film sequence of nodules → conglomerate nodules → PMF. The same chronic column ends with 'upper lobe interstitial lung disease'.",
)

add(
    S3, 225, "scenario",
    "A quarry worker with 20 years of exposure has a chest film showing small symmetric nodules and egg-shell hilar calcification, and a CT showing upper lobe fibrosis. Which staging does page 225 support?",
    "Chronic silicosis with progressive massive fibrosis and upper lobe interstitial lung disease",
    [
        "Acute silicosis with crazy pavement pattern and milky white lavage",
        "Chronic asbestosis with pleural plaques and lower lobe fibrosis",
        "Coal worker pneumoconiosis with Caplan syndrome",
    ],
    "The chronic column of page 225 runs from the symmetric centrilobular nodules to conglomerate nodules with egg-shell hilar calcification to PMF, ending with upper lobe interstitial lung disease. Pleural plaques, by contrast, are the asbestos hallmark on page 227.",
)


# ---------------------------------------------------------------- Unit 4: p226
add(
    S4, 226, "recall",
    "Which conditions are listed on page 226 as showing a crazy pavement pattern of lung?",
    "Diffuse alveolar hemorrhage (DAH), acute eosinophilic pneumonia (AEP) and pulmonary alveolar proteinosis (PAP)",
    [
        "Diffuse alveolar hemorrhage (DAH), acute eosinophilic pneumonia (AEP) and pulmonary alveolar microlithiasis",
        "Diffuse alveolar damage (DAD), allergic bronchopulmonary aspergillosis and pulmonary alveolar proteinosis (PAP)",
        "Diffuse alveolar hemorrhage (DAH), hypersensitivity pneumonitis and sarcoidosis",
    ],
    "The note lists 'Diffuse alveolar hemorrhage (DAH)', 'Acute eosinophilic pneumonia (AEP)' and 'Pulmonary alveolar proteinosis (PAP)'. DAD and ABPA are not printed in this differential.",
)

add(
    S4, 226, "recall",
    "What mechanism and lavage finding are printed for pulmonary alveolar proteinosis on page 226?",
    "Antibodies against GM-CSF causing abnormal clearance of surfactant, with PAS positive milky white BAL",
    [
        "Antibodies against GM-CSF causing excessive surfactant production, with PAS negative thin BAL",
        "Deficiency of GM-CSF receptors causing abnormal clearance of surfactant, with PAS positive milky white BAL",
        "Antibodies against surfactant protein-A causing abnormal clearance of surfactant, with PAS positive milky white BAL",
    ],
    "The PAP entry reads 'Antibodies against GM-CSF (Abnormal clearance of surfactant)' and 'PAS positive milky white BAL'. The defect is impaired macrophage clearance of surfactant driven by neutralising anti-GM-CSF antibodies.",
)

add(
    S4, 226, "recall",
    "Which four features are printed as similarities between CWP and silicosis?",
    "Upper lobe involvement, injury to PAMs causing TB or autoimmune disease, ↑COPD, and parenchymal nodules (>1 cm) ± cavitations progressing to PMF",
    [
        "Lower lobe involvement, injury to PAMs causing TB or autoimmune disease, ↓COPD, and parenchymal nodules (>3 cm) ± cavitations progressing to PMF",
        "Upper lobe involvement, injury to type II pneumocytes causing TB or autoimmune disease, ↑COPD, and pleural plaques ± calcification progressing to PMF",
        "Upper lobe involvement, injury to PAMs causing TB or autoimmune disease, ↑COPD, and parenchymal nodules (<0.5 cm) with no cavitation",
    ],
    "The block reads 'Upper lobe involvement', 'Injury to PAMs → TB or autoimmune disease', '↑ COPD' and 'Parenchymal nodules (>1 cm) ± cavitations → PMF'. CWP is AKA black lung from coal dust exposure, with black pigmentation and fibrosis due to carbon pigment.",
)

add(
    S4, 226, "recall",
    "The CWP-versus-silicosis table on page 226 has exactly three rows. Which set of entries is printed?",
    "Malignancy association present in silicosis and absent in CWP; hilar lymphadenopathy absent in silicosis and present in CWP; Caplan syndrome absent in silicosis and present in CWP",
    [
        "Malignancy association absent in silicosis and present in CWP; hilar lymphadenopathy present in silicosis and absent in CWP; Caplan syndrome present in silicosis and absent in CWP",
        "Malignancy association present in both; hilar lymphadenopathy absent in silicosis and present in CWP; Caplan syndrome absent in silicosis and present in CWP",
        "Malignancy association present in silicosis and absent in CWP; hilar lymphadenopathy present in both; Caplan syndrome present in both",
    ],
    "The table reads: 'Association with malignancy — Present (silicosis), Absent (CWP)'; 'Hilar lymphadenopathy — Absent (silicosis), Present (CWP)'; 'Caplan syndrome — Absent (silicosis), Present (CWP)'. This hilar row contradicts the chronic silicosis film label on page 225, a source inconsistency recorded in the caveat file.",
)

add(
    S4, 226, "recall",
    "Which three components make up Caplan syndrome on page 226?",
    "Coal worker pneumoconiosis (necrobiotic nodule) + rheumatoid arthritis with IgA rheumatoid factor positive + active synovitis",
    [
        "Silicosis (necrobiotic nodule) + rheumatoid arthritis with IgM rheumatoid factor positive + active synovitis",
        "Coal worker pneumoconiosis (necrobiotic nodule) + rheumatoid arthritis with IgA rheumatoid factor positive + inactive synovitis",
        "Coal worker pneumoconiosis (necrobiotic nodule) + systemic lupus erythematosus with IgA rheumatoid factor positive + active synovitis",
    ],
    "The syndrome is spelled out as 'Coal worker pneumoconiosis (Necrobiotic nodule)' plus 'Rheumatoid arthritis : IgA rheumatoid factor positive' plus 'Active synovitis'. The serotype is IgA, and the arthritis must be active.",
)

add(
    S4, 226, "scenario",
    "A coal miner with rheumatoid arthritis has multiple peripheral lung nodules with cavitation. Which eponym applies, and what is the printed nodule size threshold for CWP?",
    "Caplan syndrome; CWP nodules are >1 cm",
    [
        "Caplan syndrome; CWP nodules are >3 cm",
        "Silicosis with rheumatoid arthritis; CWP nodules are >1 cm",
        "Caplan syndrome; CWP nodules are >1 mm",
    ],
    "Caplan syndrome is defined on page 226 as CWP with a necrobiotic nodule, rheumatoid arthritis (IgA rheumatoid factor positive) and active synovitis. The same page prints parenchymal nodules '(>1 cm) ± cavitations → PMF' for CWP.",
)

add(
    S4, 226, "oddoneout",
    "Pick the ODD ONE OUT — three of these are printed under the page 226 crazy-pavement differential, one is not:",
    "Hypersensitivity pneumonitis",
    ["Diffuse alveolar hemorrhage", "Acute eosinophilic pneumonia", "Pulmonary alveolar proteinosis"],
    "The differential lists DAH, AEP and PAP only. Hypersensitivity pneumonitis appears on page 228 as a cause of non-caseating granuloma, a different list.",
)


# ---------------------------------------------------------------- Unit 5: p227
add(
    S5, 227, "match",
    "Match each fibre with its printed description on page 227 — 1) Serpentile/chrysotile 2) Crocidolite 3) Amosite … A) 90% of fibres, curly strands, less toxic B) Amphibole named first on the 10% limb C) Amphibole marked more dangerous",
    "1-A, 2-B, 3-C",
    ["1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-C, 2-B, 3-A"],
    "The diagram reads 'Asbestos fibres' with a 90% limb to 'Serpentile/chrysotile (Curly strands) — Less toxic' and a 10% limb to 'Amphibole (Brittle long straight rods)', splitting into 'Crocidolite' and 'Amosite (more dangerous)'. Chrysotile is the only serpentine form listed.",
)

add(
    S5, 227, "recall",
    "Which amphibole is marked as more dangerous on page 227, and which two amphiboles are named?",
    "Amosite is marked more dangerous; the two amphiboles are crocidolite and amosite",
    [
        "Crocidolite is marked more dangerous; the two amphiboles are crocidolite and amosite",
        "Chrysotile is marked more dangerous; the two amphiboles are chrysotile and amosite",
        "Amosite is marked more dangerous; the two amphiboles are amosite and tremolite",
    ],
    "The amphibole limb names 'Crocidolite' and 'Amosite (more dangerous)'. Chrysotile sits on the serpentine limb and is labelled less toxic.",
)

add(
    S5, 227, "match",
    "Match each pleural finding with its printed description — 1) Pleural plaques 2) Visceral pleural calcification 3) BAPE … A) Candle dripping and holly leaf sign B) Earliest, unilateral, hemorrhagic, exudative C) Crow feet sign",
    "1-A, 2-C, 3-B",
    ["1-C, 2-A, 3-B", "1-B, 2-C, 3-A", "1-A, 2-B, 3-C"],
    "The pleura table reads 'Pleural plaques (X-ray : Candle dripping, Holly leaf sign)', 'BAPE ... Earliest, unilateral, hemorrhagic, exudative' and 'Visceral pleural calcification (X-ray : Crow feet sign)'. Subpleural linear densities parallel to the plaque are also listed under the plaques.",
)

add(
    S5, 227, "recall",
    "Which set of features is printed for BAPE (benign asbestos related pleural effusion)?",
    "The earliest finding; unilateral, hemorrhagic and exudative, with eosin <25% and mesothelial cells <50%",
    [
        "The latest finding; bilateral, serous and transudative, with eosin <50% and mesothelial cells <25%",
        "The earliest finding; bilateral, hemorrhagic and exudative, with eosin <25% and mesothelial cells <50%",
        "The earliest finding; unilateral, hemorrhagic and exudative, with eosin >25% and mesothelial cells <50%",
    ],
    "The BAPE rows read 'Earliest, unilateral, hemorrhagic, exudative' and 'Eosin <25%, mesothelial cells <50%'. Both cell cut-offs are upper limits, and the fluid is exudative rather than transudative.",
)

add(
    S5, 227, "fillup",
    "Bilateral lower lobe infiltrates with pleural plaques in asbestosis produce the ______ heart sign on page 227.",
    "Shaggy",
    ["Holly leaf", "Egg shell", "Angel wing"],
    "The parenchymal row reads 'Bilateral lower lobe infiltrates with pleural plaques : Shaggy heart sign' and 'Diffuse massive fibrosis (DMF) of lower lobe'. The shaggy heart border is produced by the adjacent pleural and parenchymal disease, not by cardiomegaly.",
)

add(
    S5, 227, "recall",
    "Which parenchymal clinical features of asbestosis are printed in the right-hand column?",
    "Chest pain, dyspnea, and fibrosis with bibasal fine inspiratory crackle, clubbing and a restrictive PFT pattern",
    [
        "Chest pain, dyspnea, and fibrosis with bibasal coarse inspiratory crackle, no clubbing and an obstructive PFT pattern",
        "Chest pain, haemoptysis, and fibrosis with apical fine crackles, clubbing and a restrictive PFT pattern",
        "No clinical signs, with fibrosis detectable only on imaging and a normal PFT pattern",
    ],
    "The parenchyma column reads 'Chest pain', 'Dyspnea', and under 'Fibrosis': 'Bibasal fine inspiratory crackle', 'Clubbing' and 'PFT : Restrictive pattern'. The pleural column, in contrast, is the one printed with 'No clinical signs'.",
)

add(
    S5, 227, "truefalse",
    "TRUE or FALSE about pleural versus parenchymal asbestosis on page 227.",
    "True — the pleural column ends with 'no clinical signs', while the parenchymal column lists chest pain, dyspnoea and fibrosis signs",
    [
        "False — both columns are printed as producing no clinical signs",
        "False — the pleural column lists clubbing while the parenchymal column lists no signs",
        "True — clubbing is printed under the pleural column only",
    ],
    "The pleura column's clinical cell reads 'Progressive dyspnoea, Chest pain, No clinical signs', whereas the parenchyma column lists chest pain, dyspnoea, bibasal fine crackles, clubbing and a restrictive PFT. Clubbing belongs to the parenchymal disease.",
)

add(
    S5, 227, "scenario",
    "A shipyard worker has unilateral haemorrhagic pleural fluid with 20% eosinophils and 40% mesothelial cells. Which page 227 entity is this, and what is its temporal relationship to other asbestos findings?",
    "BAPE — the earliest asbestos-related pleural finding",
    [
        "BAPE — the latest asbestos-related pleural finding",
        "Malignant mesothelioma — with a latency of 10–30 years",
        "Pleural plaque with visceral calcification — the crow feet sign",
    ],
    "BAPE is 'Earliest, unilateral, hemorrhagic, exudative' with 'Eosin <25%, mesothelial cells <50%'. The case values sit under both cut-offs, and BAPE is explicitly the earliest pleural manifestation, preceding plaques and calcification.",
)


# ---------------------------------------------------------------- Unit 6: p228
add(
    S6, 228, "match",
    "Match each attribute with the asbestos-related tumour printed on page 228 — 1) Most common histology of lung cancer 2) Most common histology of mesothelioma 3) Latency of lung cancer 4) Latency of mesothelioma … A) > 30 years B) Adenocarcinoma > squamous cell carcinoma > small cell carcinoma C) 10–30 years D) Epitheloid > sarcomatoid",
    "1-B, 2-D, 3-C, 4-A",
    ["1-D, 2-B, 3-C, 4-A", "1-B, 2-D, 3-A, 4-C", "1-C, 2-D, 3-B, 4-A"],
    "The table reads 'Adenocarcinoma > Squamous cell carcinoma > small cell carcinoma' for lung cancer and 'Epitheloid > Sarcomatoid' for mesothelioma, with latency '10–30 years' and '> 30 years' respectively. Mesothelioma has the longer latency.",
)

add(
    S6, 228, "recall",
    "Which pair of smoking associations and clinical features is printed for lung cancer versus mesothelioma?",
    "Lung cancer: smoking association present, cough + haemoptysis; mesothelioma: smoking association absent, chest pain + mass",
    [
        "Lung cancer: smoking association absent, cough + haemoptysis; mesothelioma: smoking association present, chest pain + mass",
        "Lung cancer: smoking association present, chest pain + mass; mesothelioma: smoking association absent, cough + haemoptysis",
        "Lung cancer: smoking association present, cough + haemoptysis; mesothelioma: smoking association present, chest pain + mass",
    ],
    "The row reads 'Smoking association — Present (lung cancer), Absent (mesothelioma)' and 'Clinical features — Cough + Hemoptysis versus Chest pain + mass'. Mesothelioma is the asbestos tumour not driven by smoking.",
)

add(
    S6, 228, "recall",
    "Which mesothelioma markers and electron-microscopy features are printed on page 228?",
    "Markers pancytokeratin/calretinin; electron microscopy microvilli, desmosomes and tonofilaments",
    [
        "Markers pancytokeratin/calretinin; electron microscopy microvilli, hemidesmosomes and tonofibrils",
        "Markers cytokeratin 5/6 and WT-1; electron microscopy microvilli, desmosomes and tonofilaments",
        "Markers pancytokeratin/calretinin; electron microscopy cilia, desmosomes and tonofilaments",
    ],
    "The pathology cell lists 'markers : Pancytokeratin/calretinin', then 'electron microscopy : microvilli, Desmosomes, Tonofilaments'. The lung cancer pathology cell in the same row is printed as a dash.",
)

add(
    S6, 228, "fillup",
    "A ferruginous body is an asbestos body with a transparent core surrounded by ______ and protein, as printed on page 228.",
    "Iron",
    ["Calcium", "Silica", "Carbon"],
    "The note reads 'Ferruginous body : Asbestos body with transparent core surrounded by iron and protein.' The iron coating is what makes the body ferruginous and visible on stained sections.",
)

add(
    S6, 228, "recall",
    "How is berylliosis characterised immunologically and histologically on page 228?",
    "Delayed hypersensitivity with non-caseating granulomas, clinically similar to sarcoidosis",
    [
        "Immediate hypersensitivity with caseating granulomas, clinically similar to tuberculosis",
        "Delayed hypersensitivity with caseating granulomas, clinically similar to tuberculosis",
        "Immune complex deposition with non-caseating granulomas, clinically similar to rheumatoid arthritis",
    ],
    "The entry reads 'Berylliosis : Delayed hypersensitivity with non caseating granulomas. Clinically similar to sarcoidosis.' Caseation is absent, which is why the differential on the same page lists other non-caseating granulomatous diseases.",
)

add(
    S6, 228, "match",
    "Match each condition listed under non-caseating granuloma on page 228 with its category — 1) Sarcoidosis 2) Cat scratch disease 3) Crohn's disease … A) Infection B) Idiopathic granulomatous disease C) Inflammatory bowel disease",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "The list is 'Sarcoidosis, Tuberculosis, Lymphoma, Hypersensitive pneumonitis, Cat scratch disease, Berylliosis, Crohns disease.' Within it, cat scratch disease is infective and Crohn's is inflammatory bowel disease; sarcoidosis is the idiopathic comparator for berylliosis.",
)

add(
    S6, 228, "oddoneout",
    "Pick the ODD ONE OUT — three appear in the page 228 list of conditions with non-caseating granuloma, one does not:",
    "Tuberculosis with caseation",
    ["Sarcoidosis", "Lymphoma", "Crohn's disease"],
    "The list of conditions with non-caseating granuloma includes sarcoidosis, tuberculosis, lymphoma, hypersensitivity pneumonitis, cat scratch disease, berylliosis and Crohn's disease. The option deliberately converts tuberculosis into its caseating form, which is not the printed entity.",
)


# ---------------------------------------------------------------- Unit 7: p229
add(
    S7, 229, "recall",
    "Which sarcoidosis findings are printed as ABSENT in berylliosis on page 229?",
    "CNS symptoms, ocular symptoms, parotid findings and erythema (printed as erythemoid) lesions",
    [
        "CNS symptoms, ocular symptoms, parotid findings and erythema nodosum lesions",
        "Hilar adenopathy, ocular symptoms, parotid findings and erythema lesions",
        "CNS symptoms, cutaneous anergy, parotid findings and erythema lesions",
    ],
    "The list reads 'Findings of sarcoidosis absent in berylliosis : CNS symptoms. Ocular symptoms. Parotid findings. erythemoid lesions.' Hilar adenopathy is NOT in this absent list — it appears under the berylliosis X-ray findings on the same page.",
)

add(
    S7, 229, "recall",
    "Which three industries are printed as berylliosis risk factors?",
    "Ceramic industry, battery manufacturing and alloy industry",
    [
        "Ceramic industry, textile industry and alloy industry",
        "Ceramic industry, battery manufacturing and ship building",
        "Mining industry, battery manufacturing and alloy industry",
    ],
    "The risk factors read 'Ceramic industry', 'Battery manufacturing' and 'Alloy industry'. Textile, shipbuilding and mining belong to the asbestos and silica lists on pages 224 and 227.",
)

add(
    S7, 229, "numeric",
    "What proportion of berylliosis chest X-rays are normal, according to page 229?",
    "50% of patients",
    ["25% of patients", "75% of patients", "10% of patients"],
    "Under 'X-ray chest' the page prints 'Normal in 50% patients', then 'Hilar adenopathy' and '↑ interstitial markings'. A normal film therefore does not exclude the disease.",
)

add(
    S7, 229, "recall",
    "Which investigation is printed as positive in berylliosis, and what does it test?",
    "Lymphocyte proliferation test",
    ["Neutrophil proliferation test", "Leukocyte migration inhibition test", "Serum angiotensin converting enzyme"],
    "The investigations block opens with 'Lymphocyte proliferation test : Positive.' This reflects the delayed hypersensitivity mechanism described on page 228.",
)

add(
    S7, 229, "recall",
    "Which three HRCT findings are printed for berylliosis?",
    "Ground glass appearance (classical), parenchymal nodules and septal lines",
    [
        "Ground glass appearance (classical), honeycombing and traction bronchiectasis",
        "Consolidation (classical), parenchymal nodules and septal lines",
        "Ground glass appearance (classical), egg shell calcification and septal lines",
    ],
    "The HRCT list reads 'Ground glass appearance : Classical', 'Parenchymal nodules' and 'Septal lines'. Honeycombing and egg-shell calcification are printed elsewhere (asbestosis and silicosis respectively), not here.",
)

add(
    S7, 229, "recall",
    "Which clinical features of berylliosis are printed on page 229?",
    "Dyspnea, with upper lobe ILD progressing to PMF",
    [
        "Dyspnea, with lower lobe ILD progressing to PMF",
        "Dyspnea, with upper lobe ILD progressing to honeycombing only",
        "Cough with haemoptysis, with lower lobe ILD progressing to PMF",
    ],
    "The features block reads 'Dyspnea' and 'upper lobe ILD → PMF'. Upper lobe predominance matches silicosis and CWP, in contrast with the lower lobe fibrosis of asbestosis.",
)

add(
    S7, 229, "truefalse",
    "TRUE or FALSE about berylliosis as summarised across pages 228–229.",
    "True — it is a delayed hypersensitivity with non-caseating granulomas, mimics sarcoidosis, and is confirmed by a positive lymphocyte proliferation test",
    [
        "False — it is an immediate hypersensitivity with caseating granulomas, mimics tuberculosis, and is confirmed by a negative lymphocyte proliferation test",
        "False — it is a delayed hypersensitivity with caseating granulomas, mimics tuberculosis, and is confirmed by a positive lymphocyte proliferation test",
        "True — it is a delayed hypersensitivity whose HRCT hallmark is honeycombing",
    ],
    "Page 228 defines berylliosis as 'Delayed hypersensitivity with non caseating granulomas' and 'Clinically similar to sarcoidosis', and page 229 prints 'Lymphocyte proliferation test : Positive' with the classical HRCT finding of ground glass, not honeycombing.",
)


GUIDES = {
    S1: (
        "Disease Types, Pneumoconiosis Definition, the Dust-Particle Size/Site Table, the Four Pneumoconioses and Byssinosis (Organic Dust, Monday Fever)",
        "Occupational lung diseases (p223) divide into pneumoconiosis, occupational asthma and hypersensitivity pneumonitis. Pneumoconiosis is accumulation of dust in lung with tissue reactions to its presence.\n"
        "Dust size decides the site: >3 µm lodges in secondary bronchi, 0.5–3 µm in the bronchiole and <0.5 µm in the alveoli, which is why the finest dusts cause parenchymal disease.\n"
        "The four pneumoconioses are silicosis (most common), asbestosis, coal worker pneumoconiosis and berylliosis. Byssinosis is different — hypersensitivity to organic dust with recurrent Monday fever.",
    ),
    S2: (
        "Silicosis: Industries, Crystalline vs Amorphous Silica, Parenchymal-Only Involvement, Malignancy/COPD Risk and the Acute-vs-Chronic Table (Exposure, Pathogenesis, Clinical Triangle, BAL, PFT, Prognosis)",
        "Silicosis risk factors (p224) are mining, quarries, blast furnaces, slate industry, sand stone industry, ceramics and rock cutting. Crystalline silica (quartz) is most common, composed of SiO2 (free silica) and carries the higher occupational hazard; amorphous silica is the second type.\n"
        "Features are lung parenchymal involvement with NO pleural involvement, plus a risk of malignancy and COPD.\n"
        "Acute silicosis follows a large quantity over 2 years, has a dash for pathogenesis, presents acutely with severe dyspnea, hypoxia and weight loss, gives PAS-positive milky white BAL and has a very poor prognosis. Chronic silicosis follows 10–30 years, acts through injury to pulmonary alveolar macrophages with silicotuberculosis (reactivation of latent TB) and autoimmune illness (SLE, RA), gives chronic dry cough with dyspnea on exertion and chest signs in 25%, and shows a mixed PFT pattern.",
    ),
    S3: (
        "Radiology of Silicosis: Acute Crazy-Pavement CT Pattern and the Chronic Nodule-to-PMF Sequence with Egg-Shell Calcification and Upper Lobe ILD",
        "Acute silicosis CT (p225) shows the crazy pavement appearance: ground glass opacifications with intact lung structure, thickened septa and multiple centrilobular small nodules in the parenchyma.\n"
        "Chronic silicosis progresses from small bilateral symmetric centrilobular parenchymal nodules to large conglomerate nodules with an angel wing appearance, ± cavitations, with hilar lymphadenopathy showing egg-shell calcification, then to progressive massive fibrosis, and finally upper lobe interstitial lung disease.",
    ),
    S4: (
        "Crazy-Pavement Differential (DAH, AEP, PAP with Anti-GM-CSF), Coal Workers Pneumoconiosis, the CWP-vs-Silicosis Table and Caplan Syndrome",
        "The crazy pavement pattern (p226) also occurs in diffuse alveolar haemorrhage, acute eosinophilic pneumonia and pulmonary alveolar proteinosis — in PAP there are antibodies against GM-CSF causing abnormal clearance of surfactant, with PAS-positive milky white BAL.\n"
        "CWP (black lung) shares with silicosis upper lobe involvement, injury to PAMs causing TB or autoimmune disease, ↑COPD, and parenchymal nodules >1 cm ± cavitations progressing to PMF; the pigment is carbon.\n"
        "CWP versus silicosis: malignancy association present in silicosis and absent in CWP; hilar lymphadenopathy absent in silicosis and present in CWP; Caplan syndrome absent in silicosis and present in CWP. Caplan syndrome is CWP (necrobiotic nodule) plus rheumatoid arthritis with IgA rheumatoid factor positive plus active synovitis.",
    ),
    S5: (
        "Chronic Asbestosis: Fibre Types, Industries, Pleural Plaques (Candle Dripping, Holly Leaf), BAPE Fluid Criteria, Crow Feet Sign, Shaggy Heart Sign and Parenchymal Fibrosis",
        "Asbestos fibres (p227) are 90% serpentine/chrysotile with curly strands and less toxicity, and 10% amphibole with brittle long straight rods — crocidolite and amosite, amosite being more dangerous. Risk industries are textile, cement, ship building and automobile, and smoking adds parenchymal and malignant risk.\n"
        "Pleura: parietal pleural calcification with pleural plaques (X-ray candle dripping, holly leaf sign) and subpleural linear densities parallel to the plaque; BAPE, the earliest finding, is unilateral, hemorrhagic and exudative with eosin <25% and mesothelial cells <50%; visceral pleural calcification gives the crow feet sign. Pleural disease is printed with 'no clinical signs'.\n"
        "Parenchyma: bilateral lower lobe infiltrates with pleural plaques (shaggy heart sign) and diffuse massive fibrosis of the lower lobe, with chest pain, dyspnea, bibasal fine inspiratory crackles, clubbing and a restrictive PFT pattern.",
    ),
    S6: (
        "Asbestos Malignancy: Lung Cancer vs Mesothelioma Table, Ferruginous Body, Berylliosis as Delayed Hypersensitivity with Non-Caseating Granulomas and the Granuloma Differential",
        "Asbestos malignancy (p228): lung cancer is adenocarcinoma > squamous cell carcinoma > small cell carcinoma with a 10–30 year latency, a present smoking association and cough with haemoptysis; mesothelioma is epitheloid > sarcomatoid with a > 30 year latency, no smoking association, chest pain with mass, and pathology markers pancytokeratin/calretinin with electron microscopy showing microvilli, desmosomes and tonofilaments. The lung cancer pathology cell is printed as a dash.\n"
        "A ferruginous body is an asbestos body with a transparent core surrounded by iron and protein. Berylliosis is a delayed hypersensitivity with non-caseating granulomas, clinically similar to sarcoidosis; the non-caseating granuloma list is sarcoidosis, tuberculosis, lymphoma, hypersensitivity pneumonitis, cat scratch disease, berylliosis and Crohn's disease.",
    ),
    S7: (
        "Berylliosis: Sarcoidosis Features That Are Absent, Industries, Upper Lobe ILD to PMF, Lymphocyte Proliferation Test, X-ray in 50% and the HRCT Triad",
        "Sarcoidosis findings absent in berylliosis (p229) are CNS symptoms, ocular symptoms, parotid findings and erythemoid lesions. Risk factors are ceramic industry, battery manufacturing and alloy industry.\n"
        "Features are dyspnea with upper lobe ILD progressing to PMF. Investigations: lymphocyte proliferation test positive; chest X-ray normal in 50% of patients, with hilar adenopathy and ↑ interstitial markings in the remainder; HRCT shows the classical ground glass appearance with parenchymal nodules and septal lines.",
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
