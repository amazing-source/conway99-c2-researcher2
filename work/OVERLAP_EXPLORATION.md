# Overlapping valid structures — exploration log (started 2026-10-01, after Round 2)

Starting point: Theorem C (THEOREM_C.md) and the failure ledger (FAILURE_MEMORY.md). Closed basins not revisited: pair
tables, single coordinate cycles R_k, Om1, aggregate counts, compressions, spectra, lattices.
Status labels: DERIVED HERE (hand derivation written below), CHECKED (exact computation named), OPEN, KILLED.

## 1. Where does the orbit quotient force a structure to overlap itself?  [DERIVED HERE]
Lift a closed walk x1 - x2 - ... - xL - x1 of the orbit graph (consecutive orbits B-adjacent, or a matching pair
traversed by its a-edge or b-edge). Starting at x1+, a B-step x -> y goes to y^(-N_xy (current sign)), a matching
step goes to either lift. For a B-cycle the walk returns to x1^((-1)^L prod N). Hence:
 - (-1)^L prod N = +1: the cycle lifts to two disjoint copies (a cycle and its sigma-image): the two copies are
   independent and use the same orbit states only "in parallel".
 - (-1)^L prod N = -1: the lift is ONE sigma-invariant cycle of length 2L. The lifted structure and its
   sigma-image are the same object: the quotient forces it to overlap itself, and every orbit state on the cycle is
   used twice by one structure.
Smallest twisted cycles: L = 2, a matching pair traversed by its a-edge and its b-edge (lift: the D-square);
L = 3, a POSITIVE B-triangle (prod N = +1; lift: a sigma-invariant hexagon); L = 4, an unbalanced B-4-cycle (lift:
an octagon). Negative triangles are untwisted (they lift to two lines, the E* lines).
D-squares are the known twisted structure (apex table, Theorem S(c)). The positive triangle is the smallest new one.

## 2. Edge census by the two channels  [DERIVED HERE from (E+),(E-); m-uniform]
For a B-edge {x,y} the lifted pair (x+, y^(-N)) is adjacent (channel count lambda = 1) and (x+, y^(N)) is not
(channel count mu = 2). In each channel the contributions are: E.E paths (in the adjacent channel exactly those
closing a NEGATIVE triangle, in the other channel exactly those closing a POSITIVE triangle), d-paths (beta, in both
channels), inner vertices (a shared coordinate, on the side fixed by the signs). With neg = #negative triangles and
pos = #positive triangles on the edge:
  (s, beta) and kind       neg  pos   non-adjacent channel completed by
  (0,0) E*                  1    2    two positive triangles
  (0,1) apex                0    1    one positive triangle + one d-path (lift of pi x or pi y)
  (1,0) star                0    2    two positive triangles
  (1,0) antistar (E*)       1    1    one positive triangle + the inner vertex of the shared coordinate
  (1,1) antistar apex       0    0    one d-path + one inner vertex
  (2,0) sibling             0    1    one positive triangle + one inner vertex
(Rows (1,0) split by the star/antistar sign. Check: (B^2) = neg + pos agrees with 3 - s - 2 beta in every row.)

## 3. New object: the positive-triangle complex P  [DERIVED HERE; m-uniform]
P := the 2-complex on the orbits whose faces are the positive B-triangles (each = one sigma-invariant hexagon of the
lift). From s.2 every edge lies in at most 2 faces (pos <= 2, because the non-adjacent channel has exactly mu = 2
middle objects). So P is a pseudo-surface with boundary:
  interior edges (pos = 2): (0,0) E* edges and star edges;
  boundary edges (pos = 1): (0,1) apex edges, (1,0) antistar edges, sibling edges;
  edges not in P (pos = 0): (1,1) antistar apex edges.
The link of an orbit x in P is the graph on B(x) with y - y' iff {x,y,y'} is a positive triangle; its degrees are
pos(x,y) <= 2, so each link is a disjoint union of paths and cycles; path ends are exactly the boundary edges at x.
Hence the boundary of P is a union of closed walks.
Every boundary edge is "capped" in the lift by its non-triangle middle object: a lift of a matching partner
(apex edges; the cap is the D-square) or an inner vertex (antistar and sibling edges).
Two pieces that overlap: two positive triangles on an interior edge share the quadrangle formed by the two
non-adjacent lifts; a positive triangle and a D-square share a long diagonal of the hexagon ({x+, x-} has common
neighbours exactly the lifts of pi x).

## 4. Microscope c15 on BvLS (m = 11): the shape of P  [CHECKED, checks/c15_positive_complex_bvls.py]
Exact question and bounds in the script. Results: 110 orbits, 990 B-edges, 660 positive and 330 negative triangles;
every edge has (neg, pos) = (1, 2) (all edges there are (0,0)); every vertex link is SIX disjoint 3-cycles; P is
orientable; chi(P) = -220.
Reading: a link 3-cycle (y1 y2 y3) at x means the four triangles of {x, y1, y2, y3} are all positive (the sign of
{y1,y2,y3} is the product of the three face signs). So in BvLS, P is a union of 165 POSITIVE K4s that partition
the 990 edges (and the negative triangles, i.e. the lines, partition them a second time).
Lift of one positive K4: 8 vertices, 12 edges, 4 hexagons, chi = 0: a sigma-invariant hexagonal torus (branched
double cover of the tetrahedron's sphere at its 4 face centres; Riemann-Hurwitz 2*2 - 4 = 0).
Status: a property of BvLS. NOT a law: from (E+-) alone the two positive triangles {x,y,z1}, {x,y,z2} on an interior
edge close to a K4 iff z1 ~ z2, and the equations at the pairs involved allow z1 not adjacent to z2 (then (z1,z2) is a
non-edge whose channel has the two E.E middles x, y). Recorded as a hypothesis generator only.

## 5. The overlap of N(x+) and N(x-): the bridge graph G_x  [DERIVED HERE; m-uniform]
N(x+) and N(x-) = sigma N(x+) are two valid neighbourhoods built from the same row-x states; they overlap exactly in
{pi x+, pi x-} (notebook Lemma 1). Put U = N(x+) minus {pi x+-}, W = N(x-) minus {pi x+-} = sigma U (each = 2m - 2
vertices: the B-lifts and the two inner vertices of x). Let G_x be the bipartite graph of the 99-graph edges between U
and W.
(a) Degrees. u in U is not adjacent to x- (else u in N(x+) cap N(x-)), so mu(u, x-) = 2: u has exactly two neighbours
    in N(x-). Hence deg_G(u) = 2 - a(u), a(u) = #(lifts of pi x adjacent to u) in {0,1}. a(u) = 1 exactly for the
    lifts of the apexes of S(x) (2 - t_x of them) and for the inner vertices of the coordinates x shares with pi x
    (t_x of them). So U has exactly two vertices of degree 1, W likewise, all others have degree 2:
    G_x = exactly TWO PATHS + cycles, for every orbit x of every type.
(b) sigma acts on G_x (it swaps U and W). Its fixed edges are the edges u - sigma u: only the inner edges
    (k^(x_k), k^(-x_k)), k in supp x. Exactly two fixed edges.
(c) A sigma-invariant path is reversed by sigma and contains exactly one fixed edge (its middle); a sigma-invariant
    cycle is either rotated by half (no fixed edge) or reflected (exactly two fixed edges, no fixed vertex exists).
    Hence exactly one of:
      PHASE alpha: both paths sigma-invariant, one coordinate loop in the middle of each;
      PHASE beta : the two paths are swapped by sigma, and both loops lie on one reflected cycle.
(d) Type 2: each loop is a whole path (its inner vertices touch pi x): alpha. Type 1: the shared coordinate's loop is
    a whole path, so the other path is invariant too: alpha. Type 0 with an apex sharing a coordinate k with x: the
    slot path from that apex enters the inner slot k at once (s = 1 apex edges carry only an antistar bridge): alpha.
(e) Quotient by sigma (12 "slots" of x: its 10 B-neighbours and 2 coordinates). Slot edges are positive triangles
    {x,y,y'}, D-bridges {y, pi y} (x an apex of S(y)), antistar bridges y - k, and the loops. For a type-0 orbit the
    four path ends (concordant apex z_c, discordant apex z_d, coordinates i, j) are paired by two slot paths:
    (z_c z_d | i j) = phase beta, or (z_c i | z_d j), (z_c j | z_d i) = phase alpha. This pairing type is a canonical
    ternary invariant of each type-0 orbit, produced only by the compatibility of the twelve mu-conditions at the
    sigma-pair (x+, x-); no single pair table contains it.

## 6. Check c16 on BvLS: the bridge-graph structure  [CHECKED, checks/c16_bridge_graph_bvls.py]
BvLS rebuilt as a 243-vertex graph from (N, D) and the D11 roots (verified srg(243,22,1,2)). For all 110 orbits:
|U| = 20, two degree-1 vertices in U and two in W, exactly two paths, exactly two sigma-fixed edges, phase alpha
(all orbits there are type 2, where alpha is forced by s.5(d)). The m-uniform claims of s.5(a)-(c) hold there.

## 7. Two square-level consequences  [DERIVED HERE]
(a) Square necklace. For a type-0 square S = {x, pi x} with concordant apex z_c (lifts c1 ~ x+, pi x+; c2 = sigma c1)
    and discordant apex z_d (d1 ~ x+, pi x-; d2 = sigma d1): G_x and G_(pi x) meet exactly in these four vertices,
    which are the degree-1 vertices of both (N(x+-) cap N(pi x+-) = one apex lift each, lambda = 1; no common edge,
    since the apexes are not adjacent, Theorem S(c)). Their union is one or two sigma-invariant cycles through the
    four apex lifts, carrying 2[x in phase alpha] + 2[pi x in phase alpha] fixed edges. Case check: every
    combination of phases is consistent (two alpha: two reflected cycles; one alpha: one reflected cycle; two beta:
    two swapped cycles or one antipodal cycle). No law.
(b) Slot cycles. A cycle of length L in the slot graph lifts to two swapped L-cycles of G_x if L is even and to one
    antipodal 2L-cycle if L is odd (each slot step changes side). (BvLS: the link triangles are antipodal 6-cycles.)

## 8. Targeted duplication check (2026-10-01)
Read: conway99-involution/notes/MATH_C2_PROGRAMME.md s.1-3; c2_experimental notes 29 s.3, grep over notes 00-57.
 - sigma-invariant hexagons: KNOWN. Notebook s.3 counts sigma-fixed 6-cycles: 224 = 42 reflections through two
   block edges + 42 antipodal hexagons with an inner pair + 140 antipodal exterior hexagons ("forced: 20 exterior
   paths u-q-r-sigma u per u"), used for a Burnside parity that gives no information (impasse). Consistent with
   s.1: positive triangles (98 + n1 + 2 n2) + apex triples (42 - n1 - 2 n2) = 140.
 - Bridge graph G_x, its two-path structure, the coordinate loops as the only fixed edges, the phase alpha/beta, the
   pairing type of type-0 orbits, the square necklace, and the positive-triangle pseudo-surface P: NOT FOUND.
   Closest known object: note 29 s.3 (free-star problem at an inner vertex e_c), "Faces G_a = Phi(etoile de a): 10
   aretes, degres 1 en a, sigma a, mu a, tau sigma a, 2 ailleurs: deux chemins plus des cycles", with the suggestion
   to glue the faces into a pseudo-surface (never exploited). G_x is the analogue at an exterior sigma-pair; the
   phase invariant comes from sigma acting on G_x with the coordinate loops as its only fixed edges.

## 9. Status of this exploration
 - New representations (DERIVED, m-uniform parts CHECKED on BvLS): P (s.3), G_x with its phase and pairing type
   (s.5), the square necklace (s.7). They compress the twelve mu-conditions at a sigma-pair (and, for a square, the
   twenty-four of x and pi x) into one sigma-symmetric 2-regular structure.
 - Compatibility law: NONE found yet. Every local combination of phases checked in s.5 and s.7 is consistent.
 - Countermodel: BvLS (s.4) shows that "interior edges close into positive K4s" is a property of that graph, not a
   consequence of the equations used here.
 - Not done: a global relation among phases (it would have to come from how the G_x of different orbits share
   positive triangles and D-bridges).

## 10. Pairwise compatibility of pairing states on minimal overlaps  [DERIVED HERE]
Setting. Lambda_x = slot graph of x (sigma-quotient of G_x), loops omitted. Slots: the 10 B-neighbours of x and the
two coordinates i, j of x. Edge kinds (s.5(e)): positive triangles {x,y,y'} (B-slot to B-slot), D-bridges y - pi y
(x an apex of S(y)), antistar bridges y - k (y the antistar k-neighbour of x; each coordinate slot has exactly one).
Degrees: B-slot y has 2 - [y ~ pi x]; coordinate slots have 1. For type 0 the degree-1 slots are z_c, z_d, i, j and
Lambda_x = two paths + cycles; the state of x is the pairing of {z_c, z_d, i, j} by the two paths:
  beta = (z_c z_d | i j),  alpha_i = (z_c i | z_d j),  alpha_j = (z_c j | z_d i).
"Ordinary" type-0 orbit: neither apex of S(x) shares a coordinate with x (otherwise s.5(d) forces the state).
Two facts used throughout:
 (F1) No single edge of Lambda_x joins two degree-1 slots: z_c, z_d are not adjacent (Theorem S(c)), and a
      coordinate slot carries only its antistar bridge, to a B-slot that is not an apex (an apex edge with s = 1 has
      pos = 0 and its only Lambda_x edge goes to the coordinate: that is exactly the non-ordinary case).
 (F2) The state is a property of the connectivity of the whole of Lambda_x; an overlap that fixes finitely many edges
      and does not join two degree-1 slots by a fixed path leaves all three pairings completable: route the two
      paths through the free ordinary B-slots (positive-triangle edges), start each fixed end-edge on its path, and
      close the remaining B-slots into cycles; the edge-kind rules (D-bridges only between a D-pair, one antistar
      bridge per coordinate) are respected by using no further D-bridges.

(A) Overlap = one shared positive triangle {x, y, w}, x and y ordinary type 0.
    Data on the overlap: in Lambda_x the single edge y - w; in Lambda_y the single edge x - w (in Lambda_w the edge
    x - y). If an endpoint of the edge is an apex of the square (e.g. y ~ pi x, an apex edge (0,1)), the edge is the
    first edge of that apex's path; the other end is an ordinary B-slot (F1). Lambda_y additionally gets the D-bridge
    x - pi x in that case (y apex of S(x) means x, pi x in B(y)).
    By (F1)-(F2) each of the 3 states of x and each of the 3 states of y is completable, and the two completions
    share no edge beyond the overlap.  TABLE (A): all 9 combinations realizable on the overlap data.
(B) Overlap = a shared apex structure: z an apex of S(x) (z ~ x, z ~ pi x), x and z type 0.
    (B0) s(z,x) = 0, edge (0,1): Lambda_x: z is a path end, first edge z - w (w the unique positive triangle on
         {x,z}); Lambda_z: slot x has edges w - x and x - pi x (D-bridge). Neither fixes a path between two degree-1
         slots.  TABLE (B0): all 9 combinations realizable (x, z ordinary).
    (B1) s(z,x) = 1 at coordinate k, edge (1,1): census row (1,1) (pos = 0, non-adjacent middles = a d-path and the
         inner vertex k) gives in Lambda_x the path z - k: the state of x is FORCED (z paired with k). In Lambda_z,
         slot x has the antistar bridge to z's coordinate slot k and the D-bridge x - pi x, so z's k-path runs
         k - x - pi x - ...; z's state stays free.  TABLE (B1): 3 of 9 (state of x fixed, state of z any).
         The restriction is single-orbit forcing. It follows from existing results: census row (1,1) from (E+-),
         i.e. Theorem S(a), apex edges are not star (= note 39, Lemmas 39.1(a)-39.2), plus the definition of
         Lambda_x. It is not a pairwise compatibility law, and x is not ordinary.
(C) Overlap = the square itself, x and pi x both type 0 (they share both path ends z_c, z_d). Lift check (s.7(a)):
    every combination of states closes into a sigma-consistent necklace (two alpha: two reflected cycles, each
    through one loop of x and one of pi x, for any choice of the loops; one alpha: one reflected cycle; two beta:
    swapped or antipodal cycles). TABLE (C): all 9 realizable (for ordinary x, pi x).
(D) Overlap = a shared coordinate k (both orbits contain k): G_x and G_y share the fixed edge (k+, k-) and nothing
    forced beyond it. TABLE (D): all 9 realizable.
Lift refinement: beta splits into beta_even / beta_odd by the parity of the slot path z_c ~> z_d (s.7(a)); the
necklace check of (C) covers both, so the refinement adds no restriction.

VERDICT. On every minimal overlap of two bridge graphs (shared positive triangle; shared apex/D-bridge structure;
the square; a shared coordinate) all nine combinations of pairing states of ordinary type-0 orbits are realizable
using only the exact data on the overlap. The only restriction found is the forcing of a single non-ordinary orbit
(an apex sharing a coordinate), which follows from Theorem S(a) / note 39. No pairwise compatibility law.
The pairing states depend on the complete slot graphs, which these overlaps do not fix.
Per instruction this representation is STOPPED. (No complete neighbourhoods were built.)
