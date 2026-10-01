#!/usr/bin/env python3
"""Generate Chapter 15 Approach to Hemolysis (Book p89–91)."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 15
TITLE = "Approach to Hemolysis"
PAGES = "89-91"

S1 = "Classification of Hemolytic Anemia"
S2 = "Abbreviations & Intravascular Hemolysis"
S3 = "Extravascular Hemolysis, Summary Table & Rules"

RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    rng = random.Random(15000 + CHAPTER * 10000 + len(RAW))
    rng.shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2, f"truefalse True count: {stem}"
        assert sum(o.startswith("False") for o in options) == 2, f"truefalse False count: {stem}"
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p89 — Classification of Hyperproliferative / Hemolytic Anemia
add(S1, 89, "numeric",
    "At the opening of Chapter 15 (p89), hyperproliferative anemia is defined by a Reticulocyte Production Index (RPI) of:",
    "> 2.5",
    ["< 1.0", "< 2.5", "> 5.0"],
    "Classification on p89 begins with: Hyperproliferative anemia (RPI > 2.5) : 3 classifications.")

add(S1, 89, "recall",
    "What are the three axes of classification for hyperproliferative (hemolytic) anemia listed at the top of p89?",
    "1. Inherited vs acquired, 2. Intracorpuscular vs extracorpuscular, and 3. Intravascular vs extravascular",
    [
        "1. Microcytic vs macrocytic, 2. Megaloblastic vs normoblastic, and 3. Acute vs chronic",
        "1. Warm vs cold, 2. Autoimmune vs alloimmune, and 3. Coombs-positive vs Coombs-negative",
        "1. Single-lineage vs trilineage, 2. Iron-deficient vs iron-replete, and 3. Hepcidin-high vs hepcidin-low",
    ],
    "The three classifications listed on p89 are: 1. Inherited vs acquired, 2. Intracorpuscular vs extracorpuscular, 3. Intravascular vs extravascular.")

add(S1, 89, "recall",
    "In the p89 master flowchart, Anemia first divides into Hypoproliferative anemia and Hyperproliferative anemia using which RPI cutoffs?",
    "RPI < 2.5 for hypoproliferative anemia; RPI > 2.5 (reticulocytosis) for hyperproliferative anemia",
    [
        "RPI < 1.5 for hypoproliferative anemia; RPI > 1.5 for hyperproliferative anemia",
        "RPI > 2.5 for hypoproliferative anemia; RPI < 2.5 for hyperproliferative anemia",
        "RPI < 0.5 for hypoproliferative anemia; RPI > 5.0 for hyperproliferative anemia",
    ],
    "Anemia branches into RPI < 2.5 (Hypoproliferative anemia) and RPI > 2.5 (Reticulocytosis → Hyperproliferative anemia).")

add(S1, 89, "recall",
    "Under Hypoproliferative anemia (RPI < 2.5) on the p89 chart, which three conditions are listed under 'Low-normal MCV'?",
    "1. Iron deficiency anemia, 2. Anemia of chronic disease, and 3. Sideroblastic anemia",
    [
        "1. Sickle cell anemia, 2. Thalassemia, and 3. Hereditary spherocytosis",
        "1. Vitamin B12 deficiency, 2. Folate deficiency, and 3. Orotic aciduria",
        "1. Aplastic anemia, 2. Myelodysplastic syndrome, and 3. Pure red cell aplasia",
    ],
    "Under Low-normal MCV on p89: 1. Iron deficiency anemia, 2. Anemia of chronic disease, 3. Sideroblastic anemia.")

add(S1, 89, "recall",
    "Under Hypoproliferative anemia (RPI < 2.5) on p89, which five causes are listed under 'Elevated MCV — Megaloblastic anemia'?",
    "1. Vitamin B12 deficiency, 2. Folate deficiency, 3. Orotic aciduria, 4. Thiamine deficiency, and 5. Drugs inhibiting DNA synthesis",
    [
        "1. Liver disease, 2. Scurvy, 3. Hypothyroidism, 4. Alcoholism, and 5. COPD",
        "1. Warm AIHA, 2. Cold AIHA, 3. PCH, 4. HDN, and 5. Transfusion reaction",
        "1. G6PD deficiency, 2. Pyruvate kinase deficiency, 3. 5' nucleotidase deficiency, 4. PNH, and 5. Sepsis",
    ],
    "Under Elevated MCV (Megaloblastic anemia) on p89: 1. Vitamin B12 deficiency, 2. Folate deficiency, 3. Orotic aciduria, 4. Thiamine deficiency, 5. Drugs inhibiting DNA synthesis.")

add(S1, 89, "recall",
    "Under Hyperproliferative anemia (RPI > 2.5), how do the 'Inherited' and 'Acquired' branches subdivide in the p89 chart?",
    "Inherited: Intracorpuscular vs Extracorpuscular; Acquired: Immune vs Non-immune",
    [
        "Inherited: Warm vs Cold; Acquired: Megaloblastic vs Normoblastic",
        "Inherited: Immune vs Non-immune; Acquired: Hemoglobinopathies vs Enzymopathies",
        "Inherited: Acute vs Chronic; Acquired: Sideroblastic vs Nonsideroblastic",
    ],
    "In the p89 chart, Inherited divides into Intracorpuscular and Extracorpuscular; Acquired divides into Immune and Non-immune.")

add(S1, 89, "recall",
    "Under Inherited → Intracorpuscular defects on p89, what are the three main subcategories?",
    "1. Hemoglobinopathies, 2. Membrane defects, and 3. Enzymopathies",
    [
        "1. Autoimmune, 2. Alloimmune, and 3. Drug-induced",
        "1. Fragmentation hemolysis, 2. PNH, and 3. Sepsis",
        "1. IRIDA, 2. DMT-1 mutation, and 3. Atransferrinemia",
    ],
    "Inherited Intracorpuscular defects on p89 list: 1. Hemoglobinopathies, 2. Membrane defects, 3. Enzymopathies.")

add(S1, 89, "recall",
    "Which two disorders are listed under '1. Hemoglobinopathies' in the Inherited Intracorpuscular column on p89?",
    "Sickle cell anemia and thalassemia",
    [
        "Hereditary spherocytosis and elliptocytosis",
        "G6PD deficiency and pyruvate kinase deficiency",
        "Paroxysmal nocturnal hemoglobinuria and atypical HUS",
    ],
    "1. Hemoglobinopathies: • Sickle cell anemia, • Thalassemia.")

add(S1, 89, "recall",
    "How is category '2. Membrane defects' described in the Inherited Intracorpuscular column on p89?",
    "Hereditary spherocytosis and its variants (elliptocytosis)",
    [
        "Paroxysmal nocturnal hemoglobinuria (PIGA mutation)",
        "Acanthocytosis and abetalipoproteinemia",
        "Stomatocytosis and xerocytosis only",
    ],
    "2. Membrane defects: Hereditary spherocytosis and its variants (Elliptocytosis).")

add(S1, 89, "recall",
    "Which three enzyme deficiencies are listed under '3. Enzymopathies' in the Inherited Intracorpuscular column on p89?",
    "G6PD deficiency, pyruvate kinase deficiency and 5' nucleotidase deficiency",
    [
        "ALA synthase deficiency, ferrochelatase deficiency and heme oxygenase deficiency",
        "Pyruvate dehydrogenase deficiency, transketolase deficiency and lactase deficiency",
        "Myeloperoxidase deficiency, catalase deficiency and superoxide dismutase deficiency",
    ],
    "3. Enzymopathies: • G6PD deficiency, • Pyruvate kinase deficiency, • 5' nucleotidase deficiency.")

add(S1, 89, "fillup",
    "In the p89 flowchart, the sole condition listed under Inherited → Extracorpuscular hemolysis is ____, which affects adults.",
    "Atypical (Familial) HUS",
    ["Paroxysmal nocturnal hemoglobinuria", "Paroxysmal cold hemoglobinuria", "Autoimmune hemolytic anemia"],
    "Under Inherited → Extracorpuscular: Atypical (Familial) HUS : Affects adults.")

add(S1, 89, "recall",
    "Under Acquired → Immune hemolytic anemia on p89, what are the three main numbered categories?",
    "1. Autoimmune cause (AIHA), 2. Alloimmune causes, and 3. Drug induced",
    [
        "1. Fragmentation hemolysis, 2. PNH, and 3. Sepsis",
        "1. Hemoglobinopathies, 2. Membrane defects, and 3. Enzymopathies",
        "1. Intravascular, 2. Extravascular, and 3. Combined",
    ],
    "Under Acquired → Immune: 1. Autoimmune cause : AIHA, 2. Alloimmune causes, 3. Drug induced.")

add(S1, 89, "recall",
    "Which three entities are listed under '1. Autoimmune cause : AIHA' on p89?",
    "Warm Ab AIHA, Cold Ab AIHA and paroxysmal cold hemoglobinuria",
    [
        "Hemolytic disease of newborn, hemolytic transfusion reaction and drug-induced AIHA",
        "HUS, TTP and disseminated intravascular coagulation",
        "Hereditary spherocytosis, elliptocytosis and Southeast Asian ovalocytosis",
    ],
    "1. Autoimmune cause : AIHA → • Warm Ab AIHA, • Cold Ab AIHA, • Paroxysmal cold hemoglobinuria.")

add(S1, 89, "recall",
    "Which two conditions are listed under '2. Alloimmune causes' on p89?",
    "Hemolytic disease of newborn (HDN) and hemolytic transfusion reaction",
    [
        "Warm Ab AIHA and Cold Ab AIHA",
        "Paroxysmal nocturnal hemoglobinuria and paroxysmal cold hemoglobinuria",
        "Atypical HUS and thrombotic thrombocytopenic purpura",
    ],
    "2. Alloimmune causes: • Hemolytic disease of newborn (HDN), • Hemolytic transfusion reaction.")

add(S1, 89, "recall",
    "Which four causes are listed under Acquired → Non-immune hemolytic anemia on p89, and which one is explicitly annotated '(Intracorpuscular)'?",
    "1. Fragmentation hemolysis (HUS/TTP syndrome), 2. PNH (Intracorpuscular), 3. Sepsis, and 4. Toxins & drugs",
    [
        "1. Warm AIHA, 2. Cold AIHA (Intracorpuscular), 3. HDN, and 4. Transfusion reaction",
        "1. Sickle cell anemia, 2. Thalassemia, 3. G6PD deficiency (Intracorpuscular), and 4. Lead",
        "1. Hypersplenism, 2. Liver cirrhosis (Intracorpuscular), 3. Scurvy, and 4. Hypothyroidism",
    ],
    "Under Acquired → Non-immune on p89: 1. Fragmentation hemolysis HUS/TTP Syndrome, 2. PNH (Intracorpuscular), 3. Sepsis, 4. Toxins & drugs.")

# ---------------------------------------------------------------------------
# Book p90 — Abbreviations & Intravascular Hemolysis
add(S2, 90, "recall",
    "At the top of p90, what are the printed expansions for RPI, AIHA, and HUS/TTP?",
    "RPI: Reticulocyte production index; AIHA: Autoimmune hemolytic anemia; HUS/TTP: Hemolytic uremic syndrome / Thrombotic thrombocytopenic purpura",
    [
        "RPI: Red cell proliferation index; AIHA: Alloimmune hemolytic aplasia; HUS/TTP: Hepatic uremic syndrome / Thrombotic thrombocytosis purpura",
        "RPI: Reticulocyte maturation index; AIHA: Acute intravascular hemolytic anemia; HUS/TTP: Hemorrhagic uremic syndrome / Transient thrombocytopenia",
        "RPI: Red cell production interval; AIHA: Autoimmune hypoplastic anemia; HUS/TTP: Hemolytic urinary syndrome / Thrombotic thrombocytopenic polycythemia",
    ],
    "Abbreviations on p90: RPI = Reticulocyte production index; AIHA = Autoimmune hemolytic anemia; HUS/TTP = Hemolytic uremic syndrome/Thrombotic thrombocytopenic purpura.")

add(S2, 90, "fillup",
    "In the abbreviations list on p90, Paroxysmal nocturnal hemoglobinuria (PNH) is specifically noted as being caused by a ____ gene mutation.",
    "PIGA",
    ["HFE", "JAK2", "MYD88"],
    "PNH : Paroxysmal nocturnal hemoglobinuria (PIGA gene mutation).")

add(S2, 90, "match",
    "Match each abbreviation at the top of p90 to its printed expansion — 1) RPI 2) AIHA 3) HUS/TTP 4) PNH … A) Autoimmune hemolytic anemia B) Paroxysmal nocturnal hemoglobinuria (PIGA gene mutation) C) Reticulocyte production index D) Hemolytic uremic syndrome / Thrombotic thrombocytopenic purpura",
    "1-C, 2-A, 3-D, 4-B",
    [
        "1-A, 2-C, 3-B, 4-D",
        "1-C, 2-D, 3-A, 4-B",
        "1-B, 2-A, 3-D, 4-C",
    ],
    "Abbreviations on p90: RPI = Reticulocyte production index; AIHA = Autoimmune hemolytic anemia; HUS/TTP = Hemolytic uremic syndrome/Thrombotic thrombocytopenic purpura; PNH = Paroxysmal nocturnal hemoglobinuria (PIGA gene mutation).")

add(S2, 90, "fillup",
    "Under 'Intravascular vs Extravascular Hemolysis' on p90, the anatomical site of intravascular hemolysis is ____.",
    "Blood vessels",
    ["Spleen", "Hepatic sinusoids", "Bone marrow"],
    "Intravascular hemolysis — Site : Blood vessels.")

add(S2, 90, "recall",
    "In the Intravascular hemolysis flowchart on p90, what are the four immediate features branching directly from 'Hemolysis'?",
    "↑ LDH, Hemoglobinemia (↑ Hb levels), Reticulocytosis and ↑ MCV",
    [
        "↓ LDH, Moderate splenomegaly, Reticulocytopenia and ↓ MCV",
        "↑ Ferritin, ↑ Tissue iron, Conjugated hyperbilirubinemia and ↑ Haptoglobin",
        "Pancytopenia, Ring sideroblasts, ↓ MCV and ↑ TIBC",
    ],
    "Under Intravascular hemolysis Features: Hemolysis → ↑ LDH, Hemoglobinemia (↑ Hb levels), Reticulocytosis, ↑ MCV.")

add(S2, 90, "recall",
    "In the intravascular hemolysis flowchart on p90, what happens when Haptoglobin binds with markedly increased free hemoglobin (↑↑ Hb)?",
    "Decreased serum haptoglobin (↓ S. haptoglobin), which is the most sensitive and specific test for hemolysis",
    [
        "Increased serum haptoglobin (↑ S. haptoglobin), which rules out intravascular hemolysis",
        "Conversion of haptoglobin into hemosiderin inside renal glomeruli",
        "Precipitation of haptoglobin as Heinz bodies on peripheral smear",
    ],
    "Haptoglobin binds with ↑↑ Hb → ↓ S. haptoglobin (most sensitive and specific test for hemolysis).")

add(S2, 90, "recall",
    "Under the 'In urine' branch of intravascular hemolysis on p90, which urinary finding occurs in acute cases and produces dark urine?",
    "Hemoglobinuria",
    [
        "Hemosiderinuria",
        "Urobilinogenuria",
        "Porphyrinuria",
    ],
    "In urine → Hemoglobinuria : • Acute cases, • Dark urine.")

add(S2, 90, "fillup",
    "Under the 'In urine' branch of intravascular hemolysis on p90, chronic cases are characterized by ____.",
    "Hemosiderinuria",
    ["Hemoglobinuria", "Myoglobinuria", "Bilirubinuria"],
    "In urine → Hemosiderinuria : Chronic cases.")

add(S2, 90, "match",
    "Match each finding of intravascular hemolysis on p90 to its clinical timing or mechanism — 1) Hemoglobinuria (with dark urine) 2) Hemosiderinuria 3) Decreased serum haptoglobin … A) Chronic intravascular hemolysis cases B) Acute intravascular hemolysis cases C) Binding of free hemoglobin dimers released into plasma",
    "1-B, 2-A, 3-C",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B",
    ],
    "In intravascular hemolysis (p90): free Hb binds haptoglobin (↓ haptoglobin); in urine, Hemoglobinuria → Acute cases, Dark urine; Hemosiderinuria → Chronic cases.")

add(S2, 90, "recall",
    "What is the serum bilirubin abnormality shown on the right branch of Hemoglobinemia in intravascular hemolysis (p90)?",
    "Mild unconjugated hyperbilirubinemia",
    [
        "Severe conjugated (direct) hyperbilirubinemia",
        "Complete absence of serum bilirubin",
        "Markedly elevated delta-bilirubin with acholic stools",
    ],
    "Under Hemoglobinemia on p90, the S. bilirubin branch leads to: mild unconjugated hyperbilirubinemia.")

add(S2, 90, "recall",
    "In the Causes of Intravascular Hemolysis table on p90, which column is marked 'm/c' (most common), and which four causes does it list?",
    "Acute onset (m/c): mismatched blood transfusion, sepsis, toxins and G6PD deficiency",
    [
        "Chronic onset (m/c): PNH, MAHA and paroxysmal cold hemoglobinuria",
        "Acute onset (m/c): warm AIHA, hereditary spherocytosis, thalassemia and sickle cell trait",
        "Chronic onset (m/c): iron deficiency, anemia of chronic disease, lead and alcoholism",
    ],
    "Causes table on p90 — Acute onset (m/c): • Mismatched blood transfusion, • Sepsis, • Toxins, • G6PD deficiency.")

add(S2, 90, "recall",
    "In the 'Chronic/acute on chronic onset' column of intravascular hemolysis on p90, how is MAHA expanded and explained?",
    "Microangiopathic hemolytic anemia: fragmentation hemolysis / HUS",
    [
        "Macroangiopathic hemolytic aplasia: autoimmune splenomegaly / ITP",
        "Myeloid-associated hemolytic anemia: ring sideroblasts / MDS",
        "Membrane-associated hereditary anemia: spherocytosis / elliptocytosis",
    ],
    "Chronic/acute on chronic onset column on p90 lists: PNH, MAHA (microangiopathic hemolytic anemia : Fragmentation hemolysis/HUS), and Paroxysmal cold hemoglobinuria.")

add(S2, 90, "match",
    "Match each cause of intravascular hemolysis on p90 to its onset category and mechanism — 1) Mismatched blood transfusion, sepsis, toxins and G6PD deficiency 2) PNH (PIGA mutation) 3) MAHA (fragmentation hemolysis / HUS) and paroxysmal cold hemoglobinuria … A) Acute onset intravascular hemolysis (m/c) B) Chronic / acute-on-chronic mechanical or Donath-Landsteiner hemolysis C) Chronic / acute-on-chronic GPI-anchor complement-mediated hemolysis",
    "1-A, 2-C, 3-B",
    [
        "1-C, 2-A, 3-B",
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
    ],
    "Table on p90 separates Acute onset (m/c) (mismatched blood transfusion, sepsis, toxins, G6PD deficiency) from Chronic/acute on chronic onset (PNH, MAHA/fragmentation hemolysis/HUS, paroxysmal cold hemoglobinuria).")

# ---------------------------------------------------------------------------
# Book p91 — Extravascular Hemolysis, Summary Table & Inherited/Acquired Rules
add(S3, 91, "fillup",
    "At the top of p91, the anatomical site of extravascular hemolysis is the ____.",
    "Spleen",
    ["Blood vessels", "Renal proximal tubule", "Thymus"],
    "Extravascular hemolysis — Site : Spleen.")

add(S3, 91, "recall",
    "In the Extravascular hemolysis flowchart on p91, what are the four immediate features branching from 'Hemolysis'?",
    "Moderate splenomegaly, Hemoglobin released, Reticulocytosis and ↑ MCV",
    [
        "Hemoglobinuria, Hemosiderinuria, Reticulocytopenia and ↓ MCV",
        "Absent spleen, Plasma Hb ++, ↓ Ferritin and Normal MCV",
        "Pancytopenia, ↓ LDH, ↑ Haptoglobin and Microcytosis",
    ],
    "Extravascular hemolysis Features: Hemolysis → Moderate splenomegaly, Hemoglobin released, Reticulocytosis, ↑ MCV.")

add(S3, 91, "recall",
    "When hemoglobin is released during extravascular hemolysis on p91, it splits into Heme and Globin. What happens to the Globin moiety?",
    "Goes to the amino acid pool",
    [
        "Excreted unchanged in the urine as hemosiderin",
        "Converted by biliverdin reductase into stercobilinogen",
        "Stored inside macrophages as ferritin",
    ],
    "In the p91 flowchart: Globin → Goes to amino acid pool.")

add(S3, 91, "recall",
    "In the extravascular hemolysis flowchart on p91, Heme splits into Iron and Protoporphyrin. What is the fate of the Iron branch?",
    "Iron → ↑ Iron stores → ↑ S. ferritin",
    [
        "Iron → ↓ Iron stores → ↓ S. ferritin",
        "Iron → Excreted in urine as hemosiderinuria",
        "Iron → Binds haptoglobin in plasma",
    ],
    "Heme → Iron → ↑ Iron stores → ↑ S. ferritin.")

add(S3, 91, "fillup",
    "In the extravascular hemolysis pathway on p91, Protoporphyrin is converted into Biliverdin by the enzyme ____.",
    "Heme oxygenase",
    ["Biliverdin reductase", "ALA synthase", "Ferrochelatase"],
    "Protoporphyrin --(Heme oxygenase)--> Biliverdin.")

add(S3, 91, "fillup",
    "In the extravascular hemolysis pathway on p91, Biliverdin is converted into Bilirubin by the enzyme ____.",
    "Biliverdin reductase",
    ["Heme oxygenase", "UDP-glucuronosyltransferase", "Pyruvate kinase"],
    "Biliverdin --(Biliverdin reductase)--> Bilirubin.")

add(S3, 91, "recall",
    "In extravascular hemolysis on p91, Bilirubin production leads to unconjugated hyperbilirubinemia with which two downstream excretory findings?",
    "↑ Urobilinogen in urine and ↑ Stercobilinogen in feces",
    [
        "↑ Conjugated bilirubin in urine and clay-colored acholic feces",
        "↑ Hemoglobinuria and ↑ Hemosiderinuria",
        "↓ Urobilinogen in urine and ↓ Stercobilinogen in feces",
    ],
    "Bilirubin → Unconjugated hyperbilirubinemia: • ↑ Urobilinogen in urine, • ↑ Stercobilinogen in feces.")

add(S3, 91, "recall",
    "In the 'Summary of findings' table on p91, what are the entries for Plasma Hb, Urine Hb, and Urine hemosiderin in Intravascular vs Extravascular hemolysis?",
    "Intravascular hemolysis: ++ for all three; Extravascular hemolysis: – for all three",
    [
        "Intravascular hemolysis: – for all three; Extravascular hemolysis: ++ for all three",
        "Intravascular hemolysis: ++ for Plasma Hb only; Extravascular hemolysis: ++ for Urine Hb and hemosiderin",
        "Both Intravascular and Extravascular hemolysis: ++ for all three",
    ],
    "Summary table on p91: Plasma Hb, Urine Hb, and Urine hemosiderin are ++ in Intravascular hemolysis and – in Extravascular hemolysis.")

add(S3, 91, "recall",
    "In the 'Summary of findings' table on p91, what are the entries for Tissue iron and S. ferritin in Intravascular vs Extravascular hemolysis?",
    "Intravascular hemolysis: – for both; Extravascular hemolysis: ++ for both",
    [
        "Intravascular hemolysis: ++ for both; Extravascular hemolysis: – for both",
        "Intravascular hemolysis: ++ for Tissue iron and – for S. ferritin",
        "Both Intravascular and Extravascular hemolysis: – for both",
    ],
    "Summary table on p91: Tissue iron and S. ferritin are – in Intravascular hemolysis and ++ in Extravascular hemolysis.")

add(S3, 91, "recall",
    "In the 'Summary of findings' table on p91, how do LDH and S. haptoglobin compare between Intravascular and Extravascular hemolysis?",
    "LDH is ↑↑↑ in intravascular vs ↑↑ in extravascular; S. haptoglobin is ↓↓↓ in intravascular vs ↓↓ in extravascular",
    [
        "LDH is ↑ in intravascular vs ↑↑↑ in extravascular; S. haptoglobin is ↓ in intravascular vs ↓↓↓ in extravascular",
        "LDH is normal in intravascular vs ↑↑ in extravascular; S. haptoglobin is ↑↑ in both",
        "LDH and S. haptoglobin are both ↑↑↑ in intravascular and ↓↓ in extravascular",
    ],
    "Summary table on p91: LDH is ↑↑↑ in Intravascular vs ↑↑ in Extravascular; S. haptoglobin is ↓↓↓ in Intravascular vs ↓↓ in Extravascular.")

add(S3, 91, "recall",
    "In the 'Summary of findings' table on p91, how do S. bilirubin and Splenomegaly compare between Intravascular and Extravascular hemolysis?",
    "S. bilirubin is ↑ in intravascular vs ↑↑ in extravascular; Splenomegaly is – in intravascular vs ↑↑ in extravascular",
    [
        "S. bilirubin is ↑↑ in intravascular vs ↑ in extravascular; Splenomegaly is ↑↑ in intravascular vs – in extravascular",
        "S. bilirubin is – in intravascular vs ↑↑ in extravascular; Splenomegaly is ↑↑ in both",
        "Both S. bilirubin and Splenomegaly are ↑↑↑ in intravascular and – in extravascular",
    ],
    "Summary table on p91: S. bilirubin is ↑ in Intravascular vs ↑↑ in Extravascular; Splenomegaly is – in Intravascular vs ↑↑ in Extravascular.")

add(S3, 91, "match",
    "Match each parameter in the p91 Summary of findings table to its comparison between Intravascular (IV) and Extravascular (EV) hemolysis — 1) LDH 2) S. haptoglobin 3) S. bilirubin 4) Splenomegaly … A) IV: ↓↓↓; EV: ↓↓ B) IV: –; EV: ↑↑ C) IV: ↑↑↑; EV: ↑↑ D) IV: ↑; EV: ↑↑",
    "1-C, 2-A, 3-D, 4-B",
    [
        "1-D, 2-A, 3-C, 4-B",
        "1-C, 2-B, 3-D, 4-A",
        "1-A, 2-C, 3-B, 4-D",
    ],
    "Summary of findings on p91: LDH is ↑↑↑ in IV vs ↑↑ in EV; S. haptoglobin is ↓↓↓ in IV vs ↓↓ in EV; S. bilirubin is ↑ in IV vs ↑↑ in EV; Splenomegaly is – in IV vs ↑↑ in EV.")

add(S3, 91, "recall",
    "According to Note 1 at the bottom of p91, all inherited causes of hemolytic anemia have an intracorpuscular defect EXCEPT:",
    "Atypical HUS",
    [
        "Paroxysmal nocturnal hemoglobinuria (PNH)",
        "G6PD deficiency",
        "Hereditary spherocytosis",
    ],
    "Note 1 on p91: All inherited causes have: • Intracorpuscular defect, except atypical HUS.")

add(S3, 91, "recall",
    "According to Note 1 at the bottom of p91, all inherited causes of hemolytic anemia have extravascular hemolysis EXCEPT:",
    "G6PD deficiency (acute form: intravascular hemolysis)",
    [
        "Thalassemia trait",
        "Hereditary elliptocytosis",
        "Pyruvate kinase deficiency",
    ],
    "Note 1 on p91: All inherited causes have: • Extra vascular hemolysis, except G6PD (Acute form : Intravascular hemolysis).")

add(S3, 91, "recall",
    "According to Note 2 at the bottom of p91, all acquired causes of hemolytic anemia have an extracorpuscular defect EXCEPT:",
    "Paroxysmal nocturnal hemoglobinuria (PNH)",
    [
        "Atypical HUS",
        "Warm antibody AIHA",
        "Cold antibody AIHA",
    ],
    "Note 2 on p91: All acquired causes have: • Extracorpuscular defect, except PNH.")

add(S3, 91, "truefalse",
    "TRUE or FALSE — according to Note 2 on p91, all acquired hemolytic anemias cause intravascular hemolysis EXCEPT warm and cold antibody AIHA (which cause extravascular hemolysis), whereas paroxysmal cold hemoglobinuria causes intravascular hemolysis.",
    "True — warm and cold AIHA cause extravascular hemolysis, while paroxysmal cold hemoglobinuria causes intravascular hemolysis",
    [
        "True — both warm AIHA and paroxysmal cold hemoglobinuria cause purely extravascular hemolysis",
        "False — all acquired hemolytic anemias cause extravascular hemolysis except warm AIHA",
        "False — cold AIHA and warm AIHA cause exclusively intravascular hemolysis",
    ],
    "Note 2 on p91: All acquired causes have intravascular hemolysis, except warm and cold Ab AIHA: (a) Warm and cold AIHA: Extravascular hemolysis; (b) Paroxysmal cold hemoglobinuria: Intravascular hemolysis.")


GUIDES = {
    S1: (
        "Classification of Hemolytic Anemia",
        "Hyperproliferative anemia (RPI >2.5, reticulocytosis) is classified as inherited vs acquired, intracorpuscular vs extracorpuscular, and intravascular vs extravascular.\n"
        "Inherited intracorpuscular causes include hemoglobinopathies (sickle cell, thalassemia), membrane defects (HS, elliptocytosis) and enzymopathies (G6PD, PK, 5'-nucleotidase); inherited extracorpuscular is atypical (familial) HUS.\n"
        "Acquired causes split into immune (AIHA: warm, cold, PCH; alloimmune: HDN, transfusion reaction; drug-induced) and non-immune (HUS/TTP fragmentation, intracorpuscular PNH, sepsis, toxins/drugs).",
    ),
    S2: (
        "Abbreviations & Intravascular Hemolysis",
        "PNH results from a PIGA gene mutation; intravascular hemolysis occurs inside blood vessels with ↑ LDH, hemoglobinemia, reticulocytosis and ↑ MCV.\n"
        "Free Hb binds haptoglobin, making ↓ serum haptoglobin the most sensitive and specific test for hemolysis; urine shows hemoglobinuria (acute, dark urine) or hemosiderinuria (chronic).\n"
        "Acute onset (m/c) causes are mismatched transfusion, sepsis, toxins and G6PD deficiency; chronic/acute-on-chronic causes are PNH, MAHA/HUS and PCH.",
    ),
    S3: (
        "Extravascular Hemolysis & General Rules",
        "Extravascular hemolysis occurs in the spleen with moderate splenomegaly; globin returns to the amino acid pool, iron raises stores/ferritin, and protoporphyrin becomes unconjugated bilirubin (↑ urine urobilinogen, ↑ fecal stercobilinogen).\n"
        "The summary table contrasts intravascular (plasma/urine Hb ++, urine hemosiderin ++, LDH ↑↑↑, haptoglobin ↓↓↓) with extravascular (tissue iron/ferritin ++, bilirubin ↑↑, splenomegaly ↑↑).\n"
        "Inherited causes are intracorpuscular (except atypical HUS) and extravascular (except acute G6PD); acquired causes are extracorpuscular (except PNH) and intravascular (except warm/cold AIHA; PCH is intravascular).",
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
