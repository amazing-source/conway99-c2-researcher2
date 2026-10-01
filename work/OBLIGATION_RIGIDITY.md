# Proof obligation: sign rigidity over a complete unsigned pair

## Statement (R)

For every complete unsigned pair (B, D) there is at most one sign pattern N with |N| = B such that
(N, D) is feasible.

Consequence for EX if (R) holds: with T4 (D is determined by N), a feasible pair is determined by its
unsigned layer (B, D). The signed layer then adds no freedom: EX holds iff some complete unsigned pair
admits a solution of the ternary signing problem of TERNARY_VERIFICATION.md s.3, and that solution
is unique. (R) excludes nothing by itself; it removes the sign layer as a source of choices.
Scope: arbitrary candidates, including empty type-2 support. No symmetry, subspace or special family
is assumed.

## Set-up (PROVED HERE)

Let N, N' be two feasible signings of the same B. Put X = {B-edges with N' = -N}, Y = N restricted to X,
K = N restricted to B \ X; so N = K + Y, N' = K - Y. Subtracting the two copies of (S):

    YR = 0,        KY + YK = Y.                                                  (D)

(R) is the statement that (D) with Y in {0,+-1}, supp Y = X subset B, forces X = empty.

## What is proved

R1 (cycle-union). For each k, X meets the edges of C_k in a union of whole C_k B-cycles.
 Both N and N' obey the star/antistar alternation (note 149 s.2 / TERNARY_VERIFICATION s.4); flipping
 exactly one of the two C_k-edges at an orbit would give two star or two antistar edges there.

R2 (zero-sum). For every orbit u, the lifts l_u(w) = -N_uw r_w of the flipped neighbours w in X(u) sum
 to 0 in Z^7 (row u of YR = 0), and so do the kept ones. These are roots of distinct sigma-orbits, so no
 two cancel and none is 0. Hence |X(u)| is 0, 10, or between 3 and 7.

R3 (every flipped edge lies on a triangle with exactly two flipped edges). Entry (u,v) of (D) for
 uv in X reads: sum over common neighbours w with exactly one of uw, wv in X of N_uw N_wv equals
 N_uv != 0. In particular an edge with no common neighbour is never flipped: this applies to every
 apex edge with s = 1 ((B^2)_uv = 4 - 1 - 1 - 2 = 0). By R1 the C_k-cycle containing such an edge is
 never flipped either: its phase is fixed by (B, D).

R4 (flips confined to overlap edges). Suppose X contains no disjoint-support edge. A type-2 orbit lies
 on no B-cycle of any C_k, a type-1 orbit on exactly one (its C_k at the common coordinate is the
 pi-pair), a type-0 orbit on exactly two. By R1-R2, if a cycle through u is flipped then |X(u)| >= 3,
 so u is of type 0 and its second cycle is flipped too (in the in-cell case the shared edge forces
 this). Therefore X is a union of whole components of the "cycle graph" (C_k B-cycles, adjacent when
 they share an orbit) such that every orbit of the component is of type 0, no cycle contains an apex
 edge with s = 1, and at every orbit u the lifts of its three or four C-neighbours sum to zero.
 The last condition forces the "other" coordinates of u's C-neighbours to cancel in pairs (for example
 s_k(u), a_k(u) in cells {k,a}, {k,b} and s_l(u), a_l(u) in cells {l,a}, {l,b} with opposite signs).
 Consequence: two feasible signings of the same complete unsigned pair that agree on every
 disjoint-support edge coincide, unless the cycle graph has such an all-type-0, apex-free,
 pairing-closed component.

## Where the attempt stops (exact missing implication)

(R) needs: no flip set X containing a disjoint-support edge satisfies (D). Neither R2 (row
zero-sums) nor the triangle form of (D) excludes this: along a flipped disjoint-support edge uv with
beta = 0, (D) only requires the common neighbours with one flipped edge to be {w1}, {w2} or {w0,w1,w2}
(w0 the negative triangle), and these local patterns are compatible. The spectral side gives no
contradiction either: N, N' have equal spectra and kernel, Y = (7/2)(P_4 - P'_4) has symmetric
spectrum +-sqrt(12 + kappa - kappa^2) paired with eigenvalue pairs kappa, 1 - kappa of K, all
consistent. The missing step is global.

No experiment was run: there is no complete unsigned pair at m = 7 to test on, and the m = 11 graph
has no overlap edges at all (all squares type 2), so it cannot test R1-R4.

Status: (R) OPEN. R1-R4 PROVED HERE. R4 eliminates the C_k phase bits as independent choices except on
pairing-closed all-type-0 components. It excludes no unsigned pair and no Sigma-class.
