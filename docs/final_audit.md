# Final Audit

Generated: 2026-06-13 07:38:00 +01:00

## Decision

Workshop-only / strong-revise. The core mechanism is clear and reproducible, but the evidence is a toy one-step navigation simulator with no hardware, no broader benchmark, and no universal theorem.

## Thesis

Perception-control contracts should be synthesized relative to the downstream controller's invariant and mode structure, not as controller-agnostic uncertainty sets around perception outputs.

## Positive Evidence

- Baseline simulator: symmetric interval wrapper collision rate 0.014 and blocked-step rate 0.832.
- Controller-relative contract under reliable mode labels: collision rate 0.010 and blocked-step rate 0.434.
- Mechanism-level contribution: the admissible perception-output set is derived from the controller safety inequality rather than from perception error statistics alone.

## V2 Negative Evidence

- The v2 mode-corruption stress attacks the hidden reliable-mode assumption.
- At 20% mode-label error, the controller-relative collision rate is 0.020, worse than the symmetric wrapper's 0.014.
- At 40% mode-label error, the controller-relative collision rate rises to 0.029.
- The supported claim is therefore calibrated controller-relative admissibility, not universal dominance over conservative wrappers.

## Closest Hostile Prior Work

- Learning-based inverse perception contracts and applications.
- Gaussian mixture inverse perception contracts for uncertainty-aware robot navigation.
- Semantic perception-action pipelines for safe control.
- Runtime verification and assume-guarantee contracts for robotic systems.

## Remaining Weaknesses

- One-dimensional, one-step toy navigation setting.
- No hardware validation.
- No statistical confidence intervals beyond fixed-seed reproducibility and deterministic stress sweep.
- No general synthesis theorem for arbitrary controllers.
- Requires reliable mode semantics or a mode-calibration layer.

## Reproducibility Artifacts

- `paper/run_demo.py`
- `paper/demo_results.txt`
- `docs/mode_corruption_stress.csv`
- `docs/mode_corruption_stress_table.tex`
- `scripts/build_pdf.ps1`

## Artifact Policy

- Canonical PDF path: `C:/Users/wangz/Downloads/36.pdf`
- GitHub URL: `https://github.com/Jason-Wang313/36_perception_control_contracts`
- Visible Desktop copy: intentionally absent in v2.
- Local tracked/generated paper PDF: removed after v2 build.
