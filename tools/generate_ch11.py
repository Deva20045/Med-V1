#!/usr/bin/env python3
"""Generate Chapter 11 Clinical Approach to Anemia (Book p66–69)."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 11
TITLE = "Clinical Approach to Anemia"
PAGES = "66-69"

S1 = "WHO Thresholds and Hematopoiesis"
S2 = "Erythroid Maturation"
S3 = "Reticulocyte Count and Indices"
S4 = "Clinical Approach and Marrow Notes"
RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    random.Random(11000 + CHAPTER * 10000 + len(RAW)).shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2
        assert sum(o.startswith("False") for o in options) == 2
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p66 — anaemia thresholds and haematopoietic lineage
add(S1, 66, "numeric", "The WHO haemoglobin threshold for anaemia in an average healthy 40-year-old male is:",
    "<13 g/dL", ["<10 g/dL", "<11 g/dL", "<15 g/dL"],
    "The p66 definition gives male Hb <13 g/dL.")
add(S1, 66, "numeric", "The female haemoglobin threshold shown beside the healthy-adult definition is:",
    "<12 g/dL", ["<10 g/dL", "<11 g/dL", "<13 g/dL"],
    "The page gives female Hb <12 g/dL.")
add(S1, 66, "numeric", "The haemoglobin threshold printed for a pregnant woman is:",
    "<11 g/dL", ["<10 g/dL", "<12 g/dL", "<13 g/dL"],
    "The pregnancy threshold is <11 g/dL.")
add(S1, 66, "numeric", "The p66 definition lists which haemoglobin threshold for a patient with CKD?",
    "<10 g/dL", ["<11 g/dL", "<12 g/dL", "<13 g/dL"],
    "The page lists Hb <10 g/dL for a known CKD patient.")
add(S1, 66, "recall", "The top cell in the haematopoiesis diagram is the:",
    "Pluripotent haematopoietic stem cell (PPHSC)", ["Common lymphoid progenitor", "Proerythroblast", "Reticulocyte"],
    "The diagram begins with pluripotent haematopoietic stem cell (PPHSC).")
add(S1, 66, "recall", "The two progenitor branches directly downstream of PPHSC are:",
    "Common myeloid and common lymphoid progenitors", ["BFU-E and CFU-E", "Granulocyte and monocyte progenitors", "B/T cells and NK cells"],
    "PPHSC branches to common myeloid and common lymphoid progenitors.")
add(S1, 66, "recall", "Which set is shown downstream of the common myeloid progenitor?",
    "Platelets, granulocytes, monocytes and RBCs", ["B/T lymphocytes and NK cells only", "RBCs and plasma cells only", "Eosinophils, B cells and platelets only"],
    "The common myeloid progenitor gives platelets, granulocytes, monocytes and RBCs.")
add(S1, 66, "recall", "The common lymphoid progenitor branch gives rise to:",
    "B/T lymphocytes and NK cells", ["Platelets and RBCs", "Neutrophils and macrophages", "Eosinophils and basophils"],
    "The diagram shows B/T lymphocytes and NK cells downstream of the common lymphoid progenitor.")
add(S1, 66, "recall", "Which trio is included under granulocytes in the p66 lineage diagram?",
    "Neutrophils, eosinophils and basophils", ["Monocytes, macrophages and NK cells", "B cells, T cells and plasma cells", "Platelets, erythroblasts and reticulocytes"],
    "The listed granulocytes are neutrophils, eosinophils and basophils.")
add(S1, 66, "recall", "The monocyte branch is shown giving rise to:",
    "Macrophages", ["Platelets", "NK cells", "Chief cells"],
    "Monocytes are shown differentiating into macrophages.")
add(S1, 66, "recall", "Which sequence gives the early red-cell production pathway in the figure?",
    "PPHSC → common myeloid progenitor → BFU-E → CFU-E → proerythroblast → mature RBC", ["PPHSC → common lymphoid progenitor → NK cell → CFU-E → RBC", "PPHSC → megakaryocyte → reticulocyte → BFU-E → RBC", "PPHSC → CFU-E → BFU-E → proerythroblast → platelet"],
    "The figure traces PPHSC through CMP, BFU-E, CFU-E and proerythroblast to mature RBCs.")
add(S1, 66, "recall", "The stage labelled EPO-independent and iron-independent is:",
    "Common myeloid progenitor", ["BFU-E", "CFU-E", "Proerythroblast"],
    "The diagram marks the common myeloid progenitor as EPO-independent and iron-independent.")
add(S1, 66, "recall", "The BFU-E stage is labelled:",
    "EPO-dependent but iron-independent", ["EPO-independent and iron-independent", "EPO- and iron-dependent", "Iron-dependent but EPO-independent"],
    "BFU-E is marked EPO-dependent, iron-independent.")
add(S1, 66, "recall", "The p66 bracket labels the CFU-E stage and downstream red-cell maturation as dependent on:",
    "Both EPO and iron", ["Neither EPO nor iron", "EPO only", "Iron only"],
    "The bracket begins at CFU-E and continues through mature RBCs; it labels dependence on both EPO and iron.")
add(S1, 66, "recall", "Erythropoietin is produced by peritubular interstitial fibroblasts in the:",
    "Cortex and outer medulla of the kidney", ["Liver and spleen", "Renal pelvis only", "Bone marrow sinusoids"],
    "The note locates EPO production in peritubular interstitial fibroblasts of the renal cortex and outer medulla.")
add(S1, 66, "recall", "The source named for thrombopoietin is the:",
    "Liver", ["Kidney", "Spleen", "Bone marrow"],
    "The note says thrombopoietin is produced by the liver for platelets.")
add(S1, 66, "truefalse", "TRUE or FALSE — as erythroid cells mature, the page shows cell size and number of nucleoli decreasing.",
    "True — both decrease with maturation", ["False — both increase", "False — cell size decreases but nucleoli increase", "True — only the cytoplasm decreases"],
    "The p66 note says nucleoli decrease with chromatin condensation and cell size also decreases as maturity increases.")

# ---------------------------------------------------------------------------
# Book p67 — morphology of each erythroid precursor
add(S2, 67, "recall", "The pro-normoblast/pro-erythroblast is described as the:",
    "Largest cell", ["Smallest nucleated cell", "First enucleated cell", "Mature red cell"],
    "The page labels the pro-normoblast as the largest cell.")
add(S2, 67, "recall", "Which cytoplasmic colour is listed for the pro-normoblast?",
    "Basophilic", ["Grayish", "Reddish", "Polychromatic with no basophilia"],
    "The pro-normoblast cytoplasm is basophilic.")
add(S2, 67, "recall", "The pro-normoblast has nucleoli because the chromatin is:",
    "Fine", ["Dense and pyknotic", "Completely absent", "Fully clumped and mature"],
    "Nucleoli are present due to fine chromatin in the pro-normoblast.")
add(S2, 67, "recall", "The pro-normoblast nucleus-to-cytoplasm ratio is:",
    "High", ["Low", "Equal to one", "Absent because the nucleus has been lost"],
    "A high N:C ratio is listed for the pro-normoblast.")
add(S2, 67, "recall", "Which pair describes the early/basophilic normoblast?",
    "Basophilic cytoplasm; nucleoli absent as chromatin condensation begins", ["Gray cytoplasm; cell division ceases", "Reddish cytoplasm; dense pyknotic nucleus", "No nucleus; bluish tinge from RNA"],
    "The early normoblast remains basophilic; nucleoli are absent as chromatin condensation begins.")
add(S2, 67, "recall", "The nucleus-to-cytoplasm ratio remains high in which early precursor after the pro-normoblast?",
    "Early/basophilic normoblast", ["Reticulocyte", "Mature RBC", "Late/orthochromatic normoblast only"],
    "The early/basophilic normoblast is also described with a high N:C ratio.")
add(S2, 67, "recall", "The intermediate/polychromatic normoblast has grayish cytoplasm because of:",
    "Initiation of haemoglobin synthesis", ["RNA persistence after nucleus loss", "Complete absence of haemoglobin", "Mucus accumulation"],
    "The gray colour is attributed to the beginning of haemoglobin synthesis.")
add(S2, 67, "recall", "The nucleus of the intermediate/polychromatic normoblast is described as:",
    "Rounded, with chromatin condensation/clumping", ["Absent", "Dense and pyknotic with red cytoplasm", "Fine with prominent nucleoli"],
    "The page describes a rounded nucleus and positive chromatin condensation/clumping.")
add(S2, 67, "recall", "At which erythroid stage does cell division cease according to p67?",
    "Intermediate/polychromatic normoblast", ["Pro-normoblast", "Early/basophilic normoblast", "Reticulocyte"],
    "Cell division is stated to cease at the intermediate/polychromatic stage.")
add(S2, 67, "recall", "The late/orthochromatic normoblast cytoplasm is reddish because it is:",
    "Well haemoglobinised", ["Rich in RNA", "Starting haemoglobin synthesis", "Filled with mucin"],
    "The reddish cytoplasm is attributed to being well haemoglobinised.")
add(S2, 67, "recall", "The nucleus of the late/orthochromatic normoblast is:",
    "Dense and pyknotic", ["Fine with visible nucleoli", "Rounded with early clumping", "Absent and replaced by RNA"],
    "The late normoblast has a dense, pyknotic nucleus.")
add(S2, 67, "recall", "Which pair characterizes a reticulocyte in the stage diagram?",
    "Nucleus absent; cytoplasm has a bluish tinge from RNA", ["Nucleoli present; basophilic cytoplasm", "Dense pyknotic nucleus; red cytoplasm", "Rounded nucleus; gray cytoplasm"],
    "The reticulocyte has no nucleus and a bluish cytoplasmic tinge due to RNA.")
add(S2, 67, "recall", "The mature RBC image is described as being shown after:",
    "Romanowsky staining", ["Prussian-blue staining", "Supravital staining only", "Gram staining"],
    "The image caption says mature RBCs after Romanowsky staining.")
add(S2, 67, "recall", "A giant pro-erythroblast is noted in:",
    "Pure red cell aplasia", ["Iron-deficiency anaemia", "Celiac disease", "Toxic megacolon"],
    "The p67 note associates a giant pro-erythroblast with pure red cell aplasia.")

# ---------------------------------------------------------------------------
# Book p68 — reticulocyte staining, count, CRC and RPI
add(S3, 68, "recall", "Reticulocyte RNA is detected using which class of stain?",
    "Supravital stains", ["Romanowsky stains only", "Prussian-blue stain", "Acid-fast stain"],
    "The page says reticulocyte RNA requires supravital staining.")
add(S3, 68, "truefalse", "TRUE or FALSE — fixation is required before supravital staining to detect reticulocyte RNA.",
    "False — fixation is not required", ["True — fixation is essential", "False — but only for Romanowsky stain", "True — fixation is required for every reticulocyte test"],
    "The page explicitly notes fixation is not required for detecting RNA with supravital stain.")
add(S3, 68, "recall", "Which pair of supravital stains is listed for reticulocytes?",
    "Brilliant cresyl blue and new methylene blue", ["Prussian blue and Wright stain", "Sudan III and Sudan IV", "Gram stain and Ziehl–Neelsen stain"],
    "The listed stains are brilliant cresyl blue and new methylene blue.")
add(S3, 68, "recall", "With Romanowsky stain, reticulocytes are noted to appear:",
    "Polychromatic; the reticulocyte RNA is not detected", ["Prussian blue", "Completely colourless", "As a dark intracellular inclusion"],
    "The note says RNA is not detected with Romanowsky stain and cells appear polychromatic.")
add(S3, 68, "numeric", "The normal reticulocyte count range printed on p68 is:",
    "0.5–1.5%", ["0.05–0.15%", "2.5–5%", "5–10%"],
    "The page gives a normal RC of 0.5–1.5%.")
add(S3, 68, "recall", "In hypoproliferative anaemia, reduced RBC production leads to:",
    "Reticulocytopenia", ["Reticulocytosis", "Polychromasia with normal count only", "Thrombocytosis"],
    "Reduced RBC production is linked to reticulocytopenia/decreased reticulocyte count.")
add(S3, 68, "recall", "A hyperproliferative response associated with RBC destruction or blood loss produces:",
    "Reticulocytosis", ["Reticulocytopenia", "A normal count in every case", "A low absolute reticulocyte count"],
    "Increased destruction or blood loss is linked to reticulocytosis.")
add(S3, 68, "numeric", "The absolute reticulocyte count range shown is:",
    "25,000–75,000 cells/µL", ["2,500–7,500 cells/µL", "100,000–150,000 cells/µL", "250,000–750,000 cells/µL"],
    "The page gives an absolute count of 25,000–75,000 cells/µL.")
add(S3, 68, "recall", "The corrected reticulocyte count (CRC) corrects for:",
    "The degree of anaemia", ["The patient's age alone", "The platelet count", "The size of the spleen"],
    "CRC is described as correction for the degree of anaemia.")
add(S3, 68, "recall", "Which equation reproduces the corrected reticulocyte count formula?",
    "Reticulocyte count × (patient haemoglobin ÷ desired haemoglobin)", ["Reticulocyte count × (desired haemoglobin ÷ patient haemoglobin)", "Patient haemoglobin × desired haemoglobin ÷ reticulocyte count", "Reticulocyte count ÷ (patient haemoglobin + desired haemoglobin)"],
    "CRC = reticulocyte count × haemoglobin in patient / desired haemoglobin level.")
add(S3, 68, "numeric", "The desired haemoglobin value used for a male in the CRC note is:",
    "15 g/dL", ["10 g/dL", "12 g/dL", "13 g/dL"],
    "The boxed desired Hb value is 15 g/dL for males.")
add(S3, 68, "numeric", "The desired haemoglobin value used for a female in the CRC note is:",
    "13 g/dL", ["10 g/dL", "12 g/dL", "15 g/dL"],
    "The boxed desired Hb value is 13 g/dL for females.")
add(S3, 68, "recall", "The reticulocyte production index (RPI) additionally corrects for:",
    "The longer life of prematurely released reticulocytes", ["The shorter lifespan of mature RBCs only", "The platelet lifespan", "The degree of iron absorption"],
    "RPI corrects for the longer life of prematurely released reticulocytes.")
add(S3, 68, "numeric", "The p68 formula for RPI is:",
    "CRC divided by 2", ["CRC multiplied by 2", "RC divided by desired Hb", "Hb divided by absolute reticulocyte count"],
    "The page gives RPI = CRC/2.")
add(S3, 68, "scenario", "A male with Hb 9 g/dL has a reticulocyte count of 6%. Using the desired male Hb and CRC formula on p68, what is his corrected reticulocyte count?",
    "3.6%", ["1.8%", "6%", "10%"],
    "CRC = 6% × (9/15) = 3.6%; 1.8% would be the page's subsequent RPI calculation after dividing CRC by 2.")

# ---------------------------------------------------------------------------
# Book p69 — flowchart, MCV and marrow notes
add(S4, 69, "recall", "The first branch in the clinical-approach flowchart separates anaemia by:",
    "Single versus multiple lineages affected", ["Male versus female sex", "Iron level versus ferritin only", "Acute versus chronic onset"],
    "The first decision is single-lineage versus multiple-lineage involvement.")
add(S4, 69, "numeric", "In the p69 flowchart, RPI below what threshold is labelled hypoproliferative anaemia?",
    "<2.5", ["<0.5", "<1.0", "<5.0"],
    "RPI <2.5 is labelled hypoproliferative.")
add(S4, 69, "numeric", "An RPI above what threshold is labelled hyperproliferative anaemia?",
    ">2.5", [">0.5", ">1.0", ">5.0"],
    "RPI >2.5 is labelled hyperproliferative.")
add(S4, 69, "numeric", "The normocytic MCV interval written in the flowchart is:",
    "80–100 fL", ["60–80 fL", "100–120 fL", "120–140 fL"],
    "The note defines average RBC MCV as 80–100 fL.")
add(S4, 69, "numeric", "The microcytic branch uses which MCV cutoff?",
    "<80 fL", ["<100 fL", ">100 fL", ">120 fL"],
    "The flowchart places microcytosis below 80 fL.")
add(S4, 69, "numeric", "The macrocytic branch uses which MCV cutoff?",
    ">100 fL", ["<80 fL", "80–100 fL", ">150 fL"],
    "The flowchart defines macrocytosis as >100 fL.")
add(S4, 69, "recall", "Which group appears under the normocytic/microcytic hypoproliferative branch?",
    "Iron-deficiency anaemia, anaemia of chronic disease, sideroblastic anaemia and thalassaemia trait", ["B12 deficiency alone", "Autoimmune haemolysis, G6PD deficiency and malaria", "Aplastic anaemia and pure red-cell aplasia only"],
    "The flowchart lists iron deficiency, chronic disease, sideroblastic anaemia and thalassaemia trait under normo/microcytic disease.")
add(S4, 69, "recall", "The macrocytic branch in the flowchart points to:",
    "Megaloblastic anaemia due to vitamin B12 deficiency", ["Iron-deficiency anaemia due to blood loss", "Sideroblastic anaemia due to alcohol only", "Thalassaemia trait"],
    "The macrocytic branch is labelled megaloblastic anaemia due to vitamin B12 deficiency.")
add(S4, 69, "recall", "Megaloblasts are described as RBC precursors with delayed:",
    "Nuclear maturation despite normal cytoplasmic maturation", ["Cytoplasmic maturation with normal nuclei", "Haemoglobin synthesis with normal cell division", "Membrane maturation and platelet formation"],
    "The note defines megaloblasts as RBCs lagging in nuclear maturation with normal cytoplasmic maturation.")
add(S4, 69, "numeric", "The page estimates marrow cellularity as:",
    "100 minus the person's age", ["100 plus the person's age", "Age divided by 100", "50% at every age"],
    "The note gives marrow cellularity = 100 − age of the person.")
add(S4, 69, "scenario", "For a 50-year-old person, the marrow-cellularity example predicts approximately:",
    "50% fat and 50% cellularity", ["25% fat and 75% cellularity", "75% fat and 25% cellularity", "100% cellularity with no fat"],
    "The example says a 50-year-old has 50% fat and 50% cellular marrow.")
add(S4, 69, "recall", "The marrow-failure example says all cells are replaced by fat, as in:",
    "Aplastic anaemia", ["Iron-deficiency anaemia", "Thalassaemia trait", "Erythroid hyperplasia"],
    "The note names aplastic anaemia as an example of marrow failure with replacement by fat.")
add(S4, 69, "numeric", "The normal myeloid-to-erythroid (M:E) ratio listed is:",
    "3:1", ["1:3", "1:1", "10:1"],
    "The page gives a normal M:E ratio of 3:1.")
add(S4, 69, "recall", "Which marrow image is captioned separately from the two hyperplasia examples?",
    "Normal bone marrow", ["Myeloid hyperplasia", "Erythroid hyperplasia", "Aplastic marrow"],
    "The three image captions are normal bone marrow, myeloid hyperplasia and erythroid hyperplasia.")
add(S4, 69, "recall", "The bottom-left marrow image is captioned:",
    "Myeloid hyperplasia", ["Normal bone marrow", "Erythroid hyperplasia", "Pure red-cell aplasia"],
    "The bottom-left image is labelled myeloid hyperplasia.")
add(S4, 69, "recall", "The bottom-right marrow image is captioned:",
    "Erythroid hyperplasia", ["Normal bone marrow", "Myeloid hyperplasia", "Aplastic marrow"],
    "The bottom-right image is labelled erythroid hyperplasia.")
add(S4, 69, "truefalse", "TRUE or FALSE — the flowchart first evaluates lineage involvement, then uses RPI and MCV for a single-lineage anaemia branch.",
    "True — lineage → RPI → MCV is the displayed sequence", ["False — MCV is assessed before lineage", "False — RPI is not used in the flowchart", "True — but only for multiple-lineage disease"],
    "The diagram begins with single versus multiple lineages; the single-lineage branch then divides by RPI and MCV.")

GUIDES = {
    S1: ("WHO Thresholds & Haematopoiesis", "Hb thresholds on p66: male <13, female <12, pregnancy <11 and CKD <10 g/dL.\nPPHSC splits to myeloid and lymphoid progenitors; the chart traces RBC stages.\nEPO is renal; thrombopoietin is hepatic; early erythroid stages differ in EPO/iron dependence."),
    S2: ("Erythroid Maturation", "Pro-normoblast is largest and nucleolated; early normoblast loses nucleoli.\nPolychromatic cells become gray, round-nucleated and stop dividing; orthochromatic cells are red/pyknotic.\nReticulocytes lose the nucleus but retain RNA; a giant proerythroblast is noted in pure red-cell aplasia."),
    S3: ("Reticulocytes and Indices", "Supravital dyes detect reticulocyte RNA; normal count 0.5–1.5%, absolute 25,000–75,000/µL.\nLow production → reticulocytopenia; destruction/loss → reticulocytosis.\nCRC corrects for anaemia; RPI also corrects for premature-reticulocyte lifespan."),
    S4: ("Approach & Marrow Notes", "Start with lineages, then RPI (<2.5 hypo; >2.5 hyper) and MCV (<80, 80–100, >100 fL).\nThe page lists hypoproliferative causes and marrow images/ratio.\nCellularity = 100 − age; normal M:E = 3:1; marrow failure replaces cells with fat."),
}


def main():
    questions = []
    for i, (sec, page, fmt, stem, opts, ans, exp) in enumerate(RAW, 1):
        questions.append({"id": f"MED-C{CHAPTER}-{i:02d}", "sec": sec,
                          "page": page, "fmt": fmt, "q": stem,
                          "opts": opts, "ans": ans, "exp": exp})
    sections = list(dict.fromkeys(row[0] for row in RAW))
    units = []
    for n, sec in enumerate(sections, 1):
        title, guide = GUIDES[sec]
        units.append({"id": f"MED-U{CHAPTER}-{n}", "ch": CHAPTER, "n": n,
                      "title": title, "sec": sec, "guide": guide,
                      "qs": [q["id"] for q in questions if q["sec"] == sec]})
    out = DATA / f"ch{CHAPTER:02d}.json"
    out.write_text(json.dumps({"chapter": CHAPTER, "title": TITLE,
                               "pageRange": PAGES, "questions": questions,
                               "units": units}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out.name}: {len(questions)} questions / {len(units)} units")


if __name__ == "__main__":
    main()
