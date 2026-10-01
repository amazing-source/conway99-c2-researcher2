# Usefulness test of R2-Om1 (U**) — started 2026-10-01

Object (OBJECT_ROUND_2.md s.10-11): for every k and every cycle L of C_k^B, the apex edges of L lie in one
alternating class of L.  Count form (CNT): E11 + E20 <= 42 - n1 - 2 n2.
Q layer used below: (Deg) B1 = 10, D = fixed-point-free matching, (P) (BM)_xk = 4 - 2M_xk - 2M_(pi x,k),
(Q) (B^2)_xy + B_xy + s_xy + 2 beta_xy + 2 D_xy = 4 (x != y). No signed information, no Om1.
(The mod-2 relation B^2 + B = K (mod 2) is (Q) mod 2, so it is included.)

## Stage A — aggregate test  [PROVED HERE]
Edge classes. On a B-edge (Q) gives (B^2) = 3 - s - 2 beta, so beta <= 1, s = 2 forces beta = 0, and beta = 1
forces s <= 1. Hence every B-edge has (s, beta) in {(0,0), (0,1), (1,0), (1,1), (2,0)}; write E_s,beta for the
numbers. Then L := LHS of (CNT) = E11 + E20, and
   (CNT)  <=>  E11 + E20 <= (84 - tau)/2  <=>  E11 <= E10     (using A1 below),
i.e. among the B-edges whose cells share exactly one coordinate, at most half are apex edges.
Q-layer identities (all exact):
 A1  sum_e s_e = E10 + E11 + 2 E20 = 84 - tau        [(BK)_xx = sum_{k in supp x} f_x(k) = 4 - 2 t_x].
 A2  sum_e beta_e = E01 + E11 = 84 - tau            [sum_x (B^2)_(x,pi x) = sum_x (2 - t_x), twice].
 A3  sum_e (B^2)_e = 3E00 + E01 + 2E10 + E20 = 378 + 3 tau   (number of B-triangles 126 + tau);
     A3 follows from A1, A2 and E00 + ... + E20 = 210.
 A4  E11 = sum over (square S, apex z of S) of cov(z, S) := s(z, x) + s(z, pi x) in {0, 1, 2}.
 A5  per coordinate k, with O_k = the 12 orbits containing k and p_k = #squares whose two cells contain k:
     sum over pairs in O_k of beta = 24 - 4 p_k = 2|V_k|; this follows from (P) (it equals
     sum_{x in O_k} f_(pi x)(k)).
 A6  per square: (B^2)_(x, pi x) = 2 - t (number of apexes); (Q) fixes only this number.
Lower bound. All of A1-A6 hold with E11 = E20 = 0, E10 = E01 = 84 - tau, E00 = 42 + 2 tau for every
(n0, n1, n2), and in A5 all apex beta can sit on non-adjacent pairs (24 - 4p_k <= 54 + p_k). Locally nothing
forces s = 1 apex edges: at a square only the number of apexes is fixed (an apex may cover none of the square's
coordinates), and a cell's two orbits are never forced to be adjacent ((Q) allows both). Type-2 orbits contribute
neither (their neighbours avoid their cell, G0(i), and type-2 squares have no apex).
The strongest bound I can prove from the Q layer is therefore L >= 0, and (CNT) compared with
42 - n1 - 2 n2 >= 0 excludes nothing. In the classes left by my frozen classification (n2 <= 10, Lemma J)
the right-hand side is at least 21 - n2 >= 11, and I found no Q-layer mechanism forcing L >= 12.
VERDICT A: the aggregate inequality removes no type distribution and no class.

## Stage B — does the Q layer force Om1?  (logical implication Q => Om1)
Smallest violation: one orbit x with k in supp x minus supp pi x whose two C_k^B edges (x,w1), (x,w2) are both
apex edges (they are adjacent in the cycle, hence in different classes). Three cases: each w_i is an apex of
S(x) (alpha) or x is an apex of S(w_i) (beta). Facts for case (alpha,alpha), from (Q) alone:
 S(x) is type 0 with apexes exactly w1, w2; B(x) cap B(pi x) = {w1, w2};
 (x,w_i): s = 1, beta = 1, so (B^2) = 0 (B(x) cap B(w_i) empty) and pi w_i not in B(x);
 (pi x, w_i): beta = 1 forces pi w_i not in B(pi x), and (B^2) = 1 - s(pi x, w_i);
 (w1, w2): not adjacent (a common neighbour of x and w1 would exist), not a matching pair (their common
 neighbours x, pi x would force type 0, but they share k), beta = 0, (B^2) = 4 - s.
Microscope c13 (exact question): is there a partial Q-configuration with COMPLETE rows (B-neighbours and
matching partner) for the four centres x = (12,+), pi x = (34,+), w1 = (15,+), w2 = (16,+) (k = 1), such that
 (Deg) and (P) hold for every centre; (Q) holds exactly for every pair of centres; every pair (centre, other
 orbit) is locally consistent (known common neighbours and known beta-parts leave an admissible value); every
 other orbit stays within its (P) and degree bounds; and beta(x,w1) = beta(x,w2) = 1?
Bounds: one process, depth-first search with a 240 s cap, < 200 MB. Orbit swaps inside a cell are symmetries of
the Q layer (it sees cells only through s and M); they are used only to normalise the first row.
Result of c13 (21 s, first solution) and independent verification c14 (0 errors). Saved in
data/c13_config_alpha_alpha.json. Complete rows (B-neighbours; matching partner):
  x   = (12,+)  partner (34,+):  (15,+) (16,+) (27,+) (27,-) (37,+) (37,-) (45,+) (46,+) (56,+) (56,-)
  pi x= (34,+)  partner (12,+):  (15,+) (16,+) (26,+) (26,-) (35,+) (36,+) (47,+) (47,-) (57,+) (57,-)
  w1  = (15,+)  partner (67,+):  (12,+) (17,+) (23,+) (24,+) (25,+) (34,+) (35,-) (36,-) (46,-) (47,+)
  w2  = (16,+)  partner (67,-):  (12,+) (17,-) (23,-) (24,-) (25,-) (34,+) (34,-) (35,-) (45,-) (57,+)
Checked: (Deg) and (P) for the four centres; (Q) exactly for all six centre pairs
 ((x,pi x): 2 common = {w1,w2}; (x,w_i): 0 common, beta 1; (pi x,w_i): 1 common, beta 1; (w1,w2): 3 common,
 beta 0); every (centre, other orbit) pair locally consistent; every other orbit within its (P)/degree bounds.
The two C_1^B edges at x are (x,w1), (x,w2), both apex edges (w_i adjacent to pi x). They are consecutive edges of
the C_1^B cycle through x, so they lie in different alternating classes: Om1 fails here. In the joint system this
is impossible (NR = 0 makes one of them star, and a star edge has beta = 0).
CONCLUSION B (local): Q => Om1 has no proof that only uses the Q equations determined by these four rows.
Om1 carries genuinely joint information at this radius. A complete unsigned counterexample would need a complete
unsigned pair, and none is known; so "Q => Om1 globally" is not refuted, only shown not to be local.

## Complete unresolved classes
Om1 says nothing at type-2 orbits (G0(i): their neighbours avoid their cell, so they carry no s = 1 edges, and type-2
squares have no apex). It constrains only the local geometry of type-0/1 squares. Excluding a complete class would
need every completion of that class to put apex edges into both classes of some C_k^B cycle. I have no argument that
forces this for any class (Stage A shows no count forces it), so it excludes no complete currently unresolved
unsigned class. Not promoted.

## Targeted duplication check (repository read 2026-10-01: Desktop/conway99-involution/notes/MATH_C2_PROGRAMME.md
## s.0-1, s.11, s.14; Desktop/c2_experimental/notes 19 s.6-8, 20 (grep), 29 s.1-5, 39 s.1-2, grep hits in 22-38)
 - Notebook Lemma 3 (PROUVE): at block i the 12 orbits through i carry two perfect matchings, m_i (the neighbour
   containing (i,0): my star class) and pi_i (the neighbour containing (i,1) via sigma: my antistar class);
   R_i = m_i u pi_i is 2-regular, even alternating cycles plus digons, digons = D-pairs inside O_i; signed holonomy
   +1 on m_i, -1 on pi_i. This is my C_k structure and Theorem S(b) (already recorded as rediscovered).
 - Notebook Lemma 2 (PROUVE): an exterior triangle has pairwise disjoint labels; if u, w share an inner vertex c,
   the unique triangle of the edge uw is {c, u, w}. This contains "star edges have beta = 0".
 - c2_experimental note 39, Lemma 39.1(a) (Sigma = empty, disjoint square; proof by lambda = 1): no apex of a
   D-square contains an inner vertex of the square on the m side; Lemma 39.2: an apex meeting block i is pi_i(u),
   "l'arete R_i de U vers l'orbite de pi_i(u) est alors une arete d'apex".
   So apex edges of R_i are pi_i edges. Since pi_i is one alternating class of each R_i cycle, this IS Om1
   (cycle form), for the squares treated there. Lemma 39.1(a)'s proof is lambda = 1 and does not use
   Sigma = empty or disjointness for this point (my proof: s.4 star row of OBJECT_ROUND_2.md).
 - (CNT) is not written there; it is an immediate count of the same lemma (each R_i cycle has as many pi_i as m_i
   edges).
 - Not found in the repository: the statement that this lemma is NOT a consequence of the Q stage. That is what
   Stage B adds (c13/c14).

## FINAL VERDICT on R2-Om1
 - Content: REDISCOVERED (duplication class B): note 39 Lemmas 39.1(a)-39.2 with notebook Lemmas 2-3.
   (CNT): class D (an automatic count of the known lemma); Stage A: it excludes nothing.
 - Joint character: confirmed. The Q stage does not imply it locally (verified 4-centre Q configuration,
   c13/c14). Progress-metric item 5 (counterexample to a mechanism): "the Q stage forces the apex/pi lemma" is false
   at radius one around the violating orbit. Supporting fact only; it excludes nothing.
 - No complete unresolved class excluded. Not promoted. R2-Om1 is CLOSED.
