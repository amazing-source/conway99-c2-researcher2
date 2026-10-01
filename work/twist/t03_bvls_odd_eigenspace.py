r"""C-T3 (pre-registered in TWIST_CALCULUS.md s.1d). BvLS, m = 11.

W = the exact 4-eigenspace of Q_A (dimension 11).
 (a) K W = 0, i.e. these are exact kappa-odd eigenvectors of Q with no leakage.
 (b) For each coordinate k: dim{t in W : supp t in star(k)}.
 (c) For each k: dim{t in W : supp t in cells avoiding k}.
 (d) Support sizes of a reduced basis of W (exact rational RREF via fractions).

Run from work/. One process, < 10 s, < 100 MB.
"""
import itertools
from fractions import Fraction
import numpy as np

N = np.load('data/bvls_m11_N.npy')
D = np.load('data/bvls_m11_D.npy')
n, m = N.shape[0], 11
cells = list(itertools.combinations(range(m), 2))
nc = len(cells)
Q = np.abs(N) + 2 * D
U = np.zeros((n, nc), dtype=np.int64)
for c in range(nc):
    U[2 * c, c], U[2 * c + 1, c] = 1, -1
X = U.T @ Q @ U                                   # = 2 Q_A, an integer matrix
ZZ = (np.eye(n, dtype=np.int64) * 2 - U @ U.T) @ Q @ U   # = 2 Z


def nullspace_exact(A):
    """Exact rational null space of an integer matrix (list of Fraction vectors), via RREF."""
    A = [[Fraction(int(v)) for v in row] for row in A]
    rows, cols = len(A), len(A[0])
    piv, r = [], 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = 1 / A[r][c]
        A[r] = [v * inv for v in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for fcol in free:
        v = [Fraction(0)] * cols
        v[fcol] = Fraction(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fcol]
        basis.append(v)
    return basis


# W = ker(X - 8I) restricted to ker(2Z): stack the two conditions
Wb = nullspace_exact(np.vstack([X - 8 * np.eye(nc, dtype=np.int64), ZZ]))
print('dim W (exact, with Z = 0):', len(Wb), '| dim ker(Q_A - 4):', len(nullspace_exact(X - 8 * np.eye(nc, dtype=np.int64))))
Wm = np.array([[float(v) for v in vec] for vec in Wb]).T          # nc x dimW
print('(a) max |2Z W| =', float(np.abs(ZZ @ Wm).max()))
for k in range(m):
    outside = [c for c in range(nc) if k not in cells[c]]
    inside = [c for c in range(nc) if k in cells[c]]
    rk_out = np.linalg.matrix_rank(Wm[outside, :]) if outside else 0
    rk_in = np.linalg.matrix_rank(Wm[inside, :]) if inside else 0
    print(f'   k={k}: dim(W supported in star(k)) = {Wm.shape[1] - rk_out}, '
          f'dim(W supported off star(k)) = {Wm.shape[1] - rk_in}')
supp = sorted(sum(1 for v in vec if v != 0) for vec in Wb)
print('(d) support sizes of the RREF null-space basis:', supp)
vals = sorted({abs(v) for vec in Wb for v in vec if v != 0})
print('    distinct |entries| in that basis:', [str(v) for v in vals][:12])

# --- follow-up (same pre-registered question (c)): the vectors w_k, one per coordinate
ws = []
for k in range(m):
    inside = [c for c in range(nc) if k in cells[c]]
    A = Wm[inside, :]
    _, s, vt = np.linalg.svd(A)
    y = vt[-1]                                   # null vector of the star rows
    w = Wm @ y
    w = w / np.abs(w[np.abs(w) > 1e-9]).min()
    ws.append(w)
    vals = sorted({round(float(abs(v)), 6) for v in w if abs(v) > 1e-9})
    if k < 3:
        print(f'   w_{k}: support {int((np.abs(w) > 1e-9).sum())} cells (all avoid {k}); |entries| {vals}')
Wk = np.array(ws).T
print('    rank of {w_0..w_10}:', np.linalg.matrix_rank(Wk), '| relations (11 - rank):', 11 - np.linalg.matrix_rank(Wk))
