r"""c08: arithmetic check of the defect computations in ONE_CANDIDATE_T1.md (Theorem A).

Bounds: one process, < 1 s, < 50 MB. No search: every configuration below is written out explicitly.

For an induced subgraph H of an srg(99,14,1,2) the Wilbrink-Brouwer defect is
    D(H) = (n-N) - (kN-2M) + lam*M + mu*(C(N,2)-M) - sum_h C(deg_H h, 2) = sum_j C(j-1,2) x_j >= 0,
and for p outside H with d = |N(p) cap H| (Lemma X):
    sum_{q in N(p)\H} |N(q) cap H| = d*lam + (N-d)*mu - sum_{h in N(p) cap H} deg_H(h),
so at least  (k-d) - that  neighbours of p have no neighbour in H.
Only adjacencies FORCED by the model are used: v0 ~ inner; i+ ~ i-; exterior r ~ inner i^s iff r_i = s;
all four lifts of a pi-pair pairwise adjacent; plus the adjacencies of p stated in each case.
"""
from itertools import combinations
from math import comb

n, k, lam, mu = 99, 14, 1, 2


def build(square, extra):
    """square: (xplus, yplus) as dicts coord->sign; extra: list of (name, root dict, list of names adjacent)."""
    V = ['v0']
    inner = set()
    for r in square:
        inner |= set(r)
    for i in sorted(inner):
        V += [f'{i}+', f'{i}-']
    x, y = square
    lifts = {'x+': x, 'x-': {i: -s for i, s in x.items()}, 'y+': y, 'y-': {i: -s for i, s in y.items()}}
    V += list(lifts)
    E = set()
    for i in inner:
        E.add(frozenset(('v0', f'{i}+'))); E.add(frozenset(('v0', f'{i}-'))); E.add(frozenset((f'{i}+', f'{i}-')))
    for name, r in lifts.items():
        for i, s in r.items():
            E.add(frozenset((name, f'{i}{"+" if s > 0 else "-"}')))
    for a in ('x+', 'x-'):
        for b in ('y+', 'y-'):
            E.add(frozenset((a, b)))
    roots = dict(lifts)
    for name, r, adj in extra:
        V.append(name)
        roots[name] = r
        for i, s in r.items():
            v = f'{i}{"+" if s > 0 else "-"}'
            if v in V:
                E.add(frozenset((name, v)))
        for a in adj:
            E.add(frozenset((name, a)))
    return V, E


def defect(V, E):
    N, M = len(V), len(E)
    deg = {v: sum(1 for e in E if v in e) for v in V}
    return (n - N) - (k * N - 2 * M) + lam * M + mu * (comb(N, 2) - M) - sum(comb(d, 2) for d in deg.values()), deg


def lemma_x(V, E, p_adj):
    """p outside H adjacent to p_adj (subset of V). Returns (d, sum_q j_q, #outside nbrs, forced zeros)."""
    _, deg = defect(V, E)
    d = len(p_adj)
    s = d * lam + (len(V) - d) * mu - sum(deg[h] for h in p_adj)
    return d, s, k - d, (k - d) - s


def report(title, square, extra_H, p_name, p_root, p_adj):
    V, E = build(square, extra_H)
    D, _ = defect(V, E)
    # adjacency of p to inner vertices of H is forced by its coordinates
    adj = list(p_adj) + [f'{i}{"+" if s > 0 else "-"}' for i, s in p_root.items() if f'{i}+' in V]
    d, s, out, zeros = lemma_x(V, E, adj)
    V2, E2 = build(square, extra_H + [(p_name, p_root, p_adj)])
    D2, _ = defect(V2, E2)
    print(f'{title}: D(H)={D}  p={p_name} d={d} sum_j={s} outside_nbrs={out} forced_zero_nbrs>={zeros}  D(H+p)={D2}')
    return D, zeros, D2


X1 = {1: 1, 3: 1}      # type 1: a=1, c=3 (common), b=2; W = {4,5,6,7}
Y1 = {2: 1, 3: 1}
print('--- type-1 square, H_S = {v0, 1+-, 2+-, 3+-, x+-, y+-}')
report('state (b)  apex zeta=-e1+e4 on line (x+, y-)', (X1, Y1), [], 'zeta', {1: -1, 4: 1}, ['x+', 'y-'])
report('state (b\') apex zeta=+e2+e4 on line (x+, y-)', (X1, Y1), [], 'zeta', {2: 1, 4: 1}, ['x+', 'y-'])
for al in (1, -1):
    for be in (1, -1):
        report(f'state (a1) nu={al:+d}e1{be:+d}e2 adjacent to x+', (X1, Y1), [], 'nu', {1: al, 2: be}, ['x+'])
report('state (a*) apex zeta=e4+e5 on line (x+, y-)', (X1, Y1), [], 'zeta', {4: 1, 5: 1}, ['x+', 'y-'])
report('state (a0) hole omega=e6+e7', (X1, Y1), [], 'omega', {6: 1, 7: 1}, [])

X0 = {1: 1, 2: 1}      # type 0: x = {1,2}, y = {3,4}, W = {5,6,7}
Y0 = {3: 1, 4: 1}
print('--- type-0 square, H_S = {v0, 1..4 +-, x+-, y+-}')
report('cross apex zeta1=-e1-e3 on line (x+, y+)', (X0, Y0), [], 'zeta1', {1: -1, 3: -1}, ['x+', 'y+'])
report('kw apex zeta1=-e1+e5 on line (x+, y+)', (X0, Y0), [], 'zeta1', {1: -1, 5: 1}, ['x+', 'y+'])
report('W apex zeta1=e5+e6 on line (x+, y+)', (X0, Y0), [], 'zeta1', {5: 1, 6: 1}, ['x+', 'y+'])

print('--- second order, state (a0): H_1 = H_S + {zeta, -zeta}, zeta = e4+e5 on lines (x+,y-), (x-,y+)')
V, E = build((X1, Y1), [('zeta', {4: 1, 5: 1}, ['x+', 'y-']), ('-zeta', {4: -1, 5: -1}, ['x-', 'y+'])])
D1, deg1 = defect(V, E)
print('D(H_1) =', D1, ' (N, M) =', (len(V), len(E)))
# Lemma X on H_1 for a lift psi of pi(z) (adjacent to both +-zeta) whose only H_S-neighbour is one vertex h
for h in ('1+', '3+', 'x+'):
    adj = ['zeta', '-zeta', h]
    d = len(adj)
    s = d * lam + (len(V) - d) * mu - sum(deg1[v] for v in adj)
    print(f'  psi ~ zeta,-zeta,{h}: forced zero nbrs >= {(k - d) - s}')

print('--- two-vertex additions: D of the induced graph H_S + p + (-p) (forced edges only); must be >= 0.')
print('    Agrees with D(H) - 2C(d-1,2) + 2E_p + |N(p) cap N(-p) minus H| (ONE_CANDIDATE_T1.md, Lemma X).')
def pair(r):
    return {i: -s for i, s in r.items()}
cases = [
    ('type1 apex zeta=e4+e5', (X1, Y1), ('zeta', {4: 1, 5: 1}, ['x+', 'y-']), ('-zeta', {4: -1, 5: -1}, ['x-', 'y+'])),
    ('type1 hole omega=e6+e7', (X1, Y1), ('om', {6: 1, 7: 1}, []), ('-om', {6: -1, 7: -1}, [])),
    ('type1 {a,b}-orbit nu=e1+e2', (X1, Y1), ('nu', {1: 1, 2: 1}, []), ('-nu', {1: -1, 2: -1}, [])),
    ('type1 sibling of x: e1-e3', (X1, Y1), ('k', {1: 1, 3: -1}, []), ('-k', {1: -1, 3: 1}, [])),
    ('type1 C_a-star nbr of x: e1+e4', (X1, Y1), ('s', {1: 1, 4: 1}, ['x+']), ('-s', {1: -1, 4: -1}, ['x-'])),
    ('type0 cross apex -e1-e3', (X0, Y0), ('z1', {1: -1, 3: -1}, ['x+', 'y+']), ('-z1', {1: 1, 3: 1}, ['x-', 'y-'])),
    ('type0 kw apex -e1+e5', (X0, Y0), ('z1', {1: -1, 5: 1}, ['x+', 'y+']), ('-z1', {1: 1, 5: -1}, ['x-', 'y-'])),
    ('type0 W apex e5+e6', (X0, Y0), ('z1', {5: 1, 6: 1}, ['x+', 'y+']), ('-z1', {5: -1, 6: -1}, ['x-', 'y-'])),
]
for title, sq, p, mp in cases:
    V, E = build(sq, [p, mp])
    D, _ = defect(V, E)
    print(f'  {title}: D(H_S + p + (-p)) = {D}')
