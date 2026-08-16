# ADPKD Research Intelligence System

A personal, self-hosted research-tracking system for **Autosomal Dominant Polycystic Kidney Disease (ADPKD)**. It continuously monitors the scientific literature and clinical-trial landscape, scores new findings for evidence quality and relevance, synthesizes them into living knowledge-base documents, and serves everything through a local web dashboard.

The system runs locally (built for a Mac Mini), uses [Claude Code](https://claude.com/claude-code) for autonomous research and synthesis, stores structured data as local JSON, and optionally syncs synthesized output to Google Drive.

> **Note:** This is a personal research tool, not medical advice. Findings are automatically summarized and may contain errors — always verify against primary sources and consult a qualified clinician.

---

## How it works

Two scheduled agents (macOS `launchd`) drive the pipeline:

| Agent | Schedule | Purpose |
|-------|----------|---------|
| `com.adpkd.scan` | Every 2–3 days | Light, fast sweep for new papers and trial updates |
| `com.adpkd.deep` | Weekly (Sunday) | Comprehensive synthesis and digest generation |

Each agent invokes Claude Code with a mode-specific prompt. A typical run:

1. Fetches papers from Semantic Scholar / PubMed and checks ClinicalTrials.gov for updates
2. Assesses relevance and novelty against the existing knowledge base
3. Scores evidence using a dedicated evaluation framework (study design, sample size, limitations)
4. Updates the structured data store (`data/*.json`)
5. Updates the synthesis documents and generates alerts for significant findings

```
launchd (scan / deep)
        │
        ▼
   Claude Code  ──► fetch → assess → score → update data → synthesize
        │
        ▼
   Data layer (data/*.json)  ──►  Output (knowledge base, digests, alerts)
        │                                     │
        ▼                                     ▼
   Next.js dashboard  ◄───── reads ─────  Google Drive sync (optional)
```

---

## Research taxonomy

The agent tracks ADPKD research across six dimensions, each mapped to a living knowledge-base document:

1. **Pharmacological treatments** — V2 antagonists, PKD1 correctors, RNA therapies, repurposed drugs, gene/stem-cell therapy
2. **Dietary & lifestyle** — hydration, sodium/protein restriction, ketosis, exercise
3. **Genetics & biomarkers** — PKD1/PKD2 variants, htTKV, novel biomarkers
4. **Clinical-trials pipeline** — active/recruiting trials and their status
5. **Disease management** — imaging, blood pressure, progression staging
6. **Patient community** — patient-relevant developments and resources

See [`adpkd-research-agent-spec.md`](adpkd-research-agent-spec.md) for the full design specification.

---

## Repository layout

```
├── prompts/           # Claude Code system prompts (scan, deep, baseline) + evaluation framework
├── scripts/           # Fetchers (PubMed/Semantic Scholar), runners, launchd plists, Drive sync
├── data/              # Structured JSON store: papers, trials, findings, run-log, user-state
├── output/
│   ├── knowledge-base/  # Six living synthesis documents
│   ├── digests/         # Weekly digests (YYYY-WXX)
│   ├── alerts/          # Dated significant-finding alerts
│   └── logs/            # Per-run logs (gitignored)
└── dashboard/         # Next.js web dashboard
```

### Data store (`data/`)

| File | Contents |
|------|----------|
| `papers.json` | Tracked papers with metadata, scores, and summaries |
| `trials.json` | ClinicalTrials.gov records being followed |
| `findings.json` | Scored, synthesized findings |
| `run-log.json` | History of every scan/deep run |
| `user-state.json` | Dashboard read/seen state |

---

## Dashboard

A [Next.js](https://nextjs.org) 16 + React 19 app (Tailwind CSS 4, shadcn/ui, Recharts) that reads directly from `data/` and `output/`. Pages: overview, papers, trials, digests, and knowledge base.

```bash
cd dashboard
npm install
npm run build
npm run start   # serves on http://localhost:3000
```

> **Always run the dashboard in production mode** (`build` + `start`). Dev mode (Turbopack) has been observed to spawn runaway node processes.

---

## Setup

### Prerequisites

- macOS (uses `launchd` for scheduling)
- [Claude Code](https://claude.com/claude-code)
- Python 3 and Node.js
- (Optional) A [Semantic Scholar API key](https://www.semanticscholar.org/product/api) for higher rate limits

### 1. API keys

Create `data/.api-keys.json` (gitignored — never commit real keys):

```json
{
  "semantic_scholar": "YOUR_KEY_HERE",
  "ncbi": ""
}
```

### 2. Paths

The prompts, scripts, and `launchd` plists in this repo use absolute paths for one machine. Update them to your own project location before running.

### 3. Baseline

Run the baseline fetch/process to build the initial corpus:

```bash
python3 scripts/baseline_fetch.py
python3 scripts/baseline_process.py
```

### 4. Schedule the agents

Copy the plists to `~/Library/LaunchAgents/` and load them:

```bash
cp scripts/com.adpkd.scan.plist ~/Library/LaunchAgents/
cp scripts/com.adpkd.deep.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.adpkd.scan.plist
launchctl load ~/Library/LaunchAgents/com.adpkd.deep.plist
```

---

## License

Personal project shared for reference. No warranty; use at your own risk. Not medical advice.
