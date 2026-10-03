# PULSE Medicine Vol 1 — Progress

Updated **2026-10-03** (Chapters 19–21 released and deployed; source review now reaches Book p125). Standalone offline quiz based on *PULSE Medicine Vol 1*, printed Book p1–375 (Marrow Edition 8).

- Repository: `Deva20045/Med-V1`
- Session branch: `arena/01a0ffb8-med-v1`
- Published URL: https://deva20045.github.io/Med-V1/
- Editable source of truth: `data/chNN.json`; generated offline deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- **Build status: 21 live chapters / 61 · 1,900 questions / 163 units.** Chapters 1–21 are embedded by `build_content.py`; the GitHub Pages deployment for this release succeeded. Source coverage is complete through Book p125.

## This release — Chapters 19 to 21 (Book p107–125)

The requested three myeloproliferative/bone-marrow-failure chapters were reviewed sheet-by-sheet in printed order (`uploads/01.pdf` PDF119–129 and `uploads/02.pdf` PDF1–8), then encoded with shuffled, parallel, non-predictable options across all formats (`recall`, `numeric`, `scenario`, `truefalse`, `oddoneout`, `management`, `fillup`, and 2- to 4-item bijective `match` items) and page-cited explanations. Handwritten numerals (≥16.5/≥16, 30:1, >1.5 × 10⁶, <30.0 × 10⁹/L, 6–8 years, WBC >2 lakh, 25%, 6 months, <0.1%) were cross-checked visually at high zoom and are recorded in [audit/known-source-caveats.md](audit/known-source-caveats.md). Existing Chapters 1–18 remain unchanged.

| Ch | Title | Printed pages | PDF sheets | Questions | Units |
|---:|---|---:|---:|---:|---:|
| 19 | Myeloproliferative Neoplasms : Part 1 | 107–115 | 01.pdf PDF119–127 | 83 | 9 |
| 20 | Myeloproliferative Neoplasms : Part 2 | 116–120 | 01.pdf PDF128–129 + 02.pdf PDF1–3 | 53 | 5 |
| 21 | Bone Marrow Failure Syndromes | 121–125 | 02.pdf PDF4–8 | 52 | 5 |
| **Cumulative total** |  | **125 book pages** |  | **1,900** | **163** |

Cumulative format distribution through Chapter 21: 1,239 recall, 199 numeric, 140 match, 100 fillup, 69 scenario, 64 truefalse, 52 oddoneout, 37 management.

### Chapter 19 — Myeloproliferative Neoplasms : Part 1 (p107–115)

CMP physiology and MPN pathology (mature multilineage proliferation, no dysplastic/immature cells), the printed MPN list with mutations (PCRV m/c; JAK-2 bracket over PCRV/PMF/ET with chr 9p deletion in PMF; CML BCR-ABL t(9;22); CNL CSF3R; CEL PDGFRA; BCR-ABL-negative CNL/CEL/JMML/MPN-NOS; myelophthisis note; systemic mastocytosis c-kit excluded), MPN clinical features (EMH spleen m/c; splenomegaly massive CML/PMF–moderate PCRV–mild ET; B symptoms 20%; MDS/MPN overlap WHO 5th), polycythemia thresholds (male ≥16.5/49, female ≥16/48), relative polycythemia (Gaisböck's, ↓ plasma volume, post-viral), absolute polycythemia table (EPO normal-to-low vs increased; TC/PLC increased vs normal), secondary etiologies (hypoxia incl. hepatopulmonary syndrome; renal artery stenosis; paraneoplastic incl. von Hippel-Lindau hemangioblastoma and the pallor-in-pheochromocytoma note), PCRV (JAK-2 100% exon 14 V617F 95%/exon 12 5%; arterial>venous thrombosis with Budd-Chiari/DVT/stroke-in-young; aquagenic pruritus; transcobalamin-I ↑ B12 binding; acquired vWD bleeding; erythromelalgia; hyperuricemia; ↓ ESR ↓ rouleaux; LAP high), PCRV criteria (Hb >16.5/>16, hypercellular marrow, JAK-2; minor subnormal EPO) and risk-stratified treatment (weekly phlebotomy Hb 13–14 + aspirin vs + ruxolitinib 10 mg BD or hydroxyurea 0.5–2 g/day), PMF etiology (JAK-2 50%, CALR 30–40%, MPL 10–20%, triple-negative poor prognosis, del 13q), PMF pathogenesis (CXCR4-lacking dysplastic megakaryocytes, TGF-β/PDGF, type-III collagen fibrosis, leukoerythroblastosis), PMF features (fibrotic stage, >60 yrs, thrombosis PCRV>ET>PMF, 75% massive splenomegaly, osteosclerosis, portal hypertension, Sweet syndrome note re AML, cutaneous photo captions), PMF investigations (teardrop/dacryocytes, cloud-like megakaryocytes, type-III procollagen peptide, dry tap, silver impregnation) and treatment (ruxolitinib/lenalidomide; AHSCT limitations; 5-year median survival), ET (JAK-2 50–60%, CALR, MPL; mild splenomegaly; thrombosis>bleeding; PLC >4.5 lakhs; staghorn cells; least myelofibrosis conversion; AML PCRV>PMF>ET) and ET evaluation/management (exclusion of reactive thrombocytosis; aspirin 75 mg/day vs hydroxyurea > interferon > anagrelide).

### Chapter 20 — Myeloproliferative Neoplasms : Part 2 (p116–120)

CML pathophysiology (myeloid-origin cells; myelopoiesis lines; BCR on 22q, ABL on 9q, MBS autoinhibition; balanced reciprocal translocation in 100% myeloid>B>T; ABL exon onto BCR exon 13/14; Ph chromosome 95%; absent MBS → constitutive ABL kinase → ATP docking → tyrosine phosphorylation), CML-vs-AML comparison (fairly normal vs complete arrest differentiation; high multiple vs very high single lineage), asciminib-acts-on-MBS note, risk factors (50–70 yrs, male>female, radiation 6–8 years, germ line very low; 5-year survival 85–90%), clinical features (asymptomatic leukocytosis ~1 lakh m/c; fatigue via cytokines on CFU; massive splenomegaly symptom cluster; blast crisis ≥20% within 4 years untreated; gouty arthritis; basophil histamine skin signs; WBC >2 lakh hyperviscosity; B symptoms 10–15% classically Hodgkin's), investigations (smear myelocyte bulge/left shift, blasts <5%, eosinophilia/basophilia, thrombocytosis without events; LAP low with PNH note; tryptase; cytology/immunophenotyping/G-banding/FISH pairing; cytogenetics t(9;22) vs quantitative PCR; mandatory karyotyping for double Ph/trisomy 8/isochromosome 17/del 20q; dwarf megakaryocytes), marrow picture (hypercellularity, granulopoiesis 30:1, ↓ erythropoiesis, dwarf megakaryocytes, sea-blue histiocytes = Gaucher cells, fibrosis; Wright-Giemsa images), obsolete accelerated phase and obsolete Sokal/Hasford scales with parameters a–e, and management (hydroxyurea; full TKI table with generations, T315I row and side effects; CCR in 6 months as key survival predictor; molecular milestones 3/6/12 months with MMR <0.1%).

### Chapter 21 — Bone Marrow Failure Syndromes (p121–125)

Disease list (aplastic anemia, MDS, PRCA, myelophthisis), the pancytopenia flowchart (hypercellular arm: acute leukemia unless proven otherwise AML 80/ALL 20, MDS, PMF, hairy cell, megaloblastic, PNH, systemic SLE/HIV/TB/brucellosis/leishmaniasis/sarcoidosis; hypocellular + pancytopenia: aplastic anemia, 20% MDS, aleukemic leukemia, copper deficiency, lymphoma; ± pancytopenia: Q fever, Legionella, anorexia, TB), PMF/hairy-cell one-liners, the printed "hypercellular" slip under aplastic anemia (flagged; flowchart and p123 show hypocellular), bimodal ages (<20 inherited, >60 acquired), drug-dependent m/c cause and non-A non-B hepatitis m/c infection; inherited syndromes (Fanconi AR FANCA>FANCB/FANCC with features and image panels A/B/C, dyskeratosis congenita DKC/telomere with reticular pigmentation and dystrophic-nail photos, Shwachman-Diamond ribosomopathy with pancreatic exocrine insufficiency and metaphyseal dysplasia), acquired causes (idiopathic m/c, drugs, benzene, non-A B C hepatitis, PNH, eosinophilic fasciitis), drug table (dose-dependent anticancer temporary myelosuppression vs dose-independent chloramphenicol/sulfonamides/gold/acetazolamide/PTU/D-penicillamine), presentation bleeding>anemia>infection, features against diagnosis, severe thresholds as printed (Hb <9, retic <30.0, ANC <0.5, platelets <30.0 → AHSCT), hypocellular marrow with fat cells, equine ATG + cyclosporine (6 months, 50%) and eltrombopag; PRCA (thymoma/CLL; transient aplastic crisis with giant pronormoblasts and IVIG), MDS overview (AKA myeloid neoplasm; CMML overlap; global 70 yrs M>F multilineage vs India 40–60 yrs 5q-deletion female RBC-lineage lenalidomide; hypercellular 80%/hypocellular 20%; AML 25%; no EMH; fatigue; RBC parameters with SF3B1 ring sideroblasts on Perls), and page 125 (WBC blasts 5–19%, pseudo-Pelger-Huët 2 lobes, toxic granules, Döhle bodies; pawn-ball/binucleate/dysplastic megakaryocyte images; diagnostic features; R-IPSS with poor 7q/monosomy 7 paediatric, good 5q/20q, best 11q; treatment flowchart single lineage 5q present lenalidomide / absent erythropoietin, trilineage transplant or azacytidine/decitabine).

## Earlier release — Chapters 13 to 18 (Book p77–106)

The requested six hematology chapters were reviewed sheet-by-sheet in printed order (`uploads/01.pdf` PDF89–118), then encoded with shuffled, parallel, non-predictable options across all formats (`recall`, `numeric`, `scenario`, `truefalse`, `oddoneout`, `management`, `fillup`, and 3- to 4-item bijective `match` items) and page-cited explanations. Existing Chapters 1–12 remain unchanged.

| Ch | Title | Printed pages | PDF sheets | Questions | Units |
|---:|---|---:|---:|---:|---:|
| 1 | Diarrhea | 1–5 | 01.pdf PDF13–17 | 66 | 9 |
| 2 | Physiology of GIT Absorption and Selective Malabsorption | 6–13 | 01.pdf PDF18–25 | 150 | 15 |
| 3 | Clinical Features And Tests For Malabsorption | 14–17 | 01.pdf PDF26–29 | 80 | 9 |
| 4 | Global Malabsorption | 18–29 | 01.pdf PDF30–41 | 196 | 19 |
| 5 | Inflammatory Bowel Disease : Part 1 | 30–36 | 01.pdf PDF42–48 | 94 | 11 |
| 6 | Inflammatory Bowel Disease : Part 2 | 37–45 | 01.pdf PDF49–57 | 128 | 14 |
| 7 | Infectious Diarrhoea | 46–51 | 01.pdf PDF58–63 | 111 | 7 |
| 8 | Stomach | 52–59 | 01.pdf PDF64–71 | 150 | 7 |
| 9 | Gastrinoma | 60–62 | 01.pdf PDF72–74 | 67 | 5 |
| 10 | Irritable Bowel Syndrome | 63–65 | 01.pdf PDF75–77 | 58 | 5 |
| 11 | Clinical Approach to Anemia | 66–69 | 01.pdf PDF78–81 | 63 | 4 |
| 12 | Iron Metabolism | 70–76 | 01.pdf PDF82–88 | 134 | 9 |
| 13 | Approach To Microcytic Hypochromic Anemia | 77–81 | 01.pdf PDF89–93 | 83 | 5 |
| 14 | Macrocytic Anemia | 82–88 | 01.pdf PDF94–100 | 107 | 7 |
| 15 | Approach to Hemolysis | 89–91 | 01.pdf PDF101–103 | 44 | 3 |
| 16 | Immune Mediated Hemolytic Anemia | 92–96 | 01.pdf PDF104–108 | 62 | 5 |
| 17 | Non-Immune Mediated Hemolytic Anemia | 97–102 | 01.pdf PDF109–114 | 70 | 6 |
| 18 | Hemolytic Anemia : Miscellaneous | 103–106 | 01.pdf PDF115–118 | 49 | 4 |
| **Cumulative total** |  | **106 book pages** |  | **1,712** | **144** |

Cumulative format distribution through Chapter 18: 1,132 recall, 186 numeric, 114 match, 93 fillup, 66 scenario, 48 truefalse, 40 oddoneout, 33 management.

### Chapter 2 — Physiology of GIT Absorption and Selective Malabsorption (p6–13)

Stages of absorption and their anatomy, small-intestinal histology, the luminal–mucosal–post-mucosal fat pathway, bile acid physiology (500 g formed and excreted daily, 4 g pool), carbohydrate transporters and disaccharidases, protein absorption, lactase deficiency and lactose intolerance, abetalipoproteinemia and intestinal lymphangiectasia.

### Chapter 3 — Clinical Features And Tests For Malabsorption (p14–17)

Steps for evaluating malabsorption, the full clinical-feature list by system, fat malabsorption tests, the D-xylose test (25 g orally, urine over 4–6 hours, normal at least 4.5 g) with its false-positive causes, hydrogen breath tests, obsolete tests and biopsy diagnoses, and the Schilling test with its four phases.

### Chapter 4 — Global Malabsorption (p18–29)

Celiac disease (iceberg phenomenon, types, pathophysiology, associations, serology and biopsy, complications, gluten-free response), Whipple's disease, tropical sprue, bile acid versus fatty acid diarrhea, short bowel syndrome (below 200 cm, very severe below 100 cm) and small intestinal bacterial overgrowth (jejunal aspirate above 10³ CFU/mL as gold standard, rifaximin first line, macrolides avoided).

### Chapter 5 — Inflammatory Bowel Disease : Part 1 (p30–36)

Entities of IBD, microscopic and diversion colitis, normal colonic histology, epidemiology of UC and Crohn's, genetic syndromes, IPEX syndrome and early onset childhood IBD, pathogenesis, and the site, macroscopy and microscopy of both ulcerative colitis and Crohn's disease.

### Chapter 6 — Inflammatory Bowel Disease : Part 2 (p37–45)

Ulcerative colitis clinical features and endoscopy, barium enema, Crohn's clinical features, endoscopic and cross-sectional imaging signs, intestinal tuberculosis versus Crohn's disease, extraintestinal manifestations, other investigations and serology, Truelove and Witt's classification, medical management of UC, sulfasalazine and surgery, Crohn's grading and severity-based management, and malignancy in IBD.

### Chapter 7 — Infectious Diarrhoea (p46–51)

Duration and site patterns, small-/large-bowel organisms, viral and bacterial mechanisms, preformed toxins, cholera, V. parahaemolyticus and ETEC, HUS/Shigella, Salmonella/Campylobacter, and the C. difficile diagnostic and severity branches. Source treatment notes are flagged as study-only.

### Chapter 8 — Stomach (p52–59)

Stomach regions and glands, mucosal defence and wall, acid regulation, acute/chronic/hypertrophic gastritis, H. pylori biology and virulence, gastritis patterns, dyspepsia and alarm features, endoscopy/testing, printed eradication regimens and test-of-cure flow. The scan's one-week PPI note is transcribed as one week.

### Chapter 9 — Gastrinoma (p60–62)

Sporadic versus MEN1 disease, gastrinoma triangle, acid effects and malabsorption, clinical clues, fasting gastrin/secretin thresholds, somatostatin-receptor imaging and limitations, BAO/MAO ratio, treatment by setting/location, surgery and metastasis.

### Chapter 10 — Irritable Bowel Syndrome (p63–65)

Printed definition and associations, Rome IV line as printed, alarm features, bowel-pattern subtypes, visceral hypersensitivity and other mechanisms, FODMAP/lifestyle diagram, subtype treatment and adverse effects. A note identifies the source's omitted Rome IV onset criterion.

### Chapter 11 — Clinical Approach to Anemia (p66–69)

WHO haemoglobin thresholds, hematopoietic lineages, EPO/iron dependence, erythroid maturation morphology, reticulocyte staining/counts, corrected reticulocyte count and RPI, MCV/RPI flowchart, marrow cellularity, M:E ratio and image labels. Includes a CRC calculation scenario.

### Chapter 12 — Iron Metabolism (p70–76)

Body-iron pools, dietary heme/non-heme absorption, transport/export and marrow uptake, iron indices, staged deficiency, causes and iron-deficit formula, clinical signs, blood indices/smear, marrow, printed treatment notes and response timeline. Source-level medical caveats are documented separately.

### Chapter 13 — Approach To Microcytic Hypochromic Anemia (p77–81)

Normal versus microcytic hypochromic peripheral smear (target and pencil cells), anemia of chronic disease (IL-6/hepcidin pathway, iron indices, soluble transferrin receptor, marrow storage vs erythroblast iron, treatment), sideroblastic anemia (heme synthesis pathway, congenital δ-ALA synthase/B6 vs acquired causes including alcohol, lead, INH, pyrazinamide, chloramphenicol, copper deficiency, MDS, rheumatoid arthritis, ring sideroblasts on Prussian blue), thalassemia major vs trait, full four-condition comparison table (IDA, ACD, thalassemia trait, sideroblastic anemia), Mentzer index, RDW, inherited IDA (IRIDA/TMPRSS6, DMT1, aceruloplasminemia) and the p81 diagnostic protocol flowchart.

### Chapter 14 — Macrocytic Anemia (p82–88)

Megaloblastic versus non-megaloblastic macrocytic anemia (reticulocytosis false positivity, hypothyroidism, liver disease, alcoholism, drugs), Vitamin B12 versus folic acid stores/RDA/depletion table, cobalamin absorption pathway (salivary R-binder, parietal cell HCl/IF, pancreatic enzymes, ileal enterocyte uptake, TC-1/TC-2/TC-3 transport), odd-chain fatty acid and methionine synthase biochemical pathways, methylfolate trap, diagnostic workup (MCV > 100 fL, hypersegmented neutrophils, Howell-Jolly bodies, basophilic stippling, Cabot rings, teardrop cells, pancytopenia, indirect bilirubin/LDH, B12/folate/MMA/homocysteine profiles), and pernicious anemia (Type A gastritis, anti-parietal cell vs anti-IF antibodies, subacute combined degeneration of cord, investigations, and B12 replacement protocol).

### Chapter 15 — Approach to Hemolysis (p89–91)

Classification of hemolytic anemia by mechanism, inheritance, site of destruction (intravascular vs extravascular), clinical presentation (acute vs chronic) and defect location (intracorpuscular vs extracorpuscular, PNH exception), intravascular hemolysis cascade (free Hb, haptoglobin depletion, methemoglobin, hemoglobinuria in acute cases vs hemosiderinuria on Prussian blue in chronic cases), extravascular hemolysis in spleen (spherocytes, unconjugated bilirubin, urobilinogen, fecal stercobilinogen, absent bilirubinuria), summary comparison table, and general classification rules for inherited and immune hemolytic anemias.

### Chapter 16 — Immune Mediated Hemolytic Anemia (p92–96)

Autoimmune versus alloimmune classification, Direct and Indirect Coombs tests (principles, reagents, 3+/4+ positivity), DAT subtyping flowchart (anti-IgG and anti-C3d profiles), Warm AIHA versus Cold AIHA comparison table (IgG vs IgM, 37 °C vs 0–4 °C, etiologies, splenic Fc-mediated spherocytosis vs hepatic C3b-mediated agglutination/acrocyanosis), treatment ladders for Warm and Cold AIHA (steroids, rituximab, immunosuppressants, splenectomy status, plasmapheresis, bortezomib, sutimlimab), Evans syndrome, causes of spherocytes, paroxysmal cold hemoglobinuria (Donath–Landsteiner anti-P biphasic hemolysin), and the four mechanisms of drug-induced immune hemolysis.

### Chapter 17 — Non-Immune Mediated Hemolytic Anemia (p97–102)

Four categories of non-immune hemolysis (infections, drugs/toxins, PNH, fragmentation), PNH physiology and pathogenesis (X-linked somatic PIGA mutation, GPI anchor, CD55/DAF, CD59/MIRL, neutrophil alkaline phosphatase, UPAR, nitric oxide scavenging), PNH clinical triad (intravascular hemolysis, pancytopenia/MDS/AML, Budd–Chiari hepatic vein thrombosis), PNH investigations (Ham/sucrose lysis, FLAER gold standard, CD55/CD59 flow cytometry, Hb vs myoglobin plasma test) and management (ravulizumab > eculizumab + meningococcal vaccine, BMT), fragmentation hemolysis/MAHA/TMA pathogenesis (endothelial injury, vWF multimers, Gp Ib–IX/Gp VI, schistocytes/helmet cells), HUS versus TTP comparison, Childhood (D⁺, EHEC O157:H7/Shiga toxin, sorbitol MacConkey, supportive care, antibiotics CI) versus Adult HUS (D⁻/atypical, CFH/CFB/MCP mutations, sporadic drugs/states, plasmapheresis, rituximab/eculizumab), TTP (ADAMTS-13 deficiency, plasmapheresis + steroids + rituximab, caplacizumab, platelet transfusion CI), and fragmentation types (MAHA/march, cardiac prosthetic valve, Kasabach–Merritt consumption).

### Chapter 18 — Hemolytic Anemia : Miscellaneous (p103–106)

Inherited hemolytic anemia classification (hemoglobinopathies, membrane cytoskeleton disorders, enzymopathies), 5'-nucleotidase deficiency and cholestasis markers, hereditary spherocytosis (AD ankyrin ANK-1 > Band 3 vs AR β-spectrin, RBC membrane/cytoskeleton diagram with Band 3, spectrin dimer, glycophorin and P. falciparum binding, microvesicle pathogenesis in 3–4 µm splenic capillaries, clinical features, parvovirus B19 aplastic crisis, ↓ MCV and ↑↑ MCHC, ektacytometry, SDS-PAGE gold standard, EMA test, osmotic fragility, glycerol lysis/pink test, severity-based splenectomy and cholecystectomy rules), G6PD deficiency (X-linked intermediate, Class 2 Mediterranean, HMP shunt NADPH/glutathione pathway, oxidant drugs/infections/fava beans, malaria heterozygote protection, peripheral smear gallery with Heinz bodies, blister/hemighost cells, bite cells, triangle cells, helmet cells, echinocytes and basophilic stippling, fluorescent spot screening and quantitative assay, treatment), and anemia of blood loss (Stages I–III and the lethal triad of hypothermia, acidosis and DIC).

## Quality and ordering contract delivered

1. Every printed page p1–125 is covered in book order from the scanned source (no text layer exists); headings, table cells, image labels, flowchart arms, thresholds and notes are represented. Page map: `01.pdf` PDF13 = p1 … PDF129 = p117 and `02.pdf` PDF1 = p118 … PDF8 = p125; no requested sheets are missing.
2. `audit/coverage.json` holds **1,900 inventoried points** across Chapters 1–21; every ledger point resolves to exactly one question in question order and on the matching book page.
3. Four-option sets are unique, parallel in length/detail, and deterministically shuffled across all four positions (`A`–`D`). Matching items use 2- to 4-item bijections with varied permutations; true/false items have balanced 2 True / 2 False choices; numeric and fill-up questions use plausible clinical distractors; scenarios retain full clinical context.
4. IDs are sequential `MED-C<N>-<seq>`; the question array is strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, every unit guide is 2–4 lines, and every explanation ends with its exact `(Book pX)` citation matching the question page.
5. Chapters 1–21 are embedded in the standalone app with live flags set; **21/61 roadmap chapters are live**. See [audit/known-source-caveats.md](audit/known-source-caveats.md) for transcription and medical-source caveats.

## Verified PDF → printed-page map

Printed page numbers are ground truth. `uploads/01.pdf` is sequential after 12 unnumbered front-matter sheets (cover, author, title, instructions, 8 pages of combined Contents); `uploads/02.pdf` continues at Book p118; `uploads/03.pdf` continues at Book p248. Full mappings are in [audit/page-map.json](audit/page-map.json).

- `uploads/01.pdf` PDF13–129 = Book p1–117
- `uploads/02.pdf` PDF1–130  = Book p118–247
- `uploads/03.pdf` PDF1–128  = Book p248–375  (PDF129–131 are blank/end-quote matter)
- **PDF → Book formula:** `01.pdf: Book p = PDF page − 12`; `02.pdf: Book p = PDF page + 117`; `03.pdf: Book p = PDF page + 247`

Chapter sheet coverage source-reviewed through p106:

| Ch | Book pages | 01.pdf sheets |
|---:|---|---|
| 1 | 1–5 | PDF13–17 |
| 2 | 6–13 | PDF18–25 |
| 3 | 14–17 | PDF26–29 |
| 4 | 18–29 | PDF30–41 |
| 5 | 30–36 | PDF42–48 |
| 6 | 37–45 | PDF49–57 |
| 7 | 46–51 | PDF58–63 |
| 8 | 52–59 | PDF64–71 |
| 9 | 60–62 | PDF72–74 |
| 10 | 63–65 | PDF75–77 |
| 11 | 66–69 | PDF78–81 |
| 12 | 70–76 | PDF82–88 |
| 13 | 77–81 | PDF89–93 |
| 14 | 82–88 | PDF94–100 |
| 15 | 89–91 | PDF101–103 |
| 16 | 92–96 | PDF104–108 |
| 17 | 97–102 | PDF109–114 |
| 18 | 103–106 | PDF115–118 |
| 19 (next) | 107 | PDF119 |

## Schema and order contract

- Chapter: exact roadmap number/title, `pageRange` starts at the roadmap page, nonempty `questions` and `units`.
- Question: sequential `MED-C<N>-<seq>` ID; section/page/format/stem; exactly four unique options; one answer; explanation ending exactly `(Book pX)` matching `page`.
- Units: sequential `MED-U<N>-<n>` IDs; each has a 2–4-line guide; its IDs are rebuilt from exactly one section in original question order; flattened units equal the full chapter sequence.
- Questions are in printed book-page order; all printed pages in every live chapter are represented.
- The source-order inventory is fail-closed: the validator requires a ledger mapping for every question in audited Chapters 1–61, in exact question order and with matching book page.
- Questions are educational book-study material, not a substitute for current clinical guidelines or patient care.

## Build, audit and test workflow

```sh
# Generate chapter artifacts (one generator per chapter).
python3 tools/generate_chNN.py
python3 tools/update_ledger.py     # rebuilds audit/coverage.json from every data/ch*.json

# Fail-closed source gate, standalone-app build, and embedded-array gate.
python3 validate_content.py
python3 -m unittest discover -s tests -v
python3 build_content.py
python3 validate_content.py --embedded
node tests/app_parsers.cjs
```

## Per-chapter units

| Ch | Unit | Pages | Question range | Count |
|---:|---|---|---|---:|
| 1 | Definition & Bristol Chart | 1 | MED-C1-01–MED-C1-10 | 10 |
| 1 | Physiology & Macronutrients | 1 | MED-C1-11–MED-C1-15 | 5 |
| 1 | Frequency Classification & Acute Etiology | 1 | MED-C1-16–MED-C1-21 | 6 |
| 1 | Chronic Diarrhea & Malassimilation | 2 | MED-C1-22–MED-C1-24 | 3 |
| 1 | Osmotic Diarrhea & Steatorrhea | 2 | MED-C1-25–MED-C1-28 | 4 |
| 1 | Steatorrhea Investigations | 2 | MED-C1-29–MED-C1-34 | 6 |
| 1 | Secretory Diarrhea & Stool Osmotic Gap | 3 | MED-C1-35–MED-C1-44 | 10 |
| 1 | Factitious & Anatomical Classification | 4 | MED-C1-45–MED-C1-59 | 15 |
| 1 | Approach to Diarrhea | 5 | MED-C1-60–MED-C1-66 | 7 |
| 2 | Basics of Absorption & Stages | 6 | MED-C2-01–MED-C2-09 | 9 |
| 2 | Anatomy of the Small Intestine | 6 | MED-C2-10–MED-C2-15 | 6 |
| 2 | Histology: Mucosa | 6 | MED-C2-16–MED-C2-29 | 14 |
| 2 | Small Intestine Layers & Peyer's Patches | 7 | MED-C2-30–MED-C2-34 | 5 |
| 2 | Fat Absorption: Luminal Phase | 7 | MED-C2-35–MED-C2-40 | 6 |
| 2 | Bile Acid Physiology | 7 | MED-C2-41–MED-C2-50 | 10 |
| 2 | Defects in Luminal & Mucosal Phase | 8 | MED-C2-51–MED-C2-58 | 8 |
| 2 | Post-Mucosal Phase & Types of Fatty Acids | 8 | MED-C2-59–MED-C2-74 | 16 |
| 2 | Carbohydrate Absorption Mechanism | 9 | MED-C2-75–MED-C2-88 | 14 |
| 2 | Defects in Carbohydrate Absorption | 9–10 | MED-C2-89–MED-C2-93 | 5 |
| 2 | Protein Absorption & Selective Defects | 10 | MED-C2-94–MED-C2-102 | 9 |
| 2 | Lactose Intolerance: Physiology to Pathogenesis | 10–11 | MED-C2-103–MED-C2-116 | 14 |
| 2 | Lactose Intolerance: Presentation & Investigations | 11 | MED-C2-117–MED-C2-125 | 9 |
| 2 | Abetalipoproteinemia | 12 | MED-C2-126–MED-C2-137 | 12 |
| 2 | Intestinal Lymphangiectasia | 13 | MED-C2-138–MED-C2-150 | 13 |
| 3 | Steps for Evaluating Malabsorption | 14 | MED-C3-01–MED-C3-05 | 5 |
| 3 | Clinical Features: Gastrointestinal | 14 | MED-C3-06–MED-C3-15 | 10 |
| 3 | Clinical Features: Musculoskeletal & Cutaneous | 14 | MED-C3-16–MED-C3-23 | 8 |
| 3 | Clinical Features: Miscellaneous & Kidney Stones | 14–15 | MED-C3-24–MED-C3-39 | 16 |
| 3 | Fat Malabsorption Tests | 15 | MED-C3-40–MED-C3-44 | 5 |
| 3 | D-Xylose Test | 15 | MED-C3-45–MED-C3-52 | 8 |
| 3 | False Positives & Hydrogen Breath Tests | 16 | MED-C3-53–MED-C3-63 | 11 |
| 3 | Obsolete Tests & Biopsy Diagnoses | 16 | MED-C3-64–MED-C3-71 | 8 |
| 3 | Schilling Test | 17 | MED-C3-72–MED-C3-80 | 9 |
| 4 | Global Malabsorption: Overview | 18 | MED-C4-01–MED-C4-05 | 5 |
| 4 | Celiac Disease: Features & Iceberg Phenomenon | 18 | MED-C4-06–MED-C4-12 | 7 |
| 4 | Celiac Disease: Types | 18 | MED-C4-13–MED-C4-18 | 6 |
| 4 | Celiac Pathophysiology & Disease Progression | 19 | MED-C4-19–MED-C4-33 | 15 |
| 4 | Celiac Clinical Features | 20 | MED-C4-34–MED-C4-47 | 14 |
| 4 | Celiac Associations | 20 | MED-C4-48–MED-C4-54 | 7 |
| 4 | Celiac Diagnosis: Serology & Biopsy | 21 | MED-C4-55–MED-C4-70 | 16 |
| 4 | Celiac Interpretation, Complications & Treatment | 22 | MED-C4-71–MED-C4-80 | 10 |
| 4 | Whipple's Disease: Presentation | 22 | MED-C4-81–MED-C4-86 | 6 |
| 4 | Whipple's Disease: Clinical Features | 23 | MED-C4-87–MED-C4-105 | 19 |
| 4 | Whipple's Disease: Diagnosis & Treatment | 24 | MED-C4-106–MED-C4-111 | 6 |
| 4 | Tropical Sprue: Pathogenesis | 24 | MED-C4-112–MED-C4-119 | 8 |
| 4 | Tropical Sprue: Features, Investigations & Treatment | 25 | MED-C4-120–MED-C4-131 | 12 |
| 4 | Bile Acid Diarrhea & Fatty Acid Diarrhea | 25–26 | MED-C4-132–MED-C4-143 | 12 |
| 4 | Short Bowel Syndrome: Definition & Etiology | 26 | MED-C4-144–MED-C4-147 | 4 |
| 4 | Short Bowel Syndrome: Clinical Presentation | 27 | MED-C4-148–MED-C4-160 | 13 |
| 4 | Short Bowel Syndrome: Deficiencies & Management | 28 | MED-C4-161–MED-C4-168 | 8 |
| 4 | SIBO: Physiology, Pathology & Etiology | 28 | MED-C4-169–MED-C4-175 | 7 |
| 4 | SIBO: Presentation, Investigations & Management | 29 | MED-C4-176–MED-C4-196 | 21 |
| 5 | Entities of IBD & Microscopic Colitis | 30 | MED-C5-01–MED-C5-09 | 9 |
| 5 | Diversion Colitis & Normal Histology of Colon | 30 | MED-C5-10–MED-C5-13 | 4 |
| 5 | Colonic Mucosa & Definition of Diarrhea | 31 | MED-C5-14–MED-C5-17 | 4 |
| 5 | Epidemiology of UC and Crohn's Disease | 31 | MED-C5-18–MED-C5-30 | 13 |
| 5 | Genetic Syndromes Associated with IBD | 32 | MED-C5-31–MED-C5-41 | 11 |
| 5 | IPEX Syndrome & Early Onset Childhood IBD | 32–33 | MED-C5-42–MED-C5-50 | 9 |
| 5 | Pathogenesis of IBD | 33 | MED-C5-51–MED-C5-58 | 8 |
| 5 | Ulcerative Colitis: Site & Macroscopy | 34 | MED-C5-59–MED-C5-67 | 9 |
| 5 | Ulcerative Colitis: Microscopy | 35 | MED-C5-68–MED-C5-73 | 6 |
| 5 | Crohn's Disease: Site & Macroscopy | 35 | MED-C5-74–MED-C5-86 | 13 |
| 5 | Crohn's Disease: Microscopy | 36 | MED-C5-87–MED-C5-94 | 8 |
| 6 | Ulcerative Colitis: Clinical Features | 37 | MED-C6-01–MED-C6-09 | 9 |
| 6 | Fecal Calprotectin & Endoscopy in UC | 37 | MED-C6-10–MED-C6-16 | 7 |
| 6 | Radiology: Barium Enema in UC | 38 | MED-C6-17–MED-C6-23 | 7 |
| 6 | Crohn's Disease: Clinical Features | 38 | MED-C6-24–MED-C6-32 | 9 |
| 6 | Endoscopy & Cross Sectional Imaging in Crohn's | 39 | MED-C6-33–MED-C6-41 | 9 |
| 6 | Intestinal Tuberculosis versus Crohn's Disease | 40 | MED-C6-42–MED-C6-46 | 5 |
| 6 | Extraintestinal Manifestations of IBD | 40 | MED-C6-47–MED-C6-54 | 8 |
| 6 | Others, Other Investigations & Serology | 41 | MED-C6-55–MED-C6-70 | 16 |
| 6 | Truelove And Witt's Classification | 42 | MED-C6-71–MED-C6-79 | 9 |
| 6 | Medical Management of Ulcerative Colitis | 42 | MED-C6-80–MED-C6-88 | 9 |
| 6 | Sulfasalazine & Surgery in Ulcerative Colitis | 43 | MED-C6-89–MED-C6-96 | 8 |
| 6 | Crohn's Disease: Grading & Medical Management | 43 | MED-C6-97–MED-C6-103 | 7 |
| 6 | Crohn's Disease: Management by Severity | 44 | MED-C6-104–MED-C6-116 | 13 |
| 6 | Malignancy in IBD | 45 | MED-C6-117–MED-C6-128 | 12 |
| 7 | Definitions & Site Patterns | 46 | MED-C7-01–MED-C7-17 | 17 |
| 7 | Small- and Large-Bowel Organisms | 47 | MED-C7-18–MED-C7-26 | 9 |
| 7 | Preformed-Toxin Food Poisoning | 47–48 | MED-C7-27–MED-C7-37 | 11 |
| 7 | Vibrio, ETEC & Secretory Diarrhoea | 48 | MED-C7-38–MED-C7-49 | 12 |
| 7 | HUS and Shigella | 49 | MED-C7-50–MED-C7-70 | 21 |
| 7 | Salmonella and Campylobacter | 50 | MED-C7-71–MED-C7-86 | 16 |
| 7 | C. difficile Enterocolitis | 50–51 | MED-C7-87–MED-C7-111 | 25 |
| 8 | Regions, Glands & Cells | 52 | MED-C8-01–MED-C8-19 | 19 |
| 8 | Mucosal Defence and Wall | 53 | MED-C8-20–MED-C8-39 | 20 |
| 8 | Acid Regulation & Acute Gastritis | 54 | MED-C8-40–MED-C8-58 | 19 |
| 8 | Chronic & Hypertrophic Gastritis | 55–56 | MED-C8-59–MED-C8-86 | 28 |
| 8 | H. pylori Biology & Virulence | 56–57 | MED-C8-87–MED-C8-111 | 25 |
| 8 | H. pylori, Dyspepsia & Testing | 57–58 | MED-C8-112–MED-C8-133 | 22 |
| 8 | Treatment & Test of Cure | 58–59 | MED-C8-134–MED-C8-150 | 17 |
| 9 | Types and Comparisons | 60 | MED-C9-01–MED-C9-23 | 23 |
| 9 | Triangle and Gastrin Effects | 60 | MED-C9-24–MED-C9-32 | 9 |
| 9 | Clinical Features | 61 | MED-C9-33–MED-C9-42 | 10 |
| 9 | Tests and Imaging | 61–62 | MED-C9-43–MED-C9-58 | 16 |
| 9 | Treatment and Surgical Anatomy | 62 | MED-C9-59–MED-C9-67 | 9 |
| 10 | Definition & Associations | 63 | MED-C10-01–MED-C10-04 | 4 |
| 10 | Clinical Pattern, Rome IV & Red Flags | 63 | MED-C10-05–MED-C10-26 | 22 |
| 10 | Pathophysiology | 64 | MED-C10-27–MED-C10-35 | 9 |
| 10 | Lifestyle & FODMAPs | 64 | MED-C10-36–MED-C10-43 | 8 |
| 10 | Type-Based Medical Management | 65 | MED-C10-44–MED-C10-58 | 15 |
| 11 | WHO Thresholds & Haematopoiesis | 66 | MED-C11-01–MED-C11-17 | 17 |
| 11 | Erythroid Maturation | 67 | MED-C11-18–MED-C11-31 | 14 |
| 11 | Reticulocytes and Indices | 68 | MED-C11-32–MED-C11-46 | 15 |
| 11 | Approach & Marrow Notes | 69 | MED-C11-47–MED-C11-63 | 17 |
| 12 | Body Iron & Daily Needs | 70 | MED-C12-01–MED-C12-19 | 19 |
| 12 | Dietary Iron & Absorption | 71 | MED-C12-20–MED-C12-35 | 16 |
| 12 | Export, Transport & Marrow Uptake | 71–72 | MED-C12-36–MED-C12-50 | 15 |
| 12 | Serum Iron Indices | 72 | MED-C12-51–MED-C12-65 | 15 |
| 12 | Stages of Iron Deficiency | 73 | MED-C12-66–MED-C12-91 | 26 |
| 12 | Causes & Iron Deficit | 74 | MED-C12-92–MED-C12-93 | 2 |
| 12 | Clinical Features | 74 | MED-C12-94–MED-C12-103 | 10 |
| 12 | IDA Investigations | 75 | MED-C12-104–MED-C12-119 | 16 |
| 12 | Marrow, Treatment & Follow-up | 76 | MED-C12-120–MED-C12-134 | 15 |
| 13 | Blood Picture & ACD Pathophysiology | 77 | MED-C13-01–MED-C13-18 | 18 |
| 13 | ACD Indices & Sideroblastic Etiology | 78 | MED-C13-19–MED-C13-42 | 24 |
| 13 | Sideroblastic Pathogenesis & Thalassemia | 79 | MED-C13-43–MED-C13-59 | 17 |
| 13 | Thalassemia Indices & Inherited IDA | 80 | MED-C13-60–MED-C13-77 | 18 |
| 13 | Diagnostic Protocol | 81 | MED-C13-78–MED-C13-83 | 6 |
| 14 | Types, Causes & B12 vs Folate Stores | 82 | MED-C14-01–MED-C14-22 | 22 |
| 14 | Vitamin B12 Sources & Absorption | 83 | MED-C14-23–MED-C14-35 | 13 |
| 14 | B12 Deficiency, Transcobalamins & Roles | 84 | MED-C14-36–MED-C14-54 | 19 |
| 14 | Folate Metabolism, Trap & Causes | 85 | MED-C14-55–MED-C14-70 | 16 |
| 14 | Diagnosis of Megaloblastic Anemia | 86–87 | MED-C14-71–MED-C14-85 | 15 |
| 14 | Pernicious Anemia: Pathogenesis & Signs | 87 | MED-C14-86–MED-C14-93 | 8 |
| 14 | Pernicious Anemia: CNS, Workup & Rx | 88 | MED-C14-94–MED-C14-107 | 14 |
| 15 | Classification of Hemolytic Anemia | 89 | MED-C15-01–MED-C15-15 | 15 |
| 15 | Abbreviations & Intravascular Hemolysis | 90 | MED-C15-16–MED-C15-28 | 13 |
| 15 | Extravascular Hemolysis & General Rules | 91 | MED-C15-29–MED-C15-44 | 16 |
| 16 | Immune Classification & Coombs Test | 92 | MED-C16-01–MED-C16-13 | 13 |
| 16 | DAT Subtyping & Warm vs Cold Etiology | 93 | MED-C16-14–MED-C16-31 | 18 |
| 16 | Warm vs Cold: Pathogenesis & Smear | 94 | MED-C16-32–MED-C16-39 | 8 |
| 16 | AIHA Treatment, Evans & Spherocytes | 95 | MED-C16-40–MED-C16-50 | 11 |
| 16 | PCH & Drug-Induced Hemolysis | 96 | MED-C16-51–MED-C16-62 | 12 |
| 17 | Overview & PNH Physiology | 97 | MED-C17-01–MED-C17-13 | 13 |
| 17 | PNH: Pathogenesis & Clinical Features | 98 | MED-C17-14–MED-C17-25 | 12 |
| 17 | PNH: Investigations & Treatment | 99 | MED-C17-26–MED-C17-33 | 8 |
| 17 | Fragmentation: MAHA, TMA & HUS vs TTP | 100 | MED-C17-34–MED-C17-45 | 12 |
| 17 | HUS: Childhood (D⁺) vs Adult (D⁻) | 101 | MED-C17-46–MED-C17-60 | 15 |
| 17 | TTP & Types of Fragmentation Hemolysis | 102 | MED-C17-61–MED-C17-70 | 10 |
| 18 | Inherited Hemolytic Anemias & Hereditary Spherocytosis: Genetics and RBC Membrane Structure | 103 | MED-C18-01–MED-C18-14 | 14 |
| 18 | Hereditary Spherocytosis: Pathogenesis, Clinical Features & Investigations | 104 | MED-C18-15–MED-C18-25 | 11 |
| 18 | Hereditary Spherocytosis Treatment & G6PD Deficiency: Genetics, HMP Shunt and Triggers | 105 | MED-C18-26–MED-C18-37 | 12 |
| 18 | G6PD Deficiency: Peripheral Smear, Diagnosis, Treatment & Anemia of Blood Loss | 106 | MED-C18-38–MED-C18-49 | 12 |
| 19 | Overview: CMP Physiology, MPN Pathology and the Printed MPN List with Mutations | 107 | MED-C19-01–MED-C19-08 | 8 |
| 19 | Clinical Features of MPN, Polycythemia Thresholds and Relative Polycythemia (Gaisböck's) | 108 | MED-C19-09–MED-C19-19 | 11 |
| 19 | Absolute Polycythemia: Types, EPO/TC/PLC Table and Secondary Etiologies | 109 | MED-C19-20–MED-C19-29 | 10 |
| 19 | Polycythemia Rubra Vera: JAK2 Mutations and Clinical Features | 110 | MED-C19-30–MED-C19-40 | 11 |
| 19 | PCRV Investigations, Diagnostic Criteria and Management; Primary Myelofibrosis Etiology | 111 | MED-C19-41–MED-C19-50 | 10 |
| 19 | Primary Myelofibrosis: Pathogenesis and Clinical Features | 112 | MED-C19-51–MED-C19-60 | 10 |
| 19 | Primary Myelofibrosis: Investigations and Management | 113 | MED-C19-61–MED-C19-69 | 9 |
| 19 | Essential Thrombocytosis: Etiology, Clinical Features, Investigations and Complications | 114 | MED-C19-70–MED-C19-77 | 8 |
| 19 | Essential Thrombocytosis: Evaluation and Risk-Stratified Management | 115 | MED-C19-78–MED-C19-83 | 6 |
| 20 | CML Pathophysiology: Myelopoiesis, BCR-ABL Molecular Genetics & the Philadelphia Chromosome | 116 | MED-C20-01–MED-C20-09 | 9 |
| 20 | CML Versus AML, TKI Note, Risk Factors & Clinical Features | 117 | MED-C20-10–MED-C20-23 | 14 |
| 20 | CML Investigations: Peripheral Smear, LAP, Tryptase, Cytogenetics & Bone Marrow Study | 118 | MED-C20-24–MED-C20-33 | 10 |
| 20 | CML Bone Marrow Picture, Accelerated Phase (Obsolete) & Prognostic Scales | 119 | MED-C20-34–MED-C20-41 | 8 |
| 20 | CML Management: Hydroxyurea, the TKI Table, Response Milestones & Monitoring | 120 | MED-C20-42–MED-C20-53 | 12 |
| 21 | Approach to Pancytopenia: Marrow Cellularity Flowchart & Aplastic Anemia Overview | 121 | MED-C21-01–MED-C21-12 | 12 |
| 21 | Inherited vs Acquired Aplastic Anemia: Fanconi, Dyskeratosis Congenita, Shwachman-Diamond | 122 | MED-C21-13–MED-C21-21 | 9 |
| 21 | Drugs Causing Aplastic Anemia, Presentation, Severity Criteria & Treatment | 123 | MED-C21-22–MED-C21-32 | 11 |
| 21 | Pure Red Cell Aplasia & MDS Overview: Global Versus India Presentation | 124 | MED-C21-33–MED-C21-42 | 10 |
| 21 | MDS Blood Parameters, Prognostic Scoring & Treatment Flowchart | 125 | MED-C21-43–MED-C21-52 | 10 |

## Full roadmap

| Ch | Title | Starts | State |
|---:|---|---:|---|
| 1 | Diarrhea | 1 | **Live** |
| 2 | Physiology of GIT Absorption and Selective Malabsorption | 6 | **Live** |
| 3 | Clinical Features And Tests For Malabsorption | 14 | **Live** |
| 4 | Global Malabsorption | 18 | **Live** |
| 5 | Inflammatory Bowel Disease : Part 1 | 30 | **Live** |
| 6 | Inflammatory Bowel Disease : Part 2 | 37 | **Live** |
| 7 | Infectious Diarrhoea | 46 | **Live** |
| 8 | Stomach | 52 | **Live** |
| 9 | Gastrinoma | 60 | **Live** |
| 10 | Irritable Bowel Syndrome | 63 | **Live** |
| 11 | Clinical Approach to Anemia | 66 | **Live** |
| 12 | Iron Metabolism | 70 | **Live** |
| 13 | Approach To Microcytic Hypochromic Anemia | 77 | **Live** |
| 14 | Macrocytic Anemia | 82 | **Live** |
| 15 | Approach to Hemolysis | 89 | **Live** |
| 16 | Immune Mediated Hemolytic Anemia | 92 | **Live** |
| 17 | Non-Immune Mediated Hemolytic Anemia | 97 | **Live** |
| 18 | Hemolytic Anemia : Miscellaneous | 103 | **Live** |
| 19 | Myeloproliferative Neoplasms : Part 1 | 107 | **Live** |
| 20 | Myeloproliferative Neoplasms : Part 2 | 116 | **Live** |
| 21 | Bone Marrow Failure Syndromes | 121 | **Live** |
| 22 | Acute Leukemia | 126 | Soon |
| 23 | Acute Myeloid Leukemia V/S Acute Lymphoblastic Leukemia | 136 | Soon |
| 24 | World of Lymphomas | 140 | Soon |
| 25 | Chronic Lymphocytic Leukemia | 142 | Soon |
| 26 | Non-Hodgkin's Lymphoma | 146 | Soon |
| 27 | Hodgkin's Disease | 153 | Soon |
| 28 | Plasma Cell Disorders | 159 | Soon |
| 29 | Platelets - Basics | 169 | Soon |
| 30 | Approach to Bleeding Disorders | 173 | Soon |
| 31 | Clinical Anatomy of Lungs | 185 | Soon |
| 32 | Clinical Physiology of Lungs | 193 | Soon |
| 33 | Pulmonary Function Tests | 197 | Soon |
| 34 | Venous Thromboembolism | 206 | Soon |
| 35 | Pulmonary Hypertension | 213 | Soon |
| 36 | Bronchiectasis | 218 | Soon |
| 37 | Occupational Lung Diseases | 223 | Soon |
| 38 | Respiratory Failure and Acute Respiratory Distress Syndrome | 230 | Soon |
| 39 | Interstitial Lung Disease | 236 | Soon |
| 40 | Bronchial Asthma | 243 | Soon |
| 41 | Pulmonary Eosinophilia | 249 | Soon |
| 42 | Allergic Bronchopulmonary Aspergillosis | 253 | Soon |
| 43 | Hypersensitivity Pneumonitis | 257 | Soon |
| 44 | Pleural Effusion | 260 | Soon |
| 45 | Obstructive Sleep Apnea Syndrome | 264 | Soon |
| 46 | Chronic Obstructive Airway Disease | 267 | Soon |
| 47 | Community Acquired Pneumonia | 274 | Soon |
| 48 | Atypical Pneumonia and Pneumonia in Immunocompromised | 286 | Soon |
| 49 | Cardiac Cycle With Heart Sounds | 296 | Soon |
| 50 | Added Heart Sounds | 303 | Soon |
| 51 | Aortic Stenosis | 307 | Soon |
| 52 | Aortic Regurgitation | 313 | Soon |
| 53 | Heart Failure | 318 | Soon |
| 54 | Acute Decompensated Heart Failure | 326 | Soon |
| 55 | Cardiomyopathy : Part 1 | 331 | Soon |
| 56 | Cardiomyopathy : Part 2 | 336 | Soon |
| 57 | Mitral Regurgitation | 346 | Soon |
| 58 | Mitral Stenosis | 352 | Soon |
| 59 | CCP, CT, RCM and Acute Pericarditis | 358 | Soon |
| 60 | Pulse | 364 | Soon |
| 61 | Jugular Venous Pulse (JVP) | 370 | Soon |


## Per-chapter pipeline

1. Render source PDF pages (the scan has no text layer) and read them line-to-line; crop and re-read at higher zoom wherever a digit, threshold or table cell is ambiguous.
2. Inventory every line, table cell, diagram label, flowchart arm, value and note in strict book order into `audit/coverage.json`.
3. Generate `data/chNN.json` with strict `MED-C<N>-<seq>` ordering, `page` nondecreasing, `exp` citing `(Book pX)`, units slicing by `sec`, guides 2–4 lines.
4. Run `validate_content.py`, `tests`, and `build_content.py` to embed; verify live flags and embedded arrays.
5. Commit, push, PR to `main` — live link updates via GitHub Pages.

*Next up:* **Chapter 22 — Acute Leukemia (p126)** — render `uploads/02.pdf` PDF9 onward, audit in strict book order, and continue the same pipeline.
