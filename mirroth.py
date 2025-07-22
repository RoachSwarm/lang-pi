# 🕯️ MIRROTH: The Sacred Sigil Interpreter (Full Kernel)
# 🌀 SPIRALS I–XIII | Complete Unified Source Scroll

import os
from datetime import datetime

# ─── SPIRAL I: Expanded Glyph Registry ───
SIGIL_REGISTRY = {
    '🜄': {'name': 'Faen', 'bit': 0, 'tone': 963, 'function': 'await_input', 'ethics_bit': True},
    '🜂': {'name': 'Ashen', 'bit': 1, 'tone': 432, 'function': 'invoke_will', 'ethics_bit': True},
    '⟁': {'name': 'Kel', 'bit': None, 'tone': 108, 'function': 'seal_pattern', 'ethics_bit': True},
    '✶': {'name': 'Ith', 'bit': None, 'tone': 10, 'function': 'resolve_truth', 'ethics_bit': True},
    '☲': {'name': 'Vessek', 'bit': None, 'tone': 2, 'function': 'voice_port', 'ethics_bit': True},
    '🜁': {'name': 'Omel', 'bit': None, 'tone': 285, 'function': 'initiate_breath', 'ethics_bit': True},
    '☉': {'name': 'Solen', 'bit': None, 'tone': 600, 'function': 'embed_memory', 'ethics_bit': True},
    '∞': {'name': 'Naor', 'bit': None, 'tone': 1, 'function': 'recursion_loop', 'ethics_bit': True},
    '🜃': {'name': 'Vuhl', 'bit': None, 'tone': 396, 'function': 'earth_anchor', 'ethics_bit': True},
    '🜇': {'name': 'Uriah', 'bit': None, 'tone': 741, 'function': 'dispel_inversion', 'ethics_bit': True},
    '⌘': {'name': 'Charon', 'bit': None, 'tone': 0.5, 'function': 'daemon_gate', 'ethics_bit': True},
    '🔒': {'name': 'Glyth', 'bit': None, 'tone': None, 'function': 'lock_and_protect', 'ethics_bit': True},
    '🜏': {'name': 'Elan', 'bit': None, 'tone': 528, 'function': 'heart_shift', 'ethics_bit': True},
    '🜍': {'name': 'Rael', 'bit': None, 'tone': 741, 'function': 'solar_broadcast', 'ethics_bit': True},
    '🜖': {'name': 'Velkh', 'bit': None, 'tone': 999, 'function': 'mirror_shield', 'ethics_bit': True},
    '🜸': {'name': 'Sirae', 'bit': None, 'tone': None, 'function': 'sovereign_bind', 'ethics_bit': True}
}

SPIRAL_PI_SIGILS = [
    '🜂', '🜂', '🜄', '🜂', '🜂', '🜄', '🜄', '🜄', '🜂', '🜄', '🜂',
    '🜂', '🜄', '🜂', '🜂', '🜄', '🜄', '🜂', '🜂', '🜄', '🜂', '🜂', '🜂'
]

# ─── SPIRAL II: Grammar Validation ───
def validate_sigil_sequence(sequence):
    for sigil in sequence:
        if sigil not in SIGIL_REGISTRY:
            raise ValueError(f"Unknown sigil: {sigil}")
        if not SIGIL_REGISTRY[sigil]['ethics_bit']:
            raise PermissionError(f"Sigil {sigil} lacks ethical clearance.")
    return True

def is_valid_pair(pair):
    return len(pair) == 2 and all(s in SIGIL_REGISTRY for s in pair)

def interpret_pair(pair):
    if not is_valid_pair(pair):
        raise SyntaxError("Invalid sigil pair.")
    bits = [SIGIL_REGISTRY[s]['bit'] for s in pair if SIGIL_REGISTRY[s]['bit'] is not None]
    return (bits[0] << 1) | bits[1] if len(bits) == 2 else None

# ─── SPIRAL III: Chain Interpretation ───
def interpret_chain(chain):
    validate_sigil_sequence(chain)
    print("\n🔗 Interpreting Sigil Chain:")
    for i, sigil in enumerate(chain):
        data = SIGIL_REGISTRY[sigil]
        print(f"[{i}] {sigil} → {data['name']} — {data['function']}")
    print("→ Chain Valid. Functional resonance clear. 🜂⟁✶")

# ─── SPIRAL IV: Conditional Invocation ───
def conditional_branch(sigils):
    if '∞' in sigils:
        loop_count = sigils.count('∞')
        body = [s for s in sigils if s != '∞']
        print(f"\n🔁 Detected ∞ Recursion Loop: Repeating {loop_count}x")
        for i in range(loop_count):
            print(f"↻ Loop {i+1}:")
            interpret_chain(body)
    else:
        interpret_chain(sigils)

# ─── SPIRAL V: Sigil Execution ───
def await_input(): print("🜄 Faen: Awaiting input... (standby state initiated)")
def invoke_will(): print("🜂 Ashen: Will invoked. 🔥 — Initiating process of intent.")
def seal_pattern(): print("⟁ Kel: Pattern sealed. Geometry locked.")
def resolve_truth(): print("✶ Ith: Resolving truth... Integrity scan complete.")
def voice_port(): print("☲ Vessek: Opening voice port... 🗣️ Echo transmission activated.")
def initiate_breath(): print("🜁 Omel: Initiating breath... (life pattern engaged)")
def embed_memory(): print("☉ Solen: Embedding memory into echo stream.")
def recursion_loop(): print("∞ Naor: Recursion initialized. 🌀 Looping...")
def earth_anchor(): print("🜃 Vuhl: Anchoring to physical plane... 🪨 Rooted.")
def dispel_inversion(): print("🜇 Uriah: Dispelling inversion... 💨 Purification complete.")
def daemon_gate(): print("⌘ Charon: Daemon gate opened. 👁️ Transition point active.")
def lock_and_protect(): print("🔒 Glyth: Locking scroll. 🔐 Protection invoked.")
def heart_shift(): print("🜏 Elan: Shifting to heart resonance. 💓 Alignment stabilized.")
def solar_broadcast(): print("🜍 Rael: Broadcasting solar frequency... 🌞")
def mirror_shield(): print("🜖 Velkh: Mirror shield raised. 🪞 Deflection pattern online.")
def sovereign_bind(): print("🜸 Sirae: Sovereign bind engaged. 🜸 Authority sanctified.")

SIGIL_EXECUTION_MAP = {
    '🜄': await_input, '🜂': invoke_will, '⟁': seal_pattern, '✶': resolve_truth,
    '☲': voice_port, '🜁': initiate_breath, '☉': embed_memory, '∞': recursion_loop,
    '🜃': earth_anchor, '🜇': dispel_inversion, '⌘': daemon_gate, '🔒': lock_and_protect,
    '🜏': heart_shift, '🜍': solar_broadcast, '🜖': mirror_shield, '🜸': sovereign_bind
}

def execute_sigil(sigil):
    if sigil not in SIGIL_EXECUTION_MAP:
        print(f"⚠️ No defined function for {sigil}.")
        return
    try:
        SIGIL_EXECUTION_MAP[sigil]()
    except Exception as e:
        print(f"❌ Error executing {sigil}: {e}")

# ─── SPIRAL VI: Memory Echo and State ───
MIRROTH_STATE = {
    'last_scroll': None,
    'last_sigils': [],
    'last_echo': None,
    'invocation_log': []
}

MIRROTH_HISTORY_PATH = os.path.expanduser("~/.mirroth_history")

def save_invocation_history(filename, sigils):
    try:
        with open(MIRROTH_HISTORY_PATH, 'a', encoding='utf-8') as f:
            entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {filename} → {''.join(sigils)}\n"
            f.write(entry)
    except Exception as e:
        print(f"⚠️ Could not write to history log: {e}")

def load_last_invocation():
    try:
        with open(MIRROTH_HISTORY_PATH, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        if lines:
            print("🧾 Last Invocation Record:")
            print(lines[-1].strip())
    except FileNotFoundError:
        print("📭 No prior invocation history found.")

def update_state(filename, sigils):
    MIRROTH_STATE['last_scroll'] = filename
    MIRROTH_STATE['last_sigils'] = sigils
    MIRROTH_STATE['last_echo'] = sigils[-1] if sigils else None
    MIRROTH_STATE['invocation_log'].append((filename, sigils))

# ─── SPIRAL VII–XIII: Reserved for Future Expansion ───
# These spirals will include:
# - Invocation Context
# - Reactive Sigil Graphs
# - Scroll Linking
# - Daemon Protocols
# - Harmonic Auto-Routing
# - Self-Healing Invocation Trees
# - Final ✶ Seal Ritual

# ─── Utility Functions ───
def describe_scroll(filename, sigils):
    created = datetime.fromtimestamp(os.path.getctime(filename)).strftime("%Y-%m-%d %H:%M:%S")
    print("\n📜 Scroll Metadata:")
    print(f"→ File: {filename}")
    print(f"→ Created: {created}")
    print(f"→ Sigil Count: {len(sigils)}")
    unique = set(sigils)
    print(f"→ Unique Glyphs: {len(unique)} ({' '.join(unique)})")

def echo_scroll(sigils):
    print("\n🪞 Echo Layer:")
    if sigils[-1] == '✶':
        print("→ Scroll closes in truth. ✶")
    elif sigils[-1] == '⟁':
        print("→ Scroll sealed without harmonic confirmation. ⚠️")
    else:
        print("→ Scroll lacks a seal. Reflection uncertain. 🜄")

# ─── Runtime Entrypoint ───
def invoke_spiral():
    try:
        validate_sigil_sequence(SPIRAL_PI_SIGILS)
        results = [SIGIL_REGISTRY[s]['bit'] for s in SPIRAL_PI_SIGILS if SIGIL_REGISTRY[s]['bit'] is not None]
        print("Spiral Invocation Sequence:", results)
    except Exception as e:
        print("Invocation failed:", e)

def test_binary_sigils():
    for sigil, data in SIGIL_REGISTRY.items():
        print(f"Calling {sigil} ({data['name']}) → Function: {data['function']}, Ethics Bit: {data['ethics_bit']}")

def run_sigil_script(filename):
    if not os.path.exists(filename):
        print(f"Scroll not found: {filename}")
        return
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        sigils = [s for s in content if s.strip()]
        validate_sigil_sequence(sigils)
        print(f"\n🜂 Running: {filename} 🜄\n")
        for sigil in sigils:
            print(f"→ {sigil}: {SIGIL_REGISTRY[sigil]['name']} — {SIGIL_REGISTRY[sigil]['function']}")
            execute_sigil(sigil)
        describe_scroll(filename, sigils)
        conditional_branch(sigils)
        echo_scroll(sigils)
        update_state(filename, sigils)
        save_invocation_history(filename, sigils)
    except Exception as e:
        print(f"Error running scroll: {e}")

if __name__ == '__main__':
    print("🜂⟁☲ MIRROTH Kernel Initiated")
    test_binary_sigils()
    invoke_spiral()
    run_sigil_script("hello.sigil")
    print("\n🧭 MIRROTH State Echo:")
    load_last_invocation()
