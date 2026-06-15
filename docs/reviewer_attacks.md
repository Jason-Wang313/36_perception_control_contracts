# Reviewer Attacks

## Attack 1: This is just another uncertainty wrapper.

Response: the contract is synthesized from the controller invariant. A generic wrapper asks where the true perception target might be; the controller-relative contract asks which perception outputs preserve the controller's admissibility condition.

## Attack 2: Existing inverse perception contracts already cover this.

Response: inverse perception contracts are important prior work, but their usual synthesis target is a perception/state containment set. This paper changes the synthesis target to the downstream controller's admissible perception region.

## Attack 3: Symmetric wrappers are safer.

Response: sometimes yes. The paper keeps that boundary visible. Symmetric wrappers reduce collisions by blocking heavily: 14.76 collisions per seed with 0.80 blocked fraction. The claim is not universal dominance; it is that controller-relative contracts expose the relevant safety-conservatism tradeoff.

## Attack 4: Mode corruption breaks the method.

Response: fixed and overconfident variants can break. That is why v3 includes mode corruption, semantic false negatives, combined shift, adaptive mode calibration, robust one-sided contracts, and an overconfident negative control.

## Attack 5: The experiment is still analytic.

Response: accepted. The v3 suite is a deterministic interface study, not a hardware or learned-vision benchmark. The manuscript explicitly lays out high-fidelity simulation and hardware transition protocols as future work.

## Attack 6: The result is just CBF or MPC filtering.

Response: CBF and MPC filters still need a perception object. The paper asks what that object should be and includes CBF/MPC generic-uncertainty baselines to separate filtering from interface synthesis.
