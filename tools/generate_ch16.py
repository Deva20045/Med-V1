#!/usr/bin/env python3
"""Generate Chapter 16 Immune Mediated Hemolytic Anemia (Book p92–96)."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 16
TITLE = "Immune Mediated Hemolytic Anemia"
PAGES = "92-96"

S1 = "Classification of Immune Hemolysis & Coombs Test"
S2 = "Monovalent DAT Subtyping & Warm vs Cold AIHA Etiology"
S3 = "Warm vs Cold AIHA: Pathogenesis, Clinical Features & Smear"
S4 = "Warm vs Cold AIHA: Treatment, Evans Syndrome & Spherocytes"
S5 = "Paroxysmal Cold Hemoglobinuria & Drug-Induced Hemolysis"

RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    rng = random.Random(16000 + CHAPTER * 10000 + len(RAW))
    rng.shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2, f"truefalse True count: {stem}"
        assert sum(o.startswith("False") for o in options) == 2, f"truefalse False count: {stem}"
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p92 — Classification of Immune Hemolytic Anemia & Coombs Test
add(S1, 92, "recall",
    "At the top of p92, acquired hemolytic anemia first divides into:",
    "Immune hemolytic and non-immune hemolytic",
    [
        "Megaloblastic and normoblastic",
        "Hemoglobinopathies and enzymopathies",
        "Sideroblastic and thalassemic",
    ],
    "The opening p92 flowchart divides Acquired hemolytic anemia into Immune hemolytic and Non-immune hemolytic.")

add(S1, 92, "recall",
    "In the p92 classification chart, 'Immune hemolytic' anemia branches into which three categories?",
    "Autoimmune, alloimmune and drug induced",
    [
        "Fragmentation, PNH and sepsis",
        "Warm, cold and mechanical",
        "Intracorpuscular, membrane-defective and enzymopathic",
    ],
    "Immune hemolytic branches into Autoimmune, Alloimmune, and Drug induced.")

add(S1, 92, "recall",
    "Under the 'Autoimmune' branch on p92, what immunoglobulin class mediates Warm antibody AIHA, Cold antibody AIHA, and Paroxysmal cold hemoglobinuria (PCH) respectively?",
    "Warm antibody: IgG; Cold antibody: IgM; Paroxysmal cold hemoglobinuria (PCH): IgG",
    [
        "Warm antibody: IgM; Cold antibody: IgG; Paroxysmal cold hemoglobinuria (PCH): IgA",
        "Warm antibody: IgG; Cold antibody: IgM; Paroxysmal cold hemoglobinuria (PCH): IgM",
        "Warm antibody: IgA; Cold antibody: IgG; Paroxysmal cold hemoglobinuria (PCH): IgE",
    ],
    "Autoimmune on p92: Warm antibody : IgG; Cold antibody : IgM; Paroxysmal cold hemoglobinuria (PCH) : IgG.")

add(S1, 92, "match",
    "Match each immune hemolytic condition on p92 to its printed antibody class — 1) Warm antibody AIHA 2) Cold antibody AIHA 3) Paroxysmal cold hemoglobinuria (PCH) and Hemolytic disease of newborn … A) IgM B) IgG (warm autoantibody) C) IgG (PCH / HDN)",
    "1-B, 2-A, 3-C",
    [
        "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B",
    ],
    "On p92: Warm antibody = IgG; Cold antibody = IgM; PCH = IgG; Hemolytic disease of newborn = IgG.")

add(S1, 92, "recall",
    "Under the 'Alloimmune' branch on p92, which two conditions are listed, and which immunoglobulin is noted beside Hemolytic disease of the newborn?",
    "Hemolytic disease of newborn (IgG) and hemolytic transfusion reaction",
    [
        "Warm antibody AIHA (IgG) and cold antibody AIHA (IgM)",
        "Paroxysmal cold hemoglobinuria (IgG) and drug-induced hemolysis",
        "Atypical HUS and thrombotic thrombocytopenic purpura",
    ],
    "Alloimmune on p92 lists: Hemolytic disease of newborn : IgG, and Hemolytic transfusion reaction.")

add(S1, 92, "fillup",
    "According to the note on p92, the IgG antibody of paroxysmal cold hemoglobinuria (PCH) is called the ____ antibody.",
    "Donath Landsteiner",
    ["Paul–Bunnell", "Forssman", "Anti-intrinsic factor"],
    "Note on p92: IgG antibody of PCH : Donath Landsteiner antibody.")

add(S1, 92, "recall",
    "Under Autoimmune Hemolytic Anemia (AIHA) on p92, rapidly progressive anemia points to hemolytic anemia (suggestive of an acquired cause) and occurs at which site type?",
    "Extravascular",
    [
        "Purely intravascular",
        "Intramedullary only",
        "Renal glomerular capillaries",
    ],
    "Autoimmune Hemolytic Anemia (AIHA) on p92: Rapidly progressive anemia → Hemolytic anemia (Suggestive of acquired); Extravascular.")

add(S1, 92, "recall",
    "What is the primary diagnostic purpose of the Coombs test stated on p92?",
    "Differentiates immune and non-immune anemia",
    [
        "Differentiates megaloblastic and normoblastic macrocytosis",
        "Quantifies bone marrow iron stores in microcytic anemia",
        "Measures osmotic fragility of spectrin-deficient erythrocytes",
    ],
    "Coombs test: Differentiates immune & non immune anemia.")

add(S1, 92, "recall",
    "In the Coombs test flowchart on p92, what is the alternate name (AKA) for the Direct Coombs test, and what does it detect?",
    "Direct antiglobulin test (DAT); detects antibodies on the surface of the RBC",
    [
        "Indirect antiglobulin test (IAT); detects free antibodies in plasma",
        "Donath–Landsteiner test; detects complement C5b-9 in urine",
        "Ham acid hemolysis test; detects GPI-anchor deficiency on leukocytes",
    ],
    "Direct coombs test → AKA Direct antiglobulin test (DAT): Antibodies on the surface of RBC.")

add(S1, 92, "truefalse",
    "TRUE or FALSE — on p92, the Indirect Coombs test detects antibodies in circulation and is noted as not reliable due to the doubtful significance of the antibodies.",
    "True — Indirect Coombs test detects circulating antibodies and is noted as not reliable due to their doubtful significance",
    [
        "True — Indirect Coombs test detects antibodies bound to the RBC surface and is the gold standard for AIHA",
        "False — Indirect Coombs test is more reliable than Direct Coombs test for diagnosing warm AIHA",
        "False — Indirect Coombs test detects only C3d bound to splenic macrophages",
    ],
    "Indirect coombs test: Antibodies in circulation (Not reliable d/t doubtful significance of the antibodies).")

add(S1, 92, "recall",
    "In the Direct Coombs test procedure on p92, patient RBCs coated with antibodies are mixed with which reagent to detect antibodies on the RBC surface?",
    "Polyvalent anti-human immunoglobulin",
    [
        "Monoclonal anti-P antigen IgM",
        "Acidified serum with sucrose",
        "Potassium ferrocyanide reagent",
    ],
    "RBCs coated with antibodies + Polyvalent anti human immunoglobulin (Detects antibodies on the RBC surface).")

add(S1, 92, "recall",
    "In the Direct Coombs test flowchart on p92, what happens when the polyvalent reagent reacts with antibody (agglutination) versus when it does not react?",
    "Reacts (agglutination) → Coombs test positive (3+, 4+) → Immune hemolytic anemia; Does not react → Coombs test negative → Non-immune hemolytic anemia",
    [
        "Reacts (agglutination) → Non-immune hemolytic anemia; Does not react → Immune hemolytic anemia",
        "Reacts (hemolysis) → Coombs test negative; Does not react → Coombs test positive (3+, 4+)",
        "Reacts (agglutination) → Sideroblastic anemia; Does not react → Thalassemia trait",
    ],
    "Left branch: Reacts with antibody (Agglutination) → Coomb's test positive (3+, 4+) → Immune hemolytic anemia. Right branch: Does not react with antibody → Coomb's test negative → Non immune hemolytic anemia.")

add(S1, 92, "recall",
    "Once Immune hemolytic anemia is confirmed by a positive polyvalent Direct Coombs test (3+, 4+), what reagent is added next at the bottom of p92?",
    "Monovalent antihuman immunoglobulin (Anti-IgG, anti-C3d)",
    [
        "Polyvalent anti-rabbit complement (Anti-C1q, anti-C9)",
        "Supravital brilliant cresyl blue dye",
        "Osmotic saline gradient (0.9% to 0.1%)",
    ],
    "Below Immune hemolytic anemia on p92: Add monovalent antihuman immunoglobin (Anti IgG, anti C3d).")

# ---------------------------------------------------------------------------
# Book p93 — Monovalent DAT Subtyping & Warm vs Cold AIHA Etiology
add(S2, 93, "recall",
    "At the top of p93, when monovalent antihuman immunoglobulin shows 'Anti-IgG +ve, Anti-C3d ±', which two possibilities are indicated?",
    "Warm antibody AIHA, or Drug-induced (when negative)",
    [
        "Cold antibody AIHA, or Paroxysmal cold hemoglobinuria",
        "Hereditary spherocytosis, or G6PD deficiency",
        "Paroxysmal nocturnal hemoglobinuria, or Atypical HUS",
    ],
    "Under Anti IgG +ve / Anti C3d ± on p93: Warm antibody AIHA, and -ve → Drug induced.")

add(S2, 93, "recall",
    "At the top of p93, when monovalent antihuman immunoglobulin shows 'Anti-IgG –ve, Anti-C3d +ve', what are the three downstream diagnostic branches?",
    "1) Cold antibody AIHA, 2) Donath–Landsteiner (DL) test +ve → PCH, and 3) Drug-induced AIHA (Ab +ve, DL –ve)",
    [
        "1) Warm antibody AIHA, 2) Evans syndrome, and 3) Hemolytic disease of the newborn",
        "1) Thalassemia trait, 2) Sideroblastic anemia, and 3) Anemia of chronic disease",
        "1) HUS/TTP, 2) Sepsis, and 3) Mismatched blood transfusion",
    ],
    "Under Anti IgG -ve / Anti C3d +ve on p93: Cold antibody AIHA; Donath Landsteiner (DL) test +ve → PCH; Drug induced AIHA (• Ab +ve, • DL -ve).")

add(S2, 93, "fillup",
    "According to the note on p93, a history of ____ can cause a false-positive Coombs test.",
    "Multiple blood transfusions",
    ["Oral iron therapy", "High-dose vitamin C", "Recent splenectomy"],
    "Note on p93: Multiple blood transfusions → False positive coomb's test.")

add(S2, 93, "recall",
    "Under 'Warm & Cold Hemolytic Anemia (AIHA)' on p93, what is the sex preponderance, and which type of AIHA is marked most common (m/c)?",
    "Female > Male (F > M); Warm autoimmune hemolytic anemia is most common (m/c)",
    [
        "Male > Female (M > F); Cold autoimmune hemolytic anemia is most common (m/c)",
        "Equal sex incidence (F = M); Paroxysmal cold hemoglobinuria is most common (m/c)",
        "Male > Female (M > F); Drug-induced AIHA is most common (m/c)",
    ],
    "On p93 above the table: F > M, and the left column header reads 'Warm autoimmune hemolytic anemia (m/c)'.")

add(S2, 93, "recall",
    "In the p93 comparison table, which immunoglobulin class mediates Warm AIHA versus Cold AIHA?",
    "Warm AIHA: IgG; Cold AIHA: IgM",
    [
        "Warm AIHA: IgM; Cold AIHA: IgG",
        "Warm AIHA: IgA; Cold AIHA: IgE",
        "Warm AIHA: IgG; Cold AIHA: IgA",
    ],
    "Immunoglobin row on p93: Warm AIHA = IgG; Cold AIHA = IgM.")

add(S2, 93, "numeric",
    "In the p93 comparison table, what are the reaction temperatures listed for Warm AIHA versus Cold AIHA?",
    "Warm AIHA: 37 °C; Cold AIHA: 0–4 °C",
    [
        "Warm AIHA: 40 °C; Cold AIHA: 15–25 °C",
        "Warm AIHA: 0–4 °C; Cold AIHA: 37 °C",
        "Warm AIHA: 25 °C; Cold AIHA: –20 °C",
    ],
    "Temperature row on p93: Warm AIHA = 37 °C; Cold AIHA = 0–4 °C.")

add(S2, 93, "recall",
    "In the Incidence row of the p93 table, how are the clinical courses of Warm AIHA and Cold AIHA contrasted?",
    "Warm AIHA: Rapidly progressive subacute (1–2 months); Cold AIHA: Chronic indolent",
    [
        "Warm AIHA: Chronic indolent (years); Cold AIHA: Hyperacute fulminant (hours)",
        "Warm AIHA: Self-limiting (days); Cold AIHA: Rapidly progressive subacute (1–2 months)",
        "Warm AIHA: Congenital lifelong; Cold AIHA: Acute post-transfusion only",
    ],
    "Incidence row on p93: Warm AIHA = Rapidly progressive subacute (1–2 months); Cold AIHA = Chronic indolent.")

add(S2, 93, "match",
    "Match each feature in the p93 comparison table to Warm AIHA and Cold AIHA — 1) Immunoglobulin class 2) Optimal reaction temperature 3) Clinical incidence/course … A) Warm: 37 °C; Cold: 0–4 °C B) Warm: Rapidly progressive subacute (1–2 months); Cold: Chronic indolent C) Warm: IgG; Cold: IgM",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "Table on p93: Immunoglobin — Warm IgG vs Cold IgM; Temperature — Warm 37°C vs Cold 0–4°C; Incidence — Warm rapidly progressive subacute (1–2 months) vs Cold chronic indolent.")

add(S2, 93, "numeric",
    "In the Etiology row for Warm AIHA on p93, what percentage of cases are idiopathic?",
    "50%",
    ["10%", "25%", "90%"],
    "Warm AIHA Etiology: • Idiopathic : 50 %.")

add(S2, 93, "recall",
    "Under secondary causes of Warm AIHA on p93, what three disorders are grouped together in item 1?",
    "SLE, CLL and HIV",
    [
        "Waldenström's macroglobulinemia, EBV and CMV",
        "Multiple myeloma, Mycoplasma and parvovirus B19",
        "Hodgkin lymphoma, hepatitis B and syphilis",
    ],
    "Warm AIHA Secondary causes: 1. SLE, CLL, HIV.")

add(S2, 93, "recall",
    "Which four autoimmune diseases are listed under item '2. Auto immune' in the secondary causes of Warm AIHA on p93?",
    "Rheumatoid arthritis, polyarteritis nodosa, inflammatory bowel disease and scleroderma",
    [
        "Addison's disease, Type 1 diabetes mellitus, vitiligo and Graves' disease",
        "Myasthenia gravis, multiple sclerosis, Goodpasture syndrome and pemphigus",
        "Ankylosing spondylitis, reactive arthritis, gout and Sjögren's syndrome",
    ],
    "Warm AIHA Secondary causes — 2. Autoimmune: Rheumatoid arthritis, Polyarteritis nodosa, Inflammatory bowel disease, Scleroderma.")

add(S2, 93, "recall",
    "Under item '3. Drugs' in the Warm AIHA etiology column on p93, which antibiotic class is listed as 'drug dependent'?",
    "Cephalosporins",
    [
        "Macrolides",
        "Fluoroquinolones",
        "Tetracyclines",
    ],
    "Warm AIHA Drugs: – Cephalosporins (drug dependent).")

add(S2, 93, "recall",
    "Under item '3. Drugs' in the Warm AIHA etiology column on p93, how is α-methyldopa characterized and what is its clinical consequence?",
    "Drug-independent → features persist even after stopping the drug",
    [
        "Drug-dependent → hemolysis ceases within hours of stopping the drug",
        "Hapten-adsorbing → requires high-dose intravenous administration",
        "Complement-fixing IgM → active only at 0–4 °C in extremities",
    ],
    "Warm AIHA Drugs: – α-methyl dopa (drug independent) → Features even after stopping drug.")

add(S2, 93, "fillup",
    "In the Cold AIHA etiology column on p93, the idiopathic form is called ____.",
    "Cold agglutinin disease",
    ["Paroxysmal cold hemoglobinuria", "Evans syndrome", "Marchiafava–Micheli syndrome"],
    "Cold AIHA Etiology: • Idiopathic : Cold agglutinin disease.")

add(S2, 93, "recall",
    "What is secondary cause #1 of Cold AIHA on p93, and what molecular mutation is specified?",
    "Waldenström's macroglobulinemia: monoclonal IgM gammopathies with MYD88 mutation",
    [
        "Chronic lymphocytic leukemia: monoclonal IgG gammopathy with TP53 deletion",
        "Multiple myeloma: monoclonal IgA gammopathy with t(11;14) translocation",
        "Polycythemia vera: clonal erythrocytosis with JAK2 V617F mutation",
    ],
    "Cold AIHA Secondary causes: 1. Waldenstrom's macroglobulinemia : monoclonal IgM gammopathies with myd 88 mutation.")

add(S2, 93, "recall",
    "Under secondary causes of Cold AIHA on p93, besides Waldenström's macroglobulinemia (#1) and lymphoma (#2), which four infections are listed under #3?",
    "Infectious mononucleosis, EBV, cytomegalovirus and Mycoplasma pneumoniae",
    [
        "HIV, hepatitis C, tertiary syphilis and parvovirus B19",
        "Malaria, babesiosis, Bartonella and Clostridium perfringens",
        "Tuberculosis, brucellosis, typhoid and visceral leishmaniasis",
    ],
    "Cold AIHA Secondary causes: 2. Lymphoma; 3. Infections: – Infectious mononucleosis, – EBV, – Cytomegalovirus, – Mycoplasma pneumonia.")

add(S2, 93, "fillup",
    "Under secondary causes of Cold AIHA on p93, item '4. Drugs' specifically lists ____.",
    "Lenalidomide",
    ["α-methyldopa", "Cephalosporins", "Quinidine"],
    "Cold AIHA Secondary causes: 4. Drugs : Lenalidomide.")

add(S2, 93, "oddoneout",
    "Pick the ODD ONE OUT — which of the following is listed under secondary causes of Cold AIHA rather than Warm AIHA on p93?",
    "Mycoplasma pneumoniae",
    [
        "Systemic lupus erythematosus (SLE)",
        "Polyarteritis nodosa",
        "Scleroderma",
    ],
    "SLE, polyarteritis nodosa, and scleroderma are secondary causes of Warm AIHA on p93, whereas Mycoplasma pneumoniae is a secondary infectious cause of Cold AIHA.")

# ---------------------------------------------------------------------------
# Book p94 — Warm vs Cold AIHA: Pathogenesis, Destruction Site, Features & Smear
add(S3, 94, "recall",
    "In the Pathogenesis row on p94, what is the exact sequence of events in Warm autoimmune hemolytic anemia?",
    "Splenic macrophage has receptor for Fc portion of RBC → Pan-agglutination → Extravascular hemolysis",
    [
        "RBC agglutination in extremities with IgM → Recognized by Kupffer cells → Intravascular hemolysis",
        "Polyclonal IgG binds P-antigen at 4°C → Complement MAC lysis at 37°C → Intravascular hemolysis",
        "ADAMTS13 deficiency → Ultra-large vWF multimers shear RBCs → Microangiopathic hemolysis",
    ],
    "Warm AIHA Pathogenesis on p94: Splenic macrophage has receptor for Fc portion of RBC → Pan agglutination → Extravascular hemolysis.")

add(S3, 94, "recall",
    "In the Pathogenesis row on p94, where does IgM-mediated RBC agglutination occur in Cold autoimmune hemolytic anemia, and which cells recognize the coated RBCs?",
    "RBC agglutination occurs in the peripheral circulation/extremities with IgM; recognized by Kupffer cells",
    [
        "RBC agglutination occurs in the splenic cords at 37°C with IgG; recognized by red-pulp macrophages",
        "RBC agglutination occurs in the renal medulla with IgA; recognized by mesangial cells",
        "RBC agglutination occurs in the bone marrow sinusoids; recognized by megakaryocytes",
    ],
    "Cold AIHA Pathogenesis on p94: RBC agglutination in the peripheral circulation/extremities with IgM. Recognised by Kupffer cells.")

add(S3, 94, "recall",
    "After Kupffer cell recognition in Cold AIHA on p94, what is the relative contribution of extravascular versus intravascular hemolysis?",
    "Extravascular hemolysis (predominantly) and intravascular hemolysis (minimal)",
    [
        "Intravascular hemolysis (exclusively) with no extravascular hemolysis",
        "Equal 50:50 intravascular and splenic extravascular hemolysis",
        "Intramedullary hemolysis only with no peripheral RBC destruction",
    ],
    "Cold AIHA Pathogenesis on p94: Recognised by Kupffer cells → Extravascular hemolysis (predominantly). Intravascular hemolysis (minimal).")

add(S3, 94, "match",
    "Match Warm AIHA, Cold AIHA, and Cold AIHA with MAC formation on p94 to their site or mode of RBC destruction — 1) Warm autoimmune hemolytic anemia 2) Cold autoimmune hemolytic anemia (extravascular) 3) Cold AIHA with C5–C9 membrane attack complex … A) Liver (Kupffer cells) B) Intravascular hemolysis C) Spleen (splenic macrophages)",
    "1-C, 2-A, 3-B",
    [
        "1-A, 2-C, 3-B",
        "1-C, 2-B, 3-A",
        "1-B, 2-A, 3-C",
    ],
    "RBC destruction site row on p94: Warm AIHA = Spleen; Cold AIHA = Liver (and intravascular hemolysis when C5–C9 MAC is activated).")

add(S3, 94, "recall",
    "Which four clinical features bullets are listed for Warm autoimmune hemolytic anemia in the p94 table?",
    "1) Anemia, spherocytosis, reticulocytosis; 2) Splenomegaly (moderate); 3) Jaundice; 4) Urobilinogen (+)",
    [
        "1) Acrocyanosis; 2) Hepatomegaly; 3) Hemoglobinuria; 4) Hemosiderinuria",
        "1) Pancytopenia; 2) Beefy-red glossitis; 3) Dorsal column loss; 4) Urine MMA (+)",
        "1) Koilonychia; 2) Pica; 3) Esophageal webs; 4) Absent marrow iron",
    ],
    "Clinical features of Warm AIHA on p94: • Anemia, spherocytosis, reticulocytosis, • Splenomegaly (moderate), • Jaundice, • Urobilinogen (+).")

add(S3, 94, "fillup",
    "In the Clinical features row on p94, the characteristic clinical feature listed for Cold autoimmune hemolytic anemia is ____.",
    "Acrocyanosis",
    ["Koilonychia", "Erythromelalgia", "Kayser–Fleischer rings"],
    "Clinical features of Cold AIHA on p94: Acrocyanosis.")

add(S3, 94, "recall",
    "In the Peripheral smear row on p94, which four cell types are labelled across the two photomicrographs under Warm AIHA?",
    "Fragmented RBC, spherocyte (variable), nucleated RBC and polychromatic RBC (blue tinge)",
    [
        "Target cells, pencil cells, tear-drop cells and ring sideroblasts",
        "Sickle cells, Howell-Jolly bodies, Cabot rings and bite cells",
        "Macro-ovalocytes, hypersegmented neutrophils, acanthocytes and burr cells",
    ],
    "Peripheral smear images on p94 under Warm AIHA label: Fragmented RBC, Spherocyte (variable), Nucleated RBC, and Polychromatic RBC (blue tinge).")

add(S3, 94, "recall",
    "What is labelled in the peripheral smear photomicrograph under Cold autoimmune hemolytic anemia on p94?",
    "Agglutinated RBC",
    [
        "Uniform spherocytes",
        "Ring sideroblasts",
        "Rouleaux stacks with plasma cells",
    ],
    "The Cold AIHA peripheral smear image on p94 is labelled 'Agglutinated RBC'.")

# ---------------------------------------------------------------------------
# Book p95 — Warm vs Cold AIHA: Smear cont., Treatment, Evans Syndrome & Spherocytes
add(S4, 95, "fillup",
    "At the top of p95 under Warm AIHA peripheral smear, ____ are noted as 'AKA fragmented RBC / helmeted RBC'.",
    "Schistocytes",
    ["Drepanocytes", "Codocytes", "Stomatocytes"],
    "Top of p95: Schistocytes : AKA fragmented RBC / helmeted RBC.")

add(S4, 95, "recall",
    "What do the two additional photomicrographs at the top of p95 under Warm AIHA illustrate?",
    "Spherocytes, and Reticulocytosis (supravital stain)",
    [
        "Ring sideroblasts (Prussian blue), and Megaloblasts",
        "Heinz bodies, and Basophilic stippling",
        "Target cells, and Rouleaux formation",
    ],
    "The two photomicrographs at the top of p95 under Warm AIHA are captioned 'Spherocytes' and 'Reticulocytosis (supravital stain)'.")

add(S4, 95, "numeric",
    "In the first-line treatment of Warm AIHA on p95, what is the exact steroid dose and duration?",
    "1 mg/kg/day × 4 weeks (then taper steroid slowly)",
    [
        "0.1 mg/kg/day × 1 week (then stop abruptly)",
        "10 mg/kg/day × 12 weeks",
        "500 mg single IV bolus only",
    ],
    "Warm AIHA Treatment on p95: • Steroids : 1 mg/kg/day × 4 wks. + Rituximab : 100 mg/m² weekly × 4 doses. • Taper steroid slowly.")

add(S4, 95, "numeric",
    "In the first-line treatment of Warm AIHA on p95, what is the exact Rituximab dose and schedule combined with steroids?",
    "100 mg/m² weekly × 4 doses",
    [
        "375 mg/m² daily × 10 doses",
        "10 mg/m² monthly × 12 doses",
        "1000 mg once every 6 months",
    ],
    "Warm AIHA Treatment on p95: Steroids : 1 mg/kg/day × 4 wks. + Rituximab : 100 mg/m² weekly × 4 doses.")

add(S4, 95, "management",
    "Which three medical agents and which surgical option (with its parenthetical note) are listed under 'Relapse' for Warm AIHA on p95?",
    "Rituximab, cyclophosphamide, mycophenolate mofetil, and splenectomy (ideal but not preferred)",
    [
        "Azathioprine, cyclosporine, danazol, and bone marrow transplant (first choice)",
        "Hydroxyurea, methotrexate, 6-mercaptopurine, and thymectomy (preferred)",
        "Lenalidomide, bortezomib, thalidomide, and hepatic irradiation",
    ],
    "Warm AIHA Relapse on p95: • Rituximab, • Cyclophosphamide, • Mycophenolate mofetil, • Splenectomy (Ideal but not preferred).")

add(S4, 95, "management",
    "What is the treatment listed for Cold autoimmune hemolytic anemia in the p95 table?",
    "Rituximab (best prognosis)",
    [
        "High-dose corticosteroids (1 mg/kg/day) + urgent splenectomy",
        "Oral α-methyldopa + warm blood transfusion only",
        "Intramuscular hydroxycobalamin + folic acid",
    ],
    "Cold AIHA Treatment on p95: • Rituximab (Best prognosis).")

add(S4, 95, "recall",
    "In the Note at the bottom of p95, what two hematologic components define Evans syndrome (item a)?",
    "Warm autoimmune hemolytic anemia + thrombocytopenia",
    [
        "Cold agglutinin disease + neutropenia",
        "Microangiopathic hemolytic anemia + thrombocytosis",
        "Paroxysmal nocturnal hemoglobinuria + aplastic anemia",
    ],
    "Note on p95 — Evans syndrome: a. Warm autoimmune hemolytic anemia + thrombocytopenia.")

add(S4, 95, "recall",
    "In the Note at the bottom of p95, Evans syndrome is associated with which immunodeficiency (item b)?",
    "Common variable immunodeficiency (CVID)",
    [
        "Severe combined immunodeficiency (SCID)",
        "X-linked agammaglobulinemia (Bruton's)",
        "Chédiak–Higashi syndrome",
    ],
    "Note on p95 — Evans syndrome: b. Associated with common variable immunodeficiency (CVID).")

add(S4, 95, "recall",
    "According to the Note on p95, which four conditions are listed under 'Spherocytes are seen in', and which one specifically has 'uniform spherocytes'?",
    "a. Hereditary spherocytes (uniform spherocytes), b. G6PD deficiency, c. Transfusion reaction, and d. CuSO₄ poisoning",
    [
        "a. Thalassemia trait (uniform spherocytes), b. Iron deficiency, c. Lead poisoning, and d. Scurvy",
        "a. Sickle cell anemia (uniform spherocytes), b. Pyruvate kinase deficiency, c. PNH, and d. Malaria",
        "a. Pernicious anemia (uniform spherocytes), b. Folate deficiency, c. MDS, and d. Aplastic anemia",
    ],
    "Note on p95 — Spherocytes are seen in: a. Hereditary spherocytes (uniform spherocytes), b. G6PD deficiency, c. Transfusion reaction, d. CuSO4 poisoning.")

add(S4, 95, "oddoneout",
    "Pick the ODD ONE OUT — which of the following is NOT listed under 'Spherocytes are seen in' at the bottom of p95?",
    "Lead poisoning",
    [
        "Hereditary spherocytosis (uniform spherocytes)",
        "G6PD deficiency",
        "CuSO₄ poisoning",
    ],
    "The p95 note lists spherocytes in: a. Hereditary spherocytes (uniform spherocytes), b. G6PD deficiency, c. Transfusion reaction, and d. CuSO4 poisoning. Lead poisoning causes basophilic stippling and sideroblastic anemia.")

add(S4, 95, "fillup",
    "The final bullet in the p95 Note states that ____ activation happens in cold agglutinin disease.",
    "C3b",
    ["FcγR", "IgE", "ADAMTS13"],
    "Bottom bullet on p95: • C3b activation happens in cold agglutinin disease.")

# ---------------------------------------------------------------------------
# Book p96 — Paroxysmal Cold Hemoglobinuria (PCH) & Drug Induced Hemolysis
add(S5, 96, "recall",
    "At the top of p96, Paroxysmal Cold Hemoglobinuria (PCH) presents with which type of hemolysis and Coombs test status?",
    "Acute intravascular hemolysis; Coombs test +ve",
    [
        "Chronic extravascular hemolysis in the spleen; Coombs test –ve",
        "Insidious intramedullary hemolysis; Coombs test –ve",
        "Mechanical fragmentation hemolysis; Coombs test –ve",
    ],
    "Paroxysmal Cold Hemoglobinuria (PCH) on p96: Acute intravascular hemolysis; Coombs test +ve.")

add(S5, 96, "recall",
    "What is the thermal biphasic pathogenesis of Paroxysmal Cold Hemoglobinuria (PCH) on p96?",
    "Polyclonal IgG antibodies → bind to P-antigen of RBC at 4°C → intravascular hemolysis at 37°C",
    [
        "Monoclonal IgM antibodies → bind to I/i antigen of RBC at 37°C → splenic sequestration at 4°C",
        "Polyclonal IgA antibodies → bind to Rh-D antigen at 37°C → hepatic extravascular lysis at 0°C",
        "Drug-dependent IgG → binds to spectrin at room temperature → marrow aplasia at 37°C",
    ],
    "Pathogenesis of PCH on p96: Polyclonal IgG antibodies → Bind to P-antigen of RBC at 4°C → Intravascular hemolysis at 37°C.")

add(S5, 96, "fillup",
    "The target RBC antigen in Paroxysmal Cold Hemoglobinuria (PCH) on p96 is the ____.",
    "P-antigen",
    ["I-antigen", "Kell antigen", "Duffy antigen"],
    "Antigen : P-antigen.")

add(S5, 96, "recall",
    "What two items are listed under 'Investigation' for Paroxysmal Cold Hemoglobinuria (PCH) on p96?",
    "1. Donath–Landsteiner test; 2. Peripheral smear (PS): features of warm & cold hemolysis",
    [
        "1. Osmotic fragility test; 2. Hb electrophoresis: elevated HbA₂",
        "1. Flow cytometry for CD55/CD59; 2. Bone marrow Prussian blue stain",
        "1. Acid elution (Kleihauer–Betke) test; 2. Sickling test with sodium metabisulfite",
    ],
    "Investigation on p96: 1. Donath Landsteiner test; 2. PS : Features of warm & cold hemolysis.")

add(S5, 96, "fillup",
    "The classic infectious association listed for Paroxysmal Cold Hemoglobinuria (PCH) on p96 is ____.",
    "Tertiary syphilis",
    ["Mycoplasma pneumoniae", "Visceral leishmaniasis", "Falciparum malaria"],
    "PCH on p96 — Associations : Tertiary syphilis.")

add(S5, 96, "management",
    "What is the treatment listed for Paroxysmal Cold Hemoglobinuria (PCH) on p96?",
    "Conservative",
    [
        "Emergency splenectomy",
        "High-dose cyclophosphamide + mycophenolate",
        "Allogeneic hematopoietic stem cell transplant",
    ],
    "PCH on p96 — Treatment : Conservative.")

add(S5, 96, "recall",
    "Under 'Drug Induced Hemolysis' on p96, what are the three main mechanisms listed?",
    "1. Autoantibody mediated, 2. Immune complex mediated, and 3. Adsorption",
    [
        "1. Oxidative Heinz-body lysis, 2. Pyrimidine antagonism, and 3. ALA synthase inhibition",
        "1. Folate antagonism, 2. DNA chain termination, and 3. CUBAM blockade",
        "1. Complement regulator deficiency, 2. Spectrin cross-linking, and 3. Ferroportin inhibition",
    ],
    "Drug Induced Hemolysis on p96 lists three mechanisms: 1. Autoantibody mediated, 2. Immune complex mediated, 3. Adsorption.")

add(S5, 96, "recall",
    "Under '1. Autoantibody mediated' drug-induced hemolysis on p96, which two drugs are bracketed as 'Drug independent', and which one is marked most common (m/c)?",
    "Methyldopa (m/c) and procainamide",
    [
        "Quinidine (m/c) and rifampicin",
        "Penicillin (m/c) and cephalosporins",
        "Isoniazid (m/c) and lenalidomide",
    ],
    "1. Autoantibody mediated: • Methyldopa (m/c) and • Procainamide are bracketed together as 'Drug independent'.")

add(S5, 96, "recall",
    "Besides methyldopa and procainamide, which three other drugs/classes are listed under '1. Autoantibody mediated' on p96, and what is noted for lenalidomide?",
    "Penicillin, cephalosporins, and lenalidomide (which causes cold autoimmune hemolysis)",
    [
        "Quinidine, rifampicin, and isoniazid (which causes cold autoimmune hemolysis)",
        "Chloramphenicol, pyrazinamide, and lead (which causes cold autoimmune hemolysis)",
        "Cytarabine, hydroxyurea, and 6-mercaptopurine (which causes cold autoimmune hemolysis)",
    ],
    "1. Autoantibody mediated also lists: • Penicillin, • Cephalosporins, • Lenalidomide : Cold autoimmune hemolysis.")

add(S5, 96, "recall",
    "Which three drugs are listed under '2. Immune complex mediated' drug-induced hemolysis on p96?",
    "Quinidine, rifampicin and isoniazid",
    [
        "Methyldopa, procainamide and lenalidomide",
        "Cytarabine, hydroxyurea and 6-mercaptopurine",
        "Triamterene, pyrimethamine and sulfasalazine",
    ],
    "2. Immune complex mediated on p96: • Quinidine, • Rifampicin, • Isoniazid.")

add(S5, 96, "recall",
    "Under '3. Adsorption' (hapten mechanism) at the bottom of p96, which drug regimen and hemolysis site are specified?",
    "High-dose penicillin : Extravascular",
    [
        "Low-dose methyldopa : Intravascular",
        "Oral lenalidomide : Intravascular",
        "Intravenous quinidine : Intramedullary",
    ],
    "3. Adsorption on p96: High dose penicillin : Extravascular.")

add(S5, 96, "match",
    "Match each mechanism of drug-induced hemolysis on p96 to its classic culprit drug(s) — 1) Autoantibody mediated (drug-independent) 2) Autoantibody mediated (cold autoimmune hemolysis) 3) Immune complex mediated 4) Adsorption (extravascular) … A) Quinidine, rifampicin and isoniazid B) High-dose penicillin C) Methyldopa (m/c) and procainamide D) Lenalidomide",
    "1-C, 2-D, 3-A, 4-B",
    [
        "1-A, 2-D, 3-C, 4-B",
        "1-C, 2-B, 3-A, 4-D",
        "1-D, 2-C, 3-B, 4-A",
    ],
    "Drug Induced Hemolysis on p96: Autoantibody drug-independent = Methyldopa (m/c) & Procainamide; Cold autoimmune = Lenalidomide; Immune complex = Quinidine, Rifampicin, Isoniazid; Adsorption = High dose penicillin (Extravascular).")


GUIDES = {
    S1: (
        "Immune Classification & Coombs Test",
        "Immune hemolytic anemia divides into autoimmune (warm IgG, cold IgM, PCH IgG/Donath–Landsteiner), alloimmune (HDN IgG, transfusion reaction) and drug-induced.\n"
        "AIHA presents as rapidly progressive extravascular hemolytic anemia; the Coombs test differentiates immune from non-immune anemia.\n"
        "Direct Coombs (DAT) uses polyvalent anti-human Ig to detect RBC surface antibodies (3+/4+ agglutination), followed by monovalent anti-IgG and anti-C3d.",
    ),
    S2: (
        "DAT Subtyping & Warm vs Cold Etiology",
        "Anti-IgG+ / C3d± indicates warm AIHA (or drug-induced if negative); Anti-IgG– / C3d+ indicates cold AIHA, PCH (DL test+) or drug-induced (Ab+, DL–); multiple transfusions cause false-positive Coombs.\n"
        "Warm AIHA (m/c, IgG, 37°C, subacute 1–2 mo) is 50% idiopathic or secondary to SLE/CLL/HIV, autoimmune diseases (RA, PAN, IBD, scleroderma) and drugs (cephalosporins, drug-independent α-methyldopa).\n"
        "Cold AIHA (IgM, 0–4°C, chronic indolent) is idiopathic cold agglutinin disease or secondary to Waldenström's (MYD88), lymphoma, infections (IM, EBV, CMV, Mycoplasma) and lenalidomide.",
    ),
    S3: (
        "Warm vs Cold: Pathogenesis & Smear",
        "Warm AIHA: splenic macrophage Fc receptors mediate pan-agglutination and extravascular destruction in the spleen, causing anemia, spherocytosis, moderate splenomegaly, jaundice and urobilinogen (+).\n"
        "Cold AIHA: IgM agglutinates RBCs in peripheral extremities (causing acrocyanosis) and Kupffer cells mediate predominantly extravascular destruction in the liver (minimal intravascular).\n"
        "Warm AIHA smear shows variable spherocytes, fragmented/nucleated/polychromatic RBCs; cold AIHA smear shows agglutinated RBCs.",
    ),
    S4: (
        "AIHA Treatment, Evans & Spherocytes",
        "Schistocytes are fragmented/helmeted RBCs; warm AIHA is treated with steroids (1 mg/kg/d × 4 wk) + rituximab (100 mg/m² weekly × 4) with slow taper, and rituximab/cyclophosphamide/MMF/splenectomy on relapse.\n"
        "Cold AIHA is treated with rituximab (best prognosis); C3b activation occurs in cold agglutinin disease.\n"
        "Evans syndrome (warm AIHA + thrombocytopenia) associates with CVID; spherocytes also occur in hereditary spherocytosis (uniform), G6PD deficiency, transfusion reaction and CuSO₄ poisoning.",
    ),
    S5: (
        "PCH & Drug-Induced Hemolysis",
        "Paroxysmal cold hemoglobinuria (PCH) causes Coombs-positive acute intravascular hemolysis: polyclonal IgG binds RBC P-antigen at 4°C and lyses cells at 37°C (Donath–Landsteiner test, tertiary syphilis, conservative Rx).\n"
        "Drug-induced autoantibody hemolysis includes drug-independent methyldopa (m/c) and procainamide, penicillin, cephalosporins and cold-reacting lenalidomide.\n"
        "Immune-complex hemolysis is caused by quinidine, rifampicin and isoniazid; adsorption hemolysis is caused by high-dose penicillin (extravascular).",
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
