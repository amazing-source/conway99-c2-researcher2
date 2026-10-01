# C2: exact ternary signing, integer capacity bounds, and one excluded lifting family

Research continuation, 30 September 2026.

**Status: DERIVED HERE, with proofs. No independent referee or Lean verification has reviewed this note. No priority claim is made.** The bounded checks are implementation and arithmetic controls, not a proof that C2 is empty. No new envelope or rank-17 pair is claimed excluded.

## 0. Main outcome and its limitation

A hypothetical C2 graph supplies a particular orthogonal projector over F_3. Conversely, after two explicit support-capacity tests, the centered lift of such a projector satisfies the **entire integer signed system**, not merely its congruences. The exact matching-completion test can then be applied.

This produces an exact alternative formulation of C2. It does not solve that formulation. A second result below rules out one entire family of projectors, allowing all its nonsymmetric lifts, by a hand argument. There is no proof that every possible projector belongs to that family.

The construction avoids the unsupported inference “a new representation must make the search cheap.” No computational speedup is asserted.

## 1. Fixed objects, unknowns, and dimensions

There are 21 cells c={i,j}, 1<=i<j<=7, each with two indices c+ and c-. The 42-by-7 integer matrix R has rows

    r_(ij,+)=e_i+e_j,    r_(ij,-)=e_i-e_j.

Put M=|R| entrywise, H=RR^T, K=MM^T. Throughout, J_(a,b) is the all-ones a-by-b matrix, and unqualified I,J are 42-by-42. Then

    R^T R=12I_7,  M1_7=2 1_42,
    M^T1_42=12 1_7,  M^T M=10I_7+2J_7.

A complete signed candidate is a symmetric matrix N with diagonal zero and entries 0,+1,-1 satisfying

    NR=0,
    N^2=N+12I-H.                                      (S)

Write B=|N|. The diagonal of (S) gives B1=10 1. A double matching D is a symmetric permutation matrix with zero diagonal, disjoint from B. The ordinary quotient Q=B+2D must satisfy

    QM=4J_(42,7)-2M,
    Q^2+Q=12I+4J-K.                                   (O)

The exact orbit model in the supplied handoff reconstructs a graph from (S), (O), and the entry/matching conditions, via a=(Q-N)/2 and b=(Q+N)/2. The exterior block is [[a,b],[b,a]]. Root labels supply the remaining incidences. This normalized model covers the whole C2 branch conditional on the separate one-fixed-point theorem cited in the handoff.

For a provisional sign matrix define, over Q,

    T=2J_(42,7)-M-BM/2,
    E=(8I+4J-K-B^2-B)/2.                               (1)

Every genuine matching completion satisfies DM=T and BD+DB+D=E. Therefore every row of T is an actual row of M and E is entrywise a nonnegative integer.

These are the two **capacity tests** used below:

    (T-cap) each row of T is binary of weight 2;
    (E-cap) E is entrywise nonnegative and integral.

Because all 21 distinct binary weight-2 rows occur in M, the first test is exactly the prescribed-target-cell test, without assuming reciprocal partners exist. The second test is necessary, not sufficient, for a matching.

## 2. Lemma: a bounded residue window

**Lemma 2.1.** Let N be symmetric, diagonal zero, with entries 0,+1,-1. Suppose it satisfies

    NR=0 mod 3,
    N^2-N-12I+H=0 mod 3,                              (2)

and passes (T-cap), (E-cap). Then it satisfies (S) over the integers.

### Proof: linear row relations

From the definition of T,

    BM=4J_(42,7)-2M-2T.

Thus every entry of BM is an even integer at most four. It is nonnegative because B,M are nonnegative. Each entry of NR is a sum of (BM)_(u,i) signed units. It is consequently even and lies in [-4,4]. By (2) it is divisible by three. The only multiple of six in that interval is zero. Hence NR=0 over Z.

Also T1=2 1 and M1=2 1 imply

    2 1 =14 1-2 1-B1,

so B1=10 1.

### Proof: diagonal quadratic relations

Let F=N^2-N-12I+H. On the diagonal,

    F_uu=10-0-12+2=0.

### Proof: off-diagonal quadratic relations

For distinct u,v put

    c=K_uv, h=H_uv, b=B_uv, ell=(B^2)_uv.

Here c is the number of common underlying blocks. We have |h|<=c. Since (E-cap) holds,

    ell+b+c<=4.                                      (3)

The absolute value of the signed two-walk count (N^2)_uv is at most ell. Thus

    |F_uv| <= ell+b+|h| <= ell+b+c <=4.              (4)

Integrality of E implies B^2+B+K=0 mod 2. Since N=B and R=M mod 2, F=0 mod 2. By (2), F=0 mod 3. Hence F_uv is divisible by six. Bound (4) forces F_uv=0. This holds for every off-diagonal entry. QED.

**Important:** neither mod 3 alone nor nonnegativity of E alone suffices. The proof explicitly uses integer E to get the parity, binary weight-2 target rows to bound the row relations, and pointwise E nonnegativity to bound each quadratic error. No averaging is used in (3)-(4).

### General normalized-family version

For m lines, n=m(m-1) exterior orbit indices, replace 12 by kappa=2m-2 and 8 by kappa-4 in the definitions of (S), (O), E. The same T formula and the same off-diagonal bound four hold. T-cap then forces B1=(2m-4)1. The proof is unchanged. This is the version tested on the 9- and 243-vertex controls. The projector specialization in the next section is specifically m=7.

## 3. Exact ternary projector formulation

Use a bar for reduction modulo three. Since R^TR=12I,

    Hbar^2=0,    Hbar Rbar=0.

Consider a 42-by-42 matrix P over F_3 satisfying

    P=P^T, P^2=P, PRbar=0, diag(P)=1.                 (P)

One may additionally require rank(P)=15. It is a necessary restriction; in fact it follows whenever the capacity tests below pass.

Define N entrywise by the centered lift

    N=center(P+Hbar),

where center(0)=0, center(1)=1, center(2)=-1. Set B=|N| and compute T,E by (1) **over Q**, not modulo three.

**Theorem 3.1.** If P satisfies (P) and this N passes T-cap and E-cap, then N satisfies all the integer signed equations (S).

### Proof

N is symmetric and its diagonal is zero because diag(P+Hbar)=1+2=0 mod 3. Since P is symmetric and PRbar=0, both PHbar and Hbar P vanish. Therefore

    Nbar Rbar=0,
    Nbar^2=(P+Hbar)^2=P=Nbar-Hbar.

These are (2). Apply Lemma 2.1. QED.

**Theorem 3.2 (necessity).** Every complete N satisfying (S) supplies a P satisfying (P), namely

    P=Nbar^2=Nbar-Hbar.

This P has rank exactly 15.

### Proof

NR=0 implies NH=HN=0. On im(R), N=0. On its 35-dimensional real orthogonal complement, the equation is N^2-N-12I=0, with roots 4,-3. Trace zero gives multiplicities 15 and 20. In particular

    Pi=(N^2+3N)/28

is a rational projector of rank 15. Its entries belong to Z_(3), since 28 is invertible at three. Its reduction is Nbar^2. Reducing Pi^2=Pi and its exact characteristic polynomial t^27(t-1)^15 proves that the resulting idempotent has rank 15 over F_3. This step uses the characteristic polynomial, not merely the trace modulo three. Symmetry, PRbar=0, and diag(P)=1 follow either from this formula or from P=Nbar-Hbar. QED.

### Exact connection to C2

Assume the Exact Reconstruction Theorem from the preceding handoff, or use the integral matching/parity reconstruction directly. The resulting equivalent question is:

    Does there exist P satisfying (P), rank 15,
    such that its centered N passes T-cap and E-cap,
    and the matching-completion system for this N is feasible?    (C2-P)

A positive solution reconstructs a genuine 99-vertex graph with the prescribed involution. A proof that every such P fails at least one of the three tests excludes C2. Failing a test for one P does not exclude all P. A proof that T-cap/E-cap alone always fail would be stronger than required; it is not assumed true.

The crucial gain in logical formulation is that a P passing the two capacity tests has **no further integer signing/lifting gap**: its centered N already satisfies the full signed quadratic equation. This is an exact reformulation, not a measured runtime reduction.

## 4. Interpretation as a labelled ternary code

Let Rcal=im(Rbar) inside F_3^42 with its standard dot product. Rcal is totally isotropic of dimension seven. Its perpendicular has dimension 35 and its radical is Rcal. Consequently

    W=Rcal^perp/Rcal

is a nondegenerate quadratic space of dimension 28.

An orthogonal projector P corresponds uniquely to a nondegenerate subspace C=im(P). PRbar=0 means C is contained in Rcal^perp. C intersects Rcal trivially, so its image Cbar in W is a nondegenerate 15-dimensional subspace. **Cbar alone does not determine C.** The choice of lift (section) matters, and the original 42 coordinates matter.

After choosing a basis matrix F for C,

    P=F(F^T F)^(-1)F^T

over F_3. This parameterizes the full idempotence condition. It does not mean that all possible F should now be enumerated. There are enormously many subspaces and lifts.

Most importantly, abstract dimension, rank and quadratic-space type do not imply the pointwise integer capacities. The supplied finite-field countermodel demonstrates this concretely.

## 5. A whole lifting family can be excluded by hand

This section establishes an actual nonexistence result for a precisely defined subclass of (C2-P), with arbitrary lifts in that subclass. It does **not** assume a symmetry of the unknown N.

### 5.1 A specific quotient subspace

Reorder the coordinates as the 21 plus indices followed by the 21 minus indices. Write

    R=[U; O],

where U is the unoriented edge/vertex incidence matrix of K_7, and O has row e_i-e_j for i<j. Over Z,

    U^TU=5I+J,  O^TO=7I-J.

Over F_3, put

    Q0=I_21-OO^T.

Then Q0 is the orthogonal projector onto Z=ker(O^T), of rank 15: OO^T is an idempotent of rank six. Define

    C0={(0,z): z in Z} inside Rcal^perp.

C0 is nondegenerate and disjoint from Rcal. Let Cbar0 be its image in W.

Consider **every** nondegenerate code C whose image in W is exactly Cbar0. These codes are all graph lifts of C0 by linear maps C0 -> Rcal. They include nonsymmetric codes; no requirement of invariance under line permutations is made.

Every such lift has the following form. Choose arbitrary row vectors t_1,...,t_7 in Z, form the 7-by-21 matrix T0 with these rows, and set

    F0=[0; Q0],  F=F0+Rbar T0,  P=FF^T.             (5)

Here F has 42 rows and 21 columns but rank 15. Since F0^T Rbar=0 and Rbar^T Rbar=0,

    F^T F=Q0,

and FQ0=F. Thus P is an orthogonal projector of rank 15 with PRbar=0. Conversely all graph lifts of C0 are obtained because the dot product on Z identifies Z with its dual.

There are 7*15 free ternary coefficients before diagonal and capacity conditions. The proof below covers them simultaneously. This parameter count is **not** a count of previously verified Conway candidates or of original rank-17 classes.

### 5.2 The diagonal condition controls a 21-index block

Assume diag(P)=1. In (5), the row of F at (ij,+) is t_i+t_j. Set

    a_i=t_i dot t_i in F_3.

For i!=j,

    (t_i+t_j)^2=1
      => t_i dot t_j=a_i+a_j-1.                  (6)

Therefore the plus-by-plus block of the centered N is determined just by the seven a_i. For distinct cells,

    Nbar_(ij,+;ik,+)=1-a_j-a_k,                 (7)

and for disjoint {i,j},{k,l},

    Nbar_(ij,+;kl,+)=-a_i-a_j-a_k-a_l-1.        (8)

These are entrywise identities modulo three. A zero residue is exactly a zero centered entry, so they determine the unsigned support of this block.

### 5.3 Capacity lemma for the seven a_i

**Lemma.** If the support of the plus-by-plus block in (7)-(8) has every row of degree at most ten, all seven a_i equal 2.

**Proof.** Let x,y,z be the counts of values 0,1,2; x+y+z=7. A row in the plus block has 20 other positions. Degree at most ten means it has at least ten zero entries.

For an endpoint type ab that is present, denote this number of zero entries by Z_ab. Direct counting from (7)-(8) gives

    Z_00=2y+(x-2)z+choose(y,2),
    Z_11=2x+(y-2)z+choose(x,2),
    Z_22=Z_01=xy+choose(z,2)-1,
    Z_02=z(y+1)-1+choose(x-1,2),
    Z_12=z(x+1)-1+choose(y-1,2).                 (9)

Only use a formula if that endpoint type exists. Interchanging 0 and 1 preserves the zero patterns.

If z is 2,3,4, the 22 type exists. The requirement Z_22>=10 says xy+choose(z,2)>=11. The largest possible left sides for these z are respectively 7,7,8, a contradiction.

If z=5, the same requirement forces x=y=1. Then Z_02=9<10. If z=6, by symmetry (x,y)=(1,0), and Z_02=5<10.

If z=0 and xy>0, type 01 requires xy>=11. With x+y=7 this leaves (3,4) or (4,3). For (3,4), Z_11=6+3=9; the other case is symmetric. If xy=0, all labels are 0 or all are 1, and the same-type zero count is zero.

If z=1 and xy>0, xy<=9 contradicts the 01 requirement. If xy=0, the only cases up to symmetry are (6,0,1), where Z_00=4.

Only z=7 remains. QED.

### 5.4 All these lifts fail the graph capacities

**Theorem 5.1.** No projector whose code image in W equals Cbar0 satisfies diag(P)=1, T-cap and E-cap simultaneously.

**Proof.** Suppose one does. By Theorem 3.1 its centered N satisfies the full integer signed system. In particular B has row degree ten, hence the plus block has row degree at most ten. Lemma 5.3 forces a_i=2 for all i. Equations (7)-(8) then give

    N_(plus,plus)=0

over the integers.

For every signed N satisfying (S), the integer positive-semidefinite matrix

    G=12I+4N-H=28 Pi

has rank 15. Its plus-by-plus principal submatrix is now

    G_(plus,plus)=12I_21-UU^T.

But U^TU=5I_7+J_7 has eigenvalues 12 (once) and 5 (six times). Consequently this 21-by-21 matrix has eigenvalues

    0 (once), 7 (six times), 12 (fourteen times),

and rank 20. A principal submatrix cannot have rank larger than the whole matrix. Contradiction. QED.

The same exclusion transports under the signed relabellings of the seven blocks, because those transformations preserve the original labelled problem. It may **not** be transported under arbitrary isometries of W: such isometries need not preserve the integer support-capacity tests. No exhaustiveness of this excluded orbit of quotient subspaces is asserted.

## 6. An explicit countermodel to an overbroad modular obstruction

The file data/ternary_projector_control.json contains P satisfying all of

    P=P^T, P^2=P, rank(P)=15, PRbar=0, diag(P)=1.

Its centered N has zero diagonal and satisfies (S) modulo three. It does NOT satisfy (S) over Z and is NOT a graph.

Its row-weight distribution is:

    weight 22: 2 rows; 25: 2; 28: 9; 31: 8; 34: 11; 37: 10.

Thus the target-cell capacity fails. In particular, no proposed proof that these ternary projector axioms are themselves inconsistent can be correct. The meaningful question is their compatibility with the original labelled capacities (and the final matching test).

The generator constructs a six-dimensional totally isotropic subspace in Z, a norm-one vector orthogonal to it, and solves a 21-equation linear system. All assertions are checked in F_3. This supplies a nontrivial sanity control for the new representation, rather than relying only on the known graph controls.

## 7. What was tested in the originally proposed dual/spectral direction

The earlier suggestion was to eliminate D by a universal dual or by compressing D to eigenspaces of N. No such universal certificate was obtained in this investigation.

Two tempting low-order expressions can be disposed of exactly.

First, from B1=10 and M^T1=12,

    E1=21 1.

For any row-stochastic D, the left side of BD+DB+D has the same row sum 10+10+1=21. Thus constant all-ones multipliers give an identity, not a strict inequality. This does not rule out nonconstant dual certificates.

Second define the rational projectors

    P0=H/12,
    P4=(12I+4N-H)/28,
    Pm=(12I-3N-H)/21.

If D is a genuine matching disjoint from B, tr(D)=tr(ND)=0. With s=tr(HD),

    tr(P0 D)=s/12,
    tr(P4 D)=-s/28,
    tr(Pm D)=-s/21.

Each paired pair of distinct labels has root inner product 0,+1,-1, so |s|<=42. These values automatically satisfy the elementary absolute trace bounds given by the ranks 7,15,20. Again, this establishes the weakness of these particular first trace tests, not of every mixed higher-order operator.

The lattice/Gram route had already identified analogous automatic star moments; see C1 notes/149_COUPLAGE_SEPT_ETOILES.md. Re-deriving such equalities and calling them a new global obstruction would not advance the proof.

## 8. Exact remaining obligation and a disciplined Agent-2 objective

All genuine normalized C2 graphs are represented in (C2-P). Theorem 5.1 excludes a specific family from that representation without testing its individual lifts.

To prove C2 empty one still needs, for **every** admissible P, at least one of:

    failure of T-cap;
    failure of E-cap;
    infeasibility of the exact matching-completion system.

To prove existence one needs a single P passing all tests, followed by reconstruction and independent verification of the actual 99-by-99 adjacency matrix.

What is NOT proved:

* that every possible quotient subspace Cbar equals Cbar0 or one of its relabelled images;
* that every P passing the two capacities fails the matching step;
* that no complete signed N exists;
* that this formulation is computationally cheaper than Route C or rank-17;
* that the known computations can be reclassified into these families without further work;
* that the theorem is independently certified.

The most precise follow-on research question supplied by this work is:

    Which labelled quotient subspaces Cbar can admit a lift whose centered projector
    has the row-support and two-walk capacities T-cap and E-cap?

A statement about abstract dimension or quadratic-space type is insufficient; the control already has the advertised projector structure. The mechanism that excluded Cbar0 was instead a forced support pattern on 21 labelled coordinates, followed by an impossible real Gram rank. Generalizing that mechanism is a concrete direction, not a promised solution.

## 9. Review checklist

An independent reader should check: the integrality requirement on E; all parity and window bounds; the characteristic-polynomial justification for rank(P)=15; completeness of the graph-lift parameterization in Section 5.1; the zero-count formulas (9) and their case split; and the distinction between excluding a single labelled quotient family and excluding all possible P.

This note assumes the preceding reconstruction theorem only for the final real-LP-to-matching step. Lemma 2.1, Theorems 3.1-3.2 and Theorem 5.1 have their own proofs above and do not require that theorem.
