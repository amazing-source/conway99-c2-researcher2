# gen1_destroyer calibration script.  Single process, memory bound < 600 MB, runtime < 2 min.
# Input: work/data/bvls_m11_N.npy, bvls_m11_D.npy (m=11 analogue, same normalized form).
# Checks the CP_m representation (X2),(X3), the square-complex Hodge claim, and prints
# statistics of the transition system / triangles used in NOTES.md.
import numpy as np, itertools, collections, sys
np.set_printoptions(linewidth=200)
BASE = "C:/Users/bfhdh/Downloads/conway_c2_researcher2_start_2026_09_30/conway_c2_researcher2_start_2026_09_30/"

def build_R(m):
    rows, cells = [], []
    for i in range(m):
        for j in range(i + 1, m):
            r = np.zeros(m, int); r[i] = 1; r[j] = 1; rows.append(r)
            r = np.zeros(m, int); r[i] = 1; r[j] = -1; rows.append(r)
            cells.append((i, j))
    return np.array(rows), cells

def load(m):
    N = np.load(BASE + "work/data/bvls_m11_N.npy").astype(int)
    D = np.load(BASE + "work/data/bvls_m11_D.npy").astype(int)
    return N, D

def check_kernel(m, N, D):
    R, cells = build_R(m); n = len(R); M = np.abs(R); H = R @ R.T; K = M @ M.T
    I = np.eye(n, dtype=int); J = np.ones((n, n), int)
    Q = np.abs(N) + 2 * D
    ok = {}
    ok['NR=0'] = not (N @ R).any()
    ok['C2b'] = (N @ N == N + (2*m-2) * I - H).all()
    ok['C3'] = (Q @ Q + Q + K == (2*m-2) * I + 4 * J).all()
    ok['C4'] = (Q @ M == 4 * np.ones((n, m), int) - 2 * M).all()
    off = ~np.eye(n, dtype=bool)
    ok['C5'] = (((Q - 1) ** 2 + N ** 2)[off] == 1).all()
    ok['diag'] = (np.diag(Q) == 0).all() and (np.diag(N) == 0).all()
    return ok, R, Q, H, K, M

def exterior(m, R, Q, N):
    n = len(R)
    a = (Q - N) // 2; b = (Q + N) // 2
    X = np.block([[a, b], [b, a]])
    roots = np.vstack([R, -R])                       # vertex x: r_x, vertex x+n: -r_x
    P = 2 * m                                       # point 2k = +e_k, 2k+1 = -e_k
    Inc = np.zeros((2 * n, P), int)
    for v, r in enumerate(roots):
        for k in range(m):
            if r[k] == 1: Inc[v, 2 * k] = 1
            if r[k] == -1: Inc[v, 2 * k + 1] = 1
    Pi = np.zeros((P, P), int)
    for k in range(m): Pi[2 * k, 2 * k + 1] = Pi[2 * k + 1, 2 * k] = 1
    L = Inc @ Inc.T - 2 * np.eye(2 * n, dtype=int)
    I2 = np.eye(2 * n, dtype=int); J2 = np.ones((2 * n, 2 * n), int)
    ok = {}
    ok['X2'] = (X @ Inc == 2 - Inc - Inc @ Pi).all()
    ok['X3'] = (X @ X + X + L == (2 * m - 4) * I2 + 2 * J2).all()
    # full graph
    V = 1 + P + 2 * n
    A = np.zeros((V, V), int)
    A[0, 1:1 + P] = A[1:1 + P, 0] = 1
    A[1:1 + P, 1:1 + P] = Pi
    A[1:1 + P, 1 + P:] = Inc.T; A[1 + P:, 1:1 + P] = Inc
    A[1 + P:, 1 + P:] = X
    IV = np.eye(V, dtype=int); JV = np.ones((V, V), int)
    ok['SRG'] = (A @ A + A == (2 * m - 2) * IV + 2 * JV).all() and (A == A.T).all() and not np.diag(A).any()
    return ok, X, roots, Inc, L, A

def hodge(A, m):
    V = len(A)
    edges = [(i, j) for i in range(V) for j in range(i + 1, V) if A[i, j]]
    eid = {e: t for t, e in enumerate(edges)}
    def sedge(u, w):  # oriented edge u->w as (index, sign)
        return (eid[(u, w)], 1) if u < w else (eid[(w, u)], -1)
    cells = []
    A2 = A @ A
    for (u, w) in edges:                         # triangles
        for z in np.nonzero(A[u] & A[w])[0]:
            if z > w: cells.append([u, w, z])
    nt = len(cells)
    for u in range(V):                           # induced squares u c1 w c2, u<w non-adjacent
        for w in range(u + 1, V):
            if not A[u, w]:
                c = np.nonzero(A[u] & A[w])[0]
                assert len(c) == 2 and not A[c[0], c[1]]
                if True:
                    cells.append([u, c[0], w, c[1]])
    # each square appears twice (two diagonals): dedupe
    seen = set(); uniq = []
    for c in cells:
        key = frozenset(c) if len(c) == 4 else ('t',) + tuple(c)
        if key in seen: continue
        seen.add(key); uniq.append(c)
    cells = uniq
    d2 = np.zeros((len(edges), len(cells)), np.int8)
    for t, c in enumerate(cells):
        for i in range(len(c)):
            e, s = sedge(c[i], c[(i + 1) % len(c)])
            d2[e, t] = s
    d1 = np.zeros((V, len(edges)), np.int8)
    for t, (u, w) in enumerate(edges): d1[u, t] = -1; d1[w, t] = 1
    Lap = d1.T.astype(np.int32) @ d1.astype(np.int32) + d2.astype(np.int32) @ d2.T.astype(np.int32)
    O = Lap - (2 * m + 1) * np.eye(len(edges), dtype=np.int32)
    share = (np.abs(d1.T.astype(np.int32)) @ np.abs(d1.astype(np.int32))) > 0
    np.fill_diagonal(share, False)
    res = dict(V=V, E=len(edges), T=nt, S=len(cells) - nt,
               diag_ok=bool((np.diag(Lap) == 2 * m + 1).all()),
               shared_vertex_entries_zero=bool((O[share] == 0).all()),
               O_row_nnz=sorted(set((O != 0).sum(1).tolist())))
    ev = np.linalg.eigvalsh(Lap.astype(float))
    res['lap_min_eig'] = float(ev.min())
    return res

def transition_stats(m, n, X, roots, Inc, Q, N, D, K):
    P = 2 * m
    neg = lambda p: p ^ 1
    # mu_h : for each point h, matching on roots through h
    mu = {}
    for h in range(P):
        through = np.nonzero(Inc[:, h])[0]
        sub = X[np.ix_(through, through)]
        assert (sub.sum(1) == 1).all(), "not a perfect matching"
        other = lambda v: [p for p in np.nonzero(Inc[v])[0] if p != h][0]
        for i, v in enumerate(through):
            w = through[np.nonzero(sub[i])[0][0]]
            mu[(h, other(v))] = other(w)
    alpha = sum(1 for (h, g), g2 in mu.items() if g2 == neg(g))
    # half-edge graph X_h on roots and its cycles
    Xh = X * (Inc @ Inc.T > 0)
    assert (Xh.sum(1) == 2).all()
    seen = np.zeros(2 * n, bool); cyc = []
    for s in range(2 * n):
        if seen[s]: continue
        c = [s]; seen[s] = True; prev = -1; cur = s
        while True:
            nb = [w for w in np.nonzero(Xh[cur])[0] if w != prev]
            nxt = nb[0] if nb else np.nonzero(Xh[cur])[0][0]
            if nxt == s: break
            if seen[nxt]: break
            seen[nxt] = True; c.append(nxt); prev, cur = cur, nxt
        inv = ((s + n) % (2 * n)) in set(c)
        cyc.append((len(c), inv))
    # cell states and D types
    st = collections.Counter()
    for c in range(n // 2):
        x, y = 2 * c, 2 * c + 1
        st[{(0, 0): 'n', (2, 0): 'd', (1, -1): 'm', (1, 1): 'p'}[(Q[x, y], N[x, y])]] += 1
    dpart = D.argmax(1)
    dtyp = collections.Counter(int(K[x, dpart[x]]) for x in range(n) if x < dpart[x])
    # X-triangles and shadow types
    tri = []
    for u in range(2 * n):
        for w in np.nonzero(X[u])[0]:
            if w <= u: continue
            for z in np.nonzero(X[u] & X[w])[0]:
                if z > w: tri.append((u, w, z))
    shadow = collections.Counter()
    for t in tri:
        sup = [tuple(np.nonzero(roots[v])[0]) for v in t]
        deg = collections.Counter(k for s in sup for k in s)
        dd = tuple(sorted(deg.values(), reverse=True))
        edges = [frozenset(s) for s in sup]
        if len(set(edges)) < 3: kind = 'repeated-cell'
        elif dd == (2, 2, 2): kind = 'K3'
        elif dd == (2, 2, 1, 1): kind = 'P4'
        elif dd == (2, 1, 1, 1, 1): kind = 'P3+K2'
        elif dd == (1,) * 6: kind = '3K2'
        else: kind = str(dd)
        shadow[kind] += 1
    # orbit-level triangle signs
    B = np.abs(N)
    tp = tm = td = 0
    for x, y, z in itertools.combinations(range(n), 3):
        q = (Q[x, y] > 0) + (Q[y, z] > 0) + (Q[x, z] > 0)
        if q < 3: continue
        nd = D[x, y] + D[y, z] + D[x, z]
        if nd == 1: td += 1
        elif nd == 0:
            if N[x, y] * N[y, z] * N[x, z] > 0: tp += 1
            else: tm += 1
    return dict(alpha=alpha, cell_states=dict(st), D_types_by_K=dict(dtyp),
                Xh_cycles=collections.Counter(cyc), n_X_triangles=len(tri), shadows=dict(shadow),
                tau_plus=tp, tau_minus=tm, tau_D=td), mu

if __name__ == "__main__":
    m = 11
    N, D = load(m)
    ok, R, Q, H, K, M = check_kernel(m, N, D); print("kernel", ok)
    ok2, X, roots, Inc, L, A = exterior(m, R, Q, N); print("CP-representation", ok2)
    stats, mu = transition_stats(m, len(R), X, roots, Inc, Q, N, D, K)
    for k, v in stats.items(): print(k, v)
    if len(sys.argv) > 1 and sys.argv[1] == 'hodge':
        print("hodge", hodge(A, m))
