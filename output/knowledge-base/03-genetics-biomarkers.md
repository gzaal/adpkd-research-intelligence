# Genetics & Biomarkers in ADPKD

> **Last updated:** August 16, 2026
> **Status:** Living document, updated by automated research scans.

This document summarizes the current understanding of the genetic basis of ADPKD and the biomarkers used to track disease progression, predict risk, and guide treatment decisions. It is written to be accessible to a motivated patient while preserving the technical detail needed for informed decision-making.

---

## 1. Gene Variants: The Genetic Roots of ADPKD

ADPKD is caused by mutations in one of two genes. Which gene is affected -- and what kind of mutation it carries -- has a major influence on how the disease progresses.

### PKD1 (Chromosome 16)

- **Accounts for roughly 78% of all ADPKD cases.**
- The PKD1 gene encodes polycystin-1, a large protein involved in cell signaling and maintaining the structure of kidney tubules.
- Mutations in PKD1 generally lead to more severe disease and earlier onset than PKD2 mutations.

**Truncating vs. non-truncating mutations:**

- **Truncating mutations** (nonsense, frameshift, or large deletions that cut the protein short) are associated with the most severe disease course. Patients with PKD1 truncating mutations tend to reach end-stage kidney disease (ESKD) earliest.
- **Non-truncating mutations** (missense or in-frame changes that alter but do not destroy the protein) show highly variable severity. Some behave almost as mildly as PKD2 mutations; others track closer to the truncating group.

This distinction matters: two patients both carrying PKD1 mutations can have very different outlooks depending on the mutation type. (As of April 2026, genetic testing is increasingly recommended to refine prognosis.)

### PKD2 (Chromosome 4)

- **Accounts for roughly 15% of ADPKD cases.**
- Encodes polycystin-2, a calcium channel protein that works together with polycystin-1.
- PKD2 mutations generally produce a milder disease with later onset. Kidney function is often preserved into the fifth or sixth decade of life.

### The remaining ~7%

A small fraction of patients have no identifiable mutation in PKD1 or PKD2 with current testing methods. Some of these may carry deep intronic variants, mosaicism, or mutations in other genes that phenocopy ADPKD (such as GANAB, DNAJB11, or ALG8). Research into these rarer genetic causes is ongoing.

### Genotype-Phenotype Correlations

The relationship between genotype and disease trajectory has been studied extensively:

- **PKD1 truncating patients reach ESKD approximately 20 years earlier than PKD2 patients** on average. This is one of the most clinically significant genetic distinctions in all of nephrology.
- PKD1 non-truncating patients fall in between, though with wide individual variation.
- These population-level averages do not dictate any individual's course -- modifier genes, environment, blood pressure control, and treatment all play roles.

### PROPKD Score

The **PROPKD score** (developed by the Genkyst consortium) integrates genetic data with clinical features to produce a risk prediction:

- Inputs include: sex, presence of hypertension or urological events before age 35, and the type of PKD mutation (PKD1 truncating, PKD1 non-truncating, or PKD2).
- Scores range from 0 to 9. Higher scores predict faster progression to ESKD.
- The PROPKD score is used alongside imaging (see Section 5) to identify patients who are most likely to benefit from early treatment with tolvaptan.

### Variant-Specific Therapies: Toward Precision Medicine

A significant development in ADPKD research is the emergence of therapies that target specific types of mutations:

- **VX-407 (Vertex Pharmaceuticals)** is being developed as a PKD1 "corrector" -- a drug designed to rescue misfolded polycystin-1 protein in patients who carry specific PKD1 missense mutations. This is conceptually similar to how ivacaftor/lumacaftor transformed cystic fibrosis treatment. VX-407 is being evaluated in the AGLOW Phase 2 trial. If successful, it would mark the first true precision medicine approach in ADPKD, treating the root cause rather than downstream consequences. (As of April 2026, trial data are anticipated but not yet publicly reported.)

### RNA-Based Diagnostics

- **RNA sequencing (RNA-seq)** is being explored as a complementary diagnostic tool, particularly to resolve ambiguous cases where standard DNA sequencing is inconclusive. The Mario Negri Institute in Italy is conducting a study (ClinicalTrials.gov: NCT05996731) evaluating RNA-seq for ADPKD genetic diagnosis. This approach can detect splicing abnormalities and expression-level effects that DNA sequencing alone may miss.

### Optimizing NGS for ADPKD Genetic Diagnosis (Added May 2026)

Diagnostic genetic testing for ADPKD has historically been challenging because PKD1 has six homologous pseudogenes that confuse standard short-read sequencing alignments. A recent methodologic study (Genetics in Medicine, February 2026) on 203 CRISP patients quantified what an optimized exome sequencing (ES) pipeline can achieve:

- **95.5% of PKD1 pathogenic variants** detected with optimized ES.
- **100% of PKD2 variants** detected.
- Standard pipelines (with default GATK HardFiltering) miss at least 22 PKD1 variants due to pseudogene alignment artifacts.
- Higher-depth ES achieves 100% PKD1 detection.
- **Combined ES + genome sequencing (GS) solves 96% of well-phenotyped ADPKD cases.** GS additionally identified rare structural variants such as a balanced t(1;16)(q31.1;p13.3) translocation.

**Why this matters for patients:** If your initial genetic testing came back negative or inconclusive, ask whether the laboratory used an ADPKD-optimized pipeline (with appropriate read-depth and pseudogene handling). With current best practice, the proportion of ADPKD patients with no identified mutation should be much smaller than the historical "~7% no-mutation-found" figure suggests. As of mid-2026, leading diagnostic laboratories are transitioning from Sanger long-range PCR to optimized NGS for ADPKD.

### Long-read sequencing for cases that remain unsolved (Added May 2026)

Even with optimized short-read NGS, a small fraction of patients with strong clinical evidence of ADPKD have no identified PKD1/PKD2 variant. Some of these residual cases carry **structural variants** (large deletions, duplications, complex rearrangements, or balanced translocations) that short-read sequencing handles poorly. **PacBio HiFi long-read sequencing** is being explored as the next-step technology for these cases. A Yale group abstract (Tyagi, Somlo, Besse and colleagues, presented at the National Kidney Foundation Spring Clinical Meetings 2026) reports that HiFi long-read sequencing can recover hidden structural variants in PKD1 and PKD2 in ADPKD patients with previously unresolved diagnoses. Methods and full diagnostic yield are not yet published — this is an early signal, not a clinical-grade workflow.

### When genetic testing changes the diagnosis (Added May 2026)

Genetic testing also occasionally **reclassifies** apparent ADPKD as a different inherited kidney disease. A case from the same NKF SCM 2026 abstract series (G-531) describes a patient with a clinical PKD diagnosis and a family history of PKD whose genetic testing confirmed Alport syndrome rather than ADPKD. This is a single case, not a frequency estimate, but it reinforces the **KDIGO 2025 guidance** to consider genetic testing in cases with atypical presentation, ambiguous imaging, or features that do not fit the expected ADPKD course (e.g., proteinuria, hematuria with hearing loss, family members with markedly different phenotypes). A separate larger study in 270 kidney transplant candidates (Caliskan et al., Transplantation Direct, May 2026) reported a **38.5% diagnostic yield** with standardized genetic testing in patients evaluated for transplant — much of which would not have been captured by clinical phenotype alone.

### More PKD1 "Blind Spots" Found — and New Tools to Catch Them (Added August 2026)

This cycle added two more concrete examples of how PKD1 can be missed by standard genetic testing, plus a new tool aimed at the underlying problem:

- **A hidden "pseudoexon."** In one family, standard testing repeatedly came back negative despite a clear ADPKD picture. Combined genome and RNA sequencing eventually showed that two variants -- one inherited and individually harmless-looking, one newly arising -- combine to switch on a hidden, disease-causing piece of the PKD1 gene that isn't normally read by the cell (a "pseudoexon"). Neither variant alone would have been flagged as the cause. This is a single-family finding illustrating a mechanism, not an estimate of how often it happens.
- **A second family** with a similar exome-sequencing "miss": their PKD1 variant was only found using long-range PCR plus whole-genome sequencing, after standard exome sequencing failed -- the same pseudogene-homology problem described above, illustrated again.
- **A new alignment tool.** Researchers released an open-source tool (ParaDISM) specifically designed to reduce the false results that PKD1's pseudogene homology causes in standard sequencing pipelines, and showed improved performance on a small set of real ADPKD samples. This is a promising, but early and unreviewed, step toward the kind of "optimized pipeline" already described above -- it has not yet been shown to change diagnostic yield in an actual clinical lab.

**Bottom line, unchanged from May 2026:** if your genetic testing came back negative or inconclusive despite a clear ADPKD clinical picture, it is reasonable to ask whether the lab used an ADPKD-optimized pipeline, and whether escalation to long-read or genome+RNA sequencing has been considered.

### Cell-Biology Mechanism Roundup (Added August 2026)

Several preclinical papers this cycle add texture to *how* polycystin loss causes cysts, without changing anything actionable today. Briefly: (1) a large single-cell atlas across multiple mouse PKD models found the protein **osteopontin** consistently elevated, and removing it produced a modest improvement in cyst severity and kidney function in one mouse model; (2) deleting an enzyme called **OGT** substantially extended survival and reduced cyst formation in an aggressive mouse model -- a notably strong preclinical effect that, per this field's historically weak record of translating mouse results into human drugs, is worth watching rather than getting excited about yet; (3) two papers described specific molecular "switches" (a cilia protein called **ARL13B**, and a scaffolding protein called **Ezrin**) that appear to link the primary cilium to cyst growth through pathways separate from the classic polycystin-channel signaling story; (4) new lab tools -- a mouse strain that lets researchers directly visualize polycystin-2 protein in living tissue, and a systematic test of 29 different PKD1 disease-causing variants -- were published to help future researchers work faster. None of these are therapies; they are groundwork that may eventually inform which molecular pathway is worth targeting with a drug.

### Polycystin-1 Outside the Kidney: A Possible Explanation for ADPKD's Heart and Blood-Vessel Risk (Added August 16, 2026)

People with ADPKD have more cardiovascular problems than would be expected from their blood pressure and kidney function alone. A new study (Tardajos Ayllon et al., *Cardiovascular Research*, August 10, 2026) offers a candidate explanation. Working first in zebrafish, then in mice, then in human cells grown in the lab, the researchers found that polycystin-1 — the protein made by the **PKD1** gene — helps protect the cells lining blood vessels from dying. When they switched off *Pkd1* specifically in the blood-vessel lining of mice, atherosclerosis (fatty plaque build-up in arteries) got worse. In human aortic cells, knocking down PKD1 increased cell death and reduced **eNOS**, an enzyme that keeps blood vessels relaxed and healthy.

The most interesting detail: this effect was seen with **PKD1 loss but not PKD2 loss**. If that holds up in people, it would predict that patients with PKD1 mutations carry a different cardiovascular risk profile than patients with PKD2 mutations, independently of how their kidneys are doing. That comparison has not been made yet, and it is exactly the kind of question that existing genotyped patient cohorts could answer.

**What this does not mean.** This is entirely animal and cell-culture work. Nothing here changes how cardiovascular risk should be screened for or treated in ADPKD today, and it does not mean PKD1 patients should be managed differently. ADPKD has a long history of promising mouse findings that did not carry over to people. Treat this as a well-posed question, not an answer.

### Iron and Ferritin: A Useful Negative Result (Added August 16, 2026)

Iron handling has become a fashionable suspect across many kidney diseases, so it is worth reporting clearly when a careful test comes back empty. A mouse study (Sommer et al., *American Journal of Physiology — Renal Physiology*, August 9, 2026) confirmed that **ferritin** (the body's iron-storage protein) is genuinely mishandled in polycystic kidneys: it is elevated in the cells lining cysts and in immune cells, in both mouse and human kidney tissue, and infused ferritin piled up abnormally in PKD mouse kidneys but not in healthy ones.

But when the researchers directly tested whether this *causes* cysts to grow — by deleting the ferritin heavy chain gene in two different kidney cell types, and by infusing ferritin — **cyst growth did not change**. That is a negative result, and a useful one: it argues against ferritin itself being a promising drug target for slowing cyst growth, which saves future effort. Two caveats keep this from being the final word: deleting the heavy chain caused the cell to compensate by making more ferritin *light* chain, which could have hidden a real effect, and only two cell types were tested. Broader iron-driven oxidative stress and scarring may still play a secondary role.

*A note on how the paper is worded:* its abstract closes by saying disrupted iron trafficking "contributes to disease progression." That statement goes further than the paper's own experiments support, since every direct test of it was negative. We have logged the finding at low confidence accordingly.

### A New Mouse Model That Is Not PKD1 or PKD2 (Added August 16, 2026)

Deleting a gene called **Bicc1** in the kidneys of mice produces cystic disease that looks like ADPKD and activates the same cAMP and YAP signalling pathways (Gagnieux et al., *iScience*, August 3, 2026). Timing turned out to matter enormously: deleting *Bicc1* throughout the kidney tubules of adult mice produced only a few cysts over six months, whereas deleting it before birth in one specific part of the nephron produced aggressive disease. This gives researchers another model for studying the shared pathways that drive cyst growth, and is a reminder that developmental timing shapes mouse cystic phenotypes in ways that complicate the leap to adult-onset human ADPKD. No treatment implications.

---

## 2. Total Kidney Volume (TKV): The Primary Imaging Biomarker

Total kidney volume is the single most important biomarker for tracking ADPKD progression before kidney function declines.

### Why TKV Matters

In ADPKD, kidneys enlarge progressively as cysts grow -- often for years or decades before the GFR (a measure of filtering capacity) begins to drop. TKV captures this early structural damage and predicts future functional decline.

- **FDA-qualified as a prognostic enrichment biomarker** for use in clinical trials (as of 2024). This means the FDA accepts TKV as a valid way to select patients at high risk of progression for enrollment in drug trials.
- TKV is not yet accepted as a full surrogate endpoint for drug approval (i.e., a drug cannot be approved based solely on slowing TKV growth), but it is recognized as a "reasonably likely" surrogate, and the field is actively building the quantitative case for accelerated-approval decisions.

#### A Quantitative Framework Linking TKV to eGFR (CJASN, February 2026)

A new analysis by Yu et al. (*Clinical Journal of the American Society of Nephrology*, February 2026) used intraindividual mixed-effects modeling on the CRISP and HALT-PKD Study A registries to translate TKV growth rates into expected eGFR slope improvements within each Mayo Imaging Class. The result: within Mayo classes 1C–1E (the fast-progressing subgroups for whom tolvaptan was approved), each **1 percentage-point per year reduction in TKV growth rate corresponds to approximately 0.40–0.52 mL/min/1.73 m²/year slower eGFR decline**.

**Why this matters:** This is the first quantitative scaffold for asking, "How much TKV slowing must a new ADPKD drug deliver to plausibly translate into kidney-function benefit?" It directly informs go/no-go calls for the active Phase 2/3 pipeline (VX-407, ABBV-CLS-628, PYC-003, JMKX003142, farabursen Phase 2, CAM2029, tamibarotene) and provides regulators with a framework for accelerated-approval discussions.

**Limits of confidence:** The model is built on observational registry data, not randomized treatment effects. Generalizability to Mayo class 2 (atypical / non-PKD1), to very advanced 1E patients, and to drugs with non-cAMP mechanisms is not yet validated. **This is not yet an FDA decision**; it is a framework that may inform one.

### Measurement Standards

- **Height-adjusted TKV (htTKV)** is the standard measurement, expressed as mL/m. Adjusting for height accounts for the fact that taller people naturally have larger kidneys.
- **MRI** is the gold standard for TKV measurement due to its accuracy and reproducibility. No radiation is involved.
- **Ultrasound** remains widely used for initial diagnosis and screening (especially in families with known ADPKD), but is less precise for volume measurement.

### AI and Automated Measurement

Manual TKV measurement from MRI scans is time-consuming and requires trained radiologists to trace kidney boundaries on each image slice. This has been a barrier to wider adoption.

- **AI and deep learning methods for automated TKV measurement** are approaching clinical readiness. A systematic review published in the Journal of Clinical Medicine (2025) evaluated multiple deep learning approaches and found that several achieve accuracy comparable to expert manual segmentation.
- These tools could make TKV measurement faster, cheaper, and more widely available -- potentially extending its use beyond specialized centers.
- **TraceOrg automated kidney/liver/cyst volumetry (Sharbatdaran et al., JASN, May 2026):** A hybrid 3D U-Net + transformer model trained on 611 ADPKD plus 109 control MRI/CT scans, externally validated on the CRISP, PKD-RRC, and other independent datasets. The web tool reports kidney, liver, and cyst volumes plus Mayo Imaging Classification, with browser-side DICOM anonymization for privacy. **Why it matters:** this kind of deployed, externally-validated tool could broaden access to Mayo Imaging Classification in clinical settings without dedicated PACS-integrated software, helping more clinicians make tolvaptan eligibility decisions. **What it doesn't change:** segmentation accuracy varies by image quality; clinical workflow integration and regulatory clearance are still required for routine clinical use.

### Beyond TKV: Additional Imaging Biomarkers

A 2023 paper in the Journal of Clinical Medicine explored imaging biomarkers that go beyond simple total volume:

- **Cyst number and size distribution** -- may provide additional prognostic information, particularly in early-stage disease where TKV alone is less discriminating.
- **Cortical thickness** -- thinning of the kidney cortex (the outer functional tissue) may indicate more advanced damage.
- **Kidney parenchymal volume** -- the volume of functional tissue remaining, as opposed to cyst volume. This may better reflect residual kidney capacity.

These "beyond TKV" measures are research-stage (as of April 2026) but could refine risk prediction in the future.

### TKV Growth Rate and Treatment Response

A 2025 study in the Journal of Clinical Medicine examined whether baseline TKV growth rate predicts how well a patient will respond to tolvaptan. The finding that faster-growing kidneys may show a larger absolute benefit from treatment has implications for deciding when to initiate therapy.

### Renal Blood Flow (RBF): An Emerging Long-Term Predictor

A long-term secondary analysis of the HALT PKD Study A (Nowak et al., *Nephrology Dialysis Transplantation*, March 2026) provides new evidence that **renal blood flow (RBF)** — the rate at which blood flows through the kidneys — independently predicts progression to kidney failure over 13+ years:

- **Study:** 379 early-stage ADPKD patients from HALT PKD Study A, followed for a median of 13.1 years with outcomes linked to the US Renal Data System (USRDS).
- **Finding:** Patients in the lowest RBF tertile had a **3.19-fold higher risk** of reaching kidney failure compared to those in the highest RBF tertile (HR 3.19, 95% CI 1.05–9.67). This association held even after adjusting for eGFR and TKV.
- **Additional finding:** Lower RBF was associated with faster eGFR decline and higher odds of rapid kidney volume growth.

**What this means:** Cyst enlargement likely compresses the blood vessels supplying kidney tissue, reducing blood flow even before eGFR begins to drop. RBF may reflect this early compression effect and capture disease activity that TKV and eGFR together miss.

**Limitations:** RBF measurement requires phase-contrast MRI, which is not routinely available in all clinical centers. The CI is wide, and this was a secondary analysis. RBF is not currently used for routine clinical risk stratification. This finding is hypothesis-generating and may motivate future biomarker studies.

*Added April 12, 2026.*

---

## 3. eGFR Slope: Tracking Functional Decline

### What Is eGFR?

The estimated glomerular filtration rate (eGFR) measures how well the kidneys filter waste from the blood. It is calculated from a blood test (serum creatinine or cystatin C), adjusted for age, sex, and other factors.

- Normal eGFR is roughly 90-120 mL/min/1.73m2.
- ESKD is defined as eGFR below 15 mL/min/1.73m2 (or the need for dialysis/transplant).

### Why the Slope Matters More Than a Single Value

A single eGFR measurement is a snapshot -- influenced by hydration, diet, and day-to-day variation. The **eGFR slope** (the rate of change over time) is far more informative:

- It captures the trajectory of kidney function and is more sensitive to treatment effects than comparing individual time points.
- In clinical trials, the treatment effect on eGFR slope is now a key functional endpoint, often analyzed alongside TKV.
- Annual eGFR decline rates vary considerably:
  - **Mayo Class 1A-1B:** Slow decliners, often < 1 mL/min/year.
  - **Mayo Class 1C-1E:** Faster decliners, ranging from ~2.5 to > 5 mL/min/year.
  - **Genotype matters:** PKD1 truncating mutation carriers tend to have steeper eGFR slopes than PKD2 carriers.

### Clinical Use

eGFR slope is used alongside TKV and genetic information to build a comprehensive picture of an individual patient's trajectory. A steeper slope strengthens the case for early intervention.

### Is Creatinine-Based eGFR Always Measuring the Right Thing? (Added August 2026)

A cluster of findings this cycle raises a genuinely useful, if unsettled, question: is the everyday, creatinine-based eGFR blood test always a reliable way to measure a drug's effect on the kidneys in ADPKD trials?

**Why this comes up now.** The standard eGFR test estimates kidney function from the blood level of creatinine, a waste product mostly generated by muscle. Several independent observations this cycle point to the same concern:

- In the LIPS lanreotide trial (see 01-pharmacological-treatments.md and 04-clinical-trials-pipeline.md), a positive-looking result on the creatinine-based test did **not** hold up when the same patients were checked with two other methods (cystatin C, a different blood marker, and a urine-based measurement). This suggests the creatinine-based signal in that trial may not have reflected a true kidney-function difference.
- A not-yet-peer-reviewed perspective paper separately proposed that tolvaptan itself might change how much creatinine the body produces, which could make its measured benefit in the original TEMPO 3:4 trial look somewhat different than a muscle-independent test (cystatin C) would show. This is a hypothesis, not a demonstrated problem -- the authors have proposed, but not yet performed, a re-analysis of TEMPO 3:4 data using cystatin C.
- Separately, two studies found that simply switching between different eGFR calculation formulas (creatinine-only vs. combined creatinine-and-cystatin-C; older vs. newer "race-free" formulas) meaningfully shifts a patient's calculated eGFR and CKD stage in ADPKD cohorts -- with the combined creatinine-cystatin-C formula tracking a direct GFR measurement most closely in one study.

**What this does and doesn't mean.** None of these findings on their own changes anything about current ADPKD care -- creatinine-based eGFR remains the practical, validated standard used in every major guideline and trial to date, including the ones behind tolvaptan's approval. But taken together, they raise a fair scientific question about whether past and future ADPKD trials should routinely report a second, muscle-independent measure (cystatin C, or ideally a direct clearance test) alongside the standard eGFR, especially when a trial's result is close to the threshold of significance. **This is a "worth watching" item, not a reason to distrust your own eGFR results or any approved treatment.**

---

## 4. Serum Biomarkers: Blood-Based Indicators

While TKV and eGFR remain the primary tools, researchers are actively seeking blood-based biomarkers that could provide additional prognostic information or serve as easier-to-obtain surrogates.

### Copeptin

- **Copeptin** is a stable fragment of the vasopressin precursor protein. It serves as a surrogate marker for vasopressin (antidiuretic hormone) activity in the blood.
- Vasopressin drives cyst growth in ADPKD via the V2 receptor (the same target that tolvaptan blocks). Higher copeptin levels are associated with faster disease progression.
- Copeptin can be reduced by high water intake (which suppresses vasopressin release) -- this is the rationale behind water therapy in ADPKD.
- **Current status (April 2026):** Copeptin is primarily a research tool. It is not yet used in routine clinical decision-making but is measured in many clinical trials to assess vasopressin suppression.

### Serum Osmolality (Added May 2026)

A prospective Hong Kong study (Fung et al., *Kidney360*, February 2026, n=311 tolvaptan-naive ADPKD patients followed serially for 5 years) reported that **higher serum osmolality predicted faster eGFR decline**:

- Patients in the top quartile of serum osmolality had a hazard ratio of approximately 5.9 for a 40% eGFR decline compared to the bottom quartile.
- Serum osmolality had an AUC of 0.81 for predicting 40% eGFR decline.
- **Urine osmolality was not predictive** -- a notable finding given that urine osmolality is sometimes promoted as a self-monitoring tool.

**Important caveat -- this does not yet justify forced fluid intake:** The PREVENT-ADPKD water-intake RCT was historically negative for slowing TKV growth. An association between high serum osmolality and faster decline does not establish that lowering it (e.g., through high water intake) modifies disease trajectory. The mechanistic link (osmolality → vasopressin → cAMP → cyst growth) is plausible, and tolvaptan works on this pathway, but **drinking more water as a stand-alone intervention has not been shown to slow ADPKD progression in a controlled trial**. This finding is hypothesis-generating; it argues for continued prospective evaluation rather than a clinical recommendation today.

### Proteomics-Based Prediction Models

- Emerging research uses **proteomic profiling** (measuring hundreds of proteins simultaneously in blood or urine) to build predictive models for ADPKD progression.
- These multi-protein signatures may capture aspects of disease biology that single biomarkers miss -- including inflammation, fibrosis, and metabolic dysregulation.
- Still in the research phase; no validated proteomic panel is in clinical use for ADPKD as of April 2026.

### Where Do Serum Biomarkers Stand? GRADE-Rated Evidence Summary (Added June 2026)

A systematic review and meta-analysis spanning 58 studies (pm_42237252, published 2026) provides the most comprehensive GRADE-rated evidence synthesis to date across multiple proposed blood- and urine-based ADPKD biomarkers: NGAL (neutrophil gelatinase-associated lipocalin), MCP-1 (monocyte chemoattractant protein-1), VEGF, uromodulin (Tamm-Horsfall protein), KIM-1 (kidney injury molecule-1), and others.

**Key conclusions from the synthesis:**

- **No single serum or urine biomarker has yet accumulated sufficient evidence to warrant clinical integration** alongside TKV and eGFR slope as a routine decision-making tool in ADPKD management.
- Most biomarker studies in this field are small (often n < 50), cross-sectional, single-centre, and were not designed with prespecified kidney-failure outcome endpoints. GRADE-rated certainty is predominantly very low or low across the candidate markers.
- Candidates with the most supporting literature (NGAL, MCP-1) show associations with disease severity in cross-sectional analyses but have not been validated longitudinally against patient-important outcomes (kidney failure, eGFR slope over >5 years).
- Uromodulin and KIM-1 reflect tubular injury specifically and may correlate with disease stage, but no threshold values for clinical action have been established in ADPKD.

**What this means for patients:** If you or your nephrologist are wondering whether to order NGAL, MCP-1, or other "ADPKD biomarkers," the honest answer from the best available evidence is: these are research tools, not clinical-grade tests. TKV (from MRI) and serial eGFR remain the validated, actionable biomarkers for tracking progression and informing treatment decisions. Serum biomarker panels may become clinically useful once longitudinal, adequately powered, multi-centre validation studies are completed — but that gap has not been closed as of mid-2026.

**Research implications:** The SR/MA usefully quantifies *why* the gap persists: it is not that the markers are biologically implausible (many are), but that the study infrastructure to validate them against hard outcomes has not yet been built. Closing this gap will require collaborative biobanking linked to established cohorts (CRISP, HALT-PKD, Mayo registry) with long follow-up and pre-registered analysis plans.

### NOX4 and Oxidative Stress Biomarkers

- **NOX4** (NADPH oxidase 4) is an enzyme involved in generating reactive oxygen species. Oxidative stress is thought to contribute to cyst growth and kidney damage in ADPKD.
- Mayo Clinic is conducting a study (ClinicalTrials.gov: NCT04630613) investigating NOX4 and related biomarkers in ADPKD patients.
- Understanding the role of oxidative stress could open up new therapeutic targets.

### Nrf2 Response

- **Nrf2** (nuclear factor erythroid 2-related factor 2) is a master regulator of the body's antioxidant defense system.
- Mayo Clinic is also characterizing the Nrf2 response in ADPKD patients (ClinicalTrials.gov: NCT04344769), which may reveal whether impaired antioxidant responses contribute to disease progression.
- These studies are part of a broader effort to understand the metabolic and redox biology of ADPKD beyond cAMP signaling (the pathway targeted by tolvaptan).

---

## 5. Risk Scoring Systems: Putting It All Together

No single biomarker tells the whole story. Risk scoring systems combine multiple data points to predict an individual patient's likelihood of rapid progression.

### Mayo Clinic Imaging Classification (Classes 1A through 1E)

This is the most widely used risk classification system in ADPKD:

- **Based on:** height-adjusted TKV (htTKV) plotted against the patient's age.
- **Classes:**
  - **1A:** Lowest risk. Slow kidney growth rate (~1.5%/year). Many patients in this class will retain adequate kidney function throughout life.
  - **1B:** Low-moderate risk (~3%/year growth).
  - **1C:** Moderate risk (~4.5%/year growth). This is often the threshold where clinicians begin discussing tolvaptan.
  - **1D:** High risk (~6%/year growth).
  - **1E:** Highest risk (~>6%/year growth). Patients in this class are most likely to reach ESKD and are strong candidates for treatment.
- A patient with large kidneys for their age is classified as higher risk than a patient of the same age with smaller kidneys.
- The classification requires an MRI or CT scan for accurate TKV measurement.

### PROPKD Score

As described in Section 1, the PROPKD score adds genetic and early clinical data to the risk picture:

- **Score 0-3:** Low risk of progression.
- **Score 4-6:** Intermediate risk.
- **Score 7-9:** High risk.

### How Scoring Systems Guide Treatment

These tools are used together -- particularly to identify patients who stand to benefit most from tolvaptan, which carries a significant side effect burden (massive water intake requirement, polyuria, and liver monitoring):

- A patient classified as Mayo 1C-1E **and/or** with a high PROPKD score has the strongest evidence base for early tolvaptan initiation.
- A Mayo 1A patient with a low PROPKD score may be managed with conservative measures (blood pressure control, hydration, dietary optimization) and monitored with serial imaging.
- The 2025 KDIGO guideline incorporates these risk stratification tools into its treatment recommendations.

### New: Multivariable Kidney Failure Prediction in Early ADPKD (Ravichandran et al., JASN, May 2026)

A new prediction model published in May 2026 represents the largest externally-validated effort yet to forecast kidney failure (defined as eGFR < 15 mL/min/1.73 m², dialysis, or transplant) in early-stage ADPKD.

- **Development cohort:** 759 patients pooled from CRISP and HALT-A (baseline eGFR ~91 mL/min/1.73 m²), with median follow-up of 10.2 years.
- **Predictors:** age, sex, eGFR, ADPKD genotype, and Mayo Imaging Class.
- **External validation:** Mayo ADPKD clinical registry, ages 15–49 with eGFR ≥ 60.
- **Result:** good discrimination and calibration over a 15-year prediction horizon.

**What this changes:** This model could refine tolvaptan eligibility, trial enrichment, and patient counseling beyond Mayo Imaging Class alone -- particularly for early-stage patients where existing tools (Mayo Imaging Class, PROPKD score) are weakest.

**What it does not yet establish:** The external validation cohort was restricted to ages 15–49 with preserved eGFR (≥ 60), so generalizability to older patients, advanced disease, and non-Caucasian populations remains to be demonstrated. Calibration drift in non-research settings (where data quality and case mix differ) has not been tested. Independent replication in non-CRISP cohorts is still needed before this becomes routine clinical practice.

### Mayo Prognostic Tool: First External Validation Outside Its Original Population (Added August 2026)

A preprint posted in August 2026 provides the first known test of the Mayo Clinic's HtTKV-and-age-based prognostic tool (which predicts future eGFR) in a population outside the mostly-European/North-American cohorts it was originally built from: 50 ADPKD patients in Malaysia. Over 24 months of follow-up, the tool's predicted eGFR values correlated strongly with patients' actual measured eGFR, and agreement was high by a standard statistical test (Bland-Altman P30 > 90%, meaning over 90% of predictions were within 30% of the true value).

**Why this matters:** Prognostic tools are often developed and validated in a narrow set of populations, and it is not automatic that they will work equally well elsewhere. This is reassuring early evidence that the Mayo tool's predictions may generalize to a Southeast Asian population that was not part of its original development. **Caveats:** this is a preprint (not yet peer-reviewed), a single small cohort (n=50), and it validates the tool's ability to predict a surrogate measure (eGFR) rather than a hard outcome like kidney failure itself.

A companion review (Kidney360, August 2026) usefully maps where the field of ADPKD prognostication is headed: current tools fall into two families -- imaging-based (Mayo Classification, TKV) and genetic (PROPKD) -- and each loses accuracy in different situations (imaging tools lose resolution once fibrosis, not just cyst growth, dominates in advanced disease; genetic scores can underestimate risk in family members who progress unusually fast). The likely future direction is combining imaging, genetics, AI-derived image features, and blood/urine biomarkers into a single multimodal score -- though no such tool exists yet in validated form.

### Risk Prediction in Advanced Disease: TKV + KFRE (KI Reports, March 2026)

A complementary validation study (KI Reports, March 2026) examined the **Kidney Failure Risk Equation (KFRE)** in ADPKD patients with eGFR < 60. The KFRE was originally developed for general CKD and predicts kidney failure based on age, sex, eGFR, and urinary albumin/creatinine ratio.

- In ADPKD patients with eGFR < 60, **adding KFRE to Mayo Imaging Class improved 1-year discrimination** (ΔC up to 0.47).
- This addresses the gap that Mayo Imaging Classification alone has for advanced-disease patients, where TKV growth rate is less informative because cysts have already done much of their damage.

**Putting the risk-prediction toolkit together (as of May 2026):**
1. **Mayo Imaging Classification** -- best for early disease, htTKV-vs-age based.
2. **PROPKD score** -- adds genetics and early clinical events.
3. **Ravichandran model** -- early-disease external validation, pulls together genetics + Mayo class + clinical variables.
4. **TKV + KFRE** -- adds discrimination in advanced disease (eGFR < 60).

These tools are complementary, not interchangeable. Discuss with your nephrologist which is most relevant for your stage of disease.

---

## 6. Imaging Advances: Seeing the Disease More Clearly

### MRI-Based TKV: The Gold Standard

MRI remains the most accurate and reproducible method for measuring kidney and cyst volume. It involves no ionizing radiation, making it suitable for repeated measurements over time.

### AI-Assisted Cyst Segmentation

Beyond total volume, researchers are developing AI methods to automatically identify and measure individual cysts within the kidney:

- This enables tracking cyst number, size distribution, and growth patterns over time.
- May identify "dominant cysts" that contribute disproportionately to kidney enlargement.
- Could support more granular assessment of treatment response (e.g., does a drug slow growth of all cysts equally, or primarily affect certain sizes?).
- Multiple deep learning architectures have been published, with several achieving near-expert-level accuracy (systematic review, JCM 2025).

### Sodium-23 MRI: Functional Imaging

- **Sodium-23 MRI** is an advanced technique that maps sodium concentration within the kidney, providing information about tubular function that conventional MRI cannot.
- A study at an academic center is evaluating this approach in ADPKD (ClinicalTrials.gov: NCT05014178).
- Sodium-23 MRI could reveal early functional changes in kidney tissue before volume changes become apparent -- potentially identifying disease activity even earlier than TKV.
- This technique requires specialized MRI hardware and is currently limited to research settings.

**New evidence (August 2026) -- cyst phenotyping by sodium content:** A preprint using high-field (7-Tesla) sodium MRI in 20 ADPKD patients classified 2,299 individual cysts into two distinct types based on their sodium concentration: "high-sodium" cysts (resembling the proximal tubule, where filtration begins) and "low-sodium" cysts (resembling the collecting duct, where urine is finally concentrated). Strikingly, the vasopressin V2 receptor -- the exact target of tolvaptan -- was found *only* in the low-sodium, collecting-duct-type cysts, which made up a highly variable share of each patient's total cysts (anywhere from about 5% to 84%). If this holds up, it raises an intriguing possibility: patients (or even individual cysts within a patient) might differ in how "tolvaptan-responsive" they are, based on this sodium/cyst-type signature. This is early-stage and exploratory -- a preprint, not yet peer-reviewed, based on only 20 patients, with no data yet linking the sodium phenotype to actual treatment response. It is not a tool patients or clinicians can use today, but it is a genuinely novel imaging concept worth tracking.

### Ultrasound

- Ultrasound remains the first-line imaging tool for ADPKD diagnosis, particularly for screening at-risk family members.
- The Ravine criteria (ultrasound-based diagnostic criteria accounting for patient age and number of cysts) are well established.
- Limitations: less precise for volume quantification, operator-dependent, and can miss small cysts in early disease.
- For clinical trial enrollment and risk classification, MRI is preferred.

---

## Key Takeaways for Patients

1. **Genetic testing is increasingly valuable.** Knowing whether you carry a PKD1 truncating, PKD1 non-truncating, or PKD2 mutation meaningfully changes your prognosis and may influence treatment decisions. Ask your nephrologist whether genetic testing is appropriate for your situation.

2. **TKV is your most important early biomarker.** Even if your eGFR is still normal, a rising TKV (especially if you are classified as Mayo 1C or higher) indicates that disease is progressing and treatment may be warranted.

3. **Risk scores are tools, not destiny.** The Mayo Classification and PROPKD score are population-level predictions. Individual outcomes depend on many factors, including blood pressure control, lifestyle, and treatment.

4. **Precision medicine is coming.** VX-407 represents a new class of therapy aimed at correcting specific mutations rather than treating symptoms. If this approach succeeds, genetic testing will become essential for matching patients to targeted therapies.

5. **New biomarkers are in development.** Copeptin, proteomic panels, and oxidative stress markers may eventually allow more precise tracking of disease activity and treatment response beyond what TKV and eGFR can show.

6. **AI is making imaging faster and more accessible.** Automated TKV measurement could bring precise risk classification to more patients at more centers.

---

## Glossary

| Term | Plain-Language Meaning |
|------|----------------------|
| **eGFR** | Estimated glomerular filtration rate -- a blood-test-based measure of how well your kidneys filter waste. |
| **ESKD** | End-stage kidney disease -- when kidneys can no longer sustain life without dialysis or transplant. |
| **htTKV** | Height-adjusted total kidney volume -- kidney size normalized for your height, in mL per meter. |
| **Genotype** | Your specific genetic makeup (which gene is mutated, and how). |
| **Phenotype** | How the disease actually manifests in your body (severity, timing, symptoms). |
| **Truncating mutation** | A mutation that causes the protein to be cut short, usually producing no functional protein. |
| **Non-truncating mutation** | A mutation that changes the protein but does not cut it short -- effects are variable. |
| **Copeptin** | A blood marker that reflects vasopressin (antidiuretic hormone) levels. |
| **Nrf2** | A protein that activates the body's antioxidant defense genes. |
| **NOX4** | An enzyme that produces reactive oxygen species; part of the oxidative stress pathway. |
| **Polycystin-1 / Polycystin-2** | The proteins encoded by PKD1 and PKD2, respectively. They form a complex that helps kidney cells sense fluid flow. |
| **PROPKD score** | A risk score combining genetic and clinical data to predict ADPKD progression (range 0-9). |

---

## References and Trial IDs

For readers who want to look up specific trials mentioned in this document:

- **VX-407 / AGLOW trial:** Search ClinicalTrials.gov for Vertex Pharmaceuticals ADPKD studies.
- **RNA-seq diagnostics (Mario Negri Institute):** NCT05996731
- **NOX4 biomarker study (Mayo Clinic):** NCT04630613
- **Nrf2 characterization (Mayo Clinic):** NCT04344769
- **Sodium-23 MRI study:** NCT05014178

---

*This is a living document maintained by an automated research intelligence system. It is updated as new studies are published and trials report results. It is intended for informational purposes and does not constitute medical advice. Always discuss your individual situation with your nephrologist or clinical genetics team.*

*Last updated: August 16, 2026*
