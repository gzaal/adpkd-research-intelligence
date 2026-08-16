#!/bin/bash
# ADPKD Research Scan — runs every 2-3 days via launchd
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="$PROJECT_DIR/output/logs"

mkdir -p "$LOG_DIR"

cd "$PROJECT_DIR"
claude --print \
  --permission-mode bypassPermissions \
  --add-dir "$PROJECT_DIR" \
  -p "$(cat prompts/scan.md)" \
  2>&1 | tee -a "$LOG_DIR/scan-$(date +%Y%m%d).log"
