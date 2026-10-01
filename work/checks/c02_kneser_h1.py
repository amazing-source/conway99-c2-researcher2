# C02: H^1 over GF(2) of the triangle (clique) complex of the Kneser graph KG(7,2).
# Exact GF(2) linear algebra. Memory: trivial (< 10 MB).
import itertools, numpy as np
cells = list(itertools.combinations(range(7), 2))
idx = {c: n for n, c in enumerate(cells)}
edges = [(a, b) for a, b in itertools.combinations(range(21), 2) if not set(cells[a]) & set(cells[b])]
eidx = {e: n for n, e in enumerate(edges)}
tris = [t for t in itertools.combinations(range(21), 3)
        if all(not set(cells[x]) & set(cells[y]) for x, y in itertools.combinations(t, 2))]
print("vertices", len(cells), "edges", len(edges), "triangles", len(tris))
def rank2(A):
    A = A.copy() % 2; r = 0; rows, cols = A.shape
    for c in range(cols):
        piv = [i for i in range(r, rows) if A[i, c]]
        if not piv: continue
        A[[r, piv[0]]] = A[[piv[0], r]]
        for i in range(rows):
            if i != r and A[i, c]: A[i] ^= A[r]
        r += 1
        if r == rows: break
    return r
d0 = np.zeros((len(edges), 21), dtype=np.uint8)   # coboundary C^0 -> C^1
for n, (a, b) in enumerate(edges): d0[n, a] = d0[n, b] = 1
d1 = np.zeros((len(tris), len(edges)), dtype=np.uint8)  # C^1 -> C^2
for n, t in enumerate(tris):
    for x, y in itertools.combinations(t, 2): d1[n, eidx[(x, y)]] = 1
r0, r1 = rank2(d0), rank2(d1)
print("rank d0 =", r0, " rank d1 =", r1)
print("dim Z^1 =", len(edges) - r1, " dim B^1 =", r0, " dim H^1 =", len(edges) - r1 - r0)
