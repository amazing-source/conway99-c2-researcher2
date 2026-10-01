# Resource needed for the odd 3-eigenspace (m = 7) — 2026-10-01

**Question (from the user).** What is the minimum leakage/twist resource required to support d independent exact odd 3-eigenvectors?
- Seek d <= F(tau, ||Z||^2, fixed scalars), or ||Z||^2 >= G(d, tau).
- Insert d = 6 and compare with ||Z||^2 <= 448 - 2tau - (tau-56)^2/7.
- The twist configuration is arbitrary mixed twist. NO skeleton classification.
- If the scalar bound is too weak, identify the missing geometric information on supp Z, and STOP.

**Pre-registration.** Derivation only, from linear algebra plus the native m = 7 laws (Law G, Law T, quotas).
- No computation is planned.
- At most one tiny sanity check of standard facts about KG(7,2) (one process, < 5 s), with its quantity stated before it is run.

**Notation (as in TWIST_CALCULUS.md).**
- V' = (im M)^perp has dimension 35. It splits as Alt ⊕ Sym' with dimensions 21 and 14.
  - ū_c = (e_c+ - e_c-)/sqrt2.
  - s_c = (e_c+ + e_c-)/sqrt2.
  - Sym' is the set of star-balanced cell functions: sum over c ∋ k of b_c = 0 for every k.
- Q on V' is the block matrix [[Q_A, K^T], [K, C]], and Q^2 + Q = 12 I there; its spectrum is 3 (x20) and -4 (x15).
- K~ := (zeta_(e,c)/2), with rows the Sym cells e and columns the Alt cells c. Then K^T K = K~^T K~ and ||Z||^2 = 2||K~||_F^2.
- Y is the set of flat (type-2) cells, n2 = |Y|, and Tw = the other cells.
- tau = sum_c tau(c) = 42 - 2 n2 - s_s.

## 1. Block equations and the exact eigenvector equations [DERIVED; block identity = C2 §8]

Q^2 + Q = 12I on V' gives three block equations:
- (AA) Q_A^2 + Q_A + K^T K = 12 I_21;
- (SA) K Q_A + C K + K = 0;
- (SS) K K^T + C^2 + C = 12 I_14.

An odd vector v = sum_c t_c ū_c is a 3-eigenvector of Q  <=>  Q_A t = 3t and K t = 0.
- W denotes these t; d = dim W.
- W' denotes the odd -4-eigenvectors (Q_A t = -4t, Kt = 0); d' = dim W'.

**Flat source columns (Law G, density 2).** For a flat cell c, Disj(c) = P(c) ⊔ Dbl(c), and

      Q ū_c = -2 ū_c + sum_{d in P(c)} sigma_cd ū_d + sum_{e in Dbl(c)} eps_ec s_e        (sigma, eps = ±1).

- P(c) consists of the cells with a permutation block to c: all flat cells disjoint from c, plus the non-doubled twisted ones.
- Dbl(c) ⊆ Tw consists of the twisted cells e that are doubled at c: both labels of e see the same label of c.

**Exact odd 3-eigenvector equations**, for t in W:
- (E1) flat rows c in Y: sum_{d in P(c)} sigma_cd t_d = 5 t_c.
- (E2) twisted rows e in Tw: sum_f (Q_A)_ef t_f = 3 t_e, where (Q_A)_ee = tau(e) - 2.
- (E3) leakage rows: (K~ t)_e = 0. This is automatic for e in Y, because flat cells receive no leakage. For e in Tw it reads

      sum_{c in Y : e in Dbl(c)} eps_ec t_c + sum_{f in Tw} K~_ef t_f = 0.

For W', replace 5 by -2 in (E1) and 3 by -4 in (E2).

The flat world is the case Tw = ∅: then (E1) reads A_g t = 5t, and (E1') reads A_g t = -2t. A_g (coboundary-signed KG(7,2)) has spectrum {10, 1, -4}, so d = d' = 0.

## 2. Exact multiplicity identities [DERIVED; two-subspace decomposition of (Alt, E_3) in V'; not found in C2]

Notation: g := rank K. d_S := dim(E_3 ∩ Sym') and d'_S := dim(E_-4 ∩ Sym') count the exact EVEN eigenvectors.

Facts:
- ker K ∩ Alt = W ⊕ W'.
- (im K)^perp ∩ Sym' = (E_3 ∩ Sym') ⊕ (E_-4 ∩ Sym').
- The generic part of the pair (Alt, E_3) has dimension g in each of Alt, Sym', E_3 and E_-4.

Counting the dimensions 21, 14, 20, 15 gives

      d = 6 + d'_S,    d' = 1 + d_S,    g = 21 - d - d' = 14 - d_S - d'_S.

These are identities, not inequalities. The familiar lower bounds d >= 6 and d' >= 1 are their shadows.
- "Exactly 6 odd 3-eigenvectors" <=> no exact even -4-eigenvector.
- Every extra odd -4-eigenvector beyond 1 corresponds to an exact even 3-eigenvector.

## 3. The m = 7 inputs [Law T, Law G, quotas]

- (M1) Trace: tr Q_A = -sum_c n_s(c) = tau - 42.
- (M2) Flat even rigidity.
  - For a flat cell c, Q s_c = 2 s_c + sum_{d in Disj(c)} s_d (Law G).
  - In cell coordinates Sym' = E_1(KG(7,2)): the 14-dimensional complement of the star space.
  - Hence every star-balanced b supported on Y satisfies Q b = (2I + A) b = 3b. These are exact even 3-eigenvectors:

          d_S >= dim Sym'_Y = n2 - 7 + beta_Y,   hence   d' >= n2 - 6 + beta_Y,

    where beta_Y = the number of bipartite components (isolated vertices included) of the graph ([7], Y).
  - The even part is a corollary of C2 Lemma 9.1 (perfect grids), by linearity. The odd consequence d' >= n2 - 6 + beta_Y uses s.2.
- (M3) Support of the leakage.
  - The rows of K~ vanish on Y. Every column is a star-balanced vector with entries in (1/2)Z, supported on Tw.
  - So a nonzero column has support >= 4 (the smallest nonzero star-balanced integer vector on K7 lives on a 4-cycle) and squared norm >= 1.
  - Flat columns: K~_ec = eps_ec on Dbl(c), and 0 elsewhere.
  - Quota balance of c+ and c- at each port k (not in c) gives the following. Dbl(c) is EMPTY or an ALTERNATING EVEN SUBGRAPH of K([7] \ c), which is a K5: every vertex has as many + edges as - edges. So |Dbl(c)| is in {0, 4, 6, 10}: a 4-cycle, a bowtie (two triangles sharing a vertex), or all of K5. The value 8 is impossible, because the 2-edge complement would have odd degrees.
  - Law T caps the doubling: |{c : e in Dbl(c)}| <= tau(e) <= 2, so sum_c |Dbl(c)| <= tau.
- (M4) g = rank K <= |L| - 7 + beta_L, where L ⊆ Tw is the set of cells receiving leakage.

## 3a. Pre-registered sanity check t04 (standard facts used in M2 and M3; written before running)
Quantities, all on KG(7,2) in cell coordinates:
- (i) dim of the star-balanced space, and max |A b - b| over a basis of it (expected: 14, and 0).
- (ii) min |lambda + 6| over spec A (expected > 0).
- (iii) the number of edge sets of K7 of size <= 3 that carry a nonzero star-balanced vector (expected 0), and an explicit size-4 example.
- (iv) the sizes of nonzero ±1 edge-signings of subgraphs of K5 that are balanced at every vertex (expected {4, 6, 10}).

**t04 result** (t04_kneser_facts.py, output in t04_output.txt):
- (i) dim = 14 and max |Ab - b| = 4e-16.
- (ii) spec A = {-4, 1, 10}, so min |lambda + 6| = 2.
- (iii) 0 edge sets of size <= 3 carry a balanced vector; the 4-cycle with signs +-+- is balanced.
- (iv) balanced signing sizes in K5 = {4, 6, 10}.

All as expected.

## 4. The strongest scalar inequalities [DERIVED]

Let lambda_1..lambda_g be the "leaky" eigenvalues of Q_A, i.e. its eigenvalues on Alt ⊖ (W ⊕ W'). By (AA), K^T K = (3 - Q_A)(Q_A + 4), which is positive definite there, so every lambda_i lies in (-4, 3). Define the two TWIST SLACKS

      sigma_- := tau - 7(d - 6),        sigma_+ := 105 - 7d' - tau.

**(I1) Twist sandwich.** By (M1):
- sigma_- = sum_i (lambda_i + 4) >= 0;
- sigma_+ = sum_i (3 - lambda_i) >= 0;
- sigma_- + sigma_+ = 7g.

All three vanish together, exactly when K = 0. So the twist is pinned: 7(d - 6) <= tau <= 105 - 7d'.

**(I2) Leakage window.** ||K||^2 = sum_i (lambda_i + 4)(3 - lambda_i).
- Cauchy-Schwarz gives ||K||^2 <= sigma_- sigma_+ / g.
- (M3) gives ||K||^2 >= #(nonzero columns) >= rank K = g.

Hence

      2g  <=  ||Z||^2  <=  14 sigma_- sigma_+ / (sigma_- + sigma_+)  ( <= 14 min(sigma_-, sigma_+) ).

The window is nonempty iff g^2 <= sigma_- sigma_+, i.e. iff sigma_-/sigma_+ lies in [0.0213, 46.98] (or both slacks are 0).

**(I3) Answer to the boxed question.** Eliminating sigma_- gives

      d  <=  6 + tau/7 - ||Z||^2/98,          d'  <=  15 - tau/7 - ||Z||^2/98.

- The resource that supports exact odd 3-eigenvectors is TWIST, at exactly 7 units per eigenvector beyond 6. The first 6 are free.
- Leakage does NOT support them: it uses up twist slack (sigma_- >= ||Z||^2/14).
- The minimum resource for d is tau = 7(d - 6). It is attained iff K = 0, i.e. Q commutes with kappa, so D maps cells to cells and 7 | tau.
- So **no inequality ||Z||^2 >= G(d, tau) with G increasing in d follows from scalar data**: the leak-free data (K = 0, d = 6 + tau/7, d' = 15 - tau/7) satisfy every scalar relation of s.2-4. Whether a leak-free configuration exists is open.
- The only scalar lower bound on leakage is ||Z||^2 >= 2g = 2(21 - d - d'), which DEcreases in d.

**m = 11 calibration** (from the C-T2/C-T3 data; eigenvalues 4 and -5, gap 9). BvLS has d = 11, d' = 0, g = 44, sigma_- = sum(lambda + 5) = 66, sigma_+ = sum(4 - lambda) = 330, and ||K||^2 = 495 = sigma_- sigma_+ / g. BvLS sits exactly at the Cauchy-Schwarz (upper) end of the window: all 44 leaky eigenvalues are equal to -3.5.

## 5. Inserting d = 6 and comparing with the capacity bound

At d = 6 and the minimal d' = 1 (g = 14) we have sigma_- = tau and sigma_+ = 98 - tau, and (I2) reads

      28  <=  ||Z||^2  <=  tau(98 - tau)/7.

The right-hand side IS the displayed bound, since 448 - 2tau - (tau-56)^2/7 = tau(98 - tau)/7.
- The window is nonempty iff tau(98 - tau) >= 196, i.e. iff tau >= 3 (exactly, tau >= 2.04).
- Every configuration has tau >= |Tw| >= 11 (R7), so there is NO restriction.

With the flat input d' >= n2 - 6 + beta_Y, we get g = 15 - d' <= 21 - n2 - beta_Y. The window is then nonempty iff 0.146 g <= tau <= 6.854 g, with tau = 42 - 2 n2 - s_s.
- Example, the R7 maximum n2 = 10 with s_s = 0: tau = 22, and the window needs g >= 4, which is compatible.
- No n2 <= 20 is excluded.
- At n2 = 21 (flat) the slacks vanish, so K = 0, d = 6 and d' = 15. That is scalar-consistent; the contradiction is R4, which is geometric.

**Conclusion: the scalar resource bound is too weak.**

## 6. What the scalars cannot see: the master identity on the flat block [DERIVED; flat case = C2 Theorem D']

Restricting (AA) to Y x Y gives

      (A_g[Y] - 5I)(A_g[Y] + 2I)  +  sum_{e in Tw} ( r_e r_e^T + k_e k_e^T )  =  0,

where:
- A_g[Y] is the signed Kneser block of the flat cells (entries ±1 on disjoint flat pairs).
- r_e := (Q_A)_{Y,e} is the TRANSPORT vector of the twisted cell e: ±1 on the flat cells disjoint from e with a permutation block.
- k_e := K~_{e,Y} is the DOUBLING vector of e: ±1 on the flat cells at which e is doubled.
- For each flat c disjoint from e, exactly one of r_e(c), k_e(c) is nonzero. Both vanish if c meets e.
- |supp k_e| <= tau(e) <= 2.
- For each flat c, the set {e : k_e(c) != 0} = Dbl(c) is ∅, a 4-cycle, a bowtie, or all of K([7] \ c).

Consequences:
- spec A_g[Y] lies in [-2, 5].
- ker(A_g[Y] - 5) ⊆ W and ker(A_g[Y] + 2) ⊆ W'. These are flat-supported exact odd eigenvectors, so d >= mult_5(A_g[Y]) and d' >= mult_-2(A_g[Y]).
- Proof of the kernel inclusions: for such u the identity gives sum_e ((r_e.u)^2 + (k_e.u)^2) = 0.

Entry by entry, with pi_f(c,c') := sigma_cf sigma_fc' for flat f, and r_f(c) r_f(c') + k_f(c) k_f(c') for twisted f, so pi_f is in {0, ±1}:
- **Diagonal:** automatic (Law G count).
- **Disjoint flat pair** (c, c'), with T = [7] \ (c ∪ c') containing 3 cells: pi_f(c,c') = sigma_cc' for EVERY f ⊂ T. A twisted cell in T must therefore be UNIFORM (transported to both, or doubled at both) and carry the right sign. "Mixed" (pi = 0) is forbidden.
- **Flat cherry** (c, c'), with W = [7] \ (c ∪ c') containing 6 cells: sum_{f ⊂ W} pi_f(c,c') = 0.
  - With all six cells flat the sum is ±6 (R4). Flat cells pair up with their complements in W with equal pi (Lemma H).
  - Twisted cells in W absorb the defect only through their transport/doubling TYPE and SIGN.

What the scalar data record:
- tr(sum k_e k_e^T) = sum_c |Dbl(c)| (<= tau, part of ||Z||^2/2);
- tr(sum r_e r_e^T) = N(Y, Tw) - sum_c |Dbl(c)|;
- n2, s_s, tau, d, d', g.

**MISSING GEOMETRIC INFORMATION** (the off-diagonal entries above; this is where R4, Lemma H and R5 live):
- for every flat cherry (c, c'), the signed transport/doubling profile of the twisted cells inside W(c,c'): how many are uniform +, uniform -, or mixed;
- equivalently, the intersections Dbl(c) ∩ W(c,c') and Dbl(c') ∩ W(c,c') and the transport signs.

In other words: where the flat leakage supports Dbl(c) (4-cycles, bowties or K5's inside K([7] \ c)) sit relative to the complementary 4-sets of the flat cherries. ||Z||^2 sums |Dbl(c)| and is blind to this placement.

STOP here, as instructed. No mixed-twist skeleton is enumerated.

## 7. Duplication status (checked before promotion; greps of MATH_C2_PROGRAMME.md and c2_experimental/notes)

| Item | Status |
|---|---|
| Block identities (AA), (SA), (SS) | C2 §8 |
| Eigenvector equations (E1)-(E3) | explicit form of C2 §8 + Lemma 8.1; flat case = C2 Theorem D' (A_s^2 = 3A_s + 10I) |
| Multiplicity identities d = 6 + d'_S, d' = 1 + d_S | NOT FOUND (greps: multiplicit / Halmos / intersections with Alt) |
| Twist slacks sigma_-, sigma_+ and the leakage window (I2) | NOT FOUND (greps: N_s <=, tr Q_A); uses tr Q_A = -N_s, the C2 §8 diagonal |
| Sym'_Y consists of exact even 3-eigenvectors | corollary of C2 Lemma 9.1 |
| d' >= n2 - 6 + beta_Y | new as a combination (Lemma 9.1 + s.2) |
| Dbl(c) in {∅, C4, bowtie, K5} | elementary (port quotas); C2 has doubling budgets (note 29 §2, §8 CORRECTION); this support form NOT FOUND |
| Master identity with the (r_e, k_e) decomposition | restriction of C2 §8; flat case = Theorem D' |
| "Budgets do not bite without forced, localized doubles" | c2_experimental note 29 §2 (same conclusion, all-twisted setting) |

## 8. Verdict
- The quantitative interface is exactly (I1)-(I2):
  - tau = 7(d - 6) + sigma_-;
  - 105 - 7d' - tau = sigma_+;
  - sigma_- + sigma_+ = 7 rank K;
  - 2 rank K <= ||Z||^2 <= 14 sigma_- sigma_+ / (sigma_- + sigma_+).
- Exact odd 3-eigenvectors cost twist (7 each beyond 6). Leakage competes with them: d <= 6 + tau/7 - ||Z||^2/98.
- At d = 6 the comparison with L_7(tau) = tau(98 - tau)/7 gives only tau >= 3. Too weak.
- The decisive information is the cherry-level placement of the flat leakage supports (s.6). That is Lemma H territory: a local classification, which was not entered, as instructed.
