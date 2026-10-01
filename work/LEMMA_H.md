# Lemma H and the type-2 rigidity package (frozen 2026-09-30)

Status: PROVED HERE (hand proofs below). T4 is used as a working lemma (hand-reviewed, not formally
verified). F0 is not used. Nothing below uses the signs of N beyond B = |N|.

## 0. Exact hypotheses and the only facts used

Let (N, D) be feasible: N in S and D in L_N. Write B = |N|. By T4, D is the permutation matrix of a
fixed-point-free involution pi of the 42 orbits, with B_(x, pi x) = 0 for all x. From these hypotheses
only the following three consequences are used.

 (Deg) B 1 = 10 * 1.                               [diagonal of N^2 = N + 12I - RR^T; S]
 (P)   f_x(k) := (BM)_(x,k) = 4 - 2 M_(x,k) - 2 M_(pi x,k).    [DM = T in L_N]
 (Q)   for x != y:
       (B^2)_xy + B_xy + s(x,y) + 2 ( B_(x,pi y) + B_(pi x,y) + D_xy ) = 4,
       where s(x,y) = |cell(x) cap cell(y)| = (MM^T)_xy.
       [off-diagonal entries of BD + DB + D = E in L_N, with (BD)_xy = B_(x,pi y), (DB)_xy = B_(pi x,y)
        because D is the permutation matrix of pi (T4), and E_xy = (4 - s - (B^2)_xy - B_xy)/2.]

Notation. Each cell c (2-subset of [7]) has two orbits c^0 = (c,+), c^1 = (c,-); exponents are in
GF(2). Disj(c) = the 20 orbits whose cell is disjoint from c. A cell c is *type 2* if pi(c^0) = c^1.
Y = set of type-2 cells, X = the other cells.

## 1. Lemma G0 (structure at a type-2 cell)

Let c be type 2. Then (i) every B-neighbour of c^0 or c^1 has its cell disjoint from c;
(ii) B(c^0) and B(c^1) are disjoint; (iii) B(c^0) and B(c^1) partition Disj(c).

Proof. (i) (P) with cell(pi x) = cell(x) = c gives f_x(k) = 0 for k in c.
(ii) (Q) at (c^0, c^1): D = 1, B_(c^0,c^1) = 0 (B misses pi), s = 2, B_(c^0, pi c^1) = B_(c^0,c^0) = 0,
B_(pi c^0, c^1) = 0, so (B^2)_(c^0,c^1) = 4 - 0 - 2 - 2 = 0.
(iii) By (Deg) each set has 10 elements; by (i) both lie in Disj(c), which has 20. By (ii) they partition it.

## 2. Lemma G (neighbours inside type-2 cells) and the labels

Let c be type 2 and z any orbit with cell(z) != c.
 - If cell(z) is disjoint from c, z has exactly one B-neighbour in c; call it c^(phi_c(z)).
 - If cell(z) meets c, z has no B-neighbour in c.
Proof: G0(iii) and G0(i), read from z's side.

For disjoint type-2 cells c, d the 2x2 block B[c,d] has all row and column sums 1, so there is
g(c,d) = g(d,c) in GF(2) with phi_c(d^b) = b + g(c,d).

## 3. Lemma E' (extended cocycle)

Let c, d be disjoint type-2 cells and w any orbit whose cell is disjoint from c cup d. Then
      phi_c(w) + phi_d(w) = g(c,d).
In particular (w an orbit of a third type-2 cell e, pairwise disjoint): g(c,d) + g(d,e) + g(c,e) = 0 (Lemma E).

Proof. Fix a, put x = c^a, y' = d^(a + g(c,d) + 1). Then B_(x,y') = 0, s = 0, D_(x,y') = 0,
B_(x, pi y') = B_(x, d^(a+g)) = 1 and B_(pi x, y') = B_(c^(a+1), d^(a+1+g)) = 1 (permutation block).
(Q) gives (B^2)_(x,y') = 0: x and y' have no common B-neighbour. By Lemma G, w is adjacent to exactly
one orbit of c and one of d. Taking a = phi_c(w), w ~ x, so w is not adjacent to y'; hence
phi_d(w) = a + g(c,d).

## 4. Lemma H

Let c, d be type-2 cells with |c cap d| = 1 and W = [7] minus (c cup d) (|W| = 4). Then among the six
cells inside W there are two DISJOINT cells, both not of type 2.

Proof. Let x = c^a, y = d^b (a, b arbitrary). In (Q): B_xy = 0 (G0(i), cell d meets c), s = 1,
D_xy = 0, B_(x, pi y) = B_(x, d^(b+1)) = 0 and B_(pi x, y) = 0 (same reason). So (B^2)_xy = 3.
A common neighbour has its cell disjoint from c and from d (G0(i) twice), i.e. inside W. By Lemma G,
      #{ w in O(W) : phi_c(w) = a, phi_d(w) = b } = 3   for all (a,b),            (*)
where O(W) is the set of 12 orbits with cell inside W. Put psi(w) = phi_c(w) + phi_d(w). Summing (*)
over the two pairs with a + b = theta:  #{w in O(W): psi(w) = theta} = 6 for theta = 0, 1.   (**)
The six cells of W form three complementary pairs {e, e'} (e cup e' = W). If e' is type 2, then:
for the orbits w of e, Lemma E' applied to (c, e') and to (d, e') gives psi(w) = g(c,e') + g(d,e');
for the orbits e'^s of e', psi = (s + g(c,e')) + (s + g(d,e')) = g(c,e') + g(d,e'). So all four
orbits of e cup e' have the same psi. If every complementary pair contained a type-2 cell, every value
of psi would occur a multiple of 4 times, contradicting (**). So some complementary pair {e, e'}
consists of two non-type-2 cells.

Consequence for EX: a necessary condition on the set Y of type-2 cells of any feasible (N,D).
It does not use the N^2 equation beyond (Deg), nor the signs.

## 5. Lemma J (a type-2 cell cannot be surrounded by type-2 cells)

If v is a type-2 cell, then at least one of the 10 cells disjoint from v is not of type 2.

Proof. Say v = {6,7} and suppose all cells inside U = {1,...,5} are type 2. Let z be any orbit of
cell {1,6} (its own type is irrelevant) and x = v^a. In (Q): B_xz = 0 and B_(pi x, z) = 0 (G0(i)),
s = 1, D_xz = 0, so (B^2)_xz = 3 - 2 B_(x, pi z) is odd. Common neighbours lie in cells inside U
(G0(i) for v). None lies in a cell {1,j}: those are type 2 and meet cell(z) (Lemma G). In each of the
six cells f inside T = {2,3,4,5}, z has exactly one neighbour f^(phi_f(z)) and x has exactly one,
f^(a + g(v,f)). They coincide iff lambda(f) := phi_f(z) + g(v,f) = a. For complementary f, f' in T,
Lemma E' (cells f, f'; orbit z) gives phi_f(z) + phi_f'(z) = g(f,f'), and Lemma E on the triangle
{v, f, f'} gives g(v,f) + g(v,f') = g(f,f'); hence lambda(f) = lambda(f'). So the number of common
neighbours is even: contradiction.

## 6. What is and is not claimed

 - Lemmas G0, G, E', H, J hold for every feasible (N, D) (with T4 as working lemma).
 - They constrain only the set Y of type-2 cells and the adjacency to type-2 cells. They say nothing
   when Y is empty (all 21 squares span 3 or 4 coordinates); that case is untouched.
 - The earlier R4 (Y = all cells impossible) and R5 are special cases (R5 via Lemma H).

## 7. Support classes and the extremal case n2 = 11

Computation (CHECKED, work/code/classify_XH.c, exhaustive over all 2^21 subsets X of cells, output
work/data/classify_XH_v1.txt, 21 s, < 20 MB): impose on X = non-type-2 cells
 (H) Lemma H;
 (G4) for every non-type-2 orbit z (cell e, partner cell d != e) the degree profile (P) must be
      realisable: one neighbour in each type-2 cell disjoint from e (Lemma G), none in type-2 cells
      meeting e, and multiplicities m_f in {0,1,2} in non-type-2 cells f, with m_d <= 1 (z not adjacent
      to pi z) and m_e <= [e cap d = empty] (a B-edge between cell-mates forces both to have type 0);
 (PI) pi restricted to non-type-2 orbits is a perfect matching using only cell pairs feasible both ways.
All three are consequences of Section 0. Result: 133 S7-classes survive; |X| >= 10 always, i.e.
n2 := |Y| <= 11, and n2 = 11 occurs for exactly one S7-class:

    Y = K(U) cup {V},  U a 5-set, V = [7] minus U       (e.g. U = {1..5}, V = {6,7}).

Mathematical characterisation of this class (PROVED HERE):
 (a) pi is forced on the 20 non-type-2 orbits: an orbit z of cell {i,6} (i in U) has exactly one
     neighbour in each of the six type-2 cells inside U \ {i}, so f_z(j) >= 3 for j in U \ {i}; by (P)
     f_z(j) = 4 - 2[j in cell(pi z)], hence cell(pi z) avoids U \ {i}; it is not {6,7} (type 2) and not
     {i,6} (that cell is not type 2), so cell(pi z) = {i,7}. Thus the ten non-type-2 cells form five
     blocks {i6, i7}, each carrying two squares of type 1: (n2, n1, n0) = (11, 10, 0).
 (b) The class is nevertheless empty: Lemma J applies to v = V, since all ten cells disjoint from V
     (the cells of K(U)) are type 2.
Adding Lemma J to the filter (work/data/classify_XHJ_v1.txt) removes exactly this class:
132 classes remain, max n2 = 10, attained by a unique class Y = {12,13,14,16,23,24,27,35,45,67}.
