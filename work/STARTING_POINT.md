# Starting point (Researcher 2, written before reading DUPLICATION_NOTES.md)

Basis used: MODEL.md, AUDIT_STATUS.md, TASK.md only. Every claim below marked
PROVED HERE is derived in this note from the model; nothing is taken from memory.

## 1. Target

    EX := exists a complete symmetric 42x42 N in S such that L_N is nonempty.

Positive: one explicit (N,D), then a directly verified 99x99 A. Negative: every N in S.
(Given T4 and the reconstruction, EX <=> some srg(99,14,1,2) has an involution fixing exactly one vertex.)

## 2. Fixed / unknown / status

- Fixed: R (rows = the 42 positive roots e_i +- e_j of D7, i<j), M=|R|, chi.
- Unknown: N (and D, which T4 makes a function of N).
- T4: working lemma, independently hand-reviewed, not formally verified.
  Reconstruction: reviewed. F0: external input, not checked by that reviewer; not used below.

## 3. Initial consequences (PROVED HERE unless labelled)

(a) Canonical form. In an srg(99,14,1,2), fix v0; its 14 neighbours form 7 edges ("inner edges").
Each of the 84 non-neighbours has exactly two inner neighbours, in different inner edges, and each
such pair has exactly one common non-v0 neighbour; so non-neighbours <-> the 84 roots
s e_i + t e_j of D7 (inner vertex (i,s) ~ root r iff r_i = s). If an involution s fixes only v0 and
swapped two inner edges, the root joined to x_(i,+) and s(x_(i,+)) would be fixed; so s swaps the
ends of every inner edge and acts on roots as r -> -r. r is never adjacent to -r (their common
neighbours come in s-orbits of size 2, so lambda would be even).

(b) Odd part. With Ntil = [[I_7, -R^T], [-R, N]] (49x49):
N in S (matrix part) <=> Ntil^2 = Ntil + 12 I_49 (uses R^T R = 12 I_7).
Spectrum N: 4^15, -3^20, 0^7 with ker N = col R exactly. Diagonal of N^2 gives: B=|N| is 10-regular.
Ntil + 3I = 7 P_4 is an integral PSD Gram matrix of rank 22 (7 vectors of norm 4, 42 of norm 3).

(c) Even part. Q = B + 2D has spectrum 12^1, (-2)^6 (on col M minus 1), 3^20, (-4)^15.

(d) Meaning of D (graph side). For a positive root u, u and -u are non-adjacent, so they have exactly
2 common neighbours, forming one s-orbit {w,-w}; D_uv = 1 iff v = |w| =: pi(u). The 4-cycles
Sq(u) = {u, pi(u), -u, -pi(u)} partition the 84 exterior vertices into 21 squares.

(e) Local "sum = 2" form of S + L_N (given D a matching). For u != v, with
P=[N=1], P'=[N=-1], Y_uv=#{x: N_ux N_xv = 1}, Z_uv=#{x: N_ux N_xv = -1},
Gam_uv = #coords where r_u,r_v agree (nonzero), Del_uv = #coords where they disagree:

    (E+)  Y + P' + Gam + B_(u,pi v) + B_(pi u,v) + D = 2
    (E-)  Z + P  + Del + B_(u,pi v) + B_(pi u,v) + D = 2

(E+)-(E-) is the off-diagonal of N^2 = N + 12I - RR^T; (E+)+(E-) is BD+DB+D=E. These are lambda/mu for
the pairs (u,v) and (u,-v).

(f) Star matchings. For each inner vertex (i,s) the 12 roots with r_i = s are perfectly matched by
H (lambda = 1 at (i,s)). So each root has exactly 2 "star" neighbours, the other 420 exterior edges
split into 140 edge-disjoint triangles, 5 through each root.

(g) Types. t(u) = |supp u  cap  supp pi(u)| in {0,1,2}. At (u,pi u): Y + Z = 2 - t(u).
Traces give: #triangles of B = 126 + sum_u t(u), and (#positive - #negative) signed triangles = 70.
Per vertex: sum over B-neighbours v of |supp u cap supp v| = 4 - 2 t(u).

## 4. Candidate mechanisms

M1 Local square/star geometry. Use (d)-(g) to force the structure of pi and of B near each square
(e.g. restrict the type distribution of pi, or classify cell-level patterns).
Effect on EX: a contradiction gives not-EX; otherwise a reduction. Still needs: a coverage lemma
making the reduced family exhaustive, and then a bounded complete search or a further proof.

M2 7-modular lattice of the odd part. (Ntil - 4I)(Ntil + 3I) = 0, so K = ker(Ntil - 4I) cap Z^49 has
7-elementary discriminant (rank a = 7-rank of Ntil + 3I). Combine with the even part / full graph.
Effect: a genus or rank contradiction gives not-EX. Still needs: an invariant that actually couples
to the combinatorics (so far the constraints are internally consistent).

M3 Symmetry-ansatz positive construction. Impose an extra automorphism tau of the coordinate
structure (tau in W(B7), commuting with s, fixing v0), solve the reduced exact system in a bounded run.
Effect: an explicit verified graph gives EX. Failure excludes only that ansatz. Still needs: check which
automorphism orders are already excluded (literature, EXTERNAL INPUT) before spending effort.

Tentative choice: M1, because (e)-(g) are exact, local and immediately testable, and they tie T4's D to
the combinatorics of N; its first goal is to determine what the type of pi can be.
