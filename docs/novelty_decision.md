# Novelty Decision

## Chosen thesis

Perception-control contracts should be synthesized relative to the downstream controller's invariant and mode structure, not as a controller-agnostic uncertainty set around perception outputs.

## Central mechanism

Given a controller safety condition, derive the admissible set of perception outputs that preserves that condition under the controller's local model. Use that set as the contract interface.

## Why this is the strongest idea

- It changes the central mechanism, not just the model size or data volume.
- It is adjacent to, but not covered by, existing IPC and semantic-CBF papers.
- It exposes hidden assumptions: unimodal errors, static modes, controller-agnostic uncertainty, and perfect alignment between perception timestamps and control invariants.
- It can be supported with a small runnable simulation and a hostile comparison against the single-ellipsoid contract default.

## Rejected alternatives

- Generic uncertainty-aware navigation
- Pure runtime verification of software contracts
- Better perception calibration
- New benchmark only

## V2 hardening boundary

The paper remains a narrow mechanism paper. It is not a general safe-perception theorem. The v2 mode-corruption stress deliberately weakens the claim: at 20% mode-label error, the controller-relative contract's collision rate rises to 0.020, worse than the symmetric wrapper's 0.014. The honest novelty boundary is controller-relative synthesis under reliable local mode semantics.
