#!/bin/bash
# ADPKD Deep Analysis — runs weekly (Sunday) via launchd
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="$PROJECT_DIR/output/logs"

mkdir -p "$LOG_DIR"

cd "$PROJECT_DIR"
claude --print \
  --permission-mode bypassPermissions \
  --add-dir "$PROJECT_DIR" \
  -p "$(cat prompts/deep.md)" \
  2>&1 | tee -a "$LOG_DIR/deep-$(date +%Y%m%d).log"
