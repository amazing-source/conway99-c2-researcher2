# Public mathematical research record

This document records the mathematical developments and checked limitations, rather than a verbatim internal deliberation transcript.

## 1. Starting point

The supplied dossier already contains an exact signed quotient N, the double matching D, ordinary quotient Q, and reconstruction to 99 vertices. The newly derived real-linear theorem is assumed provisionally, pending the separate referee. An exact (N,D) orbit model existed in the project before that theorem; this pass does not claim to discover the first exact formulation of C2.

The previous recommendation was to couple ordinary multiplication N^2, the entrywise support B=N o N, and D, seeking a universal dual certificate or a mixed spectral operator. This pass actually tested elementary instances of that advice.

## 2. Low-order dual/spectral attempts

Summing the completion equations gives E1=21 1 on both sides. This cannot be a separating inequality. Compressing D to the three rational eigenspaces of N yields traces controlled by one root-inner-product sum s. Their elementary absolute trace bounds are automatically satisfied. Details and formulas are in PROOF.md Section 7.

These are rigorous negative conclusions for those particular expressions only. They do not disprove the existence of a nonconstant Farkas certificate, nor exhaust the algebra of mixed operators. No universal dual certificate was found.

## 3. The small-residue observation

The ordinary completion gives two unsigned restrictions before D is known: prescribed target cells T, and a nonnegative integer residual E. Their force is pointwise: each signed row error and quadratic error is even and lies between -4 and 4. If it also vanishes modulo three, it must vanish as an integer.

This supplied a concrete bridge that an aggregate trace identity does not provide. It is proved entry by entry, including all parity and degree assumptions, in Section 2. Bounded scalar checks verify a superset of the scalar situations used by the proof.

## 4. Why a ternary projector appears

At m=7, R^TR=12I vanishes modulo three. The fixed H=RR^T becomes square-zero. The signed equation then separates into an orthogonal idempotent P=Nbar-Hbar annihilating Rbar, plus that fixed square-zero part.

Conversely, centered lifting of P+Hbar provides a unique sign matrix. Applying the small-residue observation turns the two capacities into an exact lift from modular equations to integer signed equations. The rank-15 condition was justified by reducing a rational projector over Z_(3), not by inferring an integer rank from a trace modulo three.

This is an exact parameterization, not evidence that its parameter space is smaller in a computationally useful sense.

## 5. A countermodel was constructed, not assumed away

The bare projector conditions are realizable. A 15-dimensional cycle-space code was lifted by a linear map into the fixed radical. Six mutually orthogonal isotropic directions and one norm-one direction provide sufficient freedom to meet every diagonal condition. A finite-field linear system of rank 20 supplies an explicit example.

The stored 42-by-42 P is symmetric, idempotent, diagonal 1, rank 15, and annihilates R modulo three. Its centered N is not a graph candidate over the integers: row weights range from 22 to 37 rather than 10, and both capacity tests fail. This construction is included so that further researchers can falsify overbroad modular claims immediately.

## 6. A family exclusion, including all lifts

The same quotient cycle-space family was then treated without specializing its lift. Its arbitrary lift is described by seven cycle-space vectors t_i. The plus diagonal condition expresses every mutual product through the seven norms a_i.

An exact count on the 21 plus coordinates shows that row degree at most ten forces all a_i=2. This makes the entire corresponding N principal block zero. Once the capacities enforce the integer signed equations, the associated real Gram matrix has rank 15, but that principal block has rank 20. Contradiction.

All 105 ternary lift coefficients are covered by the proof. This does not cover all possible quotient subspaces, and no mapping to named Route C or rank-17 instances was proved. No extra symmetry of the unknown is imposed within this family.

## 7. Relation to existing project sources

Project sources consulted include:

- `conway99-c1`, commit `0bab0349028fdc88432df195c2687f74ad01a105`, `notes/149_COUPLAGE_SEPT_ETOILES.md`: automatic aggregate star moments; exact versus relaxed star conditions; warnings about spectral bookkeeping.
- `conway99-c2-experimental`, commit `609cc3bf25b11c1c7be187071d4462529ab9e384`, existing signed/ordinary quotient and target-cell work as preserved in the prior handoff.
- `conway99-rank17`, commit `d9fdc855f3a46baf0d8c230f1e257012858f18a7`: the inherited proof obligations and remaining classes, not re-counted here.
- The prior conversation's `conway_c2_theorem_handoff_2026_09_30` package, particularly THEOREMS, GRAPH_RECONSTRUCTION and the exact controls.

Targeted repository and public-paper searches did not establish priority for the new ternary capacity formulation. An absence of a search hit is not evidence of novelty. No external classification is used in the new proofs.

## 8. What to infer and what not to infer

The result gives a more concrete Agent-2 target than “try another invariant”: compatibility of a labelled ternary projector with specific integer support capacities, followed by exact matching completion. It also supplies one successful hand mechanism and an explicit modular countermodel.

It does not supply a universal obstruction. It does not show a low-dimensional abstract quadratic-space classification suffices. It does not show the remaining work is only hardware. It does not promise this direction will be faster than the existing lattice routes. The decisive missing step remains coverage or contradiction for arbitrary admissible projectors, not further refinements of the already excluded special family.
