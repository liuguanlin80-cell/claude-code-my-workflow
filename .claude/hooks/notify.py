#!/usr/bin/env python3
"""Windows notification when Claude needs attention. Replaces macOS osascript notify.sh."""
import json
import sys

try:
    hook_input = json.load(sys.stdin)
except (json.JSONDecodeError, EOFError):
    sys.exit(0)

# Silently exit -- Windows toast notifications are complex and optional.
# Users can replace this with a preferred notification method.
# For PowerShell toast: see _archive/hooks/ for examples.
sys.exit(0)
