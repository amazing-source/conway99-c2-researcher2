# C04: validation of work/code/unsigned_sat.py before any diagnostic use.
# (1) planted instances: random sparse (B, D); right-hand sides computed from them; the planted
#     assignment must be a model, and single perturbations must be refuted.
# (2) real encoding: the all-cells class (R4) and the extremal class (Lemma J) must be UNSAT.
# One process; memory < 2 GB; runtime < 5 min.
import sys, time, random, itertools
import numpy as np
sys.path.insert(0, r"C:\Users\bfhdh\Downloads\conway_c2_researcher2_start_2026_09_30\conway_c2_researcher2_start_2026_09_30\work\code")
import unsigned_sat as U
from pysat.solvers import Cadical153

def random_regular(n, d, rng):
    while True:
        stubs = [v for v in range(n) for _ in range(d)]
        rng.shuffle(stubs)
        E = set(); ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i + 1]
            if a == b or (min(a, b), max(a, b)) in E: ok = False; break
            E.add((min(a, b), max(a, b)))
        if ok: return E

def planted(seed):
    rng = random.Random(seed); n = U.NORB
    Eset = random_regular(n, 3, rng)
    B = np.zeros((n, n), dtype=np.int64)
    for a, b in Eset: B[a, b] = B[b, a] = 1
    while True:
        perm = list(range(n)); rng.shuffle(perm)
        D = np.zeros((n, n), dtype=np.int64); ok = True
        for i in range(0, n, 2):
            a, b = perm[i], perm[i + 1]
            if B[a, b]: ok = False; break
            D[a, b] = D[b, a] = 1
        if ok: break
    Mm = np.zeros((n, 7), dtype=np.int64)
    for x in range(n):
        for k in U.SUPP[x]: Mm[x, k] = 1
    K = B @ B + B; L = B @ D + D @ B + D; C = K + 2 * L
    cnt = B @ Mm; e = D @ Mm
    E = U.build(deg=list(B.sum(1)), base=lambda x, k: int(cnt[x, k] + 2 * e[x, k]),
                crhs=lambda x, y: int(C[x, y]), kmaxK=8, kmaxF=8)
    assum = []
    for x in range(n):
        for y in range(x + 1, n):
            assum.append(E.b(x, y) if B[x, y] else -E.b(x, y))
            assum.append(E.d(x, y) if D[x, y] else -E.d(x, y))
    return E, B, D, assum

t0 = time.time()
for seed in range(3):
    E, B, D, assum = planted(seed)
    with Cadical153(bootstrap_with=E.clauses) as S:
        r_true = S.solve(assumptions=assum)
        # perturbation 1: add a non-edge of B (not a D edge)
        n = U.NORB
        x, y = next((x, y) for x in range(n) for y in range(x + 1, n) if not B[x, y] and not D[x, y])
        a2 = [(-l if l == -E.b(x, y) else l) for l in assum]
        r_p1 = S.solve(assumptions=a2)
        # perturbation 2: rewire the matching on two D-pairs (keep disjoint from B if possible)
        pairs = [(x, y) for x in range(n) for y in range(x + 1, n) if D[x, y]]
        done = False
        for (a, b), (c, d) in itertools.combinations(pairs, 2):
            if not B[a, c] and not B[b, d]:
                D2 = D.copy(); D2[a, b] = D2[b, a] = D2[c, d] = D2[d, c] = 0; D2[a, c] = D2[c, a] = D2[b, d] = D2[d, b] = 1
                done = True; break
        a3 = []
        for x2 in range(n):
            for y2 in range(x2 + 1, n):
                a3.append(E.b(x2, y2) if B[x2, y2] else -E.b(x2, y2))
                a3.append(E.d(x2, y2) if D2[x2, y2] else -E.d(x2, y2))
        r_p2 = S.solve(assumptions=a3)
        # free search: fix only D, let the solver find some B
        aD = [l for l in assum if abs(l) in {E.d(x2, y2) for x2 in range(n) for y2 in range(x2 + 1, n)}]
        r_free = S.solve(assumptions=aD)
    print(f"planted seed {seed}: vars={E.pool.top} clauses={len(E.clauses)}  planted SAT={r_true}  "
          f"+edge UNSAT={not r_p1}  rewired-D UNSAT={not r_p2}  D-only SAT={r_free}  t={time.time()-t0:.1f}s")

E = U.build_real()
print(f"real encoding: vars={E.pool.top} clauses={len(E.clauses)} build t={time.time()-t0:.1f}s")
ci = {c: i for i, c in enumerate(U.CELLS)}
Y_all = set(range(21))
U5 = [0, 1, 2, 3, 4]
Y_ext = {ci[c] for c in itertools.combinations(U5, 2)} | {ci[(5, 6)]}
with Cadical153(bootstrap_with=E.clauses) as S:
    for name, Y in [("all cells type 2 (R4)", Y_all), ("extremal class K(U)+V (Lemma J)", Y_ext)]:
        t1 = time.time()
        r = S.solve(assumptions=U.class_assumptions(E, Y))
        print(f"  {name}: {'SAT' if r else 'UNSAT'}  ({time.time()-t1:.1f}s)")
        if r:
            B, D = U.decode(E, S.get_model()); print("   verify:", U.verify_unsigned(B, D))
print(f"total {time.time()-t0:.1f}s")
