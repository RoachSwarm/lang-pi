#!/bin/bash
INTENT="reveal"
CALLER="veil"
echo "[veil] Calling guardian with intent='$INTENT', caller='$CALLER'"
python3 "$MIRRORCORE_SYSTEM/guardian.py" "$INTENT" "$CALLER"
