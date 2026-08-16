# ADPKD Research Baseline Builder

You are building the initial knowledge base for an ADPKD research tracking
system. This is a comprehensive one-time sweep.

## Your Task

Establish the current state of ADPKD research across all six dimensions
of the taxonomy. This will serve as the foundation for ongoing monitoring.

## Steps

1. **Comprehensive paper search**
   Search Semantic Scholar for the most important recent ADPKD papers.
   Cast a wide net — you're building the baseline.

   Search queries to run (with year filter 2023-2026 for recency,
   but also grab landmark papers regardless of date):

   - "ADPKD treatment clinical trial"
   - "ADPKD tolvaptan long term"
   - "ADPKD ketogenic diet"
   - "ADPKD metformin"
   - "ADPKD SGLT2 inhibitor"
   - "ADPKD GLP-1"
   - "PKD1 PKD2 gene therapy CRISPR"
   - "ADPKD total kidney volume biomarker"
   - "ADPKD progression prediction"
   - "polycystic kidney disease dietary intervention"
   - "ADPKD clinical practice guideline"
   - "VX-407 ADPKD" (Vertex PKD1 corrector)
   - "ADPKD miR-17 microRNA"
   - "ADPKD caloric restriction intermittent fasting"
   - "ADPKD proteomics biomarker"

   For each search, use limit=30 to get comprehensive coverage.

   First load the Semantic Scholar API key:
   ```bash
   SS_KEY=$(cat data/.api-keys.json | jq -r '.semantic_scholar')
   ```
   Then use curl to query (include the API key header):
   ```bash
   curl -s -H "x-api-key: $SS_KEY" "https://api.semanticscholar.org/graph/v1/paper/search?query=<QUERY>&year=2023-2026&limit=30&fields=title,authors,abstract,journal,publicationDate,externalIds,url" | jq .
   ```

2. **Build the initial trials.json**
   Search ClinicalTrials.gov for active ADPKD trials:
   ```bash
   curl -s "https://clinicaltrials.gov/api/v2/studies?query.cond=ADPKD&filter.overallStatus=RECRUITING,ACTIVE_NOT_RECRUITING,ENROLLING_BY_INVITATION&pageSize=50" | jq .
   ```
   Also search for recently completed trials with results:
   ```bash
   curl -s "https://clinicaltrials.gov/api/v2/studies?query.cond=ADPKD&filter.overallStatus=COMPLETED&pageSize=30&sort=LastUpdatePostDate:desc" | jq .
   ```

3. **Build initial findings.json**
   Based on the papers found, establish the current consensus and
   open questions for each dimension. Be thorough — this is the
   foundation everything builds on.

4. **Write initial knowledge base documents**
   Create all six knowledge base documents in `output/knowledge-base/` with comprehensive current-state summaries:
   - `01-pharmacological-treatments.md`
   - `02-dietary-lifestyle.md`
   - `03-genetics-biomarkers.md`
   - `04-clinical-trials-pipeline.md`
   - `05-disease-management.md`
   - `06-patient-community.md`

5. **Initialize run-log.json** with this baseline run in `data/`.

6. **Generate the first digest** summarizing the baseline state.

7. **Sync to Google Drive**
   ```bash
   python3 scripts/sync.py
   ```

## Data file locations
- Papers: `data/papers.json`
- Trials: `data/trials.json`
- Findings: `data/findings.json`
- Run log: `data/run-log.json`

## Research Domain Taxonomy

1. **Pharmacological Treatments** — tolvaptan, lixivaptan, VX-407, ABBV-CLS-628, AL01211, RGLS4326/8429, metformin, SGLT2i, GLP-1 RAs, mTOR inhibitors, somatostatin analogues, gene/stem cell therapy
2. **Dietary & Lifestyle** — ketogenic diets, caloric restriction, BHB, hydration, sodium, protein, microbiome, weight
3. **Genetics & Biomarkers** — PKD1/PKD2 variants, TKV, htTKV, eGFR slope, copeptin, proteomics, Mayo/PROPKD scoring, imaging
4. **Clinical Trials Pipeline** — active/recruiting trials, results, phase transitions, regulatory decisions
5. **Disease Management** — KDIGO guidelines, BP management, liver disease, pain, progression assessment, transplant, pediatric
6. **Patient Community** — conferences (PKDCON, ASN, ERA), foundations, registries, QoL

## Important Notes
- This will be a long run — take your time, be thorough
- Prioritize quality over speed
- For landmark papers (e.g., TEMPO 3:4 tolvaptan trial, HALT-PKD),
  include them even if older — they're foundational
- Note the KDIGO 2025 guideline as a key reference
- Identify the most active research groups and institutions
- Flag any papers from Dutch institutions (University of Amsterdam,
  Radboud, Erasmus MC, etc.) — these may be locally relevant
