# Z[C2]-freeness of the eigenlattices: explicit mod-2 gluing and redundancy test (2026-10-01)

Question. Does Lambda_3 = Z[C2]^27, Lambda_-4 = Z[C2]^22 (the freeness lemma, kept as is) imply a relation between the
even data (Q, M) and the odd data (N, R) that is NOT an algebraic consequence of Theorem C?
No 7-adic, oddity, genus or rank-parity input is used here.

## 1. The two sectors in the 49 orbit coordinates  [DERIVED]
Orbits: infinity (fixed), 7 inner {k+, k-}, 42 exterior {x+, x-}.
Odd sector (basis d_x = e_(x+) - e_(x-), 49 coordinates u = (u_in, u_ex)):
    A_- = [[-I_7, R^T], [R, -N]],          A_-^2 + A_- = 12 I_49            (equivalent to (C2a)+(C2b), with R^T R = 12 I_7).
Even sector (values at infinity and at the representatives, 50 coordinates w = (w_inf, w_in, w_ex)):
    B_+ = [[0, 2*1^T, 0], [1, I_7, M^T], [0, M, Q]],   B_+^2 + B_+ = 12 I + 2 J^,
    with J^ = J restricted to V+ (every row (1, 2*1^T, 2*1^T)). Block by block this identity is exactly
    (ext,ext): MM^T + Q^2 + Q = 12I + 4J = (C3);   (in,ext): M^T Q + 2M^T = 4J = (C4);
    (in,in): 2J + I + M^T M + I = 12I + 4J, automatic from M^T M = 10I + 2J.
Write B_orb := [[I_7, M^T], [M, Q]] for the 49x49 orbit block of B_+.

## 2. The gluing, written in Q, N, R, M  [DERIVED]
Lambda_theta = Z^99 cap V_theta. Its odd part is U_theta := {u in Z^49 : A_- u = theta u} and its even part is
W_theta := {w in Z^50 : B_+ w = theta w}. A vector (u + w)/2 is integral iff w_inf = 0 (mod 2) and w_orb = u (mod 2)
on all 49 orbits. Since the two parts have equal rank f (27 resp. 22) and [Lambda : Lambda^+ + Lambda^-] <= 2^f, freeness
is equivalent to the statement
    (G_theta)   U_theta (mod 2) = { w_orb (mod 2) : w in W_theta, w_inf even }   as subspaces of F_2^49,
for theta = 3 and theta = -4.

Explicit glue maps (all integral):
 odd -> even:  u in U_3   |-> w = -(B_+ + 4)(B_+ - 14)(0; u)    (= 77 E_3 applied to the invariant lift);
               u in U_-4  |-> w = (27 - 9 B_+ + J^)(0; u)       (= 63 E_-4 = (B_+ - 3)(B_+ - 14)/2 by the even identity;
                                                                 NOT (B_+ - 3)(B_+ - 14) = 126 E_-4, which is 0 mod 2).
 even -> odd:  w in W_3   |-> u = (A_- + 4) w_orb;     w in W_-4 |-> u = (3 - A_-) w_orb.
 - The images lie in the right eigenspaces because (B_+ - 14)(B_+ - 3)(B_+ + 4) = 0 (from (C3), (C4)) and
   (A_- - 3)(A_- + 4) = 0 (from (C2)).
 - w_inf is even for every w in W_3 or W_-4, from the even sector alone: the infinity row gives
   theta w_inf = 2 sum_k w_k. For theta = 3 this gives 3 w_inf = 2 sum_k w_k. For theta = -4, summing the inner rows
   (sum_k M_xk = 2) gives 3 w_inf = 2 sum_x w_x.
 - The congruences w_orb = u (mod 2) hold for every one of the four maps PROVIDED
        B_orb = A_- (mod 2),   i.e.   [[I, M^T],[M, Q]] = [[-I, R^T],[R, -N]] (mod 2),   i.e.   Q = N (mod 2),
   because M = R (mod 2) and I = -I (mod 2) hold automatically.

## 3. The strongest equation G  [PROVED]
Assume only the separate systems ((C2) on the odd side, (C3)+(C4) on the even side, with the fixed inner/infinity rows).
 (a) Mod 2, A_- is idempotent (A_-^2 + A_- = 12I = 0); its image is U_3 (mod 2) and its kernel U_-4 (mod 2). The
     reductions are complementary because the odd projectors (A_- + 4)/7 and (3 - A_-)/7 have odd denominators.
 (b) Mod 2, B_+ is idempotent on F_2^50 (its idempotents have denominators 99, 77, 63, all odd), acting as 1 on the
     reduction of W_3 and as 0 on the reductions of W_14 and W_-4.
 (c) If (G_3) and (G_-4) hold, then B_orb (mod 2) acts as 1 on U_3 (mod 2) and as 0 on U_-4 (mod 2) (use w_inf even).
     These span F_2^49, so B_orb = A_- (mod 2), i.e. Q = N (mod 2).
 (d) Conversely, Q = N (mod 2) gives (G_3) and (G_-4) through the explicit glue maps of s.2 (each direction is an
     injection between spaces of the same dimension f).
THEREFORE, given the separate systems:   freeness  <=>   G(Q,N) := Q - N = 0 (mod 2) entrywise.

## 4. Redundancy test
 1. Strongest resulting equation: G: Q = N (mod 2).
 2. Theorem C implies G: (C5) allows only (Q_xy, N_xy) in {(0,0), (2,0), (1,-1), (1,1)}, all with Q = N (mod 2), and both
    diagonals are 0. G is exactly the mod-2 shadow of (C5) and forgets its 0/1 content: (Q,N) = (3,1) or (2,2)
    satisfies G but not (C5).
 3./4. G is not implied by the separate systems: a relaxed pair (each system solved separately) can violate it. See the
    m = 11 check in s.5. But since Theorem C already contains G, this supplies no information beyond Theorem C.
 5. VERDICT: the Z[C2] route is a STRUCTURAL EXPLANATION, not an obstruction. Freeness of Lambda_3, Lambda_-4 means "the
    two sectors are glued at the prime 2 along Q = N (mod 2)", the parity half of the four-state coupling. Route
    stopped. The 7-adic Proof Obligation 1 is not pursued (already in the C2 repository and automatic there).

## 5. Exact check on the m = 11 analogue  [CHECKED, checks/c17_zc2_glue_bvls.py]
(Odd eigenvalues 4, -5; glue maps 81 E_4 = 45 + 9B_+ - J^ and 243 E_-5 = 108 - 27B_+ + 2J^, odd multiples.)
 - True BvLS (Q, N): A_-^2 + A_- = 20I and B_+^2 + B_+ = 20I + 2J^ hold, Q = N (mod 2); all 242 generators
   u = (A_- - theta')e_i glue to integral theta-eigenvectors w with w_inf even and w_orb = u (mod 2): 0 failures.
 - Relaxed pair (Q' = Q with the two orbits of one cell swapped; N unchanged): both separate identities still hold,
   Q' != N (mod 2) at 144 entries, and the glue fails for 74 of the 242 generators.
So G is genuinely joint relative to the SEPARATE systems, and it is exactly the parity half of (C5).
FINAL: no relation beyond Theorem C. Z[C2] route = structural explanation; STOPPED.
