# RESULTS (Researcher 2)

Labels: PROVED HERE / CHECKED COMPUTATION / CONJECTURE / EXTERNAL INPUT / OPEN.
Notation: "orbits" = the 42 positive roots x (rows of R); supp x = cell of x; s(x,y) = |supp x cap supp y|;
kappa(x) = the other orbit in the same cell; G = MM^T; for N in S and D in L_N, pi is the matching D
(T4), t(x) = s(x, pi x) ("type"), B(x) = set of B-neighbours, f_x(k) = #{z in B(x) : k in supp z}.
T4 is used as a working lemma (hand-reviewed, not formally verified). F0 is never used.

---------------------------------------------------------------------------------------------------
## R1. Canonical form and meaning of D  [PROVED HERE]

Statement. (a) In an srg(99,14,1,2) with an involution s fixing exactly one vertex v0, s swaps the two
ends of every inner edge and acts on the 84 non-neighbours of v0 (= roots of D7) as r -> -r; no root
is adjacent to its negative. (b) For a positive root u, the common neighbours of u and -u are exactly
{w,-w} for one positive w; D_uv = 1 iff v = w. Hence D is a fixed-point-free perfect matching (this is
the graph-side meaning of T4's conclusion; T4 itself is about the linear system L_N).

Proof. (a) STARTING_POINT.md section 3(a). (b) u, -u are non-adjacent (a), so they have exactly two
common neighbours; none is inner (their inner neighbours are disjoint) and they are exchanged by s,
which has no fixed exterior vertex, so they are {w,-w}. u ~ w and u ~ -w is exactly a_uw = b_uw = 1.

Consequence for EX: none by itself; it fixes the language for R2-R5.

---------------------------------------------------------------------------------------------------
## R2. Local form of S and L_N  [PROVED HERE]

Statement. Let N in S, D in L_N (so D is the matching pi by T4). For x != y, with
Y_xy = #{w: N_xw N_wy = 1}, Z_xy = #{w: N_xw N_wy = -1}, P = [N=1], P' = [N=-1],
Gam_xy / Del_xy = number of coordinates where r_x, r_y agree / disagree (both nonzero):

    (E+)  Y + P' + Gam + B_(x,pi y) + B_(pi x,y) + D_xy = 2
    (E-)  Z + P  + Del + B_(x,pi y) + B_(pi x,y) + D_xy = 2
    (R2') f_x(k) = 4 - 2[k in supp x] - 2[k in supp pi x]   for all x, k.
    (deg) B is 10-regular.

Proof. diag(N^2) = 10 gives (deg). (E+)-(E-) is the (x,y) entry of N^2 = N + 12I - RR^T, since
(N^2)_xy = Y - Z, N = P - P', r_x.r_y = Gam - Del. (E+)+(E-) is twice the (x,y) entry of
BD + DB + D = E, using (B^2)_xy = Y + Z, B = P + P', (MM^T)_xy = Gam + Del, (BD)_xy = B_(x,pi y),
(DB)_xy = B_(pi x, y). (R2') is DM = T: M_(pi x) = 2*1 - M_x - (BM)_x / 2.
Special cases used below: at y = pi x: Y + Z = 2 - t(x) (common B-neighbours of x and pi x).

---------------------------------------------------------------------------------------------------
## R3. Mod-2 structure of B for every N in S  [PROVED HERE; uses S only, not L_N]

Statement. Over GF(2), with G = MM^T:
 (a) B^2 + B = G and BG = GB = 0;
 (b) GF(2)^42 = V0 (+) V1 orthogonally, V0 = ker B^2, V1 = ker(B+I), and B = G + P where P is the
     orthogonal projection onto V1; GP = PG = 0, diag P = 0, P 1 = 0;
 (c) dim V1 = 20, rank_2 B = 26, rank_2 (B+I) = 22.

Proof. (a) N = B mod 2 entrywise, R = M mod 2, 12 = 0: N^2 = N + 12I - RR^T gives B^2 = B + G.
NR = 0 gives BM = 0 mod 2, so BG = 0, and GB = (BG)^T = 0.
(b) B^3 + B^2 = BG = 0, so x^2(x+1) kills B and V = ker B^2 (+) ker(B+I). For v in V0, w in V1:
Bw = w, so v.w = v.B^2 w = (B^2 v).w = 0. So the sum is orthogonal and both parts nondegenerate; P is
symmetric. On V1: B = I and G = B^2 + B = 0; on V0: B^2 = 0 so G = B. Hence B = G + P, GP = 0 and
PG = 0 (G maps into V0, kills V1). P_xx = B_xx + G_xx = 0 + 2 = 0; P1 = B1 + G1 = 10*1 + M(12*1_7) = 0.
(c) N + 3I = B + I mod 2 and rank_Q(N+3I) = 42 - 20 = 22 (eigenvalue -3 has multiplicity 20), so
rank_2(B+I) <= 22. On V0, G is nilpotent so B + I = G + I is invertible; on V1, B + I = 0. Hence
rank_2(B+I) = dim V0, so dim V1 >= 20. N - 4I = B mod 2 and rank_Q(N-4I) = 27, so rank_2 B <= 27.
rank_2 B = rank(G) + dim V1 = 6 + dim V1 (rank_2 G = 6: im M^T = even-weight vectors E, and M is
injective on E because ker M = <1_7> and 1_7 is odd). So dim V1 <= 21. P is an idempotent with
trace 0, so dim V1 = rank P is even: dim V1 = 20.

Test: identities checked on fixed data in work/checks/c01. No complete N is available to test (b),(c).
Consequence for EX: a necessary condition on every N in S (hence on every candidate). By itself it
does not exclude anything; it is the engine of R4, R5.
What remains: whether the GF(2) conditions are compatible with (R2') for general pi.

---------------------------------------------------------------------------------------------------
## R4. The all-cells family is empty  [PROVED HERE + CHECKED COMPUTATION C02]

Statement. There is no N in S with L_N nonempty whose matching is pi = kappa, i.e. D pairs (c,+)
with (c,-) for all 21 cells. Graph form: no srg(99,14,1,2) with a one-fixed-point involution in which
the four roots of every cell {i,j} form a 4-cycle.

Proof. (i) By (R2') with supp pi x = supp x: f_x(k) = 0 on supp x, 4 elsewhere, so every B-neighbour of
x lies in a cell disjoint from supp x. By R2 at y = kappa x: B(x) cap B(kappa x) is empty. Both have 10
elements inside the 20 orbits of the 10 cells disjoint from supp x, so they partition those orbits.
(ii) Hence for disjoint cells c, d the 2x2 block B[c,d] has all row and column sums 1: it is a
permutation matrix, recorded by g(c,d) in GF(2) (g = 0: c+~d+, c-~d-; g = 1: crossed). B[c,d] = 0 if c, d
meet. Write p_d(x) for the neighbour of x in d.
(iii) Cocycle. If c, d, e are pairwise disjoint and y = p_d(x), x in c: in (E+)+(E-) all terms except
(B^2)_xy vanish or are known: B_xy = 1, s = 0, B_(x,kappa y) = B_(kappa x,y) = 0 (permutation block),
D_xy = 0, so (B^2)_xy = 3. The common neighbours lie in the three cells inside [7] minus (c cup d),
at most one per cell; so all three coincide, in particular p_e(x) = p_e(y), i.e.
g(c,d) + g(d,e) + g(c,e) = 0. So g is a 1-cocycle of the triangle complex of the Kneser graph KG(7,2).
(iv) H^1(triangle complex of KG(7,2); GF(2)) = 0 (C02: 21 vertices, 105 edges, 105 triangles,
rank d0 = 20, rank d1 = 85). So g(c,d) = h(c) + h(d).
(v) Take c, d with |c cap d| = 1, x = c^s in c, y = d^s' in d. B_xy = 0 and s(x,y) = 1, so by R3(a)
(B^2)_xy is odd. The common neighbours lie in the 6 cells e inside W = [7] minus (c cup d), one
candidate per cell, and they coincide iff g(c,e) + g(d,e) = s + s'. But g(c,e) + g(d,e) = h(c) + h(d)
does not depend on e, so (B^2)_xy is 0 or 6: even. Contradiction.

Strongest test: C02 (exact GF(2) rank computation). Consequence for EX: eliminates the specified
family pi = kappa (i)-type exclusion. Remains: all other pi.
Note: DUPLICATION_NOTES item 6 mentions a "special quotient-family exclusion" in an unaudited note that
is not available to me; R4 may overlap with it. R4 is proved here independently.

---------------------------------------------------------------------------------------------------
## R5. Local 3|4 obstruction  [PROVED HERE]

Statement. Call a cell c "type 2" if pi pairs its two orbits. There is no N in S with L_N nonempty
for which some partition [7] = T (+) W, |T| = 3, |W| = 4, has all 3 cells inside T and all 6 cells
inside W of type 2.

Proof. For a type-2 cell c, step (i) of R4 applies verbatim to its orbits: their B-neighbours lie in
cells disjoint from c and every orbit of a cell disjoint from c has exactly one B-neighbour in c.
So for two disjoint type-2 cells the block is a permutation (label g). Let {e,e'} be one of the three
partitions of W into two cells, x in e, y = p_e'(x). As in R4(iii), (B^2)_xy = 3, and the common
neighbours lie in cells disjoint from e cup e' = W, i.e. in the three cells of T, at most one in each
(they are type 2). So p_c(x) = p_c(y) for every cell c in T: g(e,c) = g(e,e') + g(e',c).
For distinct c, d in T this gives phi(e) = phi(e'), where phi(e) = g(c,e) + g(d,e).
Now take x in c, y in d (c, d in T meet in one point, c cup d = T). B_xy = 0, s = 1, so (B^2)_xy is odd
(R3(a)); the common neighbours lie in the 6 cells of W, one candidate each, coinciding iff
phi(e) = s + s'. Since phi is constant on each of the three complementary pairs, the count is even.
Contradiction.

Consequence for EX: excludes every pi containing such a 9-cell configuration. It does not use H^1.
Remains: pi with fewer type-2 cells. OPEN whether type-2 cells can occur at all.

---------------------------------------------------------------------------------------------------
## R6. Type-2 rigidity package: Lemmas G0, G, E', H, J  [PROVED HERE]  -> see LEMMA_H.md (frozen)

Hypotheses: feasible (N,D); T4 as working lemma. Only (Deg), (P), (Q) are used (LEMMA_H.md s.0).
 G0: at a type-2 cell c, B(c^0) and B(c^1) partition Disj(c).
 G : every orbit has exactly one B-neighbour in each type-2 cell disjoint from its cell, none in
     type-2 cells meeting it.
 E': phi_c(w) + phi_d(w) = g(c,d) for disjoint type-2 c, d and w avoiding c cup d (cocycle, extended).
 H : overlapping type-2 cells c, d  =>  [7]\(c cup d) contains two disjoint non-type-2 cells.
 J : a type-2 cell v  =>  some cell disjoint from v is not type 2.
Consequence for EX: necessary conditions on the type-2 set Y. Nothing when Y is empty.

## R7. Support classification under H + G4 + PI, and the extremal case  [CHECKED COMPUTATION + PROVED HERE]

Exhaustive over 2^21 subsets (work/code/classify_XH.c; data/classify_XH_v1.txt): 133 S7-classes of
possible type-2 sets Y; n2 = |Y| <= 11; n2 = 11 only for Y = K(U) + {V} (U a 5-set, V its complement).
That class forces pi(orbits of {i,v1}) = orbits of {i,v2} (hand proof, LEMMA_H.md s.7) and is empty by
Lemma J. With J added: 132 classes, max n2 = 10 (unique class).

## R8. First SAT diagnostic over the 133 classes  [CHECKED COMPUTATION, solver-reported, NO certificates]

See SAT_PASS_1.md. Unsigned model only. 99 UNSAT, 29 UNKNOWN (20k conflicts), 5 not run; 3 more
excluded by core containment: 102 excluded, 31 unresolved (all with n2 <= 6, sparse: forests or one
triangle with pendant edges; includes n2 = 0, the general case). Smallest cores found: K3+K2, C4, C5,
K1,4+K2 (as sets of type-2 cells). No SAT model found.
Consequence for EX (if certified): reduction to 31 support types; EX undecided because n2 = 0 remains.
What remains: a rigidity package for type-0/1 squares, or use of the sign equations.

---------------------------------------------------------------------------------------------------
## R9. The sign lift is linear mod 2  [PROVED HERE]

Statement. Fix B = |N| and write N = B - 2Pm, Pm = [N = -1] (symmetric 0/1, supported on B). Then
N in S implies, over GF(2),
      Pm B + B Pm + Pm = (B^2 - B + RR^T)/2      and      Pm M = (BR)/2,
both LINEAR in Pm for fixed B (the right-hand sides are integer matrices by R3(a) and BR = 0 mod 2).
Proof. N^2 = B^2 - 2(B Pm + Pm B) + 4 Pm^2 and N^2 = N + 12I - RR^T = B - 2Pm + 12I - RR^T; reduce
mod 4 and divide by 2. NR = 0 gives BR = 2 Pm R exactly; reduce mod 2 using R = M mod 2.
Use: for any unsigned candidate (pi, B) the existence of a sign pattern satisfying S mod 4 is a GF(2)
linear-algebra question (210 unknowns). Not yet exploited (no unsigned candidate exists to test on).

---------------------------------------------------------------------------------------------------
## R10. Joint signed/unsigned system: line decomposition (Theorem S) and Lemma CM
##      [PROVED HERE; counts checked on m = 11 in c07]  -> full statements/proofs: JOINT_CHECKPOINT_1.md

Hypotheses: feasible (N,D), T4 as working lemma; no assumption on the type-2 support.
 (a) every B-edge is star / apex (beta = 1) / E*; negative B-triangles partition E*; T_- = 28 + n1 + 2 n2.
 (b) star at k iff N_xy = -x_k y_k; C_k cycles alternate, are even, holonomy (-1)^(L/2).
 (c) apex concordance: type 0 -> one concordant + one discordant apex (not Q-adjacent);
     type 1 -> one apex, concordant iff the positive representatives disagree at the common coordinate.
 (d) e_F even, 94 <= e_F <= 112; #negative s=1 edges = n1 (mod 2); #negative apex edges = n0 + n1^a (mod 2).
 (e) Lemma CM: non-adjacent, non-pi cell-mates are never opposite on a 4-cycle of C_i or C_j; distance 2
     in C_i or C_j forces beta = 0.
Consequence for EX: (b),(e) exclude unsigned configurations that the local unsigned equations allow;
valid with Sigma = empty. Not decisive. Global product of (a)-(d) is tautological (F5).
Also PROVED: with Sigma = empty no three sigma-squares have pairwise disjoint supports, so the cocycle
mechanism of R4/R6 (and notes 17-18) has no 2-cells there.
Duplication: see DUPLICATION_CHECK.md (R1-R4, G0, E', R9 are rediscoveries; H, J add nothing to the
certified frontier). (b)'s evenness is probably known in the repository (alternating A_c/B_c cycles in
note 19 s.7); (e) was not found in the parts read.

---------------------------------------------------------------------------------------------------
## R11. Ternary note checked; signing problem restated exactly; rigidity obligation
 - PROOF.md Lemma 2.1 and Theorems 3.1, 3.2 of the (unreviewed) ternary note: CHECKED HERE, correct
   (TERNARY_VERIFICATION.md s.1-2). For ANY complete unsigned pair (B, D) both capacities hold
   automatically (T = DM, E = BD + DB + D), so feasibility of a signing N of B is EXACTLY the F3
   projector problem with support B (s.3). Reformulation only.
 - JOINT_CHECKPOINT_1 reclassified (RECONCILIATION_2.md): (b) rediscovered (c1 note 149 s.2); the rest
   newly stated with no demonstrated effect; nothing stronger than the frontier; nothing excluded.
 - Obligation (R) "at most one feasible signing per complete unsigned pair": OPEN.
   PROVED: cycle-union, zero-sum rows (|X(u)| in {0,3..7,10}), apex edges with s = 1 never flip,
   and flips confined to overlap edges live on all-type-0, apex-free, pairing-closed components of the
   cycle graph (OBLIGATION_RIGIDITY.md). Missing: flip sets containing a disjoint-support edge.

---------------------------------------------------------------------------------------------------
## R12. Type-1 squares are rigid: Theorem A  [PROVED HERE; arithmetic CHECKED in checks/c08]
##      -> full statement, pre-registration and proofs: ONE_CANDIDATE_T1.md

Hypotheses: one complete unsigned pair (B, D) (in particular one feasible triple); T4 as working lemma.
Only (P) and (Q) are used; no sign, symmetry, type-2 cell or second signing.
Statement. For every type-1 square S = {x, y}, supp x = {a,c}, supp y = {b,c}:
 (i) the apex z lies in a cell inside W = [7] minus {a,b,c};
 (ii) neither x nor y has a B-neighbour in the cell {a,b};
 (iii) exactly one W-orbit (the hole) is adjacent to neither x nor y.
Equivalently the Wilbrink-Brouwer dichotomy of c2_experimental note 07 is always (x0, x3) = (2, 0).
Proof idea: list the 12 "entries" (B-neighbours, partner twice) of the apex (state (b)) or of the
{a,b}-neighbour (state (a1)); (P) and (Q) give their total incidence with {a,b,c} and with S as 7 over 10
entries, resp. 9 over 11, so W-orbits non-adjacent to S would have to exist, which those states forbid.
Pre-registered CLAIM T1 (apex in {a,w} or {b,w}, W-orbits partitioned between x and y) is therefore
impossible for every type-1 square: T1 holds in a candidate only when n1 = 0.
Also recorded (same file): second-order consequences of (a0) (three cases for the hole versus the apex
square), and the first-order type-0 classification (a cross apex forces configuration C1: one hole,
equal to the partner of that apex).
Consequence for EX: restricts every candidate with n1 >= 1, in every branch; excludes nothing. Being a
consequence of the unsigned layer it is implicitly contained in exact unsigned (Q-stage) models, so it
does not move any solver-level frontier. Not found in the parts of notes 07 and 19 read.
Remains: whether (a0) can occur at all (claim N1: n1 = 0); the method has slack there at second order.

---------------------------------------------------------------------------------------------------
## R13. Signed apex/hole claim T1S: FALSE at radius one  [CHECKED EXAMPLE; two independent checkers]
##      -> pre-registration, attempt, lemmas, reassessment: ONE_CANDIDATE_T1S.md

Claim (pre-registered): the signed system Sigma_AH on the rows of x, y, z (apex), o (hole) of a type-1
square in state (a0) (all (E+), (E-) inside the four rows, their NR rows and profiles, and the boundary
inequalities from (E+-) toward all other orbits) has no solution. It would have given n1 = 0.
Result: explicit solution K3 (case (iii), o = pi z), verified by checks/c09 (orbit level) and checks/c10
(lift level, lambda/mu). Built by hand; no search.
By-products (PROVED HERE, case (iii) unless stated): L1 hole not adjacent to kappa z (unsigned);
L2 apexes of {z, o} adjacent to x or y avoid supp z (unsigned); L3 sign rule for the x-z / y-z common
neighbours in the cells {2,.} / {1,.} (signed, all cases); L4 sign rule for hole neighbours sharing a
coordinate with z (signed); L5 no star neighbour of z is adjacent to the hole (signed).
Why it fails: at radius one the four rows couple only through seven shared neighbours, whose
concordances give six sign relations; all other entries enter only their own balance rows.
Consequence for EX: none. The type-1 line is STALLED at radius one (missing: a signed relation at
radius >= 2, which is a search).

---------------------------------------------------------------------------------------------------
## R14. 7-rank parity of the integral lift (P7): PROVED HERE, but a REDISCOVERY with no leverage
##      -> LATTICE_PARITY_P7.md

For every integral solution N of (S): rank_F7(N - 4I) = 7 + g with g odd (oddity formula applied to the even,
2-unimodular -3-eigenlattice, whose 3-part is fixed by R). Identical to c2_experimental note 10 s.3 item 4 (same
mechanism). Holds for every integer solution, so no admissible object can violate it; no branch datum determines
the 7-rank. Excludes nothing. Route stopped (BvLS comparison not run: stop rule met).

## R15. Scan for a different global one-candidate mechanism: none with leverage  -> GLOBAL_MECHANISM_SCAN.md
Checked and found automatic/known/tautological: arithmetic invariants of the lift; sigma fixed-point parities of
parameter-determined substructures (counts in checks/c11: 99/1, 693/7, 231/7, 2079/21, 33264/0); global sum of
the square defects (= 4 n0 + n1, exact); universal GF(2) combinations of the sign lift. Grid parity gives
n2 = G (mod 2) with G (number of 3x3 grids) not fixed by the parameters: leverage only with an independent G mod 2.

---------------------------------------------------------------------------------------------------
## R16. Coupled (Gaussian-unit) form; BvLS calibration limit  [PROVED HERE] -> OBJECT_ROUND_1.md
(a) EX <=> there are integer symmetric zero-diagonal Q, N with N^2 = N + 12I - RR^T, NR = 0,
    Q^2 + Q + MM^T = 12I + 4J, QM = 4J - 2M and (Q_xy - 1)^2 + N_xy^2 = 1 for x != y (T4 used only in "=>").
    Then D = a o b with a = (Q - N)/2, b = (Q + N)/2. Classification: C (new formulation of known information).
(b) G0(iii), G, E' (hence R4, R5) and #{w = 0} = #{w = 2} per square use 2(2m-4) = (m-2)(m-3), resp.
    2(2m-4) = C(m,2) - 1, both true only at m = 7. In BvLS (m = 11, all type 2) b2 = 0 and every block between
    disjoint cells has weight exactly 1. BvLS is no test for these statements. Supporting mathematics.

---------------------------------------------------------------------------------------------------
## R17. Projection analysis of the four-state path table; R2-Om1 closed  [PROVED HERE] -> OBJECT_ROUND_2.md,
##      R2_OMEGA1_USEFULNESS.md
(a) For one pair, ker(X -> (O_Q X, O_N X)) is 2-dimensional; its coordinates are delta_xy = N_(pi x,y) and delta_yx;
    beta = |delta_xy| + |delta_yx| is visible to the Q projection; every s.4 table is reconstructed separately.
(b) The coupling adds, at one pair, only the star rule (Theorem S(a)); gluing adds K5 (the same rule on delta).
(c) R2-Om1 (apex edges of each C_k^B cycle in one alternating class) = c2_experimental note 39 Lemmas 39.1(a)-39.2
    (rediscovered). New here: it is not implied by the Q stage locally (explicit verified Q configuration with four
    complete rows, checks/c13, c14). Classification: B for the lemma; supporting fact for (c13/c14). Excludes nothing.

---------------------------------------------------------------------------------------------------
## R18. Self-overlap of the quotient; positive-triangle complex; bridge graph and phase  -> OVERLAP_EXPLORATION.md
(a) [DERIVED] A closed orbit walk lifts to one sigma-invariant cycle iff (-1)^L prod N = -1 (matching steps carry
    +1 for a, -1 for b). Smallest: D-squares (L = 2), positive B-triangles (L = 3, antipodal hexagons; known, notebook
    s.3), unbalanced 4-cycles (L = 4).
(b) [DERIVED] Edge census (neg, pos) by kind; P = positive triangles is a pseudo-surface whose boundary edges are the
    (0,1) apex, (1,0) antistar and sibling edges, capped by D-squares or inner vertices.
(c) [DERIVED; m-uniform parts CHECKED on BvLS, c16] For every orbit x the bridge graph G_x (edges between
    N(x+) and N(x-) outside pi x) is exactly two paths plus cycles; sigma fixes exactly its two coordinate loops;
    hence a phase alpha/beta (alpha forced for types 1, 2 and for type 0 with an apex sharing a coordinate) and, for
    type 0, a canonical pairing of {z_c, z_d, i, j}. Square necklace: G_x and G_(pi x) close into one or two
    sigma-invariant cycles through the four apex lifts.
(d) [CHECKED, c15] BvLS: P is 165 positive K4s (sigma-invariant hexagonal tori in the lift); a property of BvLS,
    not a law.
Status: new representations; no compatibility law and no exclusion yet. Duplication: (a) known; (b)-(c) not found
(closest: c2_experimental note 29 s.3, faces G_a at inner vertices).
