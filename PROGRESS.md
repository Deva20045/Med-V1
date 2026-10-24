# PULSE Medicine Vol 1 — Progress

Updated **2026-10-24** (Chapters 51–56 released and deployed; source review now reaches Book p345). Standalone offline quiz based on *PULSE Medicine Vol 1*, printed Book p1–375 (Marrow Edition 8).

- Repository: `Deva20045/Med-V1`
- Session branch: `arena/828a204e-med-v1` (published from this release's session)
- Published URL: https://deva20045.github.io/Med-V1/
- Editable source of truth: `data/chNN.json`; generated offline deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- **Build status: 56 live chapters / 61 · 3,690 questions / 384 units.** Chapters 1–56 are embedded by `build_content.py`; source coverage is complete through Book p345.

## This release — Chapters 51 to 56 (Book p307–345)

Chapters 51–56 of *PULSE Medicine Vol 1* are complete in strict printed order (**Ch 51 Aortic Stenosis, Ch 52 Aortic Regurgitation, Ch 53 Heart Failure, Ch 54 Acute Decompensated Heart Failure, Ch 55 Cardiomyopathy : Part 1, Ch 56 Cardiomyopathy : Part 2**). All 39 scanned sheets in `uploads/03.pdf` PDF60–98 (Book p307–345) were rendered, read line-to-line and re-checked for thresholds and table cells. Every anatomy label, classification tree, pressure-gradient arrow, risk-factor list, comparison table, dynamic-auscultation column, figure caption, dose and eponym was inventoried into 354 new questions in exact page order.

| Chapters | Book pages | Source sheets | Questions | Units |
|---|---:|---|---:|---:|
| 1–50 | 1–306 | `01.pdf` PDF13–129; `02.pdf` PDF1–130; `03.pdf` PDF1–59 | 3,336 | 345 |
| 51 | 307–312 | `03.pdf` PDF60–65 | 53 | 6 |
| 52 | 313–317 | `03.pdf` PDF66–70 | 48 | 5 |
| 53 | 318–325 | `03.pdf` PDF71–78 | 66 | 8 |
| 54 | 326–330 | `03.pdf` PDF79–83 | 46 | 5 |
| 55 | 331–335 | `03.pdf` PDF84–88 | 48 | 5 |
| 56 | 336–345 | `03.pdf` PDF89–98 | 93 | 10 |
| **Cumulative** | **345** |  | **3,690** | **384** |

The 354 new questions deliberately move beyond plain recall: 114 recall, 76 match, 34 fill-up, 33 scenario, 32 numeric, 25 management, 22 odd-one-out and 18 true/false (**240/354 = 68% non-recall**). Answer positions rotate deterministically; distractors are built from neighbouring printed lines, reversed arrows and adjacent thresholds rather than generic wrong words; all 76 `match` items are true bijections; every unit has a 2–4-line guide. Cumulative format distribution through Chapter 56: 1,990 recall, 468 match, 371 numeric, 263 fill-up, 203 scenario, 147 true/false, 147 odd-one-out and 101 management. Printed-verbatim quirks from p307–345 (the p318 `American College of Clinical Cardiology` expansion, the p325 ARNI action-arrow wording, the p327 `>30 bpm` tachypnea threshold, the p328 Kerley-line LAP bands, the p330 `diagnostic value in renal failure` fragment, the p334 `Chaga's disease` spelling, and the p343 `Ascaris lumbricoides` infection note) are preserved as source text and itemised in [audit/known-source-caveats.md](audit/known-source-caveats.md).

### Chapter 51 — Aortic Stenosis (Book p307–312; 53 questions / 6 units)

Begins with the three cusps, three commissures and one annulus, the congenital 4/2/1-cusp sequence, the printed 75% versus 20–25% BAV split, the 3–4 cm² valve area and the five coronary/commissural labels; normal systole is fixed at LVP 120 mmHg and aortic pressure 120 mmHg with no gradient. The pathogenesis chain runs from valve substrate through inflammation, lipoprotein, RAAS, osteoblast change and hydroxyapatite to sclerosis, then adds a transvalvular gradient before symptoms. Rheumatic combinations, the 30%/80% demographics, mandatory coronary angiogram and the three valve-specimen captions are followed by the aetiology ranks. BAV genetics adds NOTCH-1, eNOS, M > F, autosomal dominance, aortopathy and mandatory CT aortogram; location and severity trees keep HCM, Williams syndrome, concentric-LVH compensation, sudden death, AVR and the 40/4/1 rule. The ASD 5/3/1 clock, three angina mechanisms, fixed-output syncope, dyspnea pressure chain, AF/HTN/LVF notes, Heyde syndrome and acquired von Willebrand disease precede pulse, BP, JVP and apex findings. Heart sounds, the mixed-frequency murmur with carotid/Gallavardin components, Sokolov–Lyon >35 mm, the dilated aortic arch and definitive ECHO close with bioprosthetic AVR, all five indications, dobutamine stress testing, disadvantages and balloon-/self-expanding TAVR.

### Chapter 52 — Aortic Regurgitation (Book p313–317; 48 questions / 5 units)

Splits acute from chronic disease, then separates leaflet causes (rheumatic MS+AR/AR+AS, quadricuspid valves, Takayasu, ankylosing spondylitis) from root causes (syphilis m/c, Marfan, Ehlers–Danlos, Takayasu, Behcet, Cogan and IgG4-related disease) with every expansion. The diastolic gradient (LV 10 / aorta 80 mmHg), eccentric-hypertrophy compensation, EF equation and normal LVEDP are followed by decompensation with ESV and S3, the preload/afterload/DBP/pulse-pressure table, Hill and Lincoln signs, nocturnal angina, strict BP control and exercise benefit. The full AS-versus-AR table, high-volume and water-hammer definitions, collapsing versus pseudocollapsing pulses, aorta–pulmonary window/PDA note, bisferiens P/T rules, BP/apex/heart-sound table and the high-pitched early diastolic decrescendo murmur with Cole–Cecil and Key–Hodgkin radiations are all tested. The tracing, ESM and Austin Flint mechanism introduce all **16** peripheral signs in printed order, from Corrigan to Sherman, including Duroziez, Traube, Mayne >15 mmHg and Sherman age >75 years. Management closes with symptomatic AVR, the 55–50 rule, acute dissection/IE/sinus-rupture/trauma causes, LAP >25 mmHg, short low-pitched EDM with soft S1, shock/hypotension and immediate surgery bridged by NTG, nitroprusside and inotropes.

### Chapter 53 — Heart Failure (Book p318–325; 66 questions / 8 units)

Keeps the full ACC/AHA 2017 definition and abbreviations, all four EF types, the NYHA symptom exclusions, four class criteria and three mortality cells. Stages A–D are tested with every risk factor and example, followed by the HFrEF/NYHA 2–3/stage-C common presentation and all ten low-output systolic signs including TNF-α cachexia. Diastolic failure reproduces both converging arms, the LVEDP→LAP→PCVP→exudation chain, dyspnea/crackles/right effusion, immediate orthopnea versus 2–3-hour PND and the full supine fluid-shift mechanism. Right-heart failure, AJR site, four causes and both Framingham columns are covered cell by cell. HFpEF/HFNEF follows microvascular inflammation to longitudinal-fibre dysfunction, LVH, 25→40% atrial contribution, AF, edema, the HF-versus-COPD table and bendopnea/trepopnea/platypnea. The ESC definition, HFNEF presentation, ten ADHF risk factors, HFrEF remodelling chain and sympathetic activation lead into RAAS/ADH/natriuretic compensation, sustained-activation decompensation, nesiritide status, beta-blocker doses, ACE/ARB class effect, ARNI components and printed action arrows, hierarchy, euvolemia-first rule, Fantastic Four, ivabradine at HR >70/min and wide-versus-normal-QRS refractory branches.

### Chapter 54 — Acute Decompensated Heart Failure (Book p326–330; 46 questions / 5 units)

Opens with the 80/20 prior-versus-de-novo split, all eight risk factors in order and the four ADHF classes. Mild-to-moderate disease retains its 70% share, HFrEF substrate, LRTI trigger, progressive dyspnea, JVP/tender-liver/oedema cluster, absence of edema/shock and S3/cardiomegaly/annular-MR findings. Hypertensive ADHF is separated as female-predominant HFpEF with IV diuretics and oral antihypertensives, before acute pulmonary edema's 60–90-minute onset, orthostatic gasping, diaphoresis, tachypnea >30 bpm, hypertensive crisis, diffuse crepts and frothy sputum ± hemoptysis. The five differentials include acute AR/MR sub-branches and bilateral renal-artery stenosis with flash edema; emergency imaging covers bat-wing cardiopulmonary edema, earliest cephalisation and the complete Kerley A/B/C table with 12–19, 20–24 and >25 mmHg bands. The warm/dry, warm/wet, cold/dry and cold/wet perfusion grid is matched to PCWP, CI, stable/hypovolemic branches, nesiritide/vasodilators and inotropes. The treatment bundle preserves furosemide 360 mg as 100+100+100+60, 45°, NRBM/NIV, morphine 4 mg IV and NTG 5 µg/min; shock adds SBP <90 mmHg, lactate, early ECHO, dobutamine/milrinone/IABP/ECMO and HFpEF vasopressors. Final notes cover dialysis/SCUF, BNP/NT-proBNP >900 pg/mL, obesity and renal-failure caveats, and nitroprusside > NTG in acute AR/MR.

### Chapter 55 — Cardiomyopathy : Part 1 (Book p331–335; 48 questions / 5 units)

Defines cardiomyopathy by its CAD/HTN/valvular/congenital exclusions and inventories all seven named types. DCMP presentation is worked across systolic/diastolic symptoms, signs and auscultation, male predominance, MRI's four gold-standard uses and the dilatation→diastolic→LV→RV failure sequence with global hypokinesia and 25% of HF cases. Etiology covers the 30% genetic fraction and all three inheritance/protein rows, penetrance and expression, peripartum/alcohol/drug prognosis, thiamine/selenium/carnitine with Keshan disease, autoimmune, endocrine and inflammatory branches, four complications and the intraventricular-thrombus POCUS figure. Investigations retain limb-versus-chest voltage, sinus tachycardia, poor R progression, the large roomy thin-walled LV, MRI/angiogram for CAD after age >30, the angina-normal-coronaries triad and transplant. Peripartum CMP is tested from best prognosis/high recurrence through age >30, hypertension, third-trimester/postpartum timing, SFLT1, exertional/breastfeeding dyspnea, diaphoresis, avoidance of pregnancy and 3–4-month resolution. Drug-induced disease names every anthracycline, targeted drug, metal, hydrocarbon and cocaine, plus R-CHOP/ABVD/7+3 uses; alcohol disease follows ACE polymorphism → acetaldehyde, holiday-heart AF, stroke/ACS, deficiency aggravators and 3–6-month reversibility. Myocarditis finishes with focal/diffuse and acute/chronic timing, HHV-6/T. cruzi, cytokine release, subclinical majority, four clinical branches, ECG, troponin I, Dallas criteria, MRI peripheral enhancement and restrictive steroid use.

### Chapter 56 — Cardiomyopathy : Part 2 (Book p336–345; 93 questions / 10 units)

HCM opens with its three superlatives, mutation rank, M = F incidence, female prognosis, 95–99% asymptomatic fraction, four paediatric mimics with Pompe details, three complications, the ≥15 mm definition and the athlete-heart four-row table. Asymmetric hypertrophy, inappropriate afterload status and the three LVOT thirds lead into Yamaguchi disease and the complete diastolic chain with 25→40% atrial contribution, AF, PCWP, edema and tachycardia-related dyspnea. The SAM cascade is followed stepwise to a 30 mmHg subaortic gradient, PSM/ESM branches, symptom severity and the valvular/subvalvular/supravalvular note. Clinical HCM covers all symptom arms, normal BP/JVP, jerky and bisferiens pulses, double/triple apical impulses, S1–S4, ESM/PSM, the LV–aorta gradient principle, preload/afterload/inotropy chains, hydration, all aggravators and manoeuvres, the Valsalva MVP/HCM exceptions and ECG. ECHO ≥15 mm, dagger Doppler, beta blocker/CCB/disopyramide, propranolol 2 mg/kg max 480 mg, four beta-blocker advantages, CCB indications and six ICD indications precede refractory gradient >50 mmHg, myomectomy and alcohol ablation. RCM is covered through its nested physiology, stiff R>L ventricles, congestion, almost-normal systole, massive atria, RVEDP>LVEDP and exercise intolerance. All infiltrative/non-infiltrative causes, the Fabry figure, mutation recap and amyloid classification/features follow. Amyloid investigations, ARVD, tachycardia-induced CMP and the five Takotsubo synonyms/presentation close into ECG, troponin/NT-proBNP, angiogram, non-territorial RWMA, excellent long-term prognosis, MI-like complications and carvedilol.

## Previous release — Chapters 45 to 50 (Book p264–306)

Chapters 45–50 of *PULSE Medicine Vol 1* are complete in strict source order (**Ch 45 Obstructive Sleep Apnea Syndrome, Ch 46 Chronic Obstructive Airway Disease, Ch 47 Community Acquired Pneumonia, Ch 48 Atypical Pneumonia and Pneumonia in Immunocompromised, Ch 49 Cardiac Cycle With Heart Sounds, Ch 50 Added Heart Sounds**). Every printed line on Book p264–306 was inventoried from the `uploads/03.pdf` scans and converted into questions in exact page order, including classification trees, comparison tables, flowchart arms, pressure–volume and heart-sound timing charts, figure captions, printed thresholds and source slips.

| Chapters | Book pages | Source sheets | Questions | Units |
|---|---:|---|---:|---:|
| 1–44 | 1–263 | `01.pdf` PDF13–129; `02.pdf` PDF1–130; `03.pdf` PDF1–16 | 2,938 | 302 |
| 45 | 264–266 | `03.pdf` PDF17–19 | 30 | 3 |
| 46 | 267–273 | `03.pdf` PDF20–26 | 74 | 7 |
| 47 | 274–285 | `03.pdf` PDF27–38 | 99 | 12 |
| 48 | 286–295 | `03.pdf` PDF39–48 | 90 | 10 |
| 49 | 296–302 | `03.pdf` PDF49–55 | 61 | 7 |
| 50 | 303–306 | `03.pdf` PDF56–59 | 44 | 4 |
| **Cumulative** | **306** |  | **3,336** | **345** |

The 398 new questions keep the interactive weighting the owner asked for: 167 recall, 78 match, 52 fill-up, 41 scenario, 22 numeric, 22 odd-one-out, 16 true/false (**231/398 = 58% non-recall**) across all eight formats, with four-option sets whose distractors are built from neighbouring printed lines rather than invented plausibilities. Cumulative format distribution through Chapter 50: 1,876 recall, 392 match, 339 numeric, 229 fill-up, 170 scenario, 129 true/false, 125 odd-one-out and 76 management. The ten new `match` items were checked for a real bijection (no repeated right-hand label), and every unit guide was checked against the 2–4-line gate. Source slips and printed-verbatim quirks from p264–306 (the p265 `eps-worth` hyphenation, the p267 lower-case `global initiative for COPD`, the p268 40–45/50–75 age pair, the p269 blank irregular-emphysema cell, the p282 4 mm pneumatocele/bulla pair, the p284 `synpneumonic` spelling, the p292 monad sign, the p295 `Gram positive filamentous fungi` for Nocardia, the p300 downward arrow beside the 80 ms pulmonary hangout, and the p305 S2–OS ladder printed in `mmHg`) are preserved verbatim and itemised in [audit/known-source-caveats.md](audit/known-source-caveats.md).

### Chapter 45 — Obstructive Sleep Apnea Syndrome (Book p264–266; 30 questions / 3 units)

Opens with the obstructive-event definitions restricted to REM sleep — apnea as cessation of breathing for `>10 s` and hypopnea as `>10 s` of reduced breathing with an amplitude fall `>50%` **or** an O₂ desaturation `≥4%` — then defines the apnea-hypopnea index as total events divided by total sleep time and matches its four printed bands (`<5` normal, `5–15` mild, `15–30` moderate, `>30` severe), with the brace that leaves only normal and mild/moderate to lifestyle modification and sends severe disease to CPAP. The obesity hypoventilation note and the eight risk factors follow (male sex printed `M : F = 3 : 1`, obesity, central fat, age 50–60, postmenopausal state, alcohol, sedatives, smoking). Clinical features are tested in printed order: snoring as the cardinal symptom with its waxing-and-waning pattern and long periods of silence, worse supine; the night-time pair nocturia and sudden waking; the day-time block from morning headache/confusion (non-restorative sleep) and cognitive defects (poor concentration, personality and mood changes, depression and anxiety) through sexual dysfunction to dry throat, day-time sleepiness and GERD. The boxed instruction to suspect OSAS in unexplained pulmonary hypertension and unexplained polycythemia is tested with both "unexplained" qualifiers intact, and a scenario pairs the two. Complications are followed through the vagal sudden-death chain (vagal stimulation → bradycardia + hypoxia → premature beat, asystole, VT, cardiac arrest), the `due to HTN` brace over stroke and congestive cardiac failure against the unbracketed metabolic syndrome, and the printed dismissal of the Epworth questionnaire as obsolete, before the two captioned polysomnography traces (central apnea without effort against obstructive apnea with persistent effort) and the only treatment line on p266, severe OSAS managed with CPAP in its nasal and full-face masks.

### Chapter 46 — Chronic Obstructive Airway Disease (Book p267–273; 74 questions / 7 units)

Starts with the GOLD 2023 definition (its acronym printed as lower-case `global initiative for COPD`), the two classification trees based on clinical presentation and pathology (small airway defined by a printed diameter) and the diagnosis rule of symptoms plus spirometric confirmation, then the eight risk factors and four clinical features with the persistent progressive dyspnea and its printed aggravator. The chronic-bronchitis-versus-emphysema table is worked cell by cell: definition (3 months for 2 consecutive years), pathology (small airway disease against abnormal permanent enlargement with wall destruction), the printed age bands 40–45 against 50–75, the blue-bloater chain with its RVH/JVP/oedema finish, the pink-puffer cluster, chest X-ray and PFT columns, plus the lobule and respiratory-unit notes and centriacinar disease. Panacinar, paraseptal and the blank irregular-emphysema cell follow, then the protease-antiprotease theory with α1-antitrypsin (SERPINA1), the PiMM/PiZZ allele table and the spontaneous-pneumothorax list. Large-airway disease is contrasted with asthma (the chronic-bronchitis note table's bronchospasm, epithelial necrosis and squamous metaplasia columns) and small-airway disease with emphysema, closing on the driving-pressure formula `DP = IPP + ERP` and the `↑ IPP, ↓ ERP → DP < AP` rule of forceful exhalation. Physiology moves to the alveolar DLCO split, the hypoxia-to-cor-pulmonale chain, the emphysema PFT with bronchodilator reversibility at `FEV1/FVC <0.7`, the four GOLD grades and the ABE tool (group E defined by exacerbation history). Management covers inhaled-corticosteroid indications (`≥300 cells/μL`) against contraindications (`<100 cells/μL`), group E and the A/B groups, LABA (formoterol, indacaterol) and LAMA (tiotropium) examples, the 2019 note to reduce steroid use, and the follow-up flowchart ending in roflumilast for chronic bronchitis with FEV₁ <50% and azithromycin for a smoking/emphysema history. Long-term oxygen (15–16 hours/day, its two indications), LVRS with its `<20%` FEV₁ contraindication and the BODE index close the chapter alongside the `<14 days` exacerbation definition, its three causes, and the printed treatment bundle (nebulisation, IV hydrocortisone 100 mg, antibiotics for 5–7 days, oral steroids for 7 days, magnesium sulphate).

### Chapter 47 — Community Acquired Pneumonia (Book p274–285; 99 questions / 12 units)

Begins with pneumonia as acute infection of lung parenchyma *without necrosis*, its five parenchymal sites, the necrosis note that routes to necrotising pneumonia and abscess, the six-step pathogenesis with the cytokine split (IL-1/IL-6/TNFα for fever, IL-8 for neutrophil recruitment) and the three protective mechanisms before the aspiration route. HAP and VAP are separated from CAP by their printed 48-hour rules, then the anatomical and organism classifications, the four-part CAP criteria, five cardinal features, the auscultatory `Classical signs` and the radiological criterion. The organism tables are transcribed as drawn: lobar versus interstitial columns, the `MRSA is not common in India` note, the seven-row typical-versus-atypical comparison (site, onset, pathology, course, fever, sputum, laboratory detection and radiology), the outpatient-to-ICU organism shift and MRSA/MDR risk within three months. Pneumococcal detail follows — morphology, culture and haemolysis chart, the pneumococcus-versus-viridans discrimination, the four toxins, the Quellung reaction, type-3 invasiveness and the CAP risk and poor-prognosis notes. Clinical and radiographic sections cover type-2 alveolar binding, the cardinal and abdominal symptoms of lobar pneumonia, the older-patient caveat (confusion as the only symptom, classical signs absent), resolution timing and the four-column chest-film table, with the air bronchogram, silhouette, golden-S and mediastinal-shift captions on p281–282 and the mycoplasma-versus-Legionella films, fibrocalcific scar, necrotising Klebsiella and the pneumatocele cascade with its 4 mm wall rule. Severity is CURB-65 (with the printed BUN ≈21 mg/dL and blood urea ≈42 mg/dL equivalents), the BTS outpatient algorithm and the non-severe/severe inpatient antibiotic table; management adds MRSA cover, the 48–72-hour response rule, empyema, lung abscess and ARDS with the empyema-versus-abscess table and the lung-cavity definition. The chapter closes on the bulla/cyst/thin-walled-cavity captions, the four thick-walled causes and the seven-letter CAVITY mnemonic (squamous cell carcinoma printed as the most common histology under C).

### Chapter 48 — Atypical Pneumonia and Pneumonia in Immunocompromised (Book p286–295; 90 questions / 10 units)

Mycoplasma opens the chapter as the smallest free-living organism, with its wall-free sterol membrane explaining β-lactam failure, the ten-percent pneumonia picture, seven extrapulmonary manifestations, four radiological patterns, the biphasic PPLO culture with its fried-egg appearance, rapid cold-agglutinin testing and azithromycin as the printed drug of choice. Chlamydia is built from its four printed features (obligate intracellular, peptidoglycan-free, elementary body, metabolically inactive), the walking-pneumonia picture, HEp-2 isolation and micro-immunofluorescence, and the drugs it resists. Legionella is tested through microaspiration, BCYE medium, the sterile Gram stain with pus cells but no organisms, its four risk factors, the typical-versus-atypical contrast, Pontiac fever against Legionnaires disease, DFAT diagnosis and azithromycin plus rifampicin. Lung abscess is then covered in full: necrotising pneumonia and aspiration as its two causes with their organisms, the five-step pathogenesis, the posterior right upper lobe site, fever modified by drainage with foul expectoration and the four examination findings, the diagnostic sequence, the p290 caption strip and complications, AA amyloidosis, the four-item cavitating-lesion differential (TB, malignancy, Nocardia, `Actinomycetes` as printed), the vancomycin–piperacillin-tazobactam–clindamycin regimen and the surgery threshold. The immunocompromised half defines the three host states and seven organisms, then the renal and bone-marrow transplant infection timelines with onset-based infection. Invasive aspergillosis runs from conidia to hyphae with neutropenia as the chief risk, the halo and air-crescent signs, the reverse halo and monad notes, and the fever–hemoptysis–pleuritic triad, followed by BAL/VATS/galactomannan diagnosis, β-D-glucan cross-reactivity, voriconazole against liposomal amphotericin and the mucormycosis contrast. Pneumocystis is tested through GMS cyst staining, fluorescein antibody and PCR, its four HIV records, the cotrimoxazole ladder, steroids below the printed PaO₂ and three prophylactic drugs; Nocardia closes the release as an aerobic, acid-fast filamentous organism (printed as `fungi`) that mandates a host-defence defect, with its brain-and-lung pattern, crooked beaded filaments and sulfonamide regimen.

### Chapter 49 — Cardiac Cycle With Heart Sounds (Book p296–302; 61 questions / 7 units)

Defines heart sounds as discrete vibrations, separates intensity in decibels from frequency in hertz, tests the printed inverse relation `frequency α 1/amplitude` and the six-row high-versus-low-frequency table (features, chamber pressure difference, area heard, thrill), and isolates the ejection systolic murmur of aortic stenosis as the only mixed-frequency sound, with its harsh low-pitched carotid radiation and high-pitched apical element (the Gallavardin phenomenon). The 0.8-second cycle is then split into its 0.3-second systolic and 0.5-second diastolic phase lists, the 70/30 per cent filling division and the valve apparatus whose annular contraction and coaptation close the AV valves and open isovolumetric contraction, producing S1 from M1 and T1 less than 30 ms apart. The six determinants of S1 intensity are worked in printed order — leaflet integrity (with its calcific-MS exception and the `MS + MR: depends on predominant disease` rule), diastolic position, contraction velocity, closure timing (long PR soft against short PR loud), dP/dt and chest-wall transmission — before the valve-lesion table (AS soft, AR soft, MS loud, MR soft), the three causes of a loud T1, the aortic ejection click confused with a loud S1, and the varying, intermittent and wide-split S1 patterns including Ebstein's loud T1. S1 closes with the reverse split, the S1-to-S2 crossover pressure and the hangout interval (30 ms aortic against 80 ms pulmonary, with the printed downward arrow flagged). S2 is then built as aortic and pulmonary closure at 120–150 Hz, with the four determinants of A2 and P2, their behaviour in valve disease, the four-column loud/soft table and the six causes of a single S2, before the wide split above 50 ms with its variable and fixed arms and the paradoxical split with its early-P2 and delayed-A2 causes.

### Chapter 50 — Added Heart Sounds (Book p303–306; 44 questions / 4 units)

Continues the diastolic sequence from protodiastole to atrial systole, fixing the O-P-T-S3-S4 order and the early, mid and late diastolic positions of the added sounds, then defines S3 (ventricular/protodiastolic gallop) with its three printed mechanisms — physiological rapid filling into a hypercompliant ventricle, increased end-systolic volume in a dilated ventricle, and less-than-normal filling of a hypertrophic non-compliant ventricle — and the four valve lesions it accompanies, with MS and TS excluded by the non-stenosed-AV-valve prerequisite. S3 features follow (left lateral position, bell, apex, disappearing upright, leg raising to bring it out) together with the heart-failure-without-S3 note (MS, TS, pericardial tamponade), the pericardial knock of constrictive pericarditis (high-pitched, louder with inspiration, gone after pericardiectomy) and S4 with its four prerequisites (healthy atrium in sinus rhythm, vigorous contraction, non-stenosed AV valve, non-compliant ventricle), its valve-disease table and its three settings. The opening snap is tested through its mechanism and auscultation rules, the S2–OS severity ladder (`>120 mmHg` mild against `40–60 mmHg` severe, units as printed) and the twin proportionalities `OS α LAP` and `S2–OS α 1/LAP`, beside the low-pitched tumour plop of atrial myxoma. Systolic added sounds close the chapter: valvular and vascular ejection clicks with their S2 and S1 rules and five printed features (including absence in severe calcific stenosis), and the non-ejection click of mitral valve prolapse with its dynamic auscultation chain, tested in a standing/squatting scenario.

## Earlier release — Chapters 39 to 44 (Book p236–263)

Chapters 39–44 of *PULSE Medicine Vol 1* are complete in strict source order (**Ch 39 Interstitial Lung Disease, Ch 40 Bronchial Asthma, Ch 41 Pulmonary Eosinophilia, Ch 42 Allergic Bronchopulmonary Aspergillosis, Ch 43 Hypersensitivity Pneumonitis, Ch 44 Pleural Effusion**). Every printed line on Book p236–263 was inventoried from the upload scans and converted into questions in exact page order, including classification braces, HRCT pattern tables, severity/exacerbation tables, parasite and unknown-cause comparison tables, treatment flowcharts, figure captions, printed thresholds and source slips.

| Chapters | Book pages | Source sheets | Questions | Units |
|---|---:|---|---:|---:|
| 1–38 | 1–235 | `01.pdf` PDF13–PDF129; `02.pdf` PDF1–PDF118 | 2,716 | 274 |
| 39 | 236–242 | `02.pdf` PDF119–PDF125 | 55 | 7 |
| 40 | 243–248 | `02.pdf` PDF126–PDF130; `03.pdf` PDF1 | 45 | 6 |
| 41 | 249–252 | `03.pdf` PDF2–PDF5 | 33 | 4 |
| 42 | 253–256 | `03.pdf` PDF6–PDF9 | 29 | 4 |
| 43 | 257–259 | `03.pdf` PDF10–PDF12 | 27 | 3 |
| 44 | 260–263 | `03.pdf` PDF13–PDF16 | 33 | 4 |
| **Cumulative** | **263** |  | **2,938** | **302** |

The 222 new questions deliberately raise the interactive share in line with the owner's request for mixed formats: 75 recall, 46 match, 22 scenario, 19 numeric, 19 fill-up, 16 odd-one-out, 14 true/false and 11 management (147/222 = **66% non-recall**, against 48% in the previous release). The cumulative bank is 1,709 recall, 317 numeric, 314 match, 177 fill-up, 129 scenario, 113 true/false, 103 odd-one-out and 76 management. Source slips and debatable statements discovered on p236–263 (the p238 "End to early expiratory" crackle timing, "Anti-FDGF", the p246 header carry-over from the extrinsic/intrinsic table, "Cytogenic organising pneumonia", "TEP" for TPE, ipratropium "500 mg", the p262 "< 60 g/L" glucose cell, "Calculated effusion" as an ICD indication and "VAT" for VATS) are preserved verbatim and itemised in [audit/known-source-caveats.md](audit/known-source-caveats.md).

### Chapter 39 — Interstitial Lung Disease (Book p236–242; 55 questions / 7 units)

Opens with the interstitium's three types and the parenchymal equation (alveoli + alveolar + vascular interstitium), then defines ILD as diffuse parenchymal lung fibrosis driven TGF-β > PDGF with TGF-β the most potent fibrogenic cytokine, classifies ILD (IIP m/c, autoimmune, HP, sarcoidosis, miscellaneous) and ranks the seven idiopathic interstitial pneumonias with the smoking brace on RB-ILD/DIP and the DAD/post-COVID acute interstitial pneumonia bullets. Autoimmune and miscellaneous lists follow (asbestosis lower lobe against the silicosis/berylliosis/CWP upper-lobe brace, EGPA, NF/tuberous sclerosis, bleomycin, smoking LCH, LAM), with the UIP/NSIP/COP/LIP important-points boxes and the RA=UIP / others=NSIP note. Clinical features cover the two cardinal symptoms misdiagnosed as bronchitis, the additional-symptom pairings, the velcro-crackles/clubbing table versus bronchiectasis, the three skin signs, hypoxia→pulmonary HTN as the top prognostic factor, the direct-PH rule-out note and the bibasal subpleural CXR. PFT runs initial Type 1 diffusion failure to advanced Type 3 ventilatory failure; HRCT is investigation of choice, with the UIP suggestive/specific braces, absent nodules/GGO, captioned scans and pirfenidone/nintedanib (anti-FDGF as printed). NSIP (postero-basal GGO, better prognosis, MMF best), the ten NSIP-pattern drugs with the cyclophosphamide/methotrexate HP brace, COP/BOOP (Masson buds, halo vs reverse-halo, steroid-responsive restrictive type) and the LAM/LCH/LIP cyst panels follow, then the eight-row HRCT finding–disease table, nodular-shadow and tree-in-bud notes, mosaic-attenuation and lower-lobe captions, the upper-lobe ILD list with its "LL reticular shadows in IPF" film, and PAP (SP-B congenital vs anti-GM-CSF acquired, chunky gelatinous PAS+ sputum, batwing, whole lung lavage).

### Chapter 40 — Bronchial Asthma (Book p243–248; 45 questions / 6 units)

Starts with the pure-airway feature list (no hypercapnia/PH/cor pulmonale), the reversibility box (4 puffs SABA, 30 min, 12% + 200 ml separating Asthma from COPD), the GINA feature stack, the four symptoms and the variable/night/RSV pattern with its four triggers. Etiopathogenesis lists the nine triggers (with 5q polymorphism), the hygiene hypothesis TH2→TH1 chain, IL-4/IL-5/IL-13 actions, early (histamine/tryptase/PGD2) versus late (4–6 h, basophil) phases, and the eosinophil mediator/protein/granule sets. Histopathology numbers chronic inflammation (with Curschmann spirals captioned), muscle hypertrophy, goblet hyperplasia and patchy epithelial necrosis; the ten-row extrinsic-vs-intrinsic table and the Samters triad triangle (as printed) follow. Severity grading covers intermittent versus persistent disease and the mild/moderate/severe ladder — tested by column position because the print carries over the extrinsic/intrinsic headers and writes "Significantly ↓ activity" in the severe nocturnal cell — then the twelve-row acute-exacerbation-vs-impending-failure table with its merged gas cells and printed PEFR "L/min" bands. Management makes ICS the mainstay (five effects, three examples, the printed "Early LCS" slip noted), denies SABA any role in persistent Asthma, steps ICS–formoterol through tiotropium to the three biologics (mepolizumab's printed IL-5-receptor description and "Dupilumab" preserved), and retires methacholine/RAST in favour of FeNO. The ER flowchart (confirm→determine→acute-severe drug arm with ipratropium "500 mg" as printed→1-hour PEFR/saturation reassessment→MgSO4→NIV→intubation, impending failure straight to intubation) and brittle Asthma Types 1 (oral steroids) and 2 (s/c adrenaline) close the chapter.

### Chapter 41 — Pulmonary Eosinophilia (Book p249–252; 33 questions / 4 units)

Defines eosinophilic lung disease (airway > parenchyma, role unclear, peripheral counts not always raised) with its three defining features, then splits causes into Known (parasite hypersensitivity/invasion, drugs and toxins, TPE, ABPA) and Unknown (AEP, CEP, EGPA under three printed names, idiopathic hypereosinophilic syndrome), records the diseases *not* classified under ELD (including Asthma, "cytogenic organising pneumonia" as printed and HP) and the BAL ≥40% pair "TEP"/CEP. The parasite table contrasts Loeffler syndrome (Ascaris-first, type 1 larval hypersensitivity, migratory infiltrates, self-limiting) with Paragonimus invasion (chocolate sputum, eggs/ELISA, praziquantel DOC), followed by the NSAID-led drug/toxin list. TPE is built line-by-line: male predominance, the two filarial organisms, microfilarial hypersensitivity with its three evidence bullets, acute-on-chronic symptoms ("stimulate status asthmaticus" as printed), the >3000/mm³, BAL ≥40% and IgE >1000 u/ml laboratory triad, mottling radiology with its captioned film, and DEC dosing with its 7-day improvement and 20% relapse bullets. The unknown-cause table is completed across two pages — restarted-smoking AEP with its 2–3-day ARDS-like course and captioned imaging, atopic CEP of women 30–40 with the reverse-bat-wing/photographic-negative sign and right-predominant captions, and the JAK2/PDGFRα hypereosinophilic syndrome with its 40%/60% organ frequencies, >1500/µL-for->6-months criterion and printed steroid unresponsiveness against the merged Steroid cell for AEP/CEP.

### Chapter 42 — Allergic Bronchopulmonary Aspergillosis (Book p253–256; 29 questions / 4 units)

Microbiology ranks A. fumigatus (saprophyte) over niger/flavus/terreus with conidiophore/septate-hyphae identification and the two captioned micrographs, then draws the four lung manifestations with their descriptors (aspergilloma in a TB cavity, COPD chronic necrotising disease with thick-walled cavities, angioinvasive disease of neutropenic/steroid hosts). The pathogenesis flowchart is followed arm by arm from Asthma/CF colonisation through Type I > Type III hypersensitivity to eosinophilia/IgE, migratory infiltrates and wall-weakening bronchiectasis, and hypha-bearing plugs with atelectasis. The Th2 note and the bilateral/upper-lobe/central/proximal bronchiectasis definition pair with four captioned images (cystic central bronchiectasis with mucoid impaction, tree-in-bud central bronchiectasis, mucus-distended bronchi, hyperattenuated mucus), and the clinical block fixes recurrent exacerbations in refractory Asthma/CF, brownish plugs, 15–20% signs and rare upper-lobe fibrosis before its three-group cause list (rheumatology AS/sarcoidosis, occupational trio, ABPA/LCH/HP/TB). Evaluation tests the predisposing condition, both obligatory IgE criteria (>1000 IU/ml plus skin test/specific IgE) and the any-2 supportive tier, IgE as the most useful test, and obstructive-to-Stage-5-restrictive PFT; imaging captions cover fleeting infiltrates over dated films, tram tracks, finger-in-glove, "Trees in bud" as printed and saccular dilatation. The unlikely-versus-against X-ray tiers and the 12-week-steroid→16-week-itraconazole→omalizumab ladder with periodic IgE monitoring close the chapter.

### Chapter 43 — Hypersensitivity Pneumonitis (Book p257–259; 27 questions / 3 units)

Defines extrinsic allergic alveolitis of non-smokers through repeated organic dust, Type IV > III hypersensitivity and lymphocytic terminal-airway/alveolar/interstitial inflammation, with the no-type-1 triad of absences, diffuse→reticulo-nodular infiltrates and non-caseating granulomas. The twelve-disease etiology table is tested cell by cell, including both merged antigen spans (Thermoactinomyces vulgaris across farmer's/bagassosis/mushroom worker's; Aspergillus clavatus across compost/tobacco/malt/cheese washer's), the m/c and 2nd-m/c tags, and the table's blank source/antigen cells exactly as drawn. Presentation separates self-resolving acute disease (fever/chills/cough, ↑ESR, 2–4 days), the most common subacute form (progressive dyspnea/cough/fatiguability, no systemic features, upper lobe) and fibrosing chronic disease; complications assign rare fibrosis to bird fancier's lung and emphysema to farmer's lung, supported by the seven-cause non-caseating-granuloma note (with "30% TB") and the three non-COPD emphysema causes. Management covers non-specific type III precipitins, BAL CD8/CD4 > 2 against sarcoidosis's mirrored CD4/CD8 > 2, restrictive chronic PFT, the captioned acute-HP film, CT centrilobular nodules/GGO/head-cheese mosaic with its two captioned scans, subacute steroid response versus irreversible fibrosis, and the six-row HP-vs-ABPA table whose only shared positive is the type III IgG precipitin.

### Chapter 44 — Pleural Effusion (Book p260–263; 33 questions / 4 units)

Anatomy fixes the mesothelial lining (surfactant note as printed), 10–20 ml normal volume, lymphatic/vacuum negative pressure, the coupling-organ phrase, both pleurae with their mesodermal origins and pain properties ("Developes" preserved), the 50/200/300 mL detection ladder, and the 70/25/1–5% cellular plus glucose/protein/LDH composition. Light's criteria are tested as three printed ratios with the any-1/all-3-negative brace and the CCF-diuretic one-third misclassification against the higher-is-transudative albumin gradient. Causes enumerate all ten transudates (NT pro BNP bracket, urinothorax's ammoniacal chemistry) and six exudates (RA/SLE arrows, the left-sided pancreatitis/oesophageal-rupture brace), the both-types pair and four drugs; TB effusion keeps its 20–30-year female first-exposure profile, easing pleuritic pain and 25–30% later pulmonary TB, and examination runs through the deviated trachea of the captioned left-effusion film to stony dullness. Exudative detail covers the uncomplicated-vs-complicated parapneumonic table (glucose "< 60 g/L" as printed), empyema's pus/protein/LDH/split-pleura set against the abscess scan, the three low-pH causes with malignancy's poor-prognosis arrow, and chylothorax versus pseudochylothorax across all merged and split rows. Glucose tiers (RA alone below 30), the cardiac NT pro BNP line, the four ICD indications ("Calculated effusion" preserved against its own page's loculated film), six eosinophilic-effusion causes, the central-trachea loculated caption, the TB sensitivity ladder to 90% biopsy-plus-culture, and neoplastic effusion (mesothelioma first as printed, breast metastasis, 50% cytology, "VAT" or CT biopsy, poor prognosis except lymphoma) finish the release at p263.

## Earlier release — Chapters 34 to 38 (Book p206–235)

The requested five chapters were reviewed sheet-by-sheet in printed order (`uploads/02.pdf` PDF89–118 = Book p206–235, the second Pulmonology run after Chapters 29–33), then encoded with deterministically balanced, non-predictable options across all 8 formats (`recall`, `numeric`, `scenario`, `truefalse`, `oddoneout`, `management`, `fillup`, and 2- to 4-item bijective `match` items) and page-cited explanations. Every printed list, table cell, flowchart arm, figure caption, murmur description, formula and Note box on these 30 sheets is covered. All source-text quirks (the `>50–70%` occlusion and `SBP < 90 mmHg`/`≥ 15 mins` brace on p206, `McConnel's sign`, `NT pro BNP` and `Polo mint sign` on p207–211, `Trepostinil` and the `Right atrial pressure` box term on p212–217, `Bronchiectasis (Sicca)` and `Pseudobronchiectasis` on p218–221, the `Type-3` anaesthesiology note that conflicts with the Type III row on p231, the `PAS positive milky white BAL` shared by acute silicosis and PAP on p224–226, `Serpentile`, `Epitheloid` and `crow feet sign` on p227, the `erythemoid lesions` spelling on p229, and the `fibrotic vasoconstriction (14–21 days)` phase name on p234) are preserved faithfully and documented in [audit/known-source-caveats.md](audit/known-source-caveats.md). Existing Chapters 1–33 remain unchanged.

| Ch | Title | Printed pages | PDF sheets | Questions | Units |
|---:|---|---:|---:|---:|---:|
| 34 | Venous Thromboembolism | 206–212 | 02.pdf PDF89–95 | 53 | 7 |
| 35 | Pulmonary Hypertension | 213–217 | 02.pdf PDF96–100 | 42 | 5 |
| 36 | Bronchiectasis | 218–222 | 02.pdf PDF101–105 | 40 | 5 |
| 37 | Occupational Lung Diseases | 223–229 | 02.pdf PDF106–112 | 50 | 7 |
| 38 | Respiratory Failure and Acute Respiratory Distress Syndrome | 230–235 | 02.pdf PDF113–118 | 42 | 6 |
| **Cumulative total** |  | **235 book pages** |  | **2,716** | **274** |

Cumulative format distribution through Chapter 38: 1,634 recall, 298 numeric, 268 match, 158 fillup, 107 scenario, 99 truefalse, 87 oddoneout, 65 management. **New in this release:** 117 recall, 24 numeric, 35 match, 16 fillup, 18 scenario, 14 truefalse, 9 oddoneout, 3 management — i.e. 110 of 227 new items (48%) are non-recall formats.

### Chapter 34 — Venous Thromboembolism (p206–212)

AKA pulmonary thromboembolism with 60–80% mortality in massive PTE; pathogenesis as migration of thrombi/microthrombi from the systemic circulation to the pulmonary vasculature, with deep veins of the lower limb > upper limb and maximal risk from supra-popliteal veins draining to femoral veins or pelvic veins in pregnancy; acute cor pulmonale (RV dilatation/hypertrophy ± failure, most common cause VTE) and calf DVT as the commonest site that does not embolize; massive VTE defined as any PE with hypotension, with the printed chain of >50–70% occlusion → hypoxaemia → RV and RA dilatation → septal push → ↓LV volume → ↓cardiac output → SBP < 90 mmHg lasting ≥ 15 mins or needing inotropes; presentation (unexplained dyspnea with clear lung fields most common, chest pain second, sudden cardiac death and syncope), the two-item D/d of VTE and metabolic acidosis, and the Golden 4 (clinical hypotension; ECHO with McConnel's sign — hypocontractile RV free wall plus hypercontractile apex — septal push, LV contraction and exclusion of tamponade; NT pro BNP for RV dilatation and troponin I for RV ischaemia; CTPA as IOC showing dilated PA, clot and large RV); submassive risk stratification (RV dilatation/ischaemia low risk, escalating with biomarker rise) and non-massive VTE (10–20%, peripheral lodging, recurrent/non-resolving pneumonia, cough, pleuritic pain, haemoptysis); normal investigations with pulmonary infarction as the complication; genetic risks (factor-V Leiden commonest, antithrombin III, protein C and S) versus the acquired bracket (antiphospholipid syndrome, PRV, PMF, HIT, PNH) plus adenocarcinoma, COPD, reduced-EF heart failure, membranous nephropathy losing antithrombin III, OCPs, HRT, pregnancy/post-partum and surgery with immobilisation > 4 days; the V/P physiology with ventilation and perfusion maximal at the base and ratio maximal at the apex; dead-space (V normal, P 0, V/P ∞) versus shunt (V 0, P normal, V/P 0) physiology; the symptom/sign hierarchy with 10–20% frequencies, vagal bradycardia, cor pulmonale branches and type I failure with normal PaCO2, respiratory alkalosis and a widened A-a gradient; CXR signs (bands of atelectasis commonest, Hampton's hump, Pallas, Westermark, Fleischner) with the PAH film; ECG purposes and patterns (normal commonest, sinus tachycardia commonest abnormality, S1Q3T3 non-specific); pulmonary angiography gold standard, V/Q indications, D-dimer in low risk, ECHO for alternate diagnosis, the seven-row Wells score with its low-versus-moderate/high pathway and the polo-mint sign; and management (80 units/kg heparin IV or 1 mg/kg s/c LMWH, severity determination, alteplase 100 mg over 2 hrs within 14 days versus catheter therapy, 18 units/kg/hr with aPTT 1.5–2× and INR 2–3, the 3-month switch to NOACs lifelong with a positive genetic mutation, and the IVC filter).

### Chapter 35 — Pulmonary Hypertension (p213–217)

Ohm's law mapped to the circulation (PAP − LAP = CO × PVR, so PAP = CO × PVR + LAP) with ↑PVR giving classes 1/3/4 and ↑LAP giving class 2 (commonest cardiac cause mitral stenosis); the five classes (class 1 PAH mostly idiopathic with median survival < 9 months in young females; class 2 left heart disease; class 3 chronic lung disease via hypoxia-related vasoconstriction with chronic bronchitis as the example; class 4 CTEPH responsive to surgery; class 5 miscellaneous) and the class-to-vessel figure (arterioles, pulmonary vein, capillary, pulmonary artery, multifactorial) plus the boxed "hypoxia: vasodilatation except in pulmonary vessels"; the PAH-versus-systemic HTN logic (PAP <<< SAP, PVR <<< SAR, low-resistance high-compliance lungs, systemic HTN → LV hypertrophy versus pulmonary HTN → RV dilatation → RV failure → ↑mortality), the systemic arterial pressure box with its right atrial pressure term, the definition (mean PAP > 20 mmHg at rest on right heart catheterisation), cor pulmonale with its three causes, the wood-unit split (>3 units classes I/III/IV, <3 units class II with PCWP > 15 mmHg), plexiform arteriolopathy of the arterioles, and secondary causes from BMPR2 through limited systemic sclerosis, HIV, schistosomiasis, portal HTN (splanchnic vasodilatation → hyperdynamic circulation → ↑CO) to the serotonin appetite suppressants and toxic rapeseed oil; the pathology triad, the endothelin/NO/prostacyclin pathway table with its treatments, the presentation without overt heart or lung signs, the RV dilatation → septal push → ↑LV volume → ↓CO chain, RV ischaemia chest pain, RV failure with an outward apex shift and the auscultation/palpation/JVP signs (loud P2, wide split, S3 mechanism, 'a' waves, clubbing rare); PA catheterisation as gold standard; the three murmurs (pan systolic with Carvallo's sign, ejection systolic from pulmonary stenosis, Graham Steell's early diastolic murmur with its posture and fixed expiration); CXR, PA aneurysm in Behçet's and Takayasu, and the ECG r/s > 1 in V1 with the normal-pattern note; and the investigations (PFT with normal spirometry and ↓DLCO, ECHO, V/Q, sleep study, HRCT, 6-minute walk test), the vaso-reactivity test with nitric oxide (10% positive, PAP fall of 10 mmHg or PAP < 40 mmHg with unchanged BP and CO) implying high-dose nifedipine 240 mg, general treatment with pregnancy contraindicated, and the NYHA-stratified table (tadalafil + ambrisentan, then epoprostenol by tunnel catheter, treprostinil by microinfusion pump and selexipag) with atrial septostomy and transplant.

### Chapter 36 — Bronchiectasis (p218–222)

Definition as abnormal irreversible bronchial dilatation plus obliterative bronchiolar fibrosis producing obstructive disease that can have a restrictive component; pseudobronchiectasis after influenza or COVID; the obstructive-disease list; the pathogenesis flowchart (infection mostly TB → inflammation → loss of smooth muscle and elastic tissue with both bronchi and bronchioles containing smooth muscle → irreversible dilatation, alongside loss of cilia with pooled secretions and microbial colonisation, wall weakening, and goblet cell hyperplasia → mucus hypersecretion → obstruction) and the normal-versus-diseased bronchus diagram; the three morphological types with grades C/V/S, traction bronchiectasis as a restrictive ILD-classified lesion, the distribution (usually unilateral, left lower lobe commonest, F > M, 50–70 years) and the four histological panels; paediatric aetiology (post-infective pertussis/measles, Mounier-Kuhn, William Campbell, Kartagener, Young, cystic fibrosis, yellow nail, α1-antitrypsin deficiency), impaired mucociliary clearance, McLeod's syndrome, isolated IgA deficiency as commonest primary immunodeficiency and the adult list (idiopathic 30%, TB 40%, Brock's syndrome, IgA deficiency, Sjögren); clinical features (postural cough, copious foul three-layered sputum with early morning exacerbation, haemoptysis from a thin-walled vein, recurrent pneumonia), clubbing in children with the cystic type, coarse early-mid inspiratory crackles with diffuse rhonchi, the sicca and ABPA notes, plain-film signs (tram track, bunch of grape, finger in glove, low sensitivity) and the three CT criteria (dilatation 1–1.5× the adjacent vessel, lack of tapering, tree-in-bud with signet ring); and complications (cor pulmonale with acute versus chronic causes, massive haemoptysis in dry disease, empyema with bronchopleural fistula, AA amyloidosis, abscess), airway clearance with 7% hypertonic saline and postural drainage, CF-specific DNase and nebulised gentamycin, localized resection, the macrolide/beta-lactam penetration rationale with 6–9 months of macrolide immunomodulation, and the Pseudomonas >> H. influenzae > S. pneumoniae hierarchy.

### Chapter 37 — Occupational Lung Diseases (p223–229)

Disease groups and the pneumoconiosis definition, the dust-size table (>3 µm secondary bronchi, 0.5–3 µm bronchiole, <0.5 µm alveoli), the four pneumoconioses with silicosis commonest, and byssinosis as organic-dust hypersensitivity with recurrent Monday fever; silicosis in full (industries, crystalline quartz as SiO2 free silica with the higher hazard, parenchymal-only involvement with no pleura, malignancy/COPD risk, and the acute-versus-chronic table — 2 years versus 10–30 years, a dash versus macrophage injury with silicotuberculosis and SLE/RA, the acute dyspnea/hypoxia/weight-loss triangle versus chronic dry cough with chest signs in 25%, PAS-positive milky white BAL versus a mixed PFT pattern, very poor versus dash prognosis); its radiology (acute crazy pavement with ground glass, thickened septa and centrilobular nodules; chronic nodules → angel-wing conglomerate nodules ± cavitations with egg-shell hilar calcification → PMF and upper lobe ILD); the crazy-pavement differential (DAH, AEP, PAP with anti-GM-CSF antibodies); coal worker pneumoconiosis with its shared features, the three-row CWP-versus-silicosis table and Caplan syndrome (necrobiotic nodule + IgA rheumatoid factor-positive RA + active synovitis); chronic asbestosis (90% serpentine chrysotile versus 10% amphibole with amosite most dangerous, industries, smoking effect, pleural plaques with candle-dripping and holly-leaf signs, subpleural linear densities, BAPE as the earliest unilateral haemorrhagic exudate with eosin <25% and mesothelial cells <50%, visceral calcification with crow feet, "no clinical signs", and parenchymal lower lobe disease with shaggy heart sign, DMF, bibasal fine crackles, clubbing and restrictive PFT); asbestos malignancy (lung cancer adenocarcinoma > squamous > small cell at 10–30 years with smoking and cough/haemoptysis versus mesothelioma epitheloid > sarcomatoid beyond 30 years without smoking, with pancytokeratin/calretinin and microvilli/desmosomes/tonofilaments), the ferruginous body, berylliosis as delayed hypersensitivity with non-caseating granulomas mimicking sarcoidosis, the seven-item non-caseating granuloma list, and the berylliosis page (sarcoid features that are absent, ceramic/battery/alloy industries, upper lobe ILD to PMF, positive lymphocyte proliferation test, normal X-ray in 50%, and the ground glass/nodules/septal lines HRCT triad).

### Chapter 38 — Respiratory Failure and Acute Respiratory Distress Syndrome (p230–235)

Definition and the hypoxemic (PaO2 < 60 mmHg, SpO2 < 90%) and hypercapnic (PaCO2 > 50 mmHg) thresholds on room air, the abbreviation box (PAO2, PaO2 ~97 mmHg, PaCO2 ~40 mmHg, A-a gradient), and the four-type table — Type I diffusion failure with a 150-fold CO diffusion potential and no hypercapnia plus its aetiology list and the separate asthma entry (normal parenchyma, absent CO2 retention, ↑DLCO); Type III parenchymal damage from ILD (↓diffusion) or ARDS (↓compliance) with ↓PaO2/↑PaCO2/↑gradient; Type IV shock with a dash for pressures; the anaesthesiology "Type-3" note (↓FRC = RV + ERV → post-op atelectasis, with supine/obese/ascites, residual anaesthesia, upper abdominal incision and secretions); V/Q matching (normal 0.8, upper zone > 1 non-dependent, lower zone < 1) and the dead-space-versus-shunt table; both flowcharts (V/Q mismatch/shunt/dead space first level, then Type II versus Type III on the gradient, oxygen-correctable mismatch versus shunt, high altitude, and the hypercapnic generator/pump/effector branch versus V/Q mismatch in ARDS and ILD); ARDS synonyms, the 1992 AECC criteria (PCWP < 18 mmHg, bilateral infiltrates, PaO2/FiO2 < 200) with its 20% capture and 70–75% mortality, the Berlin 2012 definition (onset within a week, infiltrates unexplained by effusion/collapse/nodules, normal ECHO, PEEP ≥ 5 cm H2O) with mild/moderate/severe ranges and the three edema-preventing factors; ARDS aetiology (primary including pulmonary sepsis, massive transfusion, pancreatitis, TRALI, smoke, drowning and post-surgery versus secondary non-pulmonary sepsis and major trauma/burns), the cytokine-to-neutrophil chain with capillary injury and proteinaceous alveolar fluid causing surfactant loss, collapse, ↓compliance and impaired gas exchange, and the three phases (exudative 7 days with the eosinophilic hyaline membrane hallmark, fibroproliferative 7–14 days, fibrotic vasoconstriction 14–21 days); and the clinical features, ventilation strategies (inverse ratio, prone, permissive hypercapnia), the VILI table (volume/baro/atelecto trauma with low tidal volume, low plateau pressure and high PEEP), and the six-item differential of acute breathlessness.

## Earlier release — Chapters 29 to 33 (Book p169–205)

The requested five chapters were reviewed sheet-by-sheet in printed order (`uploads/02.pdf` PDF52–88 = Book p169–205, the largest single run so far and the point where Hematology hands over to Pulmonology on Book p185), then encoded with deterministically balanced, non-predictable options across all 8 formats (`recall`, `numeric`, `scenario`, `truefalse`, `oddoneout`, `management`, `fillup`, and 2- to 5-item bijective `match` items) and page-cited explanations. Every printed list, table cell, flowchart arrow, formula, curve caption, pressure trace value and Note box on these 37 sheets is covered. All source-text quirks (`IL-II`/`Oprelvekin` and the two thrombopoietin sources on p169, `Gp vl` on p171, the `vII, Ca²⁺` annotation on p172, the dash-only mechanism cells on p174, `Hb >10 mg/dL` on p176, `85%`/`–` in the vWD table and `C/I : Type 2B` on p182, the warfarin `INR` row and 6-hour factor VII half-life on p183, `150 ml` dead space and PA-above-bronchus on p186, the tracheal smooth-muscle dash on p189, `F508`/`7q` and nasal-NO gold standard on p190, `Re = 2rvd/η` on p191, `Tidal volume α 1/TPP` on p193, `1/2 FVC` on p197, `15s or minimum 6s` and the printed `mg` bronchodilator units on p198–199, `< 30` without a percent sign on p202, and the emphysema `↑ volume/surface area` pathology line on p204) are preserved faithfully and documented in [audit/known-source-caveats.md](audit/known-source-caveats.md). Existing Chapters 1–28 remain unchanged.

| Ch | Title | Printed pages | PDF sheets | Questions | Units |
|---:|---|---:|---:|---:|---:|
| 29 | Platelets - Basics | 169–172 | 02.pdf PDF52–55 | 34 | 4 |
| 30 | Approach to Bleeding Disorders | 173–184 | 02.pdf PDF56–67 | 81 | 12 |
| 31 | Clinical Anatomy of Lungs | 185–192 | 02.pdf PDF68–75 | 59 | 9 |
| 32 | Clinical Physiology of Lungs | 193–196 | 02.pdf PDF76–79 | 30 | 4 |
| 33 | Pulmonary Function Tests | 197–205 | 02.pdf PDF80–88 | 57 | 9 |
| **Cumulative total** |  | **205 book pages** |  | **2,489** | **244** |

Cumulative format distribution through Chapter 33: 1,526 recall, 274 numeric, 233 match, 142 fillup, 89 scenario, 85 truefalse, 78 oddoneout, 62 management.

### Chapter 29 — Platelets - Basics (p169–172)

Myeloid progenitor lineages (RBC, granulocyte, monocyte, megakaryocyte → platelet) and thrombopoiesis (boxed thrombopoietin "from kidneys and liver" driving the myeloid stem cell; Early limb requires thrombopoietin "from liver", IL-3 and IL-11 with recombinant Oprelvekin for chemotherapy-induced thrombocytopenia; Late limb requires SDF-1), megakaryocyte maturation with Stage II–IV morphology and endomitosis as "multiplication of megakaryocytes", and the four morphological variants (giant → ITP, dwarf → CML, cloud → primary myelofibrosis, staghorn → essential thrombocytosis); platelet basics (lifespan 10 days, normal 1.5–4 lakh/µL, stored-blood lifespan 72 hrs, thrombocytopenia <1,00,000, bleeding <20,000, significant bleeding <10,000/µL), platelet-poor vs platelet-rich plasma at room temperature with the lupus anticoagulant 4 °C exception, EDTA satellitism/pseudothrombocytopenia re-sampled into 3.2% trisodium citrate, transfusion completed within 20 mins with the SDP (apheresis, costly) vs RDP (pooled, cheap, commonly used) table and the 30,000–50,000 vs 6,000/µL increments; the platelet cascade (endothelial antiplatelet PGI₂/NO/ADPase, anticoagulant heparin-like molecules–AT III, thrombomodulin–protein C, TFPI, fibrinolytic tPA; vWF sources and coiled Weibel-Palade storage; Gp VI on collagen and Gp Ib-IX on platelet; α vs δ dense granules; Gp IIb-IIIa with fibrinogen); and the clotting cascade (intrinsic in vitro with back amplification of thrombin, extrinsic in vivo through thromboplastin/factor III, the common arm through X → prothrombin → fibrin with clot stabilisation by XIII; fibrinolysis with tPA/plasmin/FDP, the protein C-S, t-PA and TFPI checkpoints, the four antifibrinolytics, and aPTT/PT with "poor sensitivity").

### Chapter 30 — Approach to Bleeding Disorders (p173–184)

The five-step evaluation protocol (platelet vs coagulation bleed table including petechiae <3 mm/purpura 3–10 mm/ecchymotic patch >10 mm, ilio psoas as the m/c muscle site and sex distribution; single vs trilineage chart ending in leukemia/aplastic anemia/MDS → platelet-related bleeding; count-based risk at 20,000 and 10,000/µL with pharyngeal red purpura and retinal bleed as risk markers; the drug tables for chemotherapy, procainamide/gold, heparin-PF4, anticonvulsants, Gp IIb/IIIa inhibitors, NSAIDs, quinine and penicillin; hypersplenism in liver disease with platelet destruction as the m/c arm; schistocytes ruling out HUS/TTP and the normal smear with few giant platelets leading to the ITP summary flowchart); ITP in full (Werlhof's disease, not in the elderly, SLE/RA/H. pylori/HIV/HCV, IgG against Gp IIb/IIIa and Ib/IX plus inhibited platelet release, non-palpable non-blanching purpura vs palpable branching vascular purpura, Evans syndrome Coombs, marrow indications, features inconsistent with ITP, newly diagnosed/persistent/chronic durations, the 30,000/µL goal, prednisolone 2 weeks then taper, IVIg/anti-D indications and Rh-spleen mechanism with its two prerequisites, and second-line rituximab + dexamethasone, eltrombopag/romiplostim, splenectomy and azathioprine with a 2–4 day response); qualitative platelet disorders (uremic bleeding as m/c acquired cause; the adhesion/granulation/activation defect map; PFA-100 >80 s and the gold-standard aggregation test with one- vs two-wave responses); aggregation curves and the ristocetin agglutination test with the aPTT vWD-vs-BSS logic; the optical-density interpretation panels; Glanzmann thrombasthenia, afibrinogenemia (prolonged thrombin time), Bernard-Soulier syndrome with megathrombocytosis and the qualitative drug list; von Willebrand disease (m/c congenital bleeding disorder, chromosome 12p, A/D3/C domains, ADAMTS13, coiled-to-uncoiled release, factor VIII T½ 2 → 12 hours, Types 1/2A/2B/2M/2N/3 with the full two tables, pseudo-vWD, the four acquired vWF disorders and management with vWF concentrate/desmopressin — 2B contraindication, tachyphylaxis and SIADH); and DIC (the aPTT/PT/platelet clinical-approach table through factor XII/XI, hemophilia A and B, vWD, lupus anticoagulant, liver disease and warfarin with the 6-hour factor VII half-life; the etiology list from sepsis to Kasabach-Merritt; the six-step pathogenesis chain, ICU monitoring, purpura fulminans, FDP as most sensitive vs D-dimer as most specific with fragmented RBCs and low fibrinogen, and management with cryoprecipitate and the obsolete drotrecogin alfa/heparin).

### Chapter 31 — Clinical Anatomy of Lungs (p185–192)

Gross anatomy (right 3 lobes vs left 2, bilateral oblique and right horizontal fissures, the posterior lower lobe needing a lateral film or CT with infrascapular and infraaxillary auscultation, the azygos "tadpole" fissure in 1–2% of people, and the phantom tumor of the horizontal fissure in heart failure resolving with diuretics with its 2- and 4-week films); hilar structures and the PA-anterior-right/PA-above-left relations, hilar enlargement causes with hilar lymphadenopathy and PA dilatation bracketed "more common", and Weibel's 23 generations with the conducting zone 0–16 as 150 ml of anatomical dead space and the acinus from generation 17; bronchi types and the right (1.5 cm, shorter, steeper, 2 cm, 45°) vs left (1.3 cm, longer, 5 cm) dimensions with R > L foreign-body impaction, the 25 mm → 0.25–0.3 mm calibre and 5 → 7,00,000 cm² area change, the secondary pulmonary lobule and the BPS definition containing the intrasegmental artery; the ten segments of each lung with supine vs standing aspiration segments; the acinus parts with centriacinar (smokers) and panacinar (α-1 antitrypsin) emphysema; the conducting airway cells (basal, goblet, club/Clara with xenobiotic detoxification and CGRP in migraine, Kulchitzky dense-core vesicles) with the cartilage/smooth muscle/goblet table, epithelial zonation from pseudostratified ciliated columnar to simple cuboidal, and the mediator hierarchy (leukotriene as most potent constrictor, VIP as most potent dilator, methacholine challenge, anticholinergics); cilia up to the terminal bronchiole with the mucociliary escalator, primary ciliary dyskinesia (dynein arm, 5 years, nasal nitric oxide always low) and the Kartagener triad triangle; and cystic fibrosis (F508 on 7q, chloride defect, affected sites, ivacaftor); airway resistance (Ohm and Poiseuille laws, maximal resistance at generations 5–7 from parallel small airways, Reynolds number flow table); and alveolar type I vs type II cells with the bleomycin injury/hyperplasia split, surfactant function/components/synthesis, DPPC, beractant and GM-CSF in pulmonary alveolar proteinosis.

### Chapter 32 — Clinical Physiology of Lungs (p193–196)

Tidal volume (500 mL) and Boyle's law as tidal volume α 1/TPP; the three pressures with TPP = intra-alveolar − intrapleural; the pleura's lymphatics and vacuum, intrapleural negativity with positivity only in forceful expiration, the active inspiration chain and passive expiration, and intra-alveolar pressure of 0 / −1 / +1 mmHg with the −2 to −3 → −7 to −8 mmHg intrapleural trace; the three transpulmonary equations, the 760 mmHg atmospheric reference, the 7–8 mmHg end-inspiratory TPP, intrapleural fluid cohesiveness and negative pressure holding lung to chest wall, the pneumothorax note (intrapleural = intrapulmonary, TPP 0, lung not inflated), and static compliance of 200 mL/cm H₂O maximal at mid-range pressure (ΔV/ΔP with ΔP = TPP); the hysteresis loop with surface tension (more important, overcome by surfactant) and elastic recoil from elastin and collagen, plus the obstructive (↑ compliance, curve up and left, elastin loss, ↓ ERP) and restrictive (↓ compliance, curve down and right, ↑ collagen, ↑ ERP) chains; and dynamic compliance as static compliance plus resistance with the only-dynamic falls (foreign body, kinked ET tube, intrathoracic obstruction) versus static-and-dynamic falls (edema, consolidation, atelectasis, pneumothorax), together with the ERP-versus-volume table at RV, FRC (zero, equilibrium volume, RV + ERV) and TLC.

### Chapter 33 — Pulmonary Function Tests (p197–205)

Lung volumes and capacities with every printed formula and sex split; RV measurement (spirometry cannot measure RV, hence not FRC or TLC; plethysmography versus the obsolete helium/nitrogen methods that miss trapped gas) and spirometry with its physical-demand caveat and the 15 s/6 s exhalation; FVC 4.5 L over 5–6 s and FEV1/FVC ≥80% (4 L) with the obstructive/restrictive/vascular disease tree; obstructive disease in two phases (hyperinflation vs air trapping with the full FVC/FEV1/ratio/RV/TLC/reversibility table), FEV1/FVC <0.7 prompting bronchodilator reversibility with the printed salbutamol/ipratropium doses, 200 mL + >12% indicating asthma versus COPD; restrictive disease with its index ladder, intraparenchymal vs extraparenchymal patterns and RV/TLC split, and vascular disease with normal spirometry but abnormal DLCO; small airway disease (mmEFR/FEF 25–75 and closing volume 10% of VC by the obsolete Fowler technique) with the four flow-volume patterns and the coving/dog-tail shape; the three upper airway obstruction patterns with their examples, the neuromuscular and restrictive loops, and GOLD staging by post-bronchodilator FEV1; DLCO in detail (definition, 20–30 mL/min/mmHg with 70–140% and <40% bands, the six membrane layers, the 210× affinity and diffusion-limited advantage of CO, the 4 s/10 s/0.3% CO manoeuvre, blood volume as the most important determinant, the raised and lowered lists, false-low causes from oxygen and smoking, alveolar haemorrhage/Goodpasture, and the disorder-by-disorder DLCO table); and Kco = DLCO/lung volume with the complete stepwise evaluation flowchart ending in vascular disease, early ILD and the small-airway box.

### Chapter 24 — World of Lymphomas (p140–141)

Initial lymphadenopathy workup (biopsy → FNAC only for lymphoma → excisional biopsy IOC; flow cytometry for CD antigens; cytogenetics/karyotyping/FISH/PCR), common lymphoid progenitor markers (TdT+ + CD34+ + surface markers–; marrow blasts >20% = ALL vs <20% + LN mass = LBL), precursor B-cell differentiation (Pro-B CD19+, Pre-B CD20+ m/c ALL with Early pre-B best prognosis, Naive B surface IgM & IgD, CLL B-cell tumor), lymph node compartmentalization (Pre-GC → Mantle cell lymphoma CD5+, CD20+, CD23–, Cyclin D1+; Germinal centre BCL-6, CD10+, CD23+ → Follicular BCL-2+ low-grade centrocyte vs DLBCL & Burkitt's high-grade centroblast; Post-GC/marginal zone CD20+, CD5/CD10/CD23– → MALToma H. pylori/Sjögren, Splenic MZL HCV, Nodal MZL), plasma cell myeloma markers (CD38, CD138, C19 [printed]), and the B-cell vs T-cell CD marker summary table.

### Chapter 25 — Chronic Lymphocytic Leukemia (p142–145)

CLL overview (m/c elderly leukemia, >65 yrs, M>F, asymptomatic blood lymphocytosis ≥5000 cells/µL on incidental CBC; defective BCL-2 apoptosis; monoclonal mature naive B-cells; SLL nodal counterpart <5000 cells/µL; etiology with no radiation risk), diagnostic workup (lymphocytosis >60,000, smudge cells, hypercellular marrow >30% lymphoid cells, CD5+, CD19+, CD23+, ZAP-70+; Richter transformation to DLBCL; warm AIHA positive Coombs test), combined Rai & Binet staging table (Stages 0–4) & treatment indications (Stages 3–4, B symptoms, symptomatic splenomegaly, AIHA/ITP), CLL prognostic table (Good vs Bad across ZAP-70/CD38, IgVH status, del(13q14) vs del(17p) TP53, del(11q), trisomy 12, β2-microglobulin, staging) & regimens (FCR vs BR ± ibrutinib/venetoclax/rituximab), and Hairy Cell Leukemia (>50 yrs, M:F 4:1, BRAF V600E → RAF-MEK-ERK, massive splenomegaly, pancytopenia + diagnostic monocytopenia, M. kansasii, hairy projections, TRAP+ tartrate-resistant acid phosphatase, dry tap reticulin fibrosis, 'fried-egg' marrow biopsy, CD19/20/22+ & specific CD11c/CD25/CD103/Annexin+, Cladribine DOC, Pentostatin/Vemurafenib/Rituximab, polyarteritis nodosa association).

### Chapter 26 — Non-Hodgkin's Lymphoma (p146–152)

Classification by cell of origin (Precursor/Mature T-cell; Precursor B → ALL, Pre-GC → MCL, Centroblasts → DLBCL/Burkitt's, Centrocytes → Follicular, Post-GC → MZL, Plasmablast → ABC-DLBCL), mature T-cell lymphomas (ALCL ALK/CD30+, t(2;5), breast implants, hallmark cells; angioimmunoblastic; enteropathy/celiac; mycosis fungoides/Sezary; extranodal NK/T EBV+; HTLV-1 adult T-cell; hepatosplenic), grade classification, causative organisms table (EBV 100/70/40/20 rule in HD + Burkitt/PTLD/PCNSL/NK-T; HIV; HCV; H. pylori; HHV-8; HTLV-1), Ann-Arbor staging (I–IV + early unfavourable criteria), general NHL clinical profile, Mantle Cell Lymphoma (t(11;14), CD5+/Cyclin D1+/SOX-11+/CD23–, GIT lymphomatoid polyposis, R-CHOP resistance, classical vs leukemic non-nodal), Follicular Lymphoma (t(14;18) BCL-2, paratrabecular aggregates of cleaved/non-cleaved cells, watch-and-wait vs rituximab, 3%/yr Richter transformation), MALToma (95% H. pylori non-atrophic pan-gastritis, CD5/10/23–, t(11;18), 80% antibiotic response → R-CHOP trial, Sjögren salivary MZL), high-grade NHL & DLBCL (GCB vs ABC-DLBCL plasmablast/MUM-1/HIV-defining, Double/Triple-hit GCB vs Double-expressor ABC Venn diagram, R-CHOP regimen, interim-PET response flowchart), and Burkitt's Lymphoma (30% childhood NHL, chr 8 c-myc t(8;14)/t(8;2)/t(8;22), highest Ki67, Endemic jaw EBV+ vs Sporadic abdominal EBV– vs HIV, CODOX-M/IVAC, starry-sky macrophages).

### Chapter 27 — Hodgkin's Disease (p153–158)

Germinal-centre physiology diagram (Dark-zone centroblasts → Light-zone centrocytes → Post-GC memory B-cells & plasmablasts/plasma cells), B-cell tumor origin summary table, NF-κB [printed NK-κβ] upregulation & chr 9 PDL1 aberration decreasing apoptosis in dark-zone B-cells, stage cure rates (>90% / ≥85% / ~80%), HL vs NHL comparison table (bimodal 15–34 & >60 yrs, contiguous nodal spread, paraneoplastic cerebellar degeneration, 30% B symptoms including cyclical Pel-Ebstein fever), Reed-Sternberg owl-eye bilobed cells in reactive inflammatory stroma, NLPHD (benign, axillary node, CD20+/CD45+/sIg+, popcorn L&H cells, involved-node RT) vs Classical HD (CD15+/CD30+, NS m/c worldwide, MC m/c in India, EBV 100/70/40/20 rule), clinical features (posterior cervical 60–80% > supraclavicular > axillary, rubbery painless nodes, alcohol node sign, pruritus, subacute cerebellar degeneration, minimal change disease, cholangitis, vanishing bile duct syndrome; NS mediastinal/SVC/young females/lacunar cells; MC HIV+/EBV+/elderly & children), staging workup (full-thickness excision biopsy, FDG-PET single most valuable test, early unfavourable 5 criteria, β2-microglobulin in CLL/HD/MM), ABVD regimen toxicities (Adriamycin cardiotoxicity, Bleomycin lung fibrosis, Vinblastine peripheral neuropathy, Dacarbazine), Deauville 5-point interim PET protocol (scores 1–2 vs 3–5 salvage + ASCT), Brentuximab (anti-CD30), BEACOPP, and ISRT/IFRT rules.

### Chapter 28 — Plasma Cell Disorders (p159–168)

Normal plasma cell biology (eccentric cartwheel nucleus, perinuclear Golgi halo, normal κ:λ = 2:1, cytoplasmic Russell vs intranuclear Dutcher bodies), polyclonal (CD19+, CD38+, CD138+) vs monoclonal (CD19–, CD38+, CD138+, CD45–) hypergammaglobulinemia, disorder classification, Multiple Myeloma epidemiology (>70 yrs, Blacks, pesticide exposure, IgG 55% > IgA > IgM > IgD > IgE, light-chain only 20%), Rouleaux/Mott/Flame smear cells, MGUS vs Smoldering MM vs MM criteria, Slim-CRAB Myeloma Defining Events, Plasma Cell Leukemia (≥20% circulating plasma cells), workup (SPEP, 24-hr UPEP Bence Jones casts missed on dipstick, IFE, sFLC ≥100, ISS β2-microglobulin/albumin staging, high-risk FISH t(4;14)/t(14;16)/del(17p)/1q amp, low-dose whole-body CT IOC, negative Tc-99m bone scan), VRD triplet + autologous SCT & targeted drug classes, DKK-1 osteoblast inhibition vs RANK-L osteoclast activation ('raindrop' skull), renal disease (hypercalcemia m/c cause, Tamm-Horsfall cast nephropathy, Type II Fanconi RTA, AL amyloidosis, LCDD), S. pneumoniae infections (m/c cause of death), neuromyeloma, solitary plasmacytoma (curative RT), Waldenström's Macroglobulinemia (del(6q) + MYD88 L265P >90%, IgM hyperviscosity, sausage retinal veins, cryoglobulinemia, anti-MAG neuropathy, plasmapheresis + bortezomib/rituximab/bendamustine/ibrutinib, Bing-Neel syndrome), POEMS syndrome, Heavy Chain Diseases (Franklin γ, Seligmann α IPSID, Mu μ CLL), and Systemic Amyloidosis (AL, AA/SAA, dialysis Aβ2M, ATTRm/ATTRwt Tafamidis; kidney, restrictive sparkling heart with Tc-99m PYP scan & digoxin/CCB cautions, cholestatic liver biopsy bleeding contraindication, hyposplenism, ANS/CNS/endocrine, raccoon eyes, macroglossia, shoulder pad sign, abdominal fat pad Congo red apple-green birefringence, CyBorD + Daratumumab).

## Earlier release — Chapters 22 to 23 (Book p126–139)

The requested two acute leukemia chapters were reviewed sheet-by-sheet in printed order (`uploads/02.pdf` PDF9–22 = Book p126–139, including rotating the sideways scan on PDF10 / Book p127 upright for visual verification), then encoded with shuffled, parallel, non-predictable options across all formats (`recall`, `numeric`, `scenario`, `truefalse`, `oddoneout`, `management`, `fillup`, and 4-item bijective `match` items) and page-cited explanations. Source-text peculiarities (`t(8; 21) / t(RUNX1; RUNX1)` and `FLT3-ITD (Inverse tandem duplication...)` on p129, `Hypergranular myeloblasts` smear caption on p134, `Sans criteria for risk` on p135, `Nucleoli` table vs schematic on p136, and `Radiation : in AML, ALL, CLL` on p137) are documented in [audit/known-source-caveats.md](audit/known-source-caveats.md). Existing Chapters 1–21 remain unchanged.

| Ch | Title | Printed pages | PDF sheets | Questions | Units |
|---:|---|---:|---:|---:|---:|
| 22 | Acute Leukemia | 126–135 | 02.pdf PDF9–18 | 81 | 10 |
| 23 | Acute Myeloid Leukemia V/S Acute Lymphoblastic Leukemia | 136–139 | 02.pdf PDF19–22 | 40 | 4 |
| **Cumulative total** |  | **139 book pages** |  | **2,021** | **177** |

Cumulative format distribution through Chapter 23: 1,297 recall, 216 numeric, 154 match, 114 fillup, 73 scenario, 70 truefalse, 56 oddoneout, 41 management.

### Chapter 22 — Acute Leukemia (p126–135)

Adult vs paediatric leukemia distribution (adults 80% AML / 20% ALL; children 90% ALL / 10% AML), myeloid precursor differentiation table (Myeloblast → neutrophils → myeloblastic leukemia m/c 70–80%; Promyelocyte → promyelocytic leukemia 5–10%; Monoblast → monocytes → monocytic leukemia 5%; Normoblast → RBCs → erythroid leukemia 1–2%; Megakaryoblast → platelets → megakaryocytic leukemia 1–2%), AML pathogenesis (1. Somatic mutation → 2. Complete arrest of differentiation → myeloblast takes over marrow → left branch: high turnover → 2–3 months short history → acute presentation without CNS/testes/organ involvement & pancytopenia manifesting as bleeding; right branch: leaks into blood when marrow replaced → blood blasts → ↑↑ counts poor prognosis → late-stage CNS involvement), hyperviscosity note (AML >1 lakh vs ALL >5 lakhs d/t smaller lymphoblasts), 5-point hematological diagnosis (morphology, cytology, immunophenotyping, cytogenetics, molecular genetics), AML definition (clonal proliferation of immature leucocytes; myeloblast m/c; median age 65 yrs; M > F), survival by age (<60 yrs 50%, 60–75 yrs 30%, >75 yrs <10%), hereditary risk factors (1–5%; Down syndrome 10–20× ↑ risk, Klinefelter, Patau, Ataxia telangiectasia, Bloom, Fanconi, Kostmann, Wiskott-Aldrich, Diamond-Blackfan, Shwachman-Diamond, Li-Fraumeni, Noonan; germline CEBPA, RUNX1, TP53; Down syndrome TAM within 3 months GATA-1 spontaneous remission vs AML 20% within 4 yrs M7 better prognosis), environmental factors (radiation, benzene, smoking, alkylating agents 5–6 yrs, topoisomerase II inhibitors etoposide 1–3 yrs), hematological diseases (MPNs PV/PMF/ET/CML downward AML-risk arrow, PNH, aplastic anemia/eosinophilic fasciitis, myeloma, 25% MDS 10–19% → AML 20% blasts), classification (FAB M2–M7 does not give prognosis; WHO 2016 5 categories with MDS-related & therapy-related poor prognosis; Recurrent genetic abnormalities blasts ≥20% not required: good prognosis t(15;17) APML, t(8;21), inv(16) CBFβ, NPM-1, CEBPA; bad t(9;22); very bad FLT3-ITD; WHO-5 2023 4 categories with CEBPA and t(BCR,ABL) exceptions; ICC not used now), clinical features (bleeding m/c d/t thrombocytopenia: bruising, petechiae, epistaxis, gingival bleeds, excess menstrual bleeding; anemia; normal ANC → minor infection/pustules; no fever/lymphadenopathy/HSM; bone pains rare, m/c in ALL; complex infections in aplastic anemia & hairy cell leukemia; chloroma m/c orbit, independent of marrow, t(8;21); monocytic M4/M5 gum hypertrophy & perianal infections), skin involvement table (Leukemia cutis non-tender violaceous nodules on extensor forearms M4/M5 Rx chemo vs Sweet syndrome tender erythematous plaques with fever on face/neck d/t PMF/G-CSF/ATRA Rx steroids), investigations (blood picture cytopenias, high LDH, Auer rods; myeloblast vs promyelocyte morphology table with faggot cells; cytology MPO+, Sudan black+, NSE M4/M5/M7, PAS M6/M7; immunophenotyping CD11b/CD13/CD33/CD117/HLA-DR/CD14/CD11c, glycophorin/spectrin, CD41/CD61; t(8;21) RUNX1-RUNX1T1 children/chloroma/M2/CD19+/good; inv(16) M4 Eo organ infiltration; t(9;22) bad except CML; mutations c-Kit, NPM1 cup-shape blasts m/c good, CEBPA >20% blasts, FLT3-ITD bad; European risk stratification), bad prognostic factors (>1 month cytopenias), treatment (Standard vs High risk; 7+3 cytarabine + daunorubicin with ECHO; 10–14 day marrow recovery infection risk with tachycardia/tremors/fasciculations; midostaurin FLT3-ITD; venetoclax BCL-2; post-induction marrow <5% vs >5% and MRD <0.01% vs >0.01%; consolidation AHSCT vs high-dose cytarabine; unfit/elderly azacitidine/decitabine + venetoclax; gemtuzumab-ozogamicin anti-CD33 & ivosidenib IDH inhibitor), and APML (AML M3 young patient bleeding/pancytopenia t(15;17); thromboplastin → extrinsic cascade → DIC; hypergranular 2/3 low WBC faggot+ dumbbell vs hypogranular 1/3 high WBC faggot– butterfly; early ATRA & ↑ TF note; Sans/Sanz low vs high risk with idarubicin; APML differentiation syndrome at 10 days Rx I.V dexamethasone).

### Chapter 23 — Acute Myeloid Leukemia V/S Acute Lymphoblastic Leukemia (p136–139)

ALL survival by age (<10 yrs 90–95%, 10–19 yrs 70–75%, >20 yrs 50–55%), lymphoblast lineage tree (Precursor B cell ALL 80% good prognosis in children, bone marrow ± blood; Precursor T cell ALL 20% poor prognosis, bone marrow ± thymic mass causing mediastinal widening/dyspnea in adolescent boys), Lymphoblast vs Myeloblast comparison table (size smaller vs larger; nucleoli absent vs present in table, with bottom schematic showing nucleoli in both; granules absent vs present; Auer rods absent vs present; MPO/Sudan black negative vs positive; PAS/acid phosphatase positive vs negative; markers CD19/CD20/PAX-5 for B-ALL and CD1/CD2/CD3/CD5/CD7/TdT for T-ALL vs CD11b/CD11c/CD13/CD14/CD33/CD117/HLA-DR for myeloblast), ALL risk factors (Down syndrome m/c malignancy TAM > ALL > AML; defective DNA repair ataxia-telangiectasia & Bloom's syndrome; radiation; printed Note on AML/ALL/CLL), presenting features (B-ALL adult pancytopenia vs children limping/bone tenderness/inability to walk; T-ALL adolescent dyspnea/mediastinal widening; high-count ALL very poor prognosis involving CNS & testes sanctuary sites causing relapse and requiring intrathecal chemotherapy; organomegaly rare in B-ALL and ± in T-ALL; rare ocular/skin/salivary/cranial nerve/pericardial/pleural involvement), laboratory features (blood cytopenias, circulating blasts, variable counts, hypereosinophilia preceding blasts by several months; CSF leukemic blasts +ve), B-cell subtypes (Pro B, Pre B m/c with Early pre B-cell best prognosis & CD10⁺ CALLA antigen, Immature B), B-ALL vs T-ALL clinical blocks (B-ALL m/c childhood cancer, fever in 50% d/t lymphoblast cytokines, marrow expansion, bleeding, CNS involvement, misdiagnosed as ITP & aplastic anemia; T-ALL classical mediastinal mass + pleural effusion, CNS involvement, pancytopenia + = T-cell leukemia vs – = T-cell lymphoma; bone marrow smear images of large lymphoblasts; bottom Note on AML no fever & HTLV-1 adult T-cell lymphoma), ALL Prognostic Factors table (Good vs Bad: White vs Black, 2–9 yrs vs <1 or >10 yrs, Female vs Male, L1 vs L2/L3, absent vs present CNS/testes/HSM/lymphadenopathy/mediastinal mass, WBC <50,000 vs >50,000, CSF blasts absent vs present, Hyperdiploidy vs Hypodiploidy, t(12;21) vs t(9;22)/t(4;11)/t(1;19), NOTCH-1/HOX 11, Early pre B vs T cell), BFM-19 treatment protocol (1. Induction 2 cycles: steroids + vincristine + daunorubicin + cyclophosphamide; L-asparaginase not used now d/t widespread thrombosis; 2. Marrow MRD status: Negative → 3. Consolidation 2 cycles → 4. Maintenance methotrexate + 6-MP for 2–3 yrs; Positive → 3. 2 cycles chemo → 4. Transplant), and other drugs in ALL (Rituximab anti-CD20 in B-ALL; Blinatumomab bispecific anti-CD19/anti-CD3; Nelarabine for refractory T-ALL).

## Earlier release — Chapters 19 to 21 (Book p107–125)

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

1. Every printed page p1–263 is covered in book order from the scanned source (no text layer exists); headings, table cells, image labels, flowchart arms, thresholds and notes are represented. Page map: `01.pdf` PDF13 = p1 … PDF129 = p117, `02.pdf` PDF1 = p118 … PDF130 = p247 and `03.pdf` PDF1 = p248 … PDF16 = p263 so far; no requested sheets are missing.
2. `audit/coverage.json` holds **2,938 inventoried points** across Chapters 1–44; every ledger point resolves to exactly one question in question order and on the matching book page.
3. Four-option sets are unique, parallel in length/detail, and deterministically shuffled across all four positions (`A`–`D`). Matching items use 2- to 4-item bijections with varied permutations; true/false items have balanced 2 True / 2 False choices; numeric and fill-up questions use plausible clinical distractors; scenarios retain full clinical context.
4. IDs are sequential `MED-C<N>-<seq>`; the question array is strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, every unit guide is 2–4 lines, and every explanation ends with its exact `(Book pX)` citation matching the question page.
5. Chapters 1–44 are embedded in the standalone app with live flags set; **44/61 roadmap chapters are live**. See [audit/known-source-caveats.md](audit/known-source-caveats.md) for transcription and medical-source caveats.

## Verified PDF → printed-page map

Printed page numbers are ground truth. `uploads/01.pdf` is sequential after 12 unnumbered front-matter sheets (cover, author, title, instructions, 8 pages of combined Contents); `uploads/02.pdf` continues at Book p118; `uploads/03.pdf` continues at Book p248. Full mappings are in [audit/page-map.json](audit/page-map.json).

- `uploads/01.pdf` PDF13–129 = Book p1–117
- `uploads/02.pdf` PDF1–130  = Book p118–247
- `uploads/03.pdf` PDF1–128  = Book p248–375  (PDF129–131 are blank/end-quote matter)
- **PDF → Book formula:** `01.pdf: Book p = PDF page − 12`; `02.pdf: Book p = PDF page + 117`; `03.pdf: Book p = PDF page + 247`

Chapter sheet coverage source-reviewed through p263:

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
| 19 | 107–115 | 01.pdf PDF119–127 |
| 20 | 116–120 | 01.pdf PDF128–129 + 02.pdf PDF1–3 |
| 21 | 121–125 | 02.pdf PDF4–8 |
| 22 | 126–135 | 02.pdf PDF9–18 |
| 23 | 136–139 | 02.pdf PDF19–22 |
| 24 | 140–141 | 02.pdf PDF23–24 |
| 25 | 142–145 | 02.pdf PDF25–28 |
| 26 | 146–152 | 02.pdf PDF29–35 |
| 27 | 153–158 | 02.pdf PDF36–41 |
| 28 | 159–168 | 02.pdf PDF42–51 |
| 29 | 169–172 | 02.pdf PDF52–55 |
| 30 | 173–184 | 02.pdf PDF56–67 |
| 31 | 185–192 | 02.pdf PDF68–75 |
| 32 | 193–196 | 02.pdf PDF76–79 |
| 33 | 197–205 | 02.pdf PDF80–88 |
| 34 | 206–212 | 02.pdf PDF89–95 |
| 35 | 213–217 | 02.pdf PDF96–100 |
| 36 | 218–222 | 02.pdf PDF101–105 |
| 37 | 223–229 | 02.pdf PDF106–112 |
| 38 | 230–235 | 02.pdf PDF113–118 |
| 39 | 236–242 | 02.pdf PDF119–125 |
| 40 | 243–248 | 02.pdf PDF126–130; 03.pdf PDF1 |
| 41 | 249–252 | 03.pdf PDF2–5 |
| 42 | 253–256 | 03.pdf PDF6–9 |
| 43 | 257–259 | 03.pdf PDF10–12 |
| 44 | 260–263 | 03.pdf PDF13–16 |
| 45 (next) | 264 | 03.pdf PDF17 |

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
| 22 | Epidemiology of Acute Leukemia, Myeloid Precursor Lineages & AML Pathogenesis | 126 | MED-C22-01–MED-C22-11 | 11 |
| 22 | Hyperviscosity Note, 5-Point Hematological Diagnosis, AML Definition, Survival & Hereditary Risk Factors | 127 | MED-C22-12–MED-C22-21 | 10 |
| 22 | AML Risk Factors: Germline/Syndromic Predisposition, Down Syndrome, Environmental & Hematological Diseases | 128 | MED-C22-22–MED-C22-30 | 9 |
| 22 | Classification of AML: FAB Subtypes, WHO (2016) & WHO-5 (2023) Categories, and Recurrent Genetic Abnormalities | 129 | MED-C22-31–MED-C22-38 | 8 |
| 22 | Clinical Features of AML: Presenting Pancytopenia, Infections Note & Myeloid Sarcoma (Chloroma) | 130 | MED-C22-39–MED-C22-45 | 7 |
| 22 | Skin Involvement (Leukemia Cutis vs Sweet Syndrome), Blood Picture & Myeloblast vs Promyelocyte Morphology | 131 | MED-C22-46–MED-C22-52 | 7 |
| 22 | AML Cytology Stains, Immunophenotyping CD Markers, Cytogenetics, Molecular Mutations & European Risk Stratification | 132 | MED-C22-53–MED-C22-61 | 9 |
| 22 | Bad Prognostic Factors, Treatment Risk Groups, 7+3 Induction Regimen, Post-Induction Care & Targeted Agents | 133 | MED-C22-62–MED-C22-68 | 7 |
| 22 | Post-Induction Bone Marrow & MRD Evaluation, Consolidation Phase, Regimens in Unfit/Elderly, New Drugs & APML Intro | 134 | MED-C22-69–MED-C22-74 | 6 |
| 22 | APML (AML M3): DIC Pathogenesis, Hypergranular vs Hypogranular Types, Sanz Criteria & Differentiation Syndrome | 135 | MED-C22-75–MED-C22-81 | 7 |
| 23 | ALL Pathophysiology, Survival by Age, B-Cell vs T-Cell Lineage & Lymphoblast vs Myeloblast Morphology | 136 | MED-C23-01–MED-C23-10 | 10 |
| 23 | ALL Risk Factors, Presenting Features (B-ALL, T-ALL, High-Count Sanctuary Sites) & Laboratory Features | 137 | MED-C23-11–MED-C23-20 | 10 |
| 23 | B-Cell Subtypes (Pro-B, Pre-B, Early Pre-B CALLA, Immature B), B-ALL vs T-ALL Clinical Features & Smear Notes | 138 | MED-C23-21–MED-C23-29 | 9 |
| 23 | ALL Prognostic Factors Table, BFM-19 Treatment Protocol (Induction, MRD, Consolidation, Maintenance) & Other Drugs | 139 | MED-C23-30–MED-C23-40 | 11 |
| 24 | Initial Investigations, Common Lymphoid Progenitor Markers, Precursor B-Cell Maturation & CLL Origin | 140 | MED-C24-01–MED-C24-09 | 9 |
| 24 | Lymph Node Zones (Pre-Germinal, Germinal Centre, Post-Germinal/Marginal Zone), Myeloma Markers & CD Summary | 141 | MED-C24-10–MED-C24-21 | 12 |
| 25 | CLL Overview, Epidemiology, Defective Apoptosis Pathophysiology, Small Lymphocytic Leukemia (SLL) & Etiology | 142 | MED-C25-01–MED-C25-09 | 9 |
| 25 | CLL Investigations, Smudge Cells, Richter Transformation, Warm AIHA, Staging Table & Indications for Treatment | 143 | MED-C25-10–MED-C25-20 | 11 |
| 25 | CLL Prognostic Factors Table, FCR & BR Treatment Regimens, and Hairy Cell Leukemia Overview & Pathogenesis | 144 | MED-C25-21–MED-C25-28 | 8 |
| 25 | Hairy Cell Leukemia Investigations (Smear, Fried-Egg Marrow, Immunophenotype), Treatment & PAN Association | 145 | MED-C25-29–MED-C25-36 | 8 |
| 26 | Classification by Cell of Origin, Mature T-Cell Lymphomas (ALCL to Hepatosplenic) & Grade-Based Classification | 146 | MED-C26-01–MED-C26-08 | 8 |
| 26 | Causative Organisms Table (EBV 100/70/40/20 Rule, HIV, HCV, H. pylori, HHV-8, HTLV-1) & Ann-Arbor Staging | 147 | MED-C26-09–MED-C26-15 | 7 |
| 26 | NHL General Features, Mantle Cell Lymphoma (t(11;14), SOX-11, R-CHOP Resistance) & Follicular Lymphoma Genetics | 148 | MED-C26-16–MED-C26-22 | 7 |
| 26 | Follicular Lymphoma Histology/Course/Rx, Germinal Centre Malignancies Table & MALToma (t(11;18), H. pylori, Sjögren) | 149 | MED-C26-23–MED-C26-30 | 8 |
| 26 | High-Grade Lymphomas Overview, Clinical Features & Prognostic Factors, and Diffuse Large B-Cell Lymphoma (DLBCL) | 150 | MED-C26-31–MED-C26-36 | 6 |
| 26 | DLBCL Subtypes (GCB vs ABC-DLBCL), Double/Triple-Hit vs Double-Expressor Venn Diagram & R-CHOP Regimen | 151 | MED-C26-37–MED-C26-42 | 6 |
| 26 | DLBCL Interim-PET Flowchart & Burkitt's Lymphoma (c-myc Translocations, Endemic vs Sporadic, CODOX-M/IVAC, Starry Sky) | 152 | MED-C26-43–MED-C26-50 | 8 |
| 27 | Germinal-Centre Physiology Diagram, B-Cell Tumor Origin Table & NF-κB (NK-κβ) Pathogenesis | 153 | MED-C27-01–MED-C27-06 | 6 |
| 27 | Dark-Zone Origin & Chr 9 PDL1 Aberration, Stage Cure Rates, HL vs NHL Comparison Table & Pel-Ebstein Fever | 154 | MED-C27-07–MED-C27-13 | 7 |
| 27 | Reed-Sternberg Cell Morphology, NLPHD vs Classical HD Classification (Worldwide vs India) & Comparison Table | 155 | MED-C27-14–MED-C27-19 | 6 |
| 27 | EBV/ALCL Recap Notes, Hodgkin Clinical Features, Paraneoplastic Syndromes & NS vs MC Subtype Profiles | 156 | MED-C27-20–MED-C27-25 | 6 |
| 27 | Richter Recap, Staging Workup (Excision Biopsy & FDG-PET), Unfavourable Criteria & β2-Microglobulin Note | 157 | MED-C27-26–MED-C27-30 | 5 |
| 27 | Chemotherapy Response by Subtype, ABVD Toxicity Table, Deauville PET-Adapted Protocol, Brentuximab, BEACOPP & ISRT | 158 | MED-C27-31–MED-C27-37 | 7 |
| 28 | Normal Plasma Cell Morphology, Russell/Dutcher Bodies & Polyclonal vs Monoclonal Hypergammaglobulinemia | 159 | MED-C28-01–MED-C28-08 | 8 |
| 28 | Plasma Cell Disorder Classification, Myeloma Overview, Smear Variants (Mott/Flame), MGUS vs SMM vs MM & Slim-CRAB | 160 | MED-C28-09–MED-C28-16 | 8 |
| 28 | Myeloma Investigations (SPEP/UPEP, IFE, sFLC, ISS β2-M/Albumin, FISH, Whole-Body Low-Dose CT) & Therapeutics | 161 | MED-C28-17–MED-C28-24 | 8 |
| 28 | Bony & Renal Pathogenesis (DKK-1/RANK-L, Myeloma Kidney, Type II RTA, Amyloidosis) & Hypercalcemia / Infection Mechanisms | 162 | MED-C28-25–MED-C28-31 | 7 |
| 28 | Neuromyeloma Diagram, POEM Syndrome, Solitary Plasmacytoma, Poor Prognostic Factors & Waldenström Intro | 163 | MED-C28-32–MED-C28-37 | 6 |
| 28 | Waldenström's Macroglobulinemia: Chr 6q / MYD88 L265P Pathogenesis, Hyperviscosity, Cryoglobulins & Bing-Neel Syndrome | 164 | MED-C28-38–MED-C28-43 | 6 |
| 28 | POEMS Syndrome, Heavy Chain Diseases Table (Franklin's, Seligmann's, Mu) & Amyloidosis Definition/Types | 165 | MED-C28-44–MED-C28-47 | 4 |
| 28 | Primary AL vs Secondary AA vs Dialysis (Aβ2M) vs Familial/Senile ATTR Amyloidosis & Organ Overview | 166 | MED-C28-48–MED-C28-52 | 5 |
| 28 | Amyloidosis Organ Manifestations I: Renal, Cardiac (Restrictive CMP, Sparkle Sign, Digoxin) & Hepatic Bleeding Risk | 167 | MED-C28-53–MED-C28-57 | 5 |
| 28 | Amyloidosis Organ Manifestations II: Spleen/GI/ANS/CNS/Endocrine/Hemorrhagic Signs, Congo Red Biopsy & Rx | 168 | MED-C28-58–MED-C28-63 | 6 |

| 29 | Myeloid Progenitor Lineages, Thrombopoiesis (Early vs Late), Megakaryocyte Stages & Morphological Variants | 169 | MED-C29-01–MED-C29-08 | 8 |
| 29 | Platelet Counts, Lifespan, Sample Handling, Pseudothrombocytopenia & Platelet Transfusion (SDP vs RDP) | 170 | MED-C29-09–MED-C29-17 | 9 |
| 29 | Platelet Cascade I: Endothelial Antiplatelet/Anticoagulant/Fibrinolytic Roles, vWF Adhesion Receptors & Granules | 171 | MED-C29-18–MED-C29-25 | 8 |
| 29 | Clotting Cascade (Intrinsic, Extrinsic, Common), Fibrinolysis Checkpoints, Antifibrinolytics & aPTT/PT Tests | 172 | MED-C29-26–MED-C29-34 | 9 |
| 30 | Evaluation Protocol I: Platelet vs Coagulation Bleed Table, Lineage Chart, Count-Based Bleeding Risk & Drug-Induced Thrombocytopenia | 173 | MED-C30-01–MED-C30-08 | 8 |
| 30 | Evaluation Protocol II: Anticonvulsant/Gp IIb-IIIa/NSAID/Quinine/Penicillin Table, Hypersplenism, Smear & ITP Summary Flowchart | 174 | MED-C30-09–MED-C30-15 | 7 |
| 30 | Immune Thrombocytopenic Purpura I: Causes, Gp IIb/IIIa & Ib/IX Antibody Pathogenesis, Clinical Signs & Investigations | 175 | MED-C30-16–MED-C30-22 | 7 |
| 30 | ITP II: Features Inconsistent with ITP, Duration-Based Classification & First-Line Treatment (Steroids, IVIg/Anti-D) | 176 | MED-C30-23–MED-C30-29 | 7 |
| 30 | ITP III: Second-Line Therapy, Follow-Up & Qualitative Platelet Disorders (Causes, Defect Types, PFA-100 & Aggregation Test) | 177 | MED-C30-30–MED-C30-36 | 7 |
| 30 | Aggregation Curves (Biphasic vs Monophasic), Ristocetin Agglutination Test + aPTT Logic, Bleeding Time & vWF Functions | 178 | MED-C30-37–MED-C30-43 | 7 |
| 30 | Optical Density Traces: Aggregation Defect vs BSS/vWD vs Storage Pool (Granule) Defect Interpretation | 179 | MED-C30-44–MED-C30-48 | 5 |
| 30 | Glanzmann Thrombasthenia, Afibrinogenemia, Bernard-Soulier Syndrome, Megathrombocytosis & Drug-Induced Qualitative Bleeding | 180 | MED-C30-49–MED-C30-54 | 6 |
| 30 | Von Willebrand Disease I: vWF Gene/Structure Domains, ADAMTS13 Processing, Functions & Types | 181 | MED-C30-55–MED-C30-60 | 6 |
| 30 | Von Willebrand Disease II: Type 1 vs Type 3 Table, Type 2 Subtypes (2A/2B/2M/2N), Acquired vWF & Management | 182 | MED-C30-61–MED-C30-68 | 8 |
| 30 | DIC I: Clinical Approach by aPTT/PT/Platelet Combinations (Factor XII/XI/Hemophilia A & B/vWD/LAC/Liver/Warfarin) & Etiology | 183 | MED-C30-69–MED-C30-74 | 6 |
| 30 | DIC II: Pathogenesis Chain, ICU Monitoring, Purpura Fulminans, Investigations (FDP vs D-Dimer) & Management | 184 | MED-C30-75–MED-C30-81 | 7 |
| 31 | Gross Anatomy: Lobes, Oblique/Horizontal Fissures, Lower-Lobe Auscultation, Azygos Fissure 'Tadpole' & Phantom Tumor | 185 | MED-C31-01–MED-C31-06 | 6 |
| 31 | Phantom Tumor Resolution Films, Hilar Structures & Relations, Causes of Hilar Enlargement & Weibel's 23 Generations | 186 | MED-C31-07–MED-C31-12 | 6 |
| 31 | Bronchi Types, Right vs Left Bronchus Dimensions, Foreign-Body Predilection, Calibre/Area Change, Secondary Pulmonary Lobule & BPS Definition | 187 | MED-C31-13–MED-C31-19 | 7 |
| 31 | Bronchopulmonary Segments of Right and Left Lung (10 Each) & Position-Dependent Aspiration Segments | 188 | MED-C31-20–MED-C31-24 | 5 |
| 31 | Acinus Parts, Centriacinar (Smokers) vs Panacinar (α1-Antitrypsin) Emphysema & Basal/Goblet Cells of Conducting Airways | 188 | MED-C31-25–MED-C31-29 | 5 |
| 31 | Club (Clara) Cells, CGRP, Kulchitzky Cells, Cartilage/Smooth Muscle/Goblet Table, Epithelial Zonation & Airway Mediators | 189 | MED-C31-30–MED-C31-36 | 7 |
| 31 | Role of Cilia, Primary Ciliary Dyskinesia/Kartagener Triad, Nasal Nitric Oxide Gold Standard & Cystic Fibrosis (F508, Ivacaftor) | 190 | MED-C31-37–MED-C31-44 | 8 |
| 31 | Airway Resistance: Poiseuille/Ohm Laws, Generation 5–7 Resistance Peak, Reynolds Number Flow Table | 191 | MED-C31-45–MED-C31-50 | 6 |
| 31 | Alveolar Type I vs Type II Cells, Bleomycin Effect, Surfactant Function/Components/Synthesis & GM-CSF | 192 | MED-C31-51–MED-C31-59 | 9 |
| 32 | Tidal Volume, Boyle's Law, Three Pressures, Intrapleural Negativity & Intra-Alveolar Pressure Changes | 193 | MED-C32-01–MED-C32-07 | 7 |
| 32 | Transpulmonary Pressure Equations, TPP Trace Values, Intrapleural Fluid Cohesiveness, Pneumothorax Note & Static Compliance | 194 | MED-C32-08–MED-C32-15 | 8 |
| 32 | Hysteresis Loop, Surface Tension vs Elastic Recoil, Elastin/Collagen & Obstructive vs Restrictive Compliance Curves | 195 | MED-C32-16–MED-C32-22 | 7 |
| 32 | Dynamic Compliance (Only-Dynamic vs Static-and-Dynamic Falls) & Elastic Recoil Pressure of the Respiratory System at RV/FRC/TLC | 196 | MED-C32-23–MED-C32-30 | 8 |
| 33 | Lung Volumes and Capacities Tables (TV/IRV/ERV/RV with Male-Female Split; IC/FVC/FRC/TLC Formulas) & Volume-Time Graph | 197 | MED-C33-01–MED-C33-07 | 7 |
| 33 | Residual Volume Measurement (Plethysmography vs Obsolete Gas Methods), Spirometry Procedure/Disadvantage, FEV1/FVC & Obstructive-Restrictive-Vascular Disease Tree | 198 | MED-C33-08–MED-C33-14 | 7 |
| 33 | Obstructive Disease (Emphysema): Hyperinflation Phase I vs Air Trapping Phase II Table & Bronchodilator Reversibility Testing | 199 | MED-C33-15–MED-C33-21 | 7 |
| 33 | Restrictive Lung Disease: Diffusion vs Ventilation Indices, Intraparenchymal vs Extraparenchymal Types & Vascular Lung Disease | 200 | MED-C33-22–MED-C33-27 | 6 |
| 33 | Small Airway Disease (mmEFR, Closing Volume/Fowler) & Flow-Volume Curve Patterns (Normal, Mild, Severe Obstruction, Restriction) | 201 | MED-C33-28–MED-C33-33 | 6 |
| 33 | Upper Airway Obstruction Patterns (Extrathoracic/Intrathoracic/Fixed), Neuromuscular & Parenchymal Loops, and GOLD Staging | 202 | MED-C33-34–MED-C33-38 | 5 |
| 33 | DLCO: Definition, Normal Values, Alveolo-Capillary Membrane Layers, Advantages of CO, Procedure & Blood Volume Determinant | 203 | MED-C33-39–MED-C33-45 | 7 |
| 33 | Conditions Raising/Lowering DLCO, False-Low DLCO Causes, Diffuse Alveolar Hemorrhage & DLCO Across Respiratory Disorders | 204 | MED-C33-46–MED-C33-51 | 6 |
| 33 | Coefficient of Diffusion (Kco) & the Stepwise Approach to Evaluation of Lung Diseases Flowchart | 205 | MED-C33-52–MED-C33-57 | 6 |
| 34 | VTE Definition, Mortality, Thrombo-Embolic Pathogenesis, Origin of Thrombi, Acute Cor Pulmonale, Calf DVT & Massive VTE Pathogenesis Chain | 206 | MED-C34-01–MED-C34-08 | 8 |
| 34 | Presentation, D/d of Dyspnea with Clear Lung Fields, Golden 4 Assessment (Clinical, ECHO/McConnel Sign, Biomarkers, CTPA) & Submassive/Non-Massive VTE | 207 | MED-C34-09–MED-C34-17 | 9 |
| 34 | Non-Massive VTE Investigations & Complications, Genetic and Acquired Risk-Factor Lists, Malignancy/Nephrotic/Surgery Risks & Ventilation-Perfusion Physiology | 208 | MED-C34-18–MED-C34-24 | 7 |
| 34 | Dead-Space vs Shunt Physiology in PE, Symptoms/Signs, Vagal Bradycardia, Acute Cor Pulmonale Complications & Type I Respiratory Failure with A-a Gradient | 209 | MED-C34-25–MED-C34-32 | 8 |
| 34 | CXR Signs (Atelectatic Bands, Hampton's Hump, Pallas, Westermark, Fleischner), PAH Films & ECG Significance and Patterns (S1Q3T3) | 210 | MED-C34-33–MED-C34-39 | 7 |
| 34 | Pulmonary Angiography Gold Standard, V/Q Scan Indications, D-Dimer, ECHO, the Wells Score Table and CTPA Signs (Saddle Embolus, Polo Mint Sign) | 211 | MED-C34-40–MED-C34-46 | 7 |
| 34 | Management: Heparin/LMWH Dosing, Severity Determination, Thrombolysis vs Catheter Therapy, Heparin Target Ranges, 3-Month Switch and IVC Filter | 212 | MED-C34-47–MED-C34-53 | 7 |
| 35 | Ohm's Law Applied to the Pulmonary Circulation (PAP − LAP = CO × PVR), the Five WHO Classes, Class 1 PAH Features and the Class-to-Affected-Vessel Figure | 213 | MED-C35-01–MED-C35-08 | 8 |
| 35 | PAH vs Systemic HTN Mortality Logic, Definition (Mean PAP > 20 mmHg), Cor Pulmonale, Wood-Unit PVR Split, Plexiform Arteriolopathy & Secondary Causes (BMPR2 to Appetite Suppressants) | 214 | MED-C35-09–MED-C35-17 | 9 |
| 35 | Pathology Triad, Endothelin/NO/Prostacyclin Pathway Treatment Table, Clinical Presentation and the RV Dilatation and RV Failure Sign Chains | 215 | MED-C35-18–MED-C35-26 | 9 |
| 35 | PA Catheterisation Gold Standard, the Three PAH Murmurs (Carvallo, Ejection Systolic, Graham Steell), CXR Findings, PA Aneurysm Causes and ECG RVH Criteria | 216 | MED-C35-27–MED-C35-34 | 8 |
| 35 | Investigations to Exclude Other Causes (PFT, ECHO, V/Q, Sleep Study, HRCT, 6MWT), the Vaso-Reactivity Test, General Treatment and the NYHA-Stratified Drug and Surgical Table | 217 | MED-C35-35–MED-C35-42 | 8 |
| 36 | Definition (Irreversible Dilatation Plus Obliterative Bronchiolar Fibrosis), Pseudobronchiectasis, the Obstructive-Disease List, Pathogenesis Flowchart and the Normal-vs-Bronchiectasis Diagram | 218 | MED-C36-01–MED-C36-08 | 8 |
| 36 | Types of Dilatation (Cylindrical/Varicose/Cystic), Traction Bronchiectasis, Lobe/Sex/Age Distribution and the Four Histological Features | 219 | MED-C36-09–MED-C36-15 | 7 |
| 36 | Paediatric Aetiology (Post-Infective, Mounier-Kuhn, William Campbell, Kartagener, Young, Yellow Nail, α1-Antitrypsin), Impaired Mucociliary Clearance, McLeod, IgA Deficiency and Adult Aetiology | 220 | MED-C36-16–MED-C36-23 | 8 |
| 36 | Clinical Features (Three-Layered Sputum, Postural Cough, Haemoptysis Mechanism), Examination Findings, Sicca/ABPA Notes, Plain-Film Signs and the Three CT Criteria | 221 | MED-C36-24–MED-C36-32 | 9 |
| 36 | Complications (Cor Pulmonale, Massive Haemoptysis, Empyema, Amyloidosis, Abscess), Airway Clearance and CF Therapies, Surgery, Antibiotic Rationale, Macrolide Duration and the Infecting-Organism Hierarchy | 222 | MED-C36-33–MED-C36-40 | 8 |
| 37 | Disease Types, Pneumoconiosis Definition, the Dust-Particle Size/Site Table, the Four Pneumoconioses and Byssinosis (Organic Dust, Monday Fever) | 223 | MED-C37-01–MED-C37-07 | 7 |
| 37 | Silicosis: Industries, Crystalline vs Amorphous Silica, Parenchymal-Only Involvement, Malignancy/COPD Risk and the Acute-vs-Chronic Table (Exposure, Pathogenesis, Clinical Triangle, BAL, PFT, Prognosis) | 224 | MED-C37-08–MED-C37-15 | 8 |
| 37 | Radiology of Silicosis: Acute Crazy-Pavement CT Pattern and the Chronic Nodule-to-PMF Sequence with Egg-Shell Calcification and Upper Lobe ILD | 225 | MED-C37-16–MED-C37-21 | 6 |
| 37 | Crazy-Pavement Differential (DAH, AEP, PAP with Anti-GM-CSF), Coal Workers Pneumoconiosis, the CWP-vs-Silicosis Table and Caplan Syndrome | 226 | MED-C37-22–MED-C37-28 | 7 |
| 37 | Chronic Asbestosis: Fibre Types, Industries, Pleural Plaques (Candle Dripping, Holly Leaf), BAPE Fluid Criteria, Crow Feet Sign, Shaggy Heart Sign and Parenchymal Fibrosis | 227 | MED-C37-29–MED-C37-36 | 8 |
| 37 | Asbestos Malignancy: Lung Cancer vs Mesothelioma Table, Ferruginous Body, Berylliosis as Delayed Hypersensitivity with Non-Caseating Granulomas and the Granuloma Differential | 228 | MED-C37-37–MED-C37-43 | 7 |
| 37 | Berylliosis: Sarcoidosis Features That Are Absent, Industries, Upper Lobe ILD to PMF, Lymphocyte Proliferation Test, X-ray in 50% and the HRCT Triad | 229 | MED-C37-44–MED-C37-50 | 7 |
| 38 | Definition of Respiratory Failure, Hypoxemic/Hypercapnic Thresholds, the Partial-Pressure Abbreviation Box and the Type I Table (Diffusion Failure, CO Diffusion Potential, Etiology List Including the Asthma Exception) | 230 | MED-C38-01–MED-C38-08 | 8 |
| 38 | Type III (Parenchymal Damage) and Type IV (Shock) Rows, the Anaesthesiology 'Type-3' FRC Note, the V/Q Ratio Zones and the Dead-Space-vs-Shunt Table | 231 | MED-C38-09–MED-C38-15 | 7 |
| 38 | The Two Flowcharts: Hypoxemic Failure Branches (V/Q Mismatch, Shunt, Dead Space, Type II vs Type III, Oxygen-Responsiveness, High Altitude) and Hypercapnic Failure Branches | 232 | MED-C38-16–MED-C38-21 | 6 |
| 38 | ARDS Synonyms, the 1992 AECC Criteria, Limitations and Mortality, the Berlin 2012 Definition with PEEP and Severity Table and the Factors Preventing Pulmonary Edema | 233 | MED-C38-22–MED-C38-29 | 8 |
| 38 | ARDS Etiology (Primary and Secondary), the Toxin-to-Hyaline-Membrane Pathogenesis Chain, Alveolar Consequences and the Three Pathological Phases | 234 | MED-C38-30–MED-C38-36 | 7 |
| 38 | ARDS Clinical Features, Mechanical Ventilation Strategies, the VILI Table (Volume, Baro and Atelecto Trauma) and the Differential of Acute Breathlessness | 235 | MED-C38-37–MED-C38-42 | 6 |
| 39 | Interstitium and Its Types, Lung Parenchyma, TGF-β/PDGF Fibrosis, ILD Classification and the Seven Idiopathic Interstitial Pneumonias | 236 | MED-C39-01–MED-C39-08 | 8 |
| 39 | Autoimmune and Miscellaneous ILD (Occupational Lobes, Vasculitis, Inherited, Drug-Induced, LCH, LAM) with the UIP/NSIP/COP/LIP Important Points | 237 | MED-C39-09–MED-C39-16 | 8 |
| 39 | Clinical Features of ILD: Cardinal Symptoms, the Crackles-and-Clubbing Table versus Bronchiectasis, Skin Signs, Pulmonary HTN Prognosis and CXR | 238 | MED-C39-17–MED-C39-24 | 8 |
| 39 | PFT in Initial versus Advanced ILD, HRCT as Investigation of Choice and the UIP Pattern with Its Image Captions and New Antifibrotic Drugs | 239 | MED-C39-25–MED-C39-32 | 8 |
| 39 | NSIP Pattern and Its Treatment, Drugs Causing ILD, COP/BOOP with Halo Signs, and Cysts on HRCT (LAM, LCH, LIP) | 240 | MED-C39-33–MED-C39-41 | 9 |
| 39 | HRCT Finding–Disease Table, Nodular Shadows and Tree-in-Bud Notes with the Mosaic Attenuation and Lower-Lobe Infiltrate Captions | 241 | MED-C39-42–MED-C39-48 | 7 |
| 39 | Conditions with Upper-Lobe ILD, the LL Reticular Caption in IPF, and Pulmonary Alveolar Proteinosis (PAP) | 242 | MED-C39-49–MED-C39-55 | 7 |
| 40 | General Features of Asthma, the Bronchodilator Reversibility Box, GINA Features and Respiratory Symptoms with Triggers | 243 | MED-C40-01–MED-C40-08 | 8 |
| 40 | Etiopathogenesis: Triggers, Hygiene Hypothesis and TH2 Cytokines, Early versus Late Phases, and Eosinophil Mediators and Granules | 244 | MED-C40-09–MED-C40-16 | 8 |
| 40 | Histopathology of Asthma with Curschmann Spirals, the Extrinsic versus Intrinsic Table and Samter's Triad | 245 | MED-C40-17–MED-C40-24 | 8 |
| 40 | Mild versus Moderate versus Severe Asthma Table and Acute Severe Exacerbation versus Impending Respiratory Failure | 246 | MED-C40-25–MED-C40-31 | 7 |
| 40 | Management: Inhaled Corticosteroids as Mainstay, the ICS–Formoterol Step Protocol with Biologics, and Investigations | 247 | MED-C40-32–MED-C40-38 | 7 |
| 40 | Management of Asthma Exacerbation in the ER and Brittle Asthma Types One and Two | 248 | MED-C40-39–MED-C40-45 | 7 |
| 41 | Eosinophilic Lung Disease Defined, Its Three Defining Features, Known versus Unknown Causes and Diseases Not Classified under ELD | 249 | MED-C41-01–MED-C41-08 | 8 |
| 41 | Parasite-Related ELD (Loeffler Syndrome versus Lung Fluke Invasion), Drugs and Toxins, and Tropical Pulmonary Eosinophilia Pathogenesis | 250 | MED-C41-09–MED-C41-16 | 8 |
| 41 | Tropical Pulmonary Eosinophilia: Acute-on-Chronic Symptoms, Laboratory and Radiological Findings, DEC Treatment, and the Unknown-Cause Table Histories and Presentations | 251 | MED-C41-17–MED-C41-25 | 9 |
| 41 | Unknown Causes of ELD: Investigations in AEP, CEP and Idiopathic Hypereosinophilic Syndrome with Their Steroid Responses | 252 | MED-C41-26–MED-C41-33 | 8 |
| 42 | Aspergillus Microbiology and Its Four Lung Manifestations, with the ABPA Colonisation-to-Bronchiectasis Pathogenesis Flowchart | 253 | MED-C42-01–MED-C42-08 | 8 |
| 42 | Th2 Eosinophilic Inflammation, Central Proximal Bronchiectasis on Imaging, ABPA Clinical Features and the Upper-Lobe Fibrosis Causes (Rheumatology) | 254 | MED-C42-09–MED-C42-15 | 7 |
| 42 | Upper-Lobe Fibrosis Causes completed, ABPA Diagnostic Criteria with IgE, PFT Pattern and the Five Imaging Captions | 255 | MED-C42-16–MED-C42-22 | 7 |
| 42 | X-Ray Findings Unlikely or Against ABPA, the Steroid–Itraconazole–Omalizumab Treatment Flowchart and IgE Monitoring | 256 | MED-C42-23–MED-C42-29 | 7 |
| 43 | Extrinsic Allergic Alveolitis: Type IV over III Pathogenesis, Absent Type I Features, and the Twelve-Disease Etiology Table | 257 | MED-C43-01–MED-C43-09 | 9 |
| 43 | Acute, Subacute and Chronic Presentations, Complications, Non-Caseating Granuloma and Emphysema Notes, Precipitins and BAL CD8/CD4 | 258 | MED-C43-10–MED-C43-18 | 9 |
| 43 | PFT, CXR and CT in HP with the Head Cheese Pattern, Steroid Response versus Irreversible Fibrosis, and the HP versus ABPA Difference Table | 259 | MED-C43-19–MED-C43-27 | 9 |
| 44 | Pleural Anatomy and Fluid Composition, Detection Thresholds, and Light's Criteria with the Diuretic Disadvantage | 260 | MED-C44-01–MED-C44-09 | 9 |
| 44 | Transudative and Exudative Causes, Drugs Causing Effusion, TB Effusion Presentation and General Examination Signs | 261 | MED-C44-10–MED-C44-17 | 8 |
| 44 | Parapneumonic Effusion and Empyema, Low-pH Causes, and Chylothorax versus Pseudochylothorax | 262 | MED-C44-18–MED-C44-24 | 7 |
| 44 | Pleural Fluid Glucose, ICD Indications, Eosinophils in Pleural Fluid, and Tuberculous and Neoplastic Effusion Diagnosis | 263 | MED-C44-25–MED-C44-33 | 9 |

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
| 22 | Acute Leukemia | 126 | **Live** |
| 23 | Acute Myeloid Leukemia V/S Acute Lymphoblastic Leukemia | 136 | **Live** |
| 24 | World of Lymphomas | 140 | **Live** |
| 25 | Chronic Lymphocytic Leukemia | 142 | **Live** |
| 26 | Non-Hodgkin's Lymphoma | 146 | **Live** |
| 27 | Hodgkin's Disease | 153 | **Live** |
| 28 | Plasma Cell Disorders | 159 | **Live** |
| 29 | Platelets - Basics | 169 | **Live** |
| 30 | Approach to Bleeding Disorders | 173 | **Live** |
| 31 | Clinical Anatomy of Lungs | 185 | **Live** |
| 32 | Clinical Physiology of Lungs | 193 | **Live** |
| 33 | Pulmonary Function Tests | 197 | **Live** |
| 34 | Venous Thromboembolism | 206 | **Live** |
| 35 | Pulmonary Hypertension | 213 | **Live** |
| 36 | Bronchiectasis | 218 | **Live** |
| 37 | Occupational Lung Diseases | 223 | **Live** |
| 38 | Respiratory Failure and Acute Respiratory Distress Syndrome | 230 | **Live** |
| 39 | Interstitial Lung Disease | 236 | **Live** |
| 40 | Bronchial Asthma | 243 | **Live** |
| 41 | Pulmonary Eosinophilia | 249 | **Live** |
| 42 | Allergic Bronchopulmonary Aspergillosis | 253 | **Live** |
| 43 | Hypersensitivity Pneumonitis | 257 | **Live** |
| 44 | Pleural Effusion | 260 | **Live** |
| 45 | Obstructive Sleep Apnea Syndrome | 264 | **Live** |
| 46 | Chronic Obstructive Airway Disease | 267 | **Live** |
| 47 | Community Acquired Pneumonia | 274 | **Live** |
| 48 | Atypical Pneumonia and Pneumonia in Immunocompromised | 286 | **Live** |
| 49 | Cardiac Cycle With Heart Sounds | 296 | **Live** |
| 50 | Added Heart Sounds | 303 | **Live** |
| 51 | Aortic Stenosis | 307 | **Live** |
| 52 | Aortic Regurgitation | 313 | **Live** |
| 53 | Heart Failure | 318 | **Live** |
| 54 | Acute Decompensated Heart Failure | 326 | **Live** |
| 55 | Cardiomyopathy : Part 1 | 331 | **Live** |
| 56 | Cardiomyopathy : Part 2 | 336 | **Live** |
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

*Next up:* **Chapter 57 — Mitral Regurgitation (p346)** — render `uploads/03.pdf` PDF99 onward, audit in strict book order, and continue the same pipeline.