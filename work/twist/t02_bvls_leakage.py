r"""C-T2 (pre-registered in TWIST_CALCULUS.md s.1a). Calibration on BvLS, m = 11.

Quantities:
 (1) D = kappa: every cell is flat (type 2).
 (2) For every ordered pair (e, c) of DISJOINT cells, the 2x2 block B[e,c]. Count the permutation blocks and the others
     ("half-blocks"). Report the distribution of the leakage zeta(e,c) = Q(e->c+) - Q(e->c-).
 (3) Alt compression Q_A = U^T Q U / 2 and leakage Z = (I - U U^T/2) Q U, with u_c = e_(c+) - e_(c-).
     Check the C2 s.8 identity at m = 11: Q_A^2 + Q_A + Z^T Z / 2 = 20 I. Report ||Z||^2, tr Q_A, and the spectrum
     range of Q_A.
     Prediction (trace argument): if Z = 0, then 9a = 165 is not an integer, so ||Z||^2 > 0.
 (4) Lower bound on mult(4, Q_A): 55 + 55 - 99 = 11 (interlacing count).

Run from work/. One process, < 10 s, < 100 MB.
"""
import itertools
import numpy as np

N = np.load('data/bvls_m11_N.npy')
D = np.load('data/bvls_m11_D.npy')
n, m = N.shape[0], 11
cells = list(itertools.combinations(range(m), 2))
nc = len(cells)
B = np.abs(N)
Q = B + 2 * D

flat = all(D[2 * c, 2 * c + 1] == 1 for c in range(nc))
print('(1) D = kappa (all 55 cells flat):', flat)

perm = half = 0
zeta_hist = {}
for e in range(nc):
    for c in range(nc):
        if e == c or set(cells[e]) & set(cells[c]):
            continue
        blk = B[2 * e:2 * e + 2, 2 * c:2 * c + 2]
        if (blk.sum(0) == 1).all() and (blk.sum(1) == 1).all():
            perm += 1
        else:
            half += 1
        z = int(Q[2 * e:2 * e + 2, 2 * c].sum() - Q[2 * e:2 * e + 2, 2 * c + 1].sum())
        zeta_hist[z] = zeta_hist.get(z, 0) + 1
print(f'(2) ordered disjoint cell pairs: {perm + half}; permutation blocks {perm}; half-blocks {half}')
print('    zeta(e,c) distribution:', dict(sorted(zeta_hist.items())))

U = np.zeros((n, nc))
for c in range(nc):
    U[2 * c, c], U[2 * c + 1, c] = 1, -1
QA = U.T @ Q @ U / 2
Z = (np.eye(n) - U @ U.T / 2) @ Q @ U
lhs = QA @ QA + QA + Z.T @ Z / 2
print('(3) identity Q_A^2 + Q_A + Z^T Z/2 = 20 I:', bool(np.allclose(lhs, 20 * np.eye(nc))))
print(f'    ||Z||^2 = {float((Z ** 2).sum()):.3f};  tr Q_A = {float(np.trace(QA)):.1f}')
ev = np.linalg.eigvalsh(QA)
print(f'    spectrum of Q_A in [{ev.min():.4f}, {ev.max():.4f}] (must lie in [-5, 4])')
print(f'(4) mult of eigenvalue 4 in Q_A: {int(np.sum(np.abs(ev - 4) < 1e-8))} (lower bound 11); '
      f'mult of -5: {int(np.sum(np.abs(ev + 5) < 1e-8))}')
