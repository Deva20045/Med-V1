#!/usr/bin/env python3
"""Generate Chapter 13 Approach To Microcytic Hypochromic Anemia (Book p77–81)."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 13
TITLE = "Approach To Microcytic Hypochromic Anemia"
PAGES = "77-81"

S1 = "Blood Picture & Anemia of Chronic Disease Pathophysiology"
S2 = "ACD Indices & Sideroblastic Anemia Etiology"
S3 = "Sideroblastic Pathogenesis & Thalassemia Trait Genetics"
S4 = "Thalassemia Investigations, Master Table & Inherited IDA"
S5 = "Diagnostic Protocol for Microcytic Hypochromic Anemia"

RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    rng = random.Random(13000 + CHAPTER * 10000 + len(RAW))
    rng.shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2, f"truefalse True count: {stem}"
        assert sum(o.startswith("False") for o in options) == 2, f"truefalse False count: {stem}"
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p77 — Opening blood-picture table & Anemia of Chronic Disease (ACD)
add(S1, 77, "recall",
    "In the opening blood-picture table on p77, what is the baseline blood picture of iron deficiency anemia?",
    "Normocytic normochromic",
    [
        "Dimorphic (microcytic and macrocytic)",
        "Macrocytic normochromic",
        "Leukoerythroblastic",
    ],
    "The p77 table lists the baseline blood picture of iron deficiency anemia as normocytic normochromic.")

add(S1, 77, "recall",
    "When does iron deficiency anemia show a microcytic hypochromic blood picture according to the p77 table?",
    "In severe anemia",
    [
        "In Stage I pre-latent negative iron balance",
        "Only when complicated by rheumatoid arthritis",
        "Before serum ferritin begins to fall",
    ],
    "Iron deficiency anemia is normocytic normochromic (microcytic hypochromic in severe anemia).")

add(S1, 77, "recall",
    "According to the p77 table, anemia of chronic disease typically presents with which blood picture?",
    "Normocytic normochromic",
    [
        "Dimorphic (microcytic, macrocytic)",
        "Macrocytic hypochromic",
        "Uniformly microcytic hypochromic in every etiology",
    ],
    "Anemia of chronic disease has a normocytic normochromic blood picture in most cases.")

add(S1, 77, "recall",
    "Which two exceptions in anemia of chronic disease are specifically noted to produce a microcytic hypochromic blood picture?",
    "Rheumatoid arthritis and miliary tuberculosis",
    [
        "Systemic lupus erythematosus and sarcoidosis",
        "Crohn's disease and infective endocarditis",
        "Chronic kidney disease and ulcerative colitis",
    ],
    "The p77 table notes that anemia of chronic disease is normocytic normochromic except in rheumatoid arthritis and miliary TB (microcytic hypochromic).")

add(S1, 77, "fillup",
    "The blood picture of sideroblastic anemia in the p77 comparison table is ____ (microcytic, macrocytic).",
    "Dimorphic",
    ["Normocytic", "Leukoerythroblastic", "Polychromatic"],
    "Sideroblastic anemia is listed with a dimorphic (microcytic, macrocytic) blood picture.")

add(S1, 77, "recall",
    "In the opening table, the blood picture of thalassemia trait (minor) is:",
    "Microcytic hypochromic",
    [
        "Normocytic normochromic",
        "Dimorphic (microcytic, macrocytic)",
        "Macrocytic normochromic",
    ],
    "Thalassemia trait (minor) is listed as microcytic hypochromic.")

add(S1, 77, "match",
    "Match each anemia to its characteristic blood picture in the opening table — 1) Iron deficiency anemia 2) Anemia of chronic disease 3) Sideroblastic anemia 4) Thalassemia trait (minor) … A) Dimorphic (microcytic, macrocytic) B) Microcytic hypochromic C) Normocytic normochromic (microcytic hypochromic in severe anemia) D) Normocytic normochromic except in rheumatoid arthritis and miliary TB",
    "1-C, 2-D, 3-A, 4-B",
    [
        "1-B, 2-C, 3-D, 4-A",
        "1-C, 2-A, 3-D, 4-B",
        "1-D, 2-C, 3-B, 4-A",
    ],
    "IDA is normocytic normochromic (microcytic hypochromic in severe anemia); ACD is normocytic normochromic except RA and miliary TB; sideroblastic anemia is dimorphic; thalassemia trait is microcytic hypochromic.")

add(S1, 77, "recall",
    "Chemically, hepcidin is classified in the pathophysiology section as a:",
    "Peptide hormone",
    [
        "Steroid hormone",
        "Catecholamine derivative",
        "Eicosanoid lipid mediator",
    ],
    "Hepcidin is described as a peptide hormone.")

add(S1, 77, "fillup",
    "Hepcidin is a peptide hormone produced in the ____.",
    "Liver",
    ["Kidney", "Spleen", "Bone marrow"],
    "Hepcidin is produced in the liver.")

add(S1, 77, "recall",
    "In normal physiology on p77, stimulation of hepcidin acts directly on which transporter?",
    "Ferroportin",
    [
        "Divalent metal transporter-1 (DMT-1)",
        "Heme carrier protein-1 (HCP-1)",
        "Transferrin receptor-1 (TfR1)",
    ],
    "Physiology: Stimulation of hepcidin → Regulates ferroportin.")

add(S1, 77, "recall",
    "When hepcidin regulates ferroportin in normal physiology, what is the downstream effect on iron?",
    "Decreased release of Fe²⁺ into circulation",
    [
        "Increased export of Fe³⁺ from duodenal enterocytes into plasma",
        "Enhanced oxidation of Fe²⁺ to Fe³⁺ at the brush border",
        "Direct uptake of transferrin-bound iron into erythroblasts",
    ],
    "Physiology: Stimulation of hepcidin → Regulates ferroportin → ↓ release of Fe2+ into circulation.")

add(S1, 77, "fillup",
    "In the pathology of anemia of chronic disease, marked inflammation causes increased release of ____.",
    "IL-6 and activin",
    ["IL-1 and TNF-beta", "IL-4 and IL-13", "EPO and hephaestin"],
    "Pathology flowchart: ↑↑ Inflammation → ↑↑ release of IL-6, activin.")

add(S1, 77, "recall",
    "In the ACD pathology cascade, increased release of IL-6 and activin leads to increased stimulation of hepcidin synthesis, which then acts to:",
    "Inhibit ferroportin",
    [
        "Activate divalent metal transporter-1 (DMT-1)",
        "Stimulate duodenal cytochrome b reductase",
        "Upregulate transferrin receptor-1 on normoblasts",
    ],
    "↑↑ release of IL-6, activin → ↑↑ stimulation of hepcidin synthesis → Inhibit ferroportin.")

add(S1, 77, "recall",
    "When ferroportin is inhibited in anemia of chronic disease, iron becomes trapped in which three storage sites?",
    "Duodenal cells, liver and spleen",
    [
        "Renal cortex, bone matrix and skeletal muscle",
        "Gastric parietal cells, pancreas and thyroid",
        "Circulating reticulocytes, plasma and lymph nodes",
    ],
    "Inhibit ferroportin → Iron trapped in the stores (Duodenal cells, liver, spleen).")

add(S1, 77, "scenario",
    "A patient with chronic inflammatory disease has high IL-6 and activin levels that stimulate hepatic hepcidin and trap iron inside duodenal cells, liver, and spleen. What is the resulting final state in the p77 pathology flowchart?",
    "Deficient iron in circulation",
    [
        "Systemic iron overload with saturated plasma transferrin",
        "Excessive unbound ferrous iron in the portal vein",
        "Increased release of iron from macrophages into plasma",
    ],
    "The pathology cascade ends with iron trapped in stores (duodenal cells, liver, spleen) → Deficient iron in circulation.")

add(S1, 77, "recall",
    "How does hypoxia regulate hepcidin and intestinal iron absorption on p77?",
    "Hypoxia inhibits hepcidin → no regulation of ferroportin → increased iron absorption",
    [
        "Hypoxia stimulates hepcidin → degrades ferroportin → decreased iron absorption",
        "Hypoxia inhibits ferroportin directly → traps iron in enterocytes → decreased iron absorption",
        "Hypoxia stimulates HFE and Tfr2 → increases hepcidin → prevents iron overload",
    ],
    "Factors regulating hepcidin: Hypoxia → inhibits hepcidin → no regulation of ferroportin → ↑ iron absorption.")

add(S1, 77, "numeric",
    "The HFE gene that regulates hepcidin is located on which chromosome?",
    "Chromosome 6",
    ["Chromosome 11", "Chromosome 16", "Chromosome 22"],
    "The p77 note specifies HFE gene (chromosome 6).")

add(S1, 77, "recall",
    "How do the HFE gene (chromosome 6), hemojuvelin, and Tfr2 regulate hepcidin and iron balance?",
    "They stimulate hepcidin → decreased iron absorption → prevent iron overload",
    [
        "They inhibit hepcidin → increased iron absorption → promote erythropoiesis",
        "They degrade ferroportin directly → increased iron excretion in bile",
        "They block transferrin binding → increased urinary iron clearance",
    ],
    "HFE gene (chromosome 6), hemojuvelin, Tfr2 → stimulates hepcidin → ↓ iron absorption → Prevent iron overload.")

# ---------------------------------------------------------------------------
# Book p78 — Note, ACD Blood Indices, Sideroblastic Anemia Causes & Hb Physiology
add(S2, 78, "fillup",
    "According to the note at the top of p78, an HFE gene mutation leads to ____.",
    "Hemochromatosis",
    ["Sideroblastic anemia", "Atransferrinemia", "Thalassemia minor"],
    "Note on p78: HFE gene mutation → Hemochromatosis.")

add(S2, 78, "recall",
    "Besides regulating duodenal absorption, hepcidin is noted on p78 to play a role in recycling iron from which three cell types?",
    "Macrophages, enterocytes and hepatocytes",
    [
        "Erythroblasts, platelets and megakaryocytes",
        "Neutrophils, lymphocytes and plasma cells",
        "Podocytes, renal tubular cells and astrocytes",
    ],
    "Note on p78: Hepcidin also plays a role in recycling iron from macrophages, enterocytes & hepatocytes.")

add(S2, 78, "recall",
    "In the blood indices for anemia of chronic disease (p78), serum ferritin is:",
    "Normal or high",
    [
        "Very low",
        "Always absent",
        "Decreased in proportion to hemoglobin",
    ],
    "Blood indices in ACD: Sr. Ferritin : Normal / high.")

add(S2, 78, "recall",
    "In the blood indices for anemia of chronic disease (p78), serum iron is:",
    "Very low",
    [
        "Normal or high",
        "Moderately increased",
        "Unchanged from baseline",
    ],
    "Blood indices in ACD: Sr. Iron : Very low.")

add(S2, 78, "recall",
    "In the blood indices for anemia of chronic disease (p78), Total Iron Binding Capacity (TIBC) is:",
    "Low",
    [
        "High",
        "Markedly elevated",
        "Normal in all cases",
    ],
    "Blood indices in ACD: TIBC (Total iron binding capacity) : Low.")

add(S2, 78, "recall",
    "Why is TIBC low in anemia of chronic disease according to the parenthetical note on p78?",
    "Iron stores are adequate, leading to less transferrin synthesis",
    [
        "Transferrin is rapidly lost through glomerular filtration",
        "Depleted marrow stores trigger compensatory transferrin degradation",
        "Unbound protoporphyrin directly chelates circulating transferrin",
    ],
    "TIBC is Low (Store adequate → less transferrin synthesis).")

add(S2, 78, "recall",
    "Which formula is printed beneath Transferrin saturation in the blood indices list on p78?",
    "(Sr. iron ÷ TIBC) × 100",
    [
        "(TIBC ÷ Sr. iron) × 100",
        "(Sr. ferritin ÷ TIBC) × 100",
        "(Sr. iron ÷ Sr. ferritin) × 100",
    ],
    "Transferrin saturation formula on p78: (Sr. iron / TIBC) × 100.")

add(S2, 78, "recall",
    "What is the level of transferrin saturation in anemia of chronic disease on p78?",
    "Low",
    [
        "High",
        "Normal",
        "Above 50%",
    ],
    "Transferrin saturation : Low in anemia of chronic disease.")

add(S2, 78, "recall",
    "In the blood indices for anemia of chronic disease on p78, soluble transferrin receptors are:",
    "Low",
    [
        "High",
        "Markedly elevated",
        "The earliest rising marker",
    ],
    "Soluble transferrin receptors : Low in anemia of chronic disease.")

add(S2, 78, "recall",
    "In the blood indices for anemia of chronic disease on p78, serum hepcidin is:",
    "High",
    [
        "Low",
        "Absent",
        "Suppressed by IL-6",
    ],
    "Hepcidin : High in anemia of chronic disease.")

add(S2, 78, "match",
    "Match each blood index in anemia of chronic disease to its printed level — 1) Serum ferritin 2) Serum iron 3) Soluble transferrin receptors 4) Hepcidin … A) Very low B) Low C) High D) Normal / high",
    "1-D, 2-A, 3-B, 4-C",
    [
        "1-A, 2-D, 3-C, 4-B",
        "1-D, 2-B, 3-A, 4-C",
        "1-C, 2-A, 3-B, 4-D",
    ],
    "In ACD: Sr. ferritin is normal/high, Sr. iron is very low, soluble transferrin receptors are low, and hepcidin is high.")

add(S2, 78, "recall",
    "Under Sideroblastic Anemia on p78, causes are classified based on etiology into which two main groups?",
    "Inherited and acquired",
    [
        "Immune and non-immune",
        "Intravascular and extravascular",
        "Megaloblastic and normoblastic",
    ],
    "Causes of sideroblastic anemia — Based on etiology: Inherited and Acquired.")

add(S2, 78, "fillup",
    "The inherited cause of sideroblastic anemia listed on p78 is ____ deficiency.",
    "ALA synthase",
    ["Ferrochelatase", "Uroporphyrinogen decarboxylase", "Glucose-6-phosphate dehydrogenase"],
    "Inherited: ALA synthase deficiency (X-linked).")

add(S2, 78, "recall",
    "What is the mode of inheritance printed for ALA synthase deficiency on p78?",
    "X-linked",
    [
        "Autosomal dominant",
        "Autosomal recessive",
        "Mitochondrial maternal",
    ],
    "Inherited: ALA synthase deficiency (X-linked).")

add(S2, 78, "recall",
    "Which clonal bone-marrow disorder is listed first under acquired causes of sideroblastic anemia on p78?",
    "Myelodysplastic syndrome",
    [
        "Polycythemia vera",
        "Hairy-cell leukemia",
        "Chronic myeloid leukemia",
    ],
    "Acquired causes of sideroblastic anemia: first bullet is myelodysplastic syndrome.")

add(S2, 78, "fillup",
    "Which trace-element deficiency is listed under acquired causes of sideroblastic anemia on p78? ____ deficiency.",
    "Copper",
    ["Selenium", "Manganese", "Cobalt"],
    "Acquired causes of sideroblastic anemia include Copper deficiency.")

add(S2, 78, "recall",
    "Which toxin/substance-use disorder is listed as the third bullet under acquired causes of sideroblastic anemia on p78?",
    "Alcoholism",
    [
        "Tobacco smoking",
        "Opioid dependence",
        "Cannabis use",
    ],
    "Acquired causes of sideroblastic anemia: myelodysplastic syndrome, copper deficiency, alcoholism.")

add(S2, 78, "recall",
    "Which three drugs are specifically listed under acquired causes of sideroblastic anemia on p78?",
    "Chloramphenicol, isoniazid and pyrazinamide",
    [
        "Rifampicin, ethambutol and streptomycin",
        "Methotrexate, cytarabine and hydroxyurea",
        "Phenytoin, carbamazepine and valproate",
    ],
    "Drugs listed under acquired sideroblastic anemia are chloramphenicol, isoniazid, and pyrazinamide.")

add(S2, 78, "recall",
    "Which heavy metal is listed at the bottom of the acquired causes of sideroblastic anemia on p78?",
    "Lead",
    ["Arsenic", "Mercury", "Cadmium"],
    "Lead is listed as the fifth bullet under acquired causes of sideroblastic anemia.")

add(S2, 78, "oddoneout",
    "Pick the ODD ONE OUT — which of the following is NOT listed among the acquired causes of sideroblastic anemia on p78?",
    "Hydroxyurea",
    [
        "Myelodysplastic syndrome",
        "Copper deficiency",
        "Chloramphenicol",
    ],
    "Acquired causes on p78 are myelodysplastic syndrome, copper deficiency, alcoholism, drugs (chloramphenicol, isoniazid, pyrazinamide), and lead. Hydroxyurea is a DNA synthesis inhibitor causing megaloblastic anemia.")

add(S2, 78, "recall",
    "In the physiology of hemoglobin formation on p78, which two substrates and cofactor combine in the initial step?",
    "Succinyl Co-A + Glycine + Pyridoxal phosphate",
    [
        "Acetyl Co-A + Alanine + Thiamine pyrophosphate",
        "Malonyl Co-A + Glutamine + Methylcobalamin",
        "Propionyl Co-A + Serine + Tetrahydrofolate",
    ],
    "Physiology of Hb formation: Succinyl Co-A + Glycine + Pyridoxal phosphate.")

add(S2, 78, "fillup",
    "In the physiology of Hb formation diagram on p78, Succinyl Co-A + Glycine + Pyridoxal phosphate are converted into ALA by the enzyme ____.",
    "ALA synthase",
    ["ALA dehydratase", "Ferrochelatase", "Heme oxygenase"],
    "Succinyl Co-A + Glycine + Pyridoxal phosphate → (via ALA synthase) → ALA.")

add(S2, 78, "recall",
    "In the p78 hemoglobin formation pathway, ALA is converted to which intermediate before combining with iron?",
    "Protoporphyrin",
    [
        "Biliverdin",
        "Urobilinogen",
        "Transferrin",
    ],
    "ALA → Protoporphyrin, which then combines with Iron to form Heme → Hemoglobin.")

add(S2, 78, "recall",
    "In the final steps of the p78 pathway, Iron combines with Protoporphyrin to form:",
    "Heme, which then forms Hemoglobin",
    [
        "Ferritin, which then forms Hemosiderin",
        "ALA, which then forms Globin",
        "Hepcidin, which then forms Transferrin",
    ],
    "Protoporphyrin + Iron → Heme → Hemoglobin.")

# ---------------------------------------------------------------------------
# Book p79 — Pathogenesis & Investigations of Sideroblastic Anemia; Thalassemia Trait
add(S3, 79, "recall",
    "At the top of p79, what initiates the pathogenesis flowchart of sideroblastic anemia?",
    "ALA synthase deficiency",
    [
        "Spectrin and ankyrin deficiency",
        "Glucose-6-phosphate dehydrogenase deficiency",
        "Autoimmune anti-parietal cell antibodies",
    ],
    "Pathogenesis of sideroblastic anemia begins with: ALA synthase deficiency.")

add(S3, 79, "recall",
    "In the pathogenesis of sideroblastic anemia on p79, what is the immediate consequence of ALA synthase deficiency?",
    "Protoporphyrin is absent, leaving unbound iron",
    [
        "Excess protoporphyrin accumulates with depleted intracellular iron",
        "Globin chains precipitate inside the endoplasmic reticulum",
        "Ferroportin is constitutively activated, exporting iron from erythroblasts",
    ],
    "ALA synthase deficiency → Protoporphyrin absent, unbound iron.")

add(S3, 79, "recall",
    "In sideroblastic anemia, how does unbound iron distribute inside the developing red-cell precursor?",
    "Iron surrounds the erythroblast in the form of a ring",
    [
        "Iron precipitates at one pole of the mature erythrocyte as a Heinz body",
        "Iron polymerizes into linear crystalline rods inside myeloblasts",
        "Iron is extruded into plasma bound to haptocorrin",
    ],
    "Protoporphyrin absent, unbound iron → Iron surrounds erythroblast in the form of ring.")

add(S3, 79, "fillup",
    "Iron surrounding the erythroblast in the form of a ring produces ____ in Prussian blue stain, leading to sideroblastic anemia.",
    "Ring sideroblasts",
    ["Howell-Jolly bodies", "Cabot rings", "Target cells"],
    "Iron surrounds erythroblast in the form of ring → Ring sideroblasts in Prussian blue stain → Sideroblastic anemia.")

add(S3, 79, "recall",
    "Which stain is used to demonstrate ring sideroblasts in the two bone-marrow photomicrographs on p79?",
    "Prussian blue stain",
    [
        "Supravital new methylene blue stain",
        "Periodic acid–Schiff (PAS) stain",
        "Romanowsky stain without iron reagent",
    ],
    "Ring sideroblasts in Prussian blue stain are illustrated in the p79 bone marrow images.")

add(S3, 79, "recall",
    "Under investigations for sideroblastic anemia on p79, how is cellularity described?",
    "Dimorphic (microcytic + macrocytic)",
    [
        "Uniformly microcytic and hypochromic",
        "Purely macro-ovalocytic with hypersegmented neutrophils",
        "Normocytic normochromic with spherocytes",
    ],
    "Investigations: Cellularity : Dimorphic (microcytic + macrocytic).")

add(S3, 79, "fillup",
    "Under investigations for sideroblastic anemia on p79, electron microscopy shows ____.",
    "Pappenheimer bodies",
    ["Cabot rings", "Schuffner's dots", "Auer rods"],
    "Electronmicroscopy : Pappenheimer bodies.")

add(S3, 79, "recall",
    "In the blood indices for sideroblastic anemia on p79, serum ferritin is:",
    "Normal or high",
    [
        "Very low",
        "Always absent",
        "Decreased below 15 ng/mL",
    ],
    "Blood indices in sideroblastic anemia: Sr. ferritin : Normal/high.")

add(S3, 79, "recall",
    "In the blood indices for sideroblastic anemia on p79, serum iron is:",
    "High",
    [
        "Very low",
        "Decreased",
        "Zero",
    ],
    "Blood indices in sideroblastic anemia: Sr. iron : High.")

add(S3, 79, "recall",
    "Why is serum iron high in sideroblastic anemia according to the parenthetical mechanism on p79?",
    "Due to ineffective erythropoiesis leading to a compensatory increase in iron absorption",
    [
        "Due to excessive hepcidin release accelerating macrophage iron export",
        "Due to intravascular hemolysis releasing free hemoglobin into plasma",
        "Due to defective renal excretion preventing urinary iron clearance",
    ],
    "(D/t ineffective erythropoiesis → Compensatory ↑ in iron absorption).")

add(S3, 79, "recall",
    "In the blood indices for sideroblastic anemia on p79, TIBC and transferrin saturation are respectively:",
    "TIBC is low; transferrin saturation is high",
    [
        "TIBC is high; transferrin saturation is low",
        "Both TIBC and transferrin saturation are low",
        "Both TIBC and transferrin saturation are normal",
    ],
    "In sideroblastic anemia blood indices: TIBC : Low; Transferrin saturation : High.")

add(S3, 79, "match",
    "Match each blood index in sideroblastic anemia to its printed value — 1) Serum ferritin 2) Serum iron 3) TIBC 4) Transferrin saturation … A) Low B) High (due to compensatory increased absorption) C) Normal / high D) High",
    "1-C, 2-B, 3-A, 4-D",
    [
        "1-A, 2-C, 3-B, 4-D",
        "1-C, 2-A, 3-D, 4-B",
        "1-B, 2-D, 3-A, 4-C",
    ],
    "In sideroblastic anemia: Sr. ferritin is Normal/high, Sr. iron is High (due to ineffective erythropoiesis → compensatory ↑ in iron absorption), TIBC is Low, and Transferrin saturation is High.")

add(S3, 79, "recall",
    "In the Thalassemia Trait (Minor) table on p79, what level of β-chain synthesis corresponds to the β⁰ allele?",
    "Nil",
    ["Normal", "Reduced", "Increased"],
    "Gene table on p79: β⁰ → Nil β synthesis.")

add(S3, 79, "recall",
    "In the Thalassemia Trait (Minor) table on p79, what level of β-chain synthesis corresponds to the β and β⁺ alleles respectively?",
    "β: Normal synthesis; β⁺: Reduced synthesis",
    [
        "β: Reduced synthesis; β⁺: Nil synthesis",
        "β: Nil synthesis; β⁺: Normal synthesis",
        "β: Increased synthesis; β⁺: Normal synthesis",
    ],
    "Gene table on p79: β → Normal; β⁺ → Reduced.")

add(S3, 79, "match",
    "Match each β-globin gene notation in the Thalassemia Trait table to its β-chain synthesis — 1) β⁰ 2) β 3) β⁺ … A) Normal B) Reduced C) Nil",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-A, 3-C",
        "1-C, 2-B, 3-A",
    ],
    "Gene table on p79: β⁰ = Nil synthesis; β = Normal synthesis; β⁺ = Reduced synthesis.")

add(S3, 79, "recall",
    "Which genotypes are shown for thalassemia trait on p79, representing one normal β chain and one defective β chain?",
    "ββ⁰ and ββ⁺",
    [
        "β⁰β⁰ and β⁺β⁺",
        "β⁰β⁺ and αα/−−",
        "ββ and β⁰β⁰",
    ],
    "Thalassemia trait: ββ⁰, ββ⁺ → One normal β chain + One defective β chain.")

add(S3, 79, "truefalse",
    "TRUE or FALSE — in thalassemia trait on p79, ineffective erythropoiesis is absent, resulting in normal iron indices plus microcytic hypochromic anemia.",
    "True — absent ineffective erythropoiesis gives normal iron indices with microcytic hypochromic anemia",
    [
        "True — but serum ferritin and transferrin saturation are markedly elevated",
        "False — severe ineffective erythropoiesis causes iron overload in thalassemia trait",
        "False — thalassemia trait presents with normocytic anemia and low serum iron",
    ],
    "The p79 diagram states: Absent ineffective erythropoiesis → Normal iron indices + microcytic hypochromic anemia.")

# ---------------------------------------------------------------------------
# Book p80 — Thalassemia Trait Investigations, Master Table & Inherited IDA
add(S4, 80, "recall",
    "Under blood indices for thalassemia trait on p80, what is the Red Cell Distribution Width (RDW)?",
    "Normal",
    [
        "Markedly increased (>14.5%)",
        "Decreased (<8%)",
        "Bimodal",
    ],
    "Blood indices in thalassemia trait: RDW (Red cell distribution width) : Normal.")

add(S4, 80, "numeric",
    "What is the Mentzer index cutoff listed under blood indices for thalassemia trait on p80?",
    "<13",
    [">13", "<10", ">20"],
    "Blood indices in thalassemia trait: Mentzer index : <13.")

add(S4, 80, "recall",
    "Under blood indices for thalassemia trait on p80, what is the status of 'Other indices'?",
    "Normal",
    [
        "Increased TIBC and decreased ferritin",
        "Decreased serum iron and low TSAT",
        "Increased serum iron and low TIBC",
    ],
    "Blood indices in thalassemia trait: Other indices : Normal.")

add(S4, 80, "recall",
    "What is the first peripheral smear finding listed for thalassemia trait on p80?",
    "Anisopoikilocytosis",
    [
        "Macro-ovalocytosis",
        "Hypersegmented neutrophils",
        "Ring sideroblasts",
    ],
    "Peripheral smear in thalassemia trait: first bullet is Anisopoikilocytosis.")

add(S4, 80, "recall",
    "Which two peripheral smear findings in thalassemia trait are bracketed together as 'Rare' on p80?",
    "Few target cells and stippled red cells",
    [
        "Tear-drop cells and pencil cells",
        "Howell-Jolly bodies and Cabot rings",
        "Spherocytes and schistocytes",
    ],
    "Peripheral smear on p80 brackets Few target cells and Stippled red cells as Rare.")

add(S4, 80, "numeric",
    "On hemoglobin electrophoresis (p80), what is the normal HbA₂ level range?",
    "1.5–3%",
    ["0.5–1.5%", "4–8%", "8–12%"],
    "Electrophoresis HbA2 levels: Normal : 1.5–3%.")

add(S4, 80, "numeric",
    "On hemoglobin electrophoresis (p80), what is the HbA₂ level range in thalassemia trait?",
    "4–8%",
    ["1.5–3%", "10–15%", "20–30%"],
    "Electrophoresis HbA2 levels: Thalassemia : 4–8%.")

add(S4, 80, "recall",
    "In the p80 master comparison table, what is the Serum Iron (Sr. iron) pattern across Iron deficiency anemia, Anemia of chronic disease, Sideroblastic anemia, and Thalassemia trait?",
    "IDA: ↓; ACD: ↓↓; Sideroblastic anemia: ↑; Thalassemia trait: Ⓝ",
    [
        "IDA: ↓↓; ACD: ↓; Sideroblastic anemia: Ⓝ; Thalassemia trait: ↑",
        "IDA: ↓; ACD: ↑; Sideroblastic anemia: ↓↓; Thalassemia trait: Ⓝ",
        "IDA: Ⓝ; ACD: ↓↓; Sideroblastic anemia: ↑; Thalassemia trait: ↓",
    ],
    "Sr. iron row on p80: IDA ↓, ACD ↓↓, Sideroblastic anemia ↑, Thalassemia trait Ⓝ.")

add(S4, 80, "recall",
    "In the p80 master table, how is the Serum Ferritin row populated across Iron deficiency anemia, Anemia of chronic disease, Sideroblastic anemia, and Thalassemia trait?",
    "IDA: ↓ / Ⓝ / ↑; ACD: Ⓝ / ↑; Sideroblastic anemia: Ⓝ / ↑; Thalassemia trait: Ⓝ",
    [
        "IDA: ↓; ACD: ↓; Sideroblastic anemia: ↑↑; Thalassemia trait: ↑",
        "IDA: Ⓝ; ACD: ↓↓; Sideroblastic anemia: ↓; Thalassemia trait: Ⓝ / ↑",
        "IDA: ↓ / Ⓝ / ↑; ACD: ↓; Sideroblastic anemia: ↓; Thalassemia trait: ↑",
    ],
    "The Sr. ferritin row on p80 shows: IDA ↓/Ⓝ/↑, ACD Ⓝ/↑, Sideroblastic anemia Ⓝ/↑, and Thalassemia trait Ⓝ.")

add(S4, 80, "recall",
    "Across the four columns of the p80 master table, TIBC is:",
    "Increased (↑) in IDA, decreased (↓) in ACD and sideroblastic anemia, and normal (Ⓝ) in thalassemia trait",
    [
        "Increased (↑) in both IDA and ACD, and decreased (↓) in sideroblastic anemia and thalassemia trait",
        "Decreased (↓) in IDA, increased (↑) in ACD and sideroblastic anemia, and normal (Ⓝ) in thalassemia trait",
        "Normal (Ⓝ) in ACD, increased (↑) in sideroblastic anemia, and decreased (↓) in IDA and thalassemia trait",
    ],
    "TIBC row on p80: IDA ↑, ACD ↓, Sideroblastic anemia ↓, Thalassemia trait Ⓝ.")

add(S4, 80, "recall",
    "In the p80 master table, what is the Transferrin Saturation pattern across Iron deficiency anemia, Anemia of chronic disease, Sideroblastic anemia, and Thalassemia trait?",
    "IDA: ↓↓; ACD: ↓; Sideroblastic anemia: ↑↑; Thalassemia trait: Ⓝ",
    [
        "IDA: ↓; ACD: ↓↓; Sideroblastic anemia: Ⓝ; Thalassemia trait: ↑↑",
        "IDA: ↑↑; ACD: ↓; Sideroblastic anemia: ↓↓; Thalassemia trait: Ⓝ",
        "IDA: ↓↓; ACD: ↑; Sideroblastic anemia: ↑↑; Thalassemia trait: ↓",
    ],
    "Transferrin saturation row on p80: IDA ↓↓, ACD ↓, Sideroblastic anemia ↑↑, Thalassemia trait Ⓝ.")

add(S4, 80, "match",
    "Match each condition in the p80 master table to its Serum Iron and Transferrin Saturation pattern — 1) Iron deficiency anemia 2) Anemia of chronic disease 3) Sideroblastic anemia 4) Thalassemia trait … A) Sr. iron ↓↓, Transferrin saturation ↓ B) Sr. iron ↑, Transferrin saturation ↑↑ C) Sr. iron Ⓝ, Transferrin saturation Ⓝ D) Sr. iron ↓, Transferrin saturation ↓↓",
    "1-D, 2-A, 3-B, 4-C",
    [
        "1-A, 2-D, 3-B, 4-C",
        "1-D, 2-B, 3-A, 4-C",
        "1-C, 2-A, 3-B, 4-D",
    ],
    "In the p80 table: IDA has Sr. iron ↓ and TSAT ↓↓; ACD has Sr. iron ↓↓ and TSAT ↓; Sideroblastic anemia has Sr. iron ↑ and TSAT ↑↑; Thalassemia trait has both normal (Ⓝ).")

add(S4, 80, "recall",
    "Under Inherited Iron Deficiency Anemia on p80, what does the abbreviation IRIDA stand for?",
    "Iron resistant iron deficiency anemia",
    [
        "Immune refractory iron depletion anemia",
        "Inherited reticulocyte iron deficiency aplasia",
        "Idiopathic renal iron deficiency anemia",
    ],
    "1. Iron resistant iron deficiency Anemia (IRIDA).")

add(S4, 80, "recall",
    "What is the molecular defect and mechanism of Iron Resistant Iron Deficiency Anemia (IRIDA) on p80?",
    "Defective matriptase-2 → increased hepcidin → inhibition of ferroportin",
    [
        "Defective hephaestin → decreased hepcidin → activation of ferroportin",
        "Defective HFE gene → absent hepcidin → uninhibited duodenal iron export",
        "Defective ferrochelatase → absent protoporphyrin → ring sideroblast formation",
    ],
    "1. Iron resistant iron deficiency anemia (IRIDA): Defective matriptase-2 → ↑ Hepcidin → Inhibit ferroportin.")

add(S4, 80, "recall",
    "In inherited iron deficiency anemia due to a DMT-1 mutation (cause #2 on p80), what is the cellular transport defect?",
    "No transport of iron from endosomes to cytoplasm",
    [
        "Failure of ferroportin to export iron across the basolateral membrane",
        "Inability of plasma transferrin to bind ferric iron in circulation",
        "Absence of duodenal cytochrome b reductase at the brush border",
    ],
    "2. DMT-1 mutation: No transport of iron from endosomes to cytoplasm.")

add(S4, 80, "recall",
    "In a DMT-1 mutation on p80, what is the status of iron stores?",
    "Normal (Ⓝ)",
    [
        "Completely absent",
        "Markedly depleted in Stage I",
        "Replaced by hemosiderin rings",
    ],
    "DMT-1 mutation — Indices: Iron stores : Ⓝ.")

add(S4, 80, "recall",
    "In a DMT-1 mutation on p80, what are the printed levels of TIBC and serum iron?",
    "TIBC: Decreased (↓); Serum iron: Normal or increased (Ⓝ / ↑)",
    [
        "TIBC: Increased (↑); Serum iron: Decreased (↓)",
        "TIBC: Normal (Ⓝ); Serum iron: Very low (↓↓)",
        "TIBC: Increased (↑); Serum iron: Increased (↑)",
    ],
    "DMT-1 mutation — Indices: Iron stores : Ⓝ, TIBC : ↓, Sr. iron : Ⓝ / ↑.")

add(S4, 80, "fillup",
    "The third cause of inherited iron deficiency anemia listed on p80 is ____, in which there is no transfer of iron.",
    "Atransferrinemia",
    ["Aceruloplasminemia", "Abetalipoproteinemia", "Afibrinogenemia"],
    "3. Atransferrinemia : No transfer of iron.")

# ---------------------------------------------------------------------------
# Book p81 — Protocol for Diagnosis
add(S5, 81, "recall",
    "At the very top of the p81 'Protocol for Diagnosis' flowchart, what is the first branch point?",
    "Lineage: Single versus Multiple",
    [
        "MCV: Low versus High",
        "Reticulocyte production index: Low versus High",
        "Iron indices: Normal versus Abnormal",
    ],
    "The p81 protocol starts with Lineage → Single vs Multiple.")

add(S5, 81, "recall",
    "Under the 'Single' lineage arm of the p81 flowchart, what parameter is evaluated next?",
    "Reticulocyte production index (Low vs High)",
    [
        "Hemoglobin electrophoresis (HbA₂ vs HbF)",
        "Serum ferritin and TIBC",
        "Direct Coombs test (Positive vs Negative)",
    ],
    "Single lineage proceeds to Reticulocyte production index → Low vs High.")

add(S5, 81, "recall",
    "Under the 'Low' Reticulocyte production index arm on p81, how does MCV divide?",
    "Normal (Ⓝ) to Low versus High",
    [
        "Microcytic (<60 fL) versus Normocytic (60–80 fL)",
        "Dimorphic versus Normochromic",
        "Intravascular versus Extravascular",
    ],
    "Under Low RPI, MCV branches into Ⓝ to Low and High.")

add(S5, 81, "fillup",
    "In the p81 flowchart, a Normal (Ⓝ) to Low MCV leads directly to evaluation of ____.",
    "Iron indices",
    ["Bone marrow biopsy", "Osmotic fragility", "Schilling test"],
    "Ⓝ to Low MCV → Iron indices.")

add(S5, 81, "recall",
    "At the bottom of the p81 diagnostic protocol, 'Iron indices' differentiates which four conditions?",
    "Iron deficiency anemia, anemia of chronic disease, sideroblastic anemia and thalassemia trait",
    [
        "Iron deficiency anemia, megaloblastic anemia, aplastic anemia and myelodysplastic syndrome",
        "Autoimmune hemolytic anemia, G6PD deficiency, hereditary spherocytosis and sickle cell anemia",
        "Anemia of chronic disease, pure red cell aplasia, paroxysmal nocturnal hemoglobinuria and IRIDA",
    ],
    "Under Iron indices, the flowchart branches into: Iron deficiency anemia, Anemia of chronic disease, Sideroblastic anemia, and Thalassemia trait.")

add(S5, 81, "truefalse",
    "TRUE or FALSE — in the p81 diagnostic flowchart, the complete sequence to reach the four microcytic/normocytic anemias is Lineage (Single) → Reticulocyte production index (Low) → MCV (Ⓝ to Low) → Iron indices.",
    "True — Single lineage → Low RPI → Ⓝ to Low MCV → Iron indices is the exact flowchart pathway",
    [
        "True — but only when the Reticulocyte Production Index (RPI) is High",
        "False — they sit under the Multiple-lineage branch of the protocol",
        "False — Iron indices are evaluated before checking MCV or RPI",
    ],
    "The p81 flowchart shows Lineage (Single vs Multiple) → RPI (Low vs High) → MCV (Ⓝ to Low vs High) → Iron indices → four anemias.")


GUIDES = {
    S1: (
        "Blood Picture & ACD Pathophysiology",
        "IDA and ACD are normocytic normochromic initially; RA and miliary TB cause microcytic hypochromic ACD.\n"
        "Sideroblastic anemia is dimorphic (microcytic + macrocytic); thalassemia trait is microcytic hypochromic.\n"
        "Hepcidin (liver peptide) inhibits ferroportin; IL-6/activin, HFE (chr 6), hemojuvelin and Tfr2 stimulate it, while hypoxia inhibits it.",
    ),
    S2: (
        "ACD Indices & Sideroblastic Etiology",
        "HFE mutation causes hemochromatosis; in ACD, ferritin and hepcidin are normal/high while Sr. iron, TIBC, TSAT and sTfR are low.\n"
        "Sideroblastic anemia is inherited (X-linked ALA synthase deficiency) or acquired (MDS, Cu deficiency, alcohol, chloramphenicol/INH/PZA, lead).\n"
        "Normal heme synthesis proceeds from Succinyl Co-A + Glycine + B6 (via ALA synthase) → ALA → Protoporphyrin + Fe → Heme → Hb.",
    ),
    S3: (
        "Sideroblastic Pathogenesis & Thalassemia",
        "ALA synthase deficiency leaves unbound iron around the erythroblast nucleus as ring sideroblasts on Prussian blue stain.\n"
        "Sideroblastic investigations show dimorphic cellularity, EM Pappenheimer bodies, high Sr. iron/TSAT, normal/high ferritin and low TIBC.\n"
        "Thalassemia trait (ββ⁰, ββ⁺) has one normal and one defective β gene, absent ineffective erythropoiesis, and normal iron indices.",
    ),
    S4: (
        "Thalassemia Indices & Inherited IDA",
        "Thalassemia trait shows normal RDW, Mentzer index <13, rare target/stippled cells, and HbA₂ 4–8% (normal 1.5–3%).\n"
        "The master table contrasts Sr. iron, ferritin, TIBC and TSAT across IDA, ACD, sideroblastic anemia and thalassemia trait.\n"
        "Inherited IDA includes IRIDA (defective matriptase-2 → ↑ hepcidin), DMT-1 mutation (no endosome-to-cytoplasm transport) and atransferrinemia.",
    ),
    S5: (
        "Diagnostic Protocol",
        "The diagnostic protocol begins with Lineage (Single vs Multiple) followed by Reticulocyte Production Index (Low vs High).\n"
        "Under Single lineage and Low RPI, MCV divides into Normal-to-Low versus High.\n"
        "Normal-to-Low MCV proceeds to Iron indices to separate IDA, ACD, sideroblastic anemia and thalassemia trait.",
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
