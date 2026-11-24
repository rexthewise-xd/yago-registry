# YAGO Community Registry (`yago-registry`)

This repository serves as the official registry index and manifest distribution source for **YAGO** (Yet Another Game Organizer).

It distributes declarative definitions for:
- **Game Profiles & Launchers** (`games/`)
- **Mod Loader Configurations** (`loaders/`)
- **Compatibility Runner Sources** (`runners/`)
- **Shared Effect Libraries** (`effects/`)
- **Character & Object Hashes** (`hashes/`)
- **Patch Fixer Rules** (`fixers/`)

---

## Repository Structure

```
yago-registry/
├── games/          # Game templates & manifests (*.json)
├── loaders/        # 3DMigoto/XXMI loader specifications (*.json)
├── runners/        # Proton/Wine runner source feeds (*.json)
├── effects/        # Shared effect library specifications (*.json)
├── hashes/         # Game-specific hash databases (*.json)
├── fixers/         # Automated patch fixer rulesets (*.json)
├── scripts/        # Registry maintenance utilities
│   └── build_index.py
├── index.json      # Master SHA-256 index consumed by YAGO clients
└── README.md
```

---

## Contributing

### 1. Adding or Updating a Game Manifest
1. Place or edit your manifest under `games/<game_id>.json`.
2. Ensure `gamebanana_id` and `loader_id` are specified if supported.
3. Validate JSON formatting.

### 2. Adding or Updating Hashes or Fixer Rules
1. Hashes: Add or edit `hashes/<game_id>.json`.
2. Fixers: Add or edit `fixers/<game_id>.json`.

### 3. Rebuilding the Master Index
Whenever you add or modify any files, run the index builder:

```bash
python3 scripts/build_index.py
```

This updates `index.json` with deterministic SHA-256 digests and file sizes. CI will automatically verify that `index.json` matches the committed files.
