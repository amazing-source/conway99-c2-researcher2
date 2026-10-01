# From (N,D) to the full 99-vertex graph, and back

**Status:** detailed editorial expansion of the reconstruction in the original parity note §1 and linear note §7, for independent review. The original sources gave the action matrices and stated the blockwise verification. Here the block calculations and graph vertex order are explicit. This is not a record of an independent review.

The positive construction is self-contained. The reverse implication for ALL C2 objects has one external project dependency: the one-fixed-point theorem F0.

## 1. Original target

A C2 object is a pair (Γ,σ) where Γ is a simple strongly regular graph with parameters (99,14,1,2) and σ is a nonidentity involutory automorphism.

For its adjacency A_Γ and permutation P_σ, the target conditions are

\[
A_\Gamma=A_\Gamma^T\in\{0,1\}^{99\times99},\quad
\operatorname{diag}A_\Gamma=0,\quad A_\Gamma\mathbf1=14\mathbf1,
\]
\[
A_\Gamma^2+A_\Gamma=12I_{99}+2J_{99},
\]
\[
P_\sigma^2=I,\quad P_\sigma\ne I,\quad A_\Gamma P_\sigma=P_\sigma A_\Gamma.
\]

For distinct vertices, the SRG matrix identity says there is one common neighbour for an edge and two for a nonedge. On the diagonal it says the degree is 14.

## 2. Normalization used in the reverse reduction

### F0 · External input

> Every involution of an srg(99,14,1,2) fixes exactly one vertex.

The supplied project notes use this as an established, externally sourced result. The three completion archives do not contain its full proof. The matrix theorem T4 is independent of it. A universal exclusion of the normalized matrices becomes an exclusion of ALL involutions only after F0 is separately secured.

### Consequences of F0, written out

Assume a graph Γ and involution σ, with Fix(σ)={x}.

For each y∈N(x), the number of neighbours of y inside N(x) is λ=1. Hence the graph induced on N(x) is a 1-regular graph on 14 vertices: seven disjoint edges. Label them {i^+,i^-}, i=1,…,7.

There are 84 other vertices. Each has exactly two neighbours in N(x), by μ=2 applied to it and x. These neighbours cannot be in the same interior edge, because that adjacent pair already has x as its unique common neighbour. Conversely, two vertices a,b in different interior blocks are nonadjacent and have exactly two common neighbours, one being x. Their other common neighbour is outside N(x): inside N(x), every vertex has only its one matched neighbour. Thus exterior vertices are in bijection with cross-block signed pairs {i^α,j^β}. There are 4·binom(7,2)=84 such pairs.

Now σ preserves N(x). If it exchanged two interior vertices a,b in different blocks, it would preserve the unordered pair {a,b}, and hence fix their unique exterior common neighbour. That contradicts Fix(σ)={x}. It has no fixed interior vertex, so it must swap the two endpoints of every interior edge. Thus σ(i^+)=i^- and, by uniqueness of exterior labels, σ changes BOTH signs of every exterior label.

For each cell c={i,j}, i<j, choose representatives p_(c,+) labelled {i^+,j^+} and p_(c,−) labelled {i^+,j^-}. Their images have both signs reversed. These are the canonical R rows.

No exterior vertex p is adjacent to σp. Otherwise their edge's unique common neighbour is σ-fixed, hence x; but x is not adjacent to an exterior vertex. Thus a_pp=b_pp=0.

For exterior p, the two common neighbours of p and σp form a σ-invariant set of size two. It contains no fixed vertex and no interior vertex, since the interior labels of p and σp are disjoint. It is consequently one exterior orbit {q,σq}. By symmetry and μ=2, q and σq in turn have exactly {p,σp} as their common neighbours. This supplies a perfect matching D on the 42 exterior orbits, recording their double adjacencies.

Each exterior vertex has degree 14, two interior neighbours, and hence 12 exterior neighbours. One orbit supplies two neighbours; all other adjacent orbits supply one. There are ten such single adjacencies, so B has row sum ten.

## 3. Extract N and D from a normalized graph

For representatives p_u and p_v put

\[
a_{uv}=A_\Gamma(p_u,p_v),\quad b_{uv}=A_\Gamma(p_u,\sigma p_v),
\]
\[
N=b-a,\quad B=|N|,\quad D_{uv}=a_{uv}b_{uv},\quad Q=a+b=B+2D.
\]

All products a_uv b_uv in this paragraph are scalar entrywise products. The ordinary matrix product ab is not meant.

The automorphism and undirected graph imply a,b symmetric. The diagonal is zero by the previous argument. With the fixed R,M labels, the action of the adjacency on σ-odd functions is

\[
S_-=\begin{pmatrix}-I_7&R^T\\R&-N\end{pmatrix}.
\]

The all-ones matrix acts as zero on these functions. Hence the full SRG identity gives S_-²+S_-=12I_49. Its off-diagonal and lower-right blocks yield exactly

\[
NR=0,\quad N^2=N+12I_{42}-RR^T.
\]

On σ-even functions, the action matrix is the A_+ displayed in §6. Its lower-right and lower-middle block identities yield (O). This proves the graph-to-matrix implication for the normalized class.

## 4. Construct the graph from a matrix pair

Conversely, assume N satisfies (S) and D is an integral completion satisfying (O). The real-linear theorem T4 supplies such an integral D whenever L_N is feasible, but the construction in this section only uses its explicitly checkable integral properties.

Order the 99 vertices as follows:

\[
x;\quad 1^+,\ldots,7^+;\quad1^-,\ldots,7^-;
\quad p_1,\ldots,p_{42};\quad \sigma p_1,\ldots,\sigma p_{42}.
\]

Define the 42×7 binary matrices

\[
R_+=(M+R)/2,\qquad R_-=(M-R)/2,
\]

and the 42×42 matrices

\[
a=(Q-N)/2,\qquad b=(Q+N)/2,\qquad Q=B+2D.
\]

The interior adjacency and interior–exterior incidence are

\[
F=\begin{pmatrix}0&I_7\\I_7&0\end{pmatrix},\qquad
K=\begin{pmatrix}R_+^T&R_-^T\\R_-^T&R_+^T\end{pmatrix}.
\]

The exterior adjacency is

\[
H=\begin{pmatrix}a&b\\b&a\end{pmatrix}.
\]

Finally set

\[
A_\Gamma=
\begin{pmatrix}
0&\mathbf1_{14}^T&0\\
\mathbf1_{14}&F&K\\
0&K^T&H
\end{pmatrix}. \tag{4.1}
\]

### Binary entries and simplicity

If B_uv=1, N_uv=±1 and D_uv=0, so (a_uv,b_uv) is (0,1) or (1,0). If D_uv=1, B_uv=N_uv=0, so a_uv=b_uv=1. Otherwise both vanish. Their diagonals are zero. R_+,R_- are binary by the explicit signed row definitions. Therefore (4.1) is binary symmetric with zero diagonal.

### Degrees

The fixed vertex sees 14 interior vertices. Each interior vertex sees x, its mate, and 12 exterior vertices, by M^T1_42=12·1_7. Each exterior vertex sees two interior vertices and (a+b)1=Q1=(10+2)1=12 exterior vertices. Every degree is 14.

### Automorphism

Let P_σ fix x and swap the two interior layers and the two exterior layers. The displayed block forms give P_σ²=I, P_σ≠I, and A_ΓP_σ=P_σA_Γ. Its only fixed vertex is x.

## 5. Verify every σ-odd block of the SRG identity

Use the subspace of functions with value zero at x, opposite values on i^+,i^-, and opposite values on p_u,σp_u. The action matrix is S_- as in §3. Compute:

\[
(S_-^2+S_-)_{\mathrm{inner,inner}}
=I_7+R^TR-I_7=12I_7,
\]
\[
(S_-^2+S_-)_{\mathrm{inner,outer}}
=-R^T-R^TN+R^T=-R^TN=0,
\]
\[
(S_-^2+S_-)_{\mathrm{outer,inner}}=-NR=0,
\]
\[
(S_-^2+S_-)_{\mathrm{outer,outer}}
=RR^T+N^2-N=12I_{42}.
\]

Hence A_Γ²+A_Γ=12I on the 49-dimensional odd space. This is the full target identity there because J_99 kills every odd function.

## 6. Verify every σ-even block

Represent an even function by its value at x, its seven common interior-orbit values, and its 42 common exterior-orbit values. The action matrix is

\[
A_+=
\begin{pmatrix}
0&2\mathbf1_7^T&0\\
\mathbf1_7&I_7&M^T\\
0&M&Q
\end{pmatrix}.
\]

This basis is not orthonormal; A_+ need not be symmetric. The restriction of J_99 is

\[
J_+=\mathbf1_{50}(1,2\mathbf1_7^T,2\mathbf1_{42}^T),
\]

because an orbit-constant function's sum is its value at x plus twice every other orbit value. The target identity is A_+²+A_+=12I_50+2J_+.

All nine blocks are as follows; J in a block denotes the all-ones matrix of that block's size.

| Block | Computation of A_+²+A_+ | Target |
|---|---|---|
| x,x | 2·7 | 14 |
| x,inner | 2·1_7^T+2·1_7^T | 4·1_7^T |
| x,outer | 2·1_7^TM^T=2(M1_7)^T | 4·1_42^T |
| inner,x | 1_7+1_7 | 2·1_7 |
| inner,inner | 2J_7+2I_7+M^TM | 12I_7+4J_7 |
| inner,outer | 2M^T+M^TQ | 4J_(7,42) |
| outer,x | M1_7 | 2·1_42 |
| outer,inner | 2M+QM | 4J_(42,7) |
| outer,outer | MM^T+Q²+Q | 12I_42+4J_42 |

The inner–outer calculation uses the transpose of QM=4J−2M. These blocks are precisely 12I_50+2J_+.

The even and odd spaces are complementary and have dimensions 50 and 49. The target operator vanishes on each, hence on all of R^99. Thus the constructed A_Γ satisfies the complete SRG identity.

## 7. What a positive witness must include

An explicit N with a feasible completion is enough mathematically after the theorem is verified. For an independently checkable computational witness, publish N and either D or the final A_Γ; ideally publish all three with the index convention.

A direct verifier should check finite integer equalities, not a numerical spectrum:

1. A_Γ is 99×99, binary, symmetric, and has zero diagonal.
2. All row sums are 14.
3. A_Γ²+A_Γ=12I+2J exactly.
4. The displayed P_σ is a permutation, involutory, nonidentity, and commutes with A_Γ.
5. When supplied, N,D satisfy the signed and ordinary equations and agree with the reconstruction.

The code in this package implements these checks. There is no claimed m=7 witness in the package. The m=2 and m=11 test graphs are positive controls of related formulas, not examples of Conway 99.

## 8. Logical consequences

A positive verified A_Γ settles the entire Conway existence problem positively, and also establishes existence in C2. It does not need C3 or the rank-17/24 reductions.

A proof that NO normalized pair N,D exists excludes one-fixed-point involutions. Together with F0 this excludes every involution. It does not exclude graphs with no involution; in particular it does not eliminate the asymmetric branch.

If T4 failed, an explicit integral N,D could still be verified by this construction directly. Failure of the real-linear theorem is not, by itself, evidence either for or against graph existence.
