# CHECKPOINT (2026-10-01, after the lattice-parity test)

Target EX: OPEN. No branch excluded, no witness.

Lines:
 - Type-1 / apex / triangle line: CLOSED (operator decision). Kept: Theorem A (R12), T1S counterconfiguration K3
   and lemmas L1-L5 (R13).
 - Global lattice parity: STOPPED. P7 (rank_F7(N - 4I) even) proved, = c2_experimental note 10 s.3.4, automatic for
   every integral solution, excludes nothing (R14, LATTICE_PARITY_P7.md).
 - Different global one-candidate mechanism: scan in GLOBAL_MECHANISM_SCAN.md (R15). Nothing with leverage. The two
   inputs that would give leverage: an independent computation of a 7-rank, or of the number of 3x3 grids mod 2.
Secondary material kept: OBLIGATION_RIGIDITY.md, TERNARY_VERIFICATION.md. Frozen: type-2 work, JOINT_CHECKPOINT_1.md.
Not duplicated: the repository's rank-24 envelope / Borcherds line and its closed genus/moment/interlacing lines.

Exact remaining implication for EX or not-EX: existence of a complete unsigned pair admitting the F3 projector.

## Update 2026-10-01 (object round 1, protocol of 2026-10-01)
Object round 1: Om1-Om4 killed, Om5 screened in part, nothing selected, nothing pre-registered
(OBJECT_ROUND_1.md, F9, R16, FAILURE_MEMORY.md). Countable progress: one counterexample to a mechanism (BvLS
refutes m-uniform low-degree identities in Z and N + DND). EX: OPEN.

## Update 2026-10-01 (object round 2 and R2-Om1 usefulness test)
Om5 closed as compression/repackaging (OBJECT_ROUND_1.md s.3). Theorem C frozen (THEOREM_C.md; class C).
Round 2: projection analysis complete (OBJECT_ROUND_2.md s.5-9); objects R2-Om1..5 screened; R2-Om1 survived
screening, then closed by its usefulness test (rediscovered: c2_experimental note 39; Q stage does not imply it
locally; excludes nothing). No object alive. EX: OPEN.

## Update 2026-10-01 (overlap exploration after Round 2)
OVERLAP_EXPLORATION.md: where the orbit quotient forces self-overlap (twisted cycles); positive-triangle pseudo-surface
P; bridge graph G_x at each sigma-pair with phase alpha/beta and the pairing type of type-0 orbits; square necklace.
New representations (derived; m-uniform parts checked on BvLS, c15/c16). No law, no exclusion. EX: OPEN.
Bridge-graph pairing states: all nine combinations realizable on every minimal overlap (OVERLAP_EXPLORATION.md
s.10); no pairwise law; representation stopped (FAILURE_MEMORY row 19).

## Update 2026-10-01 (native-language phase)
native/NATIVE_REPRESENTATIONS.md: R-A port graphs (exact row counts 930336 / 155904 / 22176 per partner type),
R-B link involutions and twist (forced twist at m = 7 = the all-sibling theorem), R-C debt ledger (no
order-of-extension defect for raw extension). Mostly rediscovery or no leverage. EX: OPEN.
Representation B determinacy (native/B_DETERMINACY.md): R0 = (D, 14 pairings) does NOT determine the disjoint layer
(1257 realizations at one twisted link; verified minimal pair differing in 3 relations = a sign flip on an
alternating triangle). Lemma P: sign freedom of a row given its support = alternating closed trails. Refinement
collapses to "unsigned layer + phases" = the known sign-rigidity question. B does not compress.

## Update 2026-10-01 (Z[C2]-freeness redundancy test)
Freeness of Lambda_3, Lambda_-4 is equivalent, given the separate systems, to Q = N (mod 2) (R19), the parity half of
(C5); checked on BvLS with a relaxed counterexample (c17). No new information; route stopped. EX: OPEN.

## Update 2026-10-01 (twist programme, all other routes frozen)
Atomic twist = cherry move. Interaction and closure laws were derived (twist/TWIST_CALCULUS.md, checks t00/t02/t03).
Most of it is a rediscovery of the C2 dense-side analysis (§8, §14, §19, §24, §32). New: covering density 8/(m-3),
the leakage capacity law (BvLS extremal), BvLS's coordinate-indexed odd eigenspace, and 7 | tau when K = 0.
Neither target theorem was obtained. EX: OPEN.

## Update 2026-10-01 (resource needed for the odd 3-eigenspace)
Derived exact multiplicities d = 6 + d'_S and d' = 1 + d_S, the twist slacks, and the leakage window
(twist/ODD_EIGENSPACE_RESOURCE.md, R21; check t04). Exact odd 3-eigenvectors cost twist, and leakage competes with
them. At d = 6 the comparison with the capacity bound gives only tau >= 3, which is too weak. The missing datum is
the placement of the doubling supports in the flat cherries' complementary 4-sets. Stopped as instructed. EX: OPEN.
