# Exact theorem ledger

All new results below are **DERIVED HERE with written proofs**, not independently verified theorems. Their complete arguments are in PROOF.md. Small programmatic checks do not promote their status to an independent proof.

## T1. Bounded-residue lifting (PROOF Section 2)

Fix R with the 42 signed D7 labels, M=|R| and H=RR^T. Let N be symmetric, diagonal zero, entries in {0,+1,-1}. Define B=|N| and rational T,E as in PROOF (1).

Hypotheses:

- NR=0 modulo three.
- N^2-N-12I+H=0 modulo three.
- Every row of T is binary of weight two.
- Every entry of E is a nonnegative integer.

Conclusion:

- NR=0 over the integers.
- N^2=N+12I-H over the integers.

This does not assert every integer solution of the signed equations passes T-cap/E-cap. Those capacities are additional necessary conditions for C2 completion.

## T2. Projector-to-integer-signing (PROOF Section 3)

Let P over F_3 be symmetric idempotent, diagonal one, with PRbar=0. Center P+Hbar entrywise to obtain N in {0,+1,-1}.

If its T-cap/E-cap pass, then N satisfies the full integer signed equations. Its real spectrum is 4^15, (-3)^20, 0^7, and rank_F3(P)=15.

Conversely every integer signed N has a corresponding P=Nbar^2=Nbar-Hbar of rank 15 with these projector conditions. A completable N also necessarily passes the capacities.

## T3. One quotient family has no capacity-admissible lift (PROOF Section 5)

Over F_3 let Rcal=im(Rbar), W=Rcal^perp/Rcal, and Cbar0 the quotient image of the K7 oriented-edge cycle space supported on the minus indices, as defined explicitly in Section 5.1.

No rank-15 nondegenerate code C in Rcal^perp with quotient image Cbar0 has an orthogonal projector P satisfying diagonal one and both T-cap/E-cap after centered lifting.

All lifts C of this fixed quotient image are included, with no symmetry restriction. No exhaustiveness of this quotient image or its graph-relabelled orbit is claimed.

## C1. Exact C2 criterion (conditional only on the stated reconstruction inputs)

Under the normalized one-fixed-point model, C2 exists if and only if there is a P satisfying T2, the capacity tests and a feasible matching completion.

For the real-linear matching test, invoke the prior Exact Reconstruction Theorem with its actual audit status. Alternatively require a genuine matching and verify the ordinary equations directly.

For *all* involutions, also supply the separate fixed-point normalization theorem. This package does not prove it anew.

## C2. Explicit countermodel to a stronger false assertion

The supplied P proves that symmetry, idempotence, diagonal one, rank 15 and PRbar=0 alone are jointly consistent. It violates T-cap and E-cap. It is neither a C2 graph nor a solution of the integer signed system.

## Outcomes not established

- C2 nonexistence.
- Conway existence.
- Nonexistence of every integer signed N.
- Universal failure of T-cap or E-cap.
- Any new named 156-envelope or rank-17 pair exclusion.
- A cheaper exhaustive algorithm.
- A literature priority claim.
