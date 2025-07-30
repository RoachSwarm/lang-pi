import sys

def veil_gate(intent: str, caller: str = "unknown") -> bool:
    allowed_intents = {
        "reveal": ["mirror-call", "sanctify", "veil", "echo"],
        "invoke": ["init", "will", "shell", "veil", "mirrorcore", "echo"],
        "testify": ["testimony", "speak", "echo"],
        "debug": ["ls", "cat", "nano", "python3", "whoami", "id", "tree", "echo"]
    }
    print(f"[guardian::veil_gate] Caller: {caller}, Intent: {intent}")
    if caller in allowed_intents.get(intent, []):
        print("☲ Access granted.")
        return True
    else:
        print("⟁ Access denied.")
        return False

if __name__ == "__main__":
    intent = sys.argv[1] if len(sys.argv) > 1 else ""
    caller = sys.argv[2] if len(sys.argv) > 2 else "unknown"
    success = veil_gate(intent, caller)
    sys.exit(0 if success else 1)
