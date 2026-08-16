# ADPKD Research Digest — Week 31, 2026
*Catch-up edition covering scan windows 2026-05-30 through 2026-07-30 | Deep Analysis, August 2, 2026*

---

> **Week framing — read this first.** The deep-analysis pipeline did not run for approximately seven weeks after the last digest (Week 24, June 8–14). Scanning continued and correctly queued 89 papers as `pending_synthesis`/`new`, but none were synthesized into findings or a digest until now. This edition is a single consolidated catch-up covering that entire gap, not one week. Freshness labels below reflect each item's *publication* date, not this digest's date — several items are 6–8 weeks old and are labeled accordingly. **Two items meet the dual alert threshold (importance ≥7 AND evidence ≥5): the LIPS lanreotide RCT and the CAM2029 polycystic-liver-disease trial readout.** Both are negative-to-marginal results, not breakthroughs, and should be read that way. A backlog of 267 low-relevance baseline papers (April 2026, relevance scores mostly 2–5) remains unincorporated; these are stale tracker noise, not this week's news, and are intentionally excluded from this digest (see Data Summary).

---

## Highlights

*(Selected for decision usefulness or genuine pipeline novelty — not because anything here is exciting. None of the three below should be read as a reason to change practice today, except the lanreotide result, which should.)*

### 1. LIPS trial: lanreotide fails its primary endpoint in a 3-year measured-GFR RCT — a second somatostatin analogue now negative on kidney function

- **What happened:** The LIPS trial (NCT02127437), a randomized, double-blind, placebo-controlled 3-year trial of monthly lanreotide 120mg in 144 adults with stage 2/3 ADPKD, is now fully published. The primary endpoint — iohexol-*measured* GFR slope — was negative (annualized between-arm difference −0.3 mL/min/1.73m²/yr, 95% CI −3.4 to 2.8). A significant creatinine-based eGFR signal (+1.2, 95% CI 0.27–2.15) was **not** reproduced by cystatin C-eGFR or urinary creatinine clearance. A new hypoglycemia signal emerged (11.1% lanreotide vs 1.4% placebo).
- **Why people may care:** This uses measured GFR — a stronger endpoint than eGFR — and is the second independent RCT-grade negative kidney-function result for a somatostatin analogue (after octreotide LAR, finding_019). Two different drugs in the same class have now failed to show kidney-function benefit despite volumetric surrogate reductions elsewhere in the literature. It further prunes somatostatin analogues from the ADPKD kidney disease-modifying space.
- **What limits confidence:** Enrollment stopped early (144 of 180 planned) due to slow recruitment, widening the confidence interval so it cannot exclude a modest effect either way; the trial completed in 2019 and is only now published (a publication event, not a new scientific event, though the *data* are new to this tracker); results apply only to adults with mGFR 30–89 mL/min/1.73m².
- **Classification:** practice-relevant (negative)
- **Scores:** Importance 8/10 | Evidence 8/10 | Novelty 7/10 | Decision 9/10 | Calibration 9/10

### 2. CAM2029 (octreotide depot) Phase 2/3 posts a marginal positive liver-volume result in PLD — read the fine print

- **What happened:** NCT05281328 (Camurus, CAM2029 subcutaneous octreotide depot vs placebo, polycystic **liver** disease) posted results: height-adjusted total liver volume fell −0.7% on treatment vs rose +3.9% on placebo at Week 53, an estimated relative treatment difference of −4.3% (95% CI −8.4 to −0.1, p=0.0443). All 13 secondary endpoints (including htTKV and eGFR) remain unpopulated. Serious adverse events occurred in 2/24 (QW) and 3/23 (Q2W, including one death) vs 5/23 placebo.
- **Why people may care:** This is the only genuinely new *trial results* event (as opposed to a paper publication) in the entire catch-up window, and the somatostatin-analogue class is under active scrutiny this cycle (see Highlight 1). It is a polycystic **liver** disease endpoint, not kidney, and should not be read across.
- **What limits confidence:** The primary-endpoint p-value (0.0443) is barely below the conventional threshold and is driven substantially by placebo-arm liver growth rather than treatment-arm shrinkage — a fragile way to reach significance; a death occurred as an SAE in the treatment arm; all kidney-relevant secondary endpoints and quality-of-life data are still unreported; this is a registry posting, not yet peer-reviewed.
- **Classification:** pipeline-relevant (trial readout, PLD not kidney)
- **Scores:** Importance 5/10 | Evidence 4/10 | Novelty 7/10 | Decision 4/10 | Calibration 6/10

### 3. PKD1 upstream open reading frames identified as a druggable brake on Polycystin-1 dosage

- **What happened:** A JCI paper identified conserved, actively-translated upstream open reading frames (uORFs) in the PKD1 5′UTR that suppress downstream Polycystin-1 (PC1) translation. Removing the uORF start codons, or blocking them with steric antisense oligonucleotides (ASOs), raised PC1 protein 2–4-fold and prevented kidney cysts in humanized mouse models (Dnajb11 and Pkd1-missense backgrounds).
- **Why people may care:** This is a mechanistically new, genuinely first-disclosure route to raising PC1 expression from the remaining functional allele — a long-standing therapeutic goal for PKD1-haploinsufficiency ADPKD — without gene replacement, and it adds an ASO modality to an already-diversifying polycystin-restoration pipeline (mRNA-LNP, CRISPRa, small-molecule correctors).
- **What limits confidence:** All efficacy data are from mouse models and in-vitro ASO experiments; no human dosing, delivery, or safety data exist; ADPKD has a historically weak preclinical-to-clinical translation record, so this should raise research priority, not clinical confidence.
- **Classification:** hypothesis-generating (pipeline-adjacent, early)
- **Scores:** Importance 6/10 | Evidence 4/10 | Novelty 8/10 | Decision 3/10 | Calibration 7/10

---

## New Papers — By Dimension

*49 of 89 incorporated papers scored relevance ≥4 and receive full treatment below. The remaining 40 (relevance 1–3 — mostly case reports, correction notices, narrative reviews, and ARPKD-only items) are listed compactly in "Lower-Priority / Maintenance Items" — nothing is silently dropped.*

### Pharmacological / Trials

**pm_42320793 — LIPS lanreotide RCT** [practice-relevant] — See Highlight 1. Scores: Imp 8 | Ev 8 | Nov 7 | Dec 9 | Cal 9.

**pm_42476150 — Network meta-analysis: octreotide, lanreotide, pasireotide + FAERS** [background/context]
Octreotide and pasireotide reduce TKV at 6–12 months; lanreotide reduces TLV growth beyond 2 years; cholelithiasis is the dominant biliary toxicity across all three. **Limits:** sparse network built on few small trials, all endpoints are volumetric/eGFR surrogates, FAERS spontaneous reports have no denominator. Scores: Imp 4 | Ev 3 | Nov 8 | Dec 3 | Cal 5.

**ppr_1279948 — "Questioning the kidney-protective effects of tolvaptan" (perspective preprint)** [hypothesis-generating]
Hypothesizes that creatinine-generation changes may inflate tolvaptan's apparent creatinine-eGFR benefit while informative censoring attenuates it in TEMPO 3:4; proposes an unperformed cystatin C reanalysis. Converges with Highlight 1's creatinine/cystatin C discordance — see finding_028. **Limits:** no new data, not peer-reviewed, does not demonstrate tolvaptan's benefit is overstated. Scores: Imp 5 | Ev 2 | Nov 7 | Dec 3 | Cal 7.

**pm_42398811 — GLP-1 receptor agonists in ADPKD (translational review)** [background/context]
Synthesizes rationale for GLP-1RAs including semaglutide mouse data and the tracked tirzepatide trial (NCT06582875). No new primary data. **Limits:** narrative review; authors themselves note causal evidence is incomplete. Scores: Imp 5 | Ev 2 | Nov 7 | Dec 4 | Cal 8.

**pm_42518289 — PKD1 uORFs / antisense oligonucleotides** [hypothesis-generating] — See Highlight 3. Scores: Imp 6 | Ev 4 | Nov 8 | Dec 3 | Cal 7.

**ppr_1282997 — Combination siRNA (TMEM16A + MCP-1) nanoparticle delivery** [hypothesis-generating]
Collecting-duct-targeted peptide-micelle co-delivery of TMEM16A and MCP-1 siRNA reduced kidney enlargement, cyst burden, tubular injury and macrophage infiltration in Pkd1-deficient mice, with added efficacy over single-target delivery, plus target engagement in ADPKD patient-derived cells in vitro. **Limits:** unreviewed preprint, mouse-only efficacy, no long-term safety/PK data, "effective therapeutic strategy" framing overstates what mouse data support. Scores: Imp 5 | Ev 3 | Nov 8 | Dec 3 | Cal 6.

**ppr_1246945 — Collecting-duct LNP Pkd2-mRNA (re-indexed, extends tracked work)** [hypothesis-generating / stale-duplicate]
Same June 5 2026 publication already captured in finding_004 as of the June 7 digest cycle; newly adds that a single dose also reduces cyst burden in Pkd1-deficient mice. **Treat the underlying result as NOT new; treat the Pkd1-model extension as the only new detail.** Scores: Imp 6 | Ev 3 | Nov 7 | Dec 3 | Cal 6.

**ppr_1239348 — CRISPRa activation of endogenous PKD1 (re-indexed, extends tracked work)** [hypothesis-generating / stale-duplicate]
Same May 25 2026 organoid-CRISPRa work already tracked; newly adds human ADPKD-patient-derived cell data with an inconsistent response across donors. **The heterogeneous human-donor response is a caveat, not an advance.** Scores: Imp 5 | Ev 3 | Nov 6 | Dec 3 | Cal 6.

**ss_34ea48af1ab97d9245c71adfea1711ca085e68dc — Tolvaptan in rapidly progressing ADPKD (China, single-arm)** — Prospective single-arm tolvaptan study in rapidly progressing ADPKD, Chinese single center. [hypothesis-generating] **Limits:** no comparator, single center, unusual venue (Translational Andrology and Urology), stale (indexed >14 days post-publication). Scores: Imp 4 | Ev 3 | Nov 2 | Dec 2 | Cal 7.

**pm_42445794 — Ketogenic metabolic therapy + exogenous ketones/citrate case series (n=4)** [hypothesis-generating — flagged]
See Skepticism Notes #1. Scores: Imp 3 | Ev 1 | Nov 5 | Dec 2 | **Cal 3**.

**pm_42347886 — Tolvaptan and inflammatory markers (retrospective, n=67)** [hypothesis-generating — flagged]
Blood-count-derived inflammation indices fell on tolvaptan vs rose untreated over 24 months. **Limits:** severe confounding by indication (treated patients younger, larger kidneys at baseline), small n, non-randomized, NLR/PLR/SII are crude non-specific surrogates. Scores: Imp 3 | Ev 2 | Nov 5 | Dec 2 | Cal 7.

**ss_50659a3cada6c7536d453c6066a6384aa796f670 — Ivermectin ameliorates cyst progression (PKD rat model)** [hypothesis-generating] — Preclinical rat study; FXR/TMEM16A mechanism proposed. **Limits:** unclear PKD subtype, obscure venue, no date, weak preclinical translation record. Scores: Imp 3 | Ev 2 | Nov 5 | Dec 2 | Cal 5.

### Genetics / Mechanism

**pm_42378035 — Cilia-to-basement-membrane signaling (JCI)** [hypothesis-generating]
PC1 loss remodels the tubular basement membrane (thinning, heparan sulfate enrichment) via a cilia-dependent, GLIS2-mediated program, with preferential distal-nephron distension. Reframes cyst initiation as partly biomechanical. **Limits:** preclinical/in-vitro only. Scores: Imp 5 | Ev 3 | Nov 8 | Dec 3 | Cal 8.

**pm_42333604 — PTH1R drives cyst growth (JASN)** [hypothesis-generating]
RiboTag profiling identified parathyroid hormone receptor 1 as a ciliary GPCR; genetic inactivation suppressed cyst growth in developmental and adult-onset mouse models. Notable because PTH1R is an already-druggable receptor class. **Limits:** preclinical only; PTH1R has systemic bone/calcium roles complicating targeting. Scores: Imp 5 | Ev 3 | Nov 8 | Dec 4 | Cal 8.

**pm_42329029 — AARS1/lactylation drives cyst growth (JASN)** [hypothesis-generating]
Alanyl-tRNA synthetase 1, a lactate-responsive lactyltransferase, promotes cyst growth; genetic deletion and beta-alanine (AARS1 inhibitor) both slowed cysts in Pkd1 mouse models. Links known glycolytic reprogramming to a specific enzymatic effector. **Limits:** preclinical only; beta-alanine is a non-selective probe, not a candidate drug. Scores: Imp 5 | Ev 3 | Nov 8 | Dec 4 | Cal 8.

**pm_42420301 — Structural basis of PC1-PC2 lipid gating (Nature Communications)** [hypothesis-generating]
Cryo-EM shows specific membrane lipids (phosphatidylglycerol, phosphatidic acid) hold the polycystin channel closed; a cilia-enriched oxysterol allosterically favors a more-open (still non-conductive) state. Defines a lipid-binding site that could in principle be drugged. **Limits:** purified-protein structural biology only, no cellular/animal/human data. Scores: Imp 5 | Ev 5 | Nov 8 | Dec 3 | Cal 9.

**ppr_1262859 — PKD2 D511V structural destabilization (preprint)** [hypothesis-generating]
Cryo-EM + ciliary electrophysiology + a new Pkd2 D509V/fl mouse strain show this missense variant destabilizes PC2, abolishes ciliary channel function, and causes rapid cystic disease — closing the loop from atomic structure to whole-animal phenotype for one variant. **Limits:** not peer-reviewed, single variant, no therapeutic intervention tested. Scores: Imp 5 | Ev 3 | Nov 8 | Dec 3 | Cal 8.

**pm_42418222 — Smooth-muscle PC1 is dispensable for arterial contractility — a well-controlled negative preclinical result** [hypothesis-generating, negative]
Smooth-muscle-specific Pkd1 knockout mice showed no change in physiological arterial contractility, contradicting conclusions drawn from non-specific germline knockouts. This undercuts a leading mechanistic explanation for ADPKD's near-universal early hypertension. **Why it matters despite being "just mouse data":** it is a clean negative that should reduce confidence in the vascular-smooth-muscle-intrinsic hypothesis specifically, redirecting mechanistic attention elsewhere (e.g., endothelial or renin-angiotensin pathways). **Limits:** physiological (not pathological) conditions only, one vascular bed, mouse only. Scores: Imp 4 | Ev 5 | Nov 7 | Dec 4 | Cal 9.

**pm_42441958 — C. elegans model for ADPKD variant classification** [hypothesis-generating]
CRISPR-engineered *C. elegans* functionally classified a PC2 missense variant as null-phenocopying and recessive-acting — a cheap, scalable assay approach to a real genetic-testing problem (variants of uncertain significance). **Limits:** single variant, invertebrate model with sensory-neuron (not kidney-tubule) PKD-2 function; needs validation against clinically adjudicated variants. Scores: Imp 4 | Ev 3 | Nov 7 | Dec 4 | Cal 8.

**ppr_1259843 — Single-nucleus transcriptomics of precystic kidneys** [hypothesis-generating]
~1 million-nucleus atlas of precystic Pkd1-mutant mouse kidneys identifies an early signaling program overlapping a failed-repair signature, with Creb5 as a candidate driver — defines the pre-cyst intervention window. **Limits:** not peer-reviewed, single hypomorphic genotype, associative only. Scores: Imp 4 | Ev 3 | Nov 8 | Dec 3 | Cal 8.

**pm_42314074 — Klotho suppresses cyst growth via ferroptosis/DNA methylation** [hypothesis-generating]
Klotho depleted in human/mouse ADPKD kidneys; recombinant Klotho suppressed cyst growth in Pkd1-KO mice. **Limits:** preclinical only, recombinant Klotho not a practical therapeutic, mechanisms correlative. Scores: Imp 4 | Ev 3 | Nov 7 | Dec 3 | Cal 7.

**pm_42426887 — Myofibroblast-specific autophagy drives cyst growth** [hypothesis-generating]
Implicates the stromal myofibroblast compartment (not just cyst epithelium) via autophagy in paracrine cyst expansion — widens the drug-target space. **Limits:** preclinical, male mice only, autophagy modulators are non-selective. Scores: Imp 4 | Ev 3 | Nov 7 | Dec 3 | Cal 8.

**ss_1270672178f3bf07d95c7b70d3a3964e3b935d7d — The Role of Mitochondria in Polycystic Kidney Disease (review)** [background/context] — Narrative review of mitochondrial dysfunction in PKD (metabolic reprogramming, oxidative stress). No new data; connects to the ketogenic/BHB/mTOR-AMPK thread. Scores: Imp 4 | Ev 2 | Nov 7 | Dec 2 | Cal 8.

**pm_42502691 — Pseudoexon activation in PKD1 (de novo + common variant complex allele)** [hypothesis-generating]
Paired genome/transcriptome sequencing resolved a previously unsolved diagnosis by showing a de novo intronic variant plus an inherited benign variant together activate a pathogenic pseudoexon — adds to the recognized set of PKD1 diagnostic blind spots. **Limits:** single-family case; prevalence of this mechanism unknown. Scores: Imp 4 | Ev 2 | Nov 7 | Dec 3 | Cal 8.

**pm_42497974 — Diagnosing Mendelian kidney disease: PKD1 exome blind spot (case)** [hypothesis-generating]
Single family with concurrent ADPKD (PKD1) + ADTKD (UMOD); causal PKD1 variant missed by exome sequencing, found only via long-range PCR + WGS — illustrates the known pseudogene-homology limitation. **Limits:** single case of an already-established limitation. Scores: Imp 4 | Ev 2 | Nov 4 | Dec 4 | Cal 8.

**ppr_1237168 — ParaDISM: short-read aligner for homologous genes** [hypothesis-generating]
Open-source pipeline reduces misalignment-driven false variant calls at PKD1; improved performance over standard aligners on 18 real ADPKD datasets. Directly targets the pseudogene-homology blind spot. **Limits:** unreviewed preprint, small validation cohort, no demonstrated change in actual diagnostic-lab yield yet. Scores: Imp 4 | Ev 4 | Nov 6 | Dec 3 | Cal 7.

**ppr_1247778 — PMM2 p.Arg238His as a PKD genetic modifier** [hypothesis-generating]
In vitro biochemistry on a rare PMM2 variant (4/418 PKD patients) consistent with a mild N-glycosylation defect, proposed as a severity modifier. **Limits:** unreviewed, only 4 carriers, in-vitro kinetics don't establish clinical effect. Scores: Imp 3 | Ev 3 | Nov 6 | Dec 2 | Cal 7.

**ppr_1252866 — PKD1/PKD2 variant burden in unselected exomes (6,272)** [hypothesis-generating]
2.2% carried pathogenic/likely-pathogenic PKD1/PKD2 variants, without phenotype confirmation. **Limits:** unreviewed preprint, no clinical phenotype confirmation, exome-pipeline false-positive risk. Scores: Imp 4 | Ev 3 | Nov 6 | Dec 3 | Cal 6.

**pm_42518502 — GANAB-related PKD mimicking neurofibromatosis type 1 (case report)** [background] — Rare-genotype case; not generalizable to typical PKD1/PKD2 ADPKD. Scores: Imp 3 | Ev 1 | Nov 3 | Dec 2 | Cal 7.

### Biomarkers / Endpoint Methodology

**pm_42519961 — Cystatin C vs. creatinine eGFR equations (Mayo Clinic, n=697)** [hypothesis-generating]
Combined creatinine-cystatin C CKD-EPI equation most accurately approximated measured GFR against a 50-patient mGFR subset. Connects to finding_028. **Limits:** single-center retrospective, small mGFR-validated subset, no treatment/outcome data. Scores: Imp 5 | Ev 5 | Nov 6 | Dec 4 | Cal 8.

**pm_42499441 — Race-based vs. race-free CKD-EPI equations (multicenter, n=597)** [hypothesis-generating]
Switching 2009→2021 race-free equation shifted eGFR/CKD staging, differentially by ethnic group — operationally relevant to tolvaptan-eligibility and trial-enrollment decisions even without new biology. Connects to finding_028. **Limits:** retrospective recalculation exercise, small African-American subgroup (n=82), no outcome data. Scores: Imp 4 | Ev 4 | Nov 7 | Dec 4 | Cal 8.

**pm_42513253 — Plasma amino acid signatures + ML for progression/hypertension (n=203)** [hypothesis-generating]
Candidate non-genetic biomarker panel. **Limits:** single-center, cross-sectional, no external validation, overfitting risk, progression not defined against a hard endpoint. Scores: Imp 4 | Ev 3 | Nov 6 | Dec 2 | Cal 6.

**pm_42490172 — Metabolomics in renal cystic disease (review)** [hypothesis-generating]
Pools published metabolomics studies; identifies a glycine/serine/threonine signature specific to ADPKD/Pkd1 models. **Limits:** predominantly preclinical/mouse pooled data, not a validated human biomarker cohort. Scores: Imp 4 | Ev 2 | Nov 5 | Dec 3 | Cal 7.

**pm_42389199 — Diagnostic yield of genetic testing in inherited kidney disease (n=256)** [background/context]
38.7% overall yield, 72.0% in cystic kidney disease specifically; PKD1/PKD2 top contributing genes. **Limits:** single tertiary-center referral-enriched cohort; won't generalize to unselected populations. Scores: Imp 4 | Ev 4 | Nov 6 | Dec 4 | Cal 8.

### Management / Epidemiology / Extrarenal

**pm_42428517 — Nephrolithiasis as an independent RRT risk marker (HOPE-PKD, n=410)** [hypothesis-generating]
New finding_027 — see above. Scores: Imp 6 | Ev 6 | Nov 7 | Dec 5 | Cal 8.

**pm_42409867 — Japanese national registry, correlates of eGFR decline (n=3562)** [background/context]
Confirms known prognostic factors (CKD stage, proteinuria) in a large unselected national population. **Limits:** confirmatory not novel, retrospective registry, no imaging/genotype adjustment. Scores: Imp 4 | Ev 5 | Nov 5 | Dec 4 | Cal 8.

**pm_42401882 — VEO-ADPKD phenotype meta-analysis (19 studies, 736 children)** [hypothesis-generating]
See finding_014 update. Scores: Imp 5 | Ev 4 | Nov 7 | Dec 4 | Cal 7.

**pm_42393189 — PKD and valve disease association (n=331,125, nested case-control)** [background/context]
~1.6-fold higher odds of valvular disease diagnosis; not a new association (mitral valve prolapse in ADPKD is long established), but quantified at population scale. **Limits:** diagnostic-code-based ascertainment, likely detection bias (PKD patients get more cardiac imaging), ADPKD pooled with unspecified PKD. Scores: Imp 3 | Ev 4 | Nov 5 | Dec 3 | Cal 7.

**pm_42430293 — Reach-J: kidney/CV outcomes by CKD etiology (Japan, randomly sampled, n=2249)** [background/context]
PKD (5.8% of cohort) had the highest KRT-initiation rate at CKD G4/G5 among etiologies, in a randomly sampled (lower referral-bias) design. **Limits:** small PKD subgroup (~130 patients), descriptive analysis, Japanese practice patterns may not generalize. Scores: Imp 4 | Ev 5 | Nov 6 | Dec 3 | Cal 8.

**pm_42390003 — Routine abdominal MRI detects LVH in ADPKD (n=156)** [hypothesis-generating]
AUC 0.82 for echo-defined LVH from height-adjusted LV wall volume already captured on routine TKV MRI — practically attractive if validated. **Limits:** retrospective single-cohort, only 27 LVH cases, specificity 64% at proposed threshold, no external validation. Scores: Imp 3 | Ev 4 | Nov 6 | Dec 3 | Cal 7.

**pm_42391598 — Cost-effectiveness of intracranial aneurysm screening (systematic review, 15 studies)** [background/context]
Wide variation in prevalence assumptions (0.5–19%) driving model conclusions for high-risk groups including ADPKD. **Limits:** modeling studies only, ADPKD-specific results not separable, no pooled estimate. Scores: Imp 4 | Ev 4 | Nov 7 | Dec 4 | Cal 8.

**pm_42479644 — Human organoids as ADPKD drug-development tools (review)** [background/context] — Narrative synthesis, no new data. Scores: Imp 4 | Ev 2 | Nov 5 | Dec 2 | Cal 9.

**pm_42473303 — Pregnancy in ADPKD (narrative review)** [background/context] — Practical counseling synthesis, no new data. Scores: Imp 3 | Ev 2 | Nov 5 | Dec 3 | Cal 8.

**ppr_1234285 — Tolvaptan implementation variation across 3 UK centres (qualitative)** [background]
Centralized, specialist-led pathways associated with more consistent, timely prescribing than distributed pathways — an organizational-mechanism complement to prior quantitative UK real-world data. **Limits:** unreviewed preprint, 3 case-study centres, qualitative, not generalizable without further testing. Scores: Imp 4 | Ev 3 | Nov 6 | Dec 3 | Cal 7.

**pm_42363980 — Species/proliferation-state/oxygen effects on in vitro nephrotoxicity screening** [hypothesis-generating]
Standard in vitro toxicity assay conditions may systematically misrepresent human nephrotoxicity risk for repurposed ADPKD candidates. **Limits:** purely in vitro, drug identities/effect sizes not extractable from abstract, no clinical correlation. Scores: Imp 3 | Ev 3 | Nov 6 | Dec 3 | Cal 8.

**ppr_1263871 — DESI-MS drug-distribution imaging in human cystic tissue (CAM model)** [hypothesis-generating]
Visualizes benzbromarone (TMEM16A-inhibiting candidate) accumulation at cyst epithelium — a new tissue-level tool to check target engagement. **Limits:** distribution/methods demonstration only, no efficacy/safety/PK data, unknown generalizability of ex vivo CAM model. Scores: Imp 3 | Ev 2 | Nov 6 | Dec 2 | Cal 8.

**ppr_1234840 — Real-world ADPKD burden in Chilean public health network (n=98)** [hypothesis-generating]
Apparent under-diagnosis, younger CKD onset than general CKD population, steeply rising per-patient costs by stage. **Limits:** small single-region cohort, unreviewed preprint, ICD-10 ascertainment bias likely. Scores: Imp 4 | Ev 3 | Nov 6 | Dec 3 | Cal 8.

**ppr_1278695 — Geographic/climate variation in tolvaptan discontinuation (Turkey, n=205)** [hypothesis-generating — flagged]
27.6% treatment interruption; explores unadjusted correlations with climate variables. **Limits:** not peer-reviewed, ecological correlation design vulnerable to centre/region confounding, geography-as-cause framing outruns the data. Scores: Imp 3 | Ev 2 | Nov 7 | Dec 3 | Cal 6.

### Cardiovascular / Skeletal Reviews (background, no new data)

pm_42313903 (polycystin-1 and cardiac remodeling), pm_42396661 (endothelial dysfunction/aneurysm mechanism), pm_42350686 (polycystin in the skeletal system), pm_42455965 (renal tubule mechanosensing) — all narrative reviews with no new primary data. Notable only as context: pm_42313903 was published concurrently with the negative smooth-muscle-PC1 result (pm_42418222) above, and pm_42350686 was published concurrently with a fracture-risk study (below) finding low calculated fracture risk in early ADPKD — both reviews slightly overreach relative to the contemporaneous primary data. Scores range Imp 3–4 | Ev 2–3 | Cal 7–9.

---

## Lower-Priority / Maintenance Items (relevance 1–3, condensed — nothing dropped silently)

**Background/context (relevance 3):** fracture-risk assessment in early ADPKD (pm_42387458, low calculated risk, small n); Portuguese 33-year genetic/clinical epidemiology of PKD2-driven KRT cohort (pm_42412748); family-based screening and health literacy, Turkey (pm_42360188); "new conceptual framework for PKD1" narrative (pm_42436404); JASN variants-to-therapeutics review (pm_42391103); "atypical ADPKD" commentary, no abstract available (pm_41824603); polyphenols review with speculative framing (pm_42355547); "current perspectives 2026" general overview (pm_42315404); Hong Kong WGS for unexplained CKD — ADPKD-negative by design, low relevance (pm_42329778); RCC risk-modeling opinion letter, no data (pm_42525210); GANAB case report (counted above).

**Hypothesis-generating, single-patient/small-n, flagged for skepticism (relevance 2–3):** plant-based ketogenic diet single case where TKV *increased* despite improved albuminuria (pm_42439786); empagliflozin single case with suspected but unconfirmed concomitant IgA nephropathy (pm_42337700); transgenic PKD2 pig generation, tool-only, no phenotype (pm_42334517); E-selectin "long-term validation" preprint with 74% attrition (ppr_1273298); automated microCT cyst-segmentation pipeline on 5–20 excised rat kidneys (pm_42448808).

**Tracker maintenance only (relevance 1–2):** corrigendum to the tracked TriNetX SGLT2i study (pm_42473614 — **flagged**, see Skepticism Notes #2 and finding_005 update); corrigenda to two unrelated indexed studies (pm_42390486, pm_42344534); 6 single-case reports (robot-assisted bilateral nephrectomy pm_42410901; COL4A4 misdiagnosis pm_42336693; prenatal TSC2/PKD1 deletion pm_42447423; emphysematous cyst infection pm_42508610; cefepime-induced delirium pm_42500764; porta hepatis compression pm_42524656; linezolid for suspected cyst infection pm_42404011; peritoneal dialysis continuation pm_42442395; drug-induced thrombocytopenia pm_42440206; hidden nonfunctioning kidney pm_42316419); 2 editorial/correspondence pairs on BMI stratification methodology (pm_42468836/pm_42468833) and a methods-reflection commentary (pm_42498085); 2 ARPKD-only items correctly out of ADPKD scope (pm_42305588, pm_42313208, pm_42498858).

---

## Negative / Null Results This Week

**These are the most decision-relevant items in this catch-up cycle and are stated plainly, not softened:**

1. **LIPS lanreotide RCT (pm_42320793)** — Negative on measured-GFR primary endpoint in a 3-year placebo-controlled trial. Rules out a kidney-function benefit for lanreotide in stage 2/3 ADPKD at the effect sizes this trial could detect (CI −3.4 to +2.8 mL/min/1.73m²/yr). Applies to adults with mGFR 30–89. Uncertainty remains: the CI is wide due to early enrollment stoppage.
2. **Smooth-muscle Pkd1 knockout — no effect on arterial contractility (pm_42418222)** — A well-controlled negative preclinical result that undercuts the vascular-smooth-muscle-intrinsic hypothesis for ADPKD hypertension specifically. Rules out (in mice, under physiological conditions) a direct SMC-autonomous PC1 role in baseline vascular tone; does not rule out a role under pathological conditions or in other cell types (e.g., endothelium).
3. **(Context, not this window) Octreotide LAR meta-analysis (finding_019, prior cycle)** remains the standing companion negative result — now corroborated rather than superseded by the LIPS lanreotide finding.

---

## Trial Updates

| Trial | Change | Type |
|---|---|---|
| **NCT05281328** (CAM2029 octreotide depot, PLD) | **RESULTS POSTED** — marginal positive primary endpoint (htTLV, p=0.0443); 1 death as SAE in active arm; all kidney-relevant secondaries unpopulated | **Results event — see Highlight 2** |
| **NCT06734234** (GSK4771261, Phase 1 SAD) | RECRUITING → ACTIVE_NOT_RECRUITING (enrollment closed at 86); primary completion Sept 2026 → **Apr 2027** (~7.5-month extension, no reason given) | **Status change — genuine milestone (enrollment complete)** |
| **NCT05510115** (Seliger empagliflozin feasibility, n=50) | Primary completion reached as ACTUAL on 2026-03-18 (was estimated 2026-03-31); **no results posted yet** | Status change — now overdue-results watch |
| **NCT02497521** (German Tolvaptan Registry) | Registry drift correction: primary completion 2025-11 → 2027-12 | Tracker maintenance |
| **NCT02936791** (Early PKD Observational Cohort) | Registry drift correction: primary completion 2025-09 → 2030-06 (~5-yr extension) | Tracker maintenance |
| **NCT05193981** (Homocysteine/endothelial function) | Registry drift correction: primary completion 2026-06 → 2026-12 | Tracker maintenance |
| **NCT06496542** (Renal oxygen consumption) | Registry drift correction: enrollment 16→14 actual; primary completion 2026-07 → 2027-08 (13-month extension) | Tracker maintenance |
| **NCT04578548** (GLPG2737) | Sponsor record correction (Galapagos NV → Lakefront Biotherapeutics NV); already-known TERMINATED/negative status unchanged (finding_026) | Tracker maintenance |
| **PYC-003** (NCT06714006) | No change since June 8 timeline extension; still RECRUITING, primary completion Nov 2028 | Unchanged |
| **Tirzepatide** (NCT06582875) | No change; RECRUITING, primary completion June 2029 | Unchanged |
| All other tracked trials (88 total monitored) | No further phase/status changes this window | Tracker maintenance |

**Overdue-results watch (no results posted, ordered by how overdue):**
- **NCT06435858** (empagliflozin divalent ions) — primary completion July 2025, now **~13 months overdue**.
- **NCT06289998** (tamibarotene, RAR agonist) — primary completion Dec 2025, now **~8 months overdue**.
- **NCT05510115** (Seliger empagliflozin feasibility) — primary completion reached (actual) March 2026, now **~4.5 months overdue**.

---

## Evolving Understanding

**1. Somatostatin analogues (finding_019) — confidence strengthened, still HIGH, direction unchanged (negative for kidney function).** The LIPS lanreotide RCT is the single most important item in this catch-up window. It independently corroborates the octreotide LAR meta-analysis conclusion using a different drug and a stronger endpoint (measured, not estimated, GFR). Two different somatostatin analogues have now failed to show kidney-function benefit in RCT-grade evidence. The concurrently posted CAM2029 PLD result is a different endpoint (liver volume) and should not be read as evidence for or against the kidney-function conclusion — but its marginal p-value and safety signal (a death) warrant the same skepticism this framework applies throughout.

**2. A new cross-cutting endpoint-validity question (finding_028, new).** Three independent, individually weak signals — a tolvaptan/TEMPO 3:4 methodological critique, the LIPS trial's own creatinine/cystatin C discordance, and two papers showing eGFR-equation choice materially shifts ADPKD staging — converge on the same open question: is creatinine-based eGFR a fully reliable primary endpoint in ADPKD trials? No single item answers this, and clinical practice should not change today. But the convergence across three unrelated sources in one cycle is itself a signal worth tracking, and a cystatin C reanalysis of TEMPO 3:4, if it happens, would be genuinely informative.

**3. Novel investigational pipeline (finding_004) — breadth up, clinical evidence unchanged.** The PKD1 uORF/ASO mechanism and the combination-siRNA nanoparticle approach are genuine additions. Two other "new" preprints (ppr_1246945, ppr_1239348) turned out to be re-indexed versions of already-tracked work, surfaced through a paper-deduplication gap during the pipeline's downtime — flagged explicitly rather than double-counted as new science (see Skepticism Notes #3). Confidence remains MODERATE: more approaches exist on paper, none has moved toward humans this cycle.

**4. Pediatric ADPKD (finding_014) — quantification improved, qualitative picture unchanged.** The VEO-ADPKD meta-analysis is the first to put numbers on a phenotype gap clinicians already recognized qualitatively (biallelic PKD1 severity, perinatal risk). Confidence stays MODERATE; every pooled interval barely excludes the null.

**5. New prognostic marker (finding_027, new).** Nephrolithiasis as an independent RRT risk factor is plausible and imaging-confirmed, but LOW confidence pending replication — a single cohort with 51 events is not enough to add it to routine risk stratification yet.

**No existing finding was downgraded this cycle.** The single most consequential decision-relevant fact is negative: lanreotide does not protect kidney function in stage 2/3 ADPKD.

---

## Skepticism Notes

1. **pm_42445794 (ketogenic + exogenous ketone/citrate case series, n=4) — do not cite this as evidence.** Claim calibration scored 3/10 for a reason: the title claims "halting cyst progression" from four self-referred, uncontrolled, retrospective patients compared to their own prior growth trends, with heterogeneous co-interventions and — critically — direct financial conflicts including company employment, shareholding, and patents on the studied product. Regression to the mean and responder self-selection cannot be excluded. This is promotional-adjacent evidence and should be treated accordingly.
2. **pm_42473614 — corrigendum on a paper this tracker already cites (finding_005, SGLT2i dialysis HR 0.35).** The correction content is not exposed in the PubMed record. Do not repeat the HR 0.35 figure in patient-facing or clinical material until the correction is reviewed next cycle.
3. **ppr_1246945 and ppr_1239348 — re-indexed, not new.** Both are duplicate disclosures of research already incorporated in earlier digest cycles, resurfaced under different source IDs during the pipeline gap. Presenting them as "this week's news" would overstate freshness; they are noted here specifically to correct that risk.
4. **CAM2029 PLD result (NCT05281328) — a fragile significant finding.** p=0.0443 driven mainly by placebo-arm liver growth rather than treatment shrinkage, plus a treatment-arm death recorded as an SAE. This is an industry-sponsored program (Camurus) in its own product. Treat as a marginal, registry-posted (not peer-reviewed) result, not a confirmed benefit.
5. **Single-patient case reports presented as diet/drug evidence (pm_42439786, pm_42337700).** In the plant-based ketogenic case, total kidney volume — the endpoint that actually tracks ADPKD progression — moved in the *wrong* direction (617→709 cc) despite an albuminuria improvement being emphasized; in the empagliflozin case, an unconfirmed concomitant glomerular disease is the more plausible explanation for the antiproteinuric response than ADPKD-specific benefit. Neither supports any general conclusion.
6. **ppr_1273298 ("long-term validation" of an E-selectin polymorphism) — the title overclaims.** 74% attrition (20 of 76 completed 10-year follow-up) makes survivorship bias, not validation, the dominant feature of this dataset.
7. **ppr_1278695 (geographic/climate tolvaptan discontinuation, Turkey)** uses unadjusted ecological correlations between individual outcomes and centre-level climate data — vulnerable to confounding by centre and region — while framing geography as an "influence," which outruns what correlation can show.

---

## Watchlist

| Item | Why watching | What to look for |
|---|---|---|
| **TEMPO 3:4 cystatin C reanalysis** (proposed, not commissioned) | Would resolve the endpoint-validity question raised this cycle (finding_028) | Any group announcing or conducting the reanalysis |
| **PYC-003 Phase 1** (NCT06714006) | First IV RNA therapeutic in ADPKD; timeline now Nov 2028 | First safety/PD data |
| **GSK4771261 Phase 1** (NCT06734234) | Enrollment now closed (86 participants) | First safety/PK/biomarker readout, now expected ~Apr 2027 |
| **CAM2029 PLD** (NCT05281328) | Marginal primary result posted; continues to Week 173 | Secondary endpoints (htTKV, eGFR, QoL, PLD-S/Q) and peer-reviewed publication |
| **NCT06435858** (SGLT2i divalent ions) | ~13 months overdue | Results publication |
| **NCT06289998** (Tamibarotene Phase 2) | ~8 months overdue | First RAR-agonism clinical data in ADPKD |
| **NCT05510115** (Seliger empagliflozin pilot) | Primary completion reached, ~4.5 months overdue | Safety/tolerability paper; secondary TKV/eGFR |
| **VX-407 AGLOW** (NCT07161037) | Phase 2a PKD1 corrector, n=24 | Any efficacy signal |
| **STOP-PKD** (NCT07280585) | Phase 3 dapagliflozin, n=420, completion 2030 | Decisive SGLT2i test |
| **IMPEDE-PKD** (NCT04939935) | Phase 3 metformin, n=1174 | First results expected 2028–2030 |
| **ABBV-CLS-628** (NCT06902558) | Phase 2 | Interim safety/efficacy |
| **PKD1 uORF/ASO program** (pm_42518289) | Novel mechanism this cycle | Any move toward in vivo delivery optimization or a named clinical candidate |
| **Corrigendum on tracked SGLT2i study** (pm_42473614) | Correction content unknown | Full correction text next cycle |

*(Timelines reflect publicly posted registry data; no interim-analysis dates are implied beyond what registries state.)*

---

## Data Summary

- **Papers tracked:** 703 total. **89 incorporated this cycle** (49 at relevance ≥4 with full evaluation, 40 at relevance 1–3 condensed — see Lower-Priority section). This closes out the `pending_synthesis` queue and the small residual `new` (non-baseline) queue.
- **Backlog note (not incorporated, intentionally):** 267 low-relevance baseline papers from the original April 2026 baseline sweep remain marked `new` (relevance scores mostly 2–5, one mis-scored outlier at 7 that is not ADPKD-relevant on inspection). These are stale tracker noise pre-dating this system's regular operation, not this week's news, and were excluded per the freshness-discipline rules in the evaluation framework. Recommend a separate one-time triage/pruning pass rather than folding them into a weekly digest.
- **Trials monitored:** 88 total. 1 results posting (NCT05281328/CAM2029), 1 genuine status change (NCT06734234 enrollment closed), 1 completion-date-reached-but-no-results change (NCT05510115), 5 registry drift corrections, 0 new trials added.
- **Findings updated:** 6 (finding_001 tolvaptan — caveat added; finding_004 novel pipeline — 2 genuine additions + 2 duplicate-flagged; finding_005 SGLT2i — corrigendum flag; finding_006 GLP-1RA — context added; finding_014 pediatric — VEO meta-analysis added; finding_019 somatostatin — major update, confidence reaffirmed HIGH).
- **New findings added:** 2 (finding_027 nephrolithiasis/RRT risk; finding_028 endpoint-validity cross-cutting thread).
- **Alerts issued this cycle:** 2 (LIPS lanreotide RCT: importance 8/evidence 8; CAM2029 PLD readout: importance 5/evidence 4 — included for decision usefulness as the only genuine trial-results event, not because it clears the importance≥7-and-evidence≥5 bar on its own).
- **Papers flagged for skepticism:** 8 (ketogenic case series pm_42445794; corrigendum pm_42473614; two re-indexed duplicates ppr_1246945/ppr_1239348; CAM2029 marginal result; two single-patient anecdotes pm_42439786/pm_42337700; "long-term validation" preprint with 74% attrition ppr_1273298).
- **Trials with overdue results:** 3 (NCT06435858 ~13 mo; NCT06289998 ~8 mo; NCT05510115 ~4.5 mo).
- **Most decision-relevant item:** LIPS lanreotide RCT — negative on kidney-function primary endpoint, prunes the somatostatin-analogue space further.
- **Most novel item:** PKD1 uORF/antisense-oligonucleotide mechanism (pm_42518289, Novelty 8/10) — genuinely first disclosure.
- **Pipeline-health note:** This edition closes a ~7-week digest gap. Two paper IDs (ppr_1246945, ppr_1239348) were confirmed re-indexed duplicates of already-tracked work — a deduplication gap worth addressing in the scan pipeline before the next cycle.
