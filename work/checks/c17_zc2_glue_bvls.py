r"""c17 (one process, < 1 min, < 200 MB). Exact question (Z_C2_FREENESS_REDUNDANCY.md s.2-4) on BvLS, m = 11
(odd eigenvalues 4, -5; even 22, 4, -5): (a) with the true (Q, N), do the explicit glue maps send every generator
u = (A_- - theta')e_i of U_theta to an integral theta-eigenvector w of B_+ with w_inf even and w_orb = u (mod 2)?
(b) with the relaxed pair (Q' = Q with the two orbits of one cell swapped, N unchanged), do both separate systems
still hold while the congruence fails, i.e. Q' != N (mod 2)?"""
import numpy as np, itertools
N = np.load('data/bvls_m11_N.npy'); D = np.load('data/bvls_m11_D.npy'); n = N.shape[0]; m = 11
cells = list(itertools.combinations(range(m), 2))
R = np.zeros((n, m), dtype=np.int64)
for u, ((i, j), e) in enumerate(itertools.product(cells, (1, -1))): R[u, i] = 1; R[u, j] = e
M = np.abs(R); Q = np.abs(N) + 2 * D
Am = np.block([[-np.eye(m, dtype=np.int64), R.T], [R, -N]])
def Bplus(Qx):
    top = np.concatenate([[0], 2 * np.ones(m, dtype=np.int64), np.zeros(n, dtype=np.int64)])
    mid = np.hstack([np.ones((m, 1), dtype=np.int64), np.eye(m, dtype=np.int64), M.T])
    bot = np.hstack([np.zeros((n, 1), dtype=np.int64), M, Qx])
    return np.vstack([top, mid, bot])
Jh = np.vstack([np.concatenate([[1], 2 * np.ones(m + n, dtype=np.int64)])] * (1 + m + n))
I1 = np.eye(m + n, dtype=np.int64); I2 = np.eye(1 + m + n, dtype=np.int64)
print('odd identity A_-^2 + A_- = 20I:', bool((Am @ Am + Am == 20 * I1).all()))
def run(Qx, name):
    B = Bplus(Qx)
    print(f'[{name}] even identity B^2 + B = 20I + 2J^:', bool((B @ B + B == 20 * I2 + 2 * Jh).all()),
          '| Q = N (mod 2):', bool(((Qx - N) % 2 == 0).all()))
    glue = {4: 45 * I2 + 9 * B - Jh, -5: 108 * I2 - 27 * B + 2 * Jh}       # 81 E_4 and 243 E_-5 on V+
    gen = {4: Am + 5 * I1, -5: 4 * I1 - Am}                                # 9 x odd projectors
    bad = 0; tot = 0
    for th in (4, -5):
        U = gen[th]
        assert ((Am - th * I1) @ U == 0).all()
        for c in range(m + n):
            u = U[:, c]
            if not u.any(): continue
            w = glue[th] @ np.concatenate([[0], u]); tot += 1
            ok = ((B - th * I2) @ w == 0).all() and w[0] % 2 == 0 and ((w[1:] - u) % 2 == 0).all()
            bad += (not ok)
    print(f'[{name}] glue generators tested: {tot}, failures: {bad}')
run(Q, 'true (Q,N)')
P = np.arange(n); c0 = 0; P[[2 * c0, 2 * c0 + 1]] = P[[2 * c0 + 1, 2 * c0]]      # swap the two orbits of cell 0
Qr = Q[np.ix_(P, P)]
print('relaxed Q\' entries with Q\' != N (mod 2):', int(((Qr - N) % 2 != 0).sum()))
run(Qr, 'relaxed (Q\',N)')
