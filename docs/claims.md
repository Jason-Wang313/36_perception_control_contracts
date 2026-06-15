# Claims

## Main Claims

1. A controller-agnostic perception uncertainty set is often the wrong boundary object for robot safety.
2. A perception-control contract should be the set of perception outputs under which the downstream controller's local invariant remains admissible.
3. Controller-relative contracts can reduce blocking relative to generic symmetric wrappers when mode semantics and calibration signals are reliable.
4. Overconfident controller-relative contracts are unsafe: using the right contract geometry without adequate calibration can increase collisions.
5. Robust, risk-budgeted, adaptive, and residual-calibrated controller-relative variants expose the safety-conservatism tradeoff more directly than generic wrappers.

## V3 Evidence

- Full-scale suite: 10 task families, 12 regimes, 14 interfaces, 96 seeds per cell, 160 represented steps, 33 hypotheses, and 6-step lookahead.
- Represented admissibility checks: 5,109,350,400.
- Seed-level rows: 161,280.
- Aggregate rows: 1,680.
- Point-estimate controller: 93.95 collisions per seed.
- Overconfident controller-relative contract: 80.42 collisions per seed.
- Symmetric interval wrapper: 14.76 collisions per seed, 0.80 blocked fraction.
- Adaptive mode-calibrated contract: 7.25 collisions per seed, 0.52 blocked fraction.
- Robust one-sided contract: 4.77 collisions per seed, 0.70 blocked fraction.
- Oracle admissibility contract: 0.66 collisions per seed, 0.36 blocked fraction.

## Boundaries

- The paper does not claim hardware safety.
- The paper does not train or validate a learned vision model.
- The paper does not prove a universal synthesis theorem for arbitrary controllers.
- The paper does not claim controller-relative contracts universally dominate symmetric wrappers.
- Mode calibration is required; the v2 and v3 stress tests intentionally keep that failure boundary visible.
