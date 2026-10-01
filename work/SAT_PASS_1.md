# First (and only) SAT diagnostic pass over the 133 support classes

Status labels: CHECKED COMPUTATION (solver-reported; NO proof certificates produced yet).
Nothing here is used as a theorem until certified.

## What was run (exact, bounded)

- Model: the UNSIGNED system only, encoded exactly (work/code/unsigned_sat.py): B symmetric 0/1,
  D a perfect matching disjoint from B, (Deg) degree 10, (P) profile, (Q) all 861 pair equations.
  No signs, no N^2 equation beyond (Deg), no extra lemmas. A class = assumptions on the 21
  cell-diagonal D-variables (type 2 iff the cell is in Y).
- Encoder validation (work/checks/c04): 3 planted instances (random (B, D), right-hand sides computed
  from them): planted assignment is a model; adding one B-edge and rewiring D are both refuted; the
  solver finds a B for the planted D. Theorem checks: Y = all cells (R4) UNSAT in 0.4 s; the extremal
  class K(U)+V (Lemma J) UNSAT in 0.2 s.
- Pass (work/checks/c05, output work/data/sat_pass_133_budget20000.json): CaDiCaL 1.5.3 via PySAT
  (installed in an isolated scratchpad venv), one process, 20 000 conflicts per class, global guard
  270 s; total 272 s. Classes processed in order of decreasing n2 = |Y|.
- Post-analysis without new solver calls (work/checks/c06, output work/data/core_analysis_pass1.txt):
  failed-assumption cores canonicalised under S7; any class containing an image of a core
  (type-2 part inside Y, non-type-2 part inside X) is excluded as well.

## Outcome

    UNSAT 99, UNKNOWN (budget) 29, NOT RUN (guard) 5;  no SAT model.
    + 3 unresolved classes contain a known core (48, 88, 91)  ->  102 excluded, 31 unresolved.

 - Every class with n2 >= 7 is excluded. The unresolved classes have n2 <= 6.
 - Cores are small. 73 distinct cores up to S7. The smallest ones (all with EMPTY non-type-2 part,
   i.e. "these cells cannot all be type 2", whatever the other cells are):
       K3 + K2   {12,13,23,45}        (from class 115)
       C4        {12,13,24,34}        (from class 119)
       C5        {12,13,24,35,45}     (from class 110)
       K1,4 + K2 {12,13,14,15,67}     (from class 103)
   The other 5-cell cores printed contain C4 or K3+K2, so they are not minimal. Minimality of the four
   above was NOT tested (it would need further solver calls).
 - The 31 unresolved classes (Y as a graph on [7], up to S7):
     n2=6: {12,13,14,15,23,26} {12,13,14,23,25,36} K1,6 {12,13,14,15,26,37} spider{12,13,14,25,36,47}
     n2=5: {12,13,14,15,23} {12,13,14,23,25} {12,13,14,15,26} {12,13,14,25,26} {12,13,14,25,36}
           {12,14,15,23,36} {12,13,14,25}+{67} P6={12,13,24,35,46} P5+K2={12,13,24,35}+{67}
     n2=4: {12,13,14,23} K1,4 {12,13,14,25} K1,3+K2 P5 P4+K2 2P3 P3+2K2
     n2=3: K3 K1,3 P4 P3+K2 3K2;   n2=2: P3, 2K2;   n2=1: K2;   n2=0: empty.
   All are forests except those containing exactly one triangle with all other edges touching it.

## What the pass teaches (structural)

1. The type-2 package is decisive whenever type-2 cells are numerous or overlap in cycles: every
   support with n2 >= 7, and every support containing K3+K2, C4, C5 or K1,4+K2 (as found), dies,
   usually in < 0.1 s. So "type-2 rigidity" is strong and local: short cycles of type-2 cells and a
   triangle/star with a disjoint type-2 cell are incompatible with the unsigned equations.
2. Where it fails: sparse Y (trees, a triangle with pendants, <= 6 cells). These instances are
   expensive (budget exhausted at 20k conflicts). They are not "almost excluded": they approach the
   unrestricted quotient problem. The limiting class n2 = 0 is exactly the general case, where the
   type-2 package (G0, G, E', H, J) says nothing at all.
3. Why the constraints do not separate the survivors: all leverage comes from (i) the partition
   B(c^0) + B(c^1) = Disj(c) at type-2 cells and (ii) parity/cocycle relations along pairs of
   type-2 cells. With few type-2 cells the number of such relations is small, while the unknown part
   (pi on the non-type-2 orbits and B among them) is almost the whole quotient problem. Nothing in
   the unsigned model couples the non-type-2 squares (types 0 and 1) rigidly; they have no analogue of
   G0(iii) (their neighbourhoods only "almost" partition the cells avoiding the square's 3 or 4
   coordinates), and no three of them have pairwise disjoint coordinate sets (3+3+3 > 7), so there are
   no cocycle triangles among them.
   Deciding those classes therefore needs either (a) a rigidity package for type-0/1 squares or
   (b) the sign equations (NR = 0, N^2 = N + 12I - RR^T), which the unsigned model ignores.
4. Consequence (conditional on certificates): every feasible (N, D) has n2 <= 6 and its type-2 graph Y
   is one of the 31 listed S7-classes. This is a coverage-complete reduction of type (ii), but the
   remaining cases include the general case n2 = 0, so EX is not decided.

## Not done (deliberately)

 - No second pass, no larger budgets, no enriched model, no signed N.
 - No DRAT certificates yet: only needed if these exclusions are to be cited as results.
