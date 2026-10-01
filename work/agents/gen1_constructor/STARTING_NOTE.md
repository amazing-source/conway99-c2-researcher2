# gen1_constructor -- starting note (written before reading any project notes)

Target: EX = exists integer symmetric zero-diagonal (Q,N), 42x42, with C2a,C2b,C3,C4,C5
(MODEL.md conventions). Role: constructor. T4 used only as stated (working lemma).

## Own derivations from the kernel (PROVED HERE, elementary)

D1 (anti-invariant / invariant split). A^- = [[-I7, R^T],[R,-N]] satisfies (A^-)^2+A^- = 12 I49
    iff R^T R = 12 I (true), NR = 0, N^2 = N+12I-H. Spectrum of N: 0^7, 4^15, (-3)^20;
    G4 := 4N+12I-H satisfies G4^2 = 28 G4 (rank 15, diag 10).  [probably known basin]
D2 (ball labelling). Vertices <-> vectors of Z^7 of norm <= 2: infinity = 0, inner = +-e_t,
    exterior = the 84 roots of D7 (orbit x <-> +-r_x), sigma = negation. All adjacencies at
    0 and +-e_t are Hamming H(7,3) adjacencies (difference = +-e_t mod 3) restricted to the ball.
    Only the 84-vertex exterior graph X (negation invariant) is unknown.
D3 (lines). Every edge lies on one triangle ("line"). Exterior vertex v = a e_i + b e_j lies on
    2 apex lines {v, a e_i, w1}, {v, b e_j, w2} and 5 pure lines (all-exterior). In a pure line
    the three roots have pairwise no common nonzero coordinate with equal sign.
D4 (star-count law). For exterior v and inner p: |N_X(v) cap star(p)| = 1 if p in {a e_i, b e_j,
    -a e_i, -b e_j}, else 2 (this is C4 row by row).
D5 (D-squares). D(x)=y iff {v_x,-v_x,v_y,-v_y} is a sigma-invariant induced 4-cycle; 21 of them.
    type(x) := |c_x cap c_y| in {0,1,2}. Type 2 iff both apex partners of v_x are "grid"
    (a e_i - b e_j and -a e_i + b e_j), iff a 3x3 grid through infinity on lines i,j.
D6 (BvLS shadow, prediction to check on data). In the m=11 analogue (Golay coset graph), every
    D-pair is type 2 and exterior vertices in cells meeting in one coordinate are never adjacent,
    so N is supported on disjoint-cell pairs only and each pure line has pairwise disjoint
    supports plus a well-defined "direction" (the coordinate t with v +- e_t decoding to the
    other two points).
D7 (all-grid reduction for m=7). If all 21 D-pairs are type 2 then pure lines have pairwise
    disjoint supports covering 6 coordinates; the 7th is the line's direction; every v has
    exactly one pure line in each direction t not in supp(v).

## Candidate constructive mechanisms
M1 generate N in S by a structured method, then test L_N (T4: empty or one matching).
   Success = witness. Needs a generator for S; S nonemptiness itself is open.
M2 "directional decoding" ansatz (D7): a finite design problem per direction t
   (negation-invariant partition of 60 signed pairs on [7]\{t} into 20 transversal triples)
   plus lambda/mu. Exact and small. Needs: not already excluded by type-2 results.
M3 mixed-type generalisation of M2: lines with a direction plus apex defects; parameterise
   rows by (apex types, directions) and extend row by row.
