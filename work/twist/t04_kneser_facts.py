r"""t04 (pre-registered in ODD_EIGENSPACE_RESOURCE.md s.3a). Standard facts on KG(7,2), cell coordinates.
 (i)   dim of the star-balanced space S' = {b : sum_{c ∋ k} b_c = 0 for all k}, and max |A b - b| on a basis of S'.
 (ii)  min |lambda + 6| over spec A (so A + 6I is invertible).
 (iii) number of edge sets of K7 of size <= 3 carrying a nonzero star-balanced vector; an explicit size-4 example.
 (iv)  sizes of nonzero ±1 edge-signings of subgraphs of K5 that are balanced at every vertex.
One process, < 5 s, < 50 MB.
"""
import itertools
import numpy as np

cells = list(itertools.combinations(range(7), 2))
A = np.array([[1.0 if not set(a) & set(b) else 0.0 for b in cells] for a in cells])
Inc = np.array([[1.0 if k in c else 0.0 for c in cells] for k in range(7)])     # 7 x 21

_, s, vt = np.linalg.svd(Inc)
basis = vt[np.sum(s > 1e-9):]                                                    # null space of Inc
print('(i)  dim star-balanced space:', basis.shape[0],
      '| max |A b - b| on its basis:', float(np.abs(basis @ A.T - basis).max()))
ev = np.linalg.eigvalsh(A)
print('(ii) spec A (rounded):', sorted({round(float(x), 6) for x in ev}), '| min |lambda+6| =', float(np.abs(ev + 6).min()))

bad = 0
for r in range(1, 4):
    for E in itertools.combinations(range(21), r):
        if np.linalg.matrix_rank(Inc[:, list(E)]) < r:
            bad += 1
ex = [cells.index((0, 1)), cells.index((1, 2)), cells.index((2, 3)), cells.index((0, 3))]
v = np.zeros(21)
v[ex] = [1, -1, 1, -1]
print('(iii) edge sets of size <= 3 with a nonzero star-balanced vector:', bad,
      '| 4-cycle 0-1-2-3 with signs +-+- balanced:', bool(np.allclose(Inc @ v, 0)))

k5 = list(itertools.combinations(range(5), 2))
sizes = set()
for signs in itertools.product((-1, 0, 1), repeat=10):
    if not any(signs):
        continue
    if all(sum(sg for sg, e in zip(signs, k5) if k in e) == 0 for k in range(5)):
        sizes.add(sum(1 for sg in signs if sg))
print('(iv) sizes of balanced ±1 signings inside K5:', sorted(sizes))
