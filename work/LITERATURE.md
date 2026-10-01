# Literature consulted (after the starting note), with what each adds

All items are EXTERNAL INPUT: read from abstracts/HTML on 2026-09-30, not re-proved here.

1. P. G. Cesarz, A. J. Woldar, "On the automorphism group of a putative Conway 99-graph",
   Algebraic Combinatorics 8(2) (2025) 379-; arXiv:2308.02978.
   Adds: if 2 divides |Aut|, then |Aut| divides 6 (Corollary 4(a)); if 7 divides |Aut| then Aut = Z7.
   Builds on Makhnev-Minakova (2004), who showed: Aut contains an involution => |Aut| divides 42.

2. D. Crnkovic, M. Maksimovic, "Construction of strongly regular graphs having an automorphism
   group of composite order", Contrib. Discrete Math. 15(1) (2020).
   Adds: no srg(99,14,1,2) has an automorphism group of order 6 or 9 (Z6, S3, Z9, E9 excluded).

   Combined consequence of 1+2 (EXTERNAL, not checked here): a Conway graph with an involution
   has Aut exactly Z2. Hence any positive witness for EX has no automorphism besides s, and every
   "extra symmetry" ansatz commuting with s (orders 3, 7, ...) is already excluded. My mechanism M3
   is therefore abandoned. (Consistent with DUPLICATION_NOTES item 2.)

3. Y. Ishida, "No involutions in the missing Moore graph", arXiv:2606.29183 (2026).
   Trace-rank identity (Prop. 4.4) for automorphisms of prime order p when the spectral idempotent
   is p-integral. Applied to Conway only for p=3 there.
   CHECKED HERE (by hand, using my reading of the displayed statement): for p=2, one fixed point,
   a1 = #{v : v ~ s(v)} = 14, the identity reads 0 = rank_2(6/11) = 0 for theta=3 and
   0 = rank_2(4/9) = 0 for theta=-4. No contradiction: the one-fixed-point involution passes this test.
   (Matches the eigenspace split computed in RESULTS: 27/27 and 22/22.)

4. A. Thakkar, S. Severini, "A Forced-Structure Reduction and Verifiable Bounds for Conway's
   99-Graph", arXiv:2608.11211 (2026). Adds: the same one-vertex reduction to a 12-regular graph on
   84 vertices (our canonical form without the involution); heuristic partial constructions (~70%).
   Nothing on involutions.

5. A. Keramatipour, "Approaching the Conway-99 problem using SAT solvers", arXiv:2604.23037 (2026).
   Adds: direct SAT encodings of the full problem did not finish in reasonable time.

Not found: a primary source for F0 (every involution fixes exactly one vertex). F0 is not used in
any result of this directory.
