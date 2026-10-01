# Provenance log — blind Constructor / Destroyer protocol (coordinator: main session)

Rules in force: agents are blind to each other during their first interval; only CONCRETE artifacts are
cross-pollinated (Constructor -> Destroyer: explicit partial objects, exact counterexamples, repeated extension
failures, candidate Q,N fragments; Destroyer -> Constructor: proved necessary conditions, certified forbidden
configurations, exact global identities). No interpretations are transmitted. If both agents fall into the same
known basin, the generation is terminated and new agents get a different primitive representation.
Each entry records: who derived it, hypotheses, independent check status, duplication status.

## Generation 1 (launched 2026-10-01)
| Agent | Role | Input | Output folder | Constraints |
|---|---|---|---|---|
| G1-D | Destroyer (NOT-EX) | shared kernel (verbatim) + Destroyer suffix + operating rules | work/agents/gen1_destroyer/ | ~30 tool calls, <=1200-word report, tiny local checks only |
| G1-C | Constructor (EX) | shared kernel (verbatim) + Constructor suffix + operating rules | work/agents/gen1_constructor/ | same |
Operating rules given to both: write only in own folder; do not read work/agents/* of the other agent; no reading of
speculative work notes before deriving; targeted duplication check afterwards (work/FAILURE_MEMORY.md,
work/RESULTS.md, Desktop/c2_experimental/notes, Desktop/conway99-involution/notes); py -3.12 + numpy; one process,
<= 5 min, < 1 GB per check; BvLS m = 11 data available for calibration.

### Artifact ledger (filled when agents return)
| ID | Producer | Statement / object | Hypotheses | Independent check | Duplication status | Transmitted to |
|---|---|---|---|---|---|---|
| C1-A1 | G1-C | No G-invariant (signed) N in S for ~25 groups (PSL(2,7), 2^3:PSL(2,7), AGL(1,7), 2^3:7:3, 2^3:7, 2^7:7(:3), A7, S6, A6, PGL/PSL(2,5), S5xS2, S4xS3, S3wrS2, S5 + 7 sign extensions) | Theorem C (S-level only; no D, no T4) | agent: two independent implementations (symS/sweep, verify_sym); coordinator: NOT re-run | S-level version not in RESULTS/FAILURE_MEMORY; graph-level symmetry exclusions known (DUPLICATION_NOTES 2, LITERATURE 1-2). Basin: extra symmetry (FAILURE_MEMORY row 7). No leverage | pending |
| C1-A2 | G1-C | No G-invariant unsigned support B extends to (B,D) with C3+C4, exhaustive for PSL(2,7), AGL(1,7), A7, S6, A6, PGL/PSL(2,5), S5xS2, S4xS3 (+ sign ext.); capped for 7:3, D7, S3wrS2, S5 | C3, C4 | agent: one implementation (unsigned_all.py); coordinator: NOT re-run | same basin; no leverage | pending |
| C1-A3 | G1-C | Lemma: if B satisfies C4 (with Q = B + 2D) and is invariant under g in W(B7) fixing orbit x, then the coordinate permutation of g fixes the cell of D(x) setwise; large stabilizers force all-type-2 | C4, invariance of B only | coordinator: proof re-derived by hand, correct (kappa_x(t) = 4 - 2[t in c_x] - 2[t in c_D(x)] is pi-invariant) | elementary; consequence of R4/R7 for symmetric B; no leverage | pending |
| C1-A4 | G1-C | Calibration: RRR (spectral/rounding) and tabu (unsigned, exact delta) fail at m = 11 where BvLS exists (best RRR 25.5; tabu residual 9466 even with true D) | — | agent computation; coordinator: NOT re-run | methodological counterexample: heuristic failure is no evidence for NOT-EX (consistent with FAILURE_MEMORY row 9) | pending |
| C1-A5 | G1-C | Spectra of N, Q; vertices <-> Z^7 vectors of norm <= 2; BvLS all 55 D-pairs type 2, N supported on disjoint cells | — | rediscovery | rediscovery (R16(b), model) | — |
| C1-A6 | G1-C | near-miss AGL(1,7)-invariant N (NR = 0, row weight 10), 756 nonzero residual entries in N^2 - N - 12I + H; file nearmiss_AGL17_N.npy | — | agent | — (fragment far from S) | pending |
Coordinator note (G1-C): main effort in known basins (extra symmetry; generic local search). Its open target
"is S nonempty?" is recorded as a statement of the problem, not as an artifact.
| D1-R2 | G1-D | Hodge lemma: for the 99-graph-type complex X = graph + triangles + 4-cycles, Delta_1 = (k+1)I + O, O = +-1 on opposite sides of 4-cycles; Delta_1 >= 3I; H_1(X;Q) = 0 | lambda = 1, mu = 2, k-regular | coordinator: CHECKED on rebuilt BvLS (agents/coord_check_hodge.py): diag = 23, no entries on vertex-sharing edges, values +-1, min eig 3.0 | "Hodge" listed closed (note 22); exact operator identity not found by agent; no leverage (R3: Lefschetz route redundant) | pending |
| D1-R4 | G1-D | All-sibling impossible at m = 7 from C3 + C4 alone (complement-pair parity) | Q-system | agent check_thmA.py | rediscovery (notes 05/17; work R4) | — |
| D1-R6 | G1-D | H_1(X_BvLS; F3) = F3^6, H_1(F2) = 0; Paley(9): 0 for p = 2,3,5,7 | — | agent | new data | pending |
Phase change 2026-10-01: user started a native-language invention phase; generation-1 cross-pollination not executed.
