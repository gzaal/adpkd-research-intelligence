#!/usr/bin/env python3
"""
Process raw baseline data into structured papers.json and trials.json.
"""
import json
import re
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
RAW_DIR = DATA_DIR / "raw_baseline"
TODAY = datetime.now().strftime("%Y-%m-%d")
RUN_ID = f"baseline_{TODAY}_001"

# Taxonomy keywords for classification
DIMENSION_KEYWORDS = {
    "pharmacological": [
        "tolvaptan", "lixivaptan", "V2 receptor", "vasopressin",
        "VX-407", "ABBV-CLS-628", "AL01211", "RGLS4326", "RGLS8429",
        "metformin", "SGLT2", "GLP-1", "semaglutide", "liraglutide",
        "mTOR", "rapamycin", "sirolimus", "everolimus",
        "somatostatin", "pasireotide", "octreotide", "lanreotide",
        "CRISPR", "gene therapy", "stem cell", "mesenchymal",
        "miR-17", "microRNA", "antisense", "RNA therapy",
        "bosutinib", "pioglitazone", "bempedoic",
        "drug", "pharmacol", "treatment", "therapy", "inhibitor",
        "PYC-003", "venglustat", "bardoxolone",
    ],
    "dietary": [
        "ketogenic", "keto", "diet", "caloric restriction", "fasting",
        "intermittent fasting", "BHB", "beta-hydroxybutyrate", "ketosis",
        "water intake", "hydration", "sodium", "salt",
        "protein intake", "plant-based", "microbiome", "fiber",
        "weight", "BMI", "obesity", "nutrition", "lifestyle",
    ],
    "genetics": [
        "PKD1", "PKD2", "genotype", "mutation", "variant", "truncating",
        "polygenic", "genetic", "GWAS", "genome",
        "biomarker", "TKV", "htTKV", "total kidney volume",
        "eGFR", "copeptin", "proteomics", "serum",
        "Mayo classification", "PROPKD", "risk score",
        "MRI", "imaging", "segmentation", "AI-assisted",
    ],
    "clinical_trials": [
        "clinical trial", "randomized", "RCT", "phase 1", "phase 2",
        "phase 3", "NCT", "enrollment", "recruiting", "placebo",
        "endpoint", "efficacy", "safety", "FDA", "EMA",
    ],
    "management": [
        "guideline", "KDIGO", "blood pressure", "hypertension",
        "ACE inhibitor", "ARB", "liver cyst", "polycystic liver",
        "pain", "transplant", "dialysis", "pediatric", "children",
        "monitoring", "progression", "CKD stage",
    ],
    "community": [
        "PKD Foundation", "PKDCON", "ASN", "ERA Congress",
        "patient registry", "quality of life", "PRO",
        "conference", "patient-reported",
    ],
}

SUBTOPIC_KEYWORDS = {
    "V2_receptor_antagonists": ["tolvaptan", "lixivaptan", "V2 receptor", "vasopressin receptor"],
    "PKD1_correctors": ["VX-407", "PKD1 corrector", "Vertex"],
    "novel_investigational": ["ABBV-CLS-628", "AL01211", "RGLS4326", "RGLS8429", "PYC-003"],
    "RNA_therapies": ["miR-17", "microRNA", "antisense", "RNA therapy", "RGLS"],
    "repurposed_drugs": ["metformin", "SGLT2", "GLP-1", "bempedoic", "pioglitazone", "bosutinib"],
    "mTOR_pathway": ["mTOR", "rapamycin", "sirolimus", "everolimus"],
    "somatostatin": ["somatostatin", "pasireotide", "octreotide", "lanreotide"],
    "gene_therapy": ["CRISPR", "gene therapy", "gene editing"],
    "stem_cell": ["stem cell", "mesenchymal"],
    "ketogenic_diets": ["ketogenic", "keto diet", "KETO-ADPKD", "ketosis"],
    "caloric_restriction": ["caloric restriction", "fasting", "intermittent fasting", "time-restricted"],
    "BHB_supplementation": ["BHB", "beta-hydroxybutyrate", "exogenous ketone"],
    "water_intake": ["water intake", "hydration", "vasopressin suppression"],
    "sodium_restriction": ["sodium", "salt intake", "HALT-PKD"],
    "protein_management": ["protein intake", "plant-based protein", "dietary protein"],
    "gut_microbiome": ["microbiome", "gut bacteria", "fiber", "short-chain fatty acid"],
    "gene_variants": ["PKD1 truncating", "PKD2", "genotype-phenotype", "variant"],
    "progression_biomarkers": ["TKV", "htTKV", "total kidney volume", "eGFR slope"],
    "serum_biomarkers": ["proteomics", "copeptin", "serum biomarker"],
    "risk_scoring": ["Mayo classification", "PROPKD", "risk score", "prediction"],
    "imaging": ["MRI", "imaging", "segmentation", "AI-assisted", "ultrasound"],
    "blood_pressure": ["blood pressure", "hypertension", "ACE inhibitor", "ARB"],
    "liver_disease": ["liver cyst", "polycystic liver", "PLD"],
    "pain_management": ["pain", "cyst rupture", "analgesic"],
    "transplant": ["transplant", "dialysis", "renal replacement"],
    "pediatric": ["pediatric", "children", "early-onset"],
    "guidelines": ["guideline", "KDIGO", "clinical practice", "recommendation"],
}


def classify_text(text):
    """Classify text into dimensions and subtopics."""
    if not text:
        return [], []
    text_lower = text.lower()

    dimensions = []
    for dim, keywords in DIMENSION_KEYWORDS.items():
        if any(kw.lower() in text_lower for kw in keywords):
            dimensions.append(dim)

    subtopics = []
    for sub, keywords in SUBTOPIC_KEYWORDS.items():
        if any(kw.lower() in text_lower for kw in keywords):
            subtopics.append(sub)

    return dimensions or ["general"], subtopics


def score_relevance(title, abstract, dimensions):
    """Score paper relevance 0-10.

    LEGACY single-axis score kept for backwards compatibility.
    New papers should also get multi-axis scores via the LLM scan prompt.
    This function provides a rough heuristic for baseline processing.
    """
    scores = score_multi_axis(title, abstract, dimensions)
    # Composite: weighted average biased toward evidence strength and calibration
    composite = (
        scores["importance"] * 0.20
        + scores["evidence_strength"] * 0.30
        + scores["novelty"] * 0.10
        + scores["decision_usefulness"] * 0.25
        + scores["claim_calibration"] * 0.15
    )
    return min(round(composite), 10)


def score_multi_axis(title, abstract, dimensions):
    """Score paper on five axes (0-10 each) with skepticism penalties.

    Axes (per evaluation-framework.md):
      importance          — How important for the field if true?
      evidence_strength   — How believable given design & data quality?
      novelty             — How genuinely new and timely?
      decision_usefulness — Would this change clinical/research/pipeline decisions now?
      claim_calibration   — How well does the takeaway match what evidence supports?
    """
    text = f"{title or ''} {abstract or ''}".lower()
    flags = detect_skepticism_flags(text)

    # --- Importance (field significance, not optimism) ---
    # 8-10: large RCT, pivotal, regulatory, patient-important endpoint, strong negative
    # 5-7: meaningful observational, translational, early pipeline, guideline review
    # 0-4: preclinical, case reports, mechanistic, corrections, stale
    importance = 1
    if "adpkd" in text or "autosomal dominant polycystic" in text:
        importance += 2
    elif "polycystic kidney" in text:
        importance += 1
    if any(w in text for w in ["phase 3", "pivotal", "primary endpoint"]):
        importance += 3
    elif any(w in text for w in ["phase 2", "phase 1", "first-in-human", "first-in-class"]):
        importance += 2
    if any(w in text for w in ["guideline", "kdigo", "standard of care"]):
        importance += 2
    if any(w in text for w in ["dialysis", "esrd", "kidney failure", "transplant"]):
        importance += 1
    if any(w in text for w in ["tkv", "httcv", "total kidney volume"]):
        importance += 1
    # Strong negative results are important — they close questions
    if any(w in text for w in ["no significant", "did not improve", "failed to",
                                "no benefit", "not superior"]):
        if any(w in text for w in ["randomized", "rct", "double-blind"]):
            importance += 2
    # Demote case reports, corrections
    if any(w in text for w in ["case report", "case series"]):
        importance = max(importance - 2, 0)
    if any(w in text for w in ["correction", "erratum", "corrigendum"]):
        importance = max(importance - 3, 0)
    importance = min(importance, 10)

    # --- Evidence strength (study design & data quality, NOT journal prestige) ---
    # 8-10: well-designed RCT, adequately powered, clinically relevant endpoints
    # 5-7: prospective cohort, solid observational, target trial emulation
    # 2-4: uncontrolled, abstract-only, small exploratory, preclinical, narrative review
    # 0-1: case report, correction, promotional statement, conceptual abstract
    evidence = 2  # base: skeptical default
    if any(w in text for w in ["randomized", "rct", "double-blind", "placebo-controlled"]):
        evidence += 4
    elif any(w in text for w in ["meta-analysis", "systematic review"]):
        evidence += 3
    elif any(w in text for w in ["prospective", "target trial emulation"]):
        evidence += 2
    elif any(w in text for w in ["cohort", "observational"]):
        evidence += 1
    # Clear methodology and adequate power signals
    if any(w in text for w in ["adequately powered", "primary endpoint met"]):
        evidence += 1
    if any(w in text for w in ["patient", "participants", "subjects", "enrollment"]):
        evidence += 1
    # Abstract-only = evidence ceiling of 4
    is_abstract_only = any(w in text for w in [
        "conference abstract", "poster", "supplement abstract",
    ])
    # Case report / correction = evidence ceiling of 1
    is_case_or_correction = any(w in text for w in [
        "case report", "case series", "correction", "erratum",
    ])

    # === SKEPTICISM PENALTIES ===
    penalty = 0
    if flags["single_arm"]:
        penalty += 2
    if flags["retrospective"]:
        penalty += 1
    if flags["propensity_matched"]:
        penalty += 1
    if flags["pre_post_only"]:
        penalty += 2
    if flags["small_n"]:
        penalty += 1
    if flags["short_followup"]:
        penalty += 1
    if flags["commercial_sponsor"]:
        penalty += 1
    if flags["surrogate_endpoint_only"]:
        penalty += 1
    if flags["bold_claim_egfr_only"]:
        penalty += 2
    if flags["promotional_framing"]:
        penalty += 1
    if flags["abstract_only"]:
        penalty += 1
    if flags["no_full_methods"]:
        penalty += 1
    if flags["case_series"]:
        penalty += 2
    if flags["rare_genotype"]:
        penalty += 1
    evidence = max(evidence - penalty, 0)
    # Apply evidence ceilings
    if is_case_or_correction:
        evidence = min(evidence, 1)
    elif is_abstract_only:
        evidence = min(evidence, 4)
    evidence = min(evidence, 10)

    # --- Novelty/Freshness (how genuinely new and timely?) ---
    # 8-10: truly new event, first publication/disclosure
    # 5-7: recent but not same-week, newly disclosed conference item
    # 2-4: older item newly indexed, registry metadata refresh
    # 0-1: clearly stale, correction, resurfaced old item
    novelty = 4  # default: moderate (we can't assess dates heuristically)
    if any(w in text for w in ["first", "novel", "first-in-class",
                                "first-in-human"]):
        novelty += 2
    if any(w in text for w in ["phase 1", "first-in-human"]):
        novelty += 2
    # Penalize recycled/review content
    if any(w in text for w in ["review", "narrative review", "overview", "update on"]):
        novelty -= 2
    if any(w in text for w in ["correction", "erratum", "corrigendum"]):
        novelty = 0
    novelty = max(min(novelty, 10), 0)

    # --- Decision usefulness (would this change behavior NOW?) ---
    # High if it changes what clinicians/researchers/investors should do
    # Internally: clinical usefulness + research usefulness, rolled into one
    usefulness = 1  # most papers don't change behavior
    if any(w in text for w in ["guideline", "recommendation", "standard of care"]):
        usefulness += 3
    if any(w in text for w in ["phase 3", "pivotal", "primary endpoint met"]):
        usefulness += 3
    elif any(w in text for w in ["randomized", "rct"]):
        usefulness += 2
    # Negative results have HIGH decision value for pruning
    if any(w in text for w in ["no significant", "did not improve", "failed to",
                                "no benefit", "not superior"]):
        usefulness += 2
    # Preclinical = low clinical usefulness, modest research usefulness
    if any(w in text for w in ["mouse", "mice", "rat", "in vitro", "cell line",
                                "organoid"]):
        usefulness = max(usefulness - 1, 0)
        # But bump modestly for mechanistically important early work
        if any(w in text for w in ["novel", "first", "new mechanism", "new target"]):
            usefulness += 1
    # Case reports/corrections = very low
    if is_case_or_correction:
        usefulness = min(usefulness, 1)
    usefulness = max(min(usefulness, 10), 0)

    # --- Claim calibration (start at 8, subtract for overclaiming signals) ---
    # This is a heuristic proxy — the LLM agent does the real calibration check
    calibration = 8
    if flags["promotional_framing"]:
        calibration -= 3
    if flags["bold_claim_egfr_only"]:
        calibration -= 2
    if flags["surrogate_endpoint_only"]:
        calibration -= 1
    if flags["commercial_sponsor"]:
        calibration -= 1
    if flags["pre_post_only"]:
        calibration -= 1
    # Preclinical claims about clinical relevance
    if (any(w in text for w in ["mouse", "mice", "in vitro", "organoid"])
            and any(w in text for w in ["treatment", "therapy", "efficacy"])):
        calibration -= 1
    calibration = max(min(calibration, 10), 0)

    return {
        "importance": importance,
        "evidence_strength": evidence,
        "novelty": novelty,
        "decision_usefulness": usefulness,
        "claim_calibration": calibration,
    }


def detect_skepticism_flags(text):
    """Detect conditions that warrant extra skepticism.

    These flags are used both for scoring penalties and for display
    in the dashboard. See evaluation-framework.md for the full list.
    """
    text = text.lower() if isinstance(text, str) else ""
    return {
        "single_arm": (
            "single-arm" in text or "single arm" in text
            or ("open-label" in text and "randomized" not in text)
        ),
        "retrospective": "retrospective" in text,
        "propensity_matched": (
            "propensity" in text or "propensity-matched" in text
        ),
        "pre_post_only": (
            ("pre-post" in text or "before and after" in text
             or "within-subject" in text)
            and "control" not in text
        ),
        "small_n": any(
            f"n={n}" in text or f"n = {n}" in text
            for n in range(1, 31)
        ),
        "short_followup": any(
            w in text for w in [
                "3-month", "3 month", "12-week", "12 week",
                "8-week", "8 week", "6-week", "6 week",
                "4-week", "4 week", "short-term",
            ]
        ),
        "commercial_sponsor": any(
            w in text for w in [
                "sponsored by", "funded by", "commercial",
                "industry-sponsored", "ren-nu", "medical food",
            ]
        ),
        "surrogate_endpoint_only": (
            any(w in text for w in ["egfr", "surrogate"])
            and not any(w in text for w in [
                "tkv", "esrd", "dialysis", "transplant",
                "kidney failure", "hard endpoint",
            ])
        ),
        "bold_claim_egfr_only": (
            any(w in text for w in ["improvement", "improved", "reversal", "reversed"])
            and "egfr" in text
            and not any(w in text for w in ["tkv", "total kidney volume"])
        ),
        "promotional_framing": any(
            w in text for w in [
                "breakthrough", "game-changing", "revolutionary",
                "miracle", "cure", "remarkable",
            ]
        ),
        "abstract_only": any(
            w in text for w in [
                "conference abstract", "poster presentation",
                "supplement abstract",
            ]
        ),
        "no_full_methods": any(
            w in text for w in [
                "abstract only", "methods not available",
                "preliminary", "interim",
            ]
        ),
        "case_series": any(
            w in text for w in ["case report", "case series"]
        ),
        "rare_genotype": any(
            w in text for w in [
                "contiguous gene", "tsc2", "syndromic",
                "rare variant", "arpkd",
            ]
        ),
    }


def extract_entities(title, abstract):
    """Extract known entity mentions from text."""
    text = f"{title or ''} {abstract or ''}".lower()
    entities = []
    known = [
        "tolvaptan", "lixivaptan", "VX-407", "ABBV-CLS-628", "AL01211",
        "RGLS4326", "RGLS8429", "metformin", "SGLT2", "GLP-1",
        "rapamycin", "sirolimus", "everolimus", "pasireotide", "octreotide",
        "bosutinib", "pioglitazone", "bempedoic acid", "CRISPR",
        "PKD1", "PKD2", "TKV", "htTKV", "eGFR", "copeptin",
        "KDIGO", "TEMPO", "HALT-PKD", "KETO-ADPKD", "TAME PKD",
        "PYC-003", "ketogenic", "microRNA", "miR-17",
    ]
    for entity in known:
        if entity.lower() in text:
            entities.append(entity)
    return entities


def process_papers():
    """Transform raw SS papers into papers.json schema."""
    with open(RAW_DIR / "ss_papers_raw.json") as f:
        raw = json.load(f)

    papers = []
    for p in raw:
        title = p.get("title", "")
        abstract = p.get("abstract", "")
        search_text = f"{title} {abstract or ''}"

        dims, subs = classify_text(search_text)
        relevance = score_relevance(title, abstract, dims)
        entities = extract_entities(title, abstract)

        ext_ids = p.get("externalIds", {})
        doi = ext_ids.get("DOI", "")
        ss_id = p.get("paperId", "")

        authors = [a.get("name", "") for a in p.get("authors", [])]
        journal = (p.get("journal") or {}).get("name", "")
        pub_date = p.get("publicationDate", "")

        scores = score_multi_axis(title, abstract, dims)
        flags = detect_skepticism_flags(f"{title} {abstract or ''}")

        paper = {
            "id": f"ss_{ss_id}",
            "title": title,
            "authors": authors[:10],  # Cap at 10 authors
            "journal": journal,
            "published_date": pub_date or "",
            "doi": doi,
            "url": p.get("url", ""),
            "abstract": (abstract or "")[:2000],  # Cap abstract length
            "dimensions": dims,
            "subtopics": subs,
            "entities_mentioned": entities,
            "relevance_score": relevance,
            "scores": scores,
            "skepticism_flags": flags,
            "novelty_assessment": "",
            "key_findings": [],
            "clinical_implications": "",
            "added_date": TODAY,
            "last_reviewed": TODAY,
            "status": "new",
            "run_id": RUN_ID,
        }
        papers.append(paper)

    # Sort by relevance (highest first)
    papers.sort(key=lambda x: x["relevance_score"], reverse=True)

    result = {"papers": papers}
    with open(DATA_DIR / "papers.json", "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Processed {len(papers)} papers")
    print(f"  Relevance >= 8: {sum(1 for p in papers if p['relevance_score'] >= 8)}")
    print(f"  Relevance >= 5: {sum(1 for p in papers if p['relevance_score'] >= 5)}")

    # Print top papers
    print("\nTop 10 papers by relevance:")
    for p in papers[:10]:
        print(f"  [{p['relevance_score']}] {p['title'][:90]}")

    return papers


def process_trials():
    """Transform raw CT trials into trials.json schema."""
    with open(RAW_DIR / "ct_trials_raw.json") as f:
        raw = json.load(f)

    trials = []
    for t in raw:
        proto = t.get("protocolSection", {})
        ident = proto.get("identificationModule", {})
        status_mod = proto.get("statusModule", {})
        sponsor_mod = proto.get("sponsorCollaboratorsModule", {})
        desc_mod = proto.get("descriptionModule", {})
        cond_mod = proto.get("conditionsModule", {})
        design_mod = proto.get("designModule", {})
        arms_mod = proto.get("armsInterventionsModule", {})

        nct_id = ident.get("nctId", "")
        title = ident.get("briefTitle", "")
        sponsor = (sponsor_mod.get("leadSponsor") or {}).get("name", "")
        status = status_mod.get("overallStatus", "")
        phases = (design_mod.get("phases") or [])
        phase = ", ".join(phases) if phases else "N/A"
        enrollment = (design_mod.get("enrollmentInfo") or {}).get("count", 0)

        start_date = (status_mod.get("startDateStruct") or {}).get("date", "")
        completion = (status_mod.get("primaryCompletionDateStruct") or {}).get("date", "")

        interventions = arms_mod.get("interventions", [])
        intervention_names = ", ".join(i.get("name", "") for i in interventions) if interventions else ""

        summary = desc_mod.get("briefSummary", "")
        conditions = cond_mod.get("conditions", [])

        search_text = f"{title} {intervention_names} {summary}"
        dims, _ = classify_text(search_text)

        trial = {
            "nct_id": nct_id,
            "title": title,
            "sponsor": sponsor,
            "intervention": intervention_names,
            "phase": phase,
            "status": status,
            "primary_endpoint": "",
            "enrollment": enrollment or 0,
            "start_date": start_date,
            "expected_completion": completion,
            "dimensions": dims,
            "conditions": conditions,
            "latest_results_summary": "",
            "last_checked": TODAY,
            "change_log": [
                {"date": TODAY, "change": "Initial entry from baseline sweep"}
            ],
        }
        trials.append(trial)

    # Sort by status (recruiting first), then by start date
    status_order = {"RECRUITING": 0, "ACTIVE_NOT_RECRUITING": 1, "ENROLLING_BY_INVITATION": 2, "COMPLETED": 3}
    trials.sort(key=lambda x: (status_order.get(x["status"], 9), x.get("start_date", "")))

    result = {"trials": trials}
    with open(DATA_DIR / "trials.json", "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\nProcessed {len(trials)} trials")
    by_status = {}
    for t in trials:
        by_status[t["status"]] = by_status.get(t["status"], 0) + 1
    for status, count in sorted(by_status.items()):
        print(f"  {status}: {count}")

    return trials


def main():
    papers = process_papers()
    trials = process_trials()

    # Update run log
    run_log = {
        "runs": [{
            "run_id": RUN_ID,
            "mode": "baseline",
            "started_at": f"{TODAY}T08:00:00Z",
            "completed_at": datetime.now().isoformat() + "Z",
            "papers_found": len(papers),
            "papers_added": len(papers),
            "trials_updated": len(trials),
            "findings_updated": 0,
            "alerts_generated": 0,
            "errors": [],
            "token_usage_estimate": "baseline run",
        }]
    }
    with open(DATA_DIR / "run-log.json", "w") as f:
        json.dump(run_log, f, indent=2)

    print(f"\nBaseline processing complete!")


if __name__ == "__main__":
    main()
