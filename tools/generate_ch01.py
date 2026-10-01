#!/usr/bin/env python3
"""Generate Chapter 1 Diarrhea (Book p1-5) for Medicine Vol 1"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
AUDIT = ROOT / "audit"
DATA.mkdir(exist_ok=True)
AUDIT.mkdir(exist_ok=True)

def q(id, sec, page, fmt, stem, opts, ans, exp):
    return {"id":id,"sec":sec,"page":page,"fmt":fmt,"q":stem,"opts":opts,"ans":ans,"exp":exp}

chapter = 1
title = "Diarrhea"
pageRange = "1-5"

sec1 = "Definition & Bristol Chart"
sec2 = "Physiology & Macronutrients"
sec3 = "Frequency Classification & Acute Etiology"
sec4 = "Chronic Diarrhea & Malassimilation"
sec5 = "Osmotic Diarrhea & Steatorrhea"
sec6 = "Steatorrhea Investigations"
sec7 = "Secretory Diarrhea & Stool Osmotic Gap"
sec8 = "Factitious & Anatomical Classification"
sec9 = "Approach to Diarrhea"

def nid(n):
    return f"MED-C1-{n:02d}"

questions = []

# PAGE 1
questions.append(q(nid(1), sec1, 1, "fillup",
    "Diarrhea is defined as stool water content >____ mL/24 hours.",
    ["100 mL/24 hours","200 mL/24 hours","300 mL/24 hours","500 mL/24 hours"],
    1, "Definition: Stool water content >200 mL/24 hours. (Book p1)"))
questions.append(q(nid(2), sec1, 1, "match",
    "Match the Bristol stool types to the book's clinical label — 1) Type 1 & 2 2) Type 3 & 4 3) Type 6 & 7 … A) Normal B) Constipation C) Diarrhea",
    ["1-B, 2-A, 3-C","1-A, 2-B, 3-C","1-B, 2-C, 3-A","1-C, 2-A, 3-B"],
    0, "According to Bristol stool chart: Type 1 & 2 = Constipation, Type 6 & 7 = Diarrhea; Types 3-4 are Normal. (Book p1)"))
questions.append(q(nid(3), sec1, 1, "recall",
    "Bristol Type 1 is described as separate hard lumps and is labelled as:",
    ["Mild constipation","Severe constipation","Normal","Lacking fibre"],
    1, "Type 1: Separate hard lumps = SEVERE CONSTIPATION on the Bristol chart. (Book p1)"))
questions.append(q(nid(4), sec1, 1, "recall",
    "Bristol Type 2 (lumpy and sausage like) corresponds to:",
    ["Normal","Lacking fibre","Mild constipation","Mild diarrhea"],
    2, "Type 2: Lumpy and sausage like = MILD CONSTIPATION. (Book p1)"))
questions.append(q(nid(5), sec1, 1, "recall",
    "Bristol Type 3 – ‘A sausage shape with cracks in the surface’ – is classified as:",
    ["Normal","Mild constipation","Severe constipation","Lacking fibre"],
    0, "Type 3: A sausage shape with cracks in the surface = NORMAL. (Book p1)"))
questions.append(q(nid(6), sec1, 1, "recall",
    "Bristol Type 4 – ‘Like a smooth, soft sausage or snake’ – is:",
    ["Mild diarrhea","Severe diarrhea","Lacking fibre","Normal"],
    3, "Type 4: Like a smooth, soft sausage or snake = NORMAL. (Book p1)"))
questions.append(q(nid(7), sec1, 1, "oddoneout",
    "Pick the ODD ONE OUT — one pairing is NOT as printed for the Bristol chart:",
    ["Type 5 – Soft blobs with clear-cut edges – LACKING FIBRE","Type 6 – Mushy consistency with ragged edges – MILD DIARRHEA","Type 7 – Liquid consistency with no solid pieces – SEVERE DIARRHEA","Type 5 – Soft blobs with clear-cut edges – SEVERE CONSTIPATION"],
    3, "Type 5 is Soft blobs with clear-cut edges = LACKING FIBRE, not severe constipation; the other three are as printed. (Book p1)"))
questions.append(q(nid(8), sec1, 1, "fillup",
    "Bristol Type 5 (soft blobs with clear-cut edges) is labelled ____.",
    ["Normal","Lacking fibre","Mild diarrhea","Severe diarrhea"],
    1, "Type 5: Soft blobs with clear-cut edges = LACKING FIBRE. (Book p1)"))
questions.append(q(nid(9), sec1, 1, "recall",
    "Bristol Type 6 – mushy consistency with ragged edges – indicates:",
    ["Normal","Lacking fibre","Mild diarrhea","Severe constipation"],
    2, "Type 6: Mushy consistency with ragged edges = MILD DIARRHEA. (Book p1)"))
questions.append(q(nid(10), sec1, 1, "scenario",
    "A patient reports stools that are entirely liquid with no solid pieces. By Bristol chart this is Type 7 and the book labels it:",
    ["Mild diarrhea","Normal","Lacking fibre","Severe diarrhea"],
    3, "Type 7: Liquid consistency with no solid pieces = SEVERE DIARRHEA. (Book p1)"))
questions.append(q(nid(11), sec2, 1, "match",
    "Match the phases of absorption as book-ordered — 1) Luminal 2) Mucosal 3) Post mucosal … A) Post mucosal B) Luminal C) Mucosal",
    ["1-B, 2-C, 3-A","1-A, 2-B, 3-C","1-C, 2-A, 3-B","1-B, 2-A, 3-C"],
    0, "Physiology of absorption: 1. Luminal, 2. Mucosal, 3. Post mucosal. (Book p1)"))
questions.append(q(nid(12), sec2, 1, "truefalse",
    "TRUE or FALSE — the book states that the mucosal phase occurs mainly in the small intestine and accounts for maximum absorption.",
    ["True — small intestine (majority), maximum absorption","False — mucosal phase is colonic","False — maximum absorption is luminal","True — but post mucosal is majority"],
    0, "Mucosal: Small intestine (majority), maximum absorption. (Book p1)"))
questions.append(q(nid(13), sec2, 1, "recall",
    "Among macronutrients listed, which is noted as most calorie-dense?",
    ["Proteins","Carbohydrates","Fat","Fiber"],
    2, "Fat: most calorie dense nutrient. (Book p1)"))
questions.append(q(nid(14), sec2, 1, "truefalse",
    "TRUE or FALSE — fat is the most specific nutrient affected in malabsorption.",
    ["True — fat is the most specific marker","False — carbohydrate is most specific","False — protein is most specific","True — but only in pancreatic insufficiency"],
    0, "Fat: most specific nutrient affected in malabsorption. (Book p1)"))
questions.append(q(nid(15), sec2, 1, "oddoneout",
    "Three are listed under ‘macronutrients for absorption’ in the book. Pick the ODD ONE OUT:",
    ["Fat","Carbohydrates","Proteins","Vitamins"],
    3, "The book lists Fat, Carbohydrates, Proteins under macronutrients; Vitamins is not listed there. (Book p1)"))
questions.append(q(nid(16), sec3, 1, "numeric",
    "By Frequency Classification, ‘Acute’ diarrhea is defined as duration:",
    ["<2 weeks (Nuisance symptom)","<4 weeks","<1 week",">4 weeks"],
    0, "Frequency Classification: Acute <2 weeks (Nuisance symptom). (Book p1)"))
questions.append(q(nid(17), sec3, 1, "match",
    "Match the frequency label to duration — 1) Acute 2) Persistent 3) Chronic … A) >4 weeks B) <2 weeks C) >2 weeks",
    ["1-B, 2-C, 3-A","1-A, 2-B, 3-C","1-C, 2-B, 3-A","1-B, 2-A, 3-C"],
    0, "Acute <2 weeks, Persistent >2 weeks, Chronic >4 weeks. (Book p1)"))
questions.append(q(nid(18), sec3, 1, "recall",
    "The most common cause of acute diarrhea overall, per the book, is:",
    ["Bacterial toxin","Parasitic","Viral infection","Drug-induced"],
    2, "Acute diarrhea: Infectious: Viral infection (m/c). (Book p1)"))
questions.append(q(nid(19), sec3, 1, "scenario",
    "A 28-year-old food handler develops acute watery diarrhea for 12 hours after a buffet; no blood. The book’s most common viral cause in adults is:",
    ["Rotavirus","Norovirus","Adenovirus","Enterovirus"],
    1, "m/c in adults: Norovirus. (Book p1)"))
questions.append(q(nid(20), sec3, 1, "scenario",
    "A 2-year-old with acute watery diarrhea, low-grade fever, self-limited course. The book’s most common viral cause in children is:",
    ["Norovirus","Rotavirus","Sapovirus","Astrovirus"],
    1, "m/c in children: Rotavirus. (Book p1)"))
questions.append(q(nid(21), sec3, 1, "truefalse",
    "TRUE or FALSE — acute viral diarrhea as described is typically self-limiting.",
    ["True — self-limiting","False — requires antibiotics","False — always chronic","True — but only in children"],
    0, "Acute viral diarrhea is listed as Self-limiting. (Book p1)"))
questions.append(q(nid(22), sec4, 2, "match",
    "Match chronic diarrhea D/d to etiology — 1) Osmotic 2) Secretory 3) Inflammatory … A) Inflammatory bowel disease B) Malabsorption C) Tumor / Toxin",
    ["1-B, 2-C, 3-A","1-A, 2-B, 3-C","1-C, 2-A, 3-B","1-B, 2-A, 3-C"],
    0, "Chronic diarrhea table: Osmotic → malabsorption, Secretory → Tumor/Toxin, Inflammatory → Inflammatory bowel disease. (Book p2)"))
questions.append(q(nid(23), sec4, 2, "fillup",
    "Malassimilation = ____ + malabsorption.",
    ["Maldigestion","Maldistribution","Malnutrition","Malrotation"],
    0, "Malassimilation: maldigestion + malabsorption. (Book p2)"))
questions.append(q(nid(24), sec4, 2, "fillup",
    "Malassimilation is diminished intestinal digestion/absorption of ____.",
    ["One or more nutrients","Fat alone","Water alone","Vitamin B12 alone"],
    0, "Diminished intestinal digestion/absorption of one or more nutrients. (Book p2)"))
questions.append(q(nid(25), sec5, 2, "recall",
    "Which is described as the most consistent clinical symptom of malabsorption under Pathological Classification?",
    ["Hematemesis","Osmotic diarrhea","Constipation","Jaundice"],
    1, "1. OSMOTIC DIARRHEA — most consistent clinical symptom of malabsorption. (Book p2)"))
questions.append(q(nid(26), sec5, 2, "scenario",
    "A patient passes pale, bulky, fatty, malodorous, greasy stools that float. The book terms this hallmark of malabsorption as:",
    ["Melena","Steatorrhea","Hematochezia","Lientery"],
    1, "Steatorrhea: Hallmark of malabsorption. Definition: Passing of pale, bulky, fatty, malodorous, greasy stools. (Book p2)"))
questions.append(q(nid(27), sec5, 2, "truefalse",
    "TRUE or FALSE — the book lists diarrhea as the most consistent clinical finding in steatorrhea.",
    ["True — diarrhea (most consistent clinical finding)","False — weight loss is most consistent","False — steatorrhea is always painless so diarrhea is rare","True — but only in children"],
    0, "Clinical presentation: Diarrhea (most consistent clinical finding) in steatorrhea. (Book p2)"))
questions.append(q(nid(28), sec5, 2, "match",
    "Order the osmotic diarrhea pathogenesis as printed — 1) ↓ Fat absorption in small intestine 2) Unabsorbed macronutrients ↑ stool osmolality (osmotically active) in colon 3) Stool draws water from large intestinal epithelial cells … A) Stool draws water B) ↓ Fat absorption C) ↑ Stool osmolality",
    ["1-B, 2-C, 3-A","1-A, 2-B, 3-C","1-C, 2-B, 3-A","1-B, 2-A, 3-C"],
    0, "Pathology: ↓ fat absorption in small intestine → In colon → Unabsorbed macronutrients ↑ stool osmolality (osmotically active) → Stool draws water from large intestinal epithelial cells → Osmotic diarrhea. (Book p2)"))
questions.append(q(nid(29), sec6, 2, "recall",
    "Gold standard investigation for steatorrhea per the book is:",
    ["Qualitative Sudan stain","72 hour fecal fat test","Fecal elastase","D-xylose test"],
    1, "Investigations: 1. 72 hour fecal fat test: Gold standard. (Book p2)"))
questions.append(q(nid(30), sec6, 2, "numeric",
    "For the 72-hour fecal fat test, the book’s prescribed fat input is:",
    ["40 g/day","100 g/day","60 g/day","200 g/day"],
    1, "Procedure: Fat input = 100 g/day. (Book p2)"))
questions.append(q(nid(31), sec6, 2, "numeric",
    "Normal fecal fat excretion on the 72-hour test is:",
    ["<7 g/day","<14 g/day","<3 g/day","<20 g/day"],
    0, "Normal: <7 g/day. (Book p2)"))
questions.append(q(nid(32), sec6, 2, "fillup",
    "Steatorrhea is diagnosed if fecal fat is >7 g/day for 3 days on ____.",
    ["D1, D2, D3","D3, D4, D5","D2, D3, D4","Any 2 days"],
    1, ">7 g/day for 3 days (D3, D4, D5) = Steatorrhea. (Book p2)"))
questions.append(q(nid(33), sec6, 2, "truefalse",
    "TRUE or FALSE — stool fat excretion ≥7% also qualifies as steatorrhea by the book’s criteria.",
    ["True — Stool fat excretion ≥7%","False — threshold is ≥10%","False — only quantitative grams matter","True — but only with Sudan stain"],
    0, "Stool fat excretion ≥7% → Steatorrhea. (Book p2)"))
questions.append(q(nid(34), sec6, 2, "match",
    "Match the qualitative stool fat test to its stain — 1) Sudan III 2) Sudan IV 3) Oil red O … A) Oil red O B) Sudan III C) Sudan IV",
    ["1-B, 2-C, 3-A","1-A, 2-B, 3-C","1-C, 2-A, 3-B","1-B, 2-A, 3-C"],
    0, "Qualitative stool fat: Sudan III, Sudan IV, Oil red O. (Book p2)"))
questions.append(q(nid(35), sec7, 3, "recall",
    "Which pair is listed under toxins causing secretory diarrhea?",
    ["ETEC & V. cholera (heat labile toxin)","Shigella & Salmonella","Entamoeba & Giardia","C. difficile toxin A/B alone"],
    0, "Secretory: a. Toxins → ETEC, V. cholera (heat labile toxin). (Book p3)"))
questions.append(q(nid(36), sec7, 3, "truefalse",
    "TRUE or FALSE — enteropathogenic virus (rotavirus) is listed under secretory diarrhea toxin etiology.",
    ["True — listed as toxin-mediated secretory cause","False — rotavirus is osmotic","False — listed under inflammatory","True — but only for adults"],
    0, "Toxins → Enteropathogenic virus (rotavirus) is listed. (Book p3)"))
questions.append(q(nid(37), sec7, 3, "scenario",
    "A patient with chronic watery diarrhea, hypokalemia and non-anion gap acidosis with a pancreatic tumor is described. The book’s tumor and triad are:",
    ["Gastrinoma with Zollinger-Ellison","VIPoma with WDHA (Watery Diarrhea, Hypokalemia, Acidosis)","Somatostatinoma with steatorrhea","Insulinoma with Whipple triad"],
    1, "Tumours: VIPoma → Watery Diarrhoea → WDHA syndrome with Hypokalemia and Acidosis triangle. (Book p3)"))
questions.append(q(nid(38), sec7, 3, "truefalse",
    "TRUE or FALSE — in secretory diarrhea the book notes ‘No structural damage seen.’",
    ["True — No structural damage seen","False — villous atrophy is typical","False — ulcerations are characteristic","True — but only for osmotic"],
    0, "Note: No structural damage seen (secretory diarrhea). (Book p3)"))
questions.append(q(nid(39), sec7, 3, "match",
    "Match the stool osmotic gap category — 1) Osmotic diarrhea 2) Secretory diarrhea … A) Normal/decreased (<50 mOsm/kg), ↑ stool Na⁺+K⁺ B) Increased (>100 mOsm/kg)",
    ["1-B, 2-A","1-A, 2-B","1-B, 2-B","1-A, 2-A"],
    0, "Stool osmotic gap: Osmotic Increased (>100), Secretory Normal/decreased (<50), ↑ stool Na+ + K+ (By toxins). (Book p3)"))
questions.append(q(nid(40), sec7, 3, "scenario",
    "A patient’s diarrhea improves dramatically on fasting. The comparison table suggests:",
    ["Secretory diarrhea (no change on fasting)","Osmotic diarrhea (Improvement)","Factitious diarrhea","Inflammatory diarrhea"],
    1, "Response to fasting: Osmotic → Improvement, Secretory → No change. (Book p3)"))
questions.append(q(nid(41), sec7, 3, "numeric",
    "Osmotic diarrhea stool pH is typically <5.5 due to fermentation of unabsorbed carbohydrates to acids; secretory diarrhea stool pH is:",
    [">6.0","<4.5","<5.0","<6.5 but >5.5"],
    0, "Stool pH: Osmotic <5.5 (Fermentation… → Acids), Secretory >6.0. (Book p3)"))
questions.append(q(nid(42), sec7, 3, "fillup",
    "Stool osmotic gap = 290 − 2 × (stool ____ + stool ____).",
    ["Na⁺ + K⁺","Cl⁻ + HCO₃⁻","Na⁺ + Cl⁻","K⁺ + urea"],
    0, "Note: Stool osmotic gap = measured osmolality - calculated; 290 - 2 (Stool Na⁺ + K⁺). (Book p3)"))
questions.append(q(nid(43), sec7, 3, "numeric",
    "Normal stool osmotic gap is:",
    ["50–100 mOsm/kg","10–30 mOsm/kg","150–200 mOsm/kg","0–10 mOsm/kg"],
    0, "Normal: 50-100 mOsm/kg. (Book p3)"))
questions.append(q(nid(44), sec7, 3, "scenario",
    "An adolescent female with chronic diarrhea, no weight gain, fatigue, and normal supervised stool osmolality but very low unsupervised osmolality. The book’s clinical picture fits:",
    ["Osmotic diarrhea from lactase deficiency","Secretory diarrhea from VIPoma","Factitious diarrhea","Inflammatory bowel disease"],
    2, "Factitious: Adolescent female, Chronic diarrhea, Fatigue, Weight loss. (Book p3)"))
questions.append(q(nid(45), sec8, 4, "numeric",
    "In factitious diarrhea findings, unsupervised stool (mixed with water) osmolality is about ____, supervised is about 279.",
    ["~16 mOsm/kg","~100 mOsm/kg","~150 mOsm/kg","~290 mOsm/kg"],
    0, "Unsupervised (mixed with water) Very low (~16 mOsm/kg), Supervised Normal (~279). (Book p4)"))
questions.append(q(nid(46), sec8, 4, "match",
    "Match etiology to site in Anatomical Classification — 1) Osmotic/Secretory (ETEC, Vibrio cholera) 2) Invasive organisms (Shigella) / Ulcerative colitis inflammation … A) Large intestinal diarrhea B) Small intestinal diarrhea",
    ["1-B, 2-A","1-A, 2-B","1-B, 2-B","1-A, 2-A"],
    0, "Small intestinal: Osmotic, Secretory - ETEC, Vibrio cholera; Large intestinal: Invasive (Shigella), Inflammation: ulcerative colitis. (Book p4)"))
questions.append(q(nid(47), sec8, 4, "recall",
    "By the Small vs Large table, stool volume is:",
    ["Large in small intestinal (↓ nutrient absorption) vs Small in large intestinal","Small in small intestinal vs Large in large intestinal","Equal in both","Decreased only in colonic"],
    0, "Clinical presentation: Volume - Large (↓ nutrient absorption) in small intestinal, Small in large intestinal. (Book p4)"))
questions.append(q(nid(48), sec8, 4, "truefalse",
    "TRUE or FALSE — both small and large intestinal diarrheas are listed as ‘watery’ in consistency per the table.",
    ["True — both are listed as watery","False — large is bloody","False — small is formed","True — but large is semi-solid"],
    0, "Consistency: Small → watery, Large → watery. (Book p4)"))
questions.append(q(nid(49), sec8, 4, "recall",
    "Frequency/urgency in the anatomical table is:",
    ["↓ in small intestinal, ↑ in large intestinal","↑ in both","↓ in both","↑ in small, ↓ in large"],
    0, "Frequency/urgency: Small ↓, Large ↑. (Book p4)"))
questions.append(q(nid(50), sec8, 4, "truefalse",
    "TRUE or FALSE — pus/blood/mucus is Absent in small intestinal diarrhea and Present in large intestinal diarrhea.",
    ["True — Absent vs Present","False — opposite","False — present in both","True — but only with fever"],
    0, "Pus/blood/mucus: Small Absent, Large Present. (Book p4)"))
questions.append(q(nid(51), sec8, 4, "recall",
    "Tenesmus is:",
    ["Present in small, Absent in large","Absent in small, Present in large","Absent in both","Present in both"],
    1, "Tenesmus: Small Absent, Large Present. (Book p4)"))
questions.append(q(nid(52), sec8, 4, "recall",
    "Dyschezia is:",
    ["Absent in small intestinal, Present in large intestinal","Present in small, Absent in large","Present in both","Absent in both"],
    0, "Dyschezia: Small Absent, Large Present. (Book p4)"))
questions.append(q(nid(53), sec8, 4, "recall",
    "Abdominal pain is:",
    ["Absent in small intestinal, Present in large intestinal","Present in both","Absent in both","Present in small, Absent in large"],
    0, "Abdominal pain: Small Absent, Large Present. (Book p4)"))
questions.append(q(nid(54), sec8, 4, "recall",
    "Fever is:",
    ["Absent in small intestinal diarrhea, Present in large intestinal diarrhea","Present in small, Absent in large","Present in both","Absent in both"],
    0, "Fever: Small Absent, Large Present. (Book p4)"))
questions.append(q(nid(55), sec8, 4, "oddoneout",
    "Three are Present in both small and large intestinal diarrhea; pick the ODD ONE OUT that is NOT present in both:",
    ["Abdominal cramps","Bloating","Fever","Abdominal cramps and Bloating are both Present"],
    2, "Abdominal cramps: Present in both; Bloating: Present in both; Fever: Absent in small, Present in large — so fever is the odd one. (Book p4)"))
questions.append(q(nid(56), sec8, 4, "truefalse",
    "TRUE or FALSE — bloating is Present in both small and large intestinal diarrhea.",
    ["True — Present in both","False — absent in small","False — absent in large","True — but rare in large"],
    0, "Bloating: Present in both. (Book p4)"))
questions.append(q(nid(57), sec8, 4, "scenario",
    "A patient with chronic large volume diarrhea for 6 months has lost 8 kg; vomiting is occasional. The table suggests this fits:",
    ["Large intestinal diarrhea (weight loss rare)","Small intestinal diarrhea (weight loss Present if persistent, vomiting maybe present, steatorrhoea Present)","Factitious diarrhea","Secretory diarrhea only"],
    1, "Weight loss: Small intestinal Present (if persistent), Large Rare; Vomiting maybe present in small, Rare in large; Steatorrhoea Present in small, Absent in large. (Book p4)"))
questions.append(q(nid(58), sec8, 4, "recall",
    "Vomiting in the anatomical classification is:",
    ["Maybe present in small intestinal, Rare in large intestinal","Rare in small, Maybe present in large","Present in both","Absent in both"],
    0, "Vomiting: Small maybe present, Large Rare. (Book p4)"))
questions.append(q(nid(59), sec8, 4, "truefalse",
    "TRUE or FALSE — steatorrhoea is Present in small intestinal diarrhea and Absent in large intestinal diarrhea.",
    ["True — Present vs Absent","False — opposite","False — present in both","True — but only in colonic"],
    0, "Steatorrhoea: Small Present, Large Absent. (Book p4)"))
questions.append(q(nid(60), sec9, 5, "recall",
    "By ‘Approach to Diarrhea’ flowchart, diarrhea <2 weeks suggests:",
    ["Inflammatory ulcerative colitis","Osmotic malabsorption","Infection","VIPoma"],
    2, "Duration <2 weeks → Infection. (Book p5)"))
questions.append(q(nid(61), sec9, 5, "match",
    "Match the <2 weeks infection by site — 1) Small intestine (Large volume): Viral m/c, ETEC, Cholera 2) Large intestine (Fever, pain abdomen, blood, mucus) … A) Invasive: Shigella, Non-typhoid salmonella, Campylobacter B) Viral m/c, ETEC, Cholera (Self limiting)",
    ["1-B, 2-A","1-A, 2-B","1-B, 2-B","1-A, 2-A"],
    0, "<2 weeks: Small intestine (Large volume): Viral m/c, ETEC, Cholera → Self limiting; Large intestine (Fever, pain, blood, mucus): Invasive: Shigella, Non typhoid salmonella, Campylobacter. (Book p5)"))
questions.append(q(nid(62), sec9, 5, "management",
    "A traveler with 1-day history of large volume watery diarrhea, no fever/blood, likely viral/ETEC/cholera. The book’s flowchart implies:",
    ["Immediate colonoscopy","Self limiting — supportive care","Start mesalamine for UC","Check VIPoma levels"],
    1, "Small intestine viral/ETEC/Cholera → Self limiting. (Book p5)"))
questions.append(q(nid(63), sec9, 5, "match",
    "For diarrhea >4 weeks, match — 1) Small intestine - Osmotic 2) Small intestine - Secretory 3) Large intestine - Inflammatory … A) VIPoma B) ↑ stool osmotic gap, Improves on fasting C) Ulcerative colitis",
    ["1-B, 2-A, 3-C","1-A, 2-B, 3-C","1-C, 2-B, 3-A","1-B, 2-C, 3-A"],
    0, ">4 weeks: Small → Osmotic: ↑ stool osmotic gap, Improves on fasting; Secretory: VIPoma; Large → Inflammatory: ulcerative colitis. (Book p5)"))
questions.append(q(nid(64), sec9, 5, "scenario",
    "A patient has chronic watery diarrhea for 6 weeks with hypokalemia. Fasting does NOT improve stool output. Workup for VIPoma is planned. This matches which branch of the approach flowchart?",
    ["Small intestinal osmotic (>100 gap, improves on fasting)","Small intestinal secretory (VIPoma, no improvement on fasting)","Large intestinal inflammatory (ulcerative colitis)","Acute infectious small intestinal (viral)"],
    1, "Small intestinal Secretory: VIPoma (diarrhea persists fasting) vs Osmotic: ↑ gap, Improves on fasting. (Book p5)"))
questions.append(q(nid(65), sec9, 5, "scenario",
    "A patient has >4 weeks diarrhea with fever, abdominal pain, blood/mucus, urgency, and tenesmus. Approach flowchart points to:",
    ["Small intestinal osmotic with lactase deficiency","Large intestinal inflammatory: ulcerative colitis","Factitious diarrhea","Self-limiting viral"],
    1, "Large intestine >4 weeks → Inflammatory: ulcerative colitis (presents with Fever, pain abdomen, blood, mucus). (Book p5)"))
questions.append(q(nid(66), sec9, 5, "oddoneout",
    "Pick the ODD ONE OUT — not listed under invasive organisms for Large intestinal <2 weeks infection:",
    ["Shigella","Non typhoid salmonella","Campylobacter","ETEC"],
    3, "Invasive organisms for Large intestine: Shigella, Non typhoid salmonella, Campylobacter; ETEC is Small intestinal (Large volume). (Book p5)"))

# Build units dict
sec_to_qs = {}
for qq in questions:
    sec_to_qs.setdefault(qq["sec"], []).append(qq["id"])

ordered_secs = [sec1, sec2, sec3, sec4, sec5, sec6, sec7, sec8, sec9]
unit_titles_guides = {
    sec1: ("Definition & Bristol Chart","Definition >200 mL/24 h and Bristol Types 1-7.\nLink Type numbers to stool form and clinical label.\nSevere constipation (1) through severe diarrhea (7) in strict order."),
    sec2: ("Physiology & Macronutrients","Luminal → Mucosal (small intestine, maximum) → Post mucosal.\nFat is most calorie-dense and most specific in malabsorption.\nList carbs and proteins as the other macronutrients."),
    sec3: ("Frequency Classification & Acute Etiology","Acute <2w (nuisance), Persistent >2w, Chronic >4w.\nAcute viral m/c overall: Norovirus adults, Rotavirus children, self-limiting.\nClassify by duration first in the flowchart."),
    sec4: ("Chronic Diarrhea & Malassimilation","Chronic D/d: Osmotic→malabsorption, Secretory→tumor/toxin, Inflammatory→IBD.\nMalassimilation = maldigestion + malabsorption.\nDiminished digestion/absorption of one or more nutrients."),
    sec5: ("Osmotic Diarrhea & Steatorrhea","Osmotic = most consistent symptom of malabsorption.\nSteatorrhea = hallmark: pale bulky fatty malodorous greasy stools.\nPathology: ↓ fat absorption → ↑ stool osmolality → draws water → osmotic diarrhea."),
    sec6: ("Steatorrhea Investigations","72-h fecal fat = gold standard with 100 g/day fat input.\nNormal <7 g/day; steatorrhea >7 g/d for 3 d (D3-D5) or ≥7% excretion.\nQualitative: Sudan III, Sudan IV, Oil red O."),
    sec7: ("Secretory Diarrhea & Stool Osmotic Gap","Secretory: ETEC/V. cholera heat-labile toxin + rotavirus; VIPoma→WDHA + hypoK + acidosis; no structural damage.\nGap table: Osmotic >100 + pH<5.5 vs Secretory <50 + ↑Na+K + pH>6.0 + no change on fasting.\nFormula 290−2(Na⁺+K⁺), normal 50-100; factitious case adolescent female."),
    sec8: ("Factitious & Anatomical Classification","Factitious unsupervised ~16 vs supervised ~279.\nSmall vs Large etiology + full clinical table (volume, consistency, frequency, pus/blood/mucus, tenesmus, dyschezia, pain, fever, cramps, bloating, weight loss, vomiting, steatorrhoea) in order.\nWeight loss/vomiting/steatorrhoea distinguish persistent small intestinal."),
    sec9: ("Approach to Diarrhea","Duration first: <2w = infection, >4w = small vs large.\n<2w Small (large volume, viral/ETEC/cholera, self-limiting) vs Large (fever/pain/blood, Shigella etc).\n>4w Small osmotic (>100 gap, improves) vs secretory (VIPoma) vs Large inflammatory (UC)."),
}

unit_list=[]
n=1
for sec in ordered_secs:
    qs = sec_to_qs.get(sec, [])
    if not qs:
        continue
    title_u, guide = unit_titles_guides[sec]
    unit_list.append({
        "id":f"MED-U1-{n}",
        "ch":1,
        "n":n,
        "title":title_u,
        "sec":sec,
        "guide":guide,
        "qs":qs
    })
    n+=1

chapter_json = {
    "chapter":1,
    "title":"Diarrhea",
    "pageRange":pageRange,
    "questions":questions,
    "units":unit_list
}

DATA.joinpath("ch01.json").write_text(json.dumps(chapter_json, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote ch01.json with {len(questions)} questions and {len(unit_list)} units")

ledger=[]
for qq in questions:
    ledger.append({
        "chapter":1,
        "page":qq["page"],
        "point": f"{qq['sec']} — {qq['id']}: {qq['q'][:70]}",
        "question":qq["id"]
    })

AUDIT.joinpath("coverage.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote coverage.json with {len(ledger)} entries")

page_map = {
    "01.pdf": {"pdfStart":13,"bookStart":1,"pdfEnd":129,"bookEnd":117,"offset":12,"note":"12 front-matter sheets; Book p = PDF page -12"},
    "02.pdf": {"pdfStart":1,"bookStart":118,"pdfEnd":130,"bookEnd":247,"offset":-117,"note":"Book p = PDF page +117"},
    "03.pdf": {"pdfStart":1,"bookStart":248,"pdfEnd":128,"bookEnd":375,"offset":247,"note":"Book p = PDF page +247; PDF129-131 are blank/end matter"}
}
AUDIT.joinpath("page-map.json").write_text(json.dumps(page_map, ensure_ascii=False, indent=2), encoding="utf-8")
print("Wrote page-map.json")
