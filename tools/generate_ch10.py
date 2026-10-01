#!/usr/bin/env python3
"""Generate Chapter 10 Irritable Bowel Syndrome (Book p63–65), in page order."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 10
TITLE = "Irritable Bowel Syndrome"
PAGES = "63-65"

S1 = "Definition and Associations"
S2 = "Clinical Pattern, Rome IV and Red Flags"
S3 = "IBS Pathophysiology"
S4 = "Lifestyle and FODMAPs"
S5 = "Type-Based Medical Management"
RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    random.Random(10000 + CHAPTER * 10000 + len(RAW)).shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2
        assert sum(o.startswith("False") for o in options) == 2
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p63 — definition, associations and clinical presentations
add(S1, 63, "recall", "The opening line describes IBS as a functional bowel disorder and as a reaction of the GI system to:",
    "Stress", ["Dietary iron deficiency", "Bacterial invasion of all bowel-wall layers", "Bile-acid loss"],
    "The page describes IBS as a functional bowel disorder/reaction of the GI system to stress.")
add(S1, 63, "recall", "Which condition is included among the IBS associations?",
    "Lactose intolerance", ["Ulcerative colitis", "Intestinal tuberculosis", "Pseudomembranous enterocolitis"],
    "The association list includes lactose intolerance, celiac disease, fibromyalgia, chronic fatigue syndrome and generalized anxiety disorder.")
add(S1, 63, "recall", "Which pair is also listed as IBS-associated on p63?",
    "Celiac disease and fibromyalgia", ["Crohn's disease and PSC", "H. pylori and MALToma", "Campylobacter infection and IPSID"],
    "Celiac disease and fibromyalgia are both in the associations list.")
add(S1, 63, "recall", "Which neuropsychiatric/functional pair appears in the IBS associations list?",
    "Chronic fatigue syndrome and generalized anxiety disorder", ["Panic disorder and Parkinson disease", "Migraine and epilepsy", "Delirium and dementia"],
    "The page lists chronic fatigue syndrome and generalized anxiety disorder.")

add(S2, 63, "recall", "The sex distribution written for IBS is:",
    "Female > male", ["Male > female", "Equal by sex", "Male-only"],
    "The clinical-presentation section states female > male.")
add(S2, 63, "numeric", "The age group specified in the IBS clinical-presentation list is:",
    "Under 45 years", ["Under 20 years", "45–65 years", "Over 65 years"],
    "The page gives age <45 years.")
add(S2, 63, "recall", "Which symptom is marked as the most important in the IBS presentation?",
    "Abdominal pain", ["Nausea", "Belching", "Altered stool form alone"],
    "Abdominal pain is marked as the most important symptom.")
add(S2, 63, "numeric", "The page's Rome IV line requires recurrent abdominal pain at least how often?",
    "One episode per week", ["One episode per day", "One episode per month", "One episode per year"],
    "The book prints a minimum of one episode/week for ≥3 months. It omits Rome IV’s symptom-onset ≥6-month criterion; see audit/known-source-caveats.md.")
add(S2, 63, "numeric", "For how long does the p63 Rome IV line require the weekly pain pattern?",
    "At least three months", ["At least two weeks", "At least six months", "At least one year"],
    "The page states ≥3 months.")
add(S2, 63, "recall", "The Rome IV line requires the pain to be associated with at least how many of the listed stool/defecation features?",
    "Two", ["One", "All three", "None"],
    "The page says pain is associated with ≥2 of the listed features.")
add(S2, 63, "recall", "Which group contains the three associated features shown in the Rome IV line?",
    "Change in stool frequency; change in stool form; relation to defecation", ["Fever; blood in stool; raised ESR", "Steatorrhoea; weight loss; nocturnal diarrhoea", "Nausea; vomiting; early satiety"],
    "The three printed features are change in stool frequency, change in stool form/appearance and relation to defecation.")
add(S2, 63, "recall", "The typical pain location is described as:",
    "Crampy lower abdomen", ["Right upper quadrant", "Epigastrium only", "Left shoulder"],
    "The page describes crampy lower-abdominal pain.")
add(S2, 63, "numeric", "The pain frequency listed in the clinical section is:",
    "Episodic, about once per week", ["Continuous every day", "Once every six months", "Only after meals, several times per hour"],
    "The source notes episodic pain at approximately one episode per week.")
add(S2, 63, "recall", "Which pair of factors is listed as aggravating IBS pain?",
    "Stress and eating", ["Fasting and sleep", "Exercise and defecation", "Antibiotics and iron"],
    "Stress and eating are listed as aggravating factors.")
add(S2, 63, "recall", "The listed relieving factor for IBS abdominal pain is:",
    "Defecation", ["Fasting", "Vomiting", "Standing upright"],
    "Defecation is listed as a relieving factor.")
add(S2, 63, "recall", "Which symptom is called the most consistent in the IBS presentation?",
    "Altered bowel habits", ["Fever", "Steatorrhoea", "Jaundice"],
    "Altered bowel habits are marked as the most consistent symptom.")
add(S2, 63, "recall", "In the D+ pattern, diarrhoea is described as:",
    "Small-volume and associated with mucus", ["Large-volume and bloody", "Watery without mucus and high-volume", "Fatty, pale and bulky"],
    "D+ is diarrhoea-predominant with small-volume stool associated with mucus.")
add(S2, 63, "recall", "Which label is used for constipation-predominant IBS?",
    "C+", ["D+", "M+", "I+"],
    "The page labels constipation-predominant disease C+.")
add(S2, 63, "recall", "Which subtype is marked as most common and consists of prolonged constipation interrupted by episodic diarrhoea?",
    "M+ (mixed)", ["D+", "C+", "Post-infectious only"],
    "M+ is marked m/c and described as prolonged constipation interrupted by episodic diarrhoea.")
add(S2, 63, "scenario", "A patient with suspected IBS reports nocturnal diarrhoea and visible blood in stool. These findings are listed as:",
    "Features against IBS", ["The defining Rome IV association", "Typical of the D+ subtype", "Evidence for uncomplicated IBS"],
    "Nocturnal diarrhoea and blood in stools are listed against an IBS diagnosis.")
add(S2, 63, "recall", "Which symptom cluster should prompt reconsideration of IBS in the page's warning list?",
    "Steatorrhoea, weight loss, anaemia or malabsorption", ["Crampy lower-abdominal pain relieved by defecation", "Episodic pain aggravated by stress", "Mucus with small-volume D+ stool alone"],
    "Steatorrhoea, weight loss, anaemia and malabsorption are listed as features against IBS.")
add(S2, 63, "recall", "Which systemic finding is included among features against an IBS diagnosis?",
    "Fever", ["Belching", "Early satiety", "Postprandial fullness"],
    "Fever is included among features against IBS.")
add(S2, 63, "recall", "The inflammatory marker listed among features against IBS is:",
    "Increased ESR", ["Low ESR", "Low serum ferritin", "Elevated serum gastrin"],
    "The warning list includes increased ESR.")
add(S2, 63, "recall", "Besides abdominal pain and altered bowel habits, which additional presentation is listed?",
    "Abdominal distension and belching", ["Ascites and peripheral oedema", "Dysphagia and odynophagia", "Haematemesis and melaena"],
    "The clinical list includes abdominal distension and belching.")
add(S2, 63, "recall", "Which upper-GI symptom is listed under IBS clinical presentations?",
    "Dyspepsia/heartburn", ["Jaundice", "Haematemesis", "Cholestatic pruritus"],
    "Dyspepsia/heartburn is listed.")
add(S2, 63, "recall", "The remaining paired symptoms in the p63 presentation list are:",
    "Nausea and vomiting", ["Fever and chills", "Tenesmus and dyschezia", "Jaundice and pruritus"],
    "Nausea and vomiting are listed as clinical presentations.")

# ---------------------------------------------------------------------------
# Book p64 — mechanisms and lifestyle/FODMAP management
add(S3, 64, "recall", "The first pathophysiology theory on p64 is:",
    "Visceral hypersensitivity", ["Mucosal invasion", "Bile-acid overproduction", "Pancreatic exocrine failure"],
    "The first listed theory is visceral hypersensitivity.")
add(S3, 64, "scenario", "In the visceral-hypersensitivity model, minimal rectal distension can:",
    "Stimulate pain receptors because sensitivity is enhanced", ["Suppress pain receptors until very high volume", "Cause mucosal ulceration", "Inhibit colonic motor activity completely"],
    "The page says minimal rectal distension stimulates pain receptors due to enhanced sensitivity.")
add(S3, 64, "recall", "Compared with healthy controls, the graph demonstrates rectal hypersensitivity in IBS because pain/sensation occurs at:",
    "Lower distending volumes", ["Higher distending volumes only", "The same volume in every subject", "No measurable rectal volume"],
    "The IBS curve rises at lower distending volumes than the healthy-control curve.")
add(S3, 64, "recall", "Which additional motor abnormality appears second in the p64 pathophysiology list?",
    "Increased colonic motor potentials", ["Reduced oesophageal peristalsis", "Absent gastric slow waves", "Increased ileal bile-acid transport"],
    "The second listed mechanism is increased colonic motor potentials.")
add(S3, 64, "recall", "The central nervous system structure named in the IBS list is the:",
    "Cingulate cortex", ["Occipital cortex", "Cerebellar vermis", "Medulla oblongata"],
    "The page lists central activation of the cingulate cortex.")
add(S3, 64, "recall", "The cell population described as increased in IBS contains more:",
    "Serotonin in enterochromaffin cells", ["Histamine in parietal cells", "Gastrin in chief cells", "Iron in macrophages"],
    "The page lists an increase in serotonin-containing enterochromaffin cells.")
add(S3, 64, "recall", "Which ion-channel family is the fifth item in the pathophysiology list?",
    "Vanilloid channels (TRP-V1)", ["Voltage-gated calcium channels only", "Sodium-glucose transporters", "Chloride channels activated by cAMP"],
    "The final listed pathophysiology item is vanilloid channels (TRP-V1).")
add(S3, 64, "numeric", "The p64 lifestyle flowchart estimates improvement after diet and lifestyle modifications in:",
    "70% of cases", ["30% of cases", "50% of cases", "90% of cases"],
    "The flowchart gives improvement in 70% of cases.")
add(S3, 64, "numeric", "The proportion routed to medical management after no improvement with lifestyle measures is:",
    "30%", ["70%", "10%", "50%"],
    "No improvement is marked in 30% of cases, leading to medical management.")
add(S4, 64, "numeric", "The walking target listed under lifestyle management is:",
    "6,000–8,000 steps", ["2,000–3,000 steps", "10,000–12,000 steps", "15,000–18,000 steps"],
    "The page lists walking 6,000–8,000 steps.")
add(S4, 64, "recall", "The diet instruction written on p64 is to reduce:",
    "FODMAPs", ["All dietary protein", "Iron and vitamin C", "Long-chain triglycerides only"],
    "The lifestyle note says to reduce FODMAPs.")
add(S4, 64, "recall", "FODMAP is expanded on the page as:",
    "Fermentable oligo-, di-, monosaccharides and polyols", ["Fermentable proteins, minerals and peptides", "Fatty acids, bile salts and pancreatic enzymes", "Folate, oxyntic cells and mucins"],
    "The printed expansion is fermentable oligo-, di-, monosaccharides and polyols.")
add(S4, 64, "recall", "Which food is included in the p64 list of FODMAP sources?",
    "Apple", ["Chicken", "Egg white", "Plain fish"],
    "Examples listed include apple, mango, wheat, honey, legumes and cauliflower.")
add(S4, 64, "recall", "Which set contains only examples listed as FODMAP sources?",
    "Mango, wheat, honey, legumes and cauliflower", ["Rice, chicken, egg and fish", "Beef, butter, salt and water", "Oats, eggs, poultry and cheese"],
    "The source list is apple, mango, wheat, honey, legume and cauliflower, among others.")
add(S4, 64, "recall", "Which small-intestinal effect is shown for the FODMAP diagram?",
    "Water is drawn into the bowel, leading to diarrhoea", ["Water is removed from the lumen, causing constipation only", "Mucosal ulcers form and cause bleeding", "Bile acids are reabsorbed and cause jaundice"],
    "The figure shows water entering the bowel in the small intestine and a diarrhoeal outcome.")
add(S4, 64, "recall", "In the large intestine, FODMAPs are linked to which process?",
    "Bacterial fermentation", ["Pancreatic lipolysis", "Brush-border hydrolysis", "Hepatic conjugation"],
    "The large-intestine part of the diagram is labelled bacterial fermentation.")
add(S4, 64, "recall", "Which symptom cluster follows gas production in the large-intestinal FODMAP diagram?",
    "Bloating, distension, flatulence, abdominal pain and constipation", ["Haematemesis, jaundice, pruritus and fever", "Steatorrhoea, oedema, ascites and weight loss", "Tenesmus, dysuria, rash and arthritis"],
    "The diagram lists bloating, distension, flatulence, abdominal pain and constipation after gas production.")

# ---------------------------------------------------------------------------
# Book p65 — type-based treatment and table of drug effects
add(S5, 65, "management", "The p65 medical-management diagram divides IBS treatment first according to:",
    "IBS type", ["Patient age only", "Serum gastrin level", "Presence of H. pylori"],
    "The diagram says medical management is based on the type of IBS.")
add(S5, 65, "management", "Which drug is listed for diarrhoea-predominant (D+) IBS?",
    "Loperamide", ["Psyllium husk", "Lubiprostone", "Tegaserod"],
    "Loperamide is listed in the D+ branch.")
add(S5, 65, "recall", "For the D+ branch, the timing instruction for antispasmodics is:",
    "Thirty minutes before food", ["Immediately after every meal", "Only at bedtime", "One hour after food"],
    "The page says antispasmodics are taken 30 minutes before food.")
add(S5, 65, "recall", "Which additional general drug class appears in the D+ treatment list?",
    "Antidepressants", ["Anticoagulants", "Chelators", "Thrombolytics"],
    "Antidepressants are also listed in the D+ branch.")
add(S5, 65, "recall", "The p65 table labels the listed agents for diarrhoea-predominant IBS as:",
    "Obsolete drugs", ["First-line antibiotics", "Eradication regimens", "Diagnostic dyes"],
    "The table is introduced under the heading 'Obsolete drugs'.")
add(S5, 65, "recall", "Alosetron acts as a:",
    "5-HT3 antagonist", ["Guanylyl-cyclase agonist", "μ/κ agonist and δ antagonist", "Na+/H+ exchange blocker"],
    "The table lists alosetron as a 5-HT3 antagonist.")
add(S5, 65, "recall", "The adverse effect paired with alosetron is:",
    "Ischaemic colitis", ["Pancreatitis", "Cardiac toxicity", "Gastric intolerance"],
    "The table pairs alosetron with ischaemic colitis.")
add(S5, 65, "recall", "Eluxadoline's opioid-receptor profile is:",
    "μ- and κ-agonist, δ-antagonist", ["5-HT3 antagonist", "Guanylyl-cyclase agonist", "Na+/H+ exchange blocker"],
    "The table lists μ, κ agonism and δ antagonism for eluxadoline.")
add(S5, 65, "recall", "Which adverse effect is paired with eluxadoline in the p65 table?",
    "Pancreatitis", ["Ischaemic colitis", "Cardiac toxicity", "Oedema"],
    "The table pairs eluxadoline with pancreatitis.")
add(S5, 65, "recall", "The adverse effect listed beside tegaserod is:",
    "Cardiac toxicity", ["Pancreatitis", "Ischaemic colitis", "Hypoalbuminaemia"],
    "The table lists cardiac toxicity for tegaserod.")
add(S5, 65, "recall", "Which two stool-bulking agents are listed under C+ IBS?",
    "Psyllium husk and polyethylene glycol (PEG) laxatives", ["Loperamide and alosetron", "Eluxadoline and tegaserod", "Lubiprostone and tenapanor only"],
    "The C+ branch lists psyllium husk and PEG laxatives as stool-bulking agents.")
add(S5, 65, "recall", "Lubiprostone is described as a bicyclic fatty acid that activates a:",
    "Chloride channel", ["5-HT3 receptor", "Na+/H+ exchanger", "CCK-B receptor"],
    "The page describes lubiprostone as a bicyclic fatty acid and Cl− channel activator.")
add(S5, 65, "recall", "Linaclotide is identified as a:",
    "Guanylyl-cyclase agonist", ["5-HT3 antagonist", "Na+/H+ exchange blocker", "μ-opioid agonist"],
    "The page labels linaclotide a guanylyl-cyclase agonist.")
add(S5, 65, "recall", "Tenapanor's listed action is blockade of the:",
    "Na+/H+ exchanger", ["Cl− channel", "Guanylyl cyclase", "5-HT3 receptor"],
    "The page describes tenapanor as a Na+/H+ exchange blocker.")
add(S5, 65, "truefalse", "TRUE or FALSE — the p65 note says effectiveness of antibiotics, probiotics and prebiotics is not determined.",
    "True — the note says effectiveness is not determined", ["False — all three are established as effective", "False — the note addresses only loperamide", "True — but only for C+ IBS"],
    "The final note says effectiveness of antibiotics, probiotics and prebiotics is not determined.")

GUIDES = {
    S1: ("Definition & Associations", "IBS is presented as a functional bowel disorder/reaction to stress.\nAssociations: lactose intolerance, celiac disease, fibromyalgia, chronic fatigue and generalized anxiety.\nThe clinical list is more common in women and under age 45."),
    S2: ("Clinical Pattern, Rome IV & Red Flags", "Pain: crampy lower abdomen, at least weekly, aggravated by stress/eating and relieved by defecation.\nRome IV line as printed: ≥3 months and ≥2 of stool-frequency change, stool-form change or defecation relation; the source omits onset ≥6 months before diagnosis (see audit/known-source-caveats.md).\nNocturnal diarrhoea, blood, fever, weight loss, anaemia, malabsorption and raised ESR argue against IBS."),
    S3: ("Pathophysiology", "Visceral hypersensitivity, increased colonic motor potentials and cingulate activation are listed.\nThe page also notes serotonin-containing enterochromaffin cells and TRP-V1 channels.\nThe graph shows pain/sensation at lower rectal distending volumes in IBS."),
    S4: ("Lifestyle & FODMAPs", "Diet/lifestyle changes improve about 70%; walking target is 6,000–8,000 steps.\nReduce fermentable oligo-, di-, monosaccharides and polyols; examples include apple, mango, wheat, honey, legumes and cauliflower.\nWater draw in small bowel and fermentation/gas in colon explain the diagrammed symptoms."),
    S5: ("Type-Based Medical Management", "D+: loperamide, pre-meal antispasmodic, antidepressant; the table labels several drugs obsolete.\nC+: psyllium/PEG, lubiprostone, linaclotide and tenapanor.\nKeep each table drug linked to its action/adverse effect; the source says antibiotic/probiotic/prebiotic effectiveness is undetermined."),
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
