#!/usr/bin/env python3
"""Generate Chapter 14 Macrocytic Anemia (Book p82–88)."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 14
TITLE = "Macrocytic Anemia"
PAGES = "82-88"

S1 = "Types, Causes & B12 vs Folate Stores"
S2 = "Vitamin B12 Sources & Absorption Pathway"
S3 = "Causes of B12 Deficiency, Transcobalamins & Functions"
S4 = "Folic Acid Metabolism, Folate Trap & Deficiency Causes"
S5 = "Diagnosis of Megaloblastic Anemia & Bone Marrow"
S6 = "Pernicious Anemia: Pathogenesis & Clinical Features"
S7 = "Pernicious Anemia: CNS/GI Features, Workup & Treatment"

RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    rng = random.Random(14000 + CHAPTER * 10000 + len(RAW))
    rng.shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2, f"truefalse True count: {stem}"
        assert sum(o.startswith("False") for o in options) == 2, f"truefalse False count: {stem}"
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p82 — Types and Causes of Macrocytic Anemia; B12 vs Folic Acid Table
add(S1, 82, "numeric",
    "At the top of the p82 classification chart, macrocytic anemia is defined by a Mean Corpuscular Volume (MCV) threshold of:",
    "> 100 fL",
    ["< 80 fL", "80–100 fL", "> 120 fL"],
    "The p82 chart begins with MCV > 100 fL, dividing into megaloblastic and normoblastic changes.")

add(S1, 82, "recall",
    "Under MCV > 100 fL, what are the two main morphological branches in the p82 chart?",
    "Megaloblastic changes (megaloblastic anemia) and normoblastic changes",
    [
        "Microcytic hypochromic changes and dimorphic changes",
        "Intravascular hemolysis and extravascular hemolysis",
        "Hypoproliferative aplasia and hyperproliferative erythrocytosis",
    ],
    "MCV > 100 fL branches into Megaloblastic changes (megaloblastic anemia) and Normoblastic changes.")

add(S1, 82, "recall",
    "What is the first defining cellular feature listed under megaloblastic changes on p82?",
    "Large nucleated erythroid precursors",
    [
        "Small enucleated microcytes",
        "Ring-shaped mitochondrial iron deposits",
        "Sickle-shaped normoblasts",
    ],
    "Megaloblastic changes: first bullet is Large nucleated erythroid precursors.")

add(S1, 82, "recall",
    "What is the second defining cellular feature of megaloblastic changes on p82 regarding the nucleus?",
    "Nuclear maturation lags (no condensation of chromatin)",
    [
        "Cytoplasmic maturation lags behind hypercondensed pyknotic chromatin",
        "Premature extrusion of the nucleus at the proerythroblast stage",
        "Mitotic arrest in metaphase with fragmentation of the nuclear envelope",
    ],
    "Megaloblastic changes: second bullet is Nuclear maturation lags (No condensation of chromatin).")

add(S1, 82, "recall",
    "Which two classic vitamin deficiencies head the list of causes of megaloblastic changes on p82?",
    "Vitamin B12 deficiency and folate deficiency",
    [
        "Vitamin C deficiency and vitamin D deficiency",
        "Pyridoxine deficiency and riboflavin deficiency",
        "Vitamin A deficiency and vitamin E deficiency",
    ],
    "Causes of megaloblastic changes start with Vit B12 deficiency and Folate deficiency.")

add(S1, 82, "recall",
    "Which three drugs inhibiting DNA synthesis are specifically listed under causes of megaloblastic anemia on p82?",
    "Cytarabine, hydroxyurea and 6-mercaptopurine",
    [
        "Chloramphenicol, isoniazid and pyrazinamide",
        "Cyclophosphamide, vincristine and doxorubicin",
        "Cisplatin, bleomycin and etoposide",
    ],
    "Drugs inhibiting DNA synthesis listed on p82 are cytarabine, hydroxyurea, and 6-mercaptopurine.")

add(S1, 82, "fillup",
    "Besides Vitamin B12 and folate deficiency, which other B-vitamin deficiency is listed as a cause of megaloblastic anemia on p82? ____ deficiency.",
    "Thiamine",
    ["Biotin", "Niacin", "Pantothenic acid"],
    "Thiamine deficiency is listed as the fourth cause of megaloblastic anemia on p82.")

add(S1, 82, "fillup",
    "The inherited metabolic disorder of pyrimidine metabolism listed as the fifth cause of megaloblastic anemia on p82 is ____.",
    "Orotic aciduria",
    ["Homocystinuria", "Alkaptonuria", "Maple syrup urine disease"],
    "Orotic aciduria (Pyrimidine metabolism) is the fifth listed cause of megaloblastic anemia on p82.")

add(S1, 82, "recall",
    "Under normoblastic macrocytic changes on p82, bone marrow failure syndromes are subdivided into which two entities?",
    "Myelodysplastic syndrome (MDS, macro-ovalocytes) and aplastic anemia",
    [
        "Myelofibrosis and polycythemia vera",
        "Paroxysmal nocturnal hemoglobinuria and Fanconi anemia",
        "Pure red cell aplasia and sideroblastic anemia",
    ],
    "Under Normoblastic changes, bone marrow failure syndromes branch into MDS (macro-ovalocytes) and Aplastic anemia.")

add(S1, 82, "recall",
    "Which hepatic and nutritional conditions follow bone marrow failure syndromes under normoblastic macrocytic causes on p82?",
    "Liver disease and scurvy",
    [
        "Celiac disease and pellagra",
        "Tropical sprue and beriberi",
        "Whipple's disease and rickets",
    ],
    "Normoblastic causes list: Bone marrow failure syndromes, Liver disease, Scurvy.")

add(S1, 82, "recall",
    "Which endocrine and substance-related conditions are listed next under normoblastic macrocytic causes on p82?",
    "Hypothyroidism and alcoholism",
    [
        "Hyperthyroidism and opioid use",
        "Cushing's syndrome and tobacco smoking",
        "Acromegaly and salicylate toxicity",
    ],
    "Normoblastic causes list continues with Hypothyroidism and Alcoholism.")

add(S1, 82, "recall",
    "Why does brisk reticulocytosis produce normoblastic macrocytosis according to the p82 list?",
    "Reticulocytes are polychromatic big RBCs",
    [
        "Reticulocytes retain uncondensed nuclear chromatin",
        "Reticulocytes accumulate excess membrane cholesterol from the liver",
        "Reticulocytes fuse in the splenic cords after acute hemorrhage",
    ],
    "The normoblastic list notes: Brisk reticulocytosis (Polychromatic big RBCs).")

add(S1, 82, "recall",
    "Which two final conditions complete the list of normoblastic macrocytic causes on p82?",
    "Post bleeding and COPD",
    [
        "Chronic renal failure and asthma",
        "Splenectomy and bronchiectasis",
        "Lead poisoning and pulmonary embolism",
    ],
    "The final two items under normoblastic changes on p82 are Post bleeding and COPD.")

add(S1, 82, "oddoneout",
    "Pick the ODD ONE OUT — which of the following is classified under megaloblastic changes rather than normoblastic changes on p82?",
    "Orotic aciduria",
    [
        "Hypothyroidism",
        "Scurvy",
        "COPD",
    ],
    "Normoblastic causes on p82 are bone marrow failure syndromes (MDS, aplastic anemia), liver disease, scurvy, hypothyroidism, alcoholism, brisk reticulocytosis, post bleeding, and COPD; orotic aciduria is under megaloblastic changes.")

add(S1, 82, "recall",
    "The peripheral blood smear image on p82 illustrates which red-cell morphology seen in liver disease?",
    "Target cells",
    [
        "Tear-drop cells (dacrocytes)",
        "Helmet cells (schistocytes)",
        "Pencil cells",
    ],
    "The smear image on p82 is captioned 'Target cells in liver disease'.")

add(S1, 82, "recall",
    "According to the p82 note, thiamine acts as a cofactor for which two enzyme systems involved in DNA synthesis?",
    "Pyruvate dehydrogenase and transketolase–transaldolase",
    [
        "ALA synthase and ferrochelatase",
        "Methionine synthase and methylmalonyl-CoA mutase",
        "Dihydrofolate reductase and thymidylate synthase",
    ],
    "Note on p82: Thiamine acts as a co-factor for Pyruvate dehydrogenase and Transketolase–transaldolase → DNA synthesis.")

add(S1, 82, "recall",
    "What are the three morphological changes in the smear of MDS listed on p82, and which one is marked most common (m/c)?",
    "Macrocytic (macro-ovalocytes, most common), megaloblastic and sideroblastic",
    [
        "Microcytic hypochromic (most common), spherocytic and targetoid",
        "Normocytic normochromic (most common), sickle-shaped and acanthocytic",
        "Sideroblastic (most common), schistocytic and elliptocytic",
    ],
    "Morphological changes in smear of MDS: Macrocytic (macro-ovalocytes) : m/c, Megaloblastic, and Sideroblastic.")

add(S1, 82, "numeric",
    "In the bottom comparison table on p82, what are the body stores of Vitamin B12 and Folic Acid respectively?",
    "Vit B12: 2–5 mg; Folic Acid: 5–10 mg",
    [
        "Vit B12: 5–10 mg; Folic Acid: 2–5 mg",
        "Vit B12: 3–7 µg; Folic Acid: 50 µg",
        "Vit B12: 50–100 mg; Folic Acid: 500 mg",
    ],
    "Table on p82: Body stores — Vit B12: 2–5 mg; Folic Acid: 5–10 mg.")

add(S1, 82, "numeric",
    "In the p82 comparison table, what is the Recommended Daily Allowance (RDA) of Vitamin B12 and Folic Acid respectively?",
    "Vit B12: 3–7 µg/day; Folic Acid: 50 µg/day",
    [
        "Vit B12: 50 µg/day; Folic Acid: 3–7 µg/day",
        "Vit B12: 2–5 mg/day; Folic Acid: 5–10 mg/day",
        "Vit B12: 1000 µg/day; Folic Acid: 400 mg/day",
    ],
    "Table on p82: RDA — Vit B12: 3–7 µg/day; Folic Acid: 50 µg/day.")

add(S1, 82, "numeric",
    "In the p82 comparison table, what is the time taken for depletion of Vitamin B12 versus Folic Acid?",
    "Vit B12: 2–5 years; Folic Acid: Few weeks",
    [
        "Vit B12: Few weeks; Folic Acid: 2–5 years",
        "Vit B12: 2–5 months; Folic Acid: 1–2 years",
        "Vit B12: 10–15 years; Folic Acid: 6–12 months",
    ],
    "Table on p82: Time taken for depletion — Vit B12: 2–5 years; Folic Acid: Few weeks.")

add(S1, 82, "match",
    "Match each parameter in the p82 comparison table to the printed values for Vitamin B12 and Folic Acid — 1) Body stores 2) Recommended Daily Allowance (RDA) 3) Time taken for depletion … A) Vit B12: 3–7 µg/day; Folic acid: 50 µg/day B) Vit B12: 2–5 years; Folic acid: Few weeks C) Vit B12: 2–5 mg; Folic acid: 5–10 mg",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "Table on p82: Body stores — Vit B12 2–5 mg, Folic acid 5–10 mg; RDA — Vit B12 3–7 µg/day, Folic acid 50 µg/day; Time taken for depletion — Vit B12 2–5 years, Folic acid few weeks.")

add(S1, 82, "truefalse",
    "TRUE or FALSE — according to the boxed note on p82, Vitamin B12 stores take more than 3 years to deplete, making deficiency less common even in vegetarians.",
    "True — Vit B12 stores take >3 years to deplete, so deficiency is less common even in vegetarians",
    [
        "True — because the RDA of Vitamin B12 (50 µg/day) is lower than its 5–10 mg body store",
        "False — Vitamin B12 stores deplete within a few weeks in strict vegetarians",
        "False — Folic acid stores take >3 years to deplete, whereas B12 depletes in weeks",
    ],
    "Boxed note on p82: Vit B12 stores take >3 years to deplete → Deficiency is less common, even in vegetarians.")

# ---------------------------------------------------------------------------
# Book p83 — Vitamin B12 Major Causes & Absorption Pathway
add(S2, 83, "recall",
    "At the top of p83, what are the two major causes of Vitamin B12 deficiency?",
    "Autoimmune and GI pathology",
    [
        "Nutritional and increased physiological demand",
        "Drug-induced inhibition and acute blood loss",
        "Renal tubular loss and hepatic failure",
    ],
    "Top of p83: Vitamin B-12 major causes of deficiency → Autoimmune and GI pathology.")

add(S2, 83, "fillup",
    "According to the note at the top of p83, the major cause of Folic acid (FA) deficiency is ____.",
    "Nutritional",
    ["Autoimmune", "Terminal ileal resection", "Achlorhydria"],
    "Note on p83: major cause of Folic acid (FA) deficiency → Nutritional.")

add(S2, 83, "recall",
    "In the Absorption of Vit-B12 flowchart on p83, what is the most common (m/c) dietary source of Vitamin B12?",
    "Animal origin",
    [
        "Green leafy vegetables",
        "Citrus fruits and legumes",
        "Whole grains and tubers",
    ],
    "Vitamin B12 in diet : m/c animal origin.")

add(S2, 83, "recall",
    "Which two active cobalamin forms are listed for dietary Vitamin B12 on p83?",
    "Adenosylcobalamin and methylcobalamin",
    [
        "Cyanocobalamin and hydroxocobalamin",
        "Monoglutamate and polyglutamate",
        "Tetrahydrofolate and dihydrofolate",
    ],
    "Vitamin B12 in diet : m/c animal origin → Adenosylcobalamine and Methylcobalamine.")

add(S2, 83, "fillup",
    "In the stomach, dietary Vitamin B12 combines with ____ (present in saliva) to form a complex.",
    "R-factor / Haptocorrin",
    ["Intrinsic factor (IF)", "Transcobalamin-2 (TC-2)", "Cubilin-amnionless (CUBAM)"],
    "Stomach: Combines with R-factor/Haptocorrin (present in saliva) to form a complex.")

add(S2, 83, "recall",
    "Where do pancreatic enzymes split the Vitamin B12–R-factor complex according to the p83 pathway?",
    "Duodenum (Parts 2 and 3)",
    [
        "Gastric fundus and body",
        "Distal jejunum",
        "Terminal ileum",
    ],
    "Duodenum (Parts 2 & 3): Pancreatic enzymes split the complex.")

add(S2, 83, "recall",
    "After pancreatic enzymes split the R-factor complex in the duodenum, Vitamin B12 combines with:",
    "Intrinsic Factor (IF) secreted by parietal cells",
    [
        "Pepsinogen secreted by chief cells",
        "Transcobalamin-1 secreted by granulocytes",
        "Secretin released by duodenal S cells",
    ],
    "Vit B12 combines with Intrinsic Factor (IF) secreted by parietal cells.")

add(S2, 83, "recall",
    "In the ileum, the IF–B12 complex binds to which specific receptor complex before being released into circulation?",
    "CUBAM receptors (cubilin–amnionless complex)",
    [
        "DMT-1 (divalent metal transporter-1) receptors",
        "ASBT (apical sodium-dependent bile acid transporter)",
        "Heme carrier protein-1 (HCP-1) receptors",
    ],
    "Ileum: IF–B12 complex + CUBAM receptors (Cubilin amnionless complex) → Released into circulation.")

add(S2, 83, "fillup",
    "Once released into circulation, Vitamin B12 binds with Transcobalamin-2 (TC-2) to form ____.",
    "Holotranscobalamin",
    ["Haptocorrin", "Apotranscobalamin", "Hemosiderin"],
    "Circulation: Binds with Transcobalamin-2 (TC-2) to form holotranscobalamin.")

add(S2, 83, "recall",
    "What is the destination and function of holotranscobalamin at the bottom of the p83 absorption flowchart?",
    "Reaches bone marrow for hemoglobin synthesis and RBC maturation",
    [
        "Reaches renal cortex for erythropoietin transcription",
        "Reaches spleen for macrophage iron recycling",
        "Reaches duodenum for ferroportin upregulation",
    ],
    "Holotranscobalamin reaches bone marrow → Bone marrow: Hemoglobin synthesis & RBC maturation.")

add(S2, 83, "recall",
    "In the bottom note on p83, parietal cells located in the body, neck, and isthmus of the stomach secrete which two substances?",
    "HCl and Intrinsic factor (IF)",
    [
        "Pepsinogen and gastrin",
        "Mucin and somatostatin",
        "Histamine and R-factor",
    ],
    "Note on p83: Stomach — Body, neck, isthmus : Parietal cells secrete HCl and Intrinsic factor (IF).")

add(S2, 83, "recall",
    "In the bottom note on p83, which cells are located at the base of the gastric gland and what do they secrete?",
    "Chief cells secrete pepsinogen",
    [
        "Parietal cells secrete intrinsic factor",
        "G cells secrete gastrin",
        "Mucous neck cells secrete bicarbonate",
    ],
    "Note on p83: Base : Chief cells secrete pepsinogen.")

add(S2, 83, "match",
    "Match each component of the gastric cobalamin phase and p83 bottom note to its cell type or function — 1) Salivary R-binder 2) Body, neck and isthmus of gastric gland 3) Base of gastric gland … A) Chief cells secreting pepsinogen B) Binds free cobalamin released from food by HCl and pepsin C) Parietal cells secreting HCl and Intrinsic Factor (IF)",
    "1-B, 2-C, 3-A",
    [
        "1-C, 2-B, 3-A",
        "1-A, 2-C, 3-B",
        "1-B, 2-A, 3-C",
    ],
    "On p83: salivary R-binder binds free cobalamin in the stomach; Note at bottom of p83: Body, neck, isthmus — Parietal cells secrete HCl and Intrinsic factor (IF); Base — Chief cells secrete pepsinogen.")

# ---------------------------------------------------------------------------
# Book p84 — Causes of Vit-B12 Deficiency, Transcobalamins & Functions
add(S3, 84, "recall",
    "Under autoimmune causes of Vitamin B12 deficiency on p84, which condition is identified as the 'most important cause'?",
    "Pernicious anemia",
    [
        "Celiac disease",
        "Autoimmune pancreatitis",
        "Primary biliary cholangitis",
    ],
    "1. Autoimmune: Pernicious anemia — most important cause.")

add(S3, 84, "recall",
    "In pernicious anemia on p84, antibodies are produced against which two targets?",
    "Parietal cells and Intrinsic Factor (IF)",
    [
        "Chief cells and pepsinogen",
        "G cells and gastrin receptors",
        "Enterochromaffin-like (ECL) cells and haptocorrin",
    ],
    "Pernicious anemia: Antibodies produced against parietal cells and IF.")

add(S3, 84, "recall",
    "According to the side note on p84, which three substances are absorbed ONLY at the ileum?",
    "Vitamin B12, bile acids and magnesium",
    [
        "Iron, calcium and folate",
        "Vitamin B12, folate and thiamine",
        "Bile acids, copper and zinc",
    ],
    "Note on p84: Substances absorbed only at ileum: Vit B12, Bile acids, Magnesium.")

add(S3, 84, "recall",
    "Which three ileal diseases are listed under cause #2 of Vitamin B12 deficiency on p84?",
    "Crohn's disease, tropical sprue and tuberculosis (TB)",
    [
        "Ulcerative colitis, celiac disease and Whipple's disease",
        "Microscopic colitis, diversion colitis and Giardia",
        "Short bowel syndrome, carcinoid tumor and lymphoma",
    ],
    "2. Ileal disease: Crohn's disease, Tropical Sprue, TB.")

add(S3, 84, "recall",
    "How does Small Intestinal Bacterial Overgrowth (SIBO, cause #3 on p84) lead to Vitamin B12 deficiency?",
    "Bacteria from the large bowel migrate to the small bowel and consume Vitamin B12",
    [
        "Bacteria in the stomach cleave intrinsic factor before it reaches the duodenum",
        "Bacteria in the colon oxidize transcobalamin-2 in portal blood",
        "Bacteria in the jejunum secrete antibodies against CUBAM receptors",
    ],
    "3. SIBO: Bacteria from large bowel migrate to small bowel → consume Vit B12.")

add(S3, 84, "recall",
    "Which three systemic disorders are given as examples of dysmotility causing SIBO on p84?",
    "Scleroderma, diabetes mellitus (DM) and amyloidosis",
    [
        "Hyperthyroidism, Addison's disease and pheochromocytoma",
        "Systemic lupus erythematosus, gout and ankylosing spondylitis",
        "Multiple sclerosis, myasthenia gravis and Guillain–Barré syndrome",
    ],
    "SIBO causes — Dysmotility: E.g. in Scleroderma, DM, Amyloidosis.")

add(S3, 84, "recall",
    "Besides dysmotility, which two additional causes of SIBO are listed on p84?",
    "PPIs (cause hypochlorhydria) and blind loop syndrome",
    [
        "NSAIDs (cause mucosal erosions) and pyloric stenosis",
        "H2 blockers and Zenker diverticulum",
        "Antacids and Meckel diverticulum",
    ],
    "SIBO causes on p84: Dysmotility (Scleroderma, DM, Amyloidosis), PPIs (cause hypochlorhydria), and Blind loop syndrome.")

add(S3, 84, "recall",
    "Which transport-protein defect is listed first under congenital causes (cause #4) of Vitamin B12 deficiency on p84?",
    "Transcobalamin-2 deficiency",
    [
        "Transcobalamin-1 deficiency",
        "Haptocorrin excess",
        "Ceruloplasmin deficiency",
    ],
    "4. Congenital: first bullet is Transcobalamin-2 deficiency.")

add(S3, 84, "recall",
    "Under congenital causes on p84, a CUBAM mutation causes which named syndrome and clinical triad/pair?",
    "Imerslund–Gräsbeck syndrome (B12 deficiency + proteinuria)",
    [
        "Plummer–Vinson syndrome (B12 deficiency + esophageal webs)",
        "Fanconi syndrome (B12 deficiency + glycosuria)",
        "Hartnup disease (B12 deficiency + aminoaciduria)",
    ],
    "4. Congenital: CUBAM mutation causing Imerslund-Grasbeck syndrome (B12 deficiency + proteinuria).")

add(S3, 84, "fillup",
    "Cause #5 of Vitamin B12 deficiency on p84 is fish tapeworm infection caused by ____.",
    "Diphyllobothrium latum",
    ["Taenia solium", "Echinococcus granulosus", "Schistosoma haematobium"],
    "5. Fish tapeworm (Diphyllobothrium latum) infection.")

add(S3, 84, "recall",
    "According to the note below fish tapeworm on p84, what deficiency is caused by Ancylostoma (hookworm)?",
    "Iron deficiency",
    [
        "Vitamin B12 deficiency",
        "Folic acid deficiency",
        "Copper deficiency",
    ],
    "Note on p84: Ancylostoma (Hookworm) : Causes iron deficiency.")

add(S3, 84, "match",
    "Match each intestinal cause or helminth on p84 to its resulting hematological deficiency or mechanism — 1) Diphyllobothrium latum (fish tapeworm) 2) Ancylostoma (hookworm) 3) Terminal ileal resection or Crohn disease … A) Iron deficiency B) Loss of ileal IF–Cbl receptor absorption site C) Vitamin B12 deficiency",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "5. Fish tapeworm (Diphyllobothrium latum) infection causes Vit B12 deficiency; ileal disease/resection impairs ileal Cbl absorption; Note: Ancylostoma (Hookworm) causes iron deficiency.")

add(S3, 84, "recall",
    "In the Transcobalamin (TC) types chart on p84, which cells produce TC-1?",
    "Granulocytes",
    [
        "Hepatocytes",
        "Gastric parietal cells",
        "Ileal enterocytes",
    ],
    "TC-1: Produced by granulocytes.")

add(S3, 84, "recall",
    "Why is TC-1 increased in myeloproliferative neoplasms (MPN), and what laboratory effect does this produce?",
    "MPN causes proliferation of mature granulocytes, leading to increased Vitamin B12 binding capacity",
    [
        "MPN causes lysis of erythroblasts, leading to decreased Vitamin B12 binding capacity",
        "MPN causes megakaryocyte aplasia, leading to absent holotranscobalamin",
        "MPN causes hepatic fibrosis, leading to urinary loss of Vitamin B12",
    ],
    "↑ TC-1 in myeloproliferative neoplasms (MPN) (MPN → Proliferation of mature granulocytes) → Causes ↑ Vit-B12 binding capacity.")

add(S3, 84, "recall",
    "Where is Transcobalamin-2 (TC-2) produced, and what is its role on p84?",
    "Produced in all tissues, especially liver; has an important role in transport",
    [
        "Produced exclusively by mature granulocytes; stores B12 in bone marrow",
        "Produced by salivary glands; protects B12 from gastric acid",
        "Produced by renal tubular cells; reabsorbs B12 from glomerular filtrate",
    ],
    "TC-2: Produced in all tissues, especially liver; Important role in transport.")

add(S3, 84, "recall",
    "How is the role of Transcobalamin-3 (TC-3) described in the p84 chart?",
    "Has some role in transport",
    [
        "Primary receptor for ileal absorption",
        "Sole storage protein inside hepatocytes",
        "Inhibitor of intrinsic factor binding",
    ],
    "TC-3: Has some role in transport.")

add(S3, 84, "match",
    "Match each Transcobalamin (TC) type on p84 to its source and clinical role — 1) TC-1 2) TC-2 3) TC-3 … A) Produced by granulocytes; increased in MPN, causing increased Vit-B12 binding capacity B) Has some role in transport C) Produced in all tissues (especially liver); important role in transport",
    "1-A, 2-C, 3-B",
    [
        "1-C, 2-A, 3-B",
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
    ],
    "TC-1 is produced by granulocytes and ↑ in MPN (→ ↑ Vit-B12 binding capacity); TC-2 is produced in all tissues, especially liver, with an important role in transport; TC-3 has some role in transport.")

add(S3, 84, "fillup",
    "At the bottom of p84 under Functions, Vitamin B12 acts as a cofactor for Process 1: converting Homocysteine into ____.",
    "Methionine",
    ["Cystathionine", "Succinyl CoA", "Tetrahydrofolate"],
    "Functions: Co-factor for 2 processes — 1. Homocysteine --(Vit B12)--> Methionine.")

add(S3, 84, "fillup",
    "At the bottom of p84 under Functions, Vitamin B12 acts as a cofactor for Process 2: converting Methylmalonyl CoA into ____.",
    "Succinyl CoA",
    ["Propionyl CoA", "Acetyl CoA", "Malonyl CoA"],
    "Functions: Co-factor for 2 processes — 2. Methylmalonyl CoA --(Vit B12)--> Succinyl CoA.")

# ---------------------------------------------------------------------------
# Book p85 — Folic Acid Metabolism, Comparison Table, Folate Trap & Causes
add(S4, 85, "fillup",
    "Under Metabolism of Folic Acid on p85, the site of absorption is the proximal small intestine, specifically the ____.",
    "Jejunum and duodenum",
    ["Terminal ileum and cecum", "Stomach body and fundus", "Distal ileum and ascending colon"],
    "Metabolism of Folic Acid: Site of absorption : Proximal small intestine (Jejunum & duodenum).")

add(S4, 85, "recall",
    "In the intestinal lumen diagram on p85, what is the major form of folate in food?",
    "Monoglutamate",
    [
        "5-methyl THFA",
        "Adenosylcobalamin",
        "Cyanocobalamin",
    ],
    "In intestinal lumen: Monoglutamate (major form in food).")

add(S4, 85, "recall",
    "In the p85 folate metabolism diagram, monoglutamate is converted into which form that serves as the 'circulating & storage form'?",
    "5-methyl THFA",
    [
        "Dihydrofolate (DHFA)",
        "Formiminoglutamate (FIGLU)",
        "Holotranscobalamin",
    ],
    "Monoglutamate (major form in food) → 5-methyl THFA (Circulating & storage form).")

add(S4, 85, "recall",
    "In the p85 diagram, the conversion of 5-methyl THFA to active THFA is coupled to which Vitamin B12-dependent reaction?",
    "Homocysteine → Methionine",
    [
        "Methylmalonyl CoA → Succinyl CoA",
        "Succinyl CoA + Glycine → ALA",
        "Pyruvate → Acetyl CoA",
    ],
    "The arrow from 5-methyl THFA to THFA is coupled with Homocysteine --(Vit B12)--> Methionine.")

add(S4, 85, "recall",
    "What are the two functions of THFA shown at the right end of the p85 metabolism diagram?",
    "1-carbon transfer and DNA synthesis",
    [
        "Heme iron oxidation and globin folding",
        "Myelin lipid methylation and odd-chain fatty acid synthesis",
        "Disulfide bond reduction and glutathione regeneration",
    ],
    "THFA : Function → 1-carbon transfer and DNA synthesis.")

add(S4, 85, "recall",
    "In the p85 comparison table, what is the pattern of 5-methyl/THFA levels across Folate deficiency, Vit B12 deficiency, and combined Vit B12 + Folate deficiency?",
    "Folate deficiency: ↓; Vit B12 deficiency: ↑; Vit B12 + Folate deficiency: ↓",
    [
        "Folate deficiency: ↑; Vit B12 deficiency: ↓; Vit B12 + Folate deficiency: ↑",
        "Folate deficiency: ↓; Vit B12 deficiency: ↓; Vit B12 + Folate deficiency: Ⓝ",
        "Folate deficiency: Ⓝ; Vit B12 deficiency: ↑; Vit B12 + Folate deficiency: ↑",
    ],
    "5-methyl/THFA levels row on p85: Folate deficiency ↓, Vit B12 deficiency ↑, Vit B12 + Folate deficiency ↓.")

add(S4, 85, "recall",
    "In the p85 comparison table, what happens to Homocysteine levels across Folate deficiency, Vit B12 deficiency, and combined Vit B12 + Folate deficiency?",
    "Increased (↑) in all three conditions",
    [
        "Increased (↑) in Vit B12 deficiency but normal (Ⓝ) in folate deficiency",
        "Decreased (↓) in folate deficiency and increased (↑) in Vit B12 deficiency",
        "Normal (Ⓝ) in isolated deficiencies and increased (↑) only in combined deficiency",
    ],
    "Homocysteine levels row on p85: Folate deficiency ↑, Vit B12 deficiency ↑, Vit B12 + Folate deficiency ↑.")

add(S4, 85, "recall",
    "In the p85 comparison table, how do Methylmalonyl CoA levels distinguish Folate deficiency from Vit B12 deficiency (and combined deficiency)?",
    "Normal (Ⓝ) in folate deficiency; increased (↑) in Vit B12 deficiency and in combined Vit B12 + folate deficiency",
    [
        "Increased (↑) in folate deficiency; normal (Ⓝ) in Vit B12 deficiency",
        "Decreased (↓) in folate deficiency; normal (Ⓝ) in Vit B12 deficiency",
        "Increased (↑) in all three conditions equally",
    ],
    "Methylmalonyl CoA levels row on p85: Folate deficiency Ⓝ, Vit B12 deficiency ↑, Vit B12 + Folate deficiency ↑.")

add(S4, 85, "recall",
    "In the p85 comparison table, what is the Red cell folate level entry under Vit B12 deficiency?",
    "Decreased or normal (↓ / Ⓝ)",
    [
        "Markedly increased (↑↑)",
        "Always normal (Ⓝ)",
        "Completely absent (0)",
    ],
    "Red cell folate levels row on p85 shows ↓ / Ⓝ under Vit B12 deficiency (and dashes under the other two columns).")

add(S4, 85, "match",
    "Match each deficiency column in the p85 table to its metabolic profile — 1) Folate deficiency 2) Vitamin B12 deficiency 3) Combined Vit B12 + Folate deficiency … A) 5-methyl/THFA ↑, Homocysteine ↑, Methylmalonyl CoA ↑, Red cell folate ↓/Ⓝ B) 5-methyl/THFA ↓, Homocysteine ↑, Methylmalonyl CoA Ⓝ C) 5-methyl/THFA ↓, Homocysteine ↑, Methylmalonyl CoA ↑",
    "1-B, 2-A, 3-C",
    [
        "1-A, 2-B, 3-C",
        "1-C, 2-A, 3-B",
        "1-B, 2-C, 3-A",
    ],
    "p85 table: Folate deficiency has 5-methyl/THFA ↓, Homocysteine ↑, Methylmalonyl CoA Ⓝ; Vit B12 deficiency has 5-methyl/THFA ↑, Homocysteine ↑, Methylmalonyl CoA ↑, Red cell folate ↓/Ⓝ; Combined deficiency has 5-methyl/THFA ↓, Homocysteine ↑, Methylmalonyl CoA ↑.")

add(S4, 85, "fillup",
    "In the p85 note, the 'Folate trap' is defined as Vitamin B12 deficiency leading to accumulation of ____.",
    "5-methyl THFA",
    ["Monoglutamate", "Succinyl CoA", "Methionine"],
    "Note on p85: Folate trap : Vit B12 deficiency → Accumulation of 5-methyl THFA.")

add(S4, 85, "recall",
    "In the 'Causes of Deficiency (Based on mechanism)' chart for folic acid on p85, what is labelled as the 'major cause' under ↓ Intake?",
    "Nutritional",
    [
        "Autoimmune gastritis",
        "Blind loop syndrome",
        "Fish tapeworm infection",
    ],
    "↓ Intake (major cause) → Nutritional.")

add(S4, 85, "recall",
    "Under the '↓ absorption' branch of folic acid deficiency on p85, which intestinal disorder is specifically listed?",
    "Celiac disease",
    [
        "Ulcerative proctitis",
        "Diverticulosis",
        "Hirschsprung disease",
    ],
    "↓ absorption → Celiac disease.")

add(S4, 85, "recall",
    "Which three conditions are listed under the '↑ demand' branch of folic acid deficiency on p85?",
    "Pregnancy, growth and hemolysis (compensatory erythropoiesis)",
    [
        "Hypothyroidism, aplastic anemia and chronic kidney disease",
        "Cirrhosis, nephrotic syndrome and heart failure",
        "COPD, polycythemia vera and hemochromatosis",
    ],
    "↑ demand → Pregnancy, Growth, Hemolysis (Compensatory erythropoiesis).")

add(S4, 85, "recall",
    "Which six drugs or drug classes are listed under the 'Drugs' branch of folic acid deficiency on p85?",
    "Folate antagonists (methotrexate), sulfasalazine, PPIs, pyrimethamine, triamterene and phenytoin",
    [
        "Chloramphenicol, isoniazid, pyrazinamide, rifampicin, ethambutol and levofloxacin",
        "Azathioprine, mycophenolate, cyclosporine, tacrolimus, sirolimus and prednisolone",
        "Warfarin, heparin, aspirin, clopidogrel, dabigatran and rivaroxaban",
    ],
    "Drugs causing folate deficiency on p85: Folate antagonists (methotrexate), Sulfasalazine, PPIs, Pyrimethamine, Triamterene, and Phenytoin.")

add(S4, 85, "match",
    "Match each mechanism of folic acid deficiency on p85 to its printed etiology — 1) Decreased intake (major cause) 2) Decreased absorption 3) Increased demand … A) Celiac disease B) Pregnancy, growth and hemolysis (compensatory erythropoiesis) C) Nutritional",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "Causes of folate deficiency based on mechanism: ↓ Intake (major cause) → Nutritional; ↓ Absorption → Celiac disease; ↑ Demand → Pregnancy, Growth, Hemolysis (compensatory erythropoiesis).")

# ---------------------------------------------------------------------------
# Book p86 — Diagnosis of Megaloblastic Anemia
add(S5, 86, "numeric",
    "Under Diagnosis of Megaloblastic Anemia on p86, what serum Vitamin B12 threshold indicates 'Normal levels'?",
    "> 300 pg",
    ["< 200 pg", "100–200 pg", "200–300 pg"],
    "1. Serum Vit B12 levels: > 300 pg → Normal levels.")

add(S5, 86, "numeric",
    "What serum Vitamin B12 threshold on p86 directly diagnoses 'Vit B12 deficiency'?",
    "< 200 pg",
    ["> 300 pg", "200–300 pg", "> 500 pg"],
    "1. Serum Vit B12 levels: < 200 pg → Vit B12 deficiency.")

add(S5, 86, "recall",
    "When serum Vitamin B12 is borderline (200–300 pg), which three analytes does the p86 flowchart direct you to determine, and what is their printed change in Vit B12 deficiency?",
    "Methylmalonyl CoA, serum folate and homocysteine — all increased in Vit B12 deficiency (as printed)",
    [
        "Serum ferritin, TIBC and transferrin saturation — all decreased in Vit B12 deficiency",
        "Urine urobilinogen, serum haptoglobin and LDH — all normal in Vit B12 deficiency",
        "Reticulocyte count, red cell folate and holotranscobalamin — all increased in Vit B12 deficiency",
    ],
    "Under 200–300 pg: Determine levels of Methylmalonyl CoA, Serum folate, Homocysteine → All increased in Vit B12 deficiency.")

add(S5, 86, "match",
    "Match the serum Vitamin B12 level on p86 to its diagnostic interpretation — 1) > 300 pg 2) 200 – 300 pg 3) < 200 pg … A) Vitamin B12 deficiency B) Normal levels C) Borderline: determine methylmalonyl CoA, serum folate and homocysteine",
    "1-B, 2-C, 3-A",
    [
        "1-A, 2-C, 3-B",
        "1-B, 2-A, 3-C",
        "1-C, 2-B, 3-A",
    ],
    "1. Serum Vit B12 levels: >300 pg = Normal levels; 200–300 pg = Determine levels of methylmalonyl CoA, serum folate, homocysteine; <200 pg = Vit B12 deficiency.")

add(S5, 86, "recall",
    "According to item 2 of Diagnosis of Megaloblastic Anemia on p86, in which body fluid is methylmalonyl CoA (MMA) measured?",
    "In urine",
    [
        "In cerebrospinal fluid",
        "In saliva",
        "In synovial fluid",
    ],
    "2. Methylmalonyl CoA (MMA) : In urine.")

add(S5, 86, "recall",
    "According to item 3 on p86, which antibody is positive (+) in pernicious anemia?",
    "Anti-parietal cell antibody",
    [
        "Anti-mitochondrial antibody",
        "Anti-tissue transglutaminase antibody",
        "Anti-centromere antibody",
    ],
    "3. Anti-parietal cell antibody : (+) in pernicious anemia.")

add(S5, 86, "numeric",
    "On the peripheral blood smear (item 4 on p86), hypersegmented neutrophils are labelled the 'earliest change' and defined as having how many lobes?",
    "≥ 5 lobes",
    ["< 2 lobes", "2–3 lobes", "≥ 8 lobes"],
    "Peripheral blood smear shows megaloblasts and hypersegmented neutrophils with ≥ 5 lobes (earliest change).")

add(S5, 86, "recall",
    "According to the boxed note on p86, what are neutrophils with fewer than 2 lobes (< 2 lobes) called, and in what condition are they seen?",
    "Pseudo-Pelger–Huët cells, seen in myelodysplastic syndrome (MDS)",
    [
        "Dohle-body neutrophils, seen in bacterial sepsis",
        "Basket cells, seen in chronic lymphocytic leukemia",
        "Alder–Reilly neutrophils, seen in mucopolysaccharidosis",
    ],
    "Boxed note on p86: Neutrophils with < 2 lobes: Pseudo-Pelger-Huet cells, seen in MDS.")

add(S5, 86, "recall",
    "Which three peripheral blood smear inclusions are illustrated in order under 'Features of dyserythropoiesis' on p86?",
    "1. Cabot ring, 2. Basophilic stippling, and 3. Howell–Jolly bodies",
    [
        "1. Heinz bodies, 2. Pappenheimer bodies, and 3. Schuffner's dots",
        "1. Auer rods, 2. Dohle bodies, and 3. Birbeck granules",
        "1. Russell bodies, 2. Dutcher bodies, and 3. Negri bodies",
    ],
    "Features of dyserythropoiesis on p86: 1. Cabot ring, 2. Basophilic stippling, 3. Howell-Jolly bodies.")

add(S5, 86, "fillup",
    "Because megaloblastic anemia involves ineffective erythropoiesis, the reticulocyte count on peripheral smear (p86) shows ____.",
    "Reticulocytopenia",
    ["Brisk reticulocytosis", "Thrombocytosis", "Leukemoid reaction"],
    "Peripheral blood smear bullet on p86: Reticulocytopenia.")

add(S5, 86, "numeric",
    "Pancytopenia due to trilineage involvement occurs in what percentage of megaloblastic anemia cases on p86?",
    "15–20%",
    ["1–5%", "50–60%", "80–90%"],
    "The p86 smear section lists: Pancytopenia d/t trilineage involvement in 15–20%.")

add(S5, 86, "recall",
    "Which four conditions are listed in the bottom note on p86 under 'Other causes of pancytopenia'?",
    "Hairy-cell leukemia, leukemia, myelodysplastic syndromes (MDS) and aplastic anemia",
    [
        "Iron deficiency anemia, thalassemia trait, polycythemia vera and essential thrombocythemia",
        "Hereditary spherocytosis, G6PD deficiency, autoimmune hemolytic anemia and sickle cell trait",
        "Infectious mononucleosis, idiopathic thrombocytopenic purpura, hemophilia A and von Willebrand disease",
    ],
    "Note on p86 — Other causes of pancytopenia: Hairy-cell leukemia, Leukemia, Myelodysplastic syndromes (MDS), and Aplastic anemia.")

# ---------------------------------------------------------------------------
# Book p87 — Bone Marrow Smear; Pernicious Anemia Pathogenesis & Clinical Features
add(S5, 87, "recall",
    "According to item 5 at the top of p87, when is a bone marrow smear performed in megaloblastic anemia?",
    "Done in pancytopenia",
    [
        "Done in every asymptomatic patient with MCV 101 fL",
        "Done only after 10 weeks of hydroxycobalamin therapy",
        "Done only when serum Vitamin B12 exceeds 300 pg",
    ],
    "5. Bone marrow smear : Done in pancytopenia.")

add(S5, 87, "recall",
    "What are the bone marrow smear findings listed in item 5 on p87, and how do they affect the Myeloid : Erythroid (M:E) ratio?",
    "Dyserythropoiesis and erythroid hyperplasia, leading to a decreased (↓) Myeloid : Erythroid ratio",
    [
        "Myeloid hyperplasia and erythroid aplasia, leading to an increased (↑) Myeloid : Erythroid ratio",
        "Fat replacement of all marrow elements with an unchanged Myeloid : Erythroid ratio",
        "Megakaryocytic hyperplasia and fibrosis, leading to an inverted 10:1 Myeloid : Erythroid ratio",
    ],
    "Bone marrow smear findings: Dyserythropoiesis; Erythroid hyperplasia → ↓ Myeloid : Erythroid ratio.")

add(S5, 87, "recall",
    "Which two cellular abnormalities are specifically listed beneath the 'Bone marrow aspirate' photomicrograph on p87?",
    "Megaloblasts and giant metamyelocytes",
    [
        "Ring sideroblasts and micromegakaryocytes",
        "Reed–Sternberg cells and smudge cells",
        "Flame cells and Mott cells",
    ],
    "The p87 bone marrow aspirate caption lists: • Megaloblasts, • Giant metamyelocytes (alongside the Erythroid hyperplasia image).")

add(S6, 87, "recall",
    "Under Pernicious Anemia Pathogenesis on p87, which autoimmune antibody is labelled 'Sensitive' and which is labelled 'Specific'?",
    "Sensitive: Anti-parietal cell antibody; Specific: Anti-intrinsic factor antibody",
    [
        "Sensitive: Anti-intrinsic factor antibody; Specific: Anti-parietal cell antibody",
        "Sensitive: Anti-haptocorrin antibody; Specific: Anti-transcobalamin antibody",
        "Sensitive: Anti-smooth muscle antibody; Specific: Anti-gastrin antibody",
    ],
    "Pernicious anemia pathogenesis on p87: Autoimmune antibodies → Sensitive: Anti-parietal cell antibody; Specific for: Anti-intrinsic factor antibody.")

add(S6, 87, "match",
    "Match each autoimmune feature in pernicious anemia (p87) to its diagnostic characteristic — 1) Anti-parietal cell antibody 2) Anti-intrinsic factor antibody 3) Type A gastritis … A) Specific autoantibody for pernicious anemia B) Sensitive autoantibody for pernicious anemia C) Autoimmune gastritis targeting the gastric body and fundus",
    "1-B, 2-A, 3-C",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B",
    ],
    "Pernicious anemia pathogenesis on p87: Type A autoimmune gastritis affects the gastric body/fundus; Sensitive: Anti-parietal cell antibody; Specific for: Anti-intrinsic factor antibody.")

add(S6, 87, "recall",
    "In the pernicious anemia pathogenesis diagram on p87, autoimmune antibodies lead to Vitamin B12 deficiency on one branch and, on the other branch, to hypergastrinemia with which three clinical features?",
    "Abdominal pain, ulcerations and diarrhoea (osmotic/secretory)",
    [
        "Constipation, dysphagia and hematemesis",
        "Jaundice, ascites and splenomegaly",
        "Steatorrhea, tenesmus and rectal prolapse",
    ],
    "The p87 diagram prints: Antibodies → Vit B12 deficiency and 'Hyperchlorhydria' [printed source text; pathophysiologically parietal cell loss causes achlorhydria/hypochlorhydria] → Hypergastrinemia : c/f → Abdominal pain, Ulcerations, Diarrhoea (Osmotic/secretory).")

add(S6, 87, "recall",
    "Which three autoimmune diseases are listed as associations of pernicious anemia on p87?",
    "Addison's disease, Type 1 diabetes mellitus and vitiligo",
    [
        "Graves' disease, myasthenia gravis and systemic sclerosis",
        "Rheumatoid arthritis, ankylosing spondylitis and psoriasis",
        "Goodpasture syndrome, pemphigus vulgaris and polymyositis",
    ],
    "Autoimmune association on p87: Addison's, Type 1 DM, Vitiligo.")

add(S6, 87, "recall",
    "What is the anatomical distribution of gastric involvement noted in pernicious anemia on p87?",
    "Antral sparing with body involvement",
    [
        "Body sparing with isolated antral involvement",
        "Diffuse pangastritis involving fundus, body and pylorus equally",
        "Isolated cardia and gastroesophageal junction involvement",
    ],
    "The p87 pathogenesis section states: Antral sparing with body involvement.")

add(S6, 87, "recall",
    "What is the typical patient demographic and initial symptom status listed under clinical features of pernicious anemia on p87?",
    "Middle-aged to elderly female; often asymptomatic",
    [
        "Adolescent male; acute febrile crisis",
        "Infant under 1 year; severe failure to thrive",
        "Young adult male; acute hematemesis",
    ],
    "Clinical features on p87: Middle-aged to elderly female; Often asymptomatic.")

add(S6, 87, "recall",
    "Why does pallor in pernicious anemia have a yellowish tinge (lemon-yellow tint) according to p87?",
    "Due to hemolytic jaundice (from intramedullary hemolysis / ineffective erythropoiesis)",
    [
        "Due to obstructive choledocholithiasis",
        "Due to dietary carotene accumulation",
        "Due to hepatic cirrhosis and conjugated hyperbilirubinemia",
    ],
    "Pallor : With yellowish tinge (D/t hemolytic jaundice).")

add(S6, 87, "recall",
    "Which three skin and mucosal changes are listed for pernicious anemia at the bottom of p87?",
    "Angular cheilitis, atrophic glossitis with beefy-red tongue, and hyperpigmentation",
    [
        "Koilonychia, esophageal webs, and alopecia areata",
        "Erythema nodosum, pyoderma gangrenosum, and aphthous ulcers",
        "Malar rash, discoid plaques, and livedo reticularis",
    ],
    "Skin & mucosal changes on p87: Angular cheilitis, Atrophic glossitis with beefy-red tongue, and Hyperpigmentation.")

# ---------------------------------------------------------------------------
# Book p88 — CNS/GI Features, Folate Note, Investigations & Treatment
add(S7, 88, "recall",
    "In subacute combined degeneration (SCD) of the spinal cord on p88, which spinal cord columns and tracts are involved?",
    "Posterior (dorsal column) and lateral (lateral corticospinal and spinothalamic tract) columns",
    [
        "Anterior horn motor neurons and anterior spinocerebellar tracts only",
        "Substantia gelatinosa and Lissauer's tract only",
        "Central canal ependyma and vestibulospinal tracts only",
    ],
    "CNS features (Spinal cord involvement): D/t posterior (Dorsal column) and lateral (Lateral corticospinal & spinothalamic tract) column involvement.")

add(S7, 88, "recall",
    "How is peripheral neuropathy clinically manifested in the CNS features list on p88?",
    "Paraesthesia of hands and feet",
    [
        "Isolated wrist drop and foot drop without sensory loss",
        "Bulbar palsy and dysphagia",
        "Resting pill-rolling tremor and cogwheel rigidity",
    ],
    "Peripheral neuropathy (Paraesthesia of hands & feet).")

add(S7, 88, "recall",
    "Which two structures are affected in the 'Late changes' of CNS involvement on p88?",
    "Cortex and optic nerve",
    [
        "Cerebellum and oculomotor nerve",
        "Basal ganglia and facial nerve",
        "Hypothalamus and vagus nerve",
    ],
    "Late changes : Involves Cortex and Optic nerve.")

add(S7, 88, "recall",
    "Under GI symptoms on p88, pernicious anemia increases the risk of gastric cancer (M > F). Which neoplasm is marked most common (m/c), and which is marked rare?",
    "Gastric carcinoid type 1 (most common) and gastric adenocarcinoma (rare)",
    [
        "Gastric adenocarcinoma (most common) and gastric MALT lymphoma (rare)",
        "Gastrointestinal stromal tumor (most common) and gastric carcinoid type 3 (rare)",
        "Squamous cell carcinoma (most common) and leiomyosarcoma (rare)",
    ],
    "GI symptoms: ↑ risk of cancer (M>F) → Gastric carcinoid type 1 (m/c) and Gastric adenocarcinoma (Rare).")

add(S7, 88, "truefalse",
    "TRUE or FALSE — according to the boxed note on p88, folic acid deficiency can cause a less severe peripheral neuropathy, but spinal cord involvement is absent.",
    "True — in folic acid deficiency, peripheral neuropathy is (+) (less severe) and spinal cord involvement is (–)",
    [
        "True — both spinal cord involvement and optic neuropathy are more severe in folate deficiency",
        "False — folic acid deficiency never causes any peripheral neuropathy",
        "False — folic acid deficiency causes isolated posterior column degeneration without neuropathy",
    ],
    "Boxed note on p88: In folic acid deficiency: Peripheral neuropathy (+) (Less severe); Spinal cord involvement (–).")

add(S7, 88, "recall",
    "What do the two sagittal spinal MRI images on p88 illustrate?",
    "Subacute combined degeneration (SCD) before treatment and after treatment",
    [
        "Cervical spondylotic myelopathy before and after decompression",
        "Syringomyelia before and after shunting",
        "Transverse myelitis before and after plasmapheresis",
    ],
    "The two spinal MRI images on p88 are captioned 'Subacute combined degeneration (SCD) — Before treatment / After treatment'.")

add(S7, 88, "recall",
    "Which four findings are listed under Peripheral Blood Smear in the investigations of pernicious anemia on p88?",
    "Oval macrocytosis with elevated MCV, dyserythropoiesis, leukopenia (in 15–20%) with hypersegmented neutrophils, and thrombocytopenia",
    [
        "Microcytic hypochromic RBCs, thrombocytosis, leukocytosis with left shift, and target cells",
        "Spherocytosis, reticulocytosis, normoblastic erythroid precursors, and Howell-Jolly bodies only",
        "Dimorphic RBCs, ring sideroblasts, basophilia, and pseudo-Pelger-Huet neutrophils",
    ],
    "Peripheral Blood Smear on p88: Oval macrocytosis with elevated MCV, Dyserythropoiesis, Leukopenia (in 15–20%) with hypersegmented neutrophils, and Thrombocytopenia.")

add(S7, 88, "recall",
    "Under Investigations on p88, what are the bone marrow morphology and specific serological test listed for pernicious anemia?",
    "Bone marrow: Megaloblastic; Serology: Anti-IF antibody",
    [
        "Bone marrow: Normoblastic; Serology: Anti-smooth muscle antibody",
        "Bone marrow: Hypocellular aplastic; Serology: Direct Coombs test",
        "Bone marrow: Ring sideroblasts; Serology: Anti-endomysial antibody",
    ],
    "Bone marrow : Megaloblastic. Serology : Anti-IF antibody.")

add(S7, 88, "recall",
    "Under Investigations on p88, what is the pattern of serum gastrin levels and serum Vitamin B12 levels in pernicious anemia?",
    "Serum gastrin levels: Increased (↑); Serum Vit B12 levels: Markedly decreased (↓↓)",
    [
        "Serum gastrin levels: Decreased (↓); Serum Vit B12 levels: Increased (↑)",
        "Both serum gastrin and serum Vit B12 levels are decreased (↓)",
        "Both serum gastrin and serum Vit B12 levels are increased (↑)",
    ],
    "Serum gastrin levels : ↑; Serum Vit B12 levels : ↓↓.")

add(S7, 88, "match",
    "Match each investigation in pernicious anemia (p88) to its characteristic result — 1) Bone marrow 2) Serology 3) Serum gastrin levels 4) Serum Vit B12 levels … A) Markedly decreased (↓↓) B) Megaloblastic C) Anti-IF antibody D) Increased (↑)",
    "1-B, 2-C, 3-D, 4-A",
    [
        "1-B, 2-D, 3-C, 4-A",
        "1-A, 2-C, 3-D, 4-B",
        "1-C, 2-B, 3-A, 4-D",
    ],
    "Investigations on p88: Bone marrow: Megaloblastic; Serology: Anti-IF antibody; Serum gastrin levels: ↑; Serum Vit B12 levels: ↓↓.")

add(S7, 88, "fillup",
    "Under Treatment of pernicious anemia on p88, lifelong Vitamin B12 supplementation is given using ____.",
    "Hydroxycobalamin",
    ["Folinic acid", "Pyridoxal phosphate", "Ferrous carboxymaltose"],
    "Treatment: Lifelong Vit B12 supplementation (Hydroxycobalamin).")

add(S7, 88, "management",
    "What is the exact 3-step dosing regimen for Hydroxycobalamin printed under Treatment on p88?",
    "1000 µg OD for 1 week → 1000 µg weekly for 1 month → 1000 µg once a month lifelong (every 6–12 months as printed)",
    [
        "100 µg OD for 1 month → 100 µg monthly for 6 months → discontinue once MCV normalizes",
        "500 µg BD for 2 weeks → 500 µg daily for 3 months → oral maintenance only",
        "2000 µg single IV infusion → repeat once every 5 years",
    ],
    "Regimen on p88: 1000 µg OD for 1 week → 1000 µg weekly for 1 month → 1000 µg once a month lifelong every 6–12 months.")

add(S7, 88, "numeric",
    "Under Response to treatment on p88, when does the reticulocyte count begin to rise and when does it reach its maximum?",
    "Rises by Day 2–3; maximum by 6–8 days",
    [
        "Rises by Day 5–7; maximum by 10–14 days",
        "Rises by Day 10–14; maximum by 4 weeks",
        "Rises within 12 hours; maximum by Day 2",
    ],
    "Response to treatment: Reticulocyte count → ↑ by Day 2–3, maximum by 6–8 days.")

add(S7, 88, "numeric",
    "Under Response to treatment on p88, how long does it take for MCV to normalize, and what is the overall prognosis?",
    "MCV normal in 10 weeks; prognosis is good with treatment",
    [
        "MCV normal in 2 weeks; prognosis is guarded despite treatment",
        "MCV normal in 6 months; prognosis is poor if leukopenia was present",
        "MCV normal in 3 days; prognosis depends on splenectomy",
    ],
    "Response to treatment on p88: MCV : Normal in 10 weeks; Prognosis : Good with treatment.")


GUIDES = {
    S1: (
        "Types, Causes & B12 vs Folate Stores",
        "Macrocytic anemia (MCV >100 fL) divides into megaloblastic (lagging nuclear maturation) and normoblastic causes.\n"
        "Megaloblastic causes include B12/folate/thiamine deficiency, DNA-synthesis inhibitors (cytarabine, hydroxyurea, 6-MP) and orotic aciduria.\n"
        "B12 stores (2–5 mg; RDA 3–7 µg/d) last 2–5 years (>3 yr in vegetarians); folate stores (5–10 mg; RDA 50 µg/d) deplete in a few weeks.",
    ),
    S2: (
        "Vitamin B12 Sources & Absorption",
        "Dietary B12 (animal origin: adenosyl- and methylcobalamin) binds salivary R-factor/haptocorrin in the stomach.\n"
        "Pancreatic enzymes split the complex in duodenum (parts 2 & 3) so B12 binds parietal-cell Intrinsic Factor (IF).\n"
        "Ileal CUBAM receptors absorb IF-B12; plasma TC-2 forms holotranscobalamin for marrow RBC maturation.",
    ),
    S3: (
        "B12 Deficiency, Transcobalamins & Roles",
        "Causes: Pernicious anemia (most important), ileal disease (Crohn's, tropical sprue, TB), SIBO, TC-2/CUBAM defects (Imerslund–Gräsbeck), and D. latum.\n"
        "Only B12, bile acids and Mg are absorbed solely in the ileum; TC-1 (from granulocytes) rises in MPN, while TC-2 mediates transport.\n"
        "B12 is a cofactor for Homocysteine → Methionine and Methylmalonyl CoA → Succinyl CoA.",
    ),
    S4: (
        "Folate Metabolism, Trap & Causes",
        "Folate is absorbed in proximal small bowel (jejunum/duodenum); dietary monoglutamate becomes circulating/storage 5-methyl THFA → THFA.\n"
        "B12 deficiency causes the 'folate trap' (5-methyl THFA accumulation) and raises both homocysteine and methylmalonyl CoA (MMA is normal in pure folate deficiency).\n"
        "Folate deficiency stems from ↓ intake (nutritional, major cause), celiac disease, ↑ demand (pregnancy, growth, hemolysis) and drugs (MTX, sulfasalazine, PPIs, pyrimethamine, triamterene, phenytoin).",
    ),
    S5: (
        "Diagnosis of Megaloblastic Anemia",
        "Serum B12 >300 pg is normal, <200 pg is deficient, and 200–300 pg prompts MMA, folate and homocysteine testing.\n"
        "Smear shows megaloblasts, hypersegmented neutrophils (≥5 lobes, earliest change; <2 lobes = pseudo-Pelger–Huët in MDS), Cabot rings, basophilic stippling and Howell–Jolly bodies.\n"
        "Pancytopenia occurs in 15–20% and warrants bone marrow smear (dyserythropoiesis, erythroid hyperplasia, ↓ M:E ratio, giant metamyelocytes).",
    ),
    S6: (
        "Pernicious Anemia: Pathogenesis & Signs",
        "Anti-parietal cell antibody is sensitive; anti-intrinsic factor antibody is specific; body involvement with antral sparing is classic.\n"
        "Associated with Addison's disease, Type 1 DM and vitiligo; affects middle-aged to elderly females who are often asymptomatic.\n"
        "Clinical features include lemon-yellow pallor (hemolytic jaundice), angular cheilitis, beefy-red atrophic glossitis and hyperpigmentation.",
    ),
    S7: (
        "Pernicious Anemia: CNS, Workup & Rx",
        "SCD involves dorsal and lateral columns plus peripheral neuropathy and late cortical/optic changes (folate deficiency spares the spinal cord).\n"
        "Increases risk of gastric carcinoid type 1 (m/c) and gastric adenocarcinoma (rare); workup shows oval macrocytosis, anti-IF Ab, ↑ gastrin and ↓↓ B12.\n"
        "Hydroxycobalamin (1000 µg OD × 1 wk → weekly × 1 mo → monthly lifelong) raises reticulocytes by day 2–3 (peak day 6–8) and normalizes MCV in 10 weeks.",
    ),
}


def main():
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
            {
                "chapter": CHAPTER,
                "title": TITLE,
                "pageRange": PAGES,
                "questions": questions,
                "units": units,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {out.name}: {len(questions)} questions / {len(units)} units")


if __name__ == "__main__":
    main()
