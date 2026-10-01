#!/usr/bin/env python3
"""Generate Chapter 9 Gastrinoma (Book p60–62), in scanned page order."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 9
TITLE = "Gastrinoma"
PAGES = "60-62"

S1 = "Gastrinoma Types and Comparisons"
S2 = "Gastrinoma Triangle and Gastrin Effects"
S3 = "Clinical Features and Diarrhoea"
S4 = "Biochemical and Receptor Imaging"
S5 = "Treatment and Surgical Anatomy"
RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    random.Random(9000 + CHAPTER * 10000 + len(RAW)).shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2
        assert sum(o.startswith("False") for o in options) == 2
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p60 — definition and sporadic versus MEN1-associated gastrinoma
add(S1, 60, "recall", "A gastrinoma is described as a neuroendocrine tumour that secretes:",
    "Gastrin", ["Insulin", "Somatostatin", "Vasoactive intestinal peptide"],
    "The opening definition is a neuroendocrine tumour secreting gastrin.")
add(S1, 60, "recall", "Which pair is listed as neuroendocrine markers in the introduction?",
    "Chromogranin and NSE", ["CEA and CA-125", "AFP and β-hCG", "Ferritin and transferrin receptor"],
    "The page lists chromogranin and NSE as neuroendocrine markers.")
add(S1, 60, "recall", "The clinical manifestation named for gastrinoma is:",
    "Zollinger–Ellison syndrome", ["Carcinoid syndrome", "Werner syndrome", "Whipple disease"],
    "The clinical manifestation is Zollinger–Ellison syndrome.")
add(S1, 60, "numeric", "What proportion of gastrinomas is labelled sporadic in the comparison table?",
    "80%", ["20%", "50%", "60%"],
    "The table assigns 80% to sporadic gastrinoma.")
add(S1, 60, "numeric", "What proportion is labelled MEN1-associated?",
    "20%", ["80%", "10%", "60%"],
    "The table assigns 20% to MEN1-associated gastrinoma.")
add(S1, 60, "recall", "Among sporadic pancreatic neuroendocrine tumours, the page calls gastrinoma the:",
    "Second most common functional pancreatic neuroendocrine tumour", ["Most common functional pancreatic neuroendocrine tumour", "Only non-functional pancreatic tumour", "Least common pancreatic neuroendocrine tumour"],
    "The sporadic column says second most common functional pancreatic neuroendocrine tumour.")
add(S1, 60, "recall", "The typical sporadic gastrinoma is described as:",
    "Single and large", ["Multiple and small", "Multiple and large", "Single and microscopic"],
    "The sporadic column lists a single, large tumour.")
add(S1, 60, "recall", "Within MEN1, gastrinoma is described as the most common:",
    "Neuroendocrine tumour", ["Pituitary tumour", "Adrenal cortical tumour", "Parathyroid carcinoma"],
    "The MEN1 column calls it the most common neuroendocrine tumour in MEN1.")
add(S1, 60, "recall", "MEN1-associated gastrinomas are described as:",
    "Multiple and small", ["Single and large", "Single and usually benign", "Large and restricted to pancreatic tail"],
    "The MEN1 column lists multiple, small tumours.")
add(S1, 60, "numeric", "The age range associated with sporadic gastrinoma in the table is:",
    "30–50 years", ["Under 20 years", "50–70 years", "Over 70 years"],
    "The sporadic column gives an age group of 30–50 years.")
add(S1, 60, "numeric", "The age group shown for MEN1-associated gastrinoma is:",
    "Under 20 years", ["30–50 years", "50–70 years", "Over 70 years"],
    "The MEN1 column gives <20 years.")
add(S1, 60, "recall", "The sex distribution printed for sporadic gastrinoma is:",
    "Female > male", ["Male > female", "Male = female", "Female-only"],
    "The sporadic column states female > male.")
add(S1, 60, "recall", "The MEN1-associated sex distribution is shown as equal, with which inheritance pattern?",
    "Male = female; autosomal dominant", ["Female > male; X-linked recessive", "Male > female; autosomal recessive", "Equal; mitochondrial inheritance"],
    "The MEN1 column states M = F and notes autosomal-dominant inheritance.")
add(S1, 60, "numeric", "The malignancy-risk entry for sporadic gastrinoma is:",
    "60%, with liver metastasis noted", ["Low, mostly benign", "20%, with lung metastasis", "100%, with bone metastasis"],
    "The sporadic column gives 60% and notes metastasis to liver.")
add(S1, 60, "recall", "The MEN1-associated malignancy-risk entry is:",
    "Low; mostly benign", ["60% with liver metastasis", "High and more aggressive", "Uniformly metastatic at diagnosis"],
    "The MEN1 column describes low malignancy risk and mostly benign tumours.")
add(S1, 60, "recall", "The location paired with sporadic gastrinoma in the table is:",
    "Passaro's triangle (gastrinoma triangle)", ["Duodenum only", "Pyloric antrum", "Splenic hilum"],
    "The sporadic location is Passaro's/gastrinoma triangle.")
add(S1, 60, "recall", "The location cell for MEN1-associated gastrinoma reads:",
    "Duodenum", ["Passaro's triangle only", "Gastric fundus", "Liver"],
    "The MEN1 location entry is duodenum.")
add(S1, 60, "management", "The table's treatment entry for the majority of sporadic gastrinoma cases is:",
    "Surgery", ["High-dose PPI alone", "Octreotide without surgery", "Total gastrectomy in all cases"],
    "The sporadic column says surgery in the majority of cases.")
add(S1, 60, "management", "For MEN1-associated disease, the table lists high-dose PPI and surgery when tumour size exceeds:",
    ">2.5 cm", [">0.5 cm", ">1 cm", ">5 cm"],
    "The MEN1 table lists high-dose PPI and surgery if size is >2.5 cm.")
add(S1, 60, "recall", "The prognosis comparison in the table describes sporadic tumours as:",
    "Bad and more aggressive", ["Good and less aggressive", "Uniformly indolent", "Unrelated to tumour behaviour"],
    "The sporadic prognosis is labelled bad/more aggressive.")
add(S1, 60, "recall", "The prognosis entry for MEN1-associated tumours is:",
    "Good and less aggressive", ["Bad and more aggressive", "Always metastatic", "Not assessed"],
    "The MEN1 prognosis is labelled good/less aggressive.")
add(S1, 60, "recall", "The note identifies which tumour as the most common functional pancreatic neuroendocrine tumour overall?",
    "Insulinoma", ["Gastrinoma", "Glucagonoma", "VIPoma"],
    "The note says insulinoma is the most common functional pancreatic neuroendocrine tumour overall.")
add(S1, 60, "recall", "The most common cause of death in MEN1 is attributed in the note to an entero-pancreatic neuroendocrine tumour, specifically:",
    "Gastrinoma", ["Insulinoma", "Somatostatinoma", "Glucagonoma"],
    "The note identifies entero-pancreatic NET (gastrinoma) as the most common cause of death in MEN1.")

# ---------------------------------------------------------------------------
# Book p60 — triangle anatomy and effects of increased gastrin
add(S2, 60, "recall", "Which junction is point A of the gastrinoma triangle?",
    "Junction of cystic duct and common bile duct", ["Junction of second and third duodenal portions", "Junction of pancreatic body and neck", "Junction of common bile duct and pancreatic tail"],
    "Point A is the junction of the cystic duct and CBD.")
add(S2, 60, "recall", "Point B of the gastrinoma triangle is the junction of the:",
    "Second and third portions of the duodenum", ["First and second portions of the duodenum", "Body and neck of pancreas", "Cystic duct and common bile duct"],
    "Point B is the junction of the second and third portions of the duodenum.")
add(S2, 60, "recall", "The pancreatic landmark at point C is the junction of the:",
    "Body and neck of the pancreas", ["Head and uncinate process", "Body and tail", "Pancreatic duct and ampulla"],
    "Point C is the junction of the body and neck of pancreas.")
add(S2, 60, "recall", "Which group contains all three boundaries identified for the gastrinoma triangle?",
    "Cystic-duct/CBD junction; D2–D3 junction; pancreatic body–neck junction", ["Pylorus; ligament of Treitz; pancreatic tail", "Fundus; ileocecal valve; pancreatic head", "CBD/ampulla; D1–D2 junction; pancreatic body–tail junction"],
    "The three labelled points are the cystic duct/CBD junction, second–third duodenal junction and pancreatic body–neck junction.")
add(S2, 60, "recall", "In the effect diagram, increased gastrin first stimulates:",
    "Parietal cells", ["Chief cells", "Goblet cells", "Paneth cells"],
    "The diagram shows increased gastrin stimulating parietal cells.")
add(S2, 60, "recall", "The parietal-cell response to increased gastrin is increased secretion of:",
    "Hydrochloric acid", ["Pepsinogen", "Intrinsic factor only", "Bicarbonate into the lumen"],
    "The pathway is gastrin → parietal cells → increased HCl secretion.")
add(S2, 60, "recall", "Which downstream consequence is paired with mucosal acid injury in the gastrin effect diagram?",
    "Gastric ulcer or duodenal ulcer", ["Pyloric hypertrophy or ileal stricture", "MALToma or celiac disease", "Aphthous ulcer or toxic megacolon"],
    "Acid damages the GI mucosal lining and is linked to gastric or duodenal ulcer.")
add(S2, 60, "recall", "Excess acid can cause diarrhoea and steatorrhoea by inactivating:",
    "Pancreatic enzymes", ["Bile-acid transporters", "Intrinsic factor", "Brush-border lactase only"],
    "The page states that acid inactivates pancreatic enzymes, producing diarrhoea, steatorrhoea and malabsorption.")
add(S2, 60, "recall", "Which cluster is explicitly linked to acid-mediated pancreatic-enzyme inactivation?",
    "Diarrhoea, steatorrhoea and malabsorption", ["Constipation, jaundice and pruritus", "Haematemesis, leucopenia and fever", "Dysphagia, tenesmus and anaemia"],
    "The diagram lists diarrhoea, steatorrhoea and malabsorption after pancreatic enzyme inactivation.")

# ---------------------------------------------------------------------------
# Book p61 — clinical pattern and dual diarrhoeal mechanisms
add(S3, 61, "recall", "The most important symptom of gastrinoma listed on p61 is:",
    "Abdominal pain", ["Jaundice", "Dysphagia", "Painless rectal bleeding"],
    "The clinical-features list marks abdominal pain as the most important symptom.")
add(S3, 61, "recall", "The most common manifestation of gastrinoma is:",
    "Peptic ulcer disease", ["Acute pancreatitis", "Carcinoid syndrome", "Iron-deficiency anaemia"],
    "The page identifies peptic ulcer disease as the most common manifestation.")
add(S3, 61, "recall", "An unusually distal ulcer location that raises suspicion of gastrinoma is:",
    "Second part of the duodenum and beyond", ["Gastric antrum only", "First part of the duodenum only", "Lower oesophagus"],
    "The indicator list says unusual location: D2 and beyond.")
add(S3, 61, "numeric", "The book's refractory gastric-ulcer threshold is failure to respond for more than:",
    "12 weeks", ["4 weeks", "8 weeks", "24 weeks"],
    "The page lists GU >12 weeks as refractory to medical therapy.")
add(S3, 61, "numeric", "The refractory duodenal-ulcer threshold listed is more than:",
    "8 weeks", ["2 weeks", "12 weeks", "24 weeks"],
    "The page lists DU >8 weeks as refractory to medical therapy.")
add(S3, 61, "recall", "Which course feature is included as an indicator of gastrinoma in peptic-ulcer disease?",
    "Ulcer recurrence", ["A single ulcer that heals permanently", "Pain limited to fasting without recurrence", "Absence of abdominal symptoms"],
    "Recurrence is one of the listed indicators.")
add(S3, 61, "recall", "The symptom pair written together in the gastrinoma clinical-features list is:",
    "Abdominal pain and diarrhoea", ["Dysphagia and odynophagia", "Jaundice and pruritus", "Constipation and tenesmus"],
    "The list includes abdominal pain and diarrhoea.")
add(S3, 61, "recall", "The page describes gastrinoma-associated diarrhoea as having:",
    "Both osmotic and secretory components", ["Only an osmotic component", "Only a secretory component", "Neither component"],
    "The note explicitly says both osmotic and secretory components are present.")
add(S3, 61, "recall", "Which chain is the secretory component attributed to gastrin?",
    "Gastrin acts on enterocytes → water moves into the lumen", ["Gastrin inactivates lipase → steatorrhoea", "Acid blocks enterocytes → water moves into blood", "Gastrin suppresses parietal cells → constipation"],
    "The source gives gastrin acting on enterocytes and water moving into the lumen as the secretory component.")
add(S3, 61, "recall", "Which chain explains the osmotic/steatorrhoea component on p61?",
    "Increased acid → pancreatic-enzyme inactivation → reduced lipolysis → steatorrhoea", ["Increased gastrin → CCK-B blockade → bile-acid loss", "Reduced acid → increased lipolysis → constipation", "Increased secretin → pancreatic enzyme activation → diarrhoea"],
    "The page links increased acid to enzyme inactivation, reduced lipolysis and steatorrhoea.")

# ---------------------------------------------------------------------------
# Book p61–62 — fasting gastrin, secretin, scanning and notes
add(S4, 61, "numeric", "The p61 fasting-gastrin screening list labels a level above which value as 'carcinoma'?",
    ">1000 pg/mL", ["<200 pg/mL", "200–1000 pg/mL", ">200 pg/mL"],
    "The printed threshold list reads >1000 pg/mL: carcinoma; this question preserves the page's wording rather than substituting current diagnostic criteria.")
add(S4, 61, "numeric", "A fasting gastrin level in which interval is marked as needing a confirmatory test?",
    "200–1000 pg/mL", ["Below 200 pg/mL", "Above 1000 pg/mL", "50–150 pg/mL"],
    "The book says 200–1000 pg/mL requires a confirmatory test.")
add(S4, 61, "numeric", "Which fasting gastrin level is classified as normal in the p61 list?",
    "<200 pg/mL", ["200–1000 pg/mL", ">1000 pg/mL", ">2000 pg/mL"],
    "The page labels <200 pg/mL as normal.")
add(S4, 61, "recall", "The confirmatory stimulation test named for gastrinoma is the:",
    "Secretin stimulation test", ["Pentagastrin suppression test", "Schilling test", "D-xylose challenge"],
    "Secretin stimulation is identified as the confirmatory test.")
add(S4, 61, "truefalse", "TRUE or FALSE — secretin physiologically stimulates gastrin secretion, but in gastrinoma it inhibits it.",
    "False — the page says gastrinoma responds with stimulation; physiologically secretin inhibits gastrin", ["True — the response is reversed in gastrinoma", "False — secretin has no effect in either setting", "True — secretin stimulates in both settings"],
    "The source says secretin stimulates gastrin in gastrinoma, whereas physiologically it inhibits gastrin secretion.")
add(S4, 61, "recall", "The secretin-stimulation procedure begins with:",
    "Intravenous secretin", ["Oral secretin", "Intramuscular gastrin", "Radio-labelled octreotide"],
    "The procedure gives IV secretin and measures serum gastrin at regular intervals.")
add(S4, 61, "recall", "After IV secretin, serum gastrin is measured:",
    "At regular intervals", ["Only once before injection", "Only in a 24-hour urine collection", "Only after a month"],
    "The printed procedure measures serum gastrin at regular intervals.")
add(S4, 61, "numeric", "What increase in serum gastrin after secretin is shown as diagnostic of gastrinoma?",
    "A rise of at least 200 pg/mL", ["A fall of 200 pg/mL", "A rise of 20 pg/mL", "A rise of 1000 pg/mL"],
    "The diagram shows a rise by ≥200 pg/mL indicating gastrinoma.")
add(S4, 61, "recall", "The somatostatin-receptor scintigraphy test is also called the:",
    "Octreotide scan", ["Kanagawa test", "Prussian-blue scan", "Schilling scan"],
    "The source names somatostatin receptor scintigraphy (SRS)/octreotide scan.")
add(S4, 61, "recall", "The radioisotope specifically written beside SRS as most specific is:",
    "¹¹¹In", ["⁹⁹ᵐTc", "¹³¹I", "⁶⁸Ga"],
    "The p61 SRS list marks ¹¹¹In as most specific.")
add(S4, 61, "recall", "The principle behind an octreotide scan is that gastrinomas have many:",
    "Somatostatin receptors", ["CCK-B receptors in the liver only", "Insulin receptors", "Bile-acid transporters"],
    "The page explains that gastrinomas have somatostatin receptors in large numbers.")
add(S4, 61, "recall", "The page notes that octreotide is used in gastrinoma:",
    "As a treatment as well as a radiolabelled imaging agent", ["Only to provoke gastrin release", "Only as a stool marker", "Only to inhibit the rapid urease test"],
    "The note says the abundant somatostatin receptors explain octreotide use in treatment too.")
add(S4, 61, "recall", "The scan procedure described uses:",
    "Radioactive-labelled octreotide", ["Radioactive-labelled gastrin", "Oral barium and a fasting blood sample", "Unlabelled secretin only"],
    "The listed procedure gives radioactive-labelled octreotide.")
add(S4, 62, "truefalse", "TRUE or FALSE — the p62 note says SRS is not effective for small tumours/MEN1 and prefers endoscopic ultrasound.",
    "True — EUS is preferred in that note", ["False — SRS is best for every small MEN1 tumour", "False — CT is the stated preferred test", "True — but only for gastric ulcers"],
    "The note says SRS is not effective in small tumour/MEN1 and endoscopic USG is preferred.")
add(S4, 62, "recall", "The p62 note gives a basal-acid-output/maximal-acid-output ratio above what value for gastrinoma?",
    ">0.6", [">0.06", ">1.0", "<0.6"],
    "The note gives BAO/MAO >0.6 for gastrinoma.")
add(S4, 62, "recall", "The investigation listed under the p62 pheochromocytoma note is:",
    "Gallium DOTATATE PET scan", ["¹¹¹In octreotide scan only", "Prussian-blue stain", "C14 urea breath test"],
    "The page's note reads: investigation in pheochromocytoma — Gallium DOTATATE PET scan.")

# ---------------------------------------------------------------------------
# Book p62 — treatment, operation by location and notes
add(S5, 62, "numeric", "The MEN1-associated treatment note gives a high-dose PPI range of:",
    "60–80 mg", ["20–40 mg", "100–120 mg", "5–10 mg"],
    "The page gives high-dose PPI (60–80 mg) as usually enough for MEN1-associated disease.")
add(S5, 62, "scenario", "In MEN1-associated gastrinoma, the p62 treatment diagram recommends surgery when tumour size exceeds:",
    "2.5 cm", ["0.5 cm", "1 cm", "5 cm"],
    "The MEN1 note says surgery if size >2.5 cm.")
add(S5, 62, "management", "The sporadic-gastrinoma sequence on p62 is:",
    "High-dose PPI plus octreotide, followed by surgery", ["Surgery first, then low-dose PPI only", "Antibiotics followed by colectomy", "Gastrectomy without medical treatment"],
    "For sporadic disease the page lists high-dose PPI + octreotide followed by surgery.")
add(S5, 62, "recall", "For a gastrinoma in the pancreatic head, the operation listed is:",
    "Enucleation", ["Distal pancreatectomy", "Full-thickness duodenal excision", "Total gastrectomy"],
    "The page pairs pancreatic-head location with enucleation.")
add(S5, 62, "recall", "For a pancreatic-body or tail gastrinoma, the operation listed is:",
    "Distal pancreatectomy", ["Enucleation of the duodenum", "Full-thickness duodenal excision", "Total gastrectomy"],
    "The source pairs pancreatic body/tail with distal pancreatectomy.")
add(S5, 62, "recall", "The operation listed for a duodenal gastrinoma is:",
    "Full-thickness excision", ["Distal pancreatectomy", "Enucleation of pancreatic head", "Billroth II gastrectomy"],
    "The page lists full-thickness excision for duodenal location.")
add(S5, 62, "truefalse", "TRUE or FALSE — gastrectomy is required in the p62 gastrinoma treatment note.",
    "False — the note says gastrectomy is not required", ["True — it is required in all cases", "True — but only for MEN1", "False — a total gastrectomy is required for sporadic disease"],
    "The note explicitly says gastrectomy is not required.")
add(S5, 62, "recall", "The most common site of gastrinoma metastasis named in the treatment notes is:",
    "Liver", ["Bone", "Lung", "Brain"],
    "The p62 note names the liver as the most common metastasis site.")
add(S5, 62, "recall", "The gross specimen photograph on p62 is captioned as a:",
    "Surgical excision specimen", ["Octreotide scan", "Pyloric biopsy", "H. pylori culture plate"],
    "The image caption reads 'Surgical excision specimen'.")

GUIDES = {
    S1: ("Types and Comparisons", "Sporadic (80%) versus MEN1-associated (20%) differ in number/size, age, sex, location and risk.\nSporadic tumours are listed as more aggressive; MEN1 disease is usually smaller and less aggressive.\nKeep the note separating insulinoma as the commonest functional pancreatic NET overall."),
    S2: ("Triangle and Gastrin Effects", "Triangle points: cystic duct/CBD, D2–D3 and pancreatic body–neck junctions.\nGastrin → parietal cells → HCl; mucosal injury yields GU/DU.\nAcid can inactivate pancreatic enzymes, linking to diarrhoea, steatorrhoea and malabsorption."),
    S3: ("Clinical Features", "Abdominal pain is the most important symptom; PUD is the commonest manifestation.\nUnusual D2+ ulcers, refractory GU/DU, recurrence and diarrhoea raise suspicion in the page.\nDiarrhoea has secretory and enzyme-inactivation/steatorrhoea components."),
    S4: ("Tests and Imaging", "Fasting gastrin: <200 normal, 200–1000 needs confirmation; preserve the source's >1000 wording.\nSecretin gives a paradoxical gastrin rise ≥200 pg/mL in the printed test.\nSRS/¹¹¹In, octreotide rationale, EUS caveat, BAO/MAO and DOTATATE note are inventoried."),
    S5: ("Treatment and Surgical Anatomy", "MEN1: high-dose PPI 60–80 mg; surgery when >2.5 cm.\nSporadic: PPI + octreotide then surgery; procedure follows head/body-tail/duodenal location.\nThe page says gastrectomy is not required and names liver as the commonest metastasis site."),
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
