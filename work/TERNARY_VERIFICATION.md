# Independent check of the ternary note (PROOF.md sections 1-3) and its use for the signing problem

Source: work/external/c2_agent2_exact_ternary_2026_09_30/ (zip sha256 d58e042f...49360). Unreviewed by the
T4 referee. Only PROOF.md sections 1-3 were read. Section 5 (special quotient family) was not read or used.

## 1. Lemma 2.1 — CHECKED HERE, correct

Hypotheses: N symmetric, zero diagonal, entries in {0,+-1}; B = |N|, H = RR^T, K = MM^T,
T = 2J - M - BM/2, E = (8I + 4J - K - B^2 - B)/2; NR = 0 (mod 3); F := N^2 - N - 12I + H = 0 (mod 3);
(T-cap) every row of T is binary of weight 2; (E-cap) E is entrywise a nonnegative integer.

Linear part. T-cap gives BM = 4J - 2M - 2T, entries in {0,2,4}. (NR)_ui is a sum of exactly (BM)_ui terms
+-1 (the v with B_uv = M_vi = 1), hence even and in [-4,4]; with 3 | (NR)_ui it is 0. T1 = 2*1 and
M 1_7 = 2*1 give 2 = 14 - 2 - (B1)_u, so B1 = 10*1.
Diagonal. F_uu = (B1)_u - 0 - 12 + |r_u|^2 = 10 - 12 + 2 = 0.
Off-diagonal (u != v). With c = K_uv in {0,1,2}, h = H_uv (|h| <= c), b = B_uv, l = (B^2)_uv:
E_uv = (4 - c - l - b)/2 >= 0 gives l + b + c <= 4; |(N^2)_uv| <= l; so |F_uv| <= l + b + |h| <= 4.
E_uv integral gives l + b + c even; F_uv = (N^2)_uv - N_uv + h = l - b + c = 0 (mod 2) since N = B,
N^2 = B^2 and H = K mod 2. So 6 | F_uv and F_uv = 0.
Used exactly: T-cap (bounds and parity of NR, B1), integrality and nonnegativity of E off the diagonal.
Nothing else. No averaging.

## 2. Theorems 3.1 / 3.2 — CHECKED HERE, correct

3.1: for P over F3 with P = P^T, P^2 = P, P Rbar = 0, diag P = 1, put N = center(P + Hbar). Then
diag(P + Hbar) = 1 + 2 = 0, Nbar Rbar = P Rbar + Rbar(Rbar^T Rbar) = 0 (R^T R = 12 I = 0 mod 3), and
Nbar^2 = P^2 + P Hbar + Hbar P + Hbar^2 = P = Nbar - Hbar (P Hbar = P Rbar Rbar^T = 0, Hbar^2 = 0).
So (2) holds and Lemma 2.1 applies when the caps pass.
3.2: if N satisfies (S), P := Nbar - Hbar = Nbar^2 is symmetric, idempotent ((Nbar - Hbar)^2 = Nbar^2
because Nbar Hbar = 0 and Hbar^2 = 0), P Rbar = 0, diag P = 0 - 2 = 1. Pi = (N^2 + 3N)/28 is the rational
projector onto the 4-eigenspace (4 -> 1, -3 -> 0, 0 -> 0), 3-integral, reducing to Nbar^2; so rank P = 15.

## 3. The signing problem for a complete unsigned pair — equivalence CHECKED HERE

Let (B, D) be ANY complete unsigned pair: B symmetric 0/1, zero diagonal; D a fixed-point-free perfect
matching disjoint from B; Q = B + 2D satisfies QM = 4J - 2M and Q^2 + Q + K = 12I + 4J. Then
 T = 2J - M - BM/2 = DM (from QM = 4J - 2M): binary of weight 2, so T-cap holds;
 E = BD + DB + D (from the Q-equation and D^2 = I): nonnegative integers, so E-cap holds.
Both depend on B only. Hence, for a sign pattern N with |N| = B:
 (N, D) feasible  <=>  NR = 0 and N^2 = N + 12I - H over Z        [L_N is then exactly DM = T, BD+DB+D = E, D a matching]
                  <=>  Nbar Rbar = 0 and Nbar^2 - Nbar + Hbar = 0 over F3      [Lemma 2.1]
                  <=>  P := Nbar - Hbar satisfies P = P^T, P^2 = P, P Rbar = 0, diag P = 1,
                       and P_uv + Hbar_uv = 0 iff B_uv = 0 (u != v)             [Theorems 3.1/3.2]
and then rank P = 15 automatically. Conversely every such P gives N = center(P + Hbar) with |N| = B and
(N, D) feasible. D itself does not enter the signing conditions: it only certifies the two capacities.
This is a reformulation of the remaining problem, not progress on it.

## 4. Where my line-decomposition statements sit inside this problem (exact accounting)

Fix a complete unsigned pair; t(x) = type, tau = sum_x t(x). The linear conditions Nbar Rbar = 0 have
294 rows (x,k):
 tau rows with k in supp x cap supp pi x (0 terms: trivial);
 84 - tau rows with k in supp x \ supp pi x (2 terms: the two C_k-edges of x);
 84 - tau rows with k in supp pi x \ supp x (2 terms);
 126 + tau rows with k outside supp x cup supp pi x (4 terms).
The quadratic conditions have 861 off-diagonal entries: 21 at pi-pairs, 210 at B-edges, 630 others.

 - Star-sign rule and alternation (JOINT_CHECKPOINT_1 (b)) = exactly the 84 - tau two-term rows of the
   first kind. In P-language: on each C_k B-cycle, P alternates between Hbar (star) and 0 (antistar).
   They fix every overlap-edge entry of P up to one phase bit per C_k B-cycle (in-cell edges couple
   two cycles). Content of note 149 s.2 (two perfect matchings Q_c, P_c).
 - Apex concordance ((c)) = the 21 quadratic entries at pi-pairs.
 - E* triangle relations ((a)) = the 210 quadratic entries at B-edges (number of negative triangles
   per edge).
 - Lemma CM ((e)) = the 21 quadratic entries at cell-mate pairs, after substituting the forced
   products of C_i- and C_j-paths.
 Not controlled by any of these: all 84 - tau two-term rows of the second kind and all 126 + tau
 four-term rows (they mix overlap and disjoint-support edges); the remaining quadratic entries
 (about 600) whose common neighbours are reached through a disjoint-support edge or through
 overlap edges at two different coordinates. The free data are the signs of the disjoint-support
 B-edges (at least 126 of 210) and the cycle phases.
