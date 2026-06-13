# Hostile Reviewer Response

## Short Response

The paper is intentionally narrow. It does not claim a universal perception-safety theorem. It claims that a perception-control contract can be synthesized from a controller admissibility condition and that this changes the interface relative to controller-agnostic uncertainty wrappers.

## Strongest Objection

The controller-relative contract relies on the aliased perception mode being reliable. If the mode label is wrong, the contract may authorize actions that a symmetric wrapper would block.

## Response

Accepted and now tested. The v2 mode-corruption stress shows that at 20% mode-label error the controller-relative collision rate is 0.020, worse than the symmetric wrapper's 0.014, while blocked steps remain lower at 0.504 versus 0.832. The manuscript now states this as a limitation and treats reliable mode semantics as a precondition.

## Revised Claim

Controller-relative admissibility can reduce conservatism while preserving safety in the toy simulator when the controller mode semantics are reliable. It is not a universal replacement for conservative uncertainty wrappers.

