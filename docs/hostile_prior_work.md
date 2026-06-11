# Hostile Prior Work

This set is intentionally biased toward papers that make the proposed contribution less novel.

## Closest cluster

1. `Learning-based Inverse Perception Contracts and Applications`
2. `Refining Perception Contracts: Case Studies in Vision-based Safe Auto-landing`
3. `Gaussian Mixture-Based Inverse Perception Contract for Uncertainty-Aware Robot Navigation`
4. `Closing the Perception-Action Loop for Semantically Safe Navigation in Semi-Static Environments`
5. `Formal Modelling and Runtime Verification of Autonomous Grasping for Active Debris Removal`

## What each paper already covers

- IPC papers already connect perception error to safe control.
- Refinement papers already show that test-guided contract improvement is possible.
- Semantic CBF papers already use perception-derived scene structure in control.
- Runtime verification papers already treat architecture as assumptions and guarantees.

## What remains open

- Controller-relative synthesis of the contract itself
- Multi-modal contract geometry that is explicitly tied to the controller invariant
- A clean demonstration that controller-agnostic uncertainty sets can be the wrong abstraction
- A mode-indexed contract layer for hybrid robot control

