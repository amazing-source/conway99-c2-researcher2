# Object round 1 (protocol of 2026-10-01): record

Outcome: NO object survived screening; NO theorem pre-registered; EX open.
Provenance: the round was worked out in reasoning that never reached disk (every turn after the c12 debug check
hit the output limit with no output). The identities below were RE-VERIFIED BY HAND at report time from the
definitions. No computation was rerun; the c12 and debug outputs were copied verbatim from the session log into
data/c12_microscope_bvls_mixed.txt. Hypotheses: (N, D) feasible, T4 as working lemma (D = matching pi), F0 unused.
Notation: Q = B + 2D = a + b, K = MM^T, H = RR^T, s(x,y) = K_xy, beta_xy = B_(x,pi y) + B_(pi x,y),
tau = sum_x s(x, pi x) = 2(n1 + 2 n2), b2 = #{x<y : beta_xy = 2}.

## 0. BvLS beta = 2 "discrepancy": not a bug; an m = 7 counting coincidence  [RESOLVED]
Debug check: D is the sibling map (all 55 cells type 2), D*B = 0, block B[(0,1),(2,3)] = [[0,0],[1,0]], beta there
[[1,0],[0,1]], max beta = 1. beta in c12 = (BD + DB)_xy, the definition in JOINT_CHECKPOINT_1.md. The expectation
"permutation blocks between disjoint type-2 cells" came from G0(iii)/Lemma G (LEMMA_H.md), whose proof uses
|B(c^0)| + |B(c^1)| = |Disj(c)|, i.e. 2(2m-4) = (m-2)(m-3), TRUE ONLY FOR m = 7 (m = 11: 36 of 72).
G0(i), G0(ii) hold for every m. At m = 11 the 36 disjoint cells carry total block weight 36; a weight-2 block
between type-2 cells must be a permutation (G0(ii) on both sides), and b2 = 0 forbids those, so in BvLS every
such block has weight exactly 1. Consequence: BvLS cannot calibrate anything that uses G0(iii), G, E', R4, R5 or
the identity #w0 = #w2 below (also m = 7 only). R4 (all-sibling family empty at m = 7) vs BvLS (all-sibling at
m = 11) is consistent for exactly this reason.

## 1. Coupled (Gaussian-unit) form of the system  [PROVED HERE]
Off the diagonal (a,b) in {0,1}^2 gives (Q-1, N) = (-1,0), (0,-1), (0,1), (1,0) for non-edge, a-edge (N=-1),
b-edge (N=+1), D-pair. Hence z_xy := (Q_xy - 1) + i N_xy is a Gaussian unit, and conversely an integer pair with
(Q-1)^2 + N^2 = 1 gives a = (Q-N)/2, b = (Q+N)/2 in {0,1} (Q o N = N follows).
(U) Q^2 + Q + K = 12I + 4J  <=>  E-equation (given D^2 = I);  QM = 4J - 2M  <=>  DM = T.
Q1 = 12 follows from QM = 4J - 2M; B1 = 10 from diag(S); so D := a o b has D1 = 1, D o B = 0.
EX <=> exists integer symmetric zero-diagonal (Q, N): (S), NR = 0, (U), QM = 4J - 2M, coupling.
(T4 used only in "=>".)  Z := (Q - J + I) + iN: Z o Z = J - I - 2B (Seidel of B), Z o conj(Z) = J - I,
ZZ^* = 2(b - Gamma) + 25I + 20J + i[N, Q - J], Gamma_xy = #{k : x_k y_k = +1} = (K + H)_xy / 2.
Spectra (m = 7): Q: 12^1, -2^6, 3^20, -4^15;  N: 4^15, -3^20, 0^7.

## 2. Objects
| | Object (layers) | First identity | Verdict |
|---|---|---|---|
| Om1 | signed 4-cycle split C4+/C4- of B (signed+unsigned, matching) | tr(QDQD) = 168 + 2b2, tr(Q^3 D) = 2604 + 3tau, tr B^4 = 14196 - 24tau + 16b2, c4(B) = 777 - 3tau + 2b2, C4+ - C4- = -315, C4+ = 231 - 3(n1+2n2) + b2, C4- = 546 - 3(n1+2n2) + b2 | KILLED: the identities tested are consequences of (S), (U), QM = 4J - 2M and D^2 = I, and they reduce to slack relations among the free counts c4, C4+-, b2, tau (nonnegativity: 3(n1+2n2) <= 126). [Corrected 2026-10-01: the earlier wording "consequence of the spectra of N, Q" was wrong; spectra do not determine arbitrary mixed words involving D, e.g. tr(QDQD) contains the free count b2.] |
| Om2 | D-pinching N + DND = 2(P+NP+ + P-NP-), square compression (matching+spectral) | \|N f_S\|^2 = 10 - h_S, h_S = r_x.r_(pi x) in {0, +-1} (+-1 iff type 1) | KILLED: entry (x, pi x) of (S); spectrum only interlacing (closed line); BvLS: generic in [-8, 9.7362], -8 x4, 0 x2, rest simple |
| Om3 | Gaussian type matrix Z (signed+unsigned+matching) | section 1 | KILLED: identities = coupling + (S) + (U); BvLS: Z has 110 distinct eigenvalues, ZZ^* simple spectrum; no m-uniform polynomial identity |
| Om4 | Y = N - H, idempotent mod 12 (mod 2 + mod 3) | Y^2 - Y = 12(I + H); Y mod 3 = P (ternary projector), Y mod 2 = P2; off-diagonal Y = N for s in {0,2}; for s = 1: Y = -H (N = 0), 0 (antistar), -2H (star); supp P = supp P2 + {star edges with s = 1} | KILLED: restatement of (S) given NR = 0, H^2 = 12H; support relation is the value table; both projectors known |
| Om5 | square-block / D-rectangle structure (matching+support+signs) | blocks B[S,S'] have weight w <= 2; beta <= 1 on B-edges; #{w=0} = #{w=2} for each S (m = 7 only); beta = 2 <=> permutation block, b2 = 2 rho (rho = # permutation blocks); then the cross pairs have s = 0, (B^2) = 0; each permutation block = induced cube in the 99-graph | NOT KILLED, NOT SHOWN USEFUL, NOT SELECTED (screening incomplete). Sub-variants: cube sign eps = N_xy N_(pi x, pi y) recorded gauge-dependent, and every sign choice closes the cube (D-squares are K_2,2); star-trail holonomy recorded "global product automatic" (exact trail rule not on file; covered by Theorem S(b) / F5) |

Proved toward EX in this round: only the coupled form (section 1). Conjectured: nothing pre-registered.

## 3. Closure of Om5 by the bounded compression test (2026-10-01, operator request)  [DONE; Om5 STOPPED]
U = 42x21 pair incidence (columns e_x + e_(pi x)), F = U/sqrt2, W = U^T B U. Then U^T U = 2I, UU^T = I + D,
DU = U, U^T D U = 2I, W_SS' = w(S,S') for S != S', W_SS = 2 B_(x,pi x) = 0.
 (i)  W1 = U^T B 1_42 = 10 U^T 1_42 = 20 1   [needs only (Deg); weaker than (Deg)].
 (ii) F^T Q F = (U^T B U + 2 U^T D U)/2 = W/2 + 2I   [holds for EVERY symmetric 0/1 B with B o D = 0: it is the
      definition of W, not a property of solutions].
Test of each Om5 fact against (i) + (ii):
 F3 (#{w=0} = #{w=2} per S): YES, given F2. Row S of W has 20 off-diagonal entries in {0,1,2} summing to 20.
 F2 (w <= 2): NO. W-level counterexample to "(i)+(ii) => F2": start from W = J - I (21x21), set
      W_12 = W_34 = 3, W_13 = W_14 = W_23 = W_24 = 0 (symmetric). Row sums stay 20, diagonal 0, and a block of
      weight 3 is a legal 0/1 2x2 block. F2 comes from the ENTRYWISE E-equation (Q) at a B-edge inside the block
      (three ones give beta = 2 on a B-edge: (B^2) + 1 + s + 4 = 4 impossible).
 F1 (beta <= 1 on B-edges), F4 (beta = 2 <=> permutation block; b2 = 2 rho; s = 0, (B^2) = 0 on cross pairs): NO;
      these are within-block statements, finer than W (W cannot tell a permutation block from a row/column block
      of weight 2); they are entrywise readings of (Q).
 F5 (D-rectangle = induced cube): NO; it is the definition of the lift (D-squares are K_2,2, a B-edge lifts to two
      edges), not a W statement.
 F6 (disjoint type-2 cells => D-rectangle): NO; Lemma G ((Deg), (P), (Q) and the m = 7 count).
Answer to the test: the Om5 facts are NOT all consequences of (i)+(ii); only F3 is (given F2). But every Om5 fact
is either the compression W with (i), or an entrywise reading of (Q)/(P)/(Deg), or a lift definition.
Classification: compression / repackaging (duplication class D: logically automatic from the existing exact
equations). Om5 STOPPED. No cube was enumerated.
