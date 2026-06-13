# Claims

## Main claims

1. A fixed controller-agnostic perception uncertainty set is often too coarse for downstream safety.
2. A perception contract should be defined by the downstream controller's invariant, mode, and sensitivity.
3. Under multi-modal or aliased perception error, a single ellipsoid can be both over-conservative and structurally mismatched.
4. A controller-relative contract can preserve safety with less conservatism than a generic uncertainty wrapper.

## Support status

- Claim 1: supported by literature comparison and synthetic evidence
- Claim 2: conceptual contribution, supported by mechanism derivation
- Claim 3: supported by hostile-prior analysis and synthetic demonstration
- Claim 4: supported only in the demo setting; not claimed as universal
- V2 boundary: under 20% mode-label error, the controller-relative collision rate rises to 0.020, exceeding the symmetric wrapper's 0.014. The claim requires reliable mode semantics.

## Unsupported claims not made

- Universal optimality
- Full formal soundness for all robot controllers
- Hardware validation
- A general solution to perception uncertainty
- Universal safety dominance under corrupted mode labels
