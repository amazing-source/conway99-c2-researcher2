# One-candidate obligation: rigidity of type-1 squares

Setting: ONE arbitrary hypothetical feasible triple (B, D, P) — equivalently a feasible (N, D) —
with the checked bounded-residue lemma (TERNARY_VERIFICATION.md) and T4 as working lemma.
No second signing, no symmetry, no fractional matching, no type-2 cell assumed.

## Pre-registration (written before development)

Notation. A type-1 square S = {x, y}, y = pi x, supp x = {a,c}, supp y = {b,c} (common coordinate c),
U = {a,b,c}, W = [7] \ U (4 coordinates, 6 cells, 12 "W-orbits"). m(w,S) = number of B-neighbours of
w in S. The apex z = the unique common B-neighbour of x and y (it exists: |B(x) cap B(y)| = 2 - t = 1).

CLAIM T1. In every feasible triple, every type-1 square S satisfies
 (i) the apex z lies in a cell {a,w} or {b,w} with w in W, and
 (ii) every W-orbit w has m(w,S) = 1 (the 12 W-orbits are partitioned between x and y).
This is the analogue, for type-1 squares, of the partition B(c^0) + B(c^1) = Disj(c) of a type-2 cell.

What it would restrict: every candidate containing a type-1 square violating (i) or (ii). This
includes grid-free candidates (type-1 squares exist in every branch not excluded otherwise).

Implication to EX: NOT established. If true, type-1 squares acquire labels on their W-orbits like
type-2 cells. When two disjoint type-2 cells d, e partition W_S (branches with Sigma != empty, explicit),
{S, d, e} is a new cocycle triangle for the note-17/18 machinery. In the grid-free core, no triangle of
pairwise disjoint rigid squares exists (3+3+3 > 7), so T1 gives no route to EX there.

What would falsify it: a complete candidate with a type-1 square violating (i) or (ii). None exists
to test. A local configuration satisfying only some equations would NOT falsify it (local is not
complete). So T1 can only be proved, or left open with a stated gap.

## Result 1 (PROVED HERE): the type-1 trichotomy

Every type-1 square is in exactly one of three states.
 (a0) z lies in a W-cell; exactly one W-orbit has m = 0, the others m = 1 except z (m = 2);
      no orbit of cell {a,b} is adjacent to S.
 (a1) z lies in a W-cell; every W-orbit has m >= 1 (m = 1 except z); exactly one orbit of {a,b}
      has m = 1, the other m = 0.
 (b)  z lies in {a,w} or {b,w}; every W-orbit has m = 1 exactly; no orbit of {a,b} is adjacent to S.
      Moreover z is the antistar partner of x at a (resp. of y at b), so the C_a-cycle through x
      (resp. C_b through y) contains an apex edge and its phase is fixed.
CLAIM T1 is "state (b) always".

Proof. Profile (P): f_x(c) = 0, f_x(a) = f_x(b) = 2, f_x(w) = 4 (w in W). Let n_W, n_ab, n_aW, n_bW count
x's B-neighbours in W-cells, in {a,b}, in cells {a,w}, {b,w}. Coordinate counts give n_aW = n_bW =
2 - n_ab and n_W = 6 + n_ab; the same holds for y. Hence
  sum over W-orbits of m(w,S) = 12 + n_ab(x) + n_ab(y).
Since m <= 2 with equality only for z, the left side is at most 12 + [z in W]. So
n_ab(x) + n_ab(y) <= [z in W] <= 1, which also excludes z in {a,b} (that would give n_ab >= 2);
z avoids c (neither x nor y has a neighbour containing c). The three states are the three solutions.
In (b) the edge x-z lies on the square line (its unique triangle), hence is not a star edge; sharing
the coordinate a, the lifts disagree there: antistar.

Status against the literature read: c2_experimental note 07 gives the dichotomy "(x0,x3) in
{(2,0),(0,2)}" via the Wilbrink-Brouwer defect; Result 1 splits its second case by the apex
position and derives the exact partition in state (b) from profiles alone. Classification: newly
stated consequence; its effect (exclusion) is what CLAIM T1 would add.

====================================================================================================
## OUTCOME (written after development; the pre-registration above is unchanged)

Verdict on CLAIM T1: its conclusion is IMPOSSIBLE for every type-1 square. State (b) never occurs
(Theorem A). So T1 holds in a feasible triple only when that triple has no type-1 square at all.
The mechanism "type-1 squares carry a type-2-like W-partition" is refuted. What replaces it is a
rigidity statement of a different shape (Theorem A: a hole and a disjoint apex).

### Lemma X (one-vertex extension of the defect) — PROVED HERE, elementary

In an srg(n,k,lam,mu) let H be an induced subgraph with N vertices, and p a vertex outside H with
d = |N(p) cap H|. Double counting the paths p - q - h (q outside H, h in H) gives
    sum_{q in N(p) minus H} |N(q) cap H| = d*lam + (N-d)*mu - sum_{h in N(p) cap H} deg_H(h).
Hence at least (k-d) - [that number] neighbours of p have no neighbour in H, and
D(H + p) = D(H) - C(d-1,2) + sum_{q in N(p) minus H} (|N(q) cap H| - 1), where D is the
Wilbrink-Brouwer defect D(H) = sum_j C(j-1,2) x_j >= 0 (note 07's lemma).
For a sigma-pair p, -p (non-adjacent, both outside H, H sigma-invariant), with E_p the last sum:
D(H + p + (-p)) = D(H) - 2 C(d-1,2) + 2 E_p + |N(p) cap N(-p) minus H|, and N(p) cap N(-p) is the
pair of lifts of the pi-partner of p's orbit.
Orbit form of the check: for an exterior lift q outside H_S, |N(q) cap H_S| = |supp q cap supp S| + m(q, S).

### Theorem A — PROVED HERE (arithmetic checked in checks/c08_defect_squares.py, data/c08_defect_squares.txt)

Hypotheses: one feasible triple (equivalently an srg(99,14,1,2) with the one-fixed-point involution,
R1). T4 as working lemma (D = pi). No type-2 cell, symmetry or second signing is assumed.
Conclusion: every type-1 square S = {x, y} (supp x = {a,c}, supp y = {b,c}) is in state (a0):
 - the apex z lies in a cell inside W = [7] minus {a,b,c} (its two apex edges have disjoint supports);
 - neither x nor y has a B-neighbour in the cell {a,b};
 - exactly one W-orbit o (the HOLE of S) is adjacent to neither x nor y; the other ten W-orbits other
   than z are adjacent to exactly one of them.

Proof. H_S = {v0, a+-, b+-, c+-, x+-, y+-} is induced with 21 edges and D(H_S) = 2 (note 07; recomputed
in c08). Normalize x+ = e_a + e_c, y+ = e_b + e_c (switching). The square edges x+y+ and x-y- lie on the
inner lines through c+, c-; the other two lie on lines {x+, y-, zeta}, {x-, y+, -zeta}, zeta a lift of z.
State (b), z in {a,w}. zeta shares a with x+; they must disagree there, otherwise the edge x+ zeta lies
 on the line through a+ and on the line through y- (lambda = 1). So zeta = -e_a +- e_w and
 N(zeta) cap H_S = {a-, x+, y-}, with H_S-degrees 3, 4, 4. Lemma X: the 11 neighbours of zeta outside
 H_S have 3 + 8*2 - 11 = 8 neighbours in H_S altogether, and D(H_S + zeta) = 2 - 1 + (8 - 11) = -2 < 0.
 Impossible. The case z in {b,w} is the same with b and y- (c08 checks both).
State (a1), say x adjacent to v in {a,b}. The lift nu of v adjacent to x+ is +-e_a +- e_b; it is not
 adjacent to x-, y+ or y- (v is not adjacent to y and not a partner). N(nu) cap H_S = {a^s, b^t, x+}
 with degrees 3, 3, 4, so its 11 outside neighbours have 3 + 16 - 10 = 9 neighbours in H_S and
 D(H_S + nu) = 2 - 1 + (9 - 11) = -1 < 0. Impossible, for all four sign choices (c08).
By Result 1 the only remaining state is (a0). QED.

Orbit-level proof (shows that ONLY the unsigned equations (P), (Q) are used). For an orbit p list its
"entries": its 10 B-neighbours and its partner pi p twice (these are the orbits of the 12 exterior
neighbours of a lift of p). For an entry u put j(u) = |supp u cap {a,b,c}| + m(u,S), m = number of
B-neighbours of u in S. By (P), p has 4 - 2[k in supp p] entries containing k. By (Q),
sum over entries u other than x, y of m(u,S) = (B^2)_px + (B^2)_py + 2 m(pi p, S) - (terms for x, y).
 (b) p = z in {a,w}: entries containing a, b, c other than x, y: 1, 3, 2. (Q) at the B-edges (z,x)
     (s = 1, beta = 1) and (z,y) (s = 0, beta = 1): (B^2)_zx = 0, (B^2)_zy = 1, and B_(pi z,x) =
     B_(pi z,y) = 0. So the 10 entries other than x, y have sum of j equal to 6 + 1 = 7 < 10: at least
     three entries are W-orbits with m = 0. Result 1 says every W-orbit has m = 1 in state (b).
 (a1) p = v in {a,b}, v ~ x: entries other than x containing a, b, c: 1, 2, 3. (Q) at (v,x) (B-edge,
     s = 1): (B^2)_vx = 2 - 2B_(pi v,x); at (v,y) (non-edge, s = 1, B_(v,pi y) = 1): (B^2)_vy = 1 and
     B_(pi v,y) = 0. So the 11 entries other than x have sum of j equal to 6 + 3 = 9 < 11: at least two
     entries are W-orbits with m = 0, while in state (a1) every W-orbit has m >= 1.
So Theorem A is a consequence of the unsigned pair (B, D) alone: it holds for every complete unsigned
pair, the signed equations are not needed, and it is implicitly contained in any exact unsigned model
(e.g. my R8 pass and the repository's Q-stage). Its value is as an explicit structural statement, not
as a new exclusion of any solver-level branch.

### Consequences of (a0) — PROVED HERE (same method)

(1) Exact distribution relative to H_S: x0 = 2 (the lifts of the hole o), x1 = 60, x2 = 26, x_{>=3} = 0.
    j = 2 exactly for: both orbits of {a,b}; the siblings of x and y; the 4 orbits of {a,w}-cells and the
    4 orbits of {b,w}-cells that are adjacent to x or y (x's two C_a-neighbours, y's two second-kind
    neighbours at a, and symmetrically at b); the apex z.
(2) Second order. H_1 = H_S + {zeta, -zeta} has D(H_1) = 4 (c08). Counting its j-values gives exactly
    one of: (i) o is neither a B-neighbour nor the partner of z: then pi z has j = 1 and every
    B-neighbour of z other than x, y has j = 1; (ii) o is a B-neighbour of z: pi z has j = 1 and exactly
    one other B-neighbour of z has j = 2; (iii) o = pi z: exactly two B-neighbours of z other than x, y
    have j = 2.
    In case (i) the twelve exterior neighbours of zeta are x+, y-, three lifts in {a,w}-cells not adjacent
    to x, y, three such in {b,w}-cells, two in {c,w}-cells, and two in W-cells (adjacent to x- resp. y+).
(3) If a type-2 cell d lies inside W (only in branches with Sigma nonempty), then by Lemma G0 the pair
    (m(d0), m(d1)) is (1,1) or (2,0); the latter means z in d and o = pi z (case (iii)).

### Type-0 squares, first order — PROVED HERE (same method; recorded for the next step)

S = {x, y}, supp x = {a,b}, supp y = {c,d}. D(H_S) = 8. Write e_x (e_y) for the number of B-neighbours
of x (of y) in the ten orbits of cells inside {a,b,c,d}, and a_in, a_kw, a_W for the number of apexes in
cells inside {a,b,c,d} (necessarily cells meeting both {a,b} and {c,d}), in cells {k,w}, and in W-cells.
Then the number of holes (W-orbits adjacent to neither x nor y) is h0 = 2 + a_W - e_x - e_y >= 0, and
Lemma X at a cross apex (four H_S-neighbours of degree 4, 4, 3, 3) forces at least two hole lifts among
its neighbours. Consequently either a_in = 0, or the configuration is rigid:
    C1: a_in = a_W = 1, e_x = e_y = 1, exactly one hole o, and o = pi(z_in).
The defect identity itself is automatically satisfied in all other cases (a_in = 0); no further
restriction at first order.
Second order (two-vertex formula): adding the lifts of one apex to H_S gives defect 18 (apex in a
W-cell), 10 (apex in a {k,w}-cell) and 0 (cross apex, C1). So C1 is a perfect configuration (every
outside vertex has one or two neighbours in H_S + {+-zeta}); the other type-0 configurations keep slack.
For type 1 in state (a0) the corresponding numbers are 4 (apex), 18 (hole), 8 ({a,b}-orbit), 6
(siblings, and the {a,w}/{b,w} orbits adjacent to S): slack remains beyond the facts listed in (2).

### Exact status of the next implication (not proved)

 - N1 "no type-1 square exists" would reduce the grid-free core to the all-type-0 family (B).
   The defect method is tight for type 1 only at first order (the hole uses the whole defect 2). At
   second order every addition listed above has slack, so the method at this radius cannot decide
   (a0). Missing: a relation that involves the hole o or the apex square {z, pi z} beyond these counts.
 - For type-0 squares with no cross apex (a_in = 0) the method gives nothing beyond h0 = 2 + a_W -
   e_x - e_y. These are the generic squares of the grid-free core, so this mechanism does not by itself
   reach Sigma = empty.

### Where this leaves the one-candidate obligation

 - Restricted candidates: every candidate with n1 >= 1, in every branch (including Sigma = empty and the
   Sigma-classes left open in c2_experimental). Nothing is excluded outright.
 - Implication to EX: none by itself. It turns the type-1 squares into rigid local objects (disjoint apex,
   one hole, empty {a,b}-cell), which is the input the next claim needs.
 - Literature check (only the parts read earlier: note 07, whole file, 24 lines; note 19 s.7, lines
   315-347): note 07 leaves (x0,x3) in {(2,0),(0,2)} undecided and note 19 s.7 reports local probes
   without conclusion. Theorem A decides the dichotomy: (x0,x3) = (2,0) always. Not found in the parts
   read; no claim beyond that.
