# Joint signed/unsigned system — checkpoint 1 (2026-09-30)

Hypotheses throughout: (N, D) feasible (N in S, D in L_N), T4 as working lemma (D = matching pi,
B_(x,pi x) = 0). F0 not used. No type-2 assumption: every statement holds when Sigma = empty.
Notation: B = |N|, F = [N = -1], x_k = k-coordinate of the positive representative of orbit x,
s(x,y) = |supp x cap supp y|, beta_xy = B_(x,pi y) + B_(pi x,y) (for B-edges beta <= 1, from (Q)),
C_k = the multigraph on the 12 orbits containing k whose edges are the B-edges between them plus a
double edge x = pi x when k in supp x cap supp pi x. t(x) = s(x, pi x); n_t = number of squares of
type t; n_1^a / n_1^d = type-1 squares whose positive representatives agree / disagree at the common
coordinate.

Mechanism chosen: the LINE DECOMPOSITION of the joint system. Every edge of the 99-graph lies on
exactly one triangle ("line", lambda = 1); projecting the lines through the 84 exterior vertices to
the 42 orbits sorts the B-edges into three kinds, and the signs of N on two of the kinds are forced
by root coordinates. This is the part of the joint system that the unsigned Q-stage cannot see.

## Theorem S (PROVED HERE)

(a) Line trichotomy. Each B-edge (x,y) is exactly one of:
    STAR   : its lifts lie on a line through an inner vertex; then s >= 1 and beta = 0;
    APEX   : beta = 1; its lifts lie on a line containing an edge of a sigma-square;
    E*     : beta = 0, s <= 1, not star; its lifts lie on an exterior line whose three orbits are
             pairwise B-adjacent with N-product -1 ("negative B-triangle").
    The negative B-triangles partition E*, and their number is T_- = 28 + n_1 + 2 n_2.
(b) Star-sign rule. A B-edge with k in supp x cap supp y is star at k iff N_xy = -x_k y_k (antistar
    iff N_xy = +x_k y_k). At each orbit x with k in supp x minus supp pi x the two C_k-edges are one
    star and one antistar. Hence: every cycle of C_k made of B-edges alternates star/antistar, has
    even length L, and has holonomy prod N = (-1)^(L/2); the star/antistar labelling of C_k is fixed
    by the unsigned data up to one phase bit per cycle.
(c) Apex concordance. A type-0 square has exactly two apex orbits z (z adjacent to both orbits of the
    square), one with N_(zx) = N_(z,pi x) and one with N_(zx) = -N_(z,pi x). A type-1 square with common
    coordinate k has one apex, with N_(zx) = N_(z,pi x) iff x_k != (pi x)_k. The two apexes of a type-0
    square are not Q-adjacent.
(d) Global sign counts. e_F := #negative edges is even and 94 <= e_F <= 112;
    #{negative B-edges with s = 1} = n_1 (mod 2); #{negative apex edges} = n_0 + n_1^a (mod 2).
(e) Lemma CM (cell-mates). Let c = {i,j} be a cell whose orbits x, kappa x are neither B-adjacent nor
    pi-partners. Then x and kappa x are never opposite vertices of a 4-cycle of C_i or of C_j; and if
    they are at distance 2 in C_i or in C_j, then beta_(x,kappa x) = 0.

Proofs.
(a) The H-edge between the positive lift x and l = -N_xy y lies on exactly one line (lambda = 1).
 If its third vertex is inner, the edge joins two roots agreeing at a coordinate: star. If the third
 vertex is +-pi x (or +-pi y), that vertex is adjacent to a lift of y (of x), so B_(pi x,y) = 1 (resp.
 B_(x,pi y) = 1): beta >= 1. Conversely, if B_(x,pi y) = 1, the lift of pi y adjacent to x is also
 adjacent to l, because every lift of y is adjacent to both lifts of pi y; so the line of the edge x-l is
 that square line. (For B-edges beta <= 1 by (Q); star edges have beta = 0 by (E+-).) Otherwise the third vertex
 is a lift of a third orbit z B-adjacent to x and y, and lifting forces N_xy N_yz N_zx = -1. The three
 cases exclude each other because the line is unique. An in-cell edge (s = 2) is star at one of its
 coordinates, so E* edges have s <= 1. For T_-: the 84 roots lie on 7 lines each, 2 through inner
 vertices, so there are 140 exterior lines; the non-star square edges (4 - 2t per square, 84 - 2(n_1+2n_2)
 in all) each lie on one exterior line and no line contains two of them; each negative B-triangle lifts to
 exactly two exterior lines. Hence 140 = 2 T_- + 84 - 2 n_1 - 4 n_2.
(b) The lift of y adjacent to x is -N_xy y; it agrees with x at k iff -N_xy y_k = x_k. By the profile
 (HC = 2J - C - CW) each root has exactly one neighbour agreeing and one disagreeing with it at each
 coordinate of its support; when k is not in supp pi x both are B-lifts. Alternation gives even L; the
 product of the star signs sigma = -N x_k y_k around a cycle is (-1)^(L/2) and equals prod N because every
 vertex occurs twice in prod x_k y_k.
(c) (E+-) at (x, pi x) give Y = 1 - Gam, Z = 1 - Del (common B-neighbours of x and pi x that are
 concordant / discordant). Type 0: Gam = Del = 0. Type 1: (Gam, Del) = (1,0) if the positive
 representatives agree at k, (0,1) otherwise. Non-adjacency of the apexes z1, z2 of a type-0 square
 {x, y}: their lifts adjacent to x are paired with y and with -y in the local matching at x (a perfect
 matching, lambda = 1), so they are not adjacent to each other, and at y the lifts are paired with x and
 -x, so l1 is not adjacent to -l2; they are not pi-partners since pi-partners have all four lifts adjacent.
(d) Parity: from diag and row sums of N^2 = N + 12I - RR^T one gets sum phi^2 = 19 e_F - 910 (phi = negative
 degree); sum phi^2 = sum phi = 2e_F (mod 2) forces e_F even. Range: 1^T N 1 = 420 - 4 e_F lies in
 [-3|1_V|^2, 4|1_V|^2] with |1_V|^2 = 42 - |R^T 1|^2/12 = 35/3. Overlap parity: multiply (b) over all
 cycles of all C_k; in-cell edges occur twice, and sum_k L/2 = (E_1 + 2E_2)/2 = 42 - n_1 - 2 n_2 by the
 per-orbit overlap budget sum_y s(x,y) B_xy = 4 - 2t(x). Apex parity: product of (c) over all squares.
(e) If x - w - kappa x is a path in C_i then N_(xw) N_(w,kappa x) = -x_i (kappa x)_i by (b) (the two edges
 at w have opposite star signs). x_i (kappa x)_i = +1 for the smaller coordinate of the cell and -1 for
 the larger. So C_i-paths are discordant and C_j-paths concordant (i < j). (E+-) at (x, kappa x) with
 B = D = 0, Gam = Del = 1 give Y = Z = 1 - beta. Two paths (opposite vertices of a 4-cycle) would need 2.

## What this says, and does not say

- Candidate class restricted. (e) excludes every unsigned configuration (B, D) — including all with
  Sigma = empty — in which some non-adjacent, non-pi cell-mates are opposite on a 4-cycle of some C_k,
  or are at distance 2 in some C_k while x ~ pi(kappa x) or kappa x ~ pi(x). (b) excludes every (B, D)
  with an odd cycle in some C_k. The unsigned pair and profile equations, evaluated on the orbits
  involved, do not exclude either configuration (e.g. a C_k-triangle only forces beta = 0 and
  (B^2) = 2 on its edges; cell-mates with two common neighbours containing i only need beta = 0), so
  these exclusions come from the common F. Whether the global Q-stage excludes them anyway is not
  known. (d) restricts sign
  patterns (e_F in {94, 96, ..., 112}).
- Empty type-2 support: every statement above is regime-independent and applies there.
- Global bookkeeping closes. Multiplying (a)-(d) over all B-edges (prod N = (-1)^(e_F), split into
  E*, star and apex parts) gives only n_0 + n_1 + n_2 = 21 (checked by hand; FAILED_ATTEMPTS F5). So
  the line decomposition alone yields no parity obstruction; an obstruction must use the mu = 2
  counts of pairs that are not on a common line or C_k path.
- Why the note-17/18 cocycle mechanism cannot reach Sigma = empty (PROVED HERE). Squares have coordinate
  supports of size 2, 3, 4 for types 2, 1, 0. A "rigid" block (each orbit of one square has exactly one
  neighbour in the other) needs disjoint supports, and a triangle of such blocks needs three pairwise
  disjoint supports, impossible when all sizes are >= 3 (3+3+3 > 7). With Sigma = empty the complex
  carrying the cocycle has no 2-cells, so H^1 gives nothing.
- Tested: all counts of (a) and E*-partition verified on the m = 11 graph (work/checks/c07; there all
  squares are type 2, so (b),(c),(e) are vacuous and untested). No m = 7 object exists to test on.

## Remaining implication

For not-EX in the grid-free core one still needs: no unsigned configuration (B, D) with Sigma = empty,
even C_k cycles and property (e) admits a sign pattern satisfying the mu-counts (E+-) on the pairs that
are neither lines nor C_k 2-paths (distance-2 pairs across different coordinates and cross pairs of
the E* triangle structure). For EX one needs an explicit pair. Neither follows from this checkpoint.
