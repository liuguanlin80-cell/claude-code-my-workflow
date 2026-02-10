#!/usr/bin/env python3
"""Block accidental edits to protected files. Windows-compatible replacement for protect-files.sh."""
import json
import sys
import os

try:
    hook_input = json.load(sys.stdin)
except (json.JSONDecodeError, EOFError):
    sys.exit(0)

tool = hook_input.get("tool_name", "")
file_path = ""
if tool in ("Edit", "Write"):
    file_path = hook_input.get("tool_input", {}).get("file_path", "")

if not file_path:
    sys.exit(0)

basename = os.path.basename(file_path)
PROTECTED = [
    "Bibliography_base.bib",
    "settings.json",
    "\u8bba\u6587_word\u7248.docx",
]

if basename in PROTECTED:
    print(
        f"BLOCKED: {basename} is protected. Edit manually or update PROTECTED list in .claude/hooks/protect-files.py",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
