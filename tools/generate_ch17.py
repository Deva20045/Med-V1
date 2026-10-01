#!/usr/bin/env python3
"""Generate Chapter 17 Non-Immune Mediated Hemolytic Anemia (Book p97–102)."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 17
TITLE = "Non-Immune Mediated Hemolytic Anemia"
PAGES = "97-102"

S1 = "Overview & Paroxysmal Nocturnal Hemoglobinuria Physiology"
S2 = "PNH: Pathogenesis & Clinical Presentation"
S3 = "PNH: Investigations & Treatment"
S4 = "Fragmentation Hemolysis: MAHA, TMA & HUS vs TTP"
S5 = "Hemolytic Uremic Syndrome: Childhood vs Adult"
S6 = "Thrombotic Thrombocytopenic Purpura & Fragmentation Types"

RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    rng = random.Random(17000 + CHAPTER * 10000 + len(RAW))
    rng.shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2, f"truefalse True count: {stem}"
        assert sum(o.startswith("False") for o in options) == 2, f"truefalse False count: {stem}"
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p97 — Overview of Non-Immune Hemolysis & PNH Physiology
add(S1, 97, "recall",
    "At the top of p97, Non-Immune Mediated Hemolytic Anemia is divided into which four main categories?",
    "Infections (through exotoxins & endotoxins), Drugs and toxins, Paroxysmal nocturnal hemoglobinuria, and Fragmentation hemolysis",
    [
        "Warm antibody AIHA, Cold antibody AIHA, Paroxysmal cold hemoglobinuria, and Drug-induced immune hemolytic anemia",
        "Hemoglobinopathies (sickle cell/thalassemia), Membrane cytoskeleton defects, Red cell enzymopathies, and Sideroblastic anemia",
        "Iron deficiency anemia, Anemia of chronic disease, Megaloblastic macrocytic anemia, and Aplastic bone marrow failure",
    ],
    "The opening p97 chart divides non-immune mediated hemolytic anemia into Infections, Drugs and toxins, Paroxysmal nocturnal hemoglobinuria, and Fragmentation hemolysis.")

add(S1, 97, "recall",
    "Which four infectious causes (acting through exotoxins and endotoxins) are listed under Non-Immune Mediated Hemolytic Anemia on p97?",
    "Malaria, Babesia, Oroya fever and Clostridium perfringens",
    [
        "Infectious mononucleosis, EBV, cytomegalovirus and Mycoplasma pneumoniae",
        "Tertiary syphilis, HIV, hepatitis C and parvovirus B19",
        "Diphyllobothrium latum, Ancylostoma duodenale, Giardia and Entamoeba",
    ],
    "Infections (Through exotoxins & endotoxins) on p97: • Malaria, • Babesia, • Oroya fever, • Clostridium perfringens.")

add(S1, 97, "recall",
    "Which two drugs are specifically listed under 'Drugs and toxins' in the p97 non-immune hemolysis overview?",
    "Dapsone and primaquine",
    [
        "Methyldopa and procainamide",
        "Quinidine and rifampicin",
        "Penicillin and lenalidomide",
    ],
    "Drugs and toxins on p97: • Dapsone, • Primaquine.")

add(S1, 97, "recall",
    "Under Paroxysmal Nocturnal Hemoglobinuria (PNH) on p97, how is the pattern of hemolysis described?",
    "Chronic intravascular hemolysis with acute exacerbation",
    [
        "Acute self-limiting extravascular hemolysis in the spleen",
        "Purely intramedullary ineffective erythropoiesis",
        "Chronic cold-induced hepatic extravascular hemolysis",
    ],
    "Paroxysmal Nocturnal Hemoglobinuria on p97: Chronic intravascular hemolysis with acute exacerbation.")

add(S1, 97, "numeric",
    "How many blood lineages are affected in Paroxysmal Nocturnal Hemoglobinuria (PNH) according to p97?",
    "All 3 blood lineages",
    [
        "Only 1 lineage (erythroid only)",
        "Only 2 lineages (erythroid and lymphoid)",
        "Only plasma cells and T lymphocytes",
    ],
    "PNH on p97: All 3 blood lineages affected.")

add(S1, 97, "fillup",
    "The underlying defect in Paroxysmal Nocturnal Hemoglobinuria (PNH) on p97 is an acquired mutation in the ____ gene.",
    "PIGA",
    ["HFE", "ADAMTS13", "MYD88"],
    "Defect: Acquired mutation in PIGA gene.")

add(S1, 97, "recall",
    "On which chromosome is the PIGA gene located according to 'Physiology of PIGA Gene' on p97?",
    "X chromosome",
    [
        "Chromosome 6",
        "Chromosome 11",
        "Y chromosome",
    ],
    "Physiology of PIGA gene: PIGA gene (Present on X chromosome).")

add(S1, 97, "recall",
    "What is item 1 coded for by the PIGA gene on p97, and what is its function on the RBC surface?",
    "GPI anchor protein, which anchors complement regulatory proteins on the surface of the RBC",
    [
        "Ferroportin-1, which exports ferrous iron across the basolateral membrane",
        "Spectrin dimer, which maintains biconcave deformability in splenic sinusoids",
        "Transferrin receptor-1, which internalizes ferric iron into endosomes",
    ],
    "PIGA gene codes for: 1. GPI anchor protein → Anchor complement regulatory protein on the surface of RBC.")

add(S1, 97, "fillup",
    "On p97, CD55 is expanded as ____.",
    "Decay accelerating factor (DAF)",
    ["Membrane inhibitor of reactive lysis (MIRL)", "Urokinase plasminogen activator receptor (UPAR)", "Direct antiglobulin factor (DAF)"],
    "CD55 : Decay accelerating factor (DAF).")

add(S1, 97, "fillup",
    "On p97, CD59 is expanded as ____.",
    "Membrane inhibitor of reactive lysis (MIRL)",
    ["Decay accelerating factor (DAF)", "Complement factor H (CFH)", "Membrane cofactor protein (MCP)"],
    "CD59 : Membrane inhibitor of reactive lysis (MIRL).")

add(S1, 97, "match",
    "Match each GPI-anchored complement regulatory protein or anchoring moiety on the RBC surface (p97) to its full name or description — 1) CD55 2) CD59 3) GPI anchor protein … A) Glycolipid protein on RBC surface B) Decay accelerating factor (DAF) C) Membrane inhibitor of reactive lysis (MIRL)",
    "1-B, 2-C, 3-A",
    [
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
        "1-A, 2-C, 3-B",
    ],
    "Under GPI anchor protein (glycolipid protein on RBC surface) on p97: CD55 : Decay accelerating factor (DAF); CD59 : Membrane inhibitor of reactive lysis (MIRL) — bracketed as main complement regulatory proteins that prevent attack by complement-mediated protein.")

add(S1, 97, "recall",
    "Besides 1. GPI anchor protein, what are items 2 and 3 coded for/anchored via the PIGA gene on p97?",
    "2. Neutrophil alkaline phosphatase, and 3. Urokinase plasminogen activator receptor (UPAR)",
    [
        "2. Leukocyte myeloperoxidase (MPO), and 3. Tissue plasminogen activator inhibitor-1 (PAI-1)",
        "2. Erythrocyte acid phosphatase, and 3. Platelet glycoprotein Ib–IX–V receptor complex",
        "2. Glucose-6-phosphate dehydrogenase (G6PD), and 3. Pyruvate kinase tetrameric enzyme",
    ],
    "PIGA gene (Present on X chromosome) codes for: 1. GPI anchor protein, 2. Neutrophil alkaline phosphatase, 3. Urokinase plasminogen activator receptor (UPAR).")

add(S1, 97, "truefalse",
    "TRUE or FALSE — according to the bottom note on p97, inherited hemolysis is intracorpuscular, whereas acquired hemolysis is extracorpuscular EXCEPT for PNH.",
    "True — inherited hemolysis is intracorpuscular, and acquired hemolysis is extracorpuscular except PNH",
    [
        "True — both PNH and warm autoimmune hemolytic anemia are inherited intracorpuscular defects",
        "False — PNH is an inherited autosomal dominant extracorpuscular hemolytic anemia",
        "False — all acquired hemolytic anemias without exception are mediated by extracorpuscular factors",
    ],
    "Note at bottom of p97: • Inherited hemolysis : Intracorpuscular. • Acquired hemolysis : Extracorpuscular (Except PNH).")

# ---------------------------------------------------------------------------
# Book p98 — PNH Pathogenesis & Clinical Presentation
add(S2, 98, "recall",
    "In the left arm of the PNH Pathogenesis chart on p98, what is the sequence from 'Defective GPI anchor protein' to RBC lysis?",
    "Defective GPI anchor protein → Defective complement regulatory protein → Affinity to PNH III RBC (PNH III RBCs lack CD55, CD59) → Lysis of RBC",
    [
        "Defective GPI anchor protein → Splenic macrophage Fc-gamma receptor binding → Progressive membrane microvesiculation → Extravascular lysis of RBC",
        "Defective GPI anchor protein → IgM cold agglutination in peripheral extremities → Hepatic Kupffer cell C3b uptake → Extravascular hepatic lysis",
        "Defective GPI anchor protein → Absent protoporphyrin IX synthesis in mitochondria → Ring sideroblast formation → Intramedullary lysis of normoblasts",
    ],
    "Pathogenesis left arm on p98: Defective GPI anchor protein → Defective complement regulatory protein → Affinity to PNH III RBC (PNH III RBCs lack CD55, CD59) → Lysis of RBC.")

add(S2, 98, "recall",
    "In the middle and right arms of the PNH Pathogenesis chart on p98, what are the consequences of a PIGA gene mutation on neutrophil alkaline phosphatase and UPAR?",
    "Neutrophil alkaline phosphatase decreases (↓); Defective UPAR leads to Thrombosis",
    [
        "Neutrophil alkaline phosphatase increases (↑); Defective UPAR leads to Bleeding",
        "Neutrophil alkaline phosphatase is unchanged; Defective UPAR leads to Spherocytosis",
        "Neutrophil alkaline phosphatase increases (↑); Defective UPAR leads to Splenomegaly",
    ],
    "Pathogenesis middle and right arms on p98: Neutrophil alkaline phosphatase ↓; Defective UPAR → Thrombosis.")

add(S2, 98, "match",
    "Match each arm of the PIGA gene mutation pathogenesis chart on p98 to its downstream consequence — 1) Defective GPI anchor protein 2) Neutrophil alkaline phosphatase 3) Defective UPAR … A) Decreased (↓) level B) Thrombosis C) Defective complement regulatory protein → Affinity to PNH III RBC (lacking CD55, CD59) → Lysis of RBC",
    "1-C, 2-A, 3-B",
    [
        "1-B, 2-A, 3-C",
        "1-C, 2-B, 3-A",
        "1-A, 2-C, 3-B",
    ],
    "Pathogenesis on p98: Mutation of PIGA gene → (1) Defective GPI anchor protein → Lysis of PNH III RBC; (2) Neutrophil alkaline phosphatase ↓; (3) Defective UPAR → Thrombosis.")

add(S2, 98, "fillup",
    "According to the first bullet of the boxed note on p98, ____ scavenging due to RBC lysis also causes thrombosis in PNH.",
    "NO (nitric oxide)",
    ["CO (carbon monoxide)", "O₂ (oxygen)", "H₂S (hydrogen sulfide)"],
    "Boxed note on p98: • NO scavenging d/t RBC lysis also causes thrombosis.")

add(S2, 98, "recall",
    "According to the second bullet of the boxed note on p98, markedly decreased (↓↓) leukocyte/neutrophil alkaline phosphatase levels are seen in which two conditions?",
    "CML and PNH",
    [
        "Polycythemia vera and essential thrombocythemia",
        "Leukemoid reaction and pregnancy",
        "Hodgkin lymphoma and multiple myeloma",
    ],
    "Boxed note on p98: • ↓↓ alkaline phosphatase level : CML, PNH.")

add(S2, 98, "recall",
    "Under Clinical Presentation of PNH on p98, what is the sequence explaining '1. Nocturnal hemoglobinuria/hemosiderinuria'?",
    "Sleep → Acidotic pH → Intravascular hemolysis → High colored urine",
    [
        "Sleep → Respiratory alkalosis → Splenic sequestration → Acholic stool",
        "Exercise → Cold extremity temperature (4°C) → Kupffer cell phagocytosis → Acrocyanosis",
        "Fasting → Hyperbilirubinemia → Renal tubular secretion → Orange urine",
    ],
    "1. Nocturnal hemoglobinuria/hemosiderinuria: Sleep → Acidotic pH → Intravascular hemolysis → High colored urine (with image captioned 'Diurnal changes in hemoglobinuria in PNH patients').")

add(S2, 98, "recall",
    "Under '2. Thrombosis' in PNH on p98, which venous thrombosis (item a) is marked most common (m/c), and what syndrome does it cause?",
    "Hepatic venous thrombosis (m/c) → Budd–Chiari syndrome",
    [
        "Renal vein thrombosis (m/c) → Nephrotic syndrome",
        "Splenic vein thrombosis (m/c) → Sinistral portal hypertension",
        "Subclavian vein thrombosis (m/c) → Paget–Schroetter syndrome",
    ],
    "2. Thrombosis on p98: a. Hepatic venous thrombosis (m/c) → Budd Chiari Syndrome.")

add(S2, 98, "fillup",
    "Beneath Budd–Chiari syndrome on p98, an arrow notes that the other hematologic cause of Budd–Chiari syndrome is ____.",
    "PCRV (polycythemia rubra vera)",
    ["ITP (immune thrombocytopenic purpura)", "CLL (chronic lymphocytic leukemia)", "MDS (myelodysplastic syndrome)"],
    "Budd Chiari Syndrome → ↓ Other cause is PCRV.")

add(S2, 98, "recall",
    "Besides hepatic venous thrombosis (m/c), which three other thrombosis sites are listed as items b, c, and d under '2. Thrombosis' on p98?",
    "b. Intraabdominal thrombosis, c. Cerebral venous thrombosis, and d. Deep vein thrombosis",
    [
        "b. Coronary artery thrombosis, c. Retinal artery occlusion, and d. Femoral artery embolism",
        "b. Pulmonary microvascular thrombosis, c. Glomerular capillary thrombosis, and d. Digital ischemia",
        "b. Carotid artery thrombosis, c. Renal artery thrombosis, and d. Radial artery thrombosis",
    ],
    "2. Thrombosis on p98 lists: a. Hepatic venous thrombosis (m/c), b. Intraabdominal thrombosis, c. Cerebral venous thrombosis, d. Deep vein thrombosis.")

add(S2, 98, "recall",
    "Under '3. Pancytopenia' in PNH on p98, what is the bone marrow cellularity pattern, and which one is marked most common (m/c)?",
    "Hypercellular (m/c), normal or hypocellular bone marrow",
    [
        "Strictly acellular fatty bone marrow in 100% of cases",
        "Fibrotic dry-tap bone marrow (m/c) with osteosclerosis",
        "Purely megaloblastic bone marrow with giant metamyelocytes",
    ],
    "3. Pancytopenia on p98: Bone marrow : Hypercellular (m/c), normal or hypocellular bone marrow.")

add(S2, 98, "numeric",
    "What is the '25/10 rule' under '4. Aplastic anemia' in PNH on p98?",
    "25% of PNH progresses to aplastic anemia; 10% of aplastic anemia is due to PNH",
    [
        "25% of PNH progresses to CML; 10% of CML is due to PNH",
        "10% of PNH progresses to aplastic anemia; 25% of aplastic anemia is due to PNH",
        "25% of PNH resolves spontaneously; 10% requires splenectomy",
    ],
    "4. Aplastic anemia — 25/10 rule: – 25% of PNH progresses to aplastic anemia; – 10% of aplastic anemia is d/t PNH.")

add(S2, 98, "fillup",
    "At the bottom of p98 (item e), PNH is noted to rarely progress to ____.",
    "AML (acute myeloid leukemia)",
    ["ALL (acute lymphoblastic leukemia)", "CLL (chronic lymphocytic leukemia)", "Multiple myeloma"],
    "e. Rarely progresses to AML.")

# ---------------------------------------------------------------------------
# Book p99 — PNH Investigation & Treatment
add(S3, 99, "recall",
    "Under Investigation of PNH on p99, what is the Investigation of Choice (IOC), and what does it detect?",
    "Flow cytometry (IOC): detects PNH III RBCs percentage",
    [
        "Ham's acid hemolysis test (IOC): detects serum complement C3",
        "Direct Coombs test (IOC): detects surface IgG and C3d",
        "Sucrose lysis test (IOC): detects spectrin deficiency",
    ],
    "1. Flow cytometry (IOC): • Detects PNH III RBC's percentage.")

add(S3, 99, "numeric",
    "In flow cytometry for PNH on p99, what percentage of PNH III RBCs is considered 'Significant'?",
    ">50%",
    [">5%", ">15%", ">90%"],
    "1. Flow cytometry (IOC): • Significant : >50%.")

add(S3, 99, "recall",
    "In the '2. Urine analysis' flowchart on p99, when urine is centrifuged, how does the supernatant distinguish intact RBCs (hematuria) from free Hb/myoglobin?",
    "Clear supernatant indicates RBC; high-colored supernatant indicates Hb or myoglobin",
    [
        "High-colored supernatant indicates intact RBC; clear supernatant indicates free Hb",
        "Turbid precipitate indicates myoglobin; clear supernatant indicates hemosiderin",
        "Green fluorescence indicates Hb; clear supernatant indicates urobilinogen",
    ],
    "2. Urine analysis on p99: Centrifuge urine → Supernatant → Clear = RBC; High colored = Hb, myoglobin.")

add(S3, 99, "numeric",
    "In the p99 urine analysis flowchart, when a high-colored supernatant (containing Hb or myoglobin) is left to rest aside for 3–6 hours, how are Hb and myoglobin differentiated?",
    "Remains high-colored = Hb; becomes clear = myoglobin (because myoglobin has a T₁/₂ of 3–6 hours)",
    [
        "Becomes clear = Hb (T₁/₂ of 3–6 hours); remains high-colored = myoglobin",
        "Forms a blue ring = Hb; forms a red precipitate = myoglobin (T₁/₂ of 24 hours)",
        "Both become clear within 30 minutes due to spontaneous oxidation",
    ],
    "Under Hb, myoglobin on p99: Rest aside for 3–6 hrs → High colored = Hb; Clear = myoglobin (T1/2 : 3–6 hrs).")

add(S3, 99, "recall",
    "What is the result of the Coombs test (item 3) in PNH on p99?",
    "Negative",
    [
        "Strongly positive (3+, 4+) for IgG",
        "Positive for cold IgM agglutinins",
        "Positive for Donath–Landsteiner biphasic hemolysin",
    ],
    "3. Coombs : Negative.")

add(S3, 99, "recall",
    "What are items 4 and 5 under Investigation of PNH on p99?",
    "4. Bone marrow studies; 5. Ham's test (Not used)",
    [
        "4. Spleen biopsy; 5. Donath–Landsteiner test (Gold standard)",
        "4. Osmotic fragility; 5. Schilling test (Routine)",
        "4. Hb electrophoresis; 5. Prussian blue stain (Obsolete)",
    ],
    "4. Bone marrow studies. 5. Hams test (Not used).")

add(S3, 99, "management",
    "In the Treatment flowchart for PNH on p99, what is the treatment for the 'Bone marrow involvement' branch?",
    "Allogeneic hematopoietic stem cell transplant",
    [
        "Autologous peripheral blood stem cell transplant",
        "Splenectomy plus high-dose corticosteroids",
        "Oral hydroxyurea plus phlebotomy",
    ],
    "Treatment on p99: Bone marrow involvement → Allogenic hematopoietic stem cell transplant.")

add(S3, 99, "management",
    "In the Treatment flowchart for PNH on p99, what is the treatment for the 'Hemoglobinuria/thrombosis' branch?",
    "Anti-C5 antibodies (Ravulizumab > Eculizumab) + meningococcal vaccine",
    [
        "Anti-CD20 antibody (Rituximab) + BCG vaccine",
        "Anti-IgE antibody (Omalizumab) + rabies vaccine",
        "High-dose IVIG + oral warfarin monotherapy",
    ],
    "Treatment on p99: Hemoglobinuria/thrombosis → Anti C5 antibodies (Ravulizumab > Eculizumab) + meningococcal vaccine.")

# ---------------------------------------------------------------------------
# Book p100 — Non-immune Hemolysis: Fragmentation (MAHA, TMA, HUS vs TTP)
add(S4, 100, "recall",
    "At the top of p100, 'Non immune Hemolysis - Fragmentation' is defined as an acute syndrome of which two entities?",
    "Microangiopathic hemolytic anemia (MAHA) and thrombotic microangiopathy (TMA)",
    [
        "Autoimmune hemolytic anemia (AIHA) and paroxysmal nocturnal hemoglobinuria (PNH)",
        "Macroangiopathic hemolysis and disseminated intravascular coagulation (DIC)",
        "Hereditary spherocytosis and hereditary elliptocytosis",
    ],
    "Top of p100: Acute syndrome of microangiopathic hemolytic anemia (MAHA) and thrombotic microangiopathy (TMA).")

add(S4, 100, "recall",
    "Which two classic syndromes are listed under 'Seen in :' at the top of p100?",
    "Hemolytic uremic syndrome (HUS) and thrombotic thrombocytopenic purpura (TTP)",
    [
        "Evans syndrome and Imerslund–Gräsbeck syndrome",
        "Plummer–Vinson syndrome and Felty syndrome",
        "Budd–Chiari syndrome and Dressler syndrome",
    ],
    "Seen in: • Hemolytic uremic syndrome (HUS), • Thrombotic thrombocytopenic purpura (TTP).")

add(S4, 100, "recall",
    "In the MAHA etiopathogenesis flowchart on p100, endothelial injury in small vessels triggers the release of what factor and form?",
    "von Willebrand factor (vWF) — large, high-molecular-weight multimers",
    [
        "Tissue plasminogen activator (tPA) — low-molecular-weight monomers",
        "Antithrombin III — heparin-bound dimers",
        "Complement C3b — membrane-bound opsonins",
    ],
    "MAHA flowchart on p100: Endothelial injury in small vessels → Release of von Willebrand factor (vWF) (vWF : Large, high molecular weight multimers).")

add(S4, 100, "match",
    "Match each component of the MAHA microvascular platelet plug flowchart on p100 to its role — 1) vWF multimers 2) Gp Ib–IX 3) Gp VI … A) Bind to collagen B) Released upon endothelial injury to initiate platelet plug C) Attract platelets",
    "1-B, 2-C, 3-A",
    [
        "1-C, 2-B, 3-A",
        "1-A, 2-C, 3-B",
        "1-B, 2-A, 3-C",
    ],
    "Under endothelial injury on p100: vWF multimers act via Gp Ib–IX (Attract platelets) and Gp VI (Bind to collagen) to form the Platelet plug.")

add(S4, 100, "recall",
    "In the MAHA flowchart on p100, formation of the 'Platelet plug' branches into which two downstream hematologic consequences?",
    "1) Trap platelets → Thrombocytopenia; 2) Intravascular RBC destruction (fragmentation) → Microangiopathic non-immune fragmentation hemolysis",
    [
        "1) Activate plasminogen → Hyperfibrinolysis; 2) Splenic macrophage phagocytosis → Extravascular spherocytosis",
        "1) Bone marrow megakaryocyte aplasia → Pancytopenia; 2) Hepatic Kupffer cell uptake → Cold agglutination",
        "1) Prolong PT/aPTT → Coagulopathy; 2) Inhibit ferroportin → Iron-deficient erythropoiesis",
    ],
    "Platelet plug on p100 branches into: Trap platelets → Thrombocytopenia, and Intravascular RBC destruction (Fragmentation) → Microangiopathic non-immune fragmentation hemolysis.")

add(S4, 100, "recall",
    "How is TMA (Thrombotic Microangiopathy) defined under Etiopathogenesis on p100?",
    "Small vessel disease of kidney",
    [
        "Large vessel aneurysm of the abdominal aorta",
        "Medium vessel necrotizing vasculitis of the lungs",
        "Venous thrombosis of the hepatic veins",
    ],
    "TMA on p100: Small vessel disease of kidney.")

add(S4, 100, "recall",
    "Which five causes of TMA are listed on p100, and which one is parenthetically marked '(most important)'?",
    "HUS (most important), catastrophic antiphospholipid syndrome (APS), diffuse scleroderma, HELLP syndrome and malignant hypertension",
    [
        "TTP (most important), rheumatoid arthritis, ulcerative colitis, preeclampsia and benign hypertension",
        "PNH (most important), SLE, polyarteritis nodosa, gestational diabetes and coarctation of aorta",
        "DIC (most important), Sjögren's syndrome, Crohn's disease, hyperemesis gravidarum and pulmonary hypertension",
    ],
    "TMA Causes on p100: • HUS (most important), • Catastrophic antiphospholipid syndrome (APS), • Diffuse scleroderma, • HELLP Syndrome, • Malignant hypertension.")

add(S4, 100, "oddoneout",
    "Pick the ODD ONE OUT — which of the following is NOT listed among the causes of TMA on p100?",
    "Henoch–Schönlein purpura (IgA vasculitis)",
    [
        "Catastrophic antiphospholipid syndrome (APS)",
        "Diffuse scleroderma",
        "Malignant hypertension",
    ],
    "Causes of TMA listed on p100 are HUS (most important), catastrophic APS, diffuse scleroderma, HELLP syndrome, and malignant hypertension.")

add(S4, 100, "recall",
    "In the HUS v/s TTP table on p100, what are the affected anatomical sites in HUS versus TTP?",
    "HUS: Renal capillaries; TTP: Brain (small cerebral vessels) and GIT",
    [
        "HUS: Brain and GIT; TTP: Renal capillaries only",
        "HUS: Splenic sinusoids; TTP: Hepatic portal veins",
        "HUS: Pulmonary alveolar capillaries; TTP: Coronary arteries",
    ],
    "Site row in HUS v/s TTP table on p100: HUS = Renal capillaries; TTP = • Brain (Small cerebral vessels), • GIT.")

add(S4, 100, "recall",
    "In the HUS v/s TTP table on p100, what is the primary 'Disease' listed for HUS versus TTP?",
    "HUS: Renal failure; TTP: Small vessel stroke / lacunar stroke",
    [
        "HUS: Small vessel stroke / lacunar stroke; TTP: Nephrotic syndrome",
        "HUS: Budd–Chiari syndrome; TTP: Subacute combined degeneration",
        "HUS: Acute liver failure; TTP: Pulmonary embolism",
    ],
    "Disease row in HUS v/s TTP table on p100: HUS = Renal failure; TTP = Small vessel stroke/lacunar stroke.")

add(S4, 100, "recall",
    "Compare the classic clinical 'Presentation' of HUS (Triad) and TTP (Pentad) in the p100 table:",
    "HUS Triad: MAHA, thrombocytopenia, renal failure; TTP Pentad: MAHA, thrombocytopenia, fever, neurological manifestations, renal failure (rare)",
    [
        "HUS Pentad: MAHA, thrombocytosis, fever, stroke, jaundice; TTP Triad: MAHA, leukopenia, renal failure",
        "HUS Triad: spherocytosis, splenomegaly, jaundice; TTP Pentad: pancytopenia, glossitis, neuropathy, diarrhea, rash",
        "HUS Triad: hematuria, flank pain, palpable mass; TTP Pentad: fever, arthralgia, purpura, abdominal pain, melena",
    ],
    "Presentation row on p100 — HUS Triad: microangiopathic hemolytic anemia, thrombocytopenia, renal failure; TTP Pentad: microangiopathic hemolytic anemia, thrombocytopenia, fever, neurological manifestations, renal failure (Rare).")

add(S4, 100, "match",
    "Match each feature in the p100 HUS vs TTP comparison table to the corresponding disorder and category — 1) HUS target site & disease 2) HUS clinical presentation 3) TTP target site & disease 4) TTP clinical presentation … A) Triad of MAHA, thrombocytopenia, and renal failure B) Brain (small cerebral vessels) & GIT; small vessel/lacunar stroke C) Pentad of MAHA, thrombocytopenia, fever, neurological manifestations, and rare renal failure D) Renal capillaries; renal failure",
    "1-D, 2-A, 3-B, 4-C",
    [
        "1-B, 2-C, 3-D, 4-A",
        "1-D, 2-C, 3-B, 4-A",
        "1-A, 2-D, 3-C, 4-B",
    ],
    "HUS v/s TTP table on p100 contrasts HUS (Renal capillaries, Renal failure, Triad) with TTP (Brain & GIT, Small vessel stroke/lacunar stroke, Pentad).")

# ---------------------------------------------------------------------------
# Book p101 — Hemolytic Uremic Syndrome (HUS): Childhood vs Adult
add(S5, 101, "recall",
    "In the Hemolytic Uremic Syndrome (HUS) Types table on p101, what are the 'Other names' for Childhood HUS (<5 yrs) and Adult HUS?",
    "Childhood HUS (<5 yrs): D⁺ HUS; Adult HUS: D⁻ HUS / Atypical HUS",
    [
        "Childhood HUS (<5 yrs): D⁻ HUS / Atypical HUS; Adult HUS: D⁺ HUS",
        "Childhood HUS (<5 yrs): Warm HUS; Adult HUS: Cold HUS",
        "Childhood HUS (<5 yrs): Familial HUS; Adult HUS: Enteropathic HUS",
    ],
    "Other names row on p101: Childhood HUS (<5 yrs) = D+ HUS; Adult HUS = D- HUS, Atypical HUS.")

add(S5, 101, "recall",
    "In the p101 HUS table, how do Childhood HUS (<5 yrs) and Adult HUS differ in 'Associated with dysentery' and 'Severity'?",
    "Childhood HUS: Yes (preceded by bloody diarrhoea), Severity: Benign; Adult HUS: No, Severity: Leads to end stage renal disease (m/c)",
    [
        "Childhood HUS: No, Severity: Leads to ESRD; Adult HUS: Yes (preceded by bloody diarrhoea), Severity: Benign",
        "Both Childhood and Adult HUS: Preceded by bloody diarrhoea and Benign",
        "Both Childhood and Adult HUS: Not associated with dysentery and lead to ESRD",
    ],
    "Rows 2 & 3 on p101: Childhood HUS = Yes (Preceeded by bloody diarrhoea), Benign; Adult HUS = No, Leads to end stage renal disease (m/c).")

add(S5, 101, "match",
    "Match Childhood HUS (<5 yrs) and Adult HUS on p101 to their nomenclature, dysentery association, and course — 1) Childhood HUS (<5 yrs) nomenclature & trigger 2) Childhood HUS (<5 yrs) clinical course 3) Adult HUS nomenclature & trigger 4) Adult HUS clinical course … A) Benign course with good prognosis B) D⁺ HUS; associated with dysentery (preceded by bloody diarrhoea) C) Leads to end-stage renal disease (m/c) D) D⁻ HUS / Atypical HUS; not associated with dysentery",
    "1-B, 2-A, 3-D, 4-C",
    [
        "1-D, 2-C, 3-B, 4-A",
        "1-B, 2-C, 3-D, 4-A",
        "1-A, 2-B, 3-C, 4-D",
    ],
    "Top rows of p101 table: Childhood HUS (<5 yrs) = D+ HUS, associated with dysentery (preceded by bloody diarrhoea), Benign. Adult HUS = D- HUS / Atypical HUS, not associated with dysentery, leads to end stage renal disease (m/c).")

add(S5, 101, "recall",
    "Under the 'Cause' row for Childhood HUS (<5 yrs) on p101, which two bacterial toxins account for 90% of toxin-mediated endothelial injury, and which one is marked most common (m/c)?",
    "a. Enterohemorrhagic E. coli: EHEC O157:H7 (Shiga-like toxin, m/c) and b. Shiga toxin (Shigella dysenteriae)",
    [
        "a. Enterotoxigenic E. coli (heat-labile toxin, m/c) and b. Vibrio cholerae enterotoxin",
        "a. Clostridium difficile toxin A/B (m/c) and b. Salmonella typhi Vi antigen",
        "a. Staphylococcus aureus heat-stable toxin (m/c) and b. Bacillus cereus emetic toxin",
    ],
    "Childhood HUS Cause on p101: Toxin mediated endothelial injury — a. Enterohemorrhagic E. coli : EHEC O157:H7 (Shiga like toxin) : m/c, and b. Shiga toxin (Shigella dysenteriae) — bracketed together as 90%.")

add(S5, 101, "numeric",
    "What accounts for the remaining 10% of toxin-mediated endothelial injury in Childhood HUS on p101?",
    "c. Neuraminidases : 10% (Streptococcus pneumoniae)",
    [
        "c. Lecithinase : 10% (Clostridium perfringens)",
        "c. Exotoxin A : 10% (Pseudomonas aeruginosa)",
        "c. Listeriolysin O : 10% (Listeria monocytogenes)",
    ],
    "Childhood HUS Cause on p101: c. Neuraminidases : 10% (Streptococcus pneumoniae).")

add(S5, 101, "recall",
    "How is the microscopic 'Endothelial injury' in Childhood HUS described on p101?",
    "Swelling and detachment of the endothelial cell from the basement membrane",
    [
        "Transmural fibrinoid necrosis with eosinophilic granulomas",
        "Linear IgG deposition along the glomerular basement membrane",
        "Subepithelial humps of C3 without endothelial swelling",
    ],
    "Childhood HUS Cause on p101: • Endothelial injury : Swelling & detachment of endothelial cell from basement membrane.")

add(S5, 101, "numeric",
    "In Childhood HUS on p101, what percentage of infected patients develop HUS, and in what percentage does it resolve?",
    "Only 3–9% develop HUS; resolves in 95%",
    [
        "50–60% develop HUS; resolves in 10%",
        "80–90% develop HUS; resolves in 25%",
        "100% develop HUS; resolves in 5%",
    ],
    "Childhood HUS Cause bullets on p101: • Only 3–9% develop HUS. • Resolves in 95%.")

add(S5, 101, "recall",
    "Under Adult HUS causes on p101, familial/inherited disease involves activation of the alternate complement pathway via which three mutations (and which one is most common)?",
    "a. Complement factor H (CFH) mutation (m/c cause of adult HUS), b. Complement factor B (CFB) mutation, and c. Membrane cofactor P (MCP) mutation",
    [
        "a. Phosphatidylinositol glycan class A (PIGA) mutation (m/c cause of adult HUS), b. CD55 (DAF) mutation, and c. CD59 (MIRL) mutation",
        "a. Classic C1 esterase inhibitor (C1-INH) mutation (m/c cause of adult HUS), b. Complement C2 deficiency, and c. Complement C4 deficiency",
        "a. ADAMTS-13 metalloprotease mutation (m/c cause of adult HUS), b. Factor V Leiden R506Q mutation, and c. Prothrombin G20210A mutation",
    ],
    "Adult HUS Cause on p101 — Familial/inherited: Activation of alternate complement pathway: a. Complement factor H (CFH) mutation: m/c cause of adult HUS; b. Complement factor B (CFB) mutation; c. Membrane cofactor P (MCP) mutation.")

add(S5, 101, "recall",
    "Under 'Sporadic (Rare)' causes of Adult HUS on p101, which seven drugs are listed under item a?",
    "Mitomycin-C, gemcitabine, cisplatin, ticlopidine, clopidogrel, tacrolimus and cyclosporine",
    [
        "Methyldopa, procainamide, penicillin, cephalosporins, lenalidomide, quinidine and rifampicin",
        "Chloramphenicol, isoniazid, pyrazinamide, methotrexate, phenytoin, triamterene and sulfasalazine",
        "Dapsone, primaquine, hydroxyurea, cytarabine, 6-mercaptopurine, aspirin and warfarin",
    ],
    "Adult HUS Sporadic (Rare) causes on p101: a. Drugs : Mitomycin-C, Gemcitabine, Cisplatin, Ticlopidine, Clopidogrel, Tacrolimus, Cyclosporine.")

add(S5, 101, "recall",
    "Besides drugs (item a), which four clinical states (items b–e) are listed under 'Sporadic (Rare)' causes of Adult HUS on p101?",
    "b. Pregnancy, c. HELLP, d. Post bone marrow transplantation, and e. HIV",
    [
        "b. Hypothyroidism, c. Scurvy, d. COPD, and e. Alcoholism",
        "b. Celiac disease, c. Tropical sprue, d. Crohn's disease, and e. Blind loop syndrome",
        "b. Tertiary syphilis, c. Mycoplasma pneumoniae, d. EBV, and e. Malaria",
    ],
    "Adult HUS Sporadic (Rare) causes on p101: b. Pregnancy, c. HELLP, d. Post bone marrow transplantation, e. HIV.")

add(S5, 101, "match",
    "Match the HUS category or mutation in the Prognosis row on p101 to its printed outcome — 1) Childhood HUS (<5 yrs) 2) Adult HUS with CFB mutation 3) Adult HUS with MCP mutation … A) Good prognosis (childhood) B) Good prognosis (adult mutation) C) Worst prognosis",
    "1-A, 2-C, 3-B",
    [
        "1-C, 2-A, 3-B",
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
    ],
    "Prognosis row on p101: Childhood HUS = Good; Adult HUS: • CFB mutation : Worst, • MCP mutation : Good.")

add(S5, 101, "fillup",
    "Under Investigations for Childhood HUS on p101, stool culture on ____ medium identifies EHEC as non-fermenters.",
    "Sorbitol MacConkey",
    ["Thiosulfate–citrate–bile salts–sucrose (TCBS)", "Bordet–Gengou", "Buffered charcoal yeast extract (BCYE)"],
    "Investigations on p101: Culture : Sorbitol MacConkey → EHEC (Non-fermenters).")

add(S5, 101, "recall",
    "Which six blood investigation findings are listed for Childhood HUS on p101?",
    "Fragmented RBCs in PS (schistocytes), ↑↑ LDH (d/t intravascular hemolysis), –ve Coombs test, ↑ indirect bilirubin (d/t hemolysis), ↓ haptoglobin levels, and normal PT/APTT",
    [
        "Uniform microspherocytes in PS, ↓ LDH, strongly +ve Direct Coombs test (3+/4+), ↑ direct conjugated bilirubin, ↑ haptoglobin levels, and prolonged PT/APTT",
        "Target cells and Heinz bodies in PS, normal LDH, +ve Indirect Coombs test, normal serum bilirubin, normal haptoglobin levels, and isolated prolonged aPTT",
        "Ring sideroblasts and Pappenheimer bodies in PS, ↓ LDH, –ve Coombs test, ↓ serum ferritin, ↑ total iron-binding capacity (TIBC), and prolonged PT",
    ],
    "Blood investigations on p101: • Fragmented RBCs in PS (Schistocytes), • ↑↑ LDH (D/t intravascular hemolysis), • -ve Coombs test, • ↑ indirect bilirubin (D/t hemolysis), • ↓ haptoglobin levels, • Normal PT/APTT.")

add(S5, 101, "management",
    "What are the three points under 'Supportive Rx' for Childhood HUS (<5 yrs) in the bottom-left cell of p101?",
    "Isotonic saline volume expansion, bowel rest, and antibiotics are avoided (as they ↑ risk of HUS)",
    [
        "Hypertonic saline fluid restriction, high-residue fiber diet, and immediate intravenous ciprofloxacin therapy",
        "Urgent bilateral nephrectomy, high-dose intravenous methylprednisolone, and oral cyclophosphamide",
        "Prophylactic platelet transfusions, fresh frozen plasma infusions, and oral metronidazole for 14 days",
    ],
    "Childhood HUS Mx on p101 — Supportive Rx: • Isotonic saline volume expansion, • Bowel rest, • Antibiotics are avoided (↑ risk of HUS).")

add(S5, 101, "management",
    "What are the management points listed for Adult HUS in the bottom-right cell of p101?",
    "Plasmapheresis within 24 hrs; Transplantation (high recurrence) + Rituximab (anti-CD20) / Eculizumab (anti-C5)",
    [
        "Isotonic saline volume expansion and bowel rest alone, with plasmapheresis and anti-C5 therapy strictly contraindicated",
        "Emergency splenectomy within 24 hrs + oral hydroxyurea and prophylactic cholecystectomy at the same sitting",
        "Allogeneic bone marrow transplantation + intramuscular hydroxocobalamin and high-dose oral folic acid supplementation",
    ],
    "Adult HUS Mx on p101: • Plasmapheresis within 24 hrs. • Transplantation (High recurrence) + Rituximab (anti CD20) / Eculizumab (anti C5).")

# ---------------------------------------------------------------------------
# Book p102 — Thrombotic Thrombocytopenic Purpura (TTP) & Fragmentation Types
add(S6, 102, "numeric",
    "Under Causes of Thrombotic Thrombocytopenic Purpura (TTP) on p102, what percentage is due to autoantibodies (IgG) against ADAMTS-13, which two drugs are listed under idiopathic/acquired causes, and what percentage is congenital?",
    "Autoantibodies (IgG) against ADAMTS-13: 95%; Drugs: ticlopidine and clopidogrel; Congenital: 5%",
    [
        "Autoantibodies (IgM) against ADAMTS-13: 50%; Drugs: aspirin and heparin; Congenital: 50%",
        "Autoantibodies (IgG) against ADAMTS-13: 5%; Drugs: warfarin and dabigatran; Congenital: 95%",
        "Autoantibodies (IgA) against ADAMTS-13: 75%; Drugs: methyldopa and penicillin; Congenital: 25%",
    ],
    "TTP Causes on p102: • Idiopathic/acquired: – Autoantibodies (IgG) against ADAMTS-13 (95%), – Drugs: Ticlopidine, clopidogrel. • Congenital (5%).")

add(S6, 102, "recall",
    "Under Pathophysiology of TTP on p102, what is the normal physiological role of ADAMTS-13?",
    "ADAMTS-13 → cleaves vWF → hemostasis",
    [
        "ADAMTS-13 → polymerizes fibrinogen → clot retraction",
        "ADAMTS-13 → activates plasminogen → fibrinolysis",
        "ADAMTS-13 → anchors CD55 and CD59 → complement inhibition",
    ],
    "Physiology on p102: ADAMTS-13 → Cleaves vWF → Hemostasis.")

add(S6, 102, "recall",
    "In the TTP Pathogenesis flowchart on p102, what is the cascade triggered by IgG autoantibodies against ADAMTS-13?",
    "IgG autoantibodies against ADAMTS-13 → Failure to cleave vWF → Accumulates in circulation → branches into MAHA and Thrombosis",
    [
        "IgG autoantibodies against ADAMTS-13 → Excessive cleavage of vWF → Depletion of vWF → Mucosal bleeding",
        "IgG autoantibodies against ADAMTS-13 → Fc-mediated splenic phagocytosis → Spherocytosis and splenomegaly",
        "IgG autoantibodies against ADAMTS-13 → Alternate complement activation → Isolated renal cortical necrosis",
    ],
    "Pathogenesis on p102: IgG autoantibodies against ADAMTS-13 → Failure to cleave vWF → Accumulates in circulation → MAHA and Thrombosis.")

add(S6, 102, "recall",
    "In the TTP pathogenesis flowchart on p102, Thrombosis leads to Ischemia affecting which three organ systems (and which one is marked 'Predominately')?",
    "CNS manifestations (predominately), GIT manifestations and CVS manifestations",
    [
        "Renal manifestations (predominately), pulmonary manifestations and hepatic manifestations",
        "Musculoskeletal manifestations (predominately), cutaneous manifestations and ocular manifestations",
        "Splenic manifestations (predominately), endocrine manifestations and bone marrow manifestations",
    ],
    "In the p102 flowchart: Thrombosis → Ischemia → CNS manifestations (Predominately), GIT manifestations, CVS manifestations.")

add(S6, 102, "management",
    "What are the two bullets listed under Management of TTP on p102?",
    "1) Plasmapheresis + steroid + rituximab; 2) Monitor ADAMTS-13 levels",
    [
        "1) Platelet transfusion + emergency splenectomy; 2) Monitor serum ferritin levels",
        "1) Isotonic saline + bowel rest; 2) Monitor stool Shiga toxin titers",
        "1) Allogeneic stem cell transplant + ravulizumab; 2) Monitor CD55/CD59 levels",
    ],
    "Management of TTP on p102: • Plasmapheresis + steroid + rituximab. • Monitor ADAMTS-13 levels.")

add(S6, 102, "recall",
    "In the 'Types of Fragmentation Hemolysis' table at the bottom of p102, what are the Pathogenesis and Platelet count for Row 1 ('MAHA/march hemolysis')?",
    "Pathogenesis: HUS; Platelet: Low",
    [
        "Pathogenesis: Prosthetic valves; Platelet: Normal",
        "Pathogenesis: Kasabach–Merritt syndrome; Platelet: High",
        "Pathogenesis: PNH; Platelet: Normal",
    ],
    "Row 1 of Fragmentation Hemolysis table on p102: Type: MAHA/march hemolysis → Pathogenesis: HUS → Platelet: Low.")

add(S6, 102, "recall",
    "In the 'Types of Fragmentation Hemolysis' table on p102, what are the Pathogenesis and Platelet count for Row 2 ('Cardiac')?",
    "Pathogenesis: Prosthetic valves related macroangiopathic hemolysis; Platelet: Normal",
    [
        "Pathogenesis: HUS microangiopathic hemolysis; Platelet: Low",
        "Pathogenesis: Infective endocarditis autoimmune lysis; Platelet: Low",
        "Pathogenesis: Cavernous hemangioma + 2° DIC; Platelet: High",
    ],
    "Row 2 of Fragmentation Hemolysis table on p102: Type: Cardiac → Pathogenesis: Prosthetic valves related macroangiopathic hemolysis → Platelet: Normal.")

add(S6, 102, "recall",
    "In the 'Types of Fragmentation Hemolysis' table on p102, what are the Pathogenesis and Platelet count for Row 3 ('Consumption')?",
    "Pathogenesis: Kasabach–Merritt syndrome (cavernous hemangioma + 2° DIC); Platelet: Low",
    [
        "Pathogenesis: Prosthetic valves related macroangiopathic hemolysis; Platelet: Normal",
        "Pathogenesis: Evans syndrome (warm AIHA + CVID); Platelet: Normal",
        "Pathogenesis: Heyde syndrome (aortic stenosis + acquired vWD); Platelet: High",
    ],
    "Row 3 of Fragmentation Hemolysis table on p102: Type: Consumption → Pathogenesis: Kasabach Merritt syndrome : Cavernous hemangioma + 2° DIC → Platelet: Low.")

add(S6, 102, "match",
    "Match each Type of Fragmentation Hemolysis in the bottom table on p102 to its Pathogenesis and Platelet count — 1) MAHA / march hemolysis 2) Cardiac 3) Consumption … A) Prosthetic valves related macroangiopathic hemolysis; Platelet: Normal B) Kasabach–Merritt syndrome (cavernous hemangioma + 2° DIC); Platelet: Low C) HUS; Platelet: Low",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "Table at bottom of p102: MAHA/march hemolysis → Pathogenesis: HUS, Platelet: Low; Cardiac → Pathogenesis: Prosthetic valves related macroangiopathic hemolysis, Platelet: Normal; Consumption → Pathogenesis: Kasabach Merritt syndrome (Cavernous hemangioma + 2° DIC), Platelet: Low.")

add(S6, 102, "truefalse",
    "TRUE or FALSE — in the 'Types of Fragmentation Hemolysis' table on p102, Cardiac (prosthetic valve-related macroangiopathic) hemolysis has a NORMAL platelet count, whereas MAHA/march hemolysis (HUS) and Consumption (Kasabach–Merritt syndrome) have a LOW platelet count.",
    "True — platelet count is Normal in cardiac prosthetic-valve hemolysis and Low in HUS and Kasabach–Merritt syndrome",
    [
        "True — platelet count is Normal in all three types of fragmentation hemolysis",
        "False — cardiac prosthetic-valve hemolysis causes severe thrombocytopenia while HUS has normal platelets",
        "False — Kasabach–Merritt syndrome is characterized by extreme thrombocytosis",
    ],
    "The p102 table explicitly contrasts Platelet: Low in MAHA/march hemolysis (HUS) and Consumption (Kasabach–Merritt syndrome: cavernous hemangioma + 2° DIC) with Platelet: Normal in Cardiac (prosthetic valves related macroangiopathic hemolysis).")


GUIDES = {
    S1: (
        "Overview & PNH Physiology",
        "Non-immune hemolysis comprises infections (malaria, Babesia, Oroya fever, C. perfringens), drugs/toxins (dapsone, primaquine), PNH and fragmentation hemolysis.\n"
        "PNH causes chronic intravascular hemolysis with acute exacerbations and affects all 3 blood lineages due to an acquired X-linked PIGA gene mutation.\n"
        "PIGA codes for GPI anchor protein (anchoring CD55/DAF and CD59/MIRL to prevent complement attack), neutrophil alkaline phosphatase, and UPAR; PNH is the sole acquired intracorpuscular hemolytic anemia.",
    ),
    S2: (
        "PNH: Pathogenesis & Clinical Features",
        "PIGA mutation leads to CD55/CD59-deficient PNH III RBC lysis, ↓ neutrophil alkaline phosphatase (seen in CML and PNH), and thrombosis from defective UPAR and NO scavenging.\n"
        "Sleep-induced acidotic pH triggers nocturnal hemoglobinuria/hemosiderinuria with high-colored morning urine.\n"
        "Hepatic vein thrombosis (m/c) causes Budd–Chiari syndrome (also caused by PCRV); pancytopenia (hypercellular marrow m/c) and the 25/10 aplastic anemia rule (plus rare AML progression) are classic.",
    ),
    S3: (
        "PNH: Investigations & Treatment",
        "Flow cytometry is the investigation of choice (detects PNH III RBC percentage; >50% is significant); Coombs test is negative and Ham's test is not used.\n"
        "Centrifuged urine supernatant is clear in hematuria (RBCs) and high-colored in Hb/myoglobinuria; after resting 3–6 hours, myoglobin clears (T₁/₂ 3–6 h) while Hb stays dark.\n"
        "Bone marrow involvement is treated with allogeneic HSCT; hemoglobinuria/thrombosis is treated with anti-C5 antibodies (ravulizumab > eculizumab) plus meningococcal vaccination.",
    ),
    S4: (
        "Fragmentation: MAHA, TMA & HUS vs TTP",
        "Fragmentation hemolysis combines MAHA (small-vessel endothelial injury → large vWF multimers → Gp Ib-IX & Gp VI platelet plug → thrombocytopenia + RBC fragmentation) and TMA.\n"
        "TMA is small-vessel renal disease caused by HUS (most important), catastrophic APS, diffuse scleroderma, HELLP and malignant hypertension.\n"
        "HUS targets renal capillaries causing a triad (MAHA, thrombocytopenia, renal failure); TTP targets brain/GIT vessels causing lacunar stroke and a pentad (adding fever and neurological signs; renal failure is rare).",
    ),
    S5: (
        "HUS: Childhood (D⁺) vs Adult (D⁻)",
        "Childhood HUS (<5 yr, D⁺, benign, good prognosis) follows bloody diarrhea: 90% from EHEC O157:H7 (m/c, non-fermenter on Sorbitol MacConkey) or Shigella dysenteriae, and 10% from S. pneumoniae neuraminidase.\n"
        "Childhood HUS blood work shows schistocytes, ↑↑ LDH, –ve Coombs, ↑ indirect bilirubin, ↓ haptoglobin and normal PT/APTT; Rx is supportive (saline, bowel rest; avoid antibiotics).\n"
        "Adult HUS (D⁻/atypical, leads to ESRD) stems from alternate complement mutations (CFH m/c, CFB worst prognosis, MCP good prognosis) or sporadic causes; Rx is plasmapheresis within 24 h and rituximab/eculizumab.",
    ),
    S6: (
        "TTP & Types of Fragmentation Hemolysis",
        "TTP is 95% acquired (IgG autoantibodies against ADAMTS-13, or ticlopidine/clopidogrel) and 5% congenital.\n"
        "Failure to cleave vWF causes vWF accumulation, MAHA and microvascular thrombosis/ischemia (predominantly CNS, plus GIT/CVS); Rx is plasmapheresis + steroid + rituximab while monitoring ADAMTS-13.\n"
        "Fragmentation hemolysis types: MAHA/march hemolysis (HUS, low platelets), Cardiac (prosthetic valve macroangiopathic, normal platelets) and Consumption (Kasabach–Merritt cavernous hemangioma + 2° DIC, low platelets).",
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
