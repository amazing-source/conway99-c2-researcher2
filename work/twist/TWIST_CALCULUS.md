# Twist calculus (the m = 7 specific phenomenon) — started 2026-10-01

All other routes are FROZEN. No cocycle, holonomy, lattice parity or local classification is used as a starting point.
I use only the native data:
- labels x = (cell, sign);
- states n, d, m, p;
- row rules;
- port rules: the profile deg_x(k) = 4 - 2[k in supp x] - 2[k in supp pi x], and charge balance;
- pair rules: weight W = 4 - k - q and sign S = s - h.

Results that already exist are cited with their file. Status tags:
- [DERIVED] means derived here from the native rules.
- [CITED] means taken from an existing result.
- [CHECK] means confirmed by a computation.

## 0. Vocabulary and three laws

**Ports.** For k in supp x, the port (x, k) is HEAVY if k is in supp pi x, and OPEN otherwise.
- type(x) := |cell x ∩ cell pi x|.
- Type 2: both ports heavy (a "flat cell").
- Type 1: the port at the apex (the common coordinate) is heavy, and the other ("outer") port is open.
- Type 0: both ports are open.

Further notation:
- Open_k := the labels containing k whose port k is open.
- d_k := (12 - |Open_k|)/2, the number of heavy links at k. Heavy labels at k pair up under pi, so |Open_k| is even.
- link_k and anti_k are as in NATIVE_REPRESENTATIONS (Representation B).
- An incidence (c, k) is FLAT iff link_k(c+) = c-.
- tau(c) := the number of twisted incidences of c, in {0, 1, 2}; tau := sum_c tau(c).

**Law O (open-port law)** [DERIVED].
- Statement. The signed relations between labels of Open_k form a 2-regular graph G_k on Open_k. Its edges alternate between link_k and anti_k. Hence |Open_k| is in {0, 4, 6, 8, 10, 12}, equivalently d_k != 5.
- Proof, step 1. An open port k of x has quota 2 and no d-contribution, so x has exactly two signed partners z containing k.
- Proof, step 2. Each such z receives x at its own port k (q = 1). If k were in supp pi z, the port of z would already be full. So z is open at k.
- Proof, step 3. By balance at port k, the two charges are +1 and -1, so x has one link_k partner and one anti_k partner. Both relations are symmetric (B1).
- Proof, step 4. So link_k and anti_k are fixed-point-free involutions on Open_k with no common edge. Their union is a union of alternating cycles of even length >= 4.

**Law T (twist = doubling)** [DERIVED].
- Statement. For every cell c,
      tau(c) = (Q^2)_(c+,c-) = sum_z q(c+,z) q(c-,z).
- The sibling pair rule gives the value 4 - 2 - q(c+,c-) = 2 - q(c+,c-).
- By B2, a heavy sibling pair has tau = 0, a signed sibling pair has tau = 1, and an n-sibling pair has tau = 2.
- In words: a cell is twisted exactly as many times as its two labels have common partners (q-weighted). Flat means no common partner. Summing over cells,
      tau = sum_z dbl(z),   where dbl(z) := sum_c q(z,c+) q(z,c-)
  is the "doubling" of z, i.e. how much z sees both labels of one cell.

**Law G (rigid flatness at m = 7)** [CITED: R4(i), LEMMA_H.md G0/G].
- Statement. If c is type 2, every label whose cell is disjoint from c has exactly one B-neighbour in c, and every label whose cell meets c has none.
- In particular, a type-2 cell is never doubled, and every 2x2 block B[e,c] with e disjoint from c has row sums 1.
- This is where the m = 7 coincidence enters. B(c+) and B(c-) have 10 + 10 = 20 elements, and Disj(c) also has 20 elements, because 2(2m-4) = (m-2)(m-3) at m = 7.
- At m = 11 the analogue covers only 36 of the 72 labels of Disj(c).

## 1. The atomic move

**Observation F.**
- In a flat configuration (all cells type 2), link_k(x) = pi x = kappa x for every k.
- So NO coordinate pairing can change unless D changes. Every twist is carried by a change of D.

**Definition (cherry move chi(i; j, j'; eps)).**
- Take two flat cells sharing coordinate i: c = {i,j} with labels x, kappa x, and c' = {i,j'} with labels y, kappa y, where j != j'.
- Replace the D-pairs {x, kappa x} and {y, kappa y} by:
  - {x, y} and {kappa x, kappa y} (eps = +), or
  - {x, kappa y} and {kappa x, y} (eps = -).
- Both new pairs are type 1 with apex i.

**Proposition 1 (minimality)** [DERIVED].
- A change of a perfect matching touches at least 4 labels (a 2-switch). In a flat configuration, a 2-switch of two D-pairs is either:
  - a cherry move (the two cells meet), or
  - a disjoint switch (the cells are disjoint, giving two type-0 pairs).
- The cherry move changes exactly one coordinate pairing by a single 2-switch: link_i goes from kappa to (x <-> y', kappa x <-> kappa y'), and this new link is still heavy.
- A twisted SIGNED link at i would need the four labels to be open at i. That needs pi to move away from all four of them, which is again at least a 2-switch, plus signed relations.
- So the cherry move is the smallest modification of the coordinate pairings: 4 labels, one coordinate, one 2-switch.

**Proposition 2 (one move never closes; minimal closure)** [DERIVED].
- After chi(i; j, j'), the set Open_j is {x, kappa x}.
- The sibling relation x ~ kappa x must be n: kappa x contains i, and port i of x is already full.
- So x has no admissible partner at port j, and Law O fails at j (|Open_j| = 2). The same failure occurs at j'.

Classification of the smallest D-changes from the flat configuration that satisfy Law O at every coordinate:
- Let t be the number of non-type-2 cells.
- Counting open ports: a type-1 pair opens 2 ports and a type-0 pair opens 4. Every nonempty Open_k needs at least two cells.
- This rules out t <= 3. For t = 4 the four cells form a 4-cycle a-b-c-d of K7, paired in one of two ways:
  - HINGED QUAD: ab <-> bc (apex b) and cd <-> da (apex d). These are two cherry moves with the same outer pair {a, c}. The heavy twisted corners are b and d; the open twisted corners are a and c, where the cross relations are forced to be signed.
  - CROSSED QUAD: ab <-> cd and bc <-> da. All eight ports are open. The sibling relations may be signed, so a corner may be "open but flat". The minimum is 2 twisted corners (b and d), with a and c flat through signed siblings.
- Mixed pairings fail Law O. Example: ab <-> bc, ab' <-> cd, ...; this fails at b.

Terminology note. "Square" is already used in the repository for a D-pair (a 4-cycle of the 99-graph). The new 4-cycle objects of K7 are therefore called QUADS.

## 1a. Pre-registered computations (written BEFORE running anything)

**C-T0 (confirms Proposition 2; tiny).**
- Enumerate every D-change from kappa with at most 4 non-type-2 cells: every set of <= 4 cells, and every re-pairing of their labels that pairs no two cell-mates.
- Test Law O by counting: |Open_k| is in {0} ∪ [4, 12] for all k.
- Quantity tested: the list of survivors up to S7.
- Expected: none for t <= 3; for t = 4, exactly the hinged and crossed quads.

**C-T1 (step 5, closure at skeleton level).**
- The closure problem at the level of (set of twisted cells, pi) was already solved WITHOUT Law O in R7 (LEMMA_H.md s.7: 132 S7-classes survive Lemmas H, G4, PI and J; max n2 = 10).
- C-T1 adds only the new Law O, together with the refinement it implies for the degree profile (open-port partners must themselves be open at that port).
- Quantity tested: for each R7 class, does some pi exist that satisfies PI, the refined G4 and Law O at all 7 coordinates? Output: the surviving classes and the new maximum of n2.

**C-T2 (calibration of the leakage law of s.5; tiny).**
- Quantity tested: on BvLS (m = 11), the number of 2x2 blocks B[e,c] with e disjoint from c that are NOT permutation matrices ("half-blocks"), and the leakage norm ||Z||^2 defined in s.5.
- Prediction (proved in s.5 by a trace argument): ||Z||^2 > 0.

## 1b. DUPLICATION CHECK (done before any computation, 2026-10-01)

Source: C:\Users\bfhdh\Desktop\conway99-involution\notes\MATH_C2_PROGRAMME.md, read-only. I read §7-8, §14, §19, §24 (header), §32-34 and the §5 header. Its status labels are its own; I re-verified nothing below.

The twist programme is, in substance, the C2 "côté dense" analysis of the D-structure. Here is the mapping from my terms to C2 terms:

| My term | C2 term | C2 location |
|---|---|---|
| flat cell / type 2 | carré "frère", n_s(P) = Q_{P0P1} = 2 | §7, §8 |
| link_k ∪ anti_k (twist at k = non-digon cycles) | R_k = m_k ∪ π_k | Lemma 3 |
| cherry move (atomic twist) | creates a "2-cycle lié" (bound pair) of the D-graph on pairs | §14 |
| cell built only from cherry moves | configuration "ancrée" | §18-19, §24 |
| twisted pair (labels with apexes i and j) | paire "tordue" | §14 |
| Law O | weak form of Lemma 19.1 | §19 |
| Law T | Lemma 8.2 (stated there as "rien de neuf") | §8 |
| Law G | Lemma 8.1 = perfection of the grid G_P | §8, §9.1 |
| odd-sector absorption law | the Sym/Alt compression: Q_A^2 + Q_A + K^T K = 12I, with Q_A = X/2 and K = Z/sqrt2 | §8 |
| "a type-2 cell never leaks" | row P of K is null for P sibling | Lemma 8.1 |
| "leakage into a flat cell needs doubling" | the 2026-09-25 CORRECTION (the mu-partner) | §8 |
| m = 11 contrast (half-coverage) | coherence remark "18 < 36" | §7 |

Lemma 19.1 is STRONGER than Law O. Two sister orbits with n_s = 0 have at most one common neighbour in R_s. So Open_s can never be exactly the 4 orbits of two pairs whose sibling relations are both n (K_{2,2} is forbidden). Native re-derivation:
- Suppose x and kappa x share both R_s-neighbours.
- Charges then give s(x,z)s(kappa x,z) = -r_x(s) r_{kappa x}(s) for both common neighbours, so the sum is ±2.
- But the sibling rule needs that sum to be 0, while Law T says the doubling weight 2 is used up by these two partners. Contradiction. [DERIVED, agrees with C2.]

Consequences for my s.1:
- The HINGED QUAD is dead (K_{2,2} at both open corners).
- The CROSSED QUAD is dead when its sibling relations are n.
- What survives at the skeleton level is only the crossed quad with signed siblings at the "open but flat" corners.
- So two cherry moves with the same outer pair do NOT cancel. They produce a secondary defect (K_{2,2}).

Global closure in C2 (as C2 states it, not re-verified):
- Anchored configurations, i.e. twist systems built only from cherry moves: none exist. §24 "Lemme de la queue", by hand, re-read by "structures".
- Pure all-twisted: excluded. §32, with hand proofs plus 84 + 14 exact certificates, cross-checked.
- M1 (one twisted cycle, the rest anchored): mostly closed. §27, §30-31, §33.
- OPEN:
  - general mixtures (classes 6-14 and 17 leave 10^4 to 2*10^5 skeleton classes each; C2 §33 says they "need a new structural lever");
  - disjoint squares (Lemma 11.2 is open);
  - AD configurations (in progress).
- C2 §33 diagnosis: LPs at the pair (Sym) level are feasible, while the orbit-level identity kills. The contradiction lies in "which of the two orbits of a pair receives the neighbour", i.e. in the Alt (kappa-odd) sector.

Revised plan:
- C-T1 is CANCELLED. Adding the weak Law O to R7 would only reproduce, more weakly, C2 work that already exists.
- C-T0 is kept as pre-registered. I add one filter, declared now: C2's K_{2,2} rule. If |Open_k| = 4 and the open labels are exactly the 4 labels of two cells, each with at least one type-1 label (which forces n_s = 0), then the configuration dies.
  - Quantity: the survivors of (Law O) and of (Law O + K_{2,2}), by S7-type.
- C-T2 is kept (BvLS leakage calibration).

## 1c. Results of C-T0 and C-T2 [CHECK]

**C-T0** (t00_minimal_closure.py, output in t00_output.txt; < 10 s).

| broken cells t | re-pairings | pass (O) | pass (O)+(K22) |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 2 | 420 | 0 | 0 |
| 3 | 10640 | 0 | 0 |
| 4 | 359100 | 1260 (2 S7-types) | 420 (1 S7-type) |

The two t = 4 types:
- HINGED quad: 840 = 105 4-cycles x 2 orientations x 4 label matchings. All killed by K22.
- CROSSED quad: 420. Survives K22 (its labels are type 0, so its siblings may be signed).

Proposition 2 is confirmed. Note that the crossed quad = two disjoint squares (C2 "carrés disjoints"). That is exactly the family C2 has NOT closed (Lemma 11.2 open, §33).

**C-T2** (t02_bvls_leakage.py, output in t02_output.txt).
- BvLS: all 55 cells are flat (D = kappa).
- Every one of the 1980 ordered disjoint cell pairs (e, c) is a half-block: no permutation blocks, and zeta(e,c) = ±1 (990 each).
- In fact there is exactly one B-edge per disjoint cell pair: 990 B-edges for 990 Kneser edges.
- The C2 identity at m = 11, Q_A^2 + Q_A + Z^T Z/2 = 20I, holds. ||Z||^2 = 990 and tr Q_A = -110.
- spec Q_A = {4 (x11), -3.5 (x44)}. The multiplicity of 4 equals its interlacing lower bound 11, and the other 44 eigenvalues are all equal.

## 2a. Covering density of a flat cell, and the leakage capacity law [DERIVED]

**Covering density of a flat cell.** The two labels of a flat cell have 2(2m-4) neighbours spread over the C(m-2,2) disjoint cells, so

      edges per disjoint cell = 8/(m-3) = 2 at m = 7,  1 at m = 11.

- m = 7: density 2.
  - Every block to a disjoint cell carries exactly 2 edges: each label of the other cell sees exactly one label of c (Law G).
  - Between two flat cells the block is a permutation.
  - Hence a flat cell never leaks (zeta(c,.) = 0), and leakage into it arises only when one of its labels doubles a twisted cell.
  - This is "rigid flatness".
- m = 11: density 1. Every block has a single edge, so ζ = ±1 everywhere. This is "maximally leaky flatness" (C-T2).

So the m = 7 phenomenon is not "flat versus twisted". It is: **at m = 7 flatness kills leakage; at m = 11 flatness carries maximal leakage.**

**Leakage capacity law (m = 7).** The ingredients:
- Q restricted to V' (dimension 35) has eigenvalues 3 (x20) and -4 (x15).
- Alt (dimension 21) lies inside V'. Interlacing then gives:
  - Q_A has spectrum in [-4, 3];
  - dim(E_3 ∩ Alt) >= 6 (exact kappa-odd 3-eigenvectors, which carry no leakage);
  - dim(E_-4 ∩ Alt) >= 1.
- tr Q_A = -sum_c n_s(c) = tau - 42.
- The sibling rule summed over cells gives 2||Q_A||^2 + ||Z||^2 = 588 - 2 tau.
- Minimising ||Q_A||^2 under these constraints gives

      ||Z||^2 <= L_7(tau) := 448 - 2 tau - (tau - 56)^2 / 7        (L_7(0) = 0, L_7'(0) = 14, L_7(42) = 336).

At m = 11, the same computation (eigenvalues 4 x55, -5 x44; forced mult(4) >= 11; tr Q_A = tau - 110; total 2420 - 2 tau) gives

      ||Z||^2 <= L_11(tau) := 2068 - 2 tau - (tau - 154)^2 / 22   (L_11(0) = 990).

**BvLS attains L_11(0) = 990 exactly** (C-T2).

At m = 7 and tau = 0 the capacity is 0. Zero twist therefore forces Z = 0 and spec Q_A = {3^6, (-4)^15}. Why it is pinned exactly:
- the trace -42 equals the minimum trace allowed by the six forced eigenvalues 3: 6*3 + 15*(-4) = -42;
- this is the m = 7 identity -2C = a_1(theta_1 - theta_2) + theta_2 C with C = 21, a_1 = 6.

The flat Q_A = A_g - 2I instead has spectrum {8, -1^14, -6^6}, because R4 forces g to be a coboundary. This is R4 seen in the Alt sector.

Each unit of twist buys about 14 units of leakage capacity ||Z||^2. The capacity law is a necessary condition of a solution. It is not, by itself, an obstruction.

**Side remark (precise case K = 0, i.e. Q commutes with kappa).** Then Q_A has spectrum {3^a, (-4)^(21-a)}, so tau = 7a - 42, and **7 | tau**. In particular, D must map cells to cells (no twisted or mixed pairs). I did not find this case in C2 §8. It only applies under the extra hypothesis K = 0. AD-type configurations satisfy D∘kappa = kappa∘D but need not have K = 0.

## 1d. Pre-registration of C-T3 (written BEFORE running)

**Question.** The forced exact kappa-odd eigenvectors: their number is 11 = m at m = 11 and >= 6 = m - 1 at m = 7. If they are COORDINATE-INDEXED (one per coordinate, "star" vectors), the m = 7 requirement becomes a per-coordinate closure condition on 7 coordinates with one relation. Test on BvLS whether the 11-dim exact 4-eigenspace W of Q_A (with K W = 0) is coordinate-indexed.

**Quantities.**
- (a) Check that K W = 0.
- (b) For each coordinate k, dim{t in W : supp t ⊆ star(k)}.
- (c) For each k, dim{t in W : supp t ⊆ cells avoiding k}.
- (d) The support sizes of an RREF basis of W.

One process, < 10 s.

**C-T3 result** (t03_bvls_odd_eigenspace.py, output in t03_output.txt).
- W := ker(Q_A - 4) has dimension 11, and K W = 0 exactly. All forced odd eigenvectors are exact; there is no leaky part.
- No vector of W is supported inside a star.
- For EACH coordinate k there is exactly one vector w_k in W supported off star(k):
  - it is a ±1 vector on all 45 cells avoiding k;
  - {w_0, ..., w_10} is a basis of W (rank 11, no relation).
- So in BvLS the forced kappa-odd eigenspace is COORDINATE-INDEXED: v_k = sum_{c not containing k} eps_k(c) u_c, and Q v_k = 4 v_k.

At m = 7:
- A flat world has NO such vector. For d not containing k, the requirement reads sum over the 6 cells c inside [7] \ (d ∪ {k}) of eps(c) = 5 eps(d), which is impossible by parity (equivalently, A has no eigenvalue 5).
- A solution needs dim(E_3 ∩ Alt) >= 6.
- Open question raised (NOT a result): is a coordinate-indexed version forced at m = 7, i.e. 7 vectors v_k (supported on the 15 cells avoiding k) with at most one relation?

## 2. Effect of one cherry move chi(i; j, j'; eps) on a flat background [DERIVED]

Notation: c = {i,j} with labels x, kappa x; c' = {i,j'} with labels y, kappa y; y' := y (eps = +) or kappa y (eps = -).

- **D.**
  - The pairs {x, kappa x} and {y, kappa y} are replaced by {x, y'} and {kappa x, kappa y'}.
  - Census: n2 goes from 21 to 19, n1 from 0 to 2.
  - D still commutes with kappa, so D creates no leakage.
- **Q on the 4 labels (forced).**
  - Q[c,c'] = 2 * (eps-matching).
  - The sibling relations x~kappa x and y~kappa y become n (port i is full).
  - x ~ kappa y' is n.
- **Links.**
  - link_i undergoes a single heavy 2-switch.
  - Cell c becomes open at j, and c' at j'. Both cells are twisted at both coordinates, so tau rises by 4.
  - At coordinate i, the two kappa-digons of link_i ∪ kappa (cells c and c') are replaced by one alternating 4-cycle.
- **Degree profiles: the port dislocation.**
  - deg_x - deg_x(flat) = 2(e_j - e_j'), and the same for kappa x.
  - For y and kappa y it is 2(e_j' - e_j).
  - The port-shift equation, for every label: sum_e eps_e(x) m_e = 2(m_x - m_pi x). Here eps_e(x) is the deviation of x's multiplicity in cell e from the flat value.
- **Unavoidable defects in a flat background** (one move alone).
  - (O): |Open_j| = |Open_j'| = 2, a deficit of 2 partners at the outer port of each of the 4 labels.
  - (G): at the partner coordinate j' of x, the 4 flat cells {j',l} with l not in {i,j,j'} each force one neighbour (Law G), but the quota is 2. Excess 2.
  - (T): tau(c) = tau(c') = 2 creates a doubling demand of 2 per cell.
    - A common partner z of x and kappa x avoids i (port i is full). It also avoids j, since it would have to lie in Open_j = {x, kappa x}. So z lies in a cell e disjoint from c.
    - CORRECTION (2026-10-01, same session): a flat z is NOT excluded by Law G. A flat cell may see both labels of a twisted cell; that is C2's (2,0) case in the §8 correction. What excludes it here is z's quota at port j: Law G forces 3 neighbours there (the flat cells {j,l} with l not in e ∪ {i,j}), and the doubling would add 2 more, so 5 > 4.
    - If e is twisted, more twist is needed anyway. So in a flat background the demand cannot be met.
- **Pair targets.** Only 4 change:
  - (x, kappa x) and (y, kappa y): W goes from 0 to 2, S stays 0;
  - (x, y') and (kappa x, kappa y'): W goes from 3 to 1, S stays -h.
  - Row sums of the targets are unchanged.
- **N and balances.**
  - The heavy twisted link has no sign constraint (s(d) = 0).
  - The new D-pair (x, y') needs its unique common partner z with s(x,z) s(y',z) = -r_x(i) r_y'(i), so eps matters.
  - The siblings need two signed common partners of opposite concordance (no heavy witness is possible).
  - When the outer ports are filled, their link/anti charges are -/+ r_x(j) (B4).

## 3. What changes and what is conserved

**Changed by one cherry move:**
- n2 (-2) and n1 (+2);
- tau (+4);
- d_j and d_j' (-1 each, while d_i is CONSERVED);
- |Open_j| and |Open_j'| (+2 each);
- the doubling demand (+4);
- four pair targets (±2);
- link_i (by a 2-switch);
- the kappa-digons of link_i ∪ kappa at i (-2), replaced by one alternating 4-cycle.

**Conserved by every move, as identities on the linear system X_lin** (rows, quotas, balance, four states):
- the row counts and the profile totals;
- E_Q [1 | M] = 0 and E_N R = 0, i.e. the pair-rule defect is always port-balanced [DERIVED: QM = 4J - 2M and NR = 0];
- sum_x (port shift) = 0, because pi is an involution;
- |Open_k| is even;
- the trace identity 2||Q_A||^2 + ||Z||^2 = 588 - 2 tau (the sibling rule summed).

**Not conserved and not quantised:** there is no integer-valued twist defect at the skeleton level. Every skeleton law (O, K22, G-quota, H, J) is a monotone covering condition on the set of twisted cells, and none is a sign or phase that could cancel.

## 4. Interaction law of two cherry moves chi_1, chi_2 (cell-disjoint) [DERIVED + C-T0]

- **(O)** The open counts add per coordinate: |Open_k| = 2 * #{moves with outer coordinate k}.
  - Same outer pair: the counts are 4 at both outer coordinates, which is the hinged quad. But this is a SECONDARY DEFECT, not a cancellation: K_{2,2} at both outer coordinates (C2 Lemma 19.1; C-T0 kills all 840 hinged quads).
  - So cherry moves cancel at an outer coordinate only if >= 3 of them share it, or if non-cherry D-patterns contribute single open labels there.
- **(G)** The excess at the partner coordinate j' of a moved label x (cell {i,j}) equals 2 - #{twisted cells {j',l} : l not in {i,j,j'}}.
  - Cancellation: the other move twists such a cell.
  - Reinforcement: the other move adds labels with the same partner coordinate. Their demands add, while cells through i or j never help.
- **(T)** Doubling of a twisted cell c comes from labels in cells disjoint from c, flat or twisted.
  - A flat doubler z (cell e) needs quota room at both coordinates of c. By Law G this means: for each coordinate of c, at least 2 of the 4 cells through that coordinate avoiding e must be twisted.
  - So a second twist supplies the doubling of the first in two ways: by twisting those cells (cancellation), or by containing the doubler itself.
  - Example: in the hinged quad (ab-bc, cd-da), flat labels of the 3 cells inside E = [7] \ {a,b,c,d} have exactly this room.
  - The hinged quad is dead anyway, by K_{2,2}.
- **(H)** A single cherry move creates no disjoint twisted pair, so it heals none of the 105 flat cherry-pairs.
  - A quad heals exactly the 3 inside the complementary triangle.

**Summary:** at the skeleton level, two atomic twists interact by covering and never by cancellation of a signed quantity. The only phase-like interaction is K_{2,2} (a sign clash in the sibling rule), and it is DESTRUCTIVE.

## 5. Global closure on 7 coordinates

**Skeleton level.** This is the C2 dense-side case analysis (status as stated by C2, not re-verified here):
- Twist systems built only from cherry moves (HEAVY twist only = anchored configurations) never close (§24).
- Systems where every pair is split between two apexes (pure all-twisted) never close (§32).
- One twisted cycle plus anchored pairs (M1): mostly closed (§27-33).
- What remains: mixtures of the twist types, and configurations with type-0 pairs. The minimal Law-O/K22-closed unit, the crossed quad, is exactly a pair of disjoint squares, which C2 has not closed.

**Full level (the absorption mechanism, made quantitative).**
- (a) Flatness impossible = zero twist forces zero leakage (L_7(0) = 0) and pins spec Q_A = {3^6, (-4)^15}, which the rigid flat structure cannot realise (R4 in the Alt sector).
- (b) Each unit of twist creates leakage capacity, about 14 units of ||Z||^2.
- (c) Twisting impossible would need to show that no configuration supplies the forced 6-dimensional space of exact kappa-odd 3-eigenvectors together with Q_A^2 + Q_A + K^T K = 12I. NOT shown.
- (d) At m = 11 the flat BvLS supplies its forced 11-dimensional odd eigenspace through coordinate-indexed ±1 vectors and attains the leakage capacity exactly.

## 6. Verdict on the two target theorems
- "Every closed twist system has total defect 0, while m = 7 forces nonzero defect": NOT obtained.
  - At the skeleton level there is no signed or quantised defect (s.3-4), and closed skeletons survive all known skeleton laws (C2's open mixture and disjoint-square families).
  - At the full level the only exact, m = 7-specific defect found is (a) above. It vanishes once tau > 0.
- "A closed twist calculus (constructive grammar)": NOT obtained.
  - The atomic move never closes alone.
  - Its pure compositions die: heavy-only (C2 §24) and split-only (C2 §32).
  - Same-outer-pair composition gives K_{2,2}.
  - Any closure must MIX twist types or use disjoint squares.
- Precise distinction:
  - FLATNESS is impossible because flat cells at m = 7 have covering density 2 and hence no leakage. That is the m = 7 fact (8/(m-3) = 2).
  - TWISTING is impossible only in its pure forms (C2).
  - Mixed twist is the only possible absorber, and the open question is whether it can supply exact kappa-odd 3-eigenvectors (>= 6) at the leakage it creates.
- Novelty: these parts are not found in the C2 notes I read:
  - the covering-density reading of the m = 7 phenomenon;
  - the leakage capacity law L_7, L_11 (with BvLS extremal);
  - the coordinate-indexed odd eigenspace of BvLS;
  - the 7 | tau remark (case K = 0).
- Everything else in s.0-4 is a rediscovery of C2 §8, §14 and §19.
