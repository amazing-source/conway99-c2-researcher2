# One-candidate obligation, second claim: the signed apex/hole system (T1S)

Starting point: Theorem A (ONE_CANDIDATE_T1.md): every type-1 square is in state (a0).
Target of this claim: (a0) => contradiction, using signed per-pair information.

## PRE-REGISTRATION (written before the attempt; not edited afterwards)

### 1. Exact signed configuration forced by Theorem A

Notation: [i,j,+-] = e_i +- e_j (i < j), the positive roots; N_uw in {0,+-1}; the lift of w adjacent to u+ is
-N_uw r_w. Coordinate permutations and sign changes, and switching an orbit, are symmetries of the
system, so without loss:
  a = 1, b = 2, c = 3, W = {4,5,6,7};  x = [1,3,+], y = pi x = [2,3,+];  apex z = [4,5,+].
Forced (Theorem A, Result 1, JOINT_CHECKPOINT_1 (b),(c)):
 - N_xz = -1, N_yz = +1 (apex concordance N_zx N_zy = -x_3 y_3). Lifts: x+ = e1+e3, y+ = e2+e3,
   zeta := z+ = e4+e5; lines {x+, y+, 3+}, {x-, y-, 3-}, {x+, y-, zeta}, {x-, y+, -zeta}.
 - Row of x: star neighbour s in a {1,w}-cell with N_xs = -1, antistar t in a {1,w'}-cell with N_xt = +1;
   two neighbours g, g' in {2,.}-cells whose x+-lifts have opposite signs at 2; six W-cell neighbours
   including z; no neighbour containing 3 or in the cell {1,2}. Row of y: the same with 1 <-> 2
   (star/antistar at 2, two {1,.}-neighbours with opposite lift-signs at 1).
 - B(x) cap B(y) = {z}; (E+-) at (x,y): Y = 0, Z = 1.
 - Hole o: the unique W-orbit other than z adjacent to neither x nor y; each other W-orbit is adjacent
   to exactly one of x, y.
 - (E+-) at (x,z): B_(x,pi z) = 0, exactly one common neighbour u1, discordant (N_(x u1) N_(u1 z) = -1).
   (E+-) at (y,z): B_(y,pi z) = 0, exactly one common neighbour u2, concordant.
 - (E+-) at (x,o), (y,o): Y = Z = 2 - B_(x,pi o), resp. 2 - B_(y,pi o).
 - Second order (unsigned, D(H_1) = 4): (i) o not in B(z), o != pi z; (ii) o in B(z); (iii) o = pi z;
   with the j-counts of ONE_CANDIDATE_T1.md (for (iii): exactly two B-neighbours of z other than x, y
   have j = 2).

### 2. Proposed conclusion: CLAIM T1S

The apex/hole system Sigma_AH has no solution.
Sigma_AH. Unknowns: pi z, pi o and the four signed rows of X = {x, y, z, o} (pi x = y).
 (R)  for u in X: degree 10; profile (P); NR row sum_w N_uw r_w = 0; B_(u,pi u) = 0; symmetry on X.
 (I)  for u != v in X: (E+) and (E-) exactly (they only involve rows in X).
 (Bd) for u in X and w not in X: (E+) and (E-) at (u,w) with every term that is not determined by the
      rows in X dropped (all dropped terms are >= 0). Kept: P_uw, P'_uw, Gamma_uw, Delta_uw, D_uw,
      B_(pi u, w) when pi u is in X, and the common neighbours t in X, counted as concordant
      (N_ut N_tw = +1) or discordant. So P' + Gamma + D + B_(pi u,w) + conc_X <= 2 and
      P + Delta + D + B_(pi u,w) + disc_X <= 2.
 (A0) the configuration of s.1.
(I) and (Bd) use (E+) and (E-) separately: this is signed per-pair information. (Bd) contains the line
decomposition at the edges of x, y, z, o, e.g. "a star edge u-w forces w non-adjacent to pi u".

### 3. Why it would matter

For any feasible candidate with a type-1 square, its rows satisfy Sigma_AH (every equation used is an
equation of (S) + L_N, or an inequality obtained by dropping nonnegative terms). With Theorem A,
T1S gives: no feasible candidate has a type-1 square, n1 = 0 universally. This reduces the grid-free
core to the all-type-0 family (B).
Choice of radius: Theorem A's exclusions of (b) and (a1) used the rows of x, y and one more orbit.
Sigma_AH is the signed analogue at the same radius around the apex and the hole.

### 4. Falsifier

An explicit pi z, pi o and four signed rows satisfying (R), (I), (Bd), (A0). It would show that signed
per-pair information around one type-1 square at radius one leaves enough freedom. It would NOT show
that a type-1 square exists, and it could not be repaired by adding hypotheses to T1S.

### Selection note (disclosed)

While choosing the level I checked the bare row system (R) + (I) + (A0), without (Bd). It has an
explicit solution R0 (Appendix R0, case (iii)). R0 violates (Bd) at one star edge: z-[1,5,+] is a
star edge at 5 while o = pi z is adjacent to [1,5,+]. That is why T1S is registered with (Bd).
Prior: undecided.

### Appendix R0 (bare row solution, violates (Bd))

pi z = o = [6,7,+], pi o = z. Rows (orbit: N):
 x: [1,4,-]:-1 [1,5,+]:+1 [2,6,+]:-1 [2,7,+]:+1 [4,5,+]:-1 [6,7,-]:-1 [4,6,+]:+1 [4,7,+]:-1 [5,6,+]:+1 [5,7,+]:-1
 y: [2,6,-]:-1 [2,7,-]:+1 [1,6,+]:-1 [1,7,-]:+1 [4,5,+]:+1 [4,5,-]:+1 [4,6,-]:-1 [4,7,-]:-1 [5,6,-]:+1 [5,7,-]:-1
 z: x:-1 y:+1 [1,5,+]:-1 [2,6,-]:-1 [1,4,+]:+1 [1,7,+]:+1 [2,4,-]:+1 [2,5,-]:-1 [3,6,-]:+1 [3,7,+]:-1
 o: [1,3,-]:-1 [2,3,-]:+1 [1,5,+]:+1 [2,7,+]:-1 [2,6,-]:-1 [1,7,-]:-1 [1,6,-]:+1 [2,4,+]:+1 [3,4,-]:+1 [3,5,+]:-1
(Checked in checks/c09_apex_hole_system.py.)

====================================================================================================
## OUTCOME (written after the attempt; the pre-registration above is unchanged)

Verdict: CLAIM T1S is FALSE at the pre-registered level. Sigma_AH has an explicit solution K3 (case (iii)),
verified by two independent checkers: checks/c09 (orbit level: (R), (I) with (E+) and (E-) separately,
(Bd), (A0)) and checks/c10 (lift level: lambda = 1, mu = 2 between the eight lifts of x, y, z, o and every
vertex, using only adjacencies the four rows determine). Output: data/c09_c10_apex_hole.txt.
No search was run: every configuration was written by hand, with its signs solved by hand from the linear
balance equations; the scripts only verify.

### Counterconfiguration K3 (case (iii): the hole is the apex's partner, o = pi z)

 x = [1,3,+], y = [2,3,+] = pi x, z = [4,5,+], o = [6,7,+] = pi z.
 x: [1,6,+]:+1 [1,4,-]:-1 [2,5,+]:+1 [2,7,-]:-1 z:-1 [6,7,-]:-1 [4,6,+]:+1 [4,7,+]:-1 [5,6,-]:+1 [5,7,+]:-1
 y: [2,7,+]:+1 [2,6,-]:-1 [1,6,-]:+1 [1,7,+]:-1 z:+1 [4,5,-]:-1 [4,6,-]:-1 [4,7,-]:+1 [5,6,+]:-1 [5,7,-]:-1
 z: x:-1 y:+1 [1,6,+]:-1 [2,7,+]:+1 [1,4,+]:+1 [1,5,-]:+1 [2,4,+]:-1 [2,5,-]:-1 [3,6,+]:+1 [3,7,+]:-1
 o: [1,6,+]:+1 [2,7,+]:+1 [4,6,+]:-1 [5,7,-]:+1 [1,2,+]:-1 [1,2,-]:+1 [1,3,-]:-1 [2,3,-]:+1 [3,4,+]:+1 [3,5,+]:-1
Shared neighbours: u1 = [1,6,+] (x and z; x's antistar at 1; also an apex of {z,o}), u2 = [2,7,+] (y and z;
y's antistar at 2; the other apex of {z,o}), p1 = [4,6,+] (x and o; o's star at 6), p2 = [5,7,-]
(y and o; o's star at 7). Every W-orbit other than z, o is adjacent to exactly one of x, y.

### The attempt, in order (all disclosed)

 R0 (selection): bare rows; fails (Bd) at the star edge z-[1,5,+] (o adjacent to it). Signed obstruction.
 K1: fails at the cell-mate pair (z, kappa z): o adjacent to kappa z. Unsigned obstruction (lemma L1).
 K2: fails (E+) at (x, u2) with u2 = [1,7,-] in a {1,.}-cell. Signed obstruction (lemma L3).
 Two further designs were abandoned before rows were written: in each, three of the hole's special
 neighbours had forced equal signs at one coordinate (1, resp. 2 and 4), so o's NR row could not balance.
 K3: all constraints satisfied.

### Forced relations found on the way (PROVED HERE; not pursued further)

For a type-1 square in state (a0), normalized as in s.1:
 L1 (unsigned; case (iii)). The hole is not adjacent to kappa z. [(Q) at (z, kappa z): a neighbour of
    kappa z in {x, y} is a common neighbour, so beta = 0.]
 L2 (unsigned; case (iii)). An apex of the square {z, o} that is adjacent to x or y has support disjoint
    from supp z. [(Q) at (z, a): beta = 1 gives (B^2)_za = 1 - s(z,a).]
 L3 (signed; all cases). If the y-z common neighbour u2 lies in a {1,.}-cell, then N_(y,u2) = N_(z,u2) = +1.
    Symmetrically, if the x-z common neighbour u1 lies in a {2,.}-cell, then N_(x,u1) = +1, N_(z,u1) = -1.
    [(E+) at (x, u2): Gamma = 1 and beta = 1 leave no concordant common neighbour, so z is discordant.]
 L4 (signed; case (iii)). If o is adjacent to w in B(x) (w not in B(z)) sharing k in {4,5} with z, then
    N_(x,w) = (r_w)_k; if w is in B(y), then N_(y,w) = -(r_w)_k. [(E+-) at (z, w) with beta >= 1.]
 L5 (signed; case (iii)). o is not adjacent to a star neighbour of z, and z not to a star neighbour of o.
    [star edges have beta = 0 by (E+-); the unsigned (Q) alone allows beta = 1 there.]
These restrict where the shared neighbours can sit. None of them fixes more than the relative signs of
the shared neighbours.

### Exactly why the signs leave enough freedom

At radius one the rows of x, y, z, o interact only through their shared neighbours: z (x,y), u1 (x,z),
u2 (y,z), the two apexes of {z,o}, p1 (x,o), p2 (y,o). The pair equations (I) fix only the concordance
of each shared neighbour: six sign relations between products of two entries. The three relations at
(x,o), (y,o), (z,o) chain the hole's four special signs into one free sign. Every other entry of the
four rows appears only in its own NR row (a +-1 balance per coordinate) and in the (Bd) inequalities.
Those inequalities forbid a few adjacencies (L1, L2, L5) and fix a few signs relative to coordinates
(L3, L4), but no chain of them closes. In K3 the special neighbours sit on distinct coordinates
(1,6 / 2,7 / 4,6 / 5,7), so each NR balance keeps at least two free entries. The failed designs failed
exactly when three forced-equal entries met at one coordinate. That is a placement condition, not an
obstruction.

### Reassessment of type 1 as the pressure point

 - Theorem A came from first-order tightness: the defect 2 is used up by the hole. K3 shows that the
   signed per-pair system at radius one around the apex and the hole is not tight.
 - Radius two needs the rows of the shared neighbours and of the neighbours of z and o (about twenty more
   rows). That is a search, and at that scale the repository's local probes for Sigma = empty were
   inconclusive (note 19 s.7, read earlier). It cannot be done by hand, and I have not started it.
 - Even a full kill of (a0) would only give n1 = 0. The grid-free core would then be family (B), where
   every square is type 0 and the defect method has slack everywhere except configuration C1.
 - Status: the type-1 line is STALLED at radius one. Missing implication: a signed relation at
   radius >= 2 around a type-1 square. The certificate that radius one is not enough is K3.
 - Conclusion: type 1 is not the right pressure point for EX. It was the right place to find rigidity
   (Theorem A); what remains there is detail around an optional object.
