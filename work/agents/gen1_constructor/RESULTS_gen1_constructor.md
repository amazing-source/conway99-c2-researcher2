# gen1_constructor -- results of the first bounded interval

Outcome: NO WITNESS. No complete (Q,N), no complete N in S, no complete unsigned (B,D) was found.
What was obtained: exhaustive exclusion of a list of symmetric constructions (at the level of S alone and at the
unsigned level), a short lemma explaining why symmetric ansaetze collapse into the type-2 regime, and a
calibration showing that two generic heuristics cannot find the known m = 11 object.

Conventions: MODEL.md s.1. W(B7) (signed coordinate permutations) acts on orbit indices x by g r_x = eta_x r_(gx);
S is invariant under N -> (eta_x eta_y N_(g^-1 x, g^-1 y)). "G-invariant N" means N_(gx,gy) = eta_x eta_y N_xy.

## A1. No G-invariant N in S for the following groups  [CHECKED COMPUTATION, two implementations]

Groups (generators in symS.py / sweep.py / unsigned_sym.py; coordinates 0..6, Fano lines {i,i+1,i+3} mod 7):
PSL(2,7) (168), 2^3:PSL(2,7) (1344, Fano sign characters), AGL(1,7) (42), 2^3:7:3, 2^3:7, 2^7:7, 2^7:7:3,
A7, S6 (fix 6), A6, PGL(2,5) and PSL(2,5) on {0..5} (fix 6), S5xS2, S4xS3, S3 wr S2 (fix 6), S5 (fix 5,6),
and the sign extensions S6 x <flip6>, PGL(2,5) x <flip6>, S5xS2 x <flip56>, S4xS3 x <flip456>,
S6 x <even flips>, PGL(2,5) x <even flips>, S3wrS2 x <flip6>.
Method (symS.py): orbits of G on pairs with sign tracking (classes with inconsistent sign are forced 0);
exhaustive enumeration of class supports with row weight 10 per row type; filters (B^2 = B + H mod 2 off the
diagonal, (B^2)_xy >= |H_xy| on non-edges); exact NR = 0 by meet-in-the-middle over signs; exact test of
N^2 = N + 12I - H. Independent re-check (verify_sym.py): classes rebuilt by signed union-find over generators
(class counts agree for every group), brute force over all 3^f class values where f <= 13, otherwise the
different filter BM = 0 mod 2 (from NR = 0) and the same exact tests. Both: 0 elements of S for every group listed.
Not exhaustive (support enumeration capped): Z7:Z3 (order 21) and D7 (order 14). Z7, Z3, Z5, Z2-type
groups not attempted (cost plan below).
Scope: G-invariant N only. A G-invariant B with a non-invariant signing is NOT covered by A1 (see A2).
Consequence for EX: excludes C2 solutions whose N is invariant under any listed group (via T4 the D would then be
determined by B). New at the level of S as far as checked; at the graph level symmetry exclusions are already
reported by the project (DUPLICATION_NOTES item 2), so leverage for EX is small.

Near-miss measurement (nearmiss.py): the 118 AGL(1,7)-invariant N with NR = 0 and row weight 10 are exact
objects satisfying C2a; the best has 756 nonzero entries in N^2 - N - 12I + H (L1 defect 1008; spectrum
far from 0^7 4^15 (-3)^20). Saved as nearmiss_AGL17_N.npy. Symmetric N are not close to S.

## A2. Unsigned level: no G-invariant B extends to a solution of C3+C4  [CHECKED COMPUTATION]

unsigned_all.py: all pair orbits of G (signs ignored), all supports with row weight 10, the implied filters
(square parity and BM even follow from C3, C4), then the complete enumeration of perfect matchings D with
D M = T, BD + DB + D = E (this is exactly C3+C4 for Q = B + 2D; the D-degree 1 is forced by C4 row sums and the
C3 diagonal). Result: no (B,D) for PSL(2,7), AGL(1,7), A7, S6, A6, PGL(2,5), PSL(2,5), S5xS2, S4xS3 and the
sign-extended groups of A1. Capped (not exhaustive): 7:3, D7, S3wrS2, S5.
Observation used: T and E in L_N depend on B = |N| only, so EX <=> (exists unsigned (B,D) solving C3, C4) and
(B has a signing in S). Known in substance (RESULTS.md R11).

## A3. Lemma (stabilizer forces the D-cell)  [PROVED HERE]

Hypotheses: Q = B + 2D satisfies C4 (D a perfect matching); g in W(B7) with coordinate permutation pi;
B invariant under the induced permutation of orbit indices; g x = x.
Conclusion: pi fixes the cell c_D(x) setwise.
Proof: C4 row x reads kappa_x(t) := sum_y B_xy M_yt = 4 - 2[t in c_x] - 2[t in c_D(x)]. Since M_(gy, pi t) = M_yt
and B_(x,gy) = B_(gx,gy) = B_xy, kappa_x(pi t) = kappa_x(t). As pi fixes c_x, the indicator of c_D(x) equals
(4 - 2[t in c_x] - kappa_x(t))/2, which is pi-invariant.
Corollary: if for every x some element of Stab_G(x) fixes no cell other than c_x, all 21 D-pairs are type 2,
which RESULTS.md R7 (n2 <= 10, project result, CHECKED COMPUTATION there) excludes. This is why every
transitive-on-cells group with large cell stabilizers (S6, A6, S7, A7, ...) dies before any quadratic test.
It says nothing for groups acting freely on orbit indices (Z7, Z3 of type (3)(3)(1), Z5): the live symmetric cases.
Duplication: not found in RESULTS.md/FAILURE_MEMORY.md; elementary; classification "known consequence with a
new proof / no leverage" (it only organises symmetric ansaetze).

## A4. Calibration wall for generic heuristics  [CHECKED COMPUTATION]

- rrr.py: Elser RRR between {X R = 0, spectrum 4^15, (-3)^20 on R-perp} and entrywise {0,+-1} rounding.
  m = 7: 363k iterations, best distance 9.68. m = 11 (S_11 is NONEMPTY: BvLS): best distance 25.5.
- qsearch2.py: tabu on single B-entry toggles with an exact O(1) delta of ||C3 residual||^2 + ||C4 residual||^2
  (formula validated against recomputation in-run). m = 11 with the TRUE D (same-cell matching of BvLS):
  274k iterations, best F = 9466. m = 7, random D: best F about 1090 (qsearch.py, 3 seeds, similar).
Conclusion: both heuristics fail on the calibration case where a solution exists, so their failure at m = 7 is
not evidence for NOT-EX. Any future "search returned UNKNOWN/no model" must be calibrated on BvLS first.

## A5. Starting-note derivations  (see STARTING_NOTE.md)  [PROVED HERE; status]

D1 spectrum of N and Q: N: 0^7, 4^15, (-3)^20; Q: 12, (-2)^6, 3^20, (-4)^15 (Q acts on col M as 2J7 - 2I7).
D2 99 vertices = vectors of Z^7 of norm <= 2 (ternary words of weight <= 2), sigma = negation; adjacencies at
0 and +-e_t are H(7,3) adjacencies. In BvLS these are the Golay coset leaders. D6 checked on bvls_m11 data
(bvls_look.py): all 55 D-pairs type 2; states: overlap-1 pairs all n, N supported on disjoint cells only.
Duplication: D6 rediscovery (RESULTS.md R16(b)); D2 a relabelling of the model; D7 (all-grid direction
structure) moot because all-type-2 is excluded (R7).

## Cost / exhaustiveness plan for the remaining symmetric constructions (not launched)
Z7 (free, 6 row types, 123 pair classes) and Z3 = <(012)(345)> (14 row types, about 287 classes): naive support
enumeration explodes (> 3e5 supports in 30 s for 7:3). Needed: row-type-wise CSP with the A3/C4 coverage
constraints and exact NR, in C or a SAT solver with certificates; estimated far beyond the 5-minute Python bound.
Do this only if a Z7/Z3 graph-level exclusion is not already certified elsewhere (DUPLICATION_NOTES item 2).

## Provenance
Derived here: A3, A5 (D1, D2, D7), all code. Taken from kernel: Theorem C, MODEL.md conventions, T4 (working
lemma; only used to say that a G-invariant N would give a G-invariant D). Taken from project notes (after own
derivation, targeted grep): R7 (n2 <= 10), R11, R16. Independently checked: A1 by two implementations; A2 by
one implementation (shares LN_check with A1); delta formula of qsearch2.py checked in-run.
