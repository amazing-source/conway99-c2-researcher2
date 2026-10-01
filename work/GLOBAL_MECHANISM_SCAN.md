# Search for a different global one-candidate mechanism for (B, D, P) (after P7)

Requirement: a statement about one arbitrary feasible (B, D, P) that is global (not a neighbourhood), not automatic,
not already known or closed, and with a path to excluding something unresolved.

Not to duplicate (repository status: note 22 table; PROOF_SKELETON_C2 header):
 closed: genus / Brown / discriminants; moments, SOS, Lasserre; interlacing; local Delsarte; Hodge.
 active: rank-24 envelope + Borcherds classification (156 lattices; skeleton header: 93 excluded, 62 open, 1 partial).

| Candidate | Test | Verdict |
|---|---|---|
| Arithmetic invariants of the integral lift (7-rank parity P7; F3 discriminant of im P; 2-, 3-ranks) | LATTICE_PARITY_P7.md | known (note 10), automatic for (B,D,P) by Lemma 2.1 + Thm 3.1 |
| Fixed-point parity of sigma on substructures whose counts the parameters fix | checks/c11 (pentagon formula validated by brute force on Paley(9)) | automatic: vertices 99/1, edges 693/7, lines 231/7, induced 4-cycles 2079/21 (the 21 D-squares), induced pentagons 33264/0 (a sigma-invariant pentagon would need the chord i+ i-) |
| Same parity on 3x3 grids | sigma-invariant grids = grids through v0 = the n2 type-2 cells | n2 = G (mod 2), G = number of grids. G is not fixed by the parameters, and sigma gives no second count of it. Leverage only with an independent value of G mod 2 (if G were always odd, Sigma = empty and every even-|Sigma| class would die). No route found |
| Global sum of the local defect data (Wilbrink-Brouwer over all 21 squares) | exact computation: sum_S sum_q C(j-1,2) = 48 n0 + 45 n1 + 44 n2 - 924 = 4 n0 + n1 | collapses to the per-square defects (tautological) |
| GF(2) consistency of the sign lift (R9), universal combinations | (L2)M combined with (L1) reduces to M(U - U') = 0, U - U' = diag(8 - 2i) | automatic; further left-kernel vectors depend on B (not universal); repository rates "linearized parity" open and has run propagators on subsystems |
| Global sign bookkeeping, trace identities | F5, F3 | tautological (earlier) |

Conclusion: no global one-candidate mechanism with demonstrated leverage found. Two missing inputs would give
leverage: an independent (combinatorial) computation of a 7-rank (note 10 s.4), or an independent value of the
number of 3x3 grids modulo 2. I have no route to either.
