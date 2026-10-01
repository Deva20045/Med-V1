#!/usr/bin/env python3
"""Generate Chapter 12 Iron Metabolism (Book p70–76), in scanned page order."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 12
TITLE = "Iron Metabolism"
PAGES = "70-76"

S1 = "Body Iron Pools and Daily Requirements"
S2 = "Dietary Iron and Intestinal Absorption"
S3 = "Iron Export, Transport and Marrow Uptake"
S4 = "Serum Iron Indices"
S5 = "Stages of Iron Deficiency"
S6 = "Iron Deficiency Causes and Calculation"
S7 = "Clinical Features of Iron Deficiency"
S8 = "IDA Blood Indices and Smear"
S9 = "Marrow, Treatment and Follow-up"
RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    random.Random(12000 + CHAPTER * 10000 + len(RAW)).shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2
        assert sum(o.startswith("False") for o in options) == 2
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p70 — total iron, storage forms, daily requirements and Hb thresholds
add(S1, 70, "numeric", "The total-body-iron estimate for males on p70 is:",
    "50 mg/kg", ["25 mg/kg", "40 mg/kg", "70 mg/kg"],
    "The page gives total body iron as 50 mg/kg in males.")
add(S1, 70, "numeric", "The corresponding total-body-iron estimate for females is:",
    "40 mg/kg", ["20 mg/kg", "50 mg/kg", "60 mg/kg"],
    "The page gives 40 mg/kg in females.")
add(S1, 70, "numeric", "Approximately what fraction of body iron is bound to haemoglobin?",
    "67%", ["27%", "3.5%", "0.08%"],
    "The composition list gives 67% bound with Hb.")
add(S1, 70, "numeric", "The storage-iron fraction is listed as 27%, with which relationship between its two forms?",
    "Ferritin > hemosiderin", ["Hemosiderin > ferritin", "Ferritin = transferrin", "Myoglobin > ferritin"],
    "The page gives 27% as storage iron and writes ferritin > hemosiderin.")
add(S1, 70, "numeric", "The transport-iron fraction bound to transferrin is approximately:",
    "0.08%", ["0.8%", "3.5%", "27%"],
    "Transport iron/transferrin is listed as 0.08%.")
add(S1, 70, "numeric", "The proportion of total-body iron assigned to myoglobin is:",
    "3.5%", ["0.08%", "2.2%", "27%"],
    "The composition list assigns 3.5% to myoglobin.")
add(S1, 70, "numeric", "The labile iron pool is given as:",
    "2.2%", ["0.08%", "3.5%", "27%"],
    "The printed proportion for the labile pool is 2.2%.")
add(S1, 70, "recall", "Which comparison between hemosiderin and ferritin matches the p70 table?",
    "Hemosiderin is less common/less available and water-insoluble; ferritin is more common/available and water-soluble", ["Hemosiderin is water-soluble and readily available; ferritin is insoluble and unavailable", "Both forms are equally common and water-insoluble", "Ferritin is found only in macrophages and hemosiderin only in plasma"],
    "The table contrasts less-common, less-available, water-insoluble hemosiderin with more-common, available, water-soluble ferritin.")
add(S1, 70, "recall", "The iron-to-protein ratio is higher in which storage form?",
    "Hemosiderin", ["Ferritin", "Transferrin", "Haemoglobin"],
    "The table shows an increased iron:protein ratio for hemosiderin and a decreased ratio for ferritin.")
add(S1, 70, "recall", "The location specifically listed for hemosiderin is:",
    "Macrophages", ["Plasma transferrin", "Erythrocyte membrane", "Gastric parietal cells"],
    "Macrophage is the location listed for hemosiderin.")
add(S1, 70, "recall", "The gold-standard stain for assessing bone-marrow iron stores is:",
    "Prussian blue", ["Romanowsky", "Sudan III", "New methylene blue"],
    "The page calls Prussian blue stain the gold standard for bone-marrow iron stores.")
add(S1, 70, "recall", "In the stain reaction described, hemosiderin with potassium ferrocyanide turns:",
    "Blue-black", ["Red-orange", "Green-yellow", "Colourless"],
    "The p70 note says hemosiderin + potassium ferrocyanide turns blue-black.")
add(S1, 70, "numeric", "A normal diet is stated to contain approximately how much iron per day?",
    "10 mg", ["1 mg", "3 mg", "20 mg"],
    "The page says a normal diet contains 10 mg iron.")
add(S1, 70, "numeric", "The total absorption fraction is listed as 10%, rising to what proportion in deficiency?",
    "20%", ["12%", "30%", "50%"],
    "Total absorption is 10%, or 20% in deficiency.")
add(S1, 70, "numeric", "The daily iron requirement shown for an adult male is:",
    "1 mg", ["0.5 mg", "2 mg", "3 mg"],
    "The adult-male requirement is 1 mg/day.")
add(S1, 70, "numeric", "The daily iron requirement shown for an adult female is:",
    "2 mg", ["0.5 mg", "1 mg", "3 mg"],
    "The adult-female requirement is 2 mg/day.")
add(S1, 70, "numeric", "The daily iron requirement listed during pregnancy is:",
    "3 mg", ["0.5 mg", "1 mg", "2 mg"],
    "The page gives 3 mg/day during pregnancy.")
add(S1, 70, "numeric", "Which pair of daily requirements is printed for children and infants, respectively?",
    "Children 0.5 mg; infant 1 mg", ["Children 1 mg; infant 0.5 mg", "Children 2 mg; infant 3 mg", "Children 3 mg; infant 2 mg"],
    "The list gives children 0.5 mg and infant 1 mg daily.")
add(S1, 70, "recall", "The boxed note on p70 repeats anaemia thresholds as pregnancy, female and male, respectively:",
    "<11, <12 and <13 g/dL", ["<10, <11 and <12 g/dL", "<12, <13 and <14 g/dL", "<13, <12 and <11 g/dL"],
    "The note lists Hb <11 in pregnancy, <12 in females and <13 in males.")

# ---------------------------------------------------------------------------
# Book p71 — dietary iron, enterocyte uptake and absorption regulators
add(S2, 71, "recall", "Which food group is listed as a source of heme iron?",
    "Chicken, meat, oyster and poultry", ["Spinach, potato, sunflower and dark chocolate", "Apple, mango, wheat and honey", "Rice, legumes, cauliflower and tea"],
    "The heme column lists chicken, meat, oyster and poultry.")
add(S2, 71, "recall", "Which food group is listed as a source of non-heme iron?",
    "Spinach, potato, sunflower and dark chocolate", ["Chicken, meat, oyster and poultry", "Pork, custard and canned meat", "Fish, shellfish and poultry"],
    "The non-heme column lists spinach, potato, sunflower and dark chocolate.")
add(S2, 71, "recall", "Dietary heme iron is shown in which oxidation state?",
    "Fe²⁺ (ferrous)", ["Fe³⁺ (ferric)", "Fe⁴⁺", "Fe⁰"],
    "The table gives heme iron as Fe2+ (ferrous).")
add(S2, 71, "recall", "Dietary non-heme iron is shown initially in which form?",
    "Fe³⁺ (ferric)", ["Fe²⁺ (ferrous)", "Fe⁰", "Haem-bound iron only"],
    "The table gives non-heme iron as Fe3+ (ferric).")
add(S2, 71, "recall", "Heme iron uptake is paired with which carrier in the duodenum?",
    "Heme carrier protein (HCP)", ["DMT1 alone", "Ferroportin 1", "Transferrin receptor 2"],
    "The table shows heme carrier protein (HCP) transporting heme iron in the duodenum.")
add(S2, 71, "recall", "Before non-heme iron absorption, duodenal cytochrome b reductase converts:",
    "Fe³⁺ to Fe²⁺", ["Fe²⁺ to Fe³⁺", "Fe³⁺ to Fe⁰", "Haem iron to transferrin"],
    "Duodenal cytochrome b reductase reduces Fe3+ to Fe2+ in enterocytes.")
add(S2, 71, "recall", "Which transporter is labelled for uptake of ferrous iron across the luminal membrane?",
    "DMT1", ["Ferroportin 1", "HCP", "Transferrin"],
    "DMT1 is labelled as the transporter for Fe2+ entry at the luminal membrane.")
add(S2, 71, "recall", "DMT is expanded in the note as:",
    "Divalent metal transporter", ["Duodenal mucosal transferrin", "Direct marrow transfer", "Dietary metal transaminase"],
    "DMT is expanded as divalent metal transporter.")
add(S2, 71, "recall", "The alternate name printed for DMT1 is:",
    "NRAMP-2", ["NRAMP-1", "TfR2", "HCP"],
    "The p71 note gives DMT as divalent metal transporter, also called NRAMP-2.")
add(S2, 71, "recall", "Which substance is listed among reducing substances that enhance iron absorption?",
    "Ascorbic acid", ["Phytate", "Tannate", "Oxalate"],
    "Listed reducing substances include sorbitol, cysteine, fructose, lactate, pyruvate, succinate and ascorbic acid.")
add(S2, 71, "recall", "Which set contains only reducing substances listed as enhancing iron absorption?",
    "Sorbitol, cysteine, fructose, lactate, pyruvate, succinate and ascorbic acid", ["Phytates, tannates and oxalates", "Ferritin, hemosiderin and transferrin", "Gastrin, histamine and acetylcholine"],
    "Those seven substances are listed as reducing substances that enhance absorption.")
add(S2, 71, "recall", "Which set contains the inhibitors of iron absorption on p71?",
    "Phytates, tannates and oxalates", ["Sorbitol, cysteine and fructose", "Lactate, pyruvate and ascorbic acid", "Ferritin, transferrin and myoglobin"],
    "The inhibitors listed are phytates, tannates and oxalates.")
add(S2, 71, "truefalse", "TRUE or FALSE — the p71 note says acidic pH enhances Fe²⁺ absorption.",
    "True — acidic pH enhances ferrous-iron absorption", ["False — acidic pH blocks Fe²⁺ absorption", "False — the note concerns only Fe³⁺", "True — but only in the colon"],
    "The note states acidic pH enhances Fe2+ absorption.")
add(S2, 71, "recall", "The p71 diagram identifies the mucosal storage form of iron as:",
    "Fe³⁺", ["Fe²⁺", "Fe⁰", "Heme-bound Fe only"],
    "The diagram's note gives the storage form of iron as Fe3+.")
add(S2, 71, "recall", "Which protein is labelled as temporary iron storage inside the duodenal enterocyte?",
    "Mucosal ferritin", ["Transferrin", "Hepcidin", "Ferroportin 1"],
    "The enterocyte diagram labels a mucosal ferritin storage pool.")
add(S2, 71, "recall", "Iron retained in an enterocyte may be lost when the cell is:",
    "Shed", ["Converted to a reticulocyte", "Phagocytosed by a neutrophil", "Stimulated by CCK-B"],
    "The absorption diagram labels iron as lost by shedding of epithelial cells.")

# ---------------------------------------------------------------------------
# Book p71–72 — export, transport, marrow and storage
add(S3, 71, "recall", "The basolateral iron-export protein shown in the enterocyte diagram is:",
    "Ferroportin 1", ["DMT1", "Heme carrier protein", "Transferrin receptor 1"],
    "Ferroportin 1 is the basolateral exporter in the diagram.")
add(S3, 71, "recall", "The liver-derived regulator shown inhibiting ferroportin-mediated iron exit is:",
    "Hepcidin", ["Hephaestin", "Ceruloplasmin", "Erythropoietin"],
    "The diagram shows hepcidin from the liver inhibiting ferroportin 1.")
add(S3, 71, "recall", "At the basolateral surface, hephaestin converts:",
    "Fe²⁺ to Fe³⁺", ["Fe³⁺ to Fe²⁺", "Fe²⁺ to Fe⁰", "Heme to globin"],
    "Hephaestin is shown converting Fe2+ to Fe3+ at the basolateral surface.")
add(S3, 71, "recall", "Plasma transferrin is shown binding how many Fe³⁺ molecules?",
    "Two", ["One", "Three", "Four"],
    "The figure notes that one transferrin binds with two Fe3+ molecules.")
add(S3, 71, "recall", "The transferrin–iron complex transports iron toward:",
    "Erythroid marrow", ["Gastric antrum", "Small-bowel lumen", "Pancreatic duct"],
    "The diagram sends the transferrin–iron complex to erythroid marrow.")
add(S3, 71, "recall", "The p71 note attributes conversion of Fe³⁺ to Fe²⁺ in the brain to:",
    "Ceruloplasmin (as printed in the source)", ["Hephaestin", "Hepcidin", "DMT1"],
    "The scanned p71 note prints 'Ceruloplasmin: converts Fe3+ → Fe2+ in brain.' This direction is preserved as printed for source coverage; verify against a trusted physiology reference before clinical use.")
add(S3, 72, "recall", "The transferrin receptors named on the surface of marrow cells are:",
    "TfR1 and TfR2", ["DMT1 and DMT2", "HCP and NRAMP-2", "Ferroportin 1 and hephaestin"],
    "The marrow-uptake diagram lists transferrin receptors TfR1 and TfR2.")
add(S3, 72, "recall", "The transferrin–iron complex is internalized into marrow-cell:",
    "Endosomes", ["Lysosomal granules only", "Mitochondria directly", "Nucleoli"],
    "The diagram shows the complex entering endosomes.")
add(S3, 72, "recall", "The endosome environment in the marrow uptake diagram is:",
    "Acidic", ["Alkaline", "Neutral and enzyme-free", "Highly oxygenated"],
    "The p72 label specifies acidic-pH endosomes.")
add(S3, 72, "recall", "In the marrow endosome, the sequence shown before iron reaches the cytoplasm is:",
    "Fe³⁺ is reduced to Fe²⁺, then transported by DMT1", ["Fe²⁺ is oxidized to Fe³⁺, then exported by ferroportin", "Heme is split into globin, then moved by HCP", "Fe³⁺ binds hepcidin, then enters through a CCK-B receptor"],
    "The diagram shows Fe3+ reduced to Fe2+, followed by DMT1 transport to cytoplasm.")
add(S3, 72, "recall", "The cytoplasmic destination is labelled the:",
    "Common iron pool", ["Heme-free zone", "Labile plasma pool", "Storage-only compartment"],
    "The marrow diagram labels cytoplasm as the common iron pool.")
add(S3, 72, "recall", "From the common iron pool, iron proceeds to mitochondria for:",
    "Heme synthesis", ["Globin degradation", "Ferritin secretion", "Bile-acid conjugation"],
    "The final step leads to mitochondria for heme synthesis.")
add(S3, 72, "recall", "Which site is included in the p72 iron-storage list?",
    "Duodenum", ["Thyroid gland", "Adrenal cortex", "Pancreatic islets"],
    "The storage list includes duodenum, bone marrow and macrophages in liver, spleen and brain.")
add(S3, 72, "recall", "The macrophage storage sites listed on p72 are:",
    "Liver, spleen and brain", ["Kidney, lung and thyroid", "Pancreas, heart and skin", "Stomach, colon and pancreas"],
    "The page lists macrophages in liver, spleen and brain.")
add(S3, 72, "recall", "The p72 DMT-1 note lists which additional metals?",
    "Cu, Mn, Mg and Zn", ["Na, K, Ca and Cl", "Co, Se, I and F", "Pb, Hg, Cd and As"],
    "The note lists Cu, Mn, Mg and Zn after DMT-1.")

# ---------------------------------------------------------------------------
# Book p72 — serum iron indices and interpretation
add(S4, 72, "recall", "Serum ferritin primarily indicates:",
    "Iron stores, noted as predominant in marrow", ["Iron circulating bound to transferrin", "Total binding capacity of transferrin", "The proportion of transferrin occupied by iron"],
    "The table says serum ferritin indicates iron stores (predominant in marrow).")
add(S4, 72, "numeric", "The normal serum-ferritin range shown is:",
    "30–300 ng/mL", ["3–30 ng/mL", "50–150 µg/dL", "300–360 µg/dL"],
    "The p72 table gives 30–300 ng/mL.")
add(S4, 72, "recall", "A low ferritin is interpreted as:",
    "Reduced iron stores and iron deficiency", ["A normal result that excludes deficiency", "Increased circulating iron", "A high acute-phase response only"],
    "Low ferritin reflects decreased iron stores and iron deficiency.")
add(S4, 72, "truefalse", "TRUE or FALSE — a normal or high serum ferritin always rules out iron deficiency.",
    "False — ferritin is an acute-phase reactant, so normal/high values cannot rule it out", ["True — ferritin is never affected by inflammation", "False — only a low ferritin rules out iron deficiency", "True — but only when serum iron is low"],
    "The page warns that normal/high ferritin cannot rule out deficiency because ferritin is an acute-phase reactant.")
add(S4, 72, "recall", "Serum iron represents the amount of iron in circulation bound to:",
    "Transferrin", ["Ferritin", "Hemosiderin", "Albumin only"],
    "The table defines serum iron as circulating iron bound to transferrin.")
add(S4, 72, "numeric", "The normal serum-iron range in the table is:",
    "50–150 µg/dL", ["30–300 ng/mL", "300–360 µg/dL", "15–30 µg/dL"],
    "The table gives serum iron 50–150 µg/dL.")
add(S4, 72, "recall", "The table defines TIBC as the:",
    "Total iron-binding capacity of transferrin", ["Amount of ferritin stored in marrow", "Fraction of transferrin saturated with iron", "Daily iron absorbed from the diet"],
    "TIBC is total iron-binding capacity of transferrin.")
add(S4, 72, "numeric", "The normal TIBC range printed is:",
    "300–360 µg/dL", ["50–150 µg/dL", "30–300 ng/mL", "10–20 µg/dL"],
    "The normal TIBC is 300–360 µg/dL.")
add(S4, 72, "recall", "Transferrin saturation is calculated as:",
    "Serum iron ÷ TIBC × 100", ["TIBC ÷ serum iron × 100", "Ferritin ÷ TIBC × 100", "Serum iron × ferritin ÷ 100"],
    "The table gives TSAT = serum iron/TIBC × 100.")
add(S4, 72, "numeric", "The normal transferrin saturation written in the table is:",
    "33%", ["13%", "20%", "67%"],
    "The table lists TSAT 33%.")
add(S4, 72, "recall", "The serum-iron interpretation in iron deficiency is:",
    "Low, reflecting reduced absorption and reduced circulating iron", ["High due to increased absorption", "Normal because transferrin carries no iron", "Low only when ferritin is high"],
    "The table links low serum iron to decreased absorption and decreased circulation.")
add(S4, 72, "recall", "Why does TIBC rise in iron deficiency in the p72 table?",
    "Low iron triggers compensatory increased transferrin production", ["Hepcidin causes excess ferritin release", "Ferritin converts into transferrin", "The marrow stops making transferrin receptors"],
    "The table explains high TIBC as compensatory increased transferrin production when iron is low.")
add(S4, 72, "recall", "The earliest iron-deficiency marker singled out under the table is:",
    "Low ferritin", ["Low haemoglobin", "Low MCV", "High TIBC"],
    "The page explicitly labels low ferritin as earliest.")
add(S4, 72, "recall", "The most sensitive marker for iron deficiency listed beneath the table is increased:",
    "Soluble transferrin receptor", ["Serum iron", "TIBC", "Haemoglobin"],
    "The p72 note labels increased soluble transferrin receptor as most sensitive.")
add(S4, 72, "recall", "The ratio named as most specific for iron deficiency is:",
    "Soluble transferrin receptor ÷ log ferritin", ["Ferritin ÷ log soluble transferrin receptor", "Serum iron ÷ TIBC", "TIBC ÷ haemoglobin"],
    "The page names sTfR/log ferritin as the most specific measure.")

# ---------------------------------------------------------------------------
# Book p73 — staged iron deficiency and first-line causes
add(S5, 73, "recall", "Which stage labels are shown in order on the iron-deficiency table?",
    "Stage I pre-latent/negative balance → Stage II latent/iron-deficient erythropoiesis → Stage III iron-deficiency anaemia", ["Stage I anaemia → Stage II normal → Stage III negative balance", "Stage I latent → Stage II pre-latent → Stage III sideroblastic anaemia", "Stage I haemolysis → Stage II iron excess → Stage III anaemia of chronic disease"],
    "The table progresses from pre-latent negative balance to latent iron-deficient erythropoiesis to iron-deficiency anaemia.")
add(S5, 73, "recall", "In Stage I (pre-latent/negative iron balance), bone-marrow iron is:",
    "Decreased", ["Absent", "Increased", "Unchanged in all cases"],
    "The Stage I row shows decreased marrow iron.")
add(S5, 73, "recall", "Bone-marrow iron is absent in which stages of the table?",
    "Stages II and III", ["Stage I only", "Stage I and II only", "Stage III only"],
    "The marrow-iron row is absent in Stage II and Stage III.")
add(S5, 73, "recall", "Serum ferritin across the three stages is shown as:",
    "Decreased from Stage I onward", ["Normal through Stage III", "Increased in Stage I and low only in Stage III", "Absent in Stage I, then increased"],
    "The serum-ferritin row decreases in all three stages.")
add(S5, 73, "recall", "Transferrin saturation in Stage I is shown as:",
    "Normal", ["Below 20%", "Below 15%", "Increased"],
    "Stage I TSAT is marked normal in the table.")
add(S5, 73, "numeric", "Transferrin saturation in Stage II is shown as below:",
    "20%", ["10%", "15%", "33%"],
    "The Stage II TSAT entry is decreased (<20%).")
add(S5, 73, "numeric", "The Stage III TSAT threshold shown in the table is below:",
    "15%", ["10%", "20%", "33%"],
    "The Stage III TSAT entry is decreased (<15%).")
add(S5, 73, "recall", "TIBC and soluble transferrin receptor are normal in Stage I, then in Stages II and III they are:",
    "Increased", ["Both decreased", "TIBC decreased and sTfR unchanged", "Both absent"],
    "The table shows TIBC and sTfR rising from Stage II onward.")
add(S5, 73, "recall", "FEP on p73 is expanded as:",
    "Free erythrocyte protoporphyrin", ["Ferritin erythroid protein", "Free extracellular peptide", "Folate erythrocyte precursor"],
    "FEP is free erythrocyte protoporphyrin.")
add(S5, 73, "recall", "The page writes haemoglobin as:",
    "Heme + globin", ["Iron + transferrin", "Ferritin + globin", "Protoporphyrin + albumin"],
    "The FEP note states Hb = heme + globin.")
add(S5, 73, "recall", "Across the three deficiency stages, FEP is shown as:",
    "Normal in Stage I, increased in Stages II and III", ["Increased only in Stage I, then normal", "Normal in all three stages", "Decreased in Stage I, then absent"],
    "The FEP row is normal in Stage I and increased in Stages II and III.")
add(S5, 73, "recall", "As iron falls during haem synthesis, what happens to unbound protoporphyrin?",
    "It increases", ["It decreases", "It remains absent at every stage", "It is converted to transferrin"],
    "The page shows Fe + protoporphyrin and ↓Fe leading to increased unbound protoporphyrin.")
add(S5, 73, "recall", "Reticulocyte haemoglobin becomes reduced in which stages?",
    "Stages II and III", ["Stage I only", "Stage III only", "It remains normal in all three stages"],
    "The reticulocyte-haemoglobin row is normal in Stage I and decreased in Stages II and III.")
add(S5, 73, "recall", "In Stage II, haemoglobin and MCV are both shown as:",
    "Normal", ["Decreased", "Increased", "Absent"],
    "Stage II retains normal Hb and MCV; the cells are described as normocytic/normochromic.")
add(S5, 73, "recall", "The Stage II red-cell description is:",
    "Normocytic and normochromic", ["Microcytic and hypochromic", "Macrocytic and hyperchromic", "Spherocytic and polychromatic"],
    "Stage II is labelled normocytic and normochromic.")
add(S5, 73, "recall", "The symptom entry in Stage I (pre-latent/negative balance) is:",
    "No symptom is listed", ["Fatigue and hair fall", "Pica and epithelial changes", "Jaundice and splenomegaly"],
    "The Stage I symptom cell contains a dash; the table lists no symptoms there.")
add(S5, 73, "recall", "Which non-specific symptoms are listed for Stage II?",
    "Fatigue and hair fall", ["Pica and epithelial changes", "Fever and bloody diarrhoea", "Jaundice and splenomegaly only"],
    "Stage II symptoms are listed as fatigue and hair fall.")
add(S5, 73, "recall", "Stage III is associated with which paired symptom group?",
    "Pica and epithelial changes", ["No symptoms", "Fatigue and hair fall only", "Fever and arthritis"],
    "Stage III includes pica and epithelial changes.")
add(S5, 73, "scenario", "A patient with iron deficiency reports eating ice. Which Stage III symptom label applies?",
    "Pica (pagophagia)", ["Dyspepsia", "Tenesmus", "Meralgia"],
    "The page lists pica, for example eating ice, in Stage III.")
add(S5, 73, "recall", "In the Stage III row, the red-cell size/colour may be:",
    "Normocytic plus microcytic, and normochromic plus hypochromic", ["Macrocytic and hyperchromic only", "Always normocytic and normochromic", "Spherocytic with high haemoglobin"],
    "Stage III is shown as normocytic + microcytic and normochromic + hypochromic.")
add(S5, 73, "recall", "The Stage III haemoglobin and MCV rows are both shown as:",
    "Decreased", ["Normal", "Increased", "Not measured"],
    "Stage III is iron-deficiency anaemia, with decreased Hb and MCV in the table.")
add(S5, 73, "recall", "Chronic blood loss in the IDA aetiology section is qualified as:",
    "Unless proven otherwise", ["Only after iron therapy", "Only when stool is visibly bloody", "Not a possible cause"],
    "The page lists chronic blood loss with the qualifier 'unless proven otherwise'.")
add(S5, 73, "recall", "Which pair appears in the iron-loss causes list?",
    "Menstruation and haemorrhoids", ["Celiac disease and tropical sprue", "CKD and malnutrition", "Pica and epithelial changes"],
    "Menstruation and haemorrhoids are listed under iron loss.")
add(S5, 73, "recall", "Which malabsorption-site associations are printed as causes of iron deficiency?",
    "Celiac disease—duodenal involvement; tropical sprue—pan-intestinal involvement", ["Celiac disease—ileal only; tropical sprue—gastric only", "Celiac disease—colon; tropical sprue—oesophagus", "Celiac disease—pancreas; tropical sprue—stomach only"],
    "The page pairs celiac disease with duodenal involvement and tropical sprue with pan-intestinal involvement.")
add(S5, 73, "recall", "The increased-demand category on p73 lists:",
    "Chronic kidney disease", ["Haemorrhoids", "Celiac disease", "Pica"],
    "Chronic kidney disease is the item printed under increased demand on the page.")
add(S5, 73, "recall", "Which additional broad cause category appears after increased demand?",
    "Nutritional", ["Autoimmune", "Infectious", "Neoplastic"],
    "Nutritional is listed as another cause category.")

# ---------------------------------------------------------------------------
# Book p74 — iron deficit formula and clinical features
add(S6, 74, "recall", "Which formula is printed for iron deficit?",
    "2.3 × (desired Hb − patient's Hb) × body weight + 1000 mg", ["2.4 × (patient Hb − desired Hb) × body weight − 500 mg", "Body weight ÷ Hb difference × 1000 mg", "2.3 × (desired Hb + patient's Hb) ÷ body weight"],
    "The p74 formula is 2.3 × (desired Hb − patient's Hb) × body weight + 1000 mg.")
add(S6, 74, "truefalse", "TRUE or FALSE — the p74 note says EPO therapy should be given before correcting iron stores.",
    "False — correct iron stores first", ["True — EPO is first even when iron stores are depleted", "False — iron stores do not matter before EPO", "True — but only in pregnancy"],
    "The note says EPO therapy should be given after correcting iron stores.")
add(S7, 74, "recall", "Which four oral lesions are shown/labeled under epithelial lesions of iron deficiency?",
    "Angular cheilitis/stomatitis, oral candidiasis, median rhomboid glossitis and atrophic glossitis", ["Aphthae, leukoplakia, oral lichen planus and parotitis", "Hair loss, koilonychia, pica and splenomegaly", "Canker sores, gingival hyperplasia, thrush and ulcers only"],
    "The p74 images label angular cheilitis/stomatitis, oral candidiasis, median rhomboid glossitis and atrophic glossitis.")
add(S7, 74, "recall", "Atrophic glossitis is described as involving:",
    "Loss of papillae and atrophy", ["Enlarged papillae and hyperplasia", "A white pseudomembrane only", "Tongue ulceration with intact papillae"],
    "The caption describes atrophic glossitis as loss of papillae and atrophy.")
add(S7, 74, "recall", "Plummer–Vinson syndrome on p74 is associated with:",
    "Dysphagia and oesophageal webs", ["Odynophagia and gastric folds", "Diarrhoea and ileal webs", "Steatorrhoea and duodenal strictures"],
    "The page links Plummer–Vinson syndrome to dysphagia and oesophageal webs.")
add(S7, 74, "recall", "Which nail change appears in the 'Others' list for iron deficiency?",
    "Koilonychia", ["Clubbing", "Leukonychia", "Onycholysis"],
    "Koilonychia is listed among the other clinical features.")
add(S7, 74, "recall", "The gastric associations listed among other iron-deficiency features are:",
    "Achlorhydria and atrophic gastritis", ["Hyperchlorhydria and hypertrophic gastritis", "Pseudomembranous gastritis and ulcers", "Gastrinoma and MALToma"],
    "The page lists achlorhydria and atrophic gastritis.")
add(S7, 74, "recall", "Which additional syndrome appears in the p74 'Others' list?",
    "Hyperactivity syndromes", ["Nephrotic syndrome", "Carcinoid syndrome", "Dumping syndrome"],
    "The p74 list includes hyperactivity syndromes.")
add(S7, 74, "recall", "The growth/development note proposes which relationship?",
    "Increased transferrin → decreased growth hormone", ["Decreased transferrin → increased growth hormone", "Increased ferritin → increased growth hormone", "Increased hepcidin → increased growth hormone"],
    "The note links growth/development defect to increased transferrin and decreased GH.")
add(S7, 74, "recall", "The most common form of pica identified is:",
    "Pagophagia", ["Geophagia", "Amylophagia", "Trichophagia"],
    "The page notes pica and marks pagophagia as most common.")
add(S7, 74, "recall", "Which cardiovascular consequence is listed among other iron-deficiency features?",
    "Worsening congestive cardiac failure", ["Reduced cardiac output with no symptoms", "Aortic stenosis", "Pulmonary hypertension only"],
    "Worsening of congestive cardiac failure is listed.")
add(S7, 74, "recall", "Which pair completes the p74 list of systemic features?",
    "Mild splenomegaly and neuropsychiatric manifestations", ["Hepatomegaly and jaundice", "Fever and arthritis", "Oedema and ascites"],
    "The list includes mild splenomegaly and neuropsychiatric manifestations; hair loss is also included.")

# ---------------------------------------------------------------------------
# Book p75 — iron-deficiency investigations and morphology
add(S8, 75, "recall", "Which blood-test pattern is shown for iron-deficiency anaemia?",
    "Ferritin↓, serum iron↓, TSAT↓, TIBC↑, soluble transferrin receptor↑, red-cell protoporphyrin↑ and RDW↑", ["Ferritin↑, serum iron↑, TSAT↑, TIBC↓, sTfR↓ and RDW↓", "Ferritin normal, serum iron↑, TIBC↓ and RDW normal", "Ferritin↓, serum iron↑, TSAT↑, TIBC↓ and sTfR↓"],
    "The p75 blood parameters show low ferritin/iron/TSAT and increased TIBC, sTfR, red-cell protoporphyrin and RDW.")
add(S8, 75, "recall", "The MCV in IDA is described as:",
    "Normal to low", ["Always high", "Always normal", "High only in Stage I"],
    "The page states MCV normal to low.")
add(S8, 75, "recall", "The mean corpuscular haemoglobin (MCH) is described as:",
    "Normal to low", ["Always high", "Always absent", "Elevated only in Stage III"],
    "The page describes MCH as normal to low.")
add(S8, 75, "numeric", "The MCH range printed on p75 is:",
    "27–31 pg", ["17–21 pg", "32–36 pg", "80–100 pg"],
    "The source gives MCH 27–31 pg.")
add(S8, 75, "recall", "The page places hypochromia and microcytosis at which IDA stage?",
    "Stage III", ["Stage I", "Stage II", "They are present before iron stores fall"],
    "The p75 note brackets hypochromia and microcytosis as occurring at the third stage.")
add(S8, 75, "recall", "MCHC in iron deficiency is described as:",
    "Normal to low", ["Always high", "Always increased in Stage I", "Absent"],
    "The page lists MCHC as normal to low.")
add(S8, 75, "recall", "The Mentzer index is calculated as:",
    "MCV ÷ RBC count", ["RBC count ÷ MCV", "MCH × MCV", "Haemoglobin ÷ ferritin"],
    "The page defines Mentzer index as MCV/RBC.")
add(S8, 75, "numeric", "A Mentzer index above 13 favours:",
    "Iron deficiency", ["Thalassaemia trait", "Sideroblastic anaemia", "Anaemia of chronic disease only"],
    "The page labels >13 as iron deficiency.")
add(S8, 75, "numeric", "A Mentzer index below 13 is paired with:",
    "Thalassaemia trait", ["Iron deficiency", "Megaloblastic anaemia", "Haemolysis"],
    "The page labels <13 as thalassaemia trait.")
add(S8, 75, "recall", "The most common cause of anisopoikilocytosis noted on the smear page is:",
    "Iron-deficiency anaemia", ["Sickle-cell disease", "Celiac disease", "Autoimmune haemolysis"],
    "The smear note says anisopoikilocytosis (most common cause: IDA).")
add(S8, 75, "recall", "The morphology comment accompanying anisopoikilocytosis is:",
    "Variable RBC morphology", ["Uniform RBC morphology", "Only nucleated RBCs", "Large spherocytes only"],
    "The p75 smear note says variable RBC morphology.")
add(S8, 75, "numeric", "The RDW threshold marked increased in the smear note is:",
    ">14.5%", ["<11.5%", ">10%", "<14.5%"],
    "The note gives increased RDW >14.5%, with normal 11.5–14.5%.")
add(S8, 75, "numeric", "The normal RDW interval shown in parentheses is:",
    "11.5–14.5%", ["5.5–10.5%", "14.5–20%", "20–30%"],
    "The source notes normal RDW of 11.5–14.5%.")
add(S8, 75, "recall", "Which three red-cell findings are labelled in the iron-deficiency smear image?",
    "Tear-drop cells, hypochromia and pencil cells", ["Spherocytes, schistocytes and target cells", "Howell–Jolly bodies, basophilic stippling and sickle cells", "Acanthocytes, bite cells and stomatocytes"],
    "The labelled smear findings are tear-drop cell, hypochromia and pencil cells.")
add(S8, 75, "recall", "The lower-right severe iron-deficiency smear image specifically labels:",
    "Microcytes", ["Macro-ovalocytes", "Spherocytes", "Schistocytes"],
    "The severe iron-deficiency image is labelled microcytes.")
add(S8, 75, "recall", "RDW is expanded in the note as:",
    "Red-cell distribution width", ["Reticulocyte distribution window", "Red-cell diameter weight", "Reticulocyte division width"],
    "The note expands RDW as red-cell distribution width.")

# ---------------------------------------------------------------------------
# Book p76 — marrow, iron therapy and response timeline
add(S9, 76, "recall", "In IDA, a Prussian-blue bone-marrow stain shows:",
    "Absence of iron stores", ["Excess iron stores", "Increased ferritin granules", "Normal iron stores in every case"],
    "The p76 bone-marrow list states absence of iron stores on Prussian-blue stain.")
add(S9, 76, "recall", "The erythroid marrow response listed in IDA is:",
    "Erythroid hyperplasia due to ineffective erythropoiesis", ["Myeloid aplasia due to increased iron", "Megakaryocytic hyperplasia due to haemolysis", "Marrow replacement by granulomas"],
    "The page lists erythroid hyperplasia due to ineffective erythropoiesis.")
add(S9, 76, "management", "Parenteral iron is listed for which stage of iron deficiency?",
    "Stage III", ["Stage I only", "Stage II only", "All stages before ferritin falls"],
    "The page says parenteral iron is given for Stage III iron deficiency.")
add(S9, 76, "numeric", "The dose/frequency as written for iron sucrose on p76 is:",
    "200 mg × thrice daily", ["20 mg once daily", "1 g once weekly", "500 mg every month"],
    "The scan prints 'iron sucrose 200 mg × thrice daily'. This source transcription is not a current prescribing instruction; verify dosing against a trusted clinical reference.")
add(S9, 76, "recall", "Which additional parenteral iron preparation is listed between iron sucrose and ferric carboxymaltose?",
    "Iron isomaltose", ["Ferrous sulphate", "Ferritin", "Transferrin"],
    "The listed parenteral agents include iron sucrose, iron isomaltose and ferric carboxymaltose.")
add(S9, 76, "numeric", "The ferric carboxymaltose amount printed on p76 is:",
    "1 g", ["100 mg", "200 mg", "2.5 g"],
    "The page lists ferric carboxymaltose 1 g.")
add(S9, 76, "recall", "The administration routes listed for parenteral iron are:",
    "Direct IV or infusion", ["Oral or sublingual", "Intramuscular only", "Subcutaneous only"],
    "The page says direct IV or infusion.")
add(S9, 76, "management", "Oral iron is assigned in the source to:",
    "Latent-stage iron deficiency", ["Stage III only", "Iron overload", "All patients with normal ferritin"],
    "The page lists oral iron for latent-stage iron deficiency.")
add(S9, 76, "numeric", "The oral ferrous-sulphate dose shown is:",
    "200 mg three times daily", ["20 mg once daily", "200 mg once weekly", "1 g twice daily"],
    "The source gives 200 mg ferrous sulphate TID.")
add(S9, 76, "numeric", "Oral iron is to be resumed/continued for how long after correction, according to the page?",
    "6–12 months", ["6–12 days", "2 weeks", "3–5 years"],
    "The p76 note says resume for 6–12 months after correction.")
add(S9, 76, "recall", "The side effect listed for oral iron is:",
    "Gastric intolerance", ["Ischaemic colitis", "Pancreatitis", "Cardiac toxicity"],
    "The page lists gastric intolerance as a side effect.")
add(S9, 76, "numeric", "After treatment, the reticulocyte count is expected to begin rising after:",
    "5–7 days", ["1–2 days", "10–14 days", "4 weeks"],
    "The page says reticulocytes start to rise after 5–7 days.")
add(S9, 76, "numeric", "The reticulocyte-count peak is expected at:",
    "10–14 days", ["5–7 days", "2–3 weeks", "6–12 months"],
    "The page gives a reticulocyte peak at 10–14 days.")
add(S9, 76, "numeric", "Haemoglobin is expected to start rising after:",
    "2 weeks", ["2 days", "5–7 days", "10–14 weeks"],
    "The p76 follow-up note says Hb starts to rise at 2 weeks.")
add(S9, 76, "numeric", "The Hb increase listed per month is:",
    "2 g/dL", ["0.2 g/dL", "1 g/dL", "5 g/dL"],
    "The page gives an increase of 2 g/dL per month.")

GUIDES = {
    S1: ("Body Iron & Daily Needs", "Male 50 mg/kg; female 40 mg/kg. Pools: Hb 67%, storage 27%, transferrin 0.08%, myoglobin 3.5%, labile 2.2%.\nPrussian blue is the marrow-store gold standard; hemosiderin + ferrocyanide turns blue-black.\nDaily requirements and p70 Hb thresholds are included as printed."),
    S2: ("Dietary Iron & Absorption", "Heme Fe²⁺/HCP versus non-heme Fe³⁺/duodenal cytochrome b reductase → Fe²⁺/DMT1.\nReducing substances and acidic pH enhance absorption; phytate, tannate and oxalate inhibit it.\nThe diagram follows mucosal storage, epithelial shedding and basolateral export."),
    S3: ("Export, Transport & Marrow Uptake", "Ferroportin exports iron; liver hepcidin inhibits it; hephaestin oxidizes Fe²⁺ to Fe³⁺ for transferrin.\nMarrow TfR1/TfR2 → acidic endosome → Fe²⁺/DMT1 → common iron pool → mitochondrial heme.\nA source-note direction for ceruloplasmin is flagged as printed and should be verified before clinical use."),
    S4: ("Serum Iron Indices", "Ferritin 30–300 ng/mL; serum iron 50–150 µg/dL; TIBC 300–360 µg/dL; TSAT 33%.\nIron deficiency: ferritin/iron/TSAT low and TIBC/sTfR high; ferritin can be masked by acute-phase response.\nLow ferritin is earliest; sTfR is most sensitive; sTfR/log ferritin is listed as most specific."),
    S5: ("Stages of Iron Deficiency", "Stage I: pre-latent/negative balance; Stage II: latent/iron-deficient erythropoiesis; Stage III: IDA.\nTSAT falls below 20% then 15%; TIBC, sTfR and FEP rise; reticulocyte Hb falls from Stage II.\nStage II remains normocytic/normochromic; Stage III has anaemia, microcytosis/hypochromia and pica/epithelial changes."),
    S6: ("Causes & Iron Deficit", "Blood loss is emphasized ('unless proven otherwise'); menstruation and haemorrhoids are listed.\nMalabsorption: celiac (duodenum), tropical sprue (pan-intestinal); CKD and nutrition are also listed.\nThe 2.3 × Hb-difference × weight + 1000 mg formula and EPO-after-iron note are transcribed."),
    S7: ("Clinical Features", "Oral lesions: angular cheilitis/stomatitis, candidiasis, median rhomboid and atrophic glossitis.\nPlummer–Vinson: dysphagia + oesophageal webs; other findings include koilonychia, pagophagia and hair loss.\nGrowth/development, splenomegaly, heart failure and neuropsychiatric features are also inventoried."),
    S8: ("IDA Investigations", "Ferritin, serum iron, TSAT fall; TIBC, sTfR, red-cell protoporphyrin and RDW rise.\nMCH 27–31 pg; Mentzer >13 favors IDA, <13 thalassaemia trait; smear shows anisopoikilocytosis.\nTear-drop cells, hypochromia, pencil cells and microcytes are labelled in the figures."),
    S9: ("Marrow, Treatment & Follow-up", "Marrow: absent Prussian-blue stores and erythroid hyperplasia.\nThe page lists parenteral iron for Stage III, oral iron for latent disease and gastric intolerance.\nReticulocytes rise at 5–7 days/peak 10–14; Hb starts at two weeks; dosing is reproduced as printed, not current guidance."),
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
