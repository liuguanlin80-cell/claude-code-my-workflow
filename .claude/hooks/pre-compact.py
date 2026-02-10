#!/usr/bin/env python3
"""Save context snapshot before compaction. Windows-compatible replacement for pre-compact.sh."""
import json
import sys
import glob
import os
from datetime import datetime

try:
    hook_input = json.load(sys.stdin)
except (json.JSONDecodeError, EOFError):
    hook_input = {}

trigger = hook_input.get("trigger", "unknown")
project_dir = hook_input.get("cwd", os.environ.get("CLAUDE_PROJECT_DIR", "."))
log_dir = os.path.join(project_dir, "quality_reports", "session_logs")

if not os.path.isdir(log_dir):
    sys.exit(0)

logs = sorted(glob.glob(os.path.join(log_dir, "*.md")), key=os.path.getmtime, reverse=True)
if logs:
    try:
        with open(logs[0], "a", encoding="utf-8") as f:
            f.write(f"\n---\n**Context compaction ({trigger}) at {datetime.now().strftime('%H:%M')}**\n")
            f.write("Check git log and quality_reports/plans/ for current state.\n")
    except OSError:
        pass

sys.exit(0)
