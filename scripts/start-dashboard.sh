#!/bin/bash
# Start the ADPKD Research Dashboard (production mode)
# Serves on all interfaces at port 3000
set -euo pipefail

export PATH="/opt/homebrew/opt/node@22/bin:$HOME/.local/bin:$PATH"
DASHBOARD_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/dashboard"

cd "$DASHBOARD_DIR"

# Rebuild if source changed since last build
if [ ! -d ".next" ] || [ "$(find app lib components -newer .next/BUILD_ID -name '*.tsx' -o -name '*.ts' 2>/dev/null | head -1)" ]; then
  echo "Building dashboard..."
  npm run build
fi

echo "Starting dashboard at http://0.0.0.0:3000"
exec npm run start -- --hostname 0.0.0.0 --port 3000
