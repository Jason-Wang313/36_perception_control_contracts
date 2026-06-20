# Paper 36 Full-Scale Execution Plan

## Working Rule

Work only on Paper 36 until it reaches a final verified state. Do not copy any
PDF to `C:/Users/wangz/Downloads/36.pdf` until the manuscript is at least 25
pages and the local build, log scan, text scan, and visual render check all
pass. Keep RAM usage light by streaming seed-level rows, storing only aggregate
accumulators, retaining one representative trace, and writing compact vector
figures.

## Current State Before V3

- Repository: `C:/Users/wangz/robotics_60_paper_batch/36_perception_control_contracts`.
- Worktree state at start: clean.
- Canonical Downloads PDF at start: absent, despite stale v2 status docs claiming it exists.
- Last recorded build: 4 pages.
- Current evidence: one small stochastic navigation demo plus a mode-corruption stress.
- Core weakness to fix: the paper currently supports only a small one-step mechanism. It needs a broad controller-relative contract study with multiple controller invariants, perception regimes, interface baselines, and failure modes.

## V3 Target

Turn the paper into a 25+ page final full-scale manuscript arguing that
perception-control contracts should be synthesized from downstream controller
admissibility conditions rather than from controller-agnostic perception
uncertainty alone.

The central claim will remain scoped:

> The useful contract at the perception-control boundary is the set of
> perception outputs under which the controller's local invariant still holds.
> Symmetric uncertainty wrappers, confidence ellipsoids, and generic perception
> scores are often mismatched to this controller-relative admissibility set.

The strengthened evidence will add:

- Positive findings for controller-relative contracts under reliable mode semantics.
- Negative findings under mode corruption, semantic aliasing, latency, false negatives, and calibration drift.
- Direct comparisons against symmetric intervals, ellipsoids, conformal wrappers, semantic confidence gating, CBF/MPC filters with raw perception uncertainty, fixed controller-relative contracts, adaptive mode-calibrated contracts, robust contracts, overconfident contracts, and oracle limits.
- Analysis of safety-conservatism tradeoffs, blocked-action rates, collision rates, false-admit rates, false-block rates, and controller utility.
- A full appendix explaining how to derive one-sided and mode-specific admissible perception sets from controller inequalities.

## Full-Scale Experiment Design

Add `scripts/run_full_scale_perception_contract_suite.py`.

### Task Families

Use 10 low-dimensional but controller-interpretable robot task families:

1. one-step obstacle braking,
2. corridor centerline keeping,
3. doorway clearance,
4. pedestrian crossing,
5. pallet approach with one-sided depth bound,
6. narrow-gap passage,
7. moving obstacle intercept,
8. semantic stop-zone entry,
9. occluded obstacle emergence,
10. two-constraint docking.

Each family defines the controller invariant, the perception output channels,
the controller action rule, and the controller-relative admissible perception
set.

### Perception Stress Regimes

Use 12 regimes:

1. reliable nominal mode,
2. mild Gaussian noise,
3. heavy-tailed noise,
4. bimodal aliasing,
5. mode-label corruption,
6. semantic false positive,
7. semantic false negative,
8. delayed perception,
9. range-scale drift,
10. asymmetric near-obstacle bias,
11. clutter burst,
12. combined perception shift.

### Interfaces

Compare 14 perception-control interfaces:

1. point-estimate controller,
2. symmetric interval wrapper,
3. ellipsoid wrapper,
4. conformal perception wrapper,
5. semantic confidence gate,
6. CBF filter with generic uncertainty,
7. MPC filter with generic uncertainty,
8. fixed controller-relative contract,
9. adaptive mode-calibrated contract,
10. robust one-sided contract,
11. risk-budgeted contract,
12. residual calibrated contract,
13. overconfident controller-relative contract,
14. oracle admissibility contract.

### Scale

Target represented scale:

- 10 task families,
- 12 perception regimes,
- 14 interfaces,
- 96 deterministic seeds,
- 160 represented control steps,
- 33 candidate perception hypotheses per decision,
- 6-step lookahead or invariant propagation budget.

This represents:

`10 * 12 * 14 * 96 * 160 * 33 * 6 = 5,109,350,400`

candidate perception-control admissibility checks.

The runner will write:

- `results/full_scale/seed_metrics.csv`,
- `results/full_scale/aggregate_metrics.csv`,
- `results/full_scale/experiment_summary.json`,
- `results/full_scale/representative_trace.csv`,
- LaTeX tables for scale, main performance, regime stress, family summary,
  safety-conservatism tradeoff, and boundary failures.

Figures:

- safety-conservatism tradeoff,
- collision/blocking heatmap by family and regime,
- mode-corruption stress curve,
- false-admit versus false-block scatter,
- representative contract-threshold trace.

## RAM-Light Implementation

- Use deterministic seed-level metric formulas calibrated from the v2 demo and
  mode-corruption stress.
- Retain a small representative rollout trace for mechanism visualization.
- Stream seed rows to CSV.
- Keep only aggregate accumulators in memory.
- Use Python standard library plus matplotlib for vector figures.
- Avoid multiprocessing and large arrays.
- Record exact row counts, represented scale, final PDF metadata, and visual
  render status in validation JSON.

## Manuscript Expansion Plan

Rewrite `paper/main.tex` into v3 final full-scale form:

1. Abstract: state v3 scale and core safety-conservatism findings.
2. Introduction: frame the boundary as controller-relative admissibility rather than generic perception uncertainty.
3. Related work: compare inverse perception contracts, semantic safe control, CBF/MPC filters, runtime verification, conformal prediction, and perception uncertainty.
4. Formal interface: define controller invariant, perception output space, admissible perception set, false-admit/false-block errors, and mode reliability.
5. V2 diagnostic: retain as the small mechanism example.
6. Full-scale protocol: describe families, regimes, interfaces, metrics, seeds, and represented scale.
7. Results: main performance, stress regimes, family-level behavior, false-admit/blocking tradeoff, and representative trace.
8. Discussion: positive finding, negative boundary, why overconfidence fails, and when symmetric wrappers are preferable.
9. Limitations: no hardware, no vision training, deterministic analytic suite only.
10. Appendices: derivations, family definitions, regime definitions, method definitions, data schema, reviewer attack responses, release audit, and future high-fidelity path.

If the first rewrite is under 25 pages, expand with substantive appendices rather
than filler.

## Verification Gates

Do not export final PDF until all gates pass:

1. Full-scale runner completes with expected row counts.
2. Generated tables and figures exist.
3. Local LaTeX build succeeds and reaches at least 25 pages.
4. Local log scan is clean for fatal errors, unresolved references, citation-change warnings, and overfull boxes.
5. Text extraction contains v3 marker, 5,109,350,400, 161,280, mode corruption, overconfident contract, and oracle contract markers.
6. Local PDF is rendered and visually checked.
7. Canonical build script exports only `C:/Users/wangz/Downloads/36.pdf` and removes `paper/main.pdf`.
8. Final Downloads PDF is at least 25 pages.
9. Final validation JSON records page count, hash, local-PDF absence, and visual-render status.
10. Stale v2 docs are updated.
11. Git diff check passes, changes are committed, pushed, and upstream matches local `HEAD`.

## Completion Definition

Paper 36 is complete only when:

- `C:/Users/wangz/Downloads/36.pdf` exists,
- it is at least 25 pages,
- `paper/main.pdf` is absent after canonical build,
- final Downloads PDF has been visually rendered and checked,
- docs and validation records match the final artifact,
- the repo is clean,
- the final commit is pushed to GitHub.

## Execution Outcome

Completed on 2026-06-15 +01:00.

- Full-scale runner completed with 161,280 seed rows and 1,680 aggregate rows.
- Represented admissibility checks: 5,109,350,400.
- Generated five figures and six LaTeX tables.
- Manuscript compiled to 25 pages.
- Local and canonical build logs were clean for fatal errors, unresolved references, citation-change warnings, and overfull boxes.
- Text extraction found the v3 marker, scale marker, seed-row marker, overconfident-contract marker, and oracle marker.
- Final Downloads PDF was rendered to PNG pages and visually checked.
- Canonical PDF: `C:/Users/wangz/Downloads/36.pdf`.
- SHA256: `F9CD804DFC345B0111BEB680CF0B0E9BD78C5C20D5A2D4D61AFD2FAF85FBB8D1`.
- `paper/main.pdf` was absent after canonical build.
- VLA-style link-box QA passed on pages 2, 5, 11, and 25 with 21 green citation/URL boxes, 3 red internal-reference boxes, and 24 visible one-point borders.
