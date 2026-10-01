#!/usr/bin/env python3
"""Generate Chapter 8 Stomach (Book p52–59), in scanned book order."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
CHAPTER = 8
TITLE = "Stomach"
PAGES = "52-59"

S1 = "Stomach Regions, Glands & Cells"
S2 = "Gastric Mucosal Defence and Wall"
S3 = "Acid Regulation and Acute Gastritis"
S4 = "Chronic and Hypertrophic Gastritis"
S5 = "Helicobacter pylori: Biology and Virulence"
S6 = "H. pylori Gastritis, Dyspepsia and Testing"
S7 = "H. pylori Treatment and Test of Cure"
RAW = []


def add(sec, page, fmt, stem, correct, distractors, explanation):
    options = [correct, *distractors]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError(f"{sec}: each item needs four distinct options: {stem}")
    random.Random(8000 + CHAPTER * 10000 + len(RAW)).shuffle(options)
    if fmt == "truefalse":
        assert sum(o.startswith("True") for o in options) == 2
        assert sum(o.startswith("False") for o in options) == 2
    RAW.append((sec, page, fmt, stem, options, options.index(correct),
                f"{explanation.rstrip()} (Book p{page})"))


# ---------------------------------------------------------------------------
# Book p52 — regions, glands, cells and labelled anatomy
add(S1, 52, "recall", "Which three regions appear as the columns of the stomach table?",
    "Fundus, body/corpus and antrum", ["Cardia, pylorus and duodenal bulb", "Fundus, incisura and duodenum", "Oesophagus, corpus and jejunum"],
    "The table divides the stomach into fundus, body/corpus and antrum.")
add(S1, 52, "recall", "A lesion lies above the gastro-oesophageal sphincter (GES). Which stomach region is associated with that location?",
    "Fundus", ["Body/corpus", "Antrum", "Incisura"],
    "The fundus is located above the GES.")
add(S1, 52, "recall", "The body/corpus is located:",
    "Between the GES and incisura", ["Above the GES", "Below the incisura", "Within duodenal segments 1–4"],
    "The body/corpus lies between the GES and incisura.")
add(S1, 52, "recall", "Which region is located below the incisura?",
    "Antrum", ["Fundus", "Body/corpus", "Oesophagus"],
    "The antrum is below the incisura.")
add(S1, 52, "recall", "Which gland names are paired with the stomach regions in the p52 table?",
    "Fundus—fundic; body—oxyntic; antrum—pyloric", ["Fundus—pyloric; body—fundic; antrum—oxyntic", "Fundus—oxyntic; body—pyloric; antrum—fundic", "Fundus—Brunner; body—fundic; antrum—Lieberkühn"],
    "The table assigns fundic glands to fundus, oxyntic glands to body, and pyloric glands to antrum.")
add(S1, 52, "recall", "Which cell group is listed in the fundus?",
    "ECL, mucous and endocrine cells", ["G cells, chief cells and Paneth cells", "Parietal cells, chief cells and G cells", "Goblet cells, Paneth cells and enterocytes"],
    "Fundic glands contain enterochromaffin-like (ECL), mucous and endocrine cells.")
add(S1, 52, "recall", "The fundic ECL cell secretion shown in the table is:",
    "Histamine", ["Gastrin", "Pepsinogen", "Intrinsic factor"],
    "The table shows ECL cells in the fundus secreting histamine.")
add(S1, 52, "recall", "Which two secretory products are assigned to body parietal cells?",
    "Acid and intrinsic factor", ["Gastrin and mucus", "Pepsinogen and histamine", "Bicarbonate and secretin"],
    "Parietal cells in the body secrete acid and intrinsic factor.")
add(S1, 52, "recall", "In the body oxyntic gland, chief cells are concentrated at the base and secrete:",
    "Pepsinogen", ["Gastrin", "Histamine", "Intrinsic factor"],
    "Chief cells are shown at the base and secrete pepsinogen.")
add(S1, 52, "recall", "The parietal cells are labelled at which part of the oxyntic gland?",
    "Neck/isthmus", ["Base only", "Villus tip", "Pyloric lumen"],
    "The p52 table places parietal cells at the neck/isthmus.")
add(S1, 52, "recall", "Which cell type and secretion are paired in the antrum?",
    "G cell—gastrin", ["Chief cell—pepsinogen", "ECL cell—intrinsic factor", "Parietal cell—gastrin"],
    "Antral G cells secrete gastrin; mucous cells and ECL cells are also listed in the antrum.")
add(S1, 52, "recall", "Which set of cells is listed for pyloric glands in addition to antral G cells?",
    "Mucous cells and ECL cells", ["Chief cells and Paneth cells", "Parietal cells and goblet cells", "Enterocytes and endocrine cells only"],
    "The antrum/pyloric-gland column lists G cells, mucous cells and ECL cells.")
add(S1, 52, "recall", "The folds shown inside the body of the stomach are labelled:",
    "Rugae", ["Haustra", "Plicae circulares", "Kerckring valves"],
    "The stomach diagram labels the internal folds as rugae.")
add(S1, 52, "recall", "Which two named borders of the stomach are shown in the anatomy diagram?",
    "Lesser and greater curvatures", ["Mesenteric and antimesenteric borders", "Anterior and posterior taeniae", "Right and left colic flexures"],
    "The labelled stomach diagram identifies the lesser and greater curvatures.")
add(S1, 52, "recall", "The diagram places the incisura between which stomach regions?",
    "Body/corpus and antrum", ["Fundus and oesophagus", "Antrum and duodenum", "Cardia and fundus"],
    "The incisura marks the transition from body/corpus toward the antrum.")
add(S1, 52, "recall", "Which structures are shown at the outlet of the stomach in the diagram?",
    "Pylorus and duodenum", ["Ileocecal valve and caecum", "Major papilla and jejunum", "Fundus and oesophagus"],
    "The diagram labels the pylorus and the adjoining duodenum (segments 1–4).")
add(S1, 52, "recall", "The two papillae labelled beside the duodenum are the:",
    "Major and minor papillae", ["Lesser and greater curvatures", "Major and minor rugae", "Pyloric and ileocecal valves"],
    "The diagram labels the major and minor papillae in the duodenum.")
add(S1, 52, "recall", "Which additional fold pattern is labelled in the duodenum on the stomach illustration?",
    "Circular folds", ["Haustral folds", "Semilunar folds", "Gastric rugae"],
    "The label at the duodenum reads circular folds.")
add(S1, 52, "scenario", "A cell in the neck/isthmus of an oxyntic gland produces both acid and intrinsic factor. Which cell is it?",
    "Parietal cell", ["Chief cell", "G cell", "ECL cell"],
    "Parietal cells in the neck/isthmus produce acid and intrinsic factor.")

# ---------------------------------------------------------------------------
# Book p53 — mucosal defence, wall layers and innervation
add(S2, 53, "recall", "Which sequence reproduces the three layers of gastroduodenal mucosal defence?",
    "Pre-epithelial → epithelial (restitution) → subepithelial", ["Subepithelial → muscular → serosal", "Epithelial → luminal → vascular", "Mucosal → muscular → neural"],
    "The page lists pre-epithelial, epithelial (restitution) and subepithelial layers.")
add(S2, 53, "recall", "Which item is included among the listed gastric damaging factors?",
    "Acid", ["Bicarbonate in mucus", "Mucosal blood flow", "Epithelial regeneration"],
    "Acid, NSAIDs, tobacco and H. pylori (not always) are listed as damaging factors.")
add(S2, 53, "recall", "How does the page qualify the role of H. pylori in the damaging-factor list?",
    "H. pylori is marked 'not always'", ["H. pylori is described as the only cause", "H. pylori is placed among protective factors", "H. pylori is restricted to the submucosa"],
    "The list includes H. pylori with the parenthetical qualifier 'not always'.")
add(S2, 53, "recall", "The protective-factor pathway shown in the epithelial layer begins with COX-1 producing:",
    "Prostaglandins", ["Leukotrienes", "Histamine", "Gastrin"],
    "COX-1 is shown leading to prostaglandins in the epithelial layer.")
add(S2, 53, "recall", "Which item belongs to the normal gastric protective-factor list in the injury diagram?",
    "Bicarbonate secretion into mucus", ["Ischaemia", "Shock", "NSAID exposure"],
    "Normal protective factors include surface mucus, bicarbonate into mucus, mucosal blood flow, barrier function, epithelial regeneration and prostaglandins.")
add(S2, 53, "recall", "Besides mucus and bicarbonate, which vascular factor is listed as gastric mucosal protection?",
    "Mucosal blood flow", ["Portal venous pressure", "Gastric venous stasis", "Mesenteric arterial shunting"],
    "Mucosal blood flow is one of the protective factors in the normal panel.")
add(S2, 53, "recall", "Which epithelial property appears in the p53 protective-factor panel?",
    "Epithelial barrier function", ["Crypt-cell migration into colon", "Loss of regenerative capacity", "Disruption of cell junctions"],
    "The protective list includes epithelial barrier function and regenerative capacity.")
add(S2, 53, "recall", "Which combination is shown in the injury panel rather than the normal protective panel?",
    "Ischaemia, shock and NSAIDs", ["Mucosal blood flow, mucus and bicarbonate", "Epithelial repair and prostaglandins", "Barrier function and surface mucus"],
    "The injury panel names ischaemia, shock and NSAID exposure.")
add(S2, 53, "recall", "In the ulcer diagram, the label N refers to:",
    "Necrotic debris", ["Normal mucosa", "Neutrophil count", "Nerve plexus"],
    "The diagram labels N as necrotic debris.")
add(S2, 53, "recall", "The ulcer diagram's label G identifies:",
    "Granulation tissue", ["Gastric glands", "Goblet-cell layer", "Ganglion cells"],
    "The diagram labels G as granulation tissue.")
add(S2, 53, "recall", "The ulcer diagram labels S as:",
    "Fibrosis", ["Surface mucus", "Serosa", "Smooth muscle"],
    "The p53 ulcer diagram identifies S as fibrosis.")
add(S2, 53, "recall", "Which sequence gives the mucosal components of the GIT wall in the order listed?",
    "Mucosal gel coating → epithelial layer → lamina propria → muscularis mucosa", ["Epithelium → serosa → submucosa → muscularis externa", "Lamina propria → outer longitudinal muscle → mucosal gel → serosa", "Mucosal gel → muscularis externa → ganglia → serosa"],
    "The mucosa list contains mucosal gel coating, epithelial layer, lamina propria and muscularis mucosa.")
add(S2, 53, "recall", "Which plexus is placed in the submucosa?",
    "Meissner's plexus", ["Auerbach's plexus", "Celiac plexus", "Hypogastric plexus"],
    "The submucosa is associated with Meissner's plexus.")
add(S2, 53, "recall", "Which arrangement of the muscularis layer is shown on p53?",
    "Outer longitudinal — Auerbach's plexus — inner circular", ["Inner longitudinal — Meissner's plexus — outer circular", "Outer circular — Meissner's plexus — inner longitudinal", "Circular muscle only, with no intervening plexus"],
    "The muscularis layer is shown as outer longitudinal, Auerbach's plexus and inner circular.")
add(S2, 53, "recall", "Which GIT wall layer is listed after the muscularis layer?",
    "Serosa", ["Muscularis mucosa", "Submucosa", "Lamina propria"],
    "Serosa is listed as the outer GIT wall layer after muscularis.")
add(S2, 53, "recall", "The pacemaker cells of the GIT are the:",
    "Interstitial cells of Cajal", ["Paneth cells", "Enterochromaffin cells", "Chief cells"],
    "The note identifies interstitial cells of Cajal as GIT pacemaker cells.")
add(S2, 53, "recall", "Interstitial cells of Cajal generate the:",
    "Basal electric rhythm (BER)", ["Migrating motor complex only", "Gastric acid output", "Ileal brake"],
    "Interstitial cells of Cajal produce basal electric rhythm (BER).")
add(S2, 53, "recall", "Within intrinsic enteric innervation, Auerbach's plexus is associated with:",
    "Motility", ["Intestinal secretion", "Intrinsic-factor release", "Bile-acid reabsorption"],
    "The diagram links Auerbach's plexus to motility.")
add(S2, 53, "recall", "Within intrinsic enteric innervation, Meissner's plexus is linked to:",
    "Intestinal secretion", ["Motility", "Gastrin synthesis", "Mucosal blood flow only"],
    "The diagram links Meissner's plexus to intestinal secretion.")
add(S2, 53, "truefalse", "TRUE or FALSE — in the p53 autonomic diagram, sympathetic input decreases motility while parasympathetic input increases it.",
    "True — sympathetic ↓ and parasympathetic ↑ motility", ["False — sympathetic increases and parasympathetic decreases motility", "True — both divisions increase motility", "False — both divisions suppress motility"],
    "The diagram shows sympathetic input decreasing motility and parasympathetic input increasing it.")

# ---------------------------------------------------------------------------
# Book p54 — cooperative acid secretion, BAO and gastritis
add(S3, 54, "recall", "Which first messenger/second-messenger pair is shown for ECL-cell histamine?",
    "Histamine → increased cAMP", ["Gastrin → increased cAMP", "Acetylcholine → increased cGMP", "Somatostatin → increased calcium"],
    "ECL cells release histamine, which raises cAMP in the cooperative acid-secretion diagram.")
add(S3, 54, "recall", "Gastrin released from G cells acts on which receptor shown on parietal cells?",
    "CCK-B receptor", ["M3 receptor", "H2 receptor", "Secretin receptor"],
    "The diagram shows G-cell gastrin acting at CCK-B receptors on parietal cells.")
add(S3, 54, "recall", "The acetylcholine arm of the acid-secretion diagram signals through:",
    "M3 receptor and Ca²⁺", ["CCK-B receptor and cAMP", "H2 receptor and cGMP", "D2 receptor and potassium"],
    "Acetylcholine → M3 receptor → Ca²⁺ is the third cooperative arm.")
add(S3, 54, "scenario", "Histamine, gastrin and acetylcholine converge on which final effect in the diagram?",
    "Increased acid production", ["Suppressed parietal-cell output", "Reduced mucosal blood flow", "Increased intrinsic-factor degradation"],
    "The three signals converge to increase acid production.")
add(S3, 54, "recall", "GRP, also called bombesin, is shown to increase:",
    "Gastrin", ["Somatostatin", "Pepsinogen", "Intrinsic factor"],
    "GRP/bombesin is shown leading to increased gastrin.")
add(S3, 54, "recall", "Which group contains only inhibitors of gastric acid production listed on p54?",
    "CCK, prostaglandin, somatostatin and GIP", ["Gastrin, histamine, acetylcholine and GRP", "Pepsinogen, intrinsic factor, mucus and bicarbonate", "Secretin, serotonin, dopamine and motilin"],
    "The listed inhibitors are CCK, prostaglandin, somatostatin and gastric inhibitory peptide.")
add(S3, 54, "recall", "The maximum acid output (MAO) time written in the BAO note is:",
    "6 pm", ["6 am", "Noon", "Midnight"],
    "The p54 note pairs maximal acid output with 6 pm.")
add(S3, 54, "recall", "The least acid output time given in the same note is:",
    "6 am", ["6 pm", "Noon", "Midnight"],
    "The note gives least acid output at 6 am.")
add(S3, 54, "numeric", "A BAO/MAO ratio above what value is associated with a gastrin-secreting tumour in the note?",
    ">0.6", [">0.06", ">1.6", "<0.06"],
    "The printed threshold is BAO/MAO >0.6.")
add(S3, 54, "recall", "Gastritis is defined on p54 as:",
    "Histological inflammation of the gastric mucosa", ["Acute inflammation limited to the serosa", "Endoscopic redness without mucosal inflammation", "Infection of the pylorus only"],
    "The definition is histological inflammation of gastric mucosa.")
add(S3, 54, "recall", "The cause ranking written for gastritis is:",
    "NSAIDs more common than infectious causes", ["Infectious causes more common than NSAIDs", "Alcohol more common than both", "Autoimmune causes are the only listed cause"],
    "The page states causes: NSAIDs > infectious.")
add(S3, 54, "truefalse", "TRUE or FALSE — the page says endoscopic appearance and histology in gastritis correlate closely.",
    "False — it explicitly says there is no correlation", ["True — the two always match", "False — gastritis has no histological diagnosis", "True — but only in acute gastritis"],
    "The diagnostic note says endoscopy and histology have no correlation.")
add(S3, 54, "recall", "Acute phlegmonous gastritis is characterized as:",
    "Rare, severely progressive inflammation of the gastric wall", ["Common superficial inflammation of the antrum", "Chronic atrophy limited to the corpus", "Benign hypertrophy of the duodenal mucosa"],
    "The page describes acute phlegmonous gastritis as rare and severely progressive, involving the gastric wall.")
add(S3, 54, "recall", "The microscopic image beside acute phlegmonous gastritis is captioned as gastric mucosal infiltration by:",
    "Neutrophils", ["Eosinophils", "Plasma cells", "Lymphocytes only"],
    "The image caption identifies neutrophil infiltration.")
add(S3, 54, "recall", "Which gross change is listed with acute phlegmonous gastritis?",
    "Thickening of the wall and gas formation", ["Large tortuous folds sparing the antrum", "Pyloric stenosis with a string sign", "Mucosal atrophy with intestinal metaplasia"],
    "The text lists wall thickening and gas formation.")
add(S3, 54, "scenario", "Acute phlegmonous gastritis is specifically noted in which host group?",
    "Immunocompromised people", ["Healthy young athletes", "Patients with isolated ileal Crohn's disease", "Children with congenital lactase deficiency only"],
    "The page says it is seen in immunocompromised people.")
add(S3, 54, "recall", "The causative-organism ranking for acute phlegmonous gastritis is:",
    "Streptococci > E. coli", ["E. coli > Streptococci", "H. pylori > E. coli", "Salmonella > Shigella"],
    "The printed ranking is Streptococci > E. coli.")
add(S3, 54, "recall", "Which set contains the clinical features listed for acute phlegmonous gastritis?",
    "Abdominal pain, vomiting and fever", ["Painless bleeding, tenesmus and weight loss", "Dysphagia, early satiety and jaundice", "Constipation, steatorrhoea and neuropathy"],
    "The page lists abdominal pain, vomiting and fever.")
add(S3, 54, "recall", "The complication and outcome emphasized for acute phlegmonous gastritis are:",
    "Stomach-wall necrosis and high mortality", ["Gastric adenocarcinoma and low mortality", "Duodenal web and spontaneous resolution", "Oesophageal rupture and chronic recurrence"],
    "Stomach-wall necrosis and a high mortality rate are listed complications/outcomes.")

# ---------------------------------------------------------------------------
# Book p55–56 — chronic and hypertrophic gastritis
add(S4, 55, "recall", "Chronic gastritis is described as superficial involvement by:",
    "Lymphocytes and plasma cells", ["Neutrophils and eosinophils only", "Mast cells and platelets", "Macrophages without lymphocytes"],
    "The page states superficial involvement by lymphocytes and plasma cells.")
add(S4, 55, "recall", "Which chronic-gastritis type is identified as less common?",
    "Type A", ["Type B", "Type C", "Type D"],
    "Type A is marked less common; Type B is more common.")
add(S4, 55, "recall", "Type A chronic gastritis is also called:",
    "Autoimmune metaplastic atrophic gastritis (AMAG)", ["Environmental metaplastic atrophic gastritis (EMAG)", "Non-atrophic pangastritis", "Hypertrophic protein-losing gastropathy"],
    "Type A is named autoimmune metaplastic atrophic gastritis (AMAG).")
add(S4, 55, "recall", "The pattern of atrophy in Type A gastritis is:",
    "Patchy, mainly in the corpus", ["Multifocal throughout the stomach", "Antral-only without corpus involvement", "Diffuse body and fundus with antral sparing"],
    "Type A atrophy is patchy and mainly corpus-predominant.")
add(S4, 55, "recall", "The HLA association printed for Type A autoimmune gastritis is:",
    "HLA-B8/DR3", ["HLA-B27/DR4", "HLA-DQ2/DQ8", "HLA-B51/DR7"],
    "The page links autoimmune Type A gastritis with HLA B8/DR3.")
add(S4, 55, "recall", "The antibody in Type A gastritis is directed against parietal cells in the:",
    "Body", ["Antrum", "Pylorus", "Duodenal bulb"],
    "The Type A diagram specifies antibodies against parietal cells in the body.")
add(S4, 55, "recall", "Which sequence follows parietal-cell loss in Type A gastritis?",
    "↓ acid → achlorhydria → hypergastrinaemia → gastrin-secreting carcinoid tumour", ["↑ acid → hypergastrinaemia → gastric ulcer → carcinoid", "↓ intrinsic factor → intestinal metaplasia → adenocarcinoma", "H. pylori → multifocal atrophy → low gastrin"],
    "The printed Type A sequence is low acid, achlorhydria, hypergastrinaemia and then a gastrin-secreting carcinoid tumour.")
add(S4, 55, "recall", "Loss of intrinsic factor in Type A gastritis is linked to:",
    "Megaloblastic anaemia", ["Microcytic anaemia", "Thrombocytopenia", "Sideroblastic anaemia"],
    "Reduced intrinsic factor is linked to megaloblastic anaemia in the diagram.")
add(S4, 55, "recall", "The risk of malignancy column for Type A gastritis points:",
    "Downward", ["Upward", "To no change", "To a value of 60%"],
    "The table shows a downward arrow for Type A risk of malignancy.")
add(S4, 55, "recall", "Type B chronic gastritis is marked as:",
    "More common", ["Less common", "The rare childhood-only type", "Unrelated to H. pylori"],
    "Type B is marked more common.")
add(S4, 55, "recall", "Type B is also called:",
    "Environmental metaplastic atrophic gastritis (EMAG)", ["Autoimmune metaplastic atrophic gastritis (AMAG)", "Protein-losing hypertrophic gastritis", "Acute phlegmonous gastritis"],
    "Type B is named environmental metaplastic atrophic gastritis (EMAG).")
add(S4, 55, "recall", "The pattern of atrophy in Type B gastritis is:",
    "Multifocal", ["Patchy and mainly corpus-only", "Limited to the pylorus", "Absent by definition"],
    "The table labels Type B atrophy multifocal.")
add(S4, 55, "recall", "Which progression is shown for Type B/H. pylori gastritis?",
    "Gastritis → gastric atrophy → intestinal metaplasia → gastric adenocarcinoma", ["Gastritis → achlorhydria → megaloblastic anaemia → carcinoid", "Gastritis → villous atrophy → lymphoma → ileal perforation", "Gastritis → hyperplasia → mucus loss → duodenal web"],
    "The Type B diagram shows gastritis progressing through gastric atrophy and intestinal metaplasia to gastric adenocarcinoma.")
add(S4, 55, "recall", "The Type B risk-of-malignancy indicator points:",
    "Upward", ["Downward", "To zero", "To no difference from Type A"],
    "The table shows increased malignancy risk for Type B.")
add(S4, 55, "recall", "The note links eosinophilic gastritis to:",
    "Intestinal obstruction", ["Pseudo-tumour appearance", "Celiac disease", "Crohn's disease as the commonest cause"],
    "Eosinophilic gastritis is linked to intestinal obstruction.")
add(S4, 55, "recall", "Russell body gastritis is associated with which endoscopic appearance?",
    "A pseudotumour appearance", ["Large tortuous folds sparing the antrum", "A string sign", "A lead-pipe colon"],
    "Russell body gastritis is noted for a pseudotumour endoscopic appearance.")
add(S4, 55, "recall", "The commonest cause named for granulomatous gastritis is:",
    "Crohn's disease", ["Celiac disease", "H. pylori alone", "Ulcerative colitis"],
    "The note lists Crohn's disease as the most common cause of granulomatous gastritis.")
add(S4, 55, "recall", "Lymphocytic gastritis is associated with:",
    "Celiac disease", ["Crohn's disease", "CMV infection", "H. pylori-associated duodenal ulcer only"],
    "The note pairs lymphocytic gastritis with celiac disease.")
add(S4, 55, "recall", "Hypertrophic gastritis is also known as Ménétrier disease or:",
    "Protein-losing gastropathy", ["Autoimmune metaplastic atrophic gastritis", "Pseudomembranous enterocolitis", "Acute phlegmonous gastritis"],
    "The page names Ménétrier disease/protein-losing gastropathy.")
add(S4, 55, "recall", "The large tortuous folds of hypertrophic gastritis involve the:",
    "Body and fundus, sparing the antrum", ["Antrum and pylorus, sparing the fundus", "Entire bowel, including duodenum", "Corpus only, sparing the fundus and antrum"],
    "The page says body and fundus are involved with antral sparing and large tortuous mucosal folds.")
add(S4, 55, "numeric", "The demographic pattern given for hypertrophic gastritis is:",
    "More common in males, usually 40–60 years", ["More common in females, usually under 20 years", "Equal by sex, usually over 70 years", "More common in males, usually under 5 years"],
    "The page lists male > female and an age range of 40–60 years.")
add(S4, 55, "recall", "In children, hypertrophic gastritis is associated with:",
    "CMV infection", ["Rotavirus infection", "Shigella infection", "H. pylori is excluded"],
    "The note links childhood hypertrophic gastritis with CMV infection.")
add(S4, 56, "recall", "The main cytokine named in the pathogenesis of hypertrophic gastritis is:",
    "TGF-α", ["IL-5", "TNF-β", "IFN-γ"],
    "The pathogenesis section identifies TGF-α as the main cytokine.")
add(S4, 56, "recall", "Which hypertrophic-gastritis sequence is shown?",
    "Foveolar hyperplasia → mucus hypersecretion → protein loss", ["Parietal-cell loss → acid excess → iron loss", "Villous atrophy → bile-acid loss → cAMP rise", "Granuloma formation → fibrosis → ileal obstruction"],
    "The diagram links foveolar hyperplasia to mucus hypersecretion and then protein loss.")
add(S4, 56, "recall", "Which laboratory/clinical consequences of protein loss are listed?",
    "Hypoalbuminaemia and oedema", ["Hyperalbuminaemia and dehydration", "Polycythaemia and hypertension", "Hypocalcaemia and jaundice only"],
    "Clinical features include hypoalbuminaemia, oedema and upper-GI symptoms.")
add(S4, 56, "recall", "The p56 investigation note recommends endoscopy with which biopsy for hypertrophic gastritis?",
    "Full-thickness gastric biopsy", ["Antral biopsy for rapid urease testing only", "Duodenal biopsy for villous architecture", "Superficial brushing without tissue sampling"],
    "The page recommends endoscopy with full-thickness biopsy and separately describes the condition as premalignant.")
add(S4, 56, "management", "Which treatment is marked as the main treatment for hypertrophic gastritis?",
    "Surgery", ["Gluten-free diet", "Antibiotics alone", "Ringer lactate"],
    "Surgery is marked as the main treatment.")
add(S4, 56, "recall", "The medical option listed for hypertrophic gastritis is an EGFR antagonist:",
    "Cetuximab", ["Octreotide", "Azithromycin", "Linaclotide"],
    "Cetuximab is listed as the medical EGFR antagonist.")

# ---------------------------------------------------------------------------
# Book p56–57 — H. pylori introduction, pathology and virulence factors
add(S5, 56, "recall", "H. pylori is introduced as a:",
    "Gram-negative bacillus", ["Gram-positive spore-forming bacillus", "Acid-fast organism", "Helminth"],
    "The introduction identifies H. pylori as a Gram-negative bacillus.")
add(S5, 56, "recall", "Which three positive tests complete the H. pylori 'triple positive' diagram?",
    "Urease, oxidase and catalase", ["Urease, coagulase and indole", "Oxidase, CAMP and citrate", "Catalase, bile solubility and oxidase-negative"],
    "The triangle is labelled urease positive, oxidase positive and catalase positive.")
add(S5, 56, "recall", "Urease helps H. pylori:",
    "Reside in the stomach", ["Invade the bloodstream", "Absorb vitamin B12", "Form a pseudomembrane"],
    "The page notes that urease helps H. pylori reside in the stomach.")
add(S5, 56, "recall", "The page locates H. pylori initially in the antrum and says it can migrate proximally because of:",
    "Flagella", ["Pili of the toxin-coregulated pilus", "Auerbach's plexus", "Bile salts"],
    "H. pylori is present in the antrum and can migrate proximally due to flagella.")
add(S5, 56, "truefalse", "TRUE or FALSE — the introduction says H. pylori is invasive and resides on the exposed surface rather than within mucus.",
    "False — it is non-invasive and resides deep in the mucosal gel", ["True — it invades the full gastric wall", "False — it resides in the bloodstream", "True — it is limited to the pyloric lumen"],
    "The page describes H. pylori as non-invasive and resident deep in the mucosal gel.")
add(S5, 56, "recall", "The transmission route listed for H. pylori is:",
    "Faeco-oral", ["Airborne", "Tick-borne", "Parenteral only"],
    "The pathology section states faeco-oral transmission.")
add(S5, 56, "recall", "H. pylori colonisation is said to depend on:",
    "Socioeconomic factors", ["Blood group alone", "Sex only", "Gastric pH only"],
    "The page links colonisation to socioeconomic factors.")
add(S5, 56, "numeric", "The approximate H. pylori-colonised proportion printed for developing countries is:",
    "80%", ["10%", "27%", "60%"],
    "The note gives 80% in developing countries.")
add(S5, 56, "recall", "Among colonised people, the majority outcome shown in the progression diagram is:",
    "Chronic superficial gastritis", ["Peptic ulcer", "Gastric carcinoma", "MALT lymphoma"],
    "The diagram sends the majority to chronic superficial gastritis and 10% to peptic ulcer.")
add(S5, 56, "numeric", "The progression diagram assigns what proportion of colonised people to peptic ulcer?",
    "10%", ["80%", "50%", "2%"],
    "The peptic-ulcer branch is marked 10%.")
add(S5, 56, "recall", "H. pylori urease creates which local environment according to p56?",
    "An alkaline environment", ["An acidic microenvironment", "A bile-rich environment", "A low-oxygen bloodstream"],
    "Urease is described as creating an alkaline environment.")
add(S5, 56, "recall", "The second enzyme named on p56 is protease, which:",
    "Digests mucin", ["Produces intrinsic factor", "Converts gastrin to secretin", "Forms iron–transferrin complexes"],
    "The page says protease digests mucin.")
add(S5, 56, "recall", "Which conditions are listed under the note 'Protective against' on p56?",
    "GERD and Barrett's oesophagus", ["Gastric ulcer and duodenal ulcer", "MALToma and gastric adenocarcinoma", "Celiac disease and tropical sprue"],
    "The source note lists GERD and Barrett's oesophagus, as well as adenocarcinoma of oesophagus and stomach. This is reproduced as a book note, not a contemporary causal claim.")
add(S5, 56, "recall", "Which cancer does the p56 'Protective against' list include, despite this being a source-text error?",
    "Adenocarcinoma of the stomach", ["Gastric MALT lymphoma", "Pancreatic neuroendocrine tumour", "Colorectal adenocarcinoma"],
    "The scan places 'adenocarcinoma of stomach' under 'Protective against'. This contradicts authoritative cancer guidance; treat it as a source-text error, not a medical fact. See audit/known-source-caveats.md.")
add(S5, 57, "numeric", "H. pylori is attributed what proportion of duodenal ulcers on p57?",
    "70–80%", ["10–20%", "30–40%", "50–60%"],
    "The page states 70–80% of duodenal ulcers.")
add(S5, 57, "numeric", "The proportion of gastric ulcers attributed to H. pylori is listed as:",
    "50–60%", ["10–20%", "30–40%", "70–80%"],
    "The page states 50–60% of gastric ulcers.")
add(S5, 57, "recall", "Which pair of additional diseases appears under diseases caused by H. pylori?",
    "Stomach carcinoma and MALToma", ["Pancreatic carcinoma and gastrinoma", "Celiac disease and Whipple disease", "Crohn's disease and ulcerative colitis"],
    "The list includes carcinoma of the stomach and MALToma.")
add(S5, 57, "recall", "Flagella contribute to H. pylori virulence chiefly by enabling:",
    "Motility and chemotaxis to colonise beneath the mucosa", ["Direct inhibition of CD4 T-cell proliferation", "Adenyl-cyclase activation in enterocytes", "Conversion of Fe2+ to Fe3+"],
    "The diagram links flagella with bacterial mobility/chemotaxis and colonisation beneath the mucosa.")
add(S5, 57, "recall", "The urease virulence arm can injure gastric mucosa through production of:",
    "Ammonia", ["Verocytotoxin", "Neuraminidase", "cGMP"],
    "The figure says urease neutralises gastric acid and ammonia causes gastric mucosal injury.")
add(S5, 57, "recall", "In the virulence diagram, lipopolysaccharides are shown to:",
    "Adhere to host cells and promote inflammation", ["Digest mucin and create an alkaline environment", "Cause only small-bowel secretory diarrhoea", "Bind the CCK-B receptor"],
    "Lipopolysaccharides are linked to host-cell adherence and inflammation.")
add(S5, 57, "recall", "The outer proteins in the H. pylori diagram are linked to:",
    "Adherence to host cells", ["Gastrin secretion", "Bile-acid absorption", "Mucosal prostaglandin synthesis"],
    "Outer proteins are labelled as adhering to host cells.")
add(S5, 57, "recall", "VacA is described as a vacuolating toxin causing gastric mucosal injury and:",
    "Inhibition of CD4 T-cell proliferation", ["Stimulation of CD4 T-cell proliferation", "A rise in cAMP in small bowel", "Production of intrinsic factor"],
    "The VacA note links mucosal injury with inhibition of CD4 T-cell proliferation.")
add(S5, 57, "recall", "Which enzyme set is listed under H. pylori secretory enzymes?",
    "Mucinase, protease and lipase", ["Urease, catalase and oxidase", "Amylase, lactase and sucrase", "Elastase, trypsin and chymotrypsin"],
    "The figure lists mucinase, protease and lipase as secretory enzymes causing mucosal injury.")
add(S5, 57, "recall", "The H. pylori type IV secretion system is described as a pili-like structure for:",
    "Injection of effectors", ["Absorption of haem iron", "Secretion of gastric mucus", "Formation of bile salts"],
    "The diagram labels the type IV system as a pili-like structure for injection of effectors.")
add(S5, 57, "recall", "Which group of effects is attributed to CagA-related effectors in the host cell?",
    "Actin remodelling, IL-8 induction, host-cell growth and apoptosis inhibition", ["Reduced motility, lower IL-8 and increased apoptosis", "cAMP reduction, acid suppression and cell-cycle arrest", "Iron storage, ferritin secretion and erythroid maturation"],
    "The figure lists actin remodelling, IL-8 induction, host-cell growth and apoptosis inhibition.")

# ---------------------------------------------------------------------------
# Book p57–58 — gastritis forms, dyspepsia and investigations
add(S6, 57, "recall", "Which H. pylori gastritis pattern is linked to duodenal ulcer in the forms-of-gastritis list?",
    "Antral-predominant gastritis", ["Corpus-predominant atrophic gastritis", "Non-atrophic pangastritis", "Hypertrophic gastritis"],
    "Antral-predominant gastritis is linked to duodenal ulcer.")
add(S6, 57, "recall", "Which downstream sequence follows corpus-predominant atrophic gastritis in the diagram?",
    "Gastric ulcer; intestinal metaplasia → dysplasia → carcinoma", ["Duodenal ulcer; MALToma → remission", "Protein loss; oedema → CMV infection", "Pseudomembrane; toxic megacolon → perforation"],
    "Corpus-predominant atrophic gastritis is linked to gastric ulcer and intestinal metaplasia → dysplasia → carcinoma.")
add(S6, 57, "recall", "Non-atrophic pangastritis is linked to MALToma, identified on the page as the most common:",
    "Extranodal marginal-zone B-cell lymphoma", ["T-cell lymphoma of the small bowel", "Pancreatic neuroendocrine tumour", "Gastric stromal tumour"],
    "The page calls MALToma the most common extranodal marginal-zone lymphoma (B-cell).")
add(S6, 57, "numeric", "The p57 dyspepsia note estimates what proportion as functional?",
    "75%", ["25%", "50%", "90%"],
    "The printed note says dyspepsia is 75% functional.")
add(S6, 57, "recall", "Which symptom is included in the clinical-diagnosis cluster for dyspepsia?",
    "Postprandial fullness", ["Haematemesis", "Painless rectal bleeding", "Steatorrhoea"],
    "The dyspepsia symptom cluster is postprandial fullness, early satiety and epigastric discomfort.")
add(S6, 57, "recall", "Which trio is grouped as a clinical diagnosis for dyspepsia?",
    "Postprandial fullness, early satiety and epigastric discomfort", ["Nocturnal diarrhoea, tenesmus and fever", "Haematemesis, jaundice and pruritus", "Dysphagia, steatorrhoea and weight loss"],
    "The page brackets postprandial fullness, early satiety and epigastric discomfort as clinical diagnosis.")
add(S6, 57, "management", "The initial dyspepsia management trial written on p57 is:",
    "A one-week daily-dose PPI trial", ["A one-day antibiotic course", "A six-month steroid course", "A 72-hour fasting challenge"],
    "The scan reads 'a week trial of PPI (daily dose)'; it does not specify two weeks.")
add(S6, 57, "numeric", "Which age threshold is listed among indications for endoscopy in dyspepsia?",
    ">50 years", [">30 years", ">40 years", ">70 years"],
    "Age >50 years is one of the listed endoscopy indications.")
add(S6, 57, "recall", "Which pair of swallowing symptoms appears among the dyspepsia endoscopy indications?",
    "Dysphagia and odynophagia", ["Dyspepsia and dyschezia", "Regurgitation and tenesmus", "Globus and hoarseness"],
    "Dysphagia and odynophagia are listed indications for endoscopy.")
add(S6, 57, "recall", "Which laboratory/clinical feature appears in the endoscopy-indication list?",
    "Anaemia", ["Eosinophilia", "Hyperalbuminaemia", "Polycythaemia"],
    "Anaemia is listed as an indication for endoscopy.")
add(S6, 57, "recall", "Which pair completes the non-age alarm indications for dyspepsia endoscopy on p57?",
    "Weight loss and an abdominal mass", ["Constipation and abdominal distension", "Mild nausea and early satiety", "Pica and hair fall"],
    "Weight loss and an abdominal mass are listed indications.")
add(S6, 57, "recall", "The family-history indication in the dyspepsia endoscopy list is a history of:",
    "Stomach carcinoma", ["Celiac disease", "Gallstones", "Colorectal polyps only"],
    "The list includes a family history of stomach carcinoma.")
add(S6, 58, "scenario", "Which pain pattern is used on p58 to illustrate epigastric pain associated with peptic ulcer disease?",
    "Recurrent or nocturnal pain, precipitated by fasting and relieved by food", ["Continuous right-lower-quadrant pain relieved by defecation", "Postprandial pain with jaundice and fever", "Pain only during exercise, unaffected by meals"],
    "The diagram lists recurrent episodes, nocturnal pain, fasting precipitation and relief on eating.")
add(S6, 58, "recall", "The indication for endoscopy in the p58 investigation section is epigastric pain as a symptom of:",
    "Peptic ulcer disease", ["Irritable bowel syndrome", "Celiac disease", "Pseudomembranous colitis"],
    "The page says endoscopy is indicated for epigastric pain as a symptom of peptic ulcer disease.")
add(S6, 58, "recall", "After endoscopy shows an ulcer, the sequence shown is:",
    "Test for H. pylori → anti-H. pylori treatment", ["Start treatment → then decide whether to test", "Test for C. difficile → give vancomycin", "Measure serum gastrin → proceed to colectomy"],
    "The diagram gives endoscopy → if ulcer present, H. pylori testing → anti-H. pylori treatment.")
add(S6, 58, "truefalse", "TRUE or FALSE — the ACG recommendation says to test for H. pylori only if treatment will be offered when the result is positive.",
    "True — testing should be linked to an offer of treatment", ["False — test even when no treatment is planned", "False — only test after treatment fails", "True — but only in children"],
    "The note says testing should be performed only if the clinician plans to treat a positive result.")
add(S6, 58, "recall", "In the rapid urease test, the tissue sample is obtained by biopsy from the:",
    "Antrum", ["Fundus", "Oesophagus", "Terminal ileum"],
    "The sequence is endoscopy → antral biopsy → urease test on tissue.")
add(S6, 58, "recall", "A positive rapid urease test is indicated by:",
    "A colour change", ["A fall in stool pH", "A rise in serum gastrin", "A positive Kanagawa phenomenon"],
    "The rapid urease test is positive when the tissue test changes colour.")
add(S6, 58, "recall", "Which two tests are listed to confirm H. pylori eradication?",
    "Stool antigen and 13C/14C urea breath tests", ["Rapid urease and fecal calprotectin", "Serum IgE and stool culture", "D-xylose and Schilling tests"],
    "The source lists stool antigen and C13/C14 urea breath tests to confirm eradication.")
add(S6, 58, "numeric", "The stool-antigen test performance printed on p58 is:",
    "Sensitivity 94%; specificity 97%", ["Sensitivity 97%; specificity 94%", "Sensitivity 80%; specificity 60%", "Sensitivity 50%; specificity 100%"],
    "The page gives sensitivity 94% and specificity 97%.")
add(S6, 58, "recall", "Which medications are listed as affecting stool-antigen-test sensitivity?",
    "PPIs, bismuth and antibiotics", ["Iron, folate and calcium", "NSAIDs, steroids and insulin", "Loperamide, psyllium and PEG"],
    "PPI, bismuth and antibiotics are listed as affecting sensitivity.")
add(S6, 58, "numeric", "The page recommends what gap after treatment before performing the eradication test?",
    "One month", ["One week", "Three days", "Six months"],
    "The note specifies a one-month gap after treatment before testing.")

# ---------------------------------------------------------------------------
# Book p58–59 — regimens and test-of-cure algorithm
add(S7, 58, "numeric", "The first-line H. pylori regimen is given for:",
    "14 days", ["5 days", "7 days", "21 days"],
    "The page specifies a 14-day first-line regimen.")
add(S7, 58, "recall", "Which alternatives are abbreviated OCA and OCM in the p58 first-line regimen?",
    "OCA: omeprazole + clarithromycin + amoxicillin; OCM: omeprazole + clarithromycin + metronidazole", ["OCA: omeprazole + amoxicillin + metronidazole; OCM: omeprazole + clarithromycin + tetracycline", "OCA: omeprazole + clarithromycin + tetracycline; OCM: omeprazole + bismuth + amoxicillin", "Both abbreviations describe a four-drug course of omeprazole, bismuth, tetracycline and metronidazole"],
    "OCA and OCM are alternative three-drug regimens, not a single four-drug course.")
add(S7, 58, "numeric", "The omeprazole dose in the first-line regimen is:",
    "20 mg twice daily", ["20 mg once daily", "40 mg three times daily", "200 mg twice daily"],
    "The printed first-line dose is omeprazole 20 mg BD.")
add(S7, 58, "numeric", "The amoxicillin dose in the OCA first-line alternative is:",
    "1 g twice daily", ["500 mg once daily", "2 g three times daily", "200 mg twice daily"],
    "The page lists amoxicillin 1 g BD.")
add(S7, 58, "numeric", "The clarithromycin dose in the first-line regimen is:",
    "500 mg twice daily", ["200 mg twice daily", "1 g once daily", "500 mg once weekly"],
    "The page lists clarithromycin 500 mg BD.")
add(S7, 58, "numeric", "The metronidazole dose in the OCM first-line alternative is:",
    "500 mg twice daily", ["200 mg once daily", "1 g three times daily", "2 g once weekly"],
    "The source lists metronidazole 500 mg BD.")
add(S7, 58, "recall", "Which four drugs make up the second-line OBTM combination on p58?",
    "Omeprazole, bismuth subsalicylate, tetracycline and metronidazole", ["Omeprazole, clarithromycin, amoxicillin and metronidazole", "Omeprazole, azithromycin, doxycycline and vancomycin", "Bismuth, fidaxomicin, rifaximin and amoxicillin"],
    "OBTM is omeprazole, bismuth subsalicylate, tetracycline and metronidazole.")
add(S7, 58, "recall", "The note cautions that alternative regimens may depend on:",
    "Local antibiotic resistance", ["Patient height alone", "Time of day of endoscopy", "Stool volume only"],
    "The page says other regimens are used depending on antibiotic resistance in the area.")
add(S7, 59, "scenario", "A patient with a treatment indication has a negative H. pylori test. What conclusion follows in the p59 algorithm?",
    "H. pylori is not the cause", ["Proceed to second-line therapy", "Start third-line culture-directed therapy", "Repeat a positive stool antigen test"],
    "A negative initial test leads to 'H. pylori not the cause'.")
add(S7, 59, "recall", "After a positive test and first-line treatment, the algorithm delays the test of cure until:",
    "At least one month after treatment finishes", ["The next day", "One week after treatment begins", "Three months before treatment finishes"],
    "The flowchart says to wait at least one month after treatment finishes.")
add(S7, 59, "recall", "During the month before the post-treatment test, the flowchart says to avoid:",
    "Antibiotics, bismuth compounds and proton-pump inhibitors", ["Iron, folate and vitamin B12", "Only antacids and H2 blockers", "All food and fluids"],
    "The flowchart specifies no antibiotics, bismuth compounds or PPIs in the interim.")
add(S7, 59, "recall", "The post-treatment test in the algorithm is either a urea breath test or:",
    "Stool-antigen test", ["Serum gastrin test", "Rapid urease test without biopsy", "Fecal elastase"],
    "The flowchart uses urea breath or stool antigen testing.")
add(S7, 59, "scenario", "After first-line treatment, a patient's test of cure is negative but symptoms persist. The algorithm attributes the remaining symptoms to:",
    "A cause other than H. pylori", ["Persistent H. pylori by definition", "Resistance requiring third-line treatment", "A false-negative result requiring immediate surgery"],
    "A negative test leads to the note that any remaining symptoms are not due to H. pylori.")
add(S7, 59, "scenario", "The test of cure remains positive after first-line treatment. The next treatment step shown is:",
    "Second-line treatment", ["No further treatment", "Immediate gastrectomy", "Endoscopy with culture before any second-line therapy"],
    "A positive test after first-line treatment leads to second-line treatment.")
add(S7, 59, "scenario", "After second-line therapy, H. pylori remains positive. Which next approach appears in the diagram?",
    "Third-line treatment with endoscopy, culture and sensitivity", ["Return to the same first-line course without testing", "Stop treatment and diagnose IBS", "Start IV metronidazole for fulminant colitis"],
    "The third-line step is endoscopy with H. pylori culture/sensitivity and treatment according to known sensitivities.")
add(S7, 59, "recall", "How should third-line treatment be selected in the p59 algorithm?",
    "According to known antibiotic sensitivities", ["By the patient's blood group", "By the appearance of the stool alone", "Without culture or sensitivity information"],
    "The flowchart states to treat according to known antibiotic sensitivities.")
add(S7, 59, "scenario", "A patient is still positive after third-line treatment. The final pathway is to:",
    "Refer to a specialist and reconsider whether treatment remains indicated", ["Repeat first-line therapy indefinitely", "Proceed directly to colectomy", "Stop all follow-up without review"],
    "The algorithm calls for specialist referral and consideration of whether treatment is still indicated.")

GUIDES = {
    S1: ("Regions, Glands & Cells", "Fundus above GES; body between GES and incisura; antrum below incisura.\nFundic, oxyntic and pyloric glands contain region-specific ECL, parietal, chief, mucous and G cells.\nReview secretions and the diagram labels: rugae, curvatures, papillae and duodenum."),
    S2: ("Mucosal Defence and Wall", "Defence layers: pre-epithelial, epithelial/restitution and subepithelial.\nSeparate damaging exposures from mucus, bicarbonate, blood-flow, barrier and repair protection.\nAuerbach = motility; Meissner = secretion; ICC generate BER."),
    S3: ("Acid Regulation & Acute Gastritis", "Histamine/cAMP, gastrin/CCK-B and acetylcholine/M3-Ca²⁺ cooperate to increase acid.\nThe BAO/MAO threshold is >0.6; the page gives MAO at 6 pm and least output at 6 am.\nGastritis is histologic; acute phlegmonous gastritis is severe and linked to neutrophils."),
    S4: ("Chronic & Hypertrophic Gastritis", "Type A: less common autoimmune, patchy corpus, parietal-cell antibodies; Type B: commoner, multifocal, H. pylori.\nFollow each type's complications and malignancy arrow; retain the four gastritis associations.\nMénétrier disease: TGF-α/foveolar hyperplasia → mucus/protein loss; surgery is main treatment in the text."),
    S5: ("H. pylori Biology & Virulence", "Gram-negative, urease/oxidase/catalase positive; antral, flagellated, non-invasive and deep in mucosal gel.\nTransmission is faeco-oral; the source lists ulcer/cancer associations and enzyme actions.\nKnow the roles of VacA, LPS, outer proteins, type IV secretion and CagA effectors."),
    S6: ("H. pylori, Dyspepsia & Testing", "Antral-predominant → duodenal ulcer; corpus atrophy → metaplasia/dysplasia/carcinoma; pan-gastritis → MALToma.\nDyspepsia symptom cluster, one-week PPI note and alarm indications precede H. pylori investigations.\nRapid urease uses antral biopsy; stool antigen and urea-breath testing confirm eradication after a one-month gap."),
    S7: ("Treatment & Test of Cure", "The p58 first-line and OBTM second-line regimens are transcribed as printed.\nThe p59 algorithm tests, treats, waits at least one month and branches by stool antigen/urea breath result.\nPersistent positivity proceeds to later-line sensitivity-guided specialist review; this is book study, not current guidance."),
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
