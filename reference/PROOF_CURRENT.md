# Consolidated proof: real-linear completion is exact

**Status:** source-based mathematical derivation for independent review. This is a consolidated exposition of `originals/c2_linear_completion_2026_09_30/LINEAR_COMPLETION.md`, with elementary steps expanded. It is not a new independent verification and does not assert that C2 is empty.

The original file is preserved unchanged. The previous at-most-two and unsigned-uniqueness arguments are not prerequisites for this proof.

## 1. Fixed data and theorem

Let C=binom({1,…,7},2), and Ω=C×{+,−}. Order cells lexicographically, with + before − in each cell. For c={i,j}, i<j, set

\[
r_{c,+}=e_i+e_j,\qquad r_{c,-}=e_i-e_j.
\]

Let R have these 42 rows and put M=|R|, entrywise. Let χ have entry 1 at (c,+) and 0 at (c,−).

Assume N is a complete 42×42 matrix satisfying

\[
N=N^T,\quad \operatorname{diag}N=0,\quad N_{uv}\in\{0,\pm1\},
\]
\[
NR=0,\qquad N^2=N+12I_{42}-RR^T. \tag{S}
\]

Define

\[
B=|N|,\quad T=2J_{42,7}-M-\frac12BM,
\]
\[
E=\frac12(8I_{42}+4J_{42}-MM^T-B^2-B).
\]

For D real, impose

\[
D=D^T,\quad D\ge0,\quad \operatorname{diag}D=0,\quad D\mathbf1=\mathbf1,
\]
\[
B\circ D=0,\qquad DM=T,\qquad BD+DB+D=E. \tag{L}
\]

Let L_N be the feasible set of (L).

**Theorem T4.** L_N is empty or a singleton whose member is an integral perfect matching. In particular D²=I and all D entries are 0 or 1 in the feasible case, although neither condition is imposed in (L).

## 2. Label identities and parity

### Lemma 2.1 · Label identities

\[
R^TR=12I_7,\quad M\mathbf1_7=2\mathbf1_{42},\quad
M^T\mathbf1_{42}=12\mathbf1_7,\quad M^TM=10I_7+2J_7,
\]
\[
R\mathbf1_7=2\chi.
\]

**Proof.** A block belongs to six cells, each represented twice, giving each diagonal of R^TR and M^TM the value 12. For distinct i,j, the two signed rows belonging to {i,j} contribute +1 and −1 to R^TR, hence cancel. The same two rows contribute 2 to M^TM. Each row of M has exactly two ones. Finally the coordinate sum of e_i+e_j is 2 and that of e_i−e_j is 0. ∎

### Lemma 2.2 · Consequences for B, T, E

\[
B\mathbf1=10\mathbf1,\quad B\chi\equiv0\pmod2,\quad BM\equiv0\pmod2,
\]
\[
B^2+B\equiv MM^T\pmod2.
\]

In particular T,E are integral, and T1_7=2·1_42.

**Proof.** At a diagonal entry of (S),

\[
\sum_vN_{uv}^2=12-r_u\cdot r_u=10.
\]

Because every nonzero N entry has square 1, this is the row-sum assertion for B. Also
N R1_7=2Nχ=0 as an integer equality, so Nχ=0. Since N≡B mod 2, Bχ is even. Reducing NR=0 modulo 2, with R≡M, gives BM even. Reducing the other signed equation gives B²=B+MM^T in characteristic two, as claimed. Thus the numerators defining T,E are even. Finally,

\[
T\mathbf1_7=14\mathbf1-2\mathbf1-\tfrac12B(2\mathbf1)
=2\mathbf1.
\]

No graph, lattice, or matching has been assumed in these deductions. ∎

## 3. The cell-difference obstruction

This lemma supplies the contradiction in the real-linear proof. Its hypotheses are essential.

### Lemma 3.1

Let B be symmetric binary with zero diagonal, indexed by two-index cells, and let χ choose the + index in every cell. Suppose Bχ is even. There is no nonzero B-invariant space

\[
L=\operatorname{span}_{\mathbb R}\{g_c:c\in S\},\qquad
g_c=e_{c,+}-e_{c,-},
\]

where S is a nonempty collection of WHOLE cells, such that the restriction X=B|_L satisfies

\[
X^2+X=8I_L. \tag{3.1}
\]

**Proof.** Put the g_c in the columns of a matrix G. They are mutually orthogonal and have squared norm 2. Thus G^TG=2I. Since L is invariant there is a matrix X with BG=GX, and

\[
X=\tfrac12G^TBG,
\]

which is symmetric.

The coefficient of g_c in Bg_d is the (c,+) coordinate of Bg_d. It is an integer, so X is integral. At d=c this coefficient is

\[
X_{cc}=B_{c,+;c,+}-B_{c,+;c,-}=-B_{c,+;c,-}\in\{0,-1\}. \tag{3.2}
\]

Because χ^TG=1^T,

\[
\mathbf1^TX=\chi^TGX=\chi^TBG=(B\chi)^TG\equiv0\pmod2.
\]

The column sums, and by symmetry the row sums, of X are even. Take a diagonal entry of (3.1) modulo 2. As X is symmetric and integral,

\[
0=(X^2+X)_{cc}=\sum_dX_{cd}^2+X_{cc}
\equiv\sum_dX_{cd}+X_{cc}\equiv X_{cc}\pmod2.
\]

In view of (3.2), every diagonal entry is zero. Therefore tr X=0.

On the other hand f(t)=t²+t−8 is irreducible over Q, since its discriminant 33 is not a rational square. It has the two distinct roots α=(−1+√33)/2 and β=(−1−√33)/2. Equation (3.1) implies that all eigenvalues of X belong to {α,β}. The characteristic polynomial is rational. Applying the field conjugation √33↦−√33 shows that the multiplicities of α and β are equal. Since L is nonzero, both have a positive multiplicity a, hence

\[
\dim L=2a>0,\qquad \operatorname{tr}X=a(\alpha+\beta)=-a<0.
\]

This contradicts tr X=0. ∎

**Scope check.** The lemma does not prohibit every integral matrix satisfying X²+X=8I. The archived 33-similitude constructs such an X. Its associated binary lift fails Bχ≡0; this is why it is a valid negative control rather than a contradiction of the lemma.

## 4. What DM=T forces, even when D is fractional

Assume (L) is feasible. Do not assume D is integral.

### Lemma 4.1 · Targets are actual cells

Every row T_u is a binary vector of weight two. If D_uv>0 then M_v=T_u.

**Proof.** The row T_u=(DM)_u is a convex combination of the binary rows of M: the coefficients D_uv are nonnegative and sum to one. Every coordinate is therefore in [0,1]. By Lemma 2.2, it is also an integer, so each coordinate is 0 or 1. Its row sum is two. These are exactly the 21 distinct cell-incidence vectors.

If a coordinate of the convex combination equals 0, every positively weighted term has coordinate 0. If it equals 1, every positively weighted term has coordinate 1. Apply this to all seven coordinates: whenever D_uv>0, the whole row M_v must equal T_u. ∎

Write target(u) for the unique cell with incidence vector T_u. Symmetry then gives the reciprocal condition

\[
D_{uv}>0\Longrightarrow
\begin{cases}
u\ne v,\ B_{uv}=0,\
\operatorname{cell}(v)=\operatorname{target}(u),\
\operatorname{cell}(u)=\operatorname{target}(v).
\end{cases} \tag{4.1}
\]

### Lemma 4.2 · Only tiny partner components remain

Allowed edges satisfying (4.1) form components contained in K_2 or K_(2,2). Every feasible component is forced integral unless it is a full K_(2,2). A full K_(2,2) between two cells has the fractional form

\[
D_{c,d}=\begin{pmatrix}t&1-t\\1-t&t\end{pmatrix},\qquad0\le t\le1,
\]

and D_(d,c)=D_(c,d)^T. Distinct such components use disjoint whole cells. Their number s is at most ten.

**Proof.** Each index has one target cell. For two different cells c,d, allowed edges join only the indices in c targeting d to the indices in d targeting c. Each side has at most two indices. Different unordered target-cell pairs cannot share an index, because that index has a unique target. A within-cell component has at most the one edge between its two indices.

On a bipartite component, the sum of weights over its edges equals the number of vertices on each side, by the row sums. Hence a feasible component has equal side sizes. Size 1+1 forces its edge to have weight one. For size 2+2, the row and column sums yield the displayed parameterization. If any of the four potential edges is missing, its prescribed zero forces t to an endpoint. Otherwise all t∈[0,1] are allowed by these constraints. This full component consumes both indices of both cells; two such components cannot share a cell. Since there are 21 cells, s≤floor(21/2)=10. ∎

This argument also shows why the completion variables are not an arbitrary fractional matching on 42 vertices.

## 5. The remaining equations have only pins and equalities/complementations

### Lemma 5.1 · Classification of real entry equations

After the component parameterization, BD+DB+D=E is equivalent, over 0≤t_i≤1, to constant equations, endpoint pins t_i=0 or 1, and equations

\[
t_i=t_j\quad\text{or}\quad t_i=1-t_j.
\]

**Proof for different components.** The entry (BD)_uv depends only on the parameter of the component containing v. Its value is one of 0,1,t_j,1−t_j, because column v has either one unit entry or two entries t_j,1−t_j and B is binary. Similarly (DB)_uv is one of 0,1,t_i,1−t_i. Also D_uv=0 if the two indices lie in different components. Thus the equation is f(t_i)+g(t_j)=e, where e=E_uv is an integer.

If a function is constant, this is a constant check or a pin to 0 or 1. If both vary, the only possible integer right sides are 0,1,2. At 0 both summands must be 0; at 2 both must be 1. At 1 the equation is equality or complementation of the two parameters. No reduction modulo two has been used here.

**Proof for the same ambiguous component.** B has no entries between its two cells, since all four edges are eligible for D. Let a,b∈{0,1} be the B edges INSIDE the two cells. For an entry crossing the two cells, direct multiplication gives

\[
t+(a+b)(1-t)
\]

or the same expression with t replaced by 1−t. Its variable coefficient is 1−a−b∈{−1,0,1}, so equality to an integer is automatic, inconsistent, or an endpoint pin. Entries inside either cell and diagonal entries have constant value, since the intervening cross-cell B block is zero. Components already forced integral contribute only constants. This exhausts all entries. ∎

### Lemma 5.2 · A canonical half-integral feasible point

If the real system is feasible, there is a feasible point with each parameter in {0,1/2,1}. Moreover, if its feasible set contains a fractional or undetermined parameter, such a point can be chosen with at least one 1/2.

**Proof.** Make a relation graph whose edges are equalities or complementations and whose marked vertices have endpoint pins. In a connected component, every variable equals x or 1−x after choosing a root. A parity-consistent component with an endpoint pin has a unique 0/1 assignment. Incompatible endpoint pins make the whole system infeasible. An unpinned parity-consistent component has a free x∈[0,1]. An unpinned parity-inconsistent cycle imposes x=1−x and hence x=1/2. A parity-inconsistent component with an endpoint pin is infeasible.

In every free component choose x=1/2. All fixed endpoint components remain integral and all remaining components have parameter 1/2. If all components were fixed endpoint components, the feasible solution was already a unique binary point. ∎

**Important distinction.** An odd XOR cycle has no binary solution but does have the real solution 1/2 until the graph-origin lemma is used. The integrality proof must not assume it away.

## 6. A half-valued component creates an exact projector defect

Let D̄ be the canonical point from Lemma 5.2. Suppose it contains at least one half-parameter. Let S contain both cells of every half-parameter block, and define

\[
L=\operatorname{span}\{g_c:c\in S\},\qquad
P_L=\frac12\sum_{c\in S}g_cg_c^T.
\]

### Lemma 6.1 · Defect identities

\[
\bar D^2=I-P_L,\qquad\bar D P_L=P_L\bar D=0.
\]

**Proof.** A half block has off-diagonal block (1/2)J_2. It kills each of its two cell-difference vectors. On the two cell-sum vectors it swaps the cells and its square is identity. Equivalently, the square of the full 4×4 half block is diag(J_2/2,J_2/2), which is the orthogonal projector onto the two cell-sum directions. Its complement is exactly the sum of the two cell-difference projectors. All other components are integral matching edges with square identity. The components are disjoint, proving the global formulas. ∎

Set Q̄=B+2D̄. Then

\[
\bar Q M=4J_{42,7}-2M,
\]
\[
\bar Q^2+\bar Q=12I+4J-MM^T-4P_L. \tag{6.1}
\]

**Derivation.** The first equation follows from BM+2T=4J−2M. For the second,

\[
\bar Q^2+\bar Q
=B^2+B+2(B\bar D+\bar D B+\bar D)+4\bar D^2
=8I+4J-MM^T+4(I-P_L).
\]

### Lemma 6.2 · The defect space is B-invariant

**Proof.** B1=10·1 and D̄1=1 imply Q̄1=12·1. Since Q̄ is symmetric, it commutes with J_42. Also

\[
\bar Q MM^T=(4J_{42,7}-2M)M^T=8J_{42}-2MM^T.
\]

This expression is symmetric. Transposing therefore gives MM^TQ̄ equal to the same expression: Q̄ commutes with MM^T.

Every matrix commutes with its own polynomial. Take the commutator with Q̄ on both sides of (6.1). All terms except P_L already commute, hence [Q̄,P_L]=0. Lemma 6.1 gives [D̄,P_L]=0, so [B,P_L]=0. Therefore L is B-invariant. ∎

Each cell has two identical rows in M, so M^Tg_c=0, and 1^Tg_c=0 as well. Thus J and MM^T vanish on L. On L, D̄=0, hence Q̄=B. Restricting (6.1) yields

\[
(B|_L)^2+(B|_L)=8I_L.
\]

But L is a nonempty span of whole-cell differences, and Bχ is even by Lemma 2.2. Lemma 3.1 gives a contradiction. Therefore the canonical point has no half-parameter.

## 7. Conclude integrality and uniqueness

A free component could have been set to 1/2; an unpinned odd parity cycle would force 1/2. Both have been ruled out. Every component in the relation graph of a feasible system is therefore fixed to endpoints. There is exactly one solution in the parameter domain, with all parameters 0 or 1.

The forced components are integral too. Thus D is a symmetric binary row-stochastic matrix with zero diagonal. Every row has exactly one 1. Symmetry gives the same for columns and pairs its nonzero entries reciprocally; consequently D is a fixed-point-free involutory permutation matrix and D²=I. This proves Theorem T4. ∎

## 8. Consequence for the graph

If the feasible set is nonempty, use its D to set Q=B+2D. The calculation in §6 now has P_L=0, so Q satisfies the exact ordinary-sector equations. Define

\[
a=(Q-N)/2,\quad b=(Q+N)/2.
\]

On a B edge, Q=1 and N=±1, so a,b are 0 and 1 in one order. On a D edge, N=B=0 and Q=2, so a=b=1. Elsewhere both vanish. Therefore they are binary symmetric matrices with zero diagonal. Together with the fixed incidence labels they give the explicit graph in [GRAPH_RECONSTRUCTION.md](GRAPH_RECONSTRUCTION.md).

Conversely an integral valid completion satisfies (L) by expansion with D²=I. Thus real feasibility is exactly graph-completion feasibility for the normalized model.

## 9. Where this argument stops

The proof excludes a nonempty HALF-VALUED defect L. For a genuine integral matching D, that defect is zero. Lemma 3.1 then has no nonzero space to which it can be applied. Nothing above creates a contradictory nonzero space from a unique integral completion.

The existence statement remains

\[
\exists N\in\mathcal N:\ L_N\ne\varnothing.
\]

Its negation is the universal infeasibility target. This dossier does not supply it. The theorem also does not generate N or make the constraints quadratic in N become linear: B=|N| and B² occur in the coefficients.

## 10. Audit checkpoints

Every significant step can be reviewed independently in order:

1. Fixed canonical labels give R1=2χ; arbitrary representative switches cannot leave R frozen.
2. Signed equations make Bχ and BM even and T,E integral.
3. Invariance of L gives an integral symmetric restriction X with diagonal 0 or −1.
4. The parity/trace lemma really needs WHOLE cells and Bχ even.
5. Fractional support is forced by endpoints of convex combinations, not an integrality assumption.
6. All entry equations, including within an ambiguity block, have only the listed forms.
7. Real odd-parity cycles are retained as half-solutions before they are contradicted.
8. D̄²=I−P_L is exact and depends on choosing the canonical 0,1/2,1 point.
9. J_(42,7)M^T=2J_42 gives the coefficient 8 in the commutator calculation.
10. The final contradiction eliminates half-values, not the unique integral case.
11. The reconstruction must check every block of the 99×99 SRG identity.
12. The all-involutions reverse reduction separately needs the fixed-point input F0.
