# Literature Map

## Sweep summary

- Sweep size: 2,175 Crossref metadata rows in `docs/related_work_matrix.csv`
- Serious skim target: 300 highest-scoring rows in `docs/serious_skim_top300.csv`
- Deep-read focus: perception contracts, inverse perception contracts, runtime verification, and perception-aware safe control
- Hostile prior-work target: 100 papers clustered around contracts, runtime verification, CBF/MPC safety filters, and semantically aware navigation

## Main clusters

### 1. Perception contracts and inverse perception contracts

- `Learning-based Inverse Perception Contracts and Applications` proposes learning a set-valued inverse contract from data for an existing perception module and then using it in safe control.
- `Refining Perception Contracts: Case Studies in Vision-based Safe Auto-landing` extends contract testing and refinement to higher-dimensional flight systems with multi-stage vision pipelines.
- `Gaussian Mixture-Based Inverse Perception Contract for Uncertainty-Aware Robot Navigation` broadens IPC geometry from one ellipsoid to Gaussian-mixture unions and plugs the result into MPC-CBF navigation.

### 2. Semantically aware safe control

- `Closing the Perception-Action Loop for Semantically Safe Navigation in Semi-Static Environments` converts object-level semantic and consistency estimates into CBF constraints for MPC.
- Similar papers use semantic costmaps, object-aware mapping, or learned scene representations as input to safe control.

### 3. Runtime verification and assume-guarantee reasoning

- Autonomous-system verification papers use assumptions and guarantees per subsystem, plus runtime monitors, theorem proving, model checking, and testing.
- These works are important because they already frame robot software as a set of contracts, but they usually stop at software-level assumptions rather than controller-relative perception semantics.

### 4. CBF/MPC and safety filtering

- A large body of work uses CBFs and MPC to keep robots safe under state uncertainty, sensing noise, or dynamic obstacles.
- These papers make safe control non-novel by themselves, so the novelty must sit in the contract/interface layer.

## Working thesis

The field assumption to break is:

> A perception module can be safely abstracted by a fixed uncertainty set, independent of the downstream controller's actual invariant, mode structure, and sensitivity.

The proposed direction is:

> Synthesise a controller-relative perception contract that is defined by the set of perception outputs preserving the controller's safety invariant, not by a sensor-side error model alone.

