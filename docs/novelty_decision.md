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

