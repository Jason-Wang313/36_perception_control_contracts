# Novelty Decision

## Chosen Thesis

Perception-control contracts should be synthesized relative to the downstream controller's admissibility condition and mode structure, not as controller-agnostic uncertainty sets around perception outputs.

## Central Mechanism

Given a controller invariant, invert the local control condition into perception-output space and pass the resulting admissible set across the perception-control boundary.

## Why This Is The Strongest Idea

- It changes the boundary object, not merely the size of the perception set.
- It is adjacent to inverse perception contracts but uses the downstream controller's admissibility condition as the synthesis target.
- It explains why one-sided braking, two-sided corridor keeping, coupled docking, and semantic stop-zone control need different perception interfaces.
- It exposes calibration and mode reliability as part of the contract rather than as afterthoughts.
- It supports both positive and negative findings in a full-scale deterministic suite.

## V3 Boundary

The paper is not a hardware or learned-vision claim. It is a deterministic interface study with 5,109,350,400 represented admissibility checks. The honest novelty boundary is controller-relative admissibility with explicit calibration and fallback requirements.
