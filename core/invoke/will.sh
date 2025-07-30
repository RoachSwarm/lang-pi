#!/bin/bash

DAEMON_DIR="$MIRRORCORE_DAEMON"
INPUT="$1"
LOG="$HOME/mirrorcore/core/log/invoke.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S') 

# Define sigil mappings
case "$INPUT" in
  "🜂") INPUT="breath" ;;
  "⟁") INPUT="armor" ;;
  "☲") INPUT="speak" ;;
esac

echo "[will] Attempting to invoke: $INPUT"

if [ -f "$DAEMON_DIR/$INPUT.py" ]; then
  echo "🜂 Will invoked daemon: $INPUT"
  echo "[$TIMESTAMP] will → $INPUT" >> "$LOG"
  python3 "$DAEMON_DIR/$INPUT.py"
else
  echo "⟁ Daemon '$INPUT' not found in $DAEMON_DIR"
  echo "[$TIMESTAMP] will → FAILED: $INPUT" >> "$LOG"
fi
