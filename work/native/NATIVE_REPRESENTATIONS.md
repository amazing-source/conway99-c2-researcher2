# NATIVE REPRESENTATIONS of the four-state system (phase started 2026-10-01)
Blind phase: no prior notes read. Native data only: 42 labels x with roots r_x (two nonzero coordinates +-1),
m_x = |r_x|; pair states c_xy in {n,d,m,p} with (q,s) = (0,0),(2,0),(1,-1),(1,+1); row rules (1 d, 10 signed,
30 n); port rules (signed balance, unsigned quota); pair-composition rules (two target sums from the same 40 z).
Each representation: NAME / PRIMITIVES / EXACT DEFINITION / FIRST LAWS / EXAMPLES / COUNTEREXAMPLES /
EXTENSION RULE / WHAT IT COMPRESSES / WHY IT MAY MATTER / STATUS.

## R-A. PORT GRAPHS (rows as charged multigraphs on the coordinates)
PRIMITIVES. The 7 coordinates as vertices ("ports"); for each label x a multigraph Phi_x on them.
EXACT DEFINITION. Every signed partner y of x (c_xy in {m,p}) is drawn as an edge on supp(y) carrying at each end
a CHARGE s(c_xy) r_y(a) in {+1,-1}; the double partner pi x is a heavy uncharged edge on supp(pi x).
FIRST LAWS (derived from the row and port rules only).
 A1 Degree profile: deg_Phi_x(a) (signed edges) = 4 - 2[a in supp x] - 2[a in supp pi x] in {0,2,4}.
    (Quota rule minus the heavy edge.) Types: x and pi x disjoint: (2,2,2,2,4,4,4); sharing one coordinate:
    (0,2,2,4,4,4,4); same support: (0,0,4,4,4,4,4). Ten signed edges in every case.
 A2 Charge balance: at every port the charges sum to 0 (signed balance rule).
 A3 End-type law: an edge has equal end charges iff its root is of plus type (e_a + e_b); hence
    #(+ ends) = 2#(plus-type p) + #(minus type), #(- ends) = 2#(plus-type m) + #(minus type), so in EVERY row
    #p = #m among the plus-type partners.
 A4 Trail law: pair the + ends with the - ends at every port (any such pairing). Phi_x splits into closed trails,
    and each closed trail contains an EVEN number of plus-type edges (a transition flips the charge, a plus-type
    edge keeps it, a minus-type edge flips it; closing the trail needs an even number of keeps).
 A5 Duality: y is an edge of Phi_x (on supp y) iff x is an edge of Phi_y (on supp x), same state.
 A6 Pair rule in this language: Phi_x and Phi_y share labelled edges with total weight 4 - k_xy - q(c_xy) and
    total concordance s(c_xy) - h_xy (concordance of a shared edge z = s(c_xz)s(c_zy); heavy edges weigh 2).
EXTENSION RULE. Attaching a label z with partners T: draw the edge supp(z) (with charges) into Phi_t for t in T,
and build Phi_z from the edges supp(t). Legal iff every port stays within its degree and can still balance.
WHAT IT COMPRESSES. A row = a 10-edge charged multigraph on 7 points with a fixed degree profile.
WHAT IS FORGOTTEN. Which of the (at most two) labels of a cell is used is kept only through the charges.
EXAMPLES / MICROSCOPE m01 (native/m01_row_count.py, exact DP). For x = (12,+), the number of state assignments of
its row satisfying the row rules and the port rules A1-A2: double partner of type 0: 930 336; type 1: 155 904
(both signs); type 2: 22 176. About 2.2e7 admissible rows per label once all 40 partner choices are summed.
So row legality alone is very flexible; all restriction lives in A6 (two-row overlaps).
STATUS. Exact laws A1-A6 (A3, A4 derived here). Compresses rows; does not by itself see the overlaps.

## R-B. LINK INVOLUTIONS / TWIST (not pair-state based: primitives are pairings local to one coordinate)
PRIMITIVES. For each coordinate i, the 12 labels O_i containing i, and two pairings of O_i.
EXACT DEFINITION. For x in O_i, port i of x carries weight 2: either the heavy edge (i in supp pi x), or exactly two
signed partners with opposite charges (A2). Put link_i(x) = pi x in the first case and, in the second, the partner
whose charge is -r_x(i). Let kappa be the sibling pairing (i,j,s) <-> (i,j,-s). The TWIST at i is the pair
(link_i, kappa).
FIRST LAWS.
 B1 link_i is a fixed-point-free pairing of O_i (the charge condition s(c_xy) = -r_x(i) r_y(i) is symmetric, and each
    port i has exactly one partner of charge -r_x(i)). The other port-i partner defines a second pairing anti_i.
 B2 link_i U kappa splits O_i into alternating cycles. A cell {i,j} is FLAT at i when link_i(x) = kappa x for its
    labels. Flat at i happens exactly when the cell is a heavy pair (pi x = kappa x), or its two labels are signed
    partners with state m (i the smaller coordinate) or p (i the larger one). A signed sibling pair is therefore
    flat at exactly one of its two coordinates.
 B3 GLOBAL FLATNESS LAW: all 7 coordinates flat  <=>  all 21 cells are heavy sibling pairs (B2: a cell flat at both
    of its coordinates must be heavy). In the native system at m = 7 this configuration is impossible (all-sibling
    exclusion, available from the coordinate rules), so the system is NECESSARILY TWISTED somewhere. In the m = 11
    analogue every coordinate is flat (all cells heavy siblings).
 B4 Signs on links are forced: a signed link has s(c_xy) = -r_x(i) r_y(i).
 B5 A twisted signed link (x, y in different cells, linked at i) has pair targets (2, -2 r_x(i) r_y(i)): exactly two
    common signed partners, both of concordance -r_x(i) r_y(i), no heavy witnesses; and neither common partner
    contains i (a common partner in O_i would carry two anti charges at its port i, contradicting A2).
 B6 The links over all coordinates give every label exactly two links, so they form closed walks in the complete
    graph on the 7 coordinates, using each of the 42 labels once (each label is an edge traversed at its two
    coordinates). In the flat case the walks are all 21 digons.
EXTENSION RULE. Attaching a label z fixes its two links (one per coordinate of z) and its anti partners.
WHAT IT COMPRESSES. The line structure at the coordinate points: seven pairings of 12 labels.
WHY IT MAY MATTER. It measures the departure from the flat (m = 11 type) structure; m = 7 forces departure.
STATUS. Laws B1-B6 derived. Likely overlap with prior notes on how a cell's two labels are paired by coordinates
(duplication check pending). The "total twist" is the natural global quantity; no law for it found yet.

## R-C. DEBT LEDGER (primitives: residual obligations of a partial object)
PRIMITIVES. For a partial assignment P on a label set S (all pairs inside S fixed): for each pair {x,y} in S the
DEBT (W - sum_{z in S} q q, T - sum_{z in S} s s) with (W,T) = (4 - k - q(c_xy), s(c_xy) - h_xy); for each x in S
its residual ports (degree and charge still owed at each coordinate) and residual counts.
FIRST LAWS.
 C1 Weight debts never increase as S grows; a completion exists only if every debt ends at (0,0); the sign debt T'
    of a pair with weight debt W' satisfies |T'| <= W' and T' = W' (mod 2) at every stage that can still close
    (each signed witness changes weight and sign by 1, a heavy witness changes weight by 2 and sign by 0).
 C2 Attachment = paying a clique: attaching z with partner set T pays q(c_zt)q(c_zt') and s(c_zt)s(c_zt') to every
    pair {t,t'} of T, and creates the new pairs (z,t) whose debts are their targets minus the payments by S.
 C3 ORDER LAW: attaching z then w gives exactly the ledger of attaching w then z (same states). Every ledger entry
    is a sum over intermediate labels of a term depending only on two states. So raw extension has NO
    order-of-extension defect; any defect must come from a non-raw procedure (forced moves, canonical choices).
 C4 The ledger cannot be compressed to per-label data: by C2 the legality of attaching z depends on the debts of
    the pairs inside its partner set. Per-port and per-label residuals do not contain these, since they depend on
    which labels are partners and not only on port totals.
STATUS. Exact but elementary. C3 answers the order-of-extension experiment negatively for raw extension.

## Duplication status (targeted; from repository passages already read earlier in this session, no new reading)
 - R-B: link_i = the matching m_i of the notebook's Lemma 3 (MATH_C2_PROGRAMME.md s.1); B2 = its s.11 remark
   ("une arete soeur simple appartient a R_i ET a R_j, m dans l'un, pi dans l'autre"); B3 with the m = 7
   impossibility = Theoreme D (all sibling squares impossible). REDISCOVERY for B1-B3. B5 and B6 and the
   "flat / twisted" reading: not seen; no leverage yet.
 - R-A: A1 = the quota rule; A3 = the signed balance summed over coordinates (known type of identity); A4 and the
   exact row counts of m01: not seen; new data, no leverage.
 - R-C: elementary; C3 (no order defect for raw extension) not seen stated; no leverage.
