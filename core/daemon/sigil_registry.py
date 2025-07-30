#!/usr/bin/env python3

import sys
import json
import os
from datetime import datetime

registry_path = os.path.expanduser("~/mirrorcore/core/daemon/sigil_registry.json")
log_path = os.path.expanduser("~/mirrorcore/core/log/sigil_registry.log")

def load_registry():
    if os.path.exists(registry_path):
        with open(registry_path, 'r') as f:
            return json.load(f)
    return {}

def save_registry(data):
    with open(registry_path, 'w') as f:
        json.dump(data, f, indent=2)

def log_entry(entry):
    with open(log_path, 'a') as log:
        log.write(f"[{datetime.now()}] {entry}\n")

def bind(sigil, target):
    registry = load_registry()
    registry[sigil] = target
    save_registry(registry)
    log_entry(f"Bound sigil {sigil} → {target}")
    print(f"⟁ Sigil {sigil} bound to {target}")

def get(sigil):
    registry = load_registry()
    if sigil in registry:
        print(f"{sigil} → {registry[sigil]}")
    else:
        print(f"⟁ Unknown sigil: {sigil}")

def list_all():
    registry = load_registry()
    if not registry:
        print("⟁ No sigils bound.")
        return
    for sigil, target in registry.items():
        print(f"{sigil} → {target}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ["--help", "-h"]:
        print("Usage:")
        print("  sigil_registry.py bind 🜂 breath")
        print("  sigil_registry.py get 🜂")
        print("  sigil_registry.py list")
        sys.exit(0)

    command = args[0]

    if command == "bind" and len(args) == 3:
        bind(args[1], args[2])
    elif command == "get" and len(args) == 2:
        get(args[1])
    elif command == "list":
        list_all()
    else:
        print("⟁ Invalid usage. Try: bind/get/list")
