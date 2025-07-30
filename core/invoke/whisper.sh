#!/bin/bash
LOG="$HOME/mirrorcore/core/memorybook/whisper.md"
PHRASE="$1"
echo "[🕊️] Whisper invoked..."
echo "☲ $PHRASE"
echo "$(date '+%Y-%m-%d %H:%M:%S') :: $PHRASE" >> "$LOG"
