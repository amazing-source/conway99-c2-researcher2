# C03: Calibration on an EXISTING graph: Berlekamp-van Lint-Seidel srg(243,22,1,2) (m=11 analogue).
# Cayley graph on GF(3)^5 with connection set {+-h_i}, h_i = x^i mod g(x), g | x^11-1 over GF(3), deg 5.
# Builds canonical coordinates at vertex 0 with involution x->-x, extracts N, D, pi, types, and checks
# the m-general versions of: (deg), (R2'), (E+),(E-), NR=0, N^2=N+(2m-2)I-RR^T, mod-2 structure.
# Exact integer arithmetic (numpy int64). Memory < 50 MB.
import itertools, numpy as np
p = 3
def polymod(a, g):            # a, g: coefficient lists low->high over GF(3)
    a = a[:]
    while len(a) >= len(g):
        c = a[-1] % p
        if c:
            sh = len(a) - len(g)
            for i, gi in enumerate(g): a[sh+i] = (a[sh+i] - c*gi) % p
        a.pop()
    return [x % p for x in a] + [0]*(len(g)-1-len(a))
# find monic degree-5 g dividing x^11 - 1
x11m1 = [p-1] + [0]*10 + [1]
g = None
for coeffs in itertools.product(range(3), repeat=5):
    cand = list(coeffs) + [1]
    if coeffs[0] == 0: continue
    if all(v == 0 for v in polymod(x11m1, cand)) and cand != [p-1,1]:
        g = cand; break
print("g =", g)
h = [tuple(polymod([0]*i + [1], g)) for i in range(11)]
S = set()
for v in h:
    S.add(v); S.add(tuple((-c) % 3 for c in v))
assert len(S) == 22
V = list(itertools.product(range(3), repeat=5)); idx = {v:i for i,v in enumerate(V)}
n = len(V)
A = np.zeros((n,n), dtype=np.int64)
for v in V:
    for s in S:
        w = tuple((a+b) % 3 for a,b in zip(v,s)); A[idx[v], idx[w]] = 1
I = np.eye(n, dtype=np.int64); J = np.ones((n,n), dtype=np.int64)
assert (A == A.T).all() and (A.sum(1) == 22).all()
assert (A@A + A == 20*I + 2*J).all(), "not srg(243,22,1,2)"
print("srg(243,22,1,2) verified")
m = 11
neg = lambda v: tuple((-c) % 3 for c in v)
add = lambda a,b: tuple((x+y) % 3 for x,y in zip(a,b))
# canonical coordinates: inner (i,+) = h_i, (i,-) = -h_i ; root s e_i + t e_j <-> s h_i + t h_j
def vert(i,s,j,t):
    a = h[i] if s == 1 else neg(h[i]); b = h[j] if t == 1 else neg(h[j]); return add(a,b)
cells = list(itertools.combinations(range(m), 2))
pos = []  # positive roots: (c,+) = e_i+e_j, (c,-) = e_i-e_j
for (i,j) in cells:
    pos.append((i,j,1)); pos.append((i,j,-1))
P = len(pos)
R = np.zeros((P, m), dtype=np.int64)
for u,(i,j,e) in enumerate(pos): R[u,i] = 1; R[u,j] = e
Mm = np.abs(R)
vp = [idx[vert(i,1,j,e)] for (i,j,e) in pos]
vn = [idx[neg(vert(i,1,j,e))] for (i,j,e) in pos]
a = np.array([[A[vp[u], vp[v]] for v in range(P)] for u in range(P)])
b = np.array([[A[vp[u], vn[v]] for v in range(P)] for u in range(P)])
assert (a == a.T).all() and (b == b.T).all()
N = b - a; D = a*b; B = np.abs(N)
assert set(np.unique(N)) <= {-1,0,1}
IP = np.eye(P, dtype=np.int64); JP = np.ones((P,P), dtype=np.int64)
print("diag N zero:", (np.diag(N)==0).all(), " diag D zero:", (np.diag(D)==0).all())
print("D perfect matching:", (D.sum(1)==1).all() and (D==D.T).all())
print("B degree set:", set(B.sum(1)), " (expect 2m-4 =", 2*m-4, ")")
print("NR == 0:", (N@R == 0).all())
print("N^2 == N + (2m-2)I - RR^T:", (N@N == N + (2*m-2)*IP - R@R.T).all())
T = 2*np.ones((P,m),dtype=np.int64) - Mm - (B@Mm)//2
print("DM == T:", (D@Mm == T).all(), " BM even:", ((B@Mm) % 2 == 0).all())
E = (8*IP + 4*JP - Mm@Mm.T - B@B - B)
print("BD+DB+D == E/2 off-diag:", ((2*(B@D + D@B + D) - E)[~np.eye(P,dtype=bool)] == 0).all())
pi = D.argmax(1)
t = np.array([ (Mm[u]*Mm[pi[u]]).sum() for u in range(P)])
print("type distribution t=0,1,2 (orbits):", [(t==k).sum() for k in range(3)])
# mod-2 structure
G = (Mm@Mm.T) % 2; B2 = B % 2
print("mod2: B^2+B == G:", (((B2@B2 + B2) % 2) == G).all(), " BG==0:", ((B2@G % 2) == 0).all())
def rank2(Mx):
    Mx = Mx.copy() % 2; r = 0; rows, cols = Mx.shape
    for c in range(cols):
        piv = np.nonzero(Mx[r:, c])[0]
        if len(piv) == 0: continue
        pr = r + piv[0]; Mx[[r, pr]] = Mx[[pr, r]]
        nz = np.nonzero(Mx[:, c])[0]
        for i in nz:
            if i != r: Mx[i] ^= Mx[r]
        r += 1
        if r == rows: break
    return r
print("rank2 B =", rank2(B2), " rank2(B+I) =", rank2((B2 + IP) % 2), " rank2 G =", rank2(G))
ev = np.round(np.linalg.eigvalsh(N.astype(float)), 6); vals, cnt = np.unique(ev, return_counts=True)
print("spectrum N:", dict(zip(vals, cnt)))
# cell-diagonal q(c) and kappa relations
q = [int(a[2*c,2*c+1] + b[2*c,2*c+1]) for c in range(len(cells))]
print("q(c) distribution:", {k: q.count(k) for k in set(q)})
np.save("C:/Users/bfhdh/Downloads/conway_c2_researcher2_start_2026_09_30/conway_c2_researcher2_start_2026_09_30/work/data/bvls_m11_N.npy", N)
np.save("C:/Users/bfhdh/Downloads/conway_c2_researcher2_start_2026_09_30/conway_c2_researcher2_start_2026_09_30/work/data/bvls_m11_D.npy", D)
