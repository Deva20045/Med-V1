#!/usr/bin/env python3
"""Generate Chapter 7 Infectious Diarrhoea (Book p46–51).

Source: uploads/01.pdf PDF58–63. Printed pages were visually checked in order;
questions preserve that sequence. Explanations cite the corresponding book page.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 7
TITLE = "Infectious Diarrhoea"
PAGES = "46-51"

S1 = "Infectious Diarrhoea: Definitions & Patterns"
S2 = "Small- and Large-Bowel Organisms"
S3 = "Preformed-Toxin Food Poisoning"
S4 = "Vibrio, ETEC & Secretory Diarrhoea"
S5 = "HUS and Shigella"
S6 = "Salmonella and Campylobacter"
S7 = "Clostridioides difficile Enterocolitis"
RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    rng = random.Random(7000 + CHAPTER * 10000 + len(RAW))
    rng.shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2
        assert sum(o.startswith("False") for o in options) == 2
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p46 — introduction, duration/site classification, and small/large bowel
add(S1, 46, "recall", "In the book's opening definition, acute diarrhoea lasting no more than two weeks is considered:",
    "Infectious unless proved otherwise", ["Non-infectious unless a stool culture is positive", "Inflammatory only when blood is visible", "Protozoal until an organism is identified"],
    "Acute diarrhoea (≤2 weeks) is considered infectious unless proved otherwise.")
add(S1, 46, "numeric", "Which duration boundary is used in the opening definition of acute diarrhoea?",
    "≤2 weeks", ["<1 week", ">2 weeks", "≥4 weeks"],
    "The introductory definition uses acute diarrhoea of ≤2 weeks.")
add(S1, 46, "recall", "The first classification diagram organizes infectious diarrhoea by:",
    "Duration and severity", ["Stool colour and pH", "Anatomical site and electrolyte loss", "Exposure history and immune status"],
    "The first diagram is headed 'Based on duration and severity'.")
add(S1, 46, "scenario", "A brief episode is placed in the diagram's benign, short-lasting, self-limiting branch. Which class is written at its end?",
    "Viral", ["Bacterial", "Protozoal", "Enterocolitic"],
    "The <1-week benign, short-lasting, self-limiting branch ends in viral diarrhoea.")
add(S1, 46, "scenario", "In the same duration diagram, the <1-week episode marked 'complicated' leads to which broad cause?",
    "Bacterial", ["Viral", "Protozoal", "Non-infectious"],
    "The complicated <1-week branch is labelled bacterial.")
add(S1, 46, "numeric", "The diagram associates diarrhoea lasting more than one week with which broad group?",
    "Protozoal", ["Viral", "Bacterial", "Medication-related"],
    "The >1-week branch in the duration diagram is labelled protozoal.")
add(S1, 46, "recall", "The site-based classification distinguishes small bowel, large bowel, and:",
    "Enterocolitis involving small and large bowel", ["Gastric-colonic diarrhoea", "Pancreatic-enteric diarrhoea", "Ileal-only diarrhoea"],
    "The third site category is enterocolitis (small bowel + large bowel).")
add(S1, 46, "recall", "In the site classification, Yersinia is singled out for causing:",
    "Severe ileocolitis", ["Isolated proctitis", "Painless secretory diarrhoea", "Gastric inflammation without bowel disease"],
    "Yersinia is listed under enterocolitis and causes severe ileocolitis.")
add(S1, 46, "scenario", "Right-lower-quadrant tenderness during Yersinia ileocolitis is emphasized because it can mimic:",
    "Acute appendicitis", ["Biliary colic", "Pancreatitis", "Renal colic"],
    "The note states that severe Yersinia ileocolitis produces right-lower-quadrant tenderness and mimics appendicitis.")
add(S1, 46, "recall", "Which stool pattern best fits the small-bowel column on the clinical-features table?",
    "Large-volume watery stool without blood, pus or mucus", ["Small-volume bloody stool with urgency and tenesmus", "Frequent stools with fecal leukocytes and mucus", "Painless formed stool streaked with blood"],
    "Small-bowel diarrhoea is described as large-volume and watery, without blood, pus, mucus, increased frequency, urgency or tenesmus.")
add(S1, 46, "scenario", "A patient has small-volume bloody diarrhoea, abdominal pain and fecal leukocytes. The table localizes this pattern to the:",
    "Large bowel", ["Small bowel", "Stomach", "Pancreas"],
    "Fever, small-volume bloody diarrhoea, abdominal pain and fecal leukocytes are in the large-bowel column.")
add(S1, 46, "match", "Match each stool pattern to its site — 1) Large-volume watery stool without blood, pus or mucus 2) Small-volume bloody stool with fecal leukocytes … A) Large bowel B) Small bowel",
    "1-B, 2-A", ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "The table places large-volume watery non-bloody stool in small-bowel disease and small-volume bloody stool with fecal leukocytes in large-bowel disease.")
add(S1, 46, "recall", "Among adults, which virus is marked as the most common cause in the small-bowel column?",
    "Norovirus", ["Rotavirus", "Cytomegalovirus", "Adenovirus"],
    "Norovirus is marked most common in adults.")
add(S1, 46, "recall", "The virus marked most common in children is:",
    "Rotavirus", ["Norovirus", "Cytomegalovirus", "Astrovirus"],
    "Rotavirus is marked most common in children.")
add(S1, 46, "scenario", "A post-transplant patient develops sore throat, diarrhoea and leucopenia. Which virus is named beside this presentation?",
    "Cytomegalovirus", ["Norovirus", "Rotavirus", "Adenovirus"],
    "The page associates post-transplant CMV with sore throat, diarrhoea and leucopenia.")
add(S1, 46, "recall", "The table places cytomegalovirus more prominently in which site?",
    "Large bowel rather than small bowel", ["Small bowel rather than large bowel", "Stomach rather than either bowel", "Equal involvement of small and large bowel"],
    "The printed comparison is cytomegalovirus (large bowel > small bowel).")
add(S1, 46, "truefalse", "TRUE or FALSE — the site table places fecal leukocytes with the large-bowel pattern, not the large-volume watery small-bowel pattern.",
    "True — fecal leukocytes are in the large-bowel column", ["False — fecal leukocytes are listed only for small bowel", "True — but the small-bowel stool is also described as bloody", "False — the table does not mention fecal leukocytes"],
    "Fecal leukocytes are listed in the large-bowel column; small-bowel stool is large-volume and watery without blood, pus or mucus.")

# ---------------------------------------------------------------------------
# Book p47 — organism table and Staphylococcus aureus
add(S2, 47, "recall", "The small-bowel bacterial mechanism described as in-vivo toxin production raises which second messenger before secretory diarrhoea?",
    "cAMP", ["cGMP", "cGMP and cAMP both fall", "Intracellular calcium only"],
    "The table links in-vivo toxin production to increased cAMP and secretory diarrhoea.")
add(S2, 47, "recall", "Which organism is labelled the most common small-bowel in-vivo secretory-toxin cause?",
    "Enterotoxigenic Escherichia coli (ETEC)", ["Enteroinvasive E. coli (EIEC)", "Non-typhoid Salmonella", "Shigella flexneri"],
    "ETEC is marked most common under small-bowel in-vivo toxin production.")
add(S2, 47, "recall", "Which second organism is listed alongside ETEC under small-bowel in-vivo toxin production?",
    "Vibrio cholerae", ["Vibrio parahaemolyticus", "Campylobacter jejuni", "Salmonella typhi"],
    "The listed small-bowel in-vivo toxin producers are ETEC and Vibrio cholerae.")
add(S2, 47, "recall", "Which set is grouped as preformed-toxin food poisoning in the small-bowel bacteria column?",
    "Staphylococcus aureus, Bacillus cereus and Clostridium perfringens", ["ETEC, Vibrio cholerae and EIEC", "Shigella flexneri, Campylobacter and non-typhoid Salmonella", "Giardia, Cryptosporidium and Entamoeba"],
    "The preformed-toxin group contains Staphylococcus aureus, Bacillus cereus and Clostridium perfringens.")
add(S2, 47, "recall", "Which organism is listed as an invasive large-bowel bacterium and is linked to shigellosis?",
    "Shigella flexneri", ["ETEC", "Vibrio cholerae", "Bacillus cereus"],
    "Shigella flexneri is listed among invasive organisms in the large-bowel column and causes shigellosis.")
add(S2, 47, "recall", "Which complete group lists the invasive bacteria named in the large-bowel column?",
    "Shigella flexneri, V. parahaemolyticus, Campylobacter, non-typhoid Salmonella and EIEC", ["ETEC, V. cholerae and Staphylococcus aureus", "Shigella, Giardia, Cryptosporidium and ETEC", "Rotavirus, norovirus and cytomegalovirus"],
    "The complete large-bowel invasive list includes Shigella, V. parahaemolyticus, Campylobacter, non-typhoid Salmonella and EIEC.")
add(S2, 47, "recall", "Which Vibrio species appears in the large-bowel invasive-organism list rather than the small-bowel secretory list?",
    "Vibrio parahaemolyticus", ["Vibrio cholerae", "Vibrio vulnificus", "Vibrio alginolyticus"],
    "V. parahaemolyticus is listed among large-bowel invasive organisms; V. cholerae is in the small-bowel secretory group.")
add(S2, 47, "recall", "Which protozoal distribution matches the table?",
    "Small bowel: Cryptosporidium, microsporidium, Giardia; large bowel: Entamoeba histolytica", ["Small bowel: Entamoeba; large bowel: Giardia and Cryptosporidium", "Small bowel: Giardia only; large bowel: all other protozoa", "Small bowel: Entamoeba and microsporidium; large bowel: Cryptosporidium"],
    "The table lists Cryptosporidium, microsporidium and Giardia in small bowel; Entamoeba histolytica in large bowel.")
add(S2, 47, "recall", "The note distinguishes Salmonella typhi from diarrhoeal small-bowel pathogens because small-bowel invasion is associated with:",
    "Fever with chills and abdominal pain, without diarrhoea", ["Large-volume watery diarrhoea without fever", "Small-volume bloody diarrhoea with tenesmus", "Steatorrhoea with no systemic symptoms"],
    "The note describes typhoid small-bowel invasion as fever with chills and abdominal pain, with no diarrhoea.")
add(S3, 47, "recall", "Staphylococcus aureus food poisoning is caused by a:",
    "Preformed, heat-stable enterotoxin", ["Heat-labile toxin formed after ingestion", "Shiga-like cytotoxin produced in the colon", "Neuraminidase toxin formed in blood"],
    "The page labels the Staphylococcus aureus toxin preformed and heat stable.")
add(S3, 47, "numeric", "The incubation period written for Staphylococcus aureus food poisoning is:",
    "1–6 hours", ["6–12 hours", "6–72 hours", "2–4 days"],
    "The printed incubation period is 1–6 hours.")
add(S3, 47, "recall", "Which source is specifically included in the Staphylococcus aureus food-poisoning list?",
    "Custard", ["Undercooked fried rice", "Raw fish", "Unpasteurized milk only"],
    "The listed sources are custard, pork and canned meat.")
add(S3, 47, "scenario", "After a shared meal, the earliest and most prominent symptom is vomiting. The page attributes this prominent symptom in S. aureus food poisoning to stimulation of:",
    "5-HT3 receptors", ["CCK-B receptors", "Muscarinic M3 receptors", "Dopamine D2 receptors"],
    "Vomiting is the most prominent clinical feature and is attributed to 5-HT3 stimulation.")
add(S3, 47, "recall", "Besides prominent vomiting, the other clinical feature listed for S. aureus food poisoning is:",
    "Abdominal cramps", ["Tenesmus", "Jaundice", "Painless rectal bleeding"],
    "The listed clinical features are vomiting and abdominal cramps.")
add(S3, 47, "recall", "Which set reproduces the organisms listed as heat-stable-enterotoxin producers in the note?",
    "S. aureus, B. cereus, C. perfringens, Yersinia and E. coli", ["V. cholerae, Shigella, Campylobacter, Giardia and CMV", "EIEC, EHEC, S. typhi, Rotavirus and Entamoeba", "S. aureus, V. cholerae, EIEC, norovirus and CMV"],
    "The note lists S. aureus, B. cereus, C. perfringens, Yersinia and E. coli as producers of heat-stable enterotoxin.")

# ---------------------------------------------------------------------------
# Book p48 — Bacillus cereus, Vibrio and ETEC
add(S3, 48, "recall", "In the B. cereus table, which pairing is correct for the heat-stable toxin?",
    "Preformed toxin; 1–6 h incubation; vomiting; undercooked fried rice", ["Formed toxin; 6–12 h; diarrhoea; meat and pudding", "Preformed toxin; 6–12 h; diarrhoea; raw fish", "Formed toxin; 1–6 h; vomiting; canned meat"],
    "The heat-stable B. cereus toxin is preformed; incubation is 1–6 hours, vomiting predominates, and undercooked fried rice is the source.")
add(S3, 48, "recall", "Which B. cereus table entry belongs to the heat-labile toxin?",
    "Formed toxin with 6–12 h incubation and diarrhoea associated with increased cAMP", ["Preformed toxin with 1–6 h incubation and vomiting", "Shiga toxin with 6–72 h incubation and haemolysis", "Cytotoxic toxin with a 2-day incubation and pseudomembranes"],
    "The heat-labile B. cereus toxin is formed; the table gives 6–12 hours and diarrhoea with increased cAMP.")
add(S3, 48, "recall", "Which foods are listed as sources for the heat-labile B. cereus presentation?",
    "Meat, pudding and dried potato", ["Undercooked fried rice only", "Custard, pork and canned meat", "Raw fish and shellfish"],
    "The heat-labile B. cereus column lists meat, pudding and dried potato.")
add(S3, 48, "numeric", "The incubation period paired with formed, heat-labile B. cereus toxin is:",
    "6–12 hours", ["1–6 hours", "12–24 hours", "2–4 days"],
    "The table gives 6–12 hours for heat-labile B. cereus toxin.")
add(S3, 48, "scenario", "A diner eats undercooked fried rice and develops vomiting within a few hours. Which B. cereus toxin pattern fits the page?",
    "Preformed heat-stable toxin", ["Formed heat-labile toxin with diarrhoea", "In-vivo cholera toxin", "Shiga-like toxin"],
    "Undercooked fried rice, vomiting and 1–6-hour incubation identify the preformed heat-stable B. cereus pattern.")
add(S4, 48, "recall", "Vibrio cholerae is described as:",
    "Non-invasive", ["An organism that invades all four bowel-wall layers", "A protozoan restricted to the colon", "A toxin-producing virus"],
    "The pathogenesis section labels V. cholerae non-invasive.")
add(S4, 48, "recall", "The cholera enterotoxin increases secretion by activating:",
    "Adenyl cyclase", ["Guanylyl cyclase", "Phospholipase C only", "Na+/H+ exchange"],
    "The book states that the cholera enterotoxin activates adenyl cyclase.")
add(S4, 48, "recall", "The toxin-coregulated pilus of V. cholerae mediates:",
    "Attachment to intestinal mucosa", ["Invasion of the submucosa", "Binding of iron to transferrin", "Destruction of ileal Peyer's patches"],
    "The toxin-coregulated pilus is described as mediating attachment to intestinal mucosa.")
add(S4, 48, "scenario", "A patient with cholera has profuse watery stool and marked volume depletion. Which stool-volume pattern is specifically listed?",
    "Large-volume watery diarrhoea", ["Small-volume bloody diarrhoea", "Formed stool with streaks of blood", "Small-volume mucoid stool with tenesmus"],
    "The listed cholera features are large-volume watery diarrhoea and dehydration.")
add(S4, 48, "recall", "The acid–base/electrolyte disturbance listed with cholera is:",
    "Hypokalaemic normal-anion-gap metabolic acidosis", ["Hyperkalaemic metabolic alkalosis", "Hypochloraemic high-anion-gap acidosis", "Hypernatraemic respiratory alkalosis"],
    "The book lists hypokalaemic acidosis with a normal anion gap.")
add(S4, 48, "management", "For fluid replacement in the cholera treatment list, which fluid is named as the fluid of choice?",
    "Ringer lactate", ["5% dextrose alone", "Half-normal saline alone", "Colloid without crystalloid"],
    "Ringer lactate is labelled the fluid of choice.")
add(S4, 48, "management", "Which antibiotic is named as the drug of choice for cholera in the book, with a pregnancy alternative also listed?",
    "Doxycycline; azithromycin in pregnancy", ["Ciprofloxacin; metronidazole in pregnancy", "Oral vancomycin; fidaxomicin in pregnancy", "Rifaximin; doxycycline in pregnancy"],
    "The printed drug of choice is doxycycline; azithromycin is listed in pregnancy. These are book-study notes, not current treatment guidance.")
add(S4, 48, "recall", "Raw fish is the source listed for:",
    "Vibrio parahaemolyticus", ["Vibrio cholerae", "Bacillus cereus", "Enterotoxigenic E. coli"],
    "The V. parahaemolyticus section lists raw fish as the source.")
add(S4, 48, "recall", "The named diagnostic phenomenon for V. parahaemolyticus is:",
    "Kanagawa phenomenon", ["CAMP phenomenon", "String sign", "Osmotic-gap phenomenon"],
    "Kanagawa phenomenon is the listed diagnostic clue.")
add(S4, 48, "truefalse", "TRUE or FALSE — the V. parahaemolyticus section says acute diarrhoea may occur and antibiotics have no role.",
    "True — acute diarrhoea is listed and antibiotics have no role", ["False — it causes chronic steatorrhoea and antibiotics are mandatory", "False — raw fish is not a listed source", "True — but only when Kanagawa testing is negative"],
    "The page lists acute diarrhoea, Kanagawa phenomenon for diagnosis, and no role for antibiotics.")
add(S4, 48, "recall", "ETEC is identified as the most common cause of:",
    "Community-acquired and travellers' diarrhoea", ["Pseudomembranous enterocolitis", "Typhoid fever without diarrhoea", "Post-transplant CMV colitis"],
    "ETEC is called the most common cause of community-acquired diarrhoea and travellers' diarrhoea.")
add(S4, 48, "recall", "The ETEC toxin begun at the bottom of p48 is the heat-labile toxin, which raises:",
    "cAMP", ["cGMP", "Serum gastrin", "Intracellular iron"],
    "The ETEC heat-labile toxin is linked to increased cAMP.")

# ---------------------------------------------------------------------------
# Book p49 — HUS and Shigella; non-typhoid Salmonella begins
add(S5, 49, "recall", "The clinical feature used to introduce childhood HUS is the combination of:",
    "Haemolytic anaemia and thrombocytopenia", ["Neutropenia and macrocytosis", "Thrombocytosis and iron deficiency", "Leukopenia and eosinophilia"],
    "The margin defines the HUS feature as haemolytic anaemia with thrombocytopenia.")
add(S5, 49, "numeric", "Approximately what fraction of childhood HUS is assigned to the first branch on p49?",
    "90%", ["10%", "50%", "70%"],
    "The diagram divides childhood HUS into 90% and 10% branches.")
add(S5, 49, "recall", "The organism marked most common in the 90% childhood-HUS branch is:",
    "Enterohaemorrhagic E. coli O157:H7", ["Streptococcus pneumoniae", "Salmonella typhi", "Vibrio cholerae"],
    "EHEC O157:H7 is marked most common in the 90% branch.")
add(S5, 49, "recall", "The toxin paired with EHEC O157:H7 is:",
    "Shiga-like toxin (verocytotoxin)", ["Neuraminidase toxin", "Toxin A enterotoxin", "Heat-labile toxin"],
    "EHEC O157:H7 is paired with Shiga-like toxin, also called verocytotoxin.")
add(S5, 49, "recall", "Which organism-toxin pair is also included in the 90% childhood-HUS branch?",
    "Shigella dysenteriae — Shiga toxin", ["S. pneumoniae — neuraminidase", "ETEC — toxin B", "C. difficile — verocytotoxin"],
    "The 90% branch also lists Shigella dysenteriae producing Shiga toxin.")
add(S5, 49, "numeric", "The p49 diagram assigns what proportion of childhood HUS to Streptococcus pneumoniae?",
    "10%", ["90%", "50%", "25%"],
    "The S. pneumoniae branch is labelled 10%.")
add(S5, 49, "recall", "The toxin named beside S. pneumoniae in the childhood-HUS diagram is:",
    "Neuraminidase toxin", ["Shiga-like toxin", "Toxin A", "Heat-stable ETEC toxin"],
    "The 10% S. pneumoniae branch is paired with neuraminidase toxin.")
add(S5, 49, "recall", "The note distinguishes the heat-stable ETEC toxin from LT by linking it to increased:",
    "cGMP", ["cAMP", "cGMP and cAMP both decrease", "Serum creatinine"],
    "The note states that heat-stable ETEC toxin increases cGMP; the heat-labile toxin on p48 increases cAMP.")
add(S5, 49, "recall", "In the Shigella pathogenesis diagram, the invasive branch begins with:",
    "Invasion by plasmid antigen", ["Urease-mediated neutralization", "Attachment by toxin-coregulated pilus", "Transferrin-receptor binding"],
    "The diagram identifies invasion by plasmid antigen as one pathogenesis arm.")
add(S5, 49, "numeric", "The invasive Shigella process is noted to affect how many layers of the intestinal wall?",
    "All four", ["One superficial layer", "Two layers", "Three layers"],
    "The note says plasmid-antigen invasion affects all four layers of the intestinal wall.")
add(S5, 49, "recall", "The invasive Shigella pathway is linked to severe inflammatory diarrhoea and:",
    "Reactive arthritis", ["Guillain–Barré syndrome", "Aortoarteritis", "Pseudomembranous colitis"],
    "The listed outcomes are shigellosis (severe inflammatory diarrhoea) and reactive arthritis.")
add(S5, 49, "recall", "The toxin-mediated Shigella branches are paired as:",
    "Enterotoxin → diarrhoea; Shiga-like toxin → cytotoxicity", ["Enterotoxin → cytotoxicity; Shiga-like toxin → diarrhoea", "Both toxins → secretory cAMP diarrhoea only", "Both toxins → urease production"],
    "The diagram links enterotoxin with diarrhoea and Shiga-like toxin with cytotoxicity.")
add(S5, 49, "management", "Which drug is labelled the drug of choice for Shigella on p49?",
    "Ciprofloxacin", ["Azithromycin", "Oral fidaxomicin", "Doxycycline"],
    "Ciprofloxacin is labelled DOC; azithromycin is also listed as treatment. This reflects the book's study content, not current prescribing guidance.")
add(S5, 49, "management", "Which additional antibiotic is listed after ciprofloxacin in the Shigella treatment section?",
    "Azithromycin", ["Vancomycin", "Rifaximin", "Tetracycline"],
    "Azithromycin is listed alongside ciprofloxacin for Shigella in the source.")
add(S5, 49, "scenario", "A patient with diarrhoea and arthritis is being distinguished from IBD. The note says IBD can be identified by fecal:",
    "Lactoferrin or calprotectin", ["Elastase or chymotrypsin", "α-1 antitrypsin only", "Bile acids or D-xylose"],
    "The note lists fecal lactoferrin/calprotectin as IBD identifiers in the differential.")
add(S5, 49, "recall", "Which extraintestinal feature is specifically included in that IBD differential note?",
    "Erythema nodosum", ["Rose spots of enteric fever", "Koilonychia", "Pica"],
    "The note's extraintestinal list includes erythema nodosum, episcleritis and type-I peripheral arthritis.")
add(S5, 49, "recall", "The non-typhoid Salmonella source is described as:",
    "Faeco-oral", ["Respiratory droplets", "Raw fish only", "Vector-borne"],
    "Non-typhoid Salmonella is listed as faeco-oral.")
add(S5, 49, "numeric", "The incubation interval listed for non-typhoid Salmonella is:",
    "6–72 hours", ["1–6 hours", "6–12 hours", "2–4 days"],
    "The p49 incubation period is 6–72 hours.")
add(S5, 49, "recall", "The pathogenesis phrase used for non-typhoid Salmonella is:",
    "Invasive enterotoxin", ["Preformed heat-stable toxin", "Non-invasive adenyl-cyclase toxin", "Shiga-like toxin alone"],
    "The page describes non-typhoid Salmonella pathogenesis as invasive enterotoxin.")
add(S5, 49, "recall", "The complication singled out as the most severe in non-typhoid Salmonella is:",
    "Aortoarteritis", ["Endovascular infection", "Toxic megacolon", "Reactive arthritis"],
    "Aortoarteritis is marked as the most severe complication; endovascular infection is also listed.")
add(S5, 49, "recall", "Besides aortoarteritis, which complication is listed for non-typhoid Salmonella?",
    "Endovascular infection", ["Intestinal lymphangiectasia", "Gallbladder perforation", "Celiac crisis"],
    "Endovascular infection is the second listed complication.")

# ---------------------------------------------------------------------------
# Book p50 — typhoid, Campylobacter, management and C. difficile begins
add(S6, 50, "recall", "In the Salmonella typhi note, diarrhoea in enteric fever is placed in which week?",
    "The second week", ["The first 24 hours", "The third week only", "It is stated to occur before fever"],
    "The note says enteric fever has diarrhoea in the second week.")
add(S6, 50, "recall", "The common complication named for typhoid in the p50 note is:",
    "Intestinal perforation", ["Pancreatic pseudocyst", "Toxic megacolon", "Oesophageal web"],
    "Intestinal perforation is called a common complication of typhoid.")
add(S6, 50, "recall", "Which haematologic complication is included in the Salmonella typhi note?",
    "Bone-marrow suppression", ["Polycythaemia", "Eosinophilia", "Thrombocytosis"],
    "Bone-marrow suppression is listed among typhoid clinical features.")
add(S6, 50, "recall", "Which gastrointestinal complication is listed alongside typhoid perforation?",
    "Intestinal haemorrhage", ["Achalasia", "Pseudomembrane formation", "Protein-losing gastropathy"],
    "Intestinal haemorrhage is listed with perforation and bone-marrow suppression.")
add(S6, 50, "recall", "The photograph on p50 is captioned:",
    "Ileal perforation", ["Toxic megacolon", "Rose spots of enteric fever", "Pseudomembranous colitis"],
    "The photograph caption reads 'Ileal perforation'.")
add(S6, 50, "recall", "Campylobacter jejuni is acquired by the route listed as:",
    "Faeco-oral", ["Vector-borne", "Airborne droplets", "Transplacental"],
    "The C. jejuni source is faeco-oral.")
add(S6, 50, "numeric", "The incubation period listed for C. jejuni is:",
    "2–4 days", ["1–6 hours", "6–72 hours", "7–14 days"],
    "The page gives a 2–4-day incubation period for C. jejuni.")
add(S6, 50, "recall", "C. jejuni is listed as a risk factor for which later disease category?",
    "Inflammatory bowel disease", ["Celiac disease", "Autoimmune gastritis", "Pseudomembranous colitis"],
    "The complication list names inflammatory bowel disease as a risk association.")
add(S6, 50, "recall", "The neurological syndrome C. jejuni is said to trigger is:",
    "Guillain–Barré syndrome", ["Miller Fisher syndrome only", "Myasthenia gravis", "Toxic neuropathy"],
    "The source abbreviates Guillain–Barré syndrome as GBS and lists it as a trigger.")
add(S6, 50, "recall", "The immune-proliferative small-intestinal disease association is abbreviated:",
    "IPSID", ["IBS-D", "IPF", "HUS"],
    "The page lists immune proliferative small intestinal disease (IPSID)/lymphoma.")
add(S6, 50, "scenario", "An older adult with C. jejuni has fever, abdominal pain, hypovolaemia and at least six stools daily. These features are among the page's:",
    "Indications for management", ["Criteria ruling out culture", "Features of non-severe C. difficile only", "Diagnostic criteria for HUS"],
    "Age >70 years, fever, abdominal pain, hypovolaemia and ≥6 stools/day are listed under management indications.")
add(S6, 50, "numeric", "Which age threshold appears among the C. jejuni management indications?",
    ">70 years", [">50 years", "<20 years", ">40 years"],
    "The first indication listed is age >70 years.")
add(S6, 50, "numeric", "The stool-frequency threshold listed among the management indications is:",
    "≥6 stools per day", ["≥2 stools per day", "≥4 stools per day", "≥10 stools per day"],
    "The source gives ≥6 stools/day.")
add(S6, 50, "recall", "The culture organisms named in the management section are:",
    "Shigella, Salmonella and Campylobacter", ["ETEC, rotavirus and CMV", "Giardia, Entamoeba and microsporidium", "C. difficile, S. pneumoniae and norovirus"],
    "The listed culture targets are Shigella, Salmonella and Campylobacter.")
add(S6, 50, "truefalse", "TRUE or FALSE — the page groups stool culture and azithromycin treatment as not routinely indicated in small-bowel diarrhoea.",
    "True — the brace marks both as not routinely indicated in small-bowel diarrhoea", ["False — the brace applies only to culture", "False — the brace applies only to azithromycin", "True — but only for large-bowel diarrhoea"],
    "The bracket beside culture and azithromycin says they are not routinely indicated in small-bowel diarrhoea.")
add(S6, 50, "management", "The azithromycin dose shown in the C. jejuni management note is:",
    "500 mg", ["200 mg twice daily", "1 g once weekly", "100 mg"],
    "The page lists azithromycin 500 mg; it is book-study content rather than a prescribing recommendation.")
add(S7, 50, "recall", "The p50 section heading for the next disorder is:",
    "Pseudomembranous enterocolitis", ["Collagenous colitis", "Microscopic colitis", "Tropical sprue"],
    "The next heading is pseudomembranous enterocolitis.")
add(S7, 50, "recall", "The organism named under pseudomembranous-enterocolitis pathogenesis is:",
    "Clostridioides difficile", ["Clostridium perfringens", "Shigella dysenteriae", "Campylobacter jejuni"],
    "The pathogenesis section names C. difficile.")
add(S7, 50, "recall", "The page links antibiotic exposure in C. difficile pathogenesis to a change in:",
    "Gut flora", ["Gastric acid secretion", "Bile-acid synthesis", "Red-cell production"],
    "The readable pathogenesis line links antibiotics with a change in gut flora.")
add(S7, 50, "recall", "Which toxin description is correct for C. difficile on p50?",
    "Toxin A is an enterotoxin; toxin B is cytotoxic and the most potent", ["Toxin A is cytotoxic and most potent; toxin B is an enterotoxin", "Both toxins are heat-stable preformed enterotoxins", "Toxin A causes HUS; toxin B causes cholera"],
    "The source calls toxin A an enterotoxin and toxin B cytotoxic (most potent).")
add(S7, 50, "numeric", "The incubation period printed for pseudomembranous enterocolitis is:",
    "2 days", ["6 hours", "2 weeks", "6–7 days"],
    "The page gives an incubation period of 2 days.")

# ---------------------------------------------------------------------------
# Book p51 — C. difficile features, diagnosis algorithm and severity treatment
add(S7, 51, "recall", "The clinical-features list for pseudomembranous enterocolitis begins with:",
    "Fever and abdominal cramps", ["Jaundice and right-upper-quadrant pain", "Painless bleeding and constipation", "Dysphagia and early satiety"],
    "Fever and abdominal cramps are listed at the start of the clinical-features section.")
add(S7, 51, "recall", "The diarrhoea pattern described for C. difficile may be watery with:",
    "Mucus, with or without blood", ["Fat globules and no mucus", "Only formed stool streaked with blood", "Pus but never mucus or blood"],
    "The page describes watery diarrhoea with mucus ± blood.")
add(S7, 51, "recall", "The stool pattern in the C. difficile clinical-features section is categorized as:",
    "Large-bowel pattern", ["Small-bowel high-volume pattern", "Gastric outlet pattern", "Pancreatic maldigestion pattern"],
    "The source explicitly labels this a large-bowel pattern.")
add(S7, 51, "recall", "The major complication illustrated and named for C. difficile enterocolitis is:",
    "Toxic megacolon", ["Ileal perforation", "Intestinal lymphangiectasia", "Pneumatosis of the stomach"],
    "Toxic megacolon is the listed complication and the image caption.")
add(S7, 51, "recall", "The relative order of toxic-megacolon associations printed in parentheses is:",
    "Pseudomembranous enterocolitis > ulcerative colitis > invasive-organism infection", ["Ulcerative colitis > pseudomembranous enterocolitis > invasive-organism infection", "Invasive-organism infection > ulcerative colitis > pseudomembranous enterocolitis", "Pseudomembranous enterocolitis > invasive infection > ulcerative colitis"],
    "The printed order is pseudomembranous enterocolitis, then ulcerative colitis, then infection by invasive organisms.")
add(S7, 51, "recall", "The initial C. difficile diagnostic combination shown on p51 is:",
    "Glutamate dehydrogenase (GDH) test plus EIA against toxin A/B", ["Stool culture plus occult blood", "PCR alone followed by toxin culture", "Fecal calprotectin plus lactoferrin"],
    "The diagnostic algorithm begins with GDH and EIA against toxins A/B.")
add(S7, 51, "recall", "When both the GDH test and toxin EIA are positive, the diagram concludes:",
    "Confirmed diagnosis", ["C. difficile ruled out", "Repeat testing after one month", "Proceed directly to stool culture"],
    "Both-positive results lead directly to confirmed diagnosis.")
add(S7, 51, "scenario", "GDH and toxin EIA are discordant, so at least one is positive. What is the next test in the printed algorithm?",
    "PCR (nucleic-acid amplification test)", ["D-xylose urine test", "Rapid urease test", "Schilling test"],
    "When any one initial test is positive, the diagram sends the case to PCR/NAAT; a positive PCR confirms diagnosis.")
add(S7, 51, "recall", "If both initial GDH and toxin EIA tests are negative, the algorithm says:",
    "C. difficile infection is ruled out", ["PCR is mandatory in every case", "The diagnosis is confirmed", "Repeat EIA after treatment"],
    "Both-negative results rule out C. difficile infection in the printed flowchart.")
add(S7, 51, "numeric", "The non-severe branch requires a white-cell count below:",
    "15,000", ["5,000", "10,000", "20,000"],
    "The non-severe criteria show WBC <15,000.")
add(S7, 51, "numeric", "The creatinine criterion for the non-severe branch is:",
    "Serum creatinine <1.5", ["Serum creatinine <0.5", "Serum creatinine >1.5", "Serum creatinine >3.0"],
    "The flowchart pairs non-severe disease with serum creatinine <1.5.")
add(S7, 51, "management", "The non-severe first-line option labelled DOC is:",
    "Oral fidaxomicin", ["Intravenous metronidazole alone", "Oral azithromycin", "Ciprofloxacin"],
    "Oral fidaxomicin is marked DOC in the non-severe branch; oral vancomycin is also listed. These are source-book notes, not current treatment guidance.")
add(S7, 51, "recall", "The page notes that oral fidaxomicin has which advantage in the non-severe branch?",
    "Reduced recurrence", ["Prevents all toxic megacolon", "Removes the need for fluid replacement", "Provides a diagnostic PCR result"],
    "A downward arrow and 'recurrence' are noted beside oral fidaxomicin.")
add(S7, 51, "management", "Which additional oral antibiotic is listed for non-severe C. difficile disease?",
    "Vancomycin", ["Doxycycline", "Ciprofloxacin", "Amoxicillin"],
    "Oral vancomycin is listed beside fidaxomicin in the non-severe branch.")
add(S7, 51, "scenario", "A patient has WBC >15,000 and creatinine >1.5 but no ileus, shock or megacolon. Which category does the flowchart use?",
    "Severe", ["Non-severe", "Fulminant", "Not C. difficile"],
    "The severe branch is selected when the elevated WBC/creatinine criteria are present but ileus, shock and megacolon are absent.")
add(S7, 51, "management", "Which dose of oral fidaxomicin is specified in the severe branch?",
    "200 mg twice daily", ["200 mg once weekly", "500 mg once daily", "1 g three times daily"],
    "The severe branch specifies oral fidaxomicin 200 mg BD.")
add(S7, 51, "management", "Which other oral agent appears in the severe C. difficile branch?",
    "Vancomycin", ["Doxycycline", "Azithromycin", "Rifaximin"],
    "Oral vancomycin is listed as the other severe-branch option.")
add(S7, 51, "scenario", "Ileus, shock or megacolon moves a patient with C. difficile into which category?",
    "Fulminant", ["Non-severe", "Severe without complications", "Uncomplicated viral diarrhoea"],
    "The right-hand branch labels the presence of ileus, shock or megacolon as fulminant.")
add(S7, 51, "management", "Which combination is listed for fulminant C. difficile disease?",
    "Oral vancomycin, IV metronidazole and surgical consultation", ["Oral fidaxomicin alone and outpatient review", "Doxycycline, Ringer lactate and no surgical input", "Azithromycin with a repeat stool antigen test"],
    "The fulminant branch lists oral vancomycin, IV metronidazole and surgical consultation. This transcribes the book's management diagram and is not a current-care protocol.")
add(S7, 51, "truefalse", "TRUE or FALSE — in the p51 flowchart, fulminant disease adds IV metronidazole and surgical consultation to oral vancomycin.",
    "True — all three appear in the fulminant branch", ["False — IV metronidazole is listed for non-severe disease", "False — surgery is explicitly excluded", "True — but vancomycin is not included"],
    "The fulminant branch lists oral vancomycin, IV metronidazole and surgical consultation.")

GUIDES = {
    S1: ("Definitions & Site Patterns", "Acute diarrhoea ≤2 weeks is infectious unless proved otherwise.\nDuration branches: <1 week benign/viral or complicated/bacterial; >1 week protozoal.\nSeparate small-bowel large-volume watery stool from large-bowel small-volume bloody stool."),
    S2: ("Small- and Large-Bowel Organisms", "Small bowel: ETEC/V. cholerae toxins, preformed-toxin bacteria, Cryptosporidium, microsporidium, Giardia.\nLarge bowel: Shigella, Campylobacter, non-typhoid Salmonella, EIEC, V. parahaemolyticus, Entamoeba.\nTyphoid is a small-bowel invasion with fever/pain and no diarrhoea in the note."),
    S3: ("Preformed-Toxin Food Poisoning", "S. aureus: preformed heat-stable toxin, 1–6 h, custard/pork/canned meat, vomiting via 5-HT3.\nB. cereus heat-stable: fried rice/vomiting; heat-labile: formed toxin, 6–12 h, diarrhoea/cAMP.\nThe source also lists Yersinia and E. coli among heat-stable-toxin producers."),
    S4: ("Vibrio, ETEC & Secretory Diarrhoea", "V. cholerae is non-invasive; toxin activates adenyl cyclase; TCP attaches to mucosa.\nLarge-volume watery stool, dehydration and hypokalaemic normal-gap acidosis; the page names Ringer lactate.\nV. parahaemolyticus: raw fish/Kanagawa; ETEC LT raises cAMP and is linked to travellers' diarrhoea."),
    S5: ("HUS and Shigella", "Childhood HUS: 90% EHEC O157:H7/Shigella dysenteriae toxins; 10% pneumococcal neuraminidase.\nShigella invasion affects all four bowel-wall layers; enterotoxin causes diarrhoea and Shiga-like toxin is cytotoxic.\nThe note contrasts diarrhoea with arthritis against IBD markers and extraintestinal signs."),
    S6: ("Salmonella and Campylobacter", "Typhoid: diarrhoea in week two, perforation, marrow suppression and intestinal bleeding.\nC. jejuni is faeco-oral, incubates 2–4 days, and is linked to IBD, GBS and IPSID/lymphoma.\nThe page's culture and azithromycin notes are explicitly not routine for small-bowel diarrhoea."),
    S7: ("C. difficile Enterocolitis", "GDH + toxin A/B EIA → confirm if both positive; discordant results go to PCR/NAAT.\nThe p51 flowchart separates non-severe, severe and fulminant disease by WBC/creatinine and ileus/shock/megacolon.\nTreatment entries reproduce the book for study; they are not current clinical guidance."),
}


def main():
    questions = []
    for i, (sec, page, fmt, stem, opts, ans, exp) in enumerate(RAW, 1):
        questions.append({"id": f"MED-C{CHAPTER}-{i:02d}", "sec": sec,
                          "page": page, "fmt": fmt, "q": stem,
                          "opts": opts, "ans": ans, "exp": exp})
    ordered_sections = list(dict.fromkeys(row[0] for row in RAW))
    units = []
    for n, sec in enumerate(ordered_sections, 1):
        title, guide = GUIDES[sec]
        units.append({"id": f"MED-U{CHAPTER}-{n}", "ch": CHAPTER, "n": n,
                      "title": title, "sec": sec, "guide": guide,
                      "qs": [q["id"] for q in questions if q["sec"] == sec]})
    chapter = {"chapter": CHAPTER, "title": TITLE, "pageRange": PAGES,
               "questions": questions, "units": units}
    out = DATA / f"ch{CHAPTER:02d}.json"
    out.write_text(json.dumps(chapter, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out.name}: {len(questions)} questions / {len(units)} units")


if __name__ == "__main__":
    main()
