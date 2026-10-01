# Targeted duplication check (2026-09-30), after the operator's pointers

Sources read (only the cited parts, no repository audit):
 A = Desktop/conway99-involution/notes/NOTE_involution_case.md, sections 2-3;
 B = Desktop/c2_experimental/notes/17_ALLSIB_PREUVE_HUMAINE.md (whole, 117 lines);
 C = same folder, note 18 sections 2-3 and 7-8, note 19 sections 4, 6 bis, 7-12 (targeted greps first);
 D = note 07 (defect lemma, 24 lines).

| My item | Status | Where it already is |
|---|---|---|
| R1 canonical form, D a perfect matching | independently rediscovered | A s.2(a)-(c) |
| R2 local equations (E+-), (P), (Q) | rediscovered | A s.2(d) "orbit-level exact model" |
| R3 B = MM^T + P, P rank-20 GF(2) idempotent | rediscovered (same spectral-multiplicity proof) | A s.3 (their K = Gamma-bar^2); they also give the 2-adic Broue route (L3, L-4 free Z2[C2]-lattices) |
| R4 all-cells family impossible via H^1(KG(7,2)) = 0 + 3/3 count | rediscovered, identical mechanism | B, Theorem 17.1 ("allsib") |
| Lemma G0/G (type-2 partition, labels phi) | rediscovered | C note 18 s.2 (S1 at orbit level, chi_p) |
| Lemma E' (extended cocycle to every orbit avoiding c cup d) | rediscovered | C note 18 "(disj)" |
| (*) 3/3/3/3 count in Lemma H | rediscovered | C note 18 "(int)" |
| Lemma H (overlapping type-2 pair forces two disjoint non-type-2 cells in W) | a correct packaging of (disj)+(int) | not found stated as such; adds nothing to the current frontier (below) |
| Lemma J (a type-2 cell is not surrounded by type-2 cells) | correct | not found stated; subsumed by the certified bound below |
| R9 sign lift linear mod 2 | rediscovered | C note 19 s.12, system L(Q); s.10 minus-orbit parity |
| SAT pass (102/133 solver-level exclusions) | superseded | C: DRAT-certified configurations, human "star lemma" (deg Sigma <= 2), |Sigma| <= 4, full-model DRAT for C4 and P4+K2 |

Frontier in C (as recorded there, not re-verified): the type-2 support Sigma (grids through the fixed
point) has at most 4 cells and maximum degree 2; the full model leaves P5, 2P3, K3, P4 (and smaller)
undecided; the grid-free core Sigma = empty resisted all local probes (<= 22 rows, 15 min).

What H/J genuinely add: short human proofs of two support restrictions, both weaker than the
certified bound |Sigma| <= 4, deg <= 2. They exclude none of the 12 degree-<=2 survivors of C note 19.
One observation not in C as far as checked: in my solver-level unsigned pass the 4-cycle C4 is
UNSAT at the unsigned (Q-stage) level in 0.2 s (core = its 4 type-2 cells), whereas C records C4 as
SAT for the sister-line systems and UNSAT only in the full signed model (495 s, DRAT). Solver-reported,
uncertified; recorded only as a lead.

Status discipline kept: the 102 exclusions are solver-reported, not certified; the 31 unresolved
branches are not solutions; assumption cores were recorded with polarity (type-2 = positive literal,
non-type-2 = negative literal) in data/sat_pass_133_budget20000.json.
