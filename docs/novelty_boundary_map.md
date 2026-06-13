# Novelty Boundary Map

## Not novel enough

- Adding another uncertainty estimator
- Using a larger foundation model for perception
- Adding a new benchmark without a new mechanism
- Wrapping perception with a generic verifier only
- Combining standard perception and standard MPC/CBF modules
- Using RL to tune controller parameters

## Boundary-crossing ideas

### A. Controller-relative contract synthesis

Contract is computed from the downstream controller's invariant, not just from perception error statistics.

- What changes: central mechanism becomes a projection from controller safety requirements back into perception-output space
- Why it matters: the downstream controller often only needs a subset of the perception output to preserve safety

### B. Mode-aware contract switching

Contracts are indexed by control mode, rather than one static uncertainty wrapper.

- What changes: the contract becomes hybrid and temporally scoped
- Why it matters: contact and navigation modes have different admissibility regions

### C. Multi-modal contract geometry

Contracts are unions or stratified sets instead of a single ellipsoid.

- What changes: the abstraction can represent aliased perception outputs
- Why it matters: many robot perception errors are not unimodal

### D. Contract validation against controller behavior

The paper demonstrates that a contract matters by showing safety or performance failure when the field assumption is violated.

- What changes: proof/evidence is adversarial, not just descriptive
- Why it matters: a contract is only useful if it blocks the actual failure mode

## Chosen boundary

The best thesis is A plus D:

- synthesize the contract from controller invariants
- show that a generic perception uncertainty wrapper can fail or become too conservative

## V2 boundary

Inside the claim: controller-relative admissibility can be less conservative than a symmetric wrapper when the controller mode semantics are reliable.

Outside the claim: universal safety dominance under corrupted or adversarial mode labels. The mode-corruption stress shows this boundary: at 20% mode error, relative-contract collisions are 0.020 versus 0.014 for the symmetric wrapper.
