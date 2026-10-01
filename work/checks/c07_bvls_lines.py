# C07: sanity check of the line trichotomy on the only existing example (BvLS, m = 11).
# Checks: every B-edge is exactly one of {star, apex (beta=1), E*}; negative B-triangles partition E*;
# T_- = m(m-1)(m-5)/3 + n1 + 2 n2; e_F parity. Uses data saved by c03.
import numpy as np, itertools
W = r"C:\Users\bfhdh\Downloads\conway_c2_researcher2_start_2026_09_30\conway_c2_researcher2_start_2026_09_30\work\data"
N = np.load(W + r"\bvls_m11_N.npy"); D = np.load(W + r"\bvls_m11_D.npy"); m = 11
cells = list(itertools.combinations(range(m), 2))
pos = [(i, j, e) for (i, j) in cells for e in (1, -1)]
R = np.zeros((len(pos), m), dtype=int)
for u, (i, j, e) in enumerate(pos): R[u, i] = 1; R[u, j] = e
B = np.abs(N); P = len(pos); pi = D.argmax(1)
s = (np.abs(R) @ np.abs(R).T)
t = np.array([s[x, pi[x]] for x in range(P)]); n2 = (t == 2).sum() // 2; n1 = (t == 1).sum() // 2
star = apex = estar = 0; bad = 0
beta = B @ D + D @ B
for x in range(P):
    for y in range(x + 1, P):
        if not B[x, y]: continue
        isstar = any(R[x, k] != 0 and R[y, k] != 0 and N[x, y] == -R[x, k] * R[y, k] for k in range(m))
        isapex = beta[x, y] == 1
        if isstar + isapex > 1 or beta[x, y] > 1: bad += 1
        if isstar: star += 1
        elif isapex: apex += 1
        else: estar += 1
tri_neg = 0; estar_cov = {}
for x, y, z in itertools.combinations(range(P), 3):
    if B[x, y] and B[y, z] and B[x, z] and N[x, y] * N[y, z] * N[x, z] == -1:
        tri_neg += 1
        for e in ((x, y), (y, z), (x, z)): estar_cov[e] = estar_cov.get(e, 0) + 1
print("B-edges:", int(B.sum() // 2), " star:", star, " apex:", apex, " E*:", estar, " conflicts:", bad)
print("negative triangles:", tri_neg, " predicted m(m-1)(m-5)/3+n1+2n2 =", m*(m-1)*(m-5)//3 + n1 + 2*n2)
print("each E*-edge in exactly one negative triangle:", len(estar_cov) == estar and set(estar_cov.values()) <= {1})
eF = int((N == -1).sum() // 2); print("e_F =", eF, " even:", eF % 2 == 0, " (n0,n1,n2) =", (21 if False else (len(pos)//2 - n1 - n2), n1, n2))
