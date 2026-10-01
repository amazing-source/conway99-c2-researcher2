# Theorem C (coupled form of the exact system) — FROZEN 2026-10-01

Status: PROVED HERE (elementary). Reformulation only. It is NOT a solution of EX, it excludes nothing, and it makes
NO claim about computational complexity. Duplication class C (new formulation of known information): Q, a, b are
already defined in MODEL.md s.5; what is new is only that the decision problem is stated as a system in (Q, N)
alone, with D eliminated. Uses T4 (working lemma) only where marked. F0 not used.

Notation (MODEL.md s.1-2): R = 42x7 matrix of the positive roots of D7, M = |R|, H = RR^T, K = MM^T, J = all-ones
matrices of the sizes required, S = the signed candidate set, L_N = the real-linear completion system.

## Statement
Consider integer 42x42 matrices Q, N and the conditions
 (C1) Q = Q^T, N = N^T, diag Q = diag N = 0;
 (C2) NR = 0 and N^2 = N + 12I - H;
 (C3) Q^2 + Q + K = 12I + 4J;
 (C4) QM = 4J_(42,7) - 2M;
 (C5) (Q_xy - 1)^2 + N_xy^2 = 1 for all x != y.

(a) If N in S and D in L_N is integral, then (Q, N) with Q := |N| + 2D satisfies (C1)-(C5).
(b) If (Q, N) satisfies (C1)-(C5), put B := [Q = 1], D := [Q = 2] (entrywise indicators off the diagonal, 0 on it).
    Then N in S, B = |N|, Q = B + 2D, D is the permutation matrix of a fixed-point-free involution, D o B = 0,
    and D in L_N.
(c) The maps of (a) and (b) are mutually inverse between {(N, D) : N in S, D in L_N, D integral} and the solution
    set of (C1)-(C5). With T4 (every D in L_N is integral): EX <=> (C1)-(C5) has an integer solution.

## Proof
Off the diagonal put a = (Q - N)/2, b = (Q + N)/2.
(C5) <=> (Q_xy - 1, N_xy) in {(-1,0), (1,0), (0,-1), (0,1)} <=> (a_xy, b_xy) in {(0,0), (1,1), (1,0), (0,1)}.
In particular N_xy in {0, +-1}, B_xy := |N_xy| = [Q_xy = 1], and Q = B + 2D with D = [Q = 2] = a o b.

(a) T4 is not needed here, only integrality of D: D >= 0 integral with D1 = 1 is a 0/1 matrix with one 1 per row;
D = D^T and diag D = 0 make it the matrix of a fixed-point-free involution, so D^2 = I; D o B = 0 is part of L_N.
The off-diagonal cases (B, D) = (0,0), (0,1), (1,0) with N = -1, (1,0) with N = +1 give exactly the four cases of
(C5). (C1), (C2) are N in S.
 (C3): Q^2 = B^2 + 2(BD + DB) + 4I, and 2(BD + DB + D) = 2E = 8I + 4J - K - B^2 - B; add Q = B + 2D.
 (C4): QM = BM + 2DM = BM + 2T = BM + 4J - 2M - BM.
(b) Q 1_42 = 12 1: apply (C4) to 1_7 and use M 1_7 = 2 1_42 (each orbit has two coordinates): 2 Q1 = 28 1 - 4 1.
 B 1_42 = 10 1: diagonal of (C2), sum_y N_xy^2 = 12 - H_xx = 10.
 Hence 2 D1 = Q1 - B1 = 2 1, so D is symmetric 0/1 with zero diagonal and one 1 per row: the permutation matrix of
 a fixed-point-free involution; D^2 = I; D o B = 0 since Q cannot be 1 and 2 at once.
 L_N: symmetric, >= 0, diag 0, D1 = 1, D = 0 on B: shown. DM = (Q - B)M/2 = (4J - 2M - BM)/2 = T.
 BD + DB + D = E: expand (C3) with Q = B + 2D and D^2 = I (reverse of (a)).
 N in S: (C1), (C2), N_xy in {0, +-1}.
(c) (a) and (b) invert each other because Q = |N| + 2D and D = [Q = 2]. The last sentence uses T4.  QED

## Remarks recorded at freezing
 - (C3) and (C4) involve Q only, (C2) involves N only; the two layers meet only in (C5), which is entrywise.
 - In lift language (MODEL.md s.5): a = [x+ ~ y+], b = [x+ ~ y-]; (C3) is the sum of the two channel equations
   (E+): (a^2 + b^2)_xy + Gamma_xy + a_xy = 2 and (E-): (ab + ba)_xy + Gamma'_xy + b_xy = 2 (x != y), with
   Gamma = (K + H)/2, Gamma' = (K - H)/2; the N-part of (C2) is their difference.
