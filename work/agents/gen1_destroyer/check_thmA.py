# gen1_destroyer: auxiliary checks for Theorem A / Lemma S.  Single process, memory < 300 MB, runtime < 1 min.
# (1) m-specificity of Lemma S on the m=11 BvLS calibration (all cells sib there).
# (2) orbit-triangle counts on BvLS (tau+, tau-, tauD) with the boolean bug of calib_m11.py fixed.
# (3) GF(2) check of the second proof route of Theorem A: on the Kneser graph KG(7,2), every +-1 edge labelling
#     with product +1 on all triangles is a coboundary  =>  B = 2 copies of KG(7,2)  =>  (B^2)_xy in {0,6} != 3.
#     Also checks the complement-pair parity lemma as a linear functional on the cocycle space.
import numpy as np, itertools, collections
from calib_m11 import build_R, load, check_kernel

def gf2_rank(Mat):
    A = (Mat.copy() % 2).astype(np.uint8); r = 0; rows, cols = A.shape
    for c in range(cols):
        piv = np.nonzero(A[r:, c])[0]
        if len(piv) == 0: continue
        p = r + piv[0]; A[[r, p]] = A[[p, r]]
        nz = np.nonzero(A[:, c])[0]; nz = nz[nz != r]
        A[nz] ^= A[r]; r += 1
        if r == rows: break
    return r

# (1),(2)
m = 11; N, D = load(m); ok, R, Q, H, K, M = check_kernel(m, N, D); B = np.abs(N); n = len(R)
cells = [(i, j) for i in range(m) for j in range(i + 1, m)]
hist = collections.Counter(); cover = collections.Counter()
for c, cc in enumerate(cells):
    x, xp = 2 * c, 2 * c + 1
    covered = 0; tot = 0
    for d, dd in enumerate(cells):
        if set(cc) & set(dd): continue
        y, yp = 2 * d, 2 * d + 1
        blk = B[np.ix_([x, xp], [y, yp])]
        hist[tuple(blk.flatten())] += 1
        covered += int(((blk.sum(0)) == 1).sum()); tot += 2
    cover[(covered, tot)] += 1
print("m=11 B-blocks between disjoint sib cells (x,x')x(y,y') histogram:", dict(hist))
print("m=11 #orbits of disjoint cells covered exactly once by {x,x'} / total:", dict(cover))
tp = tm = td = 0
for x, y, z in itertools.combinations(range(n), 3):
    if Q[x, y] == 0 or Q[y, z] == 0 or Q[x, z] == 0: continue
    nd = int(D[x, y] + D[y, z] + D[x, z])
    if nd == 1: td += 1
    elif nd == 0:
        if N[x, y] * N[y, z] * N[x, z] > 0: tp += 1
        else: tm += 1
print("m=11 orbit triangles: tau+ =", tp, " tau- =", tm, " tauD =", td)

# (3) KG(7,2)
m7 = 7; C7 = [frozenset(p) for p in itertools.combinations(range(m7), 2)]
E = [(a, b) for a, b in itertools.combinations(range(21), 2) if not (C7[a] & C7[b])]
eid = {e: i for i, e in enumerate(E)}
T = [t for t in itertools.combinations(range(21), 3) if all(not (C7[u] & C7[v]) for u, v in itertools.combinations(t, 2))]
Bd = np.zeros((len(T), len(E)), np.uint8)          # triangle -> its 3 edges  (delta_1^T)
for i, (a, b, c) in enumerate(T):
    for e in [(a, b), (a, c), (b, c)]: Bd[i, eid[e]] = 1
Cob = np.zeros((len(E), 21), np.uint8)              # vertex -> incident edges (delta_0)
for i, (a, b) in enumerate(E): Cob[i, a] = Cob[i, b] = 1
rT = gf2_rank(Bd); rC = gf2_rank(Cob)
print("KG(7,2): |E| =", len(E), "|T| =", len(T), " rank(triangle map) =", rT,
      " dim cocycles =", len(E) - rT, " dim coboundaries =", rC)
# parity functional: for c={0,1}, c''={0,2}, W={3,4,5,6}: sum over d subset W of psi(c,d)+psi(c'',d)
c1, c2 = C7.index(frozenset({0, 1})), C7.index(frozenset({0, 2}))
f = np.zeros(len(E), np.uint8)
for d in itertools.combinations(range(3, 7), 2):
    dd = C7.index(frozenset(d))
    f[eid[tuple(sorted((c1, dd)))]] ^= 1; f[eid[tuple(sorted((c2, dd)))]] ^= 1
# f vanishes on cocycles  <=>  f lies in the row space of Bd
print("parity functional lies in span of triangle relations:", gf2_rank(np.vstack([Bd, f])) == rT)
