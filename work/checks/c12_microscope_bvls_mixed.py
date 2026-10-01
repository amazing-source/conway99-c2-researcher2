"""c12 microscope (one process, < 10 s, < 200 MB). Exact question:
In the only real analogue (BvLS, m = 11, all-sibling), do the mixed objects built from the coupling
(Q, N) -- the Gaussian type matrix Z = (Q - J + I) + iN, the matching compression N + DND, the
matching-twisted product ND -- satisfy a low-degree identity that the separate equations do not give?"""
import numpy as np, itertools
N = np.load('data/bvls_m11_N.npy'); D = np.load('data/bvls_m11_D.npy')
n = N.shape[0]; I = np.eye(n, dtype=np.int64); J = np.ones((n, n), dtype=np.int64)
B = np.abs(N); Q = B + 2 * D
print('n =', n, ' Q entries', sorted(set(Q.flatten())), ' coupling (Q-1)^2+N^2 = 1 off diag:',
      bool((((Q - 1) ** 2 + N ** 2)[~np.eye(n, dtype=bool)] == 1).all()))
Z = (Q - J + I) + 1j * N
def spec(Mx, herm=False, tol=1e-6):
    ev = np.linalg.eigvalsh(Mx) if herm else np.linalg.eigvals(Mx)
    vals = []
    for e in sorted(ev, key=lambda z: (round(z.real, 4), round(getattr(z, 'imag', 0), 4))):
        for v in vals:
            if abs(v[0] - e) < tol:
                v[1] += 1; break
        else:
            vals.append([e, 1])
    return [(np.round(v[0], 4), v[1]) for v in vals]
print('distinct eigenvalues of Z (count):', len(spec(Z)))
print('Z Z^* hermitian spectrum:', spec(Z @ Z.conj().T, herm=True)[:12])
print('N + DND spectrum:', spec(N + D @ N @ D, herm=True))
print('commutator [N,D] zero?', bool((N @ D == D @ N).all()))
ND = N @ D
print('tr((ND)^2) =', int(np.trace(ND @ ND)))
beta2 = sum(1 for x in range(n) for y in range(x + 1, n) if (B @ D)[x, y] + (D @ B)[x, y] == 2)
print('beta=2 pairs b2 =', beta2)
