# FAILED / ABANDONED ATTEMPTS

## F1. Simulated annealing on the unsigned system (pi, B)   [abandoned]
Code: work/code/sa_unsigned.c (exact integer residuals, incremental updates checked against full
recomputation). Runs: up to 2e7 moves, several restarts, < 2 min each.
Result: energy never below ~700; about half of the 861 pair equations off by +-1.
Diagnosis: those residuals are exactly the GF(2) conditions of R3 (B^2 + B = MM^T mod 2). XOR-type
constraints give local search no gradient. Not evidence about existence either way.

## F2. Mechanism M3 (extra-symmetry ansatz)   [abandoned before starting]
Literature (LITERATURE.md items 1-2, EXTERNAL INPUT): a Conway graph with an involution has Aut = Z2,
so every ansatz with an automorphism besides s is already excluded.

## F3. Global trace / counting identities for the type distribution   [no information]
Counting B-triangles in two ways (tr Q^3, tr N^3, triangle decomposition of H) and the kappa-odd /
pi-even spectral compressions all reproduce identities already implied by S and L_N; they give no
restriction on (n0, n1, n2). Recorded so that it is not repeated.

## F4. Unsigned SAT on sparse type-2 supports   [stopped by design]
SAT_PASS_1.md: 29 classes exhaust 20k conflicts, all with n2 <= 7; the limiting class n2 = 0 is the
general quotient problem. Larger budgets were deliberately not tried (see SAT_PASS_1.md, point 3,
for why the unsigned type-2 package cannot separate these classes).

## F5. Global sign bookkeeping over the line decomposition   [closes tautologically]
Product of N over all B-edges, split into E* (negative triangles), star (root-sign rule) and apex
(concordance) parts, with the per-cycle holonomies of all C_k: the result is equivalent to
n0 + n1 + n2 = 21. A first version gave a spurious condition because it treated every type-1 apex as
discordant; corrected in JOINT_CHECKPOINT_1.md (c). Lesson: parity obstructions for Sigma = empty must use
mu-counts of pairs that are not on a common line or C_k 2-path.

## F6. CLAIM T1: "type-1 squares partition their W-orbits like type-2 cells"   [conclusion impossible]
Pre-registered in ONE_CANDIDATE_T1.md before development. The partition state (b) is impossible for
every type-1 square (Theorem A): the apex's 12 entries meet {a,b,c} and S only 7 times, forcing
non-adjacent W-orbits that (b) forbids. The actual structure is the opposite one: one hole, apex disjoint.
Lesson: the type-2 partition (defect 0) has no type-1 analogue (defect 2 is spent on the hole).

## F7. CLAIM T1S: the signed apex/hole system kills state (a0)   [false at radius one]
Pre-registered in ONE_CANDIDATE_T1S.md. Explicit solution K3 (checks c09, c10). R0, K1, K2 each failed on one
constraint (star edge with beta = 1; hole adjacent to kappa z; z concordant for (x, u2)), each giving a lemma;
K3 avoids all of them. Lesson: at radius one the signed equations only fix the concordance of the few shared
neighbours; placement of those neighbours on distinct coordinates leaves every balance row enough free entries.
Do not iterate apex constraints further by hand (radius two is a search).

## F8. Global lattice parity (7-rank of N - 4I)   [rediscovery, no leverage]
Proved rank_F7(N - 4I) even for every integral solution of (S); this is c2_experimental note 10 s.3.4, and note 10
s.4 already explains why it cannot filter. Lesson: invariants of the integral lift are automatic for (B, D, P)
(Lemma 2.1 + Thm 3.1 make the lift automatic); they bite only next to an independent computation of the invariant.

## F9. Object round 1: mixed objects Om1-Om5 (OBJECT_ROUND_1.md)   [no survivor]
Om1 (signed 4-cycle split) automatic: C4+ - C4- = -315, C4+ + C4- = 777 - 3 tau + 2 b2. Om2 (D-pinching) = entries of
(S) plus interlacing. Om3 (Gaussian type matrix Z) = coupling plus (S), (U); BvLS (c12): 110 distinct eigenvalues.
Om4 (Y = N - H mod 12) restates (S); Y mod 3 = P, Y mod 2 = P2 are known. Om5 (square blocks / D-rectangles): proved
facts are unsigned (w <= 2, #w0 = #w2 at m = 7, b2 = 2 rho, cube lift); its sign variants are dead (cube sign
gauge-dependent and unconstrained; star-trail holonomy = Theorem S(b) / F5). Usefulness test of Om5 not finished.
Lesson: an object that mixes layers only through the entrywise unit condition inherits the automatic identities of
each layer; BvLS refutes only m-uniform identities.

## F10. Object round 2 (joint path tables) and the usefulness test of R2-Om1   [no survivor; rediscovery]
The four-state path table at one pair: the s.4 family (beta; A, C) is reconstructed from the separate projections; its
hidden coordinates delta_xy = N_(pi x,y) are invisible to the pair's own equations and are the endpoint data of
the partner table (K1). The only joint constraint the gluing adds is the star rule (Theorem S(a)). The one object
that survived screening, R2-Om1 (apex edges of every C_k^B cycle lie in one alternating class), is genuinely joint
(c13/c14: a verified 4-centre Q configuration violates it) but is c2_experimental note 39 Lemmas 39.1(a)-39.2, and
its count form excludes nothing. Lesson: the joint content of single-pair and block-level path tables is the line
structure (lambda = 1) already exploited by the repository; new leverage has to come from configurations that are
not determined by one line at a time.
