# Submission Readiness Decision

Decision: workshop-only / strong-revise.

## Rationale

The paper has a coherent mechanism, clear hostile-prior boundary, reproducible toy evidence, and an explicit negative stress test. It is not submit-ready for a full venue because it lacks hardware validation, multiple tasks, multiple seeds with uncertainty intervals, and a general proof.

## Allowed Claim

In a one-step navigation simulator with reliable perception mode semantics, controller-relative admissibility reduces blocked actions while preserving safety relative to the tested symmetric wrapper.

## Disallowed Claim

Controller-relative contracts are universally safer than conservative symmetric uncertainty wrappers. The v2 mode-corruption stress falsifies that claim under corrupted mode labels.

## Next Work Needed For Full Submission

- Multi-seed confidence intervals.
- More than one controller family.
- A mode-calibration or mode-rejection mechanism.
- Hardware or high-fidelity simulator validation.
- Formal conditions under which controller-relative admissibility implies safety.

