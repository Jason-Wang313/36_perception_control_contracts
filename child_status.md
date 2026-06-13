# Child Status 36

Status: v2_hardened_workshop_only
Attempt: 3
Recovery: manual
V2 hardening timestamp: 2026-06-13 07:38:00 +01:00
PDF exists: True
PDF: C:\Users\wangz\Downloads\36.pdf
Desktop PDF: intentionally absent
Repository: https://github.com/Jason-Wang313/36_perception_control_contracts

Notes:
- V1 recovered the literature package, simulator, manuscript, and numbered PDF.
- V2 refactored `paper/run_demo.py` into reproducible baseline and stress modes.
- V2 added a mode-corruption stress showing that the controller-relative contract becomes less safe than the symmetric wrapper when mode labels are unreliable.
- V2 added the canonical build script, removed Desktop-copy language, and narrowed the claims to reliable local mode semantics.
