# gen1_destroyer -- starting note (written before any duplication check)

Target: EX <=> exists integer (Q,N) with C1-C5 (Theorem C; T4 = working lemma, F0 not used).
Role: look for a GLOBAL obstruction; any claimed law must hold for every m where the analogous
object exists (m=2: Paley(9) with x->-x; m=11: BvLS srg(243,22,1,2), data in work/data).

## D1. Representation (derived here from MODEL.md s.5 / reconstruction)
Vertex set of the 99-graph = {0} u P u Phi, P = {+-e_k} (14 "points"), Phi = 84 roots of D7.
0 ~ all of P; e_k ~ -e_k; point p ~ root v iff p is one of the two "halves" of v.
So Phi = edge set of the cocktail-party graph CP_m on P (v={h,g}, g != +-h), sigma = -1.
Exterior graph X (84x84, 0/1, sigma-invariant) with L = line graph of CP_m (L_vw = |v cap w|),
I_inc = 84x14 incidence:
 (X2) X I_inc = 2J - I_inc(I + Pi)      [from lambda/mu at point-root pairs]
 (X3) X^2 + X + L = (2m-4)I + 2J        [root-root pairs]  (m=7: 10I+2J)
Even/odd parts of X under sigma are Q and -N; (X2) is (C4)+(C2a), (X3) is (C3)+(C2b).

## D2. Forced local geometry (lambda=1, mu=2)
- every edge in exactly one triangle; every non-adjacent pair = opposite corners of exactly one
  INDUCED 4-cycle; no 4-cycle has a chord.
- X-edges split: "half" (share a point; 2 per root) and "free" (10 per root, 5 X-triangles per root).
- half-edges at point h = perfect matching mu_h of the 12 roots through h  -> a TRANSITION SYSTEM on
  CP_m (sigma-equivariant), i.e. on the signed multigraph +-K_m after quotient. Its closed trails = the
  2-regular graph X_h.
- X-triangles = 3 pairwise point-disjoint roots; per sigma-orbit: unbalanced B-triangle or D-B-B triangle.

## Candidate mechanisms
M1 (square complex): 2-complex Xhat = graph + 231 triangles + 2079 induced squares; links are K_14.
   Wanted: an Aut-character / homology constraint violated by sigma.
M2 (transition system): global law on trails/voltages of mu on +-K_m forced by (X2),(X3).
M3 (triangle shadows): count X-triangles by their K_m shadow two ways.
Success for any of them must be m-sensitive (7 vs 11); otherwise it cannot be a contradiction.
