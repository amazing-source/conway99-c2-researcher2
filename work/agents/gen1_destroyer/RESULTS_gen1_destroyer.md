# gen1_destroyer -- results of the first research interval (2026-10-01)

Scope: arbitrary solution (Q,N) of C1-C5 (Theorem C; T4 working lemma; F0 not used). m = 7 unless stated; general m
means the analogous system for srg(1+2m^2, 2m, 1, 2) with a one-fixed-point involution (m=2: Paley(9), m=11: BvLS,
data work/data/bvls_m11_*.npy). Scripts: calib_m11.py, check_thmA.py, spec_O.py (this folder; each < 1 min, < 600 MB).
Labels: PROVED HERE / CHECKED / REDISCOVERY / NO LEVERAGE.

## R1. Cocktail-party / Hamming-ball model  [PROVED HERE; CHECKED m=11; REDISCOVERY in substance]
Vertices: 0, points P={+-e_k}, roots Phi (= edges of the cocktail-party graph CP_m = weight-2 vectors of Z_3^m,
-1=2). Exterior X = [[a,b],[b,a]] (a=(Q-N)/2, b=(Q+N)/2), Inc = root-point incidence, L = line graph of CP_m:
 (X2) X Inc = 2J - Inc(I+Pi)      <=> (C4)+(NR=0)
 (X3) X^2 + X + L = (2m-4)I + 2J  <=> (C3)+(C2b)
calib_m11.py: m=11 data satisfies C1-C5, (X2), (X3) and the full 243-vertex SRG identity.
Consequences used below: half-edges (roots sharing a point) form, at every point h, a perfect matching mu_h of the
2m-2 roots through h; at each coordinate k, Q restricted to the 12 orbits containing k is S_k u C_k, two perfect
matchings (same-sign transition / sign-crossing edge); X-triangles = 3 pairwise point-disjoint roots.

## R2. Hodge lemma for the triangle+square complex  [PROVED HERE; CHECKED m=2, m=11]
Hypothesis: G connected k-regular, every edge in exactly one triangle, every non-adjacent pair has exactly two common
neighbours (so: every 4-cycle is induced). Xhat = G + all triangles + all 4-cycles (99-graph: 99/693/231/2079).
Claim: Delta_1 = d1^T d1 + d2 d2^T = (k+1) I + O, where O_{e,e'} = +-1 iff e,e' are opposite sides of a 4-cycle
(each row: exactly k-2 nonzeros). Hence Delta_1 >= 3I, H_1(Xhat;Q)=0, b_2 = chi-1 (=1715 for m=7).
Proof: two edges sharing a vertex w, u-w-z, lie in exactly one 2-cell (the triangle if u~z, else the unique square
u w z t, t = second common neighbour of u,z); in Delta_1 the down-term gives -1 and the up-term +1 for head-to-tail
orientation, so all such entries cancel. Diagonal: 2 + (1 triangle + (k-2) squares). Disjoint edges: up-term only, and
two disjoint edges are opposite in at most one square (else K_4 minus an edge, violating lambda=1). Row sums of |O|
are k-2 < k+1.  On im d1^T, O = -(theta+1) on the theta-eigenspace of A (theta = r,s).
Equality case: ker(Delta_1 - 3I) = flat parallel classes of the opposite-edge graph (|z| constant on a component, no
sign holonomy). Data: m=11 spectrum of Delta_1 = 3^11, 18^792, 21^660, 27^990, 30^220 (the 11 = translation
directions of the Golay quotient); m=2: 3^6, 6^12.

## R3. Redundancy of every homological Lefschetz route on Xhat  [PROVED HERE; NO LEVERAGE by design]
For an automorphism g of order prime to p (in particular sigma, p odd), Hopf's trace formula with Brauer characters
gives beta(H_2(F_p)) - beta(H_1(F_p)) = L(g) - 1 identically; with R2 and universal coefficients,
H_2(Xhat;F_p) = H_2(Z)(x)F_p + Tor(H_1 Z, F_p), H_2(Z) free of rank chi-1 with character 21 (sigma), and
beta(T[p]) = beta(T/pT) for the p-torsion T. So the identity holds for EVERY possible torsion module: "H_1(F_3) forced
+ Lefschetz contradicts" (c2_experimental notes/12 item 23, theorem E) cannot yield a contradiction by itself.
p=2 (Smith theory): Fix(sigma) = contractible 7-star u 21 square centres, chi(Fix)=22 = L(sigma); inequalities trivial.

## R4. All-sib exclusion by a 4-point complement parity  [PROVED HERE; REDISCOVERY of notes 05/17, new variant]
Hypotheses: m=7, Q from a solution with Q_{x,x'} = 2 for every cell partner x' (all cells in state d). Only C3, C4
and D=[Q=2] a perfect matching are used (no N).
(a) C4 at k in cell(x): the partner uses all weight, so B o K = 0.
(b) Saturation (m=7 only): x,x' have no common Q-neighbour ((Q^2)_{xx'}=0) and each has B-weight 10 on the 20 orbits of
the 10 cells disjoint from c; 2*10 = 20 forces every such orbit adjacent to exactly one of x,x'. With the same fact for
the other cell, B between two disjoint cells is a perfect matching; write f_x(d) for x's neighbour in cell d.
(c) For a B-edge x~u: (Q^2)_{xu}=3 = (B^2)_{xu}, all common neighbours lie in the 3 cells avoiding c u d, so
f_x = f_u there.  (d) For |c cap c''| = 1, (Q^2)_{xy} = 3 = (B^2)_{xy} = #{d in W : f_x(d)=f_y(d)}, W = the 4 remaining
points. By (c) applied to u=f_x(d), u'=f_y(d) and the perfect matching d<->dbar, agreement on d <=> agreement on dbar
(dbar = W minus d). The 6 cells of W form 3 such pairs, so the count is even, not 3.  Contradiction.
m-specificity: 4(m-2) = (m-2)(m-3) iff m=7. check_thmA.py: at m=11 every B-block between disjoint sib cells has 1 edge
(330+660+330+660 blocks), never a matching. Second route checked: on KG(7,2), dim Z^1 = dim B^1 = 20 over GF(2), and
the parity functional lies in the span of the triangle relations.

## R5. Automatic laws recorded so as not to be rediscovered  [PROVED HERE; NO LEVERAGE]
- Star cycles: S_k u C_k is a union of alternating cycles; lifts have length 0 mod 4; voltage (-1)^(#C-steps).
- Trail voltage: #sigma-invariant half-edge cycles = C(m,2) mod 2 (product of orbit signs). (m=11: 55 cycles, odd.)
- Triangle counts: tau_D = 2 delta_0 + delta_1, tau_- + tau_D = 70, tau_+ - tau_- = 70 (m=11: 660/330/0, checked).
- Sum over X-triangles of #antipodal point pairs = 4c_n + 2(c_m + c_p); t_j(missing j) = 20 + t_{e_j,-e_j}.
- sum_x sum_cells Q_{x,d+}Q_{x,d-} = 42 - (2c_d + c_m + c_p)  (= tr(Q^2 C)/2).

## Wall
R4's mechanism needs the saturation of (b). For a cell in state n (resp. m/p) the B-weight of {x,x'} on the 20 orbits
of disjoint cells is 16 (resp. 18) with 2 (resp. 1) units of common neighbours, so f_pq is not defined; with the known
|Sigma| <= 4 (notes 19), the open grid-free regime has no saturated cells at all. A transfer would need a different
object carrying a Z_2 connection in every cell state; R2 suggests the opposite-edge graph (parallel transport across
squares) as the candidate, whose flat classes are exactly ker(Delta_1 - 3I). Not developed here.

## R6. Calibration of the planned "H_1(Xhat;F_3)" test  [CHECKED (h1_modp.py) + PROVED HERE lower bound]
m=2 (Paley 9): H_1(Xhat;F_p) = 0 for p = 2,3,5,7 (exact ranks).  m=11 (BvLS): H_1(F_2) = 0 (rank 2431 = dim Z_1,
rigorous since a projected rank is a lower bound); H_1(F_3) = F_3^6 exactly: dim <= 6 from the projected rank 2425, and
dim >= 6 because on the Cayley graph Cay(F_3^5, +-c_1..c_11) every antisymmetric alpha on the 11 directions gives the
F_3-cocycle (x -> x+c) |-> alpha(c) (squares commute; lines give 3 alpha(c) = 0 mod 3), and only the 5-dim space of
linear functionals restricted to the directions consists of coboundaries.  This matches the expectation "F_3^6" in
c2_experimental notes/12 item 23; by R3 it cannot feed a Lefschetz contradiction. Mechanism: mod-3 torsion of H_1 is
produced by flat parallel direction fields (R2 equality case reduced mod 3).
