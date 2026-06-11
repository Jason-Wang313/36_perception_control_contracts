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

