# Object round 2 — joint path compositions of the four-state variable (started 2026-10-01)

Starting point: Theorem C (THEOREM_C.md, frozen). Hypotheses: (Q, N) solves (C1)-(C5). No other input unless named.
Written incrementally; each section is final when written unless marked DRAFT.
Parameter-independence is stated for every derivation (m = 7 vs the m-uniform system satisfied by BvLS).

## 1. Alphabet
Off the diagonal c_xy := (Q_xy - 1, N_xy) takes one of four values; names and value maps:
  n = (-1, 0): non-edge          Q = 0, N = 0
  d = ( 1, 0): matching pair     Q = 2, N = 0
  m = ( 0,-1): edge with N = -1  Q = 1, N = -1
  p = ( 0, 1): edge with N = +1  Q = 1, N = +1
E := {m, p} (edges), Z := {n, d} (N-zero states). c_yx = c_xy.
Row census (Theorem C(b)): every row has exactly one d (at pi x), ten states in E, thirty n.  [m = 7 numbers;
m-uniform form: one d, 2m - 4 edges.]

## 2. Contribution table of a length-2 path x - z - y (x != y, z not in {x, y})
The path adds Q_xz Q_zy to (Q^2)_xy and N_xz N_zy to (N^2)_xy (z = x, y add 0: zero diagonals).
Pair (Q-contribution, N-contribution) for (c_xz, c_zy):

            n        d        m         p
   n      (0,0)    (0,0)    (0,0)     (0,0)
   d      (0,0)    (4,0)    (2,0)     (2,0)
   m      (0,0)    (2,0)    (1,1)     (1,-1)
   p      (0,0)    (2,0)    (1,-1)    (1,1)

Read in the value pairs (Q, N), the contribution is the componentwise product, and it is again a state value:
n absorbs everything; d.E = E.d = d; equal signs give p = (1,1); opposite signs give m = (1,-1); d.d = 2d.
A d-step erases the sign of the other step: (d, m) and (d, p) contribute the same (2, 0).

Structural facts (Theorem C(b)): c_xz = d iff z = pi x. Hence for x != y the d-row of the path distribution is the
single z = pi x, the d-column the single z = pi y, (d, d) never occurs (pi x = pi y forces x = y), and if
c_xy = d both are empty.

## 3. The equations at one pair, in path counts
For x != y put
  A_xy = #{z : N_xz N_zy = +1}   (concordant E.E paths)
  C_xy = #{z : N_xz N_zy = -1}   (discordant E.E paths)
  beta_xy = #{z : one step d, the other in E} = B_(pi x, y) + B_(x, pi y)
  Gamma_xy = #{k : x_k y_k = +1}, Gamma'_xy = #{k : x_k y_k = -1}  (s = Gamma + Gamma', H = Gamma - Gamma')
(C3) at (x,y):  A + C + 2 beta = 4 - Q_xy - s_xy.
(C2) at (x,y):  A - C = N_xy - H_xy.
Equivalent channel form (sum/difference; a = (Q-N)/2, b = (Q+N)/2):
  (E+)  A + beta + Gamma + a_xy = 2,      (E-)  C + beta + Gamma' + b_xy = 2.
In value pairs: sum_z (c_xz . c_zy) + Gamma p + Gamma' m + conj(c_xy) = 2d, where conj swaps p and m.
The inner vertices act as extra intermediate points: an inner vertex shared with equal signs composes to p, with
opposite signs to m.
Parameter-independence: uses lambda = 1, mu = 2 only (the "2" on the right); valid for every m (BvLS included).

## 4. The conditional joint table (complete)
Given c_xy and (Gamma, Gamma') (fixed by the coordinates: (0,0) disjoint cells; (1,0) s = 1, H = +1;
(0,1) s = 1, H = -1; (1,1) siblings), the equations allow exactly the one-parameter families
  A = 2 - Gamma - a - beta,  C = 2 - Gamma' - b - beta,  beta >= 0,  A >= 0,  C >= 0:

 c_xy \ (Gamma,Gamma') | (0,0)               | (1,0)                  | (0,1)                  | (1,1)
 n                     | beta 0..2, A=C=2-b. | beta 0..1, A=1-b,C=2-b | beta 0..1, A=2-b,C=1-b | beta 0..1, A=C=1-b
 d (beta = 0 forced)   | A = C = 1           | A = 0, C = 1           | A = 1, C = 0           | A = C = 0
 m                     | beta 0..1, A=1-b,C=2-b | STAR: beta=0, A=0,C=2 | antistar: beta 0..1, A=C=1-b | beta=0, A=0, C=1
 p                     | beta 0..1, A=2-b,C=1-b | antistar: beta 0..1, A=C=1-b | STAR: beta=0, A=2,C=0 | beta=0, A=1, C=0
(b = beta in the cells.)  For c = d the column is the type of the square: (0,0) type 0, (1,0)/(0,1) type 1,
(1,1) type 2; this is the apex table (Theorem S(c)).  Parameter-independent (for every m).

## 5. Projection analysis, part 1: three views of one conditional table  [PROVED HERE; m-uniform]
Fix x != y, the endpoint state c_xy and the overlap class (Gamma, Gamma'). For r, s in {n, d, m, p}:
  X_rs = #{z not in {x,y} : c_xz = r, c_zy = s}   (16 entries, sum 40 at m = 7; sum m(m-1) - 2 in general).
Value maps: q(n) = 0, q(m) = q(p) = 1, q(d) = 2;  v(n) = v(d) = 0, v(m) = -1, v(p) = +1.

View F (full): X itself.
View Q: X^Q_ij = sum_{q(r)=i, q(s)=j} X_rs (i, j in {0,1,2}), explicitly
  X^Q_00 = X_nn   X^Q_01 = X_nm + X_np   X^Q_02 = X_nd
  X^Q_10 = X_mn + X_pn   X^Q_11 = X_mm + X_mp + X_pm + X_pp   X^Q_12 = X_md + X_pd
  X^Q_20 = X_dn   X^Q_21 = X_dm + X_dp   X^Q_22 = X_dd.
View N: X^N_kl = sum_{v(r)=k, v(s)=l} X_rs (k, l in {-1,0,1}), explicitly
  X^N_00 = X_nn + X_nd + X_dn + X_dd   X^N_0,-1 = X_nm + X_dm   X^N_0,1 = X_np + X_dp
  X^N_-1,0 = X_mn + X_md   X^N_1,0 = X_pn + X_pd
  X^N_-1,-1 = X_mm   X^N_-1,1 = X_mp   X^N_1,-1 = X_pm   X^N_1,1 = X_pp.
Everything else available to each layer separately (all of it acts on X only through the view's cells):
 Q layer: Q-census of every row (one 2, ten 1, thirty 0: diagonal of (C3) gives sum_y Q_xy^2 = 14, (C4) gives
   Q1 = 12, so e1 + 2e2 = 12, e1 + 4e2 = 14); the 2s form a fixed-point-free matching (so X^Q_2. is the single
   z = pi x, X^Q_.2 the single z = pi y, X^Q_22 = 0); the rows of (C4); the equation
   (EQ)  X^Q_11 + 2 X^Q_12 + 2 X^Q_21 + 4 X^Q_22 = 4 - Q_xy - s_xy.
 N layer: N-census (ten nonzero entries per row, p_x + m_x = 10, p_x - m_x free); the rows of NR = 0; the equation
   (EN)  X^N_1,1 + X^N_-1,-1 - X^N_1,-1 - X^N_-1,1 = N_xy - H_xy.
 Both layers fix the marginals of their own view from the row censuses (row x minus z = y, row y minus z = x).

## 6. Projection analysis, part 2: kernel, compatibility, and the status of beta  [PROVED HERE; m-uniform]
(a) Kernel. ker(X -> (O_Q X, O_N X)) on R^16 is 2-dimensional, spanned by
      kappa1 = e_nm - e_np - e_dm + e_dp,     kappa2 = e_mn - e_pn - e_md + e_pd.
    Proof, cell by cell: the four E.E cells are separated by N (each alone in its N-cell) -> 0. The four Z.Z cells
    nn, nd, dn, dd are separated by Q -> 0. Z.E cells: X_nm + X_np = 0 (Q01), X_dm + X_dp = 0 (Q21),
    X_nm + X_dm = 0 (N0,-1), X_np + X_dp = 0 (N0,1): rank 3 on 4 unknowns, solution t(1,-1,-1,1). E.Z: same, u.
(b) Compatibility (cokernel). The image has dimension 14 = 18 - 4; (O_Q, O_N) must agree on the coarse table
    {Z,E} x {Z,E}:  X^Q_11 = sum_{k,l != 0} X^N_kl;  X^Q_01 + X^Q_21 = X^N_0,-1 + X^N_0,1;
    X^Q_10 + X^Q_12 = X^N_-1,0 + X^N_1,0;  X^Q_00 + X^Q_02 + X^Q_20 + X^Q_22 = X^N_00.
(c) beta is DETERMINED by the separate Q projection: beta_xy = X^Q_12 + X^Q_21 (= B_(x,pi y) + B_(pi x,y)).
    A = X^N_1,1 + X^N_-1,-1 and C = X^N_1,-1 + X^N_-1,1 are determined by the N projection.
    beta is not invisible and not partially constrained: it is a Q cell sum.
(d) Every s.4 joint table (beta; A, C) is therefore reconstructed from the separate projections.
    VERDICT on the s.4 family: the operator's STOP condition is MET for it. The one-parameter family in beta exposes
    no mixed information.
(e) What the coupling adds to the two equations is exactly compatibility (b), first line (E.E totals agree).
    With A, C >= 0 it gives beta <= (4 - Q - s - |N - H|)/2, against beta <= (4 - Q - s)/2 from (EQ) alone.
    Case check over the 16 cells of s.4: the bounds differ only for star edges (c in E, s = 1, N = -H), where the
    joint bound is beta = 0 and Q alone allows 1. This is Theorem S(a) (JOINT_CHECKPOINT_1.md): known.
(f) But the 16-cell table is NOT reconstructed: the kernel (a) is nonzero. See s.7.

## 7. The joint degree of freedom delta  [PROVED HERE; m-uniform]
(a) Canonical coordinate. Within a fiber of (O_Q, O_N) the table moves only along t kappa1 + u kappa2.
    X^Q_21 = X_dm + X_dp is fixed by the Q view and is 0 or 1 (the single z = pi x), and likewise X^Q_12.
    If X^Q_21 = 0, t cannot move. If X^Q_21 = 1, (X_dm, X_dp) is (1,0) or (0,1). The smallest integer measuring
    the motion is the bit X_dp, equivalently the sign
        delta_xy := X_dp - X_dm = N_(pi x, y)      (in {-1, 0, +1}; 0 exactly when B_(pi x,y) = 0).
    The second kernel coordinate is X_pd - X_md = N_(x, pi y) = delta_yx (transpose of table (y,x)).
    So the fiber of table (x,y) is parametrized by (delta_xy, delta_yx).
(b) Relation to beta: beta_xy = |delta_xy| + |delta_yx|. beta is the Q-visible absolute value; delta is its
    signed refinement. delta is NOT beta and NOT a centered or parity version of beta: its sign is the only thing
    hidden.
(c) Blindness: the equations at (x,y) do not see delta. The cells dm and dp both contribute (2, 0) to
    ((Q^2)_xy, (N^2)_xy) (s.2), and likewise md and pd.
(d) Critical test: same separate data, different delta, one conditional table (m = 7 census).
    c_xy = n, (Gamma, Gamma') = (0,0), p_x = m_x = p_y = m_y = 5. Rows r = n, d, m, p; columns s = n, d, m, p.
       X  :  n [21, 1, 4, 3]   d [0, 0, 0, 1]   m [5, 0, 0, 0]   p [3, 0, 1, 1]
       X' :  n [21, 1, 3, 4]   d [0, 0, 1, 0]   m [5, 0, 0, 0]   p [3, 0, 1, 1]      (X' = X - kappa1)
    Both tables satisfy every single-table condition:
     - row sums (n,d,m,p) = (29, 1, 5, 5) = row x census minus z = y;
     - column sums (29, 1, 5, 5) = row y census minus z = x;
     - X_dd = 0, a single d in the d-row and a single d in the d-column;
     - A = 1, C = 1, beta = 1: (EQ) 1 + 1 + 2 = 4 = 4 - 0 - 0 and (EN) 1 - 1 = 0 = 0 - 0.
    O_Q(X) = O_Q(X') (Q01 = 7, Q21 = 1, other cells equal) and O_N(X) = O_N(X') (N0,-1 = 4, N0,1 = 4, other
    cells equal). But delta = +1 in X and -1 in X'.
    So the fiber is nontrivial at the level of ONE conditional table, and delta carries genuinely mixed
    information. By (c) that information is unconstrained by the table's own equations.

## 8. Consistency laws linking the delta's (double counting of the 861 states)  [PROVED HERE]
The family {X^xy : x != y} comes from one state matrix iff all tables are computed from it. Double counting gives:
 K0 (transpose) X^yx_rs = X^xy_sr; so the second kernel coordinate of (x,y) is delta_yx.
 K1 (d-row gluing) for y != pi x: X^xy_ds = [c_(pi x,y) = s] for every s (the only z with c_xz = d is pi x).
    Hence delta_xy = v(c_(pi x,y)), |delta_xy| = [c_(pi x,y) in E] = X^xy,Q_21.
    THE HIDDEN COORDINATE OF TABLE (x,y) IS THE ENDPOINT STATE OF TABLE (pi x, y): free in (x,y), conditioning
    data in (pi x, y).
 K2 (partner swap) K1 at (pi x, y): delta_(pi x, y) = N_xy. As matrices delta = DN.
 K3 (row aggregation) sum_{y : c_xy = r} X^xy_ds = X^(x, pi x)_rs (the matching-pair table of x). With the d row
    of s.4 (A, C fixed by the type t_x of the square of x):
      sum_{c_xy = p} delta_xy - sum_{c_xy = m} delta_xy = A - C = -H_(x, pi x);
      sum_{c_xy in E} |delta_xy| = A + C = 2 - t_x;   sum_y |delta_xy| = 10;   sum_y delta_xy = u_(pi x) := (N1)_(pi x).
 K4 (coordinate balance) sum_y delta_xy r_y = (NR)_(pi x) = 0.
 K5 (star transport) if c_(pi x,y) in E, s(pi x, y) = 1, and (c_xy in E or c_(pi x, pi y) in E), then
    delta_xy = H_(pi x, y) (antistar). Proof: by K1 applied to table (pi x, y), its beta is
    |c_xy| + |c_(pi x, pi y)| >= 1, and s.4 forbids a star edge with beta >= 1.
 K6 (transport of (C2)) N = D delta turns (C2) into delta D delta = delta + 12 D - DH and delta R = 0. This is (C2).
 K7 (census gluing) all tables of row x use the same census (1 d, 10 E split p_x/m_x, 30 n).
Status of the laws as joint constraints:
 - K0, K1, K2, K7 are definitions of the gluing: they constrain nothing by themselves.
 - K3 lines 1-2 are (C2) at (x, pi x) together with N_(x,pi x) = 0, i.e. the entrywise coupling. K3 lines 3-4,
   K4 and K6 are (C2)/NR = 0 transported by the permutation D: valid for ANY fixed-point-free involution, so
   they are N-layer facts.
 - K5 is the only law that ties a hidden coordinate to Q-visible data of OTHER tables by a constraint that neither
   layer imposes alone. It is Theorem S(a) ("apex edges are not star") read on the hidden coordinates.
Answer to the gluing question at this level: individually feasible tables leave delta free (s.7(d)); gluing
identifies delta with endpoint data (K1); the only constraint the gluing adds beyond the two layers is K5.
Everything else is the two layers separately.

## 9. Universal versus m = 7  [PROVED HERE]
 Universal (any m; BvLS satisfies them): s.2 table, s.3 equations, s.4 table, s.5 views and maps, s.6 kernel,
 compatibility and the beta verdict, s.7(a)-(c), K0-K7 with the constants 10 -> 2m - 4, 12 -> 2m - 2.
 m = 7 numbers: the census (1, 10, 30), the example of s.7(d) (row sums 29, 1, 5, 5).
 m = 7 specific collapses (NOT to be tested on BvLS):
   - the block-weight coincidence 2(2m-4) = C(m,2) - 1 (#w0 = #w2 per square);
   - G0(iii): 2(2m-4) = (m-2)(m-3); every pair of disjoint type-2 cells is a permutation block, which creates
     beta = 2 pairs and hence tables in which BOTH hidden coordinates are nonzero.
 BvLS remark: in BvLS every orbit is type 2, so f_x(k) = 0 on supp x; C_k has no B-edges, star and antistar
 edges with s = 1 do not exist there, and K5 is vacuous. BvLS cannot test anything built on K5.

## 10. Round 2 objects (built from delta, K5 and the gluing; distinction test first)
Distinction test D: (i) the separate Q layer and the separate N layer each permit the quantity to vary (shown at
the level of individually feasible pair tables); (ii) joint realization constrains it. Failing D => killed before
screening.
Notation: C_k^B = the B-edges among the 12 orbits containing k. By (P) an orbit x has exactly two C_k^B edges
if k in supp x minus supp pi x and none otherwise, so C_k^B is a disjoint union of cycles; by Theorem S(b)
(from NR = 0) every cycle alternates star/antistar, so it has even length and two alternating classes.
Apex edge := a B-edge e = (u,v) with beta_e >= 1, i.e. v adjacent to pi u or u adjacent to pi v.

R2-Om1  Apex edges of a C_k^B cycle lie in ONE alternating class   (unsigned shadow of K5 along cycles)
  Statement (U**): for every k and every cycle L of C_k^B, the apex edges of L are contained in one alternating
  class of L (namely the antistar class).
  Proof: apex edges have beta >= 1, hence are antistar (s.4 / K5); the antistar edges of L form one class.
  D(i): Q layer: an s = 1 edge with beta = 1 is table-feasible ((EQ): X^Q_11 = 0, 0 + 2 = 4 - 1 - 1), on either
        class; nothing in a single Q table refers to the class. N layer: does not see beta.
  D(ii): jointly forbidden: apex edges in both classes. Smallest instance: the two C_k^B edges at one vertex x
        (k in supp x minus supp pi x) are both apex edges. Each of the two tables is Q-feasible, but NR = 0 makes
        one of them star and a star edge has beta = 0. Longer instance (genuinely global): a 6-cycle with apex
        edges e1 in class I and e4 in class II (no common vertex): every vertex condition holds, (U**) fails.
  PASSES D.
R2-Om2  Phase forcing: a C_k^B cycle containing an apex edge has its star class, hence all its signs, fixed by
  unsigned data (signs N_e = -x_k y_k on the star class, +x_k y_k on the other).
  D: N layer permits both phases (Theorem S(b): one free phase bit per cycle); Q layer does not see signs; jointly
  forced. PASSES D.
R2-Om3  Hidden product at beta = 2 tables: delta_xy delta_yx = N_(pi x,y) N_(x,pi y) (the matching-rectangle sign).
  D(i) yes. D(ii): no joint constraint found (the four tables of the block see only |delta|; s.6(e) is the only
  joint single-table constraint and does not apply: the rectangle edges have beta = 0). KILLED before screening.
R2-Om4  K5 itself (apex edges are not star), as a local law.  D passes, but it is Theorem S(a) (known).
  KILLED at screening (rediscovery, duplication class B).
R2-Om5  Row aggregates of delta (K3).  D(ii) fails: line 1 is (C2) at (x, pi x) plus the entrywise coupling
  N_(x, pi x) = 0; the other lines hold for every involution in the N layer. KILLED before screening.

## 11. Screening of the two objects that passed D
R2-Om2 (phase forcing). First identity: holonomy prod N = (-1)^(L/2) on every C_k^B cycle (Theorem S(b), known).
  Usefulness: it only removes sign choices (stop condition "only proves uniqueness"; failure memory row 5).
  KILLED.
R2-Om1 (U**).
  First exact identities (m = 7; m-uniform with 84 -> 2m(m-1)):
   - sum_k |E(C_k^B)| = sum_x (2 - t_x) = 84 - tau  (a sibling B-edge counts in two C_k);
   - star incidences = antistar incidences = (84 - tau)/2 = 42 - n1 - 2 n2 (each cycle alternates);
   - total apex edges = 2 sum_S (2 - t_S) = 84 - tau (an edge is never an apex edge twice: beta <= 1 on B-edges);
   - every s = 1 apex edge is antistar, every sibling B-edge is antistar at exactly one of its two coordinates,
     siblings are never apex edges (beta = 0 for s = 2). Hence
        (CNT)  #(apex edges with s = 1) + #(sibling B-edges) <= 42 - n1 - 2 n2,
     i.e. at least half of all apex edges join disjoint cells.
  Usefulness: NOT-EX direction only. It is a necessary condition on the unsigned pair (B, D) for a signing to
   exist. It bites if the Q layer forces apex edges onto both classes of some C_k^B cycle, or forces (CNT) to fail.
   EX direction: pruning only.
  Automaticity: not implied by any single Q table nor by the N layer (test D). Whether the FULL Q system implies it:
   OPEN. It is not a trace or spectral statement: it needs the cycle classes (NR = 0) and beta (D).
  Local counterexamples: the one-vertex and 6-cycle configurations of s.10 (Q-table feasible, jointly forbidden).
  Known? Its ingredients are Theorem S(a) (category (ii)) and S(b) (= note 149 s.2). The combination (U**) and
   (CNT) are not stated in my notes; the repository has not been checked (duplication check is due only after a
   theorem is derived).
  Verdict: SURVIVES SCREENING. Not selected for pre-registration: its usefulness test has not been run.

## 12. Stopping point of this step
Only R2-Om1 survives. Under the protocol nothing is pre-registered until it passes a usefulness test.
The usefulness test it needs (bounded, no search): from the Q layer alone ((Deg), (P), (Q), m = 7 counts), derive
the best lower bound for #(s = 1 apex edges) + #(sibling B-edges) in terms of (n0, n1, n2). If that bound exceeds
42 - n1 - 2 n2 for some class not already excluded, (CNT) excludes that class. If the bound never exceeds it,
the count form of (U**) has no leverage and only the cycle form remains to be tested.

## 13. Final verdict on R2-Om1 (usefulness test, R2_OMEGA1_USEFULNESS.md)
Stage A: (CNT) excludes nothing (best Q-layer bound L >= 0). Stage B: the Q stage does not force Om1 locally
(verified 4-centre Q configuration, checks c13/c14). Duplication: Om1 is c2_experimental note 39, Lemmas
39.1(a)-39.2 (apex edges of R_i are pi_i edges), with notebook Lemmas 2-3. Verdict: rediscovered (B); joint
character confirmed; no class excluded; CLOSED. Round 2 has no surviving object.
