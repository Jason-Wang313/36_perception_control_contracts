# Hostile Reviewer Response

## Short Response

The paper does not claim that perception contracts, CBF filters, MPC filters, conformal prediction, or semantic safety are new in isolation. The claim is narrower: the perception-control boundary object should be the set of perception outputs under which the downstream controller's local invariant remains admissible.

## Strongest Objection

Controller-relative contracts may become unsafe when mode semantics, calibration, delay, or semantic labels are unreliable.

## Response

Accepted and tested. The v2 mode-corruption stress exposed the hidden reliable-mode assumption. The v3 suite expands this boundary across 12 regimes and includes an overconfident controller-relative contract as an explicit negative control. That negative control averages 80.42 collisions per seed, compared with 14.76 for the symmetric interval wrapper, 7.25 for adaptive mode calibration, 4.77 for robust one-sided contracts, and 0.66 for the oracle.

## Revised Claim

Controller-relative admissibility is the right interface geometry when the controller invariant is known and calibration signals are healthy. The geometry must be paired with residual, mode, semantic, delay, and drift calibration, plus fallback to conservative wrappers or blocking when those signals fail.

## What Remains Out Of Scope

- Hardware validation.
- Learned perception model training.
- A universal theorem for arbitrary controllers.
- A claim that controller-relative contracts always beat symmetric wrappers.
