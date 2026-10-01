r"""Coordinator independent check of G1-D R2 (one process, < 2 min, < 1 GB). Exact question: for the rebuilt BvLS
srg(243,22,1,2), with X = graph + all triangles + all 4-cycles, is Delta_1 = d1^T d1 + d2 d2^T equal to (k+1)I + O
(O supported on pairs of disjoint edges that are opposite in a 4-cycle, entries +-1), and is min eig Delta_1 = 3?"""
import numpy as np, itertools
N = np.load('data/bvls_m11_N.npy'); D = np.load('data/bvls_m11_D.npy'); n = N.shape[0]; m = 11
cells = list(itertools.combinations(range(m), 2))
R = np.zeros((n, m), dtype=int)
for u, ((i, j), e) in enumerate(itertools.product(cells, (1, -1))): R[u, i] = 1; R[u, j] = e
B = np.abs(N); Q = B + 2 * D; a = (Q - N) // 2; b = (Q + N) // 2
V = 1 + 2 * m + 2 * n; A = np.zeros((V, V), dtype=np.int64)
inn = lambda k, s: 1 + 2 * k + (s < 0); ext = lambda x, e: 1 + 2 * m + 2 * x + (e < 0)
for k in range(m):
    for s in (1, -1): A[0, inn(k, s)] = A[inn(k, s), 0] = 1
    A[inn(k, 1), inn(k, -1)] = A[inn(k, -1), inn(k, 1)] = 1
for x in range(n):
    for e in (1, -1):
        for k in range(m):
            if R[x, k]: A[ext(x, e), inn(k, e * R[x, k])] = A[inn(k, e * R[x, k]), ext(x, e)] = 1
        for y in range(n):
            for d in (1, -1):
                if (e * d == 1 and a[x, y]) or (e * d == -1 and b[x, y]): A[ext(x, e), ext(y, d)] = 1
k = 2 * m
assert (A @ A + A == (k - 2) * np.eye(V, dtype=int) + 2).all()
edges = [(u, v) for u in range(V) for v in range(u + 1, V) if A[u, v]]; eid = {e: i for i, e in enumerate(edges)}
E = len(edges)
def sgn_edge(u, v): return (eid[(u, v)], 1) if u < v else (eid[(v, u)], -1)
d1 = np.zeros((V, E)); 
for i, (u, v) in enumerate(edges): d1[u, i] = -1; d1[v, i] = 1
cols = []
for u, v, w in itertools.combinations(range(V), 3):
    if A[u, v] and A[v, w] and A[u, w]: cols.append([(u, v), (v, w), (w, u)])
A2 = A @ A; seen = set()
for u in range(V):
    for w in range(u + 1, V):
        if not A[u, w]:
            c = np.nonzero(A[u] * A[w])[0]
            v1, v2 = int(c[0]), int(c[1]); key = frozenset([u, w, v1, v2])
            if key not in seen: seen.add(key); cols.append([(u, v1), (v1, w), (w, v2), (v2, u)])
d2 = np.zeros((E, len(cols)))
for j, cyc in enumerate(cols):
    for (p, q) in cyc:
        i, s = sgn_edge(p, q); d2[i, j] += s
L = d1.T @ d1 + d2 @ d2.T
diag_ok = np.allclose(np.diag(L), k + 1)
off = L - np.diag(np.diag(L)); bad = 0
for i, j in zip(*np.nonzero(off)):
    if set(edges[i]) & set(edges[j]): bad += 1
ev = np.linalg.eigvalsh(L)
print('V', V, 'E', E, '2-cells', len(cols), '| diag = k+1:', diag_ok, '| nonzero off-diag on edges sharing a vertex:', bad,
      '| off-diag values', sorted(set(np.round(off[off != 0]).astype(int))), '| min eig', round(ev.min(), 6))
