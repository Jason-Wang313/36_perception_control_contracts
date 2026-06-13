# Reviewer Attacks

## Likely attack 1

This is just another uncertainty estimate wrapped around a controller.

- Response: the contract is synthesized from the controller invariant, not from sensor error alone.

## Likely attack 2

Single-case simulation is too weak.

- Response: the paper explicitly frames the result as a mechanism paper and marks the evidence as a pilot.

## Likely attack 3

Existing inverse perception contracts already do this.

- Response: existing IPC work usually maps perception error to a set; this paper changes the synthesis target to the controller's admissible perception region and emphasizes mode-relative assumptions.

## Likely attack 4

Why not just use a verifier?

- Response: verification checks a fixed model; the central problem here is that the model/interface itself is wrong if the controller assumption is not encoded in the perception contract.

## Likely attack 5

The contract is too abstract to be useful.

- Response: usefulness depends on the downstream invariant; the paper provides an executable toy demonstration and a clear recipe for instantiation.

## Likely attack 6

The result depends on giving the controller-relative contract a reliable mode label.

- Response: accepted. The v2 stress corrupts the mode label and shows the boundary directly. At 20% mode error, the relative contract has collision rate 0.020 versus 0.014 for the symmetric wrapper; at 40% mode error it rises to 0.029. The paper therefore claims calibrated controller-relative admissibility, not universal dominance.
