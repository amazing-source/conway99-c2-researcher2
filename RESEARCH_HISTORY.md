# Research history — Conway 99-graph, involution branch C2 (Researcher 2), 2026-09-30 to 2026-10-01

Target (MODEL.md): EX := exists N in S such that L_N is nonempty. T4 used as a working lemma; F0 never used.
**Status at the end of this record: EX is OPEN.** No witness, no universal contradiction.

The task packet (MODEL.md, TASK.md, AUDIT_STATUS.md, DUPLICATION_NOTES.md, CLAUDE.md, reference/, provenance/,
code/, data/) is kept unchanged. All research output is under `work/`. The master indexes are:
`work/RESULTS.md` (R1-R18), `work/FAILED_ATTEMPTS.md` (F1-F10), `work/FAILURE_MEMORY.md` (closed basins, rows 1-19),
`work/CHECKPOINT.md` (dated checkpoints).

## Phase 1 — starting point, calibration, type-2 rigidity, unsigned search (2026-09-30)
- `work/STARTING_POINT.md`, `work/LITERATURE.md`. Checks c01 (fixed identities), c02 (Kneser KG(7,2) H^1 = 0).
- BvLS m = 11 calibration (`work/checks/c03_bvls_m11.py`, data `work/data/bvls_m11_*.npy`).
- R1-R5: canonical form of D, local form of S and L_N, mod-2 structure, all-cells family empty (R4), 3|4 obstruction.
- R6 / `work/LEMMA_H.md`: type-2 rigidity package (G0, G, E', H, J). R7: support classification (C code in
  `work/code/classify_*.c`). R8 / `work/SAT_PASS_1.md`: unsigned SAT diagnostic (solver-reported, no certificates).
- F1 (simulated annealing), F2 (symmetry ansatz), F3 (trace identities), F4 (sparse SAT) recorded as failures.
- `work/DUPLICATION_CHECK.md`: R1-R4, G0, E', R9 are rediscoveries.

## Phase 2 — joint signed/unsigned system (2026-09-30)
- R9: sign lift linear mod 2. R10 / `work/JOINT_CHECKPOINT_1.md`: Theorem S (line trichotomy star/apex/E*,
  star-sign rule, apex concordance, global sign counts, Lemma CM). F5: global sign bookkeeping is tautological.
- R11 / `work/TERNARY_VERIFICATION.md`, `work/RECONCILIATION_2.md`, `work/OBLIGATION_RIGIDITY.md` (sign rigidity (R), open).

## Phase 3 — one candidate (B, D, P) (2026-10-01, night)
- R12 / `work/ONE_CANDIDATE_T1.md`: Theorem A (type 1 => state (a0)), checks c08.
- R13 / `work/ONE_CANDIDATE_T1S.md`: claim T1S false at radius one (explicit configuration K3, checks c09/c10).
- R14 / `work/LATTICE_PARITY_P7.md`: 7-rank parity — proved, but a rediscovery of c2_experimental note 10.
- R15 / `work/GLOBAL_MECHANISM_SCAN.md`: no global one-candidate mechanism with leverage (checks c11).

## Phase 4 — object rounds (2026-10-01)
- `work/OBJECT_ROUND_1.md`: objects Om1-Om5 screened; all killed (Om5 closed as a compression), c12 microscope on BvLS.
- `work/THEOREM_C.md` (FROZEN): EX <=> integer (Q,N) with C1-C5 (four-state coupling); reformulation only.
- `work/OBJECT_ROUND_2.md`: four-state path tables; projection kernel (hidden signs delta); consistency laws K0-K7.
- `work/R2_OMEGA1_USEFULNESS.md`: R2-Om1 genuinely joint (verified Q-level counterconfiguration, checks c13/c14)
  but a rediscovery of c2_experimental note 39. R16, R17.

## Phase 5 — overlapping structures (2026-10-01)
- `work/OVERLAP_EXPLORATION.md`: self-overlap of the quotient (twisted cycles), positive-triangle pseudo-surface P,
  bridge graphs G_x with phase alpha/beta, square necklace (checks c15/c16 on BvLS: P = 165 positive K4s).
  Minimal overlaps of pairing states: all nine combinations realizable; representation stopped. R18.

## Phase 6 — blind Constructor / Destroyer agents (2026-10-01)
- `work/agents/PROVENANCE_LOG.md`; outputs in `work/agents/gen1_constructor/` and `work/agents/gen1_destroyer/`.
- Constructor: symmetric N in S excluded for ~25 groups (S level); heuristic search fails even at m = 11.
- Destroyer: Hodge lemma (Delta_1 = (k+1)I + O >= 3I; checked independently, `work/agents/coord_check_hodge.py`);
  Lefschetz/homology route redundant; H_1 data for BvLS.

## Phase 7 — native-language phase (2026-10-01)
- `work/native/NATIVE_REPRESENTATIONS.md`, `work/native/BASIN_ALERTS.md`: port graphs (exact admissible-row counts
  930336 / 155904 / 22176, m01), link involutions and twist (forced twist at m = 7), debt ledger (no order defect).

## Phase 8 — determinacy of Representation B (2026-10-01)
- `work/native/B_DETERMINACY.md`: R0 = (D, 14 coordinate pairings) does NOT determine the disjoint-cell layer.
  1257 realizations at one twisted link (m02/m03); verified minimal pair differing in 3 relations (m04);
  Lemma P: the sign freedom of a row with fixed support is exactly a union of alternating closed trails.
  Refinement collapses to "unsigned layer + phases", i.e. the open sign-rigidity question.

## Reproducibility
Python 3.12 + numpy; every check script states its exact question and resource bound in its header.
C sources in `work/code/` (compiled binaries are not tracked). Checks run from `work/` (e.g. `py -3.12 checks/c16_bridge_graph_bvls.py`).
