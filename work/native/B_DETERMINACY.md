# Representation B — determinacy of the disjoint-cell layer (started 2026-10-01)
Question: do R0 = (D, {link_i, anti_i}_{i=1..7}) and the exact rules determine every disjoint-cell state
(pairs with k_xy = 0)?

## 0. What R0 fixes  [DERIVED]
L0. R0 fixes the state of EVERY coordinate-sharing pair (k_xy >= 1): if x, y share i, then y is a signed partner of
    x iff y in {link_i(x), anti_i(x)} (or y = pi x), with s(c_xy) = -r_x(i) r_y(i) for link and +r_x(i) r_y(i)
    for anti; otherwise c_xy = n. (Sibling pairs: link at one coordinate and anti at the other, consistent by B2.)
L1. R0 fixes, for every label x and every outer coordinate e (not in supp x), the RESIDUAL PORT: the degree and the
    charge that x's disjoint partners must still supply at e (quota minus heavy edge minus the R0 edges ending at e;
    minus the R0 charges). For type 0 the residual degrees sum to 12 (six disjoint signed partners), type 1 to 16,
    type 2 to 20.
So the unknown layer is exactly: the disjoint signed partners of every label (and their signs), subject to the
residual ports and to every pair rule.

## 1. Microscope at the smallest scale where a pair rule couples disjoint relations  [CHECKED, m02/m03]
Scale: one TWISTED link y = (12,+), w = (13,+) (link at coordinate 1, state m), complete rows, fixed R0 data:
D-partners (45,+), (46,+); y: link_1 = w, anti_1 = (14,+) p, link_2 = (25,-) m, anti_2 = (26,+) p;
w: link_1 = y, anti_1 = (15,+) p, link_3 = (37,+) m, anti_3 = (23,-) m.
Visible equations: row and port rules of y and w (exact), the pair rule (y,w) (exact), all partially visible pair
rules (y,u), (w,u).
 - admissible disjoint rows: y 66, w 302;
 - joint realizations satisfying every visible equation: 1257;
 - distinct witness pairs of the link: 28 (one witness pair still allows up to 291 realizations);
 - distinct UNSIGNED disjoint supports: 1007; realizations per support: 1 (781 supports), 2 (214), 4 (12).
VERDICT AT R0: NOT DETERMINED.

## 2. The smallest exact pair  [CHECKED twice: m03 search, m04 independent from-scratch verifier, 0 errors]
Two realizations with identical D, identical link/anti data at all four ports of y and w, identical forced
coordinate-sharing relations, satisfying every visible equation, differing in exactly THREE disjoint relations, all
of the label w:   (46,-): p -> m,   (47,-): m -> p,   (67,-): p -> m.      (file native/m04_minimal_pair.json)
The three edges form a triangle on the coordinates {4,6,7} in w's port graph; at each corner the two triangle edges
carry opposite charges, so flipping all three keeps every port of w balanced. No pair of realizations differs in
fewer relations (m03 checked all 1257 realizations pairwise).

## 3. Lemma P (exact description of the sign freedom of one row)  [PROVED HERE]
Fix a label x, its R0 data and the UNSIGNED set of its disjoint partners. Two sign assignments satisfying all of x's
port rules differ exactly on an edge set F that is a union of edge-disjoint ALTERNATING closed trails of x's port
graph (closed trails whose two edges at each traversed coordinate carry opposite charges); conversely flipping any
such trail preserves every port rule of x.
Proof. Flipping an edge changes its charge at both ends by -2(charge). Both assignments balance every port, so at
each coordinate the flipped edges' charges (in the first assignment) sum to 0; pair each + with a - at every
coordinate and follow the pairing: the flipped set splits into closed trails alternating in charge. The converse is
the same computation read backwards.  (By the trail law A4 each such trail has an even number of plus-type edges;
the minimal example of s.2 is a triangle of three minus-type edges.)

## 4. Refinement R0 -> R1 -> R2 at this scale
 R0 = (D, 14 pairings)                                  : 1257 realizations (supports AND signs free).
 Minimal datum separating the closest pair (s.2)        : one PHASE bit (the sign orientation) of one alternating
                                                          closed trail of one row.
 R1 = R0 + unsigned disjoint support of every row        : at most 4 realizations remain; by Lemma P they differ
                                                          exactly by phase flips of alternating closed trails.
 R2 = R1 + one phase bit per alternating closed trail    : determined, but this is the whole state again.
Supports are not determined by R0 (1007 distinct), and nothing coarser that I tested fixes them: the witness pair of
the link leaves up to 291 realizations.

## 5. Verdict
Case 2 (NO). R0 does not determine the disjoint layer, already at the smallest coupling scale. The minimal missing
datum is a phase bit of an alternating closed trail in a single row (Lemma P). The full missing data is the unsigned
disjoint layer plus these phases. So Representation B gives no compression: refining it collapses into the split
"unsigned layer + sign phases". Globally, flipping a trail in one row changes the ports of the partners at
supp(row label), so a global phase freedom must be an alternating structure balanced at every port of every label
and preserving every pair sign sum. Whether R0 plus the unsigned layer forces the phases globally is exactly the
sign-rigidity question (statement (R), OBLIGATION_RIGIDITY.md; FAILURE_MEMORY row 5): a known open basin.
