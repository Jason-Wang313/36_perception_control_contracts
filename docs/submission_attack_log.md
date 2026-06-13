# Submission Attack Log

Generated: 2026-06-13 07:29:49 +01:00

## Attack Rounds

1. Novelty overlap with inverse perception contracts.
   - Action: narrowed the mechanism to controller-relative admissibility synthesis, not set-valued perception uncertainty.
2. Evidence is a single toy simulator.
   - Action: marked the paper workshop-only / strong-revise and removed any broad validation claim.
3. Symmetric wrapper baseline might be weak only because it is too conservative.
   - Action: retained collision and blocked-step rates together so safety and conservatism are both visible.
4. Reliable mode labels are an untested hidden assumption.
   - Action: added v2 mode-corruption stress.
5. Controller-relative contract may become unsafe under corrupt mode semantics.
   - Action: reported the negative result directly: 20% mode error gives 0.020 collision rate versus 0.014 for the symmetric wrapper.
6. PDF and repository artifact policy was inconsistent with batch rules.
   - Action: added `scripts/build_pdf.ps1`, canonicalized `C:/Users/wangz/Downloads/36.pdf`, and removed Desktop-copy claims.

## Honest Stopping Point

The recoverable claim and artifact issues are fixed. The remaining blockers require a larger benchmark, hardware validation, or a formal theorem and are outside the honest scope of this generated paper.

