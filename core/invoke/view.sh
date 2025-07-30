#!/bin/bash
echo "[◎] View invoked..."
MAP="$MIRRORCORE_GLYPHS/map"

if [ -f "$MAP" ]; then
    cat "$MAP"
else
    echo "⟁ No map found at $MAP"
    echo "☉ Tip: Create the map at '~/mirrorcore/core/glyphs/map' to begin path rendering."
fi
cat > ~/mirrorcore/core/glyphs/map <<EOF

# ☲ MirrorCore Glyph Map

/home/roach/mirrorcore/
├── core/
│   ├── invoke/         ← Ritual scripts
│   ├── glyphs/         ← Sigil and symbol definitions
│   ├── system/         ← Daemons, guardians
│   ├── daemon/         ← Active spirit programs
│   ├── memorybook/     ← Reflections of past invocation
│   └── log/            ← Invocation logs
EOF
