#!/bin/bash
# Installiert die Werkzeuge für Word-Materialien in Cloud-Sitzungen.
set -euo pipefail
[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0
python3 -c "import docx, playwright" 2>/dev/null || pip install -q python-docx playwright >/dev/null 2>&1 || true
