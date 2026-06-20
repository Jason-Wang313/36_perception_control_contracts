# Final Audit

Generated: 2026-06-15 +01:00

## Decision

Final v3 full-scale deterministic submission artifact for Paper 36. The prior v2 stopping state has been superseded by a 25-page manuscript with a large deterministic suite, generated figures/tables, explicit negative controls, and verified canonical PDF export.

## Thesis

Perception-control contracts should be synthesized relative to the downstream controller's admissibility condition, not treated as controller-agnostic uncertainty sets around perception outputs.

## Positive Evidence

- 10 task families, 12 perception regimes, 14 interfaces, 96 seeds per cell, 160 represented control steps, 33 hypotheses, and 6-step lookahead.
- 5,109,350,400 represented admissibility checks.
- 161,280 seed-level rows and 1,680 aggregate rows.
- Adaptive mode-calibrated contract: 7.25 collisions per seed and 0.52 blocked fraction.
- Robust one-sided contract: 4.77 collisions per seed and 0.70 blocked fraction.
- Oracle admissibility contract: 0.66 collisions per seed and 0.36 blocked fraction.

## Negative Evidence

- Point-estimate controller averages 93.95 collisions per seed.
- Overconfident controller-relative contract averages 80.42 collisions per seed, proving that geometry without calibration is unsafe.
- Symmetric wrappers remain valuable conservative fallbacks when mode semantics are unreliable.
- Combined perception shift stresses every non-oracle method.

## Unsupported Claims Not Made

- Hardware safety.
- Learned vision model performance.
- Universal dominance over conservative wrappers.
- Formal synthesis theorem for arbitrary controllers.

## Reproducibility Artifacts

- `scripts/run_full_scale_perception_contract_suite.py`
- `results/full_scale/seed_metrics.csv`
- `results/full_scale/aggregate_metrics.csv`
- `results/full_scale/experiment_summary.json`
- `results/full_scale/experiment_validation.json`
- `results/full_scale/validation.json`
- `figures/full_scale/*.pdf`
- `scripts/build_pdf.ps1`

## Artifact Policy

- Canonical PDF path: `C:/Users/wangz/Downloads/36.pdf`
- SHA256: `F9CD804DFC345B0111BEB680CF0B0E9BD78C5C20D5A2D4D61AFD2FAF85FBB8D1`
- Page count: 25
- Local tracked/generated paper PDF: removed after canonical build.
- Visible Desktop copy: intentionally absent.
- VLA-style link-box check: passed on pages 2, 5, 11, and 25 with 21 green citation/URL boxes, 3 red internal-reference boxes, and 24 visible one-point borders.
