# Research handoff: the actual C2 existence question

You are the research agent, not the referee of the prior reconstruction dossier. Use the prior reconstruction theorem only with its supplied review status. Audit the new lemmas in PROOF.md before building on them; do not accept a label as evidence.

## Exact objective

Decide whether a strongly regular graph (99,14,1,2) with an involution exists. A positive example settles Conway existence positively. A negative result on C2 alone does not settle asymmetric Conway existence.

Do not assume nonexistence, extra symmetry, a minimum for K, zero same-cell inner products, or membership in the special family below.

## New foothold, with proof supplied

Use the fixed labelled 42-by-7 root matrix R, with rows e_i+e_j and e_i-e_j. Put H=RR^T and M=|R|. Seek a symmetric orthogonal projector P over F_3 with rank 15, PR=0 and diagonal 1. Define N as the entrywise centered lift of P+H, and B=|N|.

The capacity expressions are rational/integer expressions, NOT finite-field expressions:

    T=2J-M-BM/2,
    E=(8I+4J-MM^T-B^2-B)/2.

Every row of T must be binary of weight two, and every entry of E must be a nonnegative integer.

The bounded-residue lemma proves that these conditions recover ALL integer signed equations from the ternary ones. There is no remaining choice of signs for this P. The final matching-completion test remains necessary; passing only the two capacities does not yet produce a graph.

## The negative control you must preserve

`data/ternary_projector_control.json` is an actual P satisfying every bare ternary projector condition. Its centered lift violates the capacities. Thus no theorem asserting the bare projector conditions impossible can be right.

Do not discard this control because it looks generic, nonsymmetric, or unlike a graph. It is exactly the witness showing what the modular conditions alone fail to say.

## A concrete proven family, not an exhaustive partition

The quotient W=im(R)^perp/im(R) has dimension 28 over F_3. A rank-15 projector corresponds to a nondegenerate code C in im(R)^perp and its labelled quotient image Cbar in W, plus the choice of lift.

One particular Cbar0 is the image of the K7 oriented-edge cycle space placed on the minus coordinates. Section 5 excludes ALL its lifts, including nonsymmetric ones. The proof reduces its 105 ternary lift coefficients to seven norm values, uses actual coordinate support budgets, and then contradicts the real rank-15 Gram matrix with a rank-20 principal submatrix.

There is NO proof that all Cbar equal Cbar0 or lie in its relabelling orbit. Arbitrary isometries of W do not preserve the integer coordinate capacities. Never replace permitted graph relabellings with the full orthogonal group just to reduce cases.

## Primary research question

What does the original coordinate labelling force on a nondegenerate quotient subspace Cbar if it admits a lift whose centered P+H satisfies the row-support and two-walk capacities?

Seek a graph-level or labelled-code theorem that restricts EVERY feasible pair, or excludes an explicitly quantified family with a proved link to the full space. The most promising concrete mechanism found in this pass is:

    finite-field subspace/lift structure
       -> forced support on an actual coordinate set
       -> integer signed identity, via the capacity window
       -> incompatible rank, common-neighbour count, or matching condition.

This is a mechanism to examine, not a promised universal obstruction. You may reject it and choose a better representation if you give a precise reason. Do not spend the main budget enumerating all projectors or the 3^105 lifts. The hand family proof is an example of avoiding that enumeration, not a demand to grind through neighbouring families.

## Required connection to the main claim

For each serious direction state what happens if it succeeds:

- If it excludes every P passing the two capacities, C2 is excluded (stronger than necessary).
- If it leaves P but proves their matching systems infeasible, C2 is also excluded.
- If it finds one P passing capacities and completion, reconstruct and independently check the full adjacency matrix.
- If it excludes only a family, specify exactly which family and which other families remain. Do not translate that into 156-envelope or rank-17 coverage without a proved map.

Do not investigate further uniqueness of D or fractional completions as the main target. A genuine graph has one integral D, and those arguments do not eliminate it. Constant dual sums and elementary compressed-D traces were tested and are identities or slack; do not rename them new obstructions. Nonconstant certificates and genuinely richer operators remain possible.

## Verification and stopping discipline

Work on one arbitrary valid object unless a case assumption is explicitly introduced. Keep exact quantifiers and distinguish:

- DERIVED WITH A WRITTEN PROOF;
- independently VERIFIED;
- a bounded COMPUTATION;
- CONJECTURE or unproved coverage.

Small exact tests are allowed for falsification, with their scope recorded. They are not substitutes for universal proofs. Do not start cloud workloads, contact providers, send messages, or run unbounded parallel jobs. Keep a checkpoint and respect the operator's resource limits.

The useful endpoint is a proof, a verified witness, or a precise mathematical obstruction/coverage statement. A fresh representation by itself is not a completed existence decision and should not be reported as one.
