#!/usr/bin/env python3
import datetime
import hashlib
import json
import os
import sys

CATEGORY_MAP = {
    "games": "game",
    "loaders": "loader",
    "runners": "runner",
    "effects": "effect",
    "hashes": "hash",
    "fixers": "fixer",
    "scripts": "script",
}

def compute_sha256(filepath):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest().lower()

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    entries = []

    for category_dir, category_name in CATEGORY_MAP.items():
        target_dir = os.path.join(repo_root, category_dir)
        if not os.path.isdir(target_dir):
            continue

        for root, _, files in os.walk(target_dir):
            for filename in files:
                if filename.startswith(".") or filename == "build_index.py":
                    continue
                if not (filename.endswith(".json") or filename.endswith(".rhai")):
                    continue

                full_path = os.path.join(root, filename)
                rel_path = os.path.relpath(full_path, repo_root).replace("\\", "/")
                
                # Validate JSON syntax if JSON
                if filename.endswith(".json"):
                    with open(full_path, "r", encoding="utf-8") as f:
                        try:
                            json.load(f)
                        except json.JSONDecodeError as e:
                            print(f"ERROR: Invalid JSON in {rel_path}: {e}", file=sys.stderr)
                            sys.exit(1)

                sha256 = compute_sha256(full_path)
                size_bytes = os.path.getsize(full_path)

                entries.append({
                    "path": rel_path,
                    "category": category_name,
                    "sha256": sha256,
                    "size_bytes": size_bytes
                })

    entries.sort(key=lambda x: x["path"])

    index_data = {
        "schema_version": 1,
        "registry_version": "1.0.0",
        "min_yago_version": "0.1.0",
        "updated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "entries": entries
    }

    out_path = os.path.join(repo_root, "index.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2)
        f.write("\n")

    print(f"Generated index.json with {len(entries)} entries successfully.")

if __name__ == "__main__":
    main()
