r"""c14: independent verification of the c13 configuration (reads data/c13_config_alpha_alpha.json).
Written separately from c13; re-derives every condition from the definitions:
 rows: 10 distinct orbits, no self, no partner; partners: x <-> pi x mutual, pi w1, pi w2 outside the centres;
 symmetry of B between centres; (P) for every centre; (Q) exactly for every pair of centres;
 local consistency for every (centre, other orbit) pair; (P)/degree bounds for other orbits;
 the Om1 violation: the two orbits of row x containing coordinate 1 are w1, w2, and beta(x, w_i) = 1.
One process, < 1 s, < 50 MB.
"""
import json, itertools

cfg = json.load(open('data/c13_config_alpha_alpha.json'))


def parse(nm):              # '(15,+)' -> (frozenset({1,5}), '+')
    return (frozenset((int(nm[1]), int(nm[2]))), nm[4])


ORBS = [(frozenset(c), sg) for c in itertools.combinations(range(1, 8), 2) for sg in '+-']
assert len(ORBS) == 42
C = {parse(k): {'p': parse(v['partner']), 'row': {parse(o) for o in v['row']}} for k, v in cfg.items()}
cent = set(C)
x, px, w1, w2 = parse('(12,+)'), parse('(34,+)'), parse('(15,+)'), parse('(16,+)')
err = []


def s(a, b):
    return len(a[0] & b[0])


def B(a, b):              # adjacency, known if a or b is a centre
    if a in cent:
        return int(b in C[a]['row'])
    if b in cent:
        return int(a in C[b]['row'])
    return None


for u in cent:
    r = C[u]['row']
    if len(r) != 10 or u in r or C[u]['p'] in r:
        err.append(f'row {u}')
    for k in range(1, 8):
        f = sum(1 for o in r if k in o[0])
        want = 4 - 2 * (k in u[0]) - 2 * (k in C[u]['p'][0])
        if f != want:
            err.append(f'(P) {u} k={k}: {f} != {want}')
if C[x]['p'] != px or C[px]['p'] != x:
    err.append('partners x, pi x')
for w in (w1, w2):
    if C[w]['p'] in cent:
        err.append('partner of w in centres')
if C[w1]['p'] == C[w2]['p']:
    err.append('pi w1 = pi w2')
partner = {u: C[u]['p'] for u in cent}
for u in cent:
    partner[C[u]['p']] = u
for u, v in itertools.permutations(cent, 2):
    if (v in C[u]['row']) != (u in C[v]['row']):
        err.append(f'asymmetric {u},{v}')
for u, v in itertools.combinations(cent, 2):
    B2 = len(C[u]['row'] & C[v]['row'])
    beta = B(partner[u], v) + B(u, partner[v])
    D = int(partner[u] == v)
    lhs = B2 + B(u, v) + s(u, v) + 2 * beta + 2 * D
    if lhs != 4:
        err.append(f'(Q) {u},{v}: {lhs}')
# local consistency for (centre, other)
for u in cent:
    for v in ORBS:
        if v in cent or v == u:
            continue
        Buv, Duv = B(u, v), int(partner[u] == v)
        a = B(partner[u], v) if partner[u] in cent else None
        a_opts = [a] if a is not None else ([0] if partner[u] == v else [0, 1])
        if v in partner:
            b_opts = [int(partner[v] in C[u]['row'])]
        else:
            b_opts = [0, 1] if any(z not in partner and z != v for z in C[u]['row']) else [0]
        lb = sum(1 for c in cent if c in C[u]['row'] and v in C[c]['row'])
        ub = 10 - sum(1 for c in cent if c in C[u]['row'] and v not in C[c]['row'])
        good = any(lb <= 4 - Buv - s(u, v) - 2 * Duv - 2 * (aa + bb) <= ub
                   and 4 - Buv - s(u, v) - 2 * Duv - 2 * (aa + bb) >= 0
                   and not (Buv and aa + bb > 1) for aa in a_opts for bb in b_opts)
        if not good:
            err.append(f'local {u},{v}')
for v in ORBS:
    if v in cent:
        continue
    nb = [c for c in cent if v in C[c]['row']]
    pv = partner.get(v)
    for k in range(1, 8):
        mx = 4 - 2 * (k in v[0]) - (2 * (k in pv[0]) if pv else 0)
        if sum(1 for c in nb if k in c[0]) > mx:
            err.append(f'bound {v} k={k}')
ones = sorted([o for o in C[x]['row'] if 1 in o[0]], key=str)
viol = set(ones) == {w1, w2} and all(B(px, w) + B(x, partner[w]) == 1 for w in (w1, w2))
print('errors:', len(err))
for e in err[:20]:
    print('  ', e)
print('coordinate-1 neighbours of x:', ones)
print('beta(x,w1), beta(x,w2):', [B(px, w) + B(x, partner[w]) for w in (w1, w2)])
print('Om1 violated at x (both C_1^B edges at x are apex edges):', viol)
