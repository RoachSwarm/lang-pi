#!/bin/bash
PHRASE="$1"
echo "[🎙️] Speak invoked..."
if command -v espeak &> /dev/null; then
    espeak "$PHRASE"
else
    echo "⟁ espeak not found. Install it to enable voice output."
fi
