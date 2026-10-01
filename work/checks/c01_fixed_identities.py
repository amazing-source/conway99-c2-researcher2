# C01: exact identities for the fixed data R, M (no unknowns). Integer arithmetic only.
import numpy as np, itertools
cells = list(itertools.combinations(range(7), 2))
R = []
for (i, j) in cells:
    for s in (+1, -1):
        r = [0]*7; r[i] = 1; r[j] = s; R.append(r)
R = np.array(R, dtype=np.int64); M = np.abs(R)
assert (R.T @ R == 12*np.eye(7, dtype=np.int64)).all()
assert (M.T @ M == 10*np.eye(7, dtype=np.int64) + 2).all()
G = R @ R.T; MM = M @ M.T
Gam = (MM + G)//2; Del = (MM - G)//2          # agree / disagree counts
off = ~np.eye(42, dtype=bool)
print("sum_{u!=v} Gamma =", Gam[off].sum(), " sum_{u!=v} Delta =", Del[off].sum())
print("R^T 1 =", R.sum(0), " |P_R 1|^2*3 =", (R.sum(0)**2).sum()*3//12)
# chi: R 1_7 = 2 chi
print("R 1_7 / 2 == chi (plus-index indicator):", ((R.sum(1)//2) == np.array([1,0]*21)).all())
