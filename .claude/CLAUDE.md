# ADPKD Research Project

## Dashboard

- **Port**: 3000 (Lymphedema uses 3001)
- **IMPORTANT — always use production mode** (`npm run build && npm run start`), never `npm run dev`. Dev mode (Turbopack) causes runaway node process spawning that crashes the Mac Mini. The `.claude/launch.json` and `scripts/start-dashboard.sh` are both configured for production mode.
- After any code change to the dashboard, run `npm run build` in `dashboard/` before starting.
- Network-accessible on all interfaces via `--hostname 0.0.0.0`.

## LaunchD Agents

- `com.adpkd.scan` — scheduled scan agent
- `com.adpkd.deep` — scheduled deep analysis agent
- Installed in `~/Library/LaunchAgents/`, source plists in `scripts/`.

## Data Pipeline

- Dashboard reads from `../data/` and `../output/` relative to the dashboard dir.
