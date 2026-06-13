# Submission Version Log

## v1

- Recovered draft manuscript, literature package, simulator, and initial numbered PDF.
- Main result: controller-relative contract collision rate 0.010 and blocked-step rate 0.434 versus symmetric wrapper collision rate 0.014 and blocked-step rate 0.832.

## v2

- Added explicit submission-hardening version marker in the paper.
- Refactored `paper/run_demo.py` into baseline and `--stress-only` modes.
- Added `docs/mode_corruption_stress.csv` and `docs/mode_corruption_stress_table.tex`.
- Added v2 negative result: under 20% mode-label error, relative-contract collisions rise to 0.020, worse than the symmetric wrapper's 0.014.
- Narrowed claims to reliable mode semantics and calibrated local assumptions.
- Added canonical Downloads-only PDF build script.
- Decision: workshop-only / strong-revise.

