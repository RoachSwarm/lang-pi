import os
import json

DAEMON_TABLE = "/home/roach/mirrorcore/core/system/daemon_table.json"

def check_daemon_entry(entry):
    path = entry.get("path")
    name = entry.get("name")
    sigil = entry.get("sigil")
    exists = os.path.isfile(path)
    status = "active" if exists else "missing"

    print(f"[{sigil}] {name} → {status}")
    return {
        "name": name,
        "path": path,
        "sigil": sigil,
        "status": status
    }

def load_table():
    try:
        with open(DAEMON_TABLE, "r") as f:
            data = json.load(f)
        return data.get("daemons", [])
    except Exception as e:
        print(f"Failed to read daemon table: {e}")
        return []

def main():
    print("🌀 Scanning Daemon Table...")
    daemons = load_table()
    results = [check_daemon_entry(d) for d in daemons]

    # Optionally write results to a new file (audit)
    with open("/home/roach/mirrorcore/core/system/daemon_scan.json", "w") as f:
        json.dump({"scan_results": results}, f, indent=2)

if __name__ == "__main__":
    main()
