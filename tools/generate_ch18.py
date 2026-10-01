#!/usr/bin/env python3
"""Generate Chapter 18: Hemolytic Anemia : Miscellaneous (Book p103–106).

Every question is anchored to a specific line, diagram label, smear panel, or flowchart step
in uploads/01.pdf (PDF pages 115–118 = Book pages 103–106) in strict book order.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 18
TITLE = "Hemolytic Anemia : Miscellaneous"
PAGES = "103-106"

S1 = "Inherited Hemolytic Anemias & Hereditary Spherocytosis: Genetics and RBC Membrane Structure"
S2 = "Hereditary Spherocytosis: Pathogenesis, Clinical Features & Investigations"
S3 = "Hereditary Spherocytosis Treatment & G6PD Deficiency: Genetics, HMP Shunt and Triggers"
S4 = "G6PD Deficiency: Peripheral Smear, Diagnosis, Treatment & Anemia of Blood Loss"

RAW: list[tuple] = []


def add(sec: str, page: int, fmt: str, stem: str, correct: str, distractors: list[str], explanation: str) -> None:
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    rng = random.Random(18000 + CHAPTER * 10000 + len(RAW))
    rng.shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2, f"truefalse True count: {stem}"
        assert sum(o.startswith("False") for o in options) == 2, f"truefalse False count: {stem}"
    if fmt == "fillup":
        assert "______" in stem, f"fillup stem must contain ______: {stem}"
    if fmt == "match":
        assert " — 1)" in stem and " … A)" in stem, f"match stem must use ' — 1) ... … A) ...' grammar: {stem}"
    clean_exp = explanation.rstrip()
    if clean_exp.endswith(f"(Book p{page})"):
        final_exp = clean_exp
    else:
        final_exp = f"{clean_exp} (Book p{page})"
    RAW.append((sec, page, fmt, stem, options, options.index(correct), final_exp))


# ==============================================================================
# UNIT 1 — Page 103: Inherited Hemolytic Anemias & Hereditary Spherocytosis (Structure)
# ==============================================================================

add(
    S1,
    103,
    "match",
    "Match the category of inherited hemolytic anemia with its prototype disorder(s) — 1) Hemoglobinopathies 2) Membrane cytoskeleton disorders 3) Other RBC enzymopathies 4) Most common RBC enzymopathy … A) Hereditary spherocytosis B) G6PD deficiency C) Sickle cell anemia & thalassemia D) Pyruvate kinase & 5'-nucleotidase deficiency",
    "1-C, 2-A, 3-D, 4-B",
    [
        "1-A, 2-C, 3-B, 4-D",
        "1-C, 2-D, 3-A, 4-B",
        "1-B, 2-A, 3-C, 4-D",
    ],
    "Inherited hemolytic anemias are classified into hemoglobinopathies (sickle cell anemia, thalassemia), membrane cytoskeleton disorders (hereditary spherocytosis), and enzymopathies (G6PD deficiency [most common], pyruvate kinase deficiency, and 5'-nucleotidase deficiency).",
)

add(
    S1,
    103,
    "recall",
    "Which is the most common inherited red blood cell enzymopathy causing hemolytic anemia?",
    "Glucose-6-phosphate dehydrogenase (G6PD) deficiency",
    [
        "Pyruvate kinase deficiency",
        "5'-nucleotidase deficiency",
        "Hexokinase deficiency",
    ],
    "Under inherited hemolytic anemias, enzymopathies include G6PD deficiency (most common, m/c), pyruvate kinase deficiency, and 5'-nucleotidase deficiency.",
)

add(
    S1,
    103,
    "recall",
    "Which inherited red blood cell enzymopathy is specifically noted for producing prominent basophilic stippling on the peripheral blood smear?",
    "5'-nucleotidase deficiency",
    [
        "Glucose-6-phosphate dehydrogenase (G6PD) deficiency",
        "Pyruvate kinase deficiency",
        "Glutathione synthetase deficiency",
    ],
    "Basophilic stippling is characteristically seen in 5'-nucleotidase deficiency.",
)

add(
    S1,
    103,
    "oddoneout",
    "All of the following are listed as biochemical markers of cholestasis on page 103 EXCEPT:",
    "Pyruvate kinase",
    [
        "5'-nucleotidase",
        "Alkaline phosphatase",
        "Gamma-glutamyl transferase (GGT)",
    ],
    "The three listed markers of cholestasis are 5'-nucleotidase (printed as 5' nucleotidase deficiency), alkaline phosphatase, and gamma-glutamyl transferase.",
)

add(
    S1,
    103,
    "fillup",
    "Hereditary spherocytosis is characterized by chronic compensated ______ hemolysis.",
    "extravascular",
    [
        "intravascular",
        "complement-mediated",
        "microangiopathic",
    ],
    "Hereditary spherocytosis (HS) causes chronic compensated extravascular hemolysis.",
)

add(
    S1,
    103,
    "recall",
    "What is the most common mode of inheritance and underlying membrane protein defect in hereditary spherocytosis?",
    "Autosomal dominant inheritance; Ankyrin defect (more common than Band 3)",
    [
        "Autosomal recessive inheritance; β-spectrin defect (more common than Ankyrin)",
        "X-linked recessive inheritance; Glycophorin A defect",
        "Autosomal dominant inheritance; Band 4.1 defect (more common than Ankyrin)",
    ],
    "Hereditary spherocytosis is most commonly autosomal dominant, with ankyrin (ANK-1 gene) defects being more common than Band 3 defects (Ankyrin > Band 3).",
)

add(
    S1,
    103,
    "recall",
    "Autosomal recessive hereditary spherocytosis is classically caused by a defect in which RBC cytoskeleton protein?",
    "β-spectrin",
    [
        "Ankyrin (ANK-1)",
        "Band 3 anion exchanger",
        "Glycophorin C",
    ],
    "Autosomal recessive hereditary spherocytosis is associated with β-spectrin deficiency.",
)

add(
    S1,
    103,
    "recall",
    "What is the fundamental structural defect in the RBC membrane in hereditary spherocytosis?",
    "Defective pattern of the lipid bilayer between vertical and tangential associations",
    [
        "Failure of GPI-anchor synthesis due to somatic PIGA mutation",
        "Polymerization of deoxygenated hemoglobin S chains into rigid tactoids",
        "Inability to generate NADPH via the hexose monophosphate shunt",
    ],
    "The primary defect in hereditary spherocytosis is a defective pattern of the lipid bilayer between vertical and tangential associations.",
)

add(
    S1,
    103,
    "recall",
    "In the RBC membrane structure diagram, defects in Band 3 (an abundant integral membrane protein associated with HS) also cause which two red cell membrane disorders and confer protection against which parasite?",
    "Hereditary ovalocytosis and stomatocytosis; protective against Plasmodium falciparum",
    [
        "Hereditary elliptocytosis and pyropoikilocytosis; protective against Babesia microti",
        "Paroxysmal nocturnal hemoglobinuria and acanthocytosis; protective against Plasmodium vivax",
        "Southeast Asian xerocytosis and echinocytosis; protective against Leishmania donovani",
    ],
    "Band 3 is abundant in the RBC membrane, associated with hereditary spherocytosis, hereditary ovalocytosis, and stomatocytosis, and is protective against Plasmodium falciparum.",
)

add(
    S1,
    103,
    "recall",
    "According to the RBC membrane structure diagram, what is the primary physiological role of the spectrin dimer and which two clinical disorders result from its defect?",
    "Responsible for biconcavity of RBC (abundant in cytoskeleton); causes severe autosomal recessive HS in children/neonates and hereditary elliptocytosis",
    [
        "Acts as the primary anion channel in the lipid bilayer; causes hereditary ovalocytosis and stomatocytosis",
        "Serves as the extracellular sialoglycoprotein receptor; causes paroxysmal cold hemoglobinuria",
        "Catalyzes glutathione reduction in the cytosol; causes favism and neonatal kernicterus",
    ],
    "Spectrin dimer is abundant in the cytoskeleton and responsible for the biconcavity of the RBC; its defects cause severe autosomal recessive HS in children and neonates as well as hereditary elliptocytosis.",
)

add(
    S1,
    103,
    "recall",
    "Which gene is mutated in the most common autosomal dominant form of hereditary spherocytosis?",
    "ANK-1 gene (encoding Ankyrin)",
    [
        "SPTA1 gene (encoding α-spectrin)",
        "EPB42 gene (encoding Protein 4.2)",
        "PIGA gene (encoding phosphatidylinositol glycan class A)",
    ],
    "Mutation in the ANK-1 gene (autosomal dominant), which encodes ankyrin, is the most common cause of hereditary spherocytosis (m/c HS).",
)

add(
    S1,
    103,
    "recall",
    "In the RBC membrane cytoskeleton diagram on page 103, which accessory proteins are depicted at the junctional complexes on the cytoplasmic face of the lipid bilayer?",
    "Tropomyosin and Actin on one complex, and Band 4.1, Adducin, and Band 4.9 on the other",
    [
        "CD55 (DAF) and CD59 (MIRL) anchored via glycolipid tails",
        "Dystrophin, sarcoglycan, and syntrophin",
        "Clathrin, caveolin, and dynamin",
    ],
    "The RBC cytoskeleton diagram illustrates Ankyrin linking Band 3 to the spectrin dimer, with Tropomyosin and Actin at one junctional complex and Band 4.1, Adducin, and Band 4.9 at the other.",
)

add(
    S1,
    103,
    "fillup",
    "Plasmodium falciparum binds with ______ on the red blood cell surface, which is noted as the most abundant protein on the RBC membrane.",
    "glycophorin",
    [
        "ankyrin",
        "spectrin",
        "tropomyosin",
    ],
    "Plasmodium falciparum binds with glycophorin, noted at the bottom of page 103 as the most abundant protein on the RBC membrane.",
)

add(
    S1,
    103,
    "match",
    "Match the RBC membrane protein with its key attribute from the Structure of RBC diagram — 1) Band 3 2) Ankyrin 3) Spectrin dimer 4) Glycophorin … A) Cytoskeletal protein responsible for RBC biconcavity & elliptocytosis B) Integral protein associated with ovalocytosis & stomatocytosis C) Surface receptor bound by Plasmodium falciparum D) ANK-1 gene (AD) — most common cause of HS",
    "1-B, 2-D, 3-A, 4-C",
    [
        "1-D, 2-B, 3-C, 4-A",
        "1-A, 2-D, 3-B, 4-C",
        "1-B, 2-C, 3-A, 4-D",
    ],
    "Band 3 is associated with HS, ovalocytosis, and stomatocytosis; Ankyrin (ANK-1 gene, AD) is the most common defect in HS; Spectrin dimer maintains biconcavity and is defective in severe AR HS and hereditary elliptocytosis; Glycophorin is bound by P. falciparum.",
)

# ==============================================================================
# UNIT 2 — Page 104: Hereditary Spherocytosis Pathogenesis, Clinical Features & Investigations
# ==============================================================================

add(
    S2,
    104,
    "recall",
    "In the pathogenesis of hereditary spherocytosis, what immediate membrane event converts a biconcave red blood cell with a lipid bilayer defect into a sphere?",
    "Formation and detachment of microvesicles from the RBC membrane",
    [
        "Osmotic influx of sodium and water through leaky cation channels",
        "Fc-receptor-mediated partial phagocytosis by hepatic Kupffer cells",
        "Cross-linking of membrane sulfhydryl groups by precipitated Heinz bodies",
    ],
    "A defect in the lipid bilayer leads to microvesicle formation on the RBC membrane followed by detachment of the microvesicle from the membrane, causing the RBC to become spherical.",
)

add(
    S2,
    104,
    "fillup",
    "When a red blood cell loses membrane microvesicles and becomes spherical, a sphere has the ______ surface area to volume ratio.",
    "least",
    [
        "highest",
        "most deformable",
        "unchanged",
    ],
    "A sphere has the least surface area : volume ratio, which prevents degradation in the general circulation but prevents elongation in narrow splenic capillaries.",
)

add(
    S2,
    104,
    "numeric",
    "Why do spherocytes fail to traverse the splenic cords and undergo extravascular destruction by splenic macrophages?",
    "Normal RBC diameter is 7–8 μm whereas splenic capillaries measure only 3–4 μm, and spherical RBCs fail to elongate",
    [
        "Normal RBC diameter is 12–15 μm whereas splenic capillaries measure 8–10 μm",
        "Normal RBC diameter is 3–4 μm whereas splenic capillaries measure 7–8 μm",
        "Spherocytes polymerize at splenic pH < 6.8 and occlude 15–20 μm venules",
    ],
    "Because RBC diameter is 7–8 μm while splenic capillaries measure 3–4 μm, spherical RBCs fail to elongate and are destroyed by splenic macrophages (extravascular hemolysis).",
)

add(
    S2,
    104,
    "oddoneout",
    "All of the following are classic clinical features of hereditary spherocytosis listed on page 104 EXCEPT:",
    "Recurrent hemoglobinuria and pancytopenia with hepatic vein thrombosis",
    [
        "Anemia and intermittent jaundice",
        "Moderate splenomegaly and gallstones",
        "Aplastic crisis due to parvovirus B19",
    ],
    "Clinical features of hereditary spherocytosis are anemia, moderate splenomegaly, aplastic crisis due to parvovirus B19, gallstones, and intermittent jaundice.",
)

add(
    S2,
    104,
    "recall",
    "Which viral infection classically precipitates an acute aplastic crisis in patients with hereditary spherocytosis?",
    "Parvovirus B19",
    [
        "Epstein-Barr virus (EBV)",
        "Cytomegalovirus (CMV)",
        "Human herpesvirus-6 (HHV-6)",
    ],
    "Aplastic crisis in hereditary spherocytosis is caused by Parvovirus B19.",
)

add(
    S2,
    104,
    "scenario",
    "A 19-year-old patient presents with intermittent jaundice, moderate splenomegaly, and pigment gallstones on ultrasound. Peripheral blood smear demonstrates round red blood cells lacking central pallor (microspherocytes). What red blood cell index pattern is expected?",
    "Decreased MCV (↓) and markedly increased MCHC (↑↑)",
    [
        "Increased MCV (↑↑) and decreased MCHC (↓↓)",
        "Decreased MCV (↓) and markedly decreased MCHC (↓↓)",
        "Normal MCV and decreased MCHC (↓)",
    ],
    "In hereditary spherocytosis, peripheral smear shows microspherocytes (round with no pallor) and red cell indices characteristically show ↓ MCV and ↑↑ MCHC.",
)

add(
    S2,
    104,
    "recall",
    "In the diagnostic workup of hereditary spherocytosis, which investigation is listed as the MOST PREFERRED test and which is the GOLD STANDARD?",
    "Ektacytometry is most preferred; SDS-PAGE electrophoresis is the gold standard",
    [
        "Osmotic fragility test is most preferred; glycerol lysis (pink) test is the gold standard",
        "Eosin-5-maleimide (EMA) test is most preferred; osmotic fragility is the gold standard",
        "Direct Coombs test is most preferred; FLAER flow cytometry is the gold standard",
    ],
    "Under HS investigations on page 104: Ektacytometry is most preferred, and SDS-PAGE electrophoresis is the gold standard.",
)

add(
    S2,
    104,
    "match",
    "Match the diagnostic investigation in hereditary spherocytosis with its status or characteristic — 1) Ektacytometry 2) SDS-PAGE electrophoresis 3) Eosin-5-maleimide (EMA) binding test 4) Glycerol lysis / Pink test … A) Obsolete test B) Gold standard test C) Flow fluorescence test (less specific for ankyrin) D) Most preferred test",
    "1-D, 2-B, 3-C, 4-A",
    [
        "1-B, 2-D, 3-A, 4-C",
        "1-D, 2-C, 3-B, 4-A",
        "1-A, 2-B, 3-D, 4-C",
    ],
    "In HS investigations: Ektacytometry is most preferred, SDS-PAGE electrophoresis is the gold standard, Eosin-5-maleimide (EMA) test measures RBC fluorescence (less specific for ankyrin), osmotic fragility has low sensitivity/specificity and is not used, and the glycerol lysis/pink test is obsolete.",
)

add(
    S2,
    104,
    "recall",
    "In the Eosin-5-maleimide (EMA) test for hereditary spherocytosis, what is the principle and noted limitation?",
    "EMA binds with RBC membrane proteins to produce fluorescence; it is less specific for ankyrin defects",
    [
        "EMA precipitates unstable hemoglobin H inclusions; it is falsely negative in splenectomized patients",
        "EMA measures glucose-6-phosphate oxidation under UV light; it is falsely normal during acute reticulocytosis",
        "EMA chelates intracellular non-heme iron; it is only positive in hereditary elliptocytosis",
    ],
    "In the Eosin-5-maleimide (EMA) test, EMA binds with the RBC to produce fluorescence and is noted as less specific for ankyrin.",
)

add(
    S2,
    104,
    "numeric",
    "What saline concentrations and clinical utility are listed for the osmotic fragility test in hereditary spherocytosis on page 104?",
    "Printed principle lists (N) ≥ 0.7% saline and HS rupture at 0.3% (fragile RBCs); it has low sensitivity and specificity and is not used",
    [
        "Printed principle lists (N) 0.1% saline and HS rupture at 0.9% saline; it is the gold standard test with > 99% sensitivity and specificity",
        "Printed principle lists (N) 3.0% hypertonic saline and HS rupture at 1.8% saline; it is the most preferred first-line screening investigation",
        "Printed principle lists acidified serum lysis at pH 6.5 in 5% sucrose; it is more specific than SDS-PAGE electrophoresis for ankyrin defects",
    ],
    "The osmotic fragility test tests RBC rupture in hypotonic saline (printed on page 104 as '(N): Rupture of RBC in ≥ 0.7% saline; HS: Rupture at 0.3% → Fragile RBCs'); because it has low sensitivity and specificity, it is not used.",
)

add(
    S2,
    104,
    "truefalse",
    "Which of the following statements regarding diagnostic tests for hereditary spherocytosis is TRUE?",
    "True — Ektacytometry is the most preferred investigation, whereas SDS-PAGE electrophoresis is the gold standard",
    [
        "True — The osmotic fragility test has the highest sensitivity and specificity for hereditary spherocytosis",
        "False — Red blood cell indices in hereditary spherocytosis characteristically show elevated MCV and decreased MCHC",
        "False — The glycerol lysis (pink) test is the current first-line screening test for hereditary spherocytosis",
    ],
    "Ektacytometry is the most preferred test and SDS-PAGE electrophoresis is the gold standard; MCV is decreased with markedly increased MCHC (↑↑), osmotic fragility has low sensitivity/specificity and is not used, and the glycerol lysis (pink) test is obsolete.",
)

# ==============================================================================
# UNIT 3 — Page 105: HS Treatment & G6PD Deficiency (Genetics, HMP Shunt, Triggers)
# ==============================================================================

add(
    S3,
    105,
    "match",
    "Match the severity grade of hereditary spherocytosis with its typical clinical presentation and definitive management — 1) Mild disease 2) Moderate disease 3) Severe disease 4) Concomitant gallbladder rule … A) Cholecystectomy is done only if gallstones are positive B) Seen in adults; supportive care C) Anemia & gallstones; splenectomy at puberty D) Seen in children with jaundice & complications; splenectomy at 3–4 years",
    "1-B, 2-C, 3-D, 4-A",
    [
        "1-D, 2-B, 3-C, 4-A",
        "1-B, 2-D, 3-C, 4-A",
        "1-C, 2-B, 3-A, 4-D",
    ],
    "In HS treatment: mild disease (seen in adults) is managed with supportive care; moderate disease (anemia, gallstones) with splenectomy at puberty; severe disease (seen in children with jaundice and complications) with splenectomy at 3–4 years; and cholecystectomy is done only if gallstones are positive (+ve).",
)

add(
    S3,
    105,
    "management",
    "How is moderate hereditary spherocytosis (presenting with anemia and gallstones/cholelithiasis) managed surgically?",
    "Splenectomy at puberty (with cholecystectomy performed if gallstones are positive)",
    [
        "Supportive care alone with lifelong avoidance of splenectomy",
        "Emergency splenectomy in the neonatal period (< 6 months of age)",
        "Allogeneic hematopoietic stem cell transplantation in early childhood",
    ],
    "Moderate HS presents with anemia and gallstones (cholelithiasis) and is treated with splenectomy at puberty; mild HS (seen in adults) receives supportive care.",
)

add(
    S3,
    105,
    "management",
    "A child with severe hereditary spherocytosis has persistent jaundice and transfusion-dependent complications. At what age is splenectomy recommended, and what pre-operative and post-operative considerations apply?",
    "Splenectomy at 3–4 years of age; pre-operative vaccination is required, and post-operative risks include sepsis and thrombosis",
    [
        "Immediate splenectomy in the neonatal period (< 6 months); no vaccination needed until puberty",
        "Defer splenectomy until age 25 years; main post-operative risk is autoimmune warm hemolysis",
        "Perform prophylactic cholecystectomy without splenectomy at 1 year of age",
    ],
    "Severe HS in children (jaundice, complications) is treated with splenectomy at 3–4 years of age. Pre-operative vaccination is mandatory, and post-operative complications include the risk of sepsis and thrombosis.",
)

add(
    S3,
    105,
    "recall",
    "When performing splenectomy in a patient with hereditary spherocytosis, when is cholecystectomy indicated?",
    "Only if gallstones are positive (+ve)",
    [
        "Routinely in all patients undergoing splenectomy as prophylaxis",
        "Only if serum alkaline phosphatase exceeds 1,000 IU/L",
        "Never at the same sitting as splenectomy due to portal vein thrombosis risk",
    ],
    "As highlighted in the boxed note on page 105: Cholecystectomy is done only if gallstones are positive (+ve).",
)

add(
    S3,
    105,
    "recall",
    "What are the two major post-operative risks following splenectomy highlighted on page 105?",
    "Sepsis and thrombosis",
    [
        "Autoimmune thyroiditis and aplastic anemia",
        "Pigment nephropathy and fat embolism",
        "Secondary hemochromatosis and monoclonal gammopathy",
    ],
    "Under Splenectomy on page 105: Pre-operative requires vaccination, and post-operative carries the risk of sepsis and thrombosis.",
)

add(
    S3,
    105,
    "recall",
    "What is the mode of inheritance, specific variant class highlighted, and pattern of hemolysis in Glucose-6-Phosphate Dehydrogenase (G6PD) deficiency?",
    "X-linked intermediate inheritance; Class 2 Mediterranean type has ↓ G6PD; causes combined hemolysis with acute intravascular > chronic extravascular hemolysis",
    [
        "Autosomal dominant inheritance; Class 1 African type has ↑ G6PD activity; causes isolated chronic extravascular hemolysis in the hepatic sinusoids",
        "Autosomal recessive inheritance; Class 4 Asian type has absent Band 3 protein; causes isolated chronic extravascular hemolysis in the splenic cords",
        "Mitochondrial maternal inheritance; Class 3 Mediterranean type has ↑ NADPH; causes pure microangiopathic mechanical fragmentation hemolysis",
    ],
    "G6PD deficiency shows X-linked intermediate inheritance, Class 2 Mediterranean type has decreased (↓) G6PD activity, and hemolysis is combined (acute intravascular hemolysis > chronic extravascular hemolysis).",
)

add(
    S3,
    105,
    "fillup",
    "In the hexose monophosphate (HMP) shunt, G6PD converts glucose-6-phosphate into 6-phosphogluconolactone while generating ______, which maintains reduced glutathione to protect RBCs from oxidative injury.",
    "NADPH",
    [
        "NADH",
        "2,3-bisphosphoglycerate (2,3-BPG)",
        "FADH2",
    ],
    "In the HMP shunt: G6PD → 6-phosphogluconolactone → NADPH → Reduced glutathione → Protects RBCs from oxidative injury.",
)

add(
    S3,
    105,
    "recall",
    "Trace the exact sequence of the HMP shunt protective pathway depicted under G6PD Deficiency pathophysiology on page 105:",
    "G6PD → 6-Phosphogluconolactone → NADPH → Reduced glutathione → Protects RBCs from oxidative injury",
    [
        "G6PD → Pyruvate → NADH → Methemoglobin reductase → Protects RBCs from osmotic lysis",
        "G6PD → Fructose-1,6-bisphosphate → ATP → Na+/K+-ATPase → Maintains biconcavity",
        "G6PD → 2,3-BPG → Oxidized glutathione → Catalase → Prevents sickle polymerization",
    ],
    "The HMP shunt flowchart on page 105 shows: G6PD → 6 Phosphogluconolactone → NADPH → Reduced glutathione → Protects RBCs from oxidative injury.",
)

add(
    S3,
    105,
    "numeric",
    "Above what dose thresholds do aspirin and vitamin C precipitate oxidative hemolysis in patients with G6PD deficiency?",
    "High-dose aspirin > 3 g/dL (3 g/day) and high-dose vitamin C > 1 g",
    [
        "Low-dose aspirin > 75 mg and vitamin C > 60 mg",
        "Aspirin > 325 mg and vitamin C > 250 mg",
        "Aspirin > 10 g and vitamin C > 10 g",
    ],
    "The precipitating drugs list specifies high-dose aspirin (> 3 g/dL as printed) and high-dose vitamin C (> 1 g) alongside primaquine, dapsone, sulfamethoxazole (cotrimoxazole), nitrofurantoin, rasburicase, methylene blue, and chloroquine.",
)

add(
    S3,
    105,
    "oddoneout",
    "All of the following drugs and exposures are listed as precipitants of acute oxidative hemolysis in G6PD deficiency EXCEPT:",
    "Penicillin G",
    [
        "Primaquine, chloroquine, and dapsone",
        "Sulfamethoxazole (cotrimoxazole), nitrofurantoin, and rasburicase",
        "Methylene blue, fava beans, and acute infection",
    ],
    "Listed precipitants of G6PD hemolysis include primaquine, dapsone, sulfamethoxazole (cotrimoxazole), nitrofurantoin, rasburicase, high-dose aspirin (>3 g/dL), high-dose vitamin C (>1 g), methylene blue, chloroquine, infection, and fava beans.",
)

add(
    S3,
    105,
    "recall",
    "Why is methylene blue contraindicated in a patient with G6PD deficiency (for example, during treatment of dapsone- or rasburicase-induced methemoglobinemia)?",
    "Methylene blue requires NADPH from the HMP shunt and is itself a precipitating oxidant drug that worsens hemolysis in G6PD deficiency",
    [
        "Methylene blue irreversibly chelates mitochondrial iron in normoblasts and precipitates acute ringed sideroblastic arrest in the bone marrow",
        "Methylene blue induces warm IgG autoantibodies against Rh antigens that trigger fulminant Fc-receptor-mediated splenic sequestration",
        "Methylene blue inhibits hepatic ferrochelatase and delta-ALA dehydratase, precipitating acute neurovisceral porphyria and vasospasm",
    ],
    "Methylene blue and rasburicase are both explicitly listed among the drugs that precipitate acute oxidative hemolysis in G6PD deficiency.",
)

add(
    S3,
    105,
    "fillup",
    "In G6PD deficiency, the ______ state is protective against malaria.",
    "heterozygote",
    [
        "homozygous null",
        "splenectomized",
        "iron-overloaded",
    ],
    "As stated in the boxed note on page 105: Heterozygote is protective against malaria.",
)

# ==============================================================================
# UNIT 4 — Page 106: G6PD Smear, Diagnosis, Treatment & Anemia of Blood Loss
# ==============================================================================

add(
    S4,
    106,
    "recall",
    "In G6PD deficiency, what are Heinz bodies composed of, and what red cell morphologies result when splenic macrophages pit them out?",
    "Heinz bodies are precipitates of denatured globin inside the RBC; their removal produces blister cells (hemighosts), bite cells, and triangle cells",
    [
        "Heinz bodies are nuclear DNA remnants; hepatic Kupffer cells convert them into target cells",
        "Heinz bodies are iron-laden mitochondria; bone marrow macrophages convert them into acanthocytes",
        "Heinz bodies are precipitated ribosomal RNA aggregates; complement MAC converts them into spherocytes",
    ],
    "On the peripheral smear in G6PD deficiency, Heinz bodies represent precipitation of denatured globin inside the RBC; also illustrated on page 106 are blister cells (hemighosts), bite cells, triangle cells, and Howell-Jolly bodies.",
)

add(
    S4,
    106,
    "fillup",
    "On the peripheral blood smear in oxidative hemolysis, blister cells are also known as ______.",
    "hemighosts",
    [
        "drepanocytes",
        "dacrocytes",
        "codocytes",
    ],
    "Page 106 labels blister cells on the peripheral smear as Hemighosts ('Blister cells (Hemighosts)').",
)

add(
    S4,
    106,
    "match",
    "Match the peripheral blood smear red cell morphology depicted on page 106 with its description or disease association — 1) Heinz bodies 2) Blister cells 3) Helmet cells 4) Echinocytes … A) Also called hemighosts B) Classical of fragmented hemolysis C) Seen in CKD and pyruvate kinase deficiency D) Precipitation of denatured globin inside RBC",
    "1-D, 2-A, 3-B, 4-C",
    [
        "1-B, 2-D, 3-C, 4-A",
        "1-D, 2-C, 3-A, 4-B",
        "1-A, 2-D, 3-B, 4-C",
    ],
    "Page 106 illustrates: Howell-Jolly bodies, Heinz bodies (precipitation of denatured globin inside RBC), blister cells (hemighosts), bite cells, triangle cells, helmet cells (classical of fragmented hemolysis), echinocytes (in CKD and pyruvate kinase deficiency), and basophilic stippling (also seen in 5'-pyrimidine nucleotidase).",
)

add(
    S4,
    106,
    "recall",
    "Helmet cells on the peripheral blood smear panel on page 106 are highlighted as classical of which type of hemolysis?",
    "Fragmented hemolysis",
    [
        "Extravascular warm autoimmune hemolysis",
        "Hereditary stomatocytosis",
        "5'-pyrimidine nucleotidase deficiency",
    ],
    "Helmet cells are labeled on page 106 as 'Classical of fragmented hemolysis'.",
)

add(
    S4,
    106,
    "recall",
    "Echinocytes (burr cells with uniform short projections) shown on the peripheral smear panel on page 106 are characteristically associated with which two conditions?",
    "Chronic kidney disease (CKD) and pyruvate kinase deficiency",
    [
        "Abetalipoproteinemia and McLeod syndrome",
        "Hereditary spherocytosis and warm autoimmune hemolytic anemia",
        "Paroxysmal nocturnal hemoglobinuria and cold agglutinin disease",
    ],
    "The peripheral smear gallery on page 106 highlights echinocytes in chronic kidney disease (CKD) and pyruvate kinase deficiency.",
)

add(
    S4,
    106,
    "recall",
    "Which specific laboratory test is used as the screening test for G6PD deficiency, and how is the diagnosis confirmed?",
    "Fluorescent spot test for screening, followed by quantitative enzyme assay",
    [
        "Eosin-5-maleimide (EMA) binding test for screening, followed by SDS-PAGE electrophoresis",
        "Sucrose lysis test for screening, followed by FLAER flow cytometry",
        "Direct Coombs test for screening, followed by cold agglutinin titer",
    ],
    "Investigations for G6PD deficiency are: (1) peripheral smear, (2) fluorescent spot test (screening test), and (3) quantitative assay.",
)

add(
    S4,
    106,
    "management",
    "What is the primary treatment for a patient experiencing acute hemolysis due to G6PD deficiency?",
    "Stop the precipitating agent and provide symptomatic treatment",
    [
        "Emergency splenectomy and high-dose intravenous methylprednisolone",
        "Intravenous methylene blue and high-dose ascorbic acid (> 1 g/day)",
        "Terminal complement C5 inhibition with eculizumab",
    ],
    "Treatment of G6PD deficiency consists of stopping the precipitating agent and providing symptomatic Rx.",
)

add(
    S4,
    106,
    "match",
    "Match the sequential physiological stages and lethal triad of anemia due to acute blood loss — 1) Stage I 2) Stage II 3) Stage III 4) Lethal triad of hemorrhage … A) Increased EPO (↑) and increased reticulocytes (↑) B) Hypothermia, Acidosis, and DIC C) Hypovolemia D) Volume shift (extravascular → intravascular)",
    "1-C, 2-D, 3-A, 4-B",
    [
        "1-D, 2-C, 3-A, 4-B",
        "1-A, 2-D, 3-C, 4-B",
        "1-C, 2-A, 3-D, 4-B",
    ],
    "Blood loss stages are: Stage I — Hypovolemia; Stage II — Volume shift (extravascular → intravascular); Stage III — ↑ EPO and ↑ reticulocytes. The triangle diagram shows the triad of Hypothermia, Acidosis, and DIC.",
)

add(
    S4,
    106,
    "recall",
    "During Stage II of acute blood loss, what fluid compartment shift occurs?",
    "Volume shift from the extravascular space into the intravascular compartment",
    [
        "Volume shift from the intravascular compartment into the extravascular interstitial space",
        "Selective shift of red blood cells from the spleen into the portal vein",
        "Osmotic shift of intracellular water out of red blood cells into plasma",
    ],
    "In Stage I of blood loss there is hypovolemia; in Stage II, volume shift occurs from the extravascular to the intravascular compartment (Extravascular → Intravascular); in Stage III, EPO ↑ and reticulocytes ↑.",
)

add(
    S4,
    106,
    "recall",
    "What characterizes Stage III of the physiological response to blood loss anemia?",
    "Increased erythropoietin (EPO ↑) and increased reticulocyte count (reticulocyte ↑)",
    [
        "Acute hypovolemic shock with normal hemoglobin concentration",
        "Extravascular-to-intravascular interstitial fluid shift with falling hematocrit",
        "Suppression of erythropoietin with bone marrow erythroid hypoplasia",
    ],
    "Stage III of blood loss is characterized by ↑ EPO and ↑ reticulocytes.",
)

add(
    S4,
    106,
    "recall",
    "What are the three components of the triad illustrated at the bottom of page 106 under Blood Loss?",
    "Hypothermia, Acidosis, and DIC (printed with Hypercoagulability)",
    [
        "Hemolysis, Elevated liver enzymes, and Low platelets (HELLP)",
        "Hemoglobinuria, Pancytopenia, and Hepatic vein thrombosis",
        "Microangiopathic hemolytic anemia, Thrombocytopenia, and Acute kidney injury",
    ],
    "The triangle diagram at the bottom of page 106 shows the triad of Hypothermia, Acidosis, and DIC (printed as 'DIC (Hypercoagulability)').",
)

add(
    S4,
    106,
    "truefalse",
    "Which of the following statements regarding G6PD deficiency and blood loss anemia on page 106 is TRUE?",
    "True — The fluorescent spot test is used as the screening test for G6PD deficiency, and echinocytes are seen in CKD and pyruvate kinase deficiency",
    [
        "True — Helmet cells are pathognomonic of 5'-pyrimidine nucleotidase deficiency",
        "False — In Stage II of acute blood loss, fluid shifts from the intravascular compartment into the extravascular compartment",
        "False — Heinz bodies are composed of precipitated ribosomal RNA and are stained with Wright-Giemsa as basophilic stippling",
    ],
    "The fluorescent spot test is the screening test for G6PD deficiency, echinocytes are seen in CKD and pyruvate kinase deficiency, helmet cells are classical of fragmented hemolysis, Heinz bodies are denatured globin precipitates, and Stage II of blood loss involves an extravascular → intravascular volume shift.",
)


GUIDES = {
    S1: (
        "Inherited Hemolytic Anemias & Hereditary Spherocytosis: Genetics and RBC Membrane Structure",
        "Inherited hemolytic anemias classify into hemoglobinopathies (sickle cell, thalassemia), membrane cytoskeleton disorders (HS), and enzymopathies (G6PD most common, pyruvate kinase, 5'-nucleotidase).\n"
        "5'-nucleotidase deficiency shows basophilic stippling; cholestasis markers include 5'-nucleotidase, alkaline phosphatase, and GGT.\n"
        "Hereditary spherocytosis causes chronic compensated extravascular hemolysis from vertical/tangential membrane-cytoskeleton defects — AD (ankyrin ANK-1 > Band 3) more common than AR (β-spectrin).\n"
        "Band 3 (abundant in membrane; ovalocytosis/stomatocytosis; protects against P. falciparum), spectrin dimer (biconcavity, abundant in cytoskeleton; severe AR HS & hereditary elliptocytosis), and glycophorin (P. falciparum receptor).",
    ),
    S2: (
        "Hereditary Spherocytosis: Pathogenesis, Clinical Features & Investigations",
        "Lipid bilayer defect → membrane microvesicle formation and detachment → spherical RBCs with the least surface-area-to-volume ratio.\n"
        "7–8 μm spherocytes fail to elongate through 3–4 μm splenic capillaries and undergo extravascular destruction by splenic macrophages.\n"
        "Presents with anemia, moderate splenomegaly, parvovirus B19 aplastic crisis, gallstones, and intermittent jaundice; indices show decreased MCV and markedly elevated MCHC with microspherocytes lacking central pallor.\n"
        "Ektacytometry is most preferred, SDS-PAGE electrophoresis is the gold standard, EMA flow cytometry is less specific for ankyrin, osmotic fragility is not used, and glycerol lysis/pink test is obsolete.",
    ),
    S3: (
        "Hereditary Spherocytosis Treatment & G6PD Deficiency: Genetics, HMP Shunt and Triggers",
        "HS treatment by severity: mild (adults) gets supportive care; moderate (anemia, gallstones) gets splenectomy at puberty; severe (children with jaundice/complications) gets splenectomy at 3–4 years.\n"
        "Cholecystectomy is performed only if gallstones are positive; splenectomy requires pre-op vaccination and carries post-op risk of sepsis and thrombosis.\n"
        "G6PD deficiency is X-linked intermediate (Class 2 Mediterranean has decreased G6PD) and causes combined hemolysis with acute intravascular > chronic extravascular hemolysis.\n"
        "HMP shunt generates NADPH and reduced glutathione to protect RBCs from oxidative injury triggered by oxidant drugs (primaquine, dapsone, cotrimoxazole, nitrofurantoin, rasburicase, high-dose aspirin/vitamin C, methylene blue, chloroquine), infections, and fava beans.",
    ),
    S4: (
        "G6PD Deficiency: Peripheral Smear, Diagnosis, Treatment & Anemia of Blood Loss",
        "Peripheral smear morphology includes Heinz bodies (denatured globin precipitates), blister cells (hemighosts), bite cells, triangle cells, Howell-Jolly bodies, helmet cells, echinocytes (CKD, PK deficiency), and basophilic stippling (5'-pyrimidine nucleotidase).\n"
        "G6PD diagnosis uses the fluorescent spot test for screening and quantitative enzyme assay for confirmation; management is stopping the precipitating agent and symptomatic care.\n"
        "Anemia of blood loss progresses through Stage I (hypovolemia), Stage II (extravascular-to-intravascular volume shift), and Stage III (increased EPO and reticulocytes).\n"
        "The lethal triad in severe hemorrhage/blood loss comprises hypothermia, acidosis, and DIC.",
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
            {
                "chapter": CHAPTER,
                "title": TITLE,
                "pageRange": PAGES,
                "questions": questions,
                "units": units,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {out.name}: {len(questions)} questions / {len(units)} units")


if __name__ == "__main__":
    main()
