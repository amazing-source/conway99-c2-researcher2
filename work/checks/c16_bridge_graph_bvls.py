r"""c16 microscope (one process, < 60 s, < 300 MB). Exact question (OVERLAP_EXPLORATION.md s.5): in BvLS (m = 11),
rebuilt as a 243-vertex graph from the saved orbit data (N, D) and the positive roots of D11, does every orbit's bridge
graph G_x (edges between N(x+) minus {pi x lifts} and N(x-) minus {pi x lifts}) have (i) degrees 2 - a with exactly
two degree-1 vertices on each side, (ii) exactly two path components, (iii) exactly two sigma-fixed edges, and
(iv) phase alpha (both paths sigma-invariant), as derived for type-2 orbits?"""
import numpy as np, itertools, collections
N = np.load('data/bvls_m11_N.npy'); D = np.load('data/bvls_m11_D.npy'); n = N.shape[0]; m = 11
cells = list(itertools.combinations(range(m), 2))
R = np.zeros((n, m), dtype=int)
for u, ((i, j), e) in enumerate(itertools.product(cells, (1, -1))):
    R[u, i] = 1; R[u, j] = e
B = np.abs(N); Q = B + 2 * D; a = (Q - N) // 2; b = (Q + N) // 2
# vertices: 0 = v0; inner (k, s) -> 1 + 2k + (s<0); exterior (x, eps) -> 1 + 2m + 2x + (eps<0)
V = 1 + 2 * m + 2 * n
def inner(k, s): return 1 + 2 * k + (1 if s < 0 else 0)
def ext(x, e): return 1 + 2 * m + 2 * x + (1 if e < 0 else 0)
A = np.zeros((V, V), dtype=np.int64)
for k in range(m):
    for s in (1, -1):
        A[0, inner(k, s)] = A[inner(k, s), 0] = 1
    A[inner(k, 1), inner(k, -1)] = A[inner(k, -1), inner(k, 1)] = 1
for x in range(n):
    for e in (1, -1):
        for k in range(m):
            if R[x, k] != 0:
                s = e * R[x, k]
                A[ext(x, e), inner(k, s)] = A[inner(k, s), ext(x, e)] = 1
        for y in range(n):
            for d in (1, -1):
                if (e * d == 1 and a[x, y]) or (e * d == -1 and b[x, y]):
                    A[ext(x, e), ext(y, d)] = 1
I = np.eye(V, dtype=np.int64); J = np.ones((V, V), dtype=np.int64)
k = 2 * m
print('rebuilt graph is srg(%d,%d,1,2):' % (V, k), bool((A == A.T).all() and (A.sum(1) == k).all()
      and (A @ A + A == (k - 2) * I + 2 * J).all()))
sigma = {0: 0}
for kk in range(m):
    sigma[inner(kk, 1)] = inner(kk, -1); sigma[inner(kk, -1)] = inner(kk, 1)
for x in range(n):
    sigma[ext(x, 1)] = ext(x, -1); sigma[ext(x, -1)] = ext(x, 1)
pi = [int(np.nonzero(D[x])[0][0]) for x in range(n)]
summary = collections.Counter(); bad = []
for x in range(n):
    xp, xm = ext(x, 1), ext(x, -1)
    excl = {ext(pi[x], 1), ext(pi[x], -1)}
    U = [v for v in np.nonzero(A[xp])[0] if v not in excl]
    W = [v for v in np.nonzero(A[xm])[0] if v not in excl]
    Ws = set(W)
    E = [(u, w) for u in U for w in W if A[u, w]]
    deg = collections.Counter()
    for u, w in E: deg[u] += 1; deg[w] += 1
    d1U = sum(1 for u in U if deg[u] == 1); d1W = sum(1 for w in W if deg[w] == 1)
    fixed = sum(1 for u, w in E if sigma[u] == w)
    adj = collections.defaultdict(list)
    for u, w in E: adj[u].append(w); adj[w].append(u)
    seen = set(); paths = []; cycles = 0
    for v in U + W:
        if v in seen or deg[v] != 1: continue
        comp = [v]; seen.add(v); cur, prev = v, None
        while True:
            nxt = [t for t in adj[cur] if t != prev]
            if not nxt: break
            prev, cur = cur, nxt[0]; comp.append(cur); seen.add(cur)
        paths.append(comp)
    rest = [v for v in U + W if v not in seen]
    inv = [all(sigma[v] in set(p) for v in p) for p in paths]
    phase = 'alpha' if all(inv) else ('beta' if not any(inv) else 'mixed')
    t = int((R[x] != 0).astype(int) @ (R[pi[x]] != 0).astype(int))
    summary[(t, len(U), d1U, d1W, len(paths), fixed, phase)] += 1
    if not (d1U == 2 and d1W == 2 and len(paths) == 2 and fixed == 2): bad.append(x)
print('(type, |U|, deg1 in U, deg1 in W, #paths, #fixed edges, phase) -> #orbits:', dict(summary))
print('orbits violating the derived structure:', len(bad))
