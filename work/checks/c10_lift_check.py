r"""c10: independent lift-level verification of the configurations in c09 (NOT a search).

Builds the partial 99-vertex graph that the rows of x, y, z, o determine:
  v0 ~ all inner vertices; k+ ~ k-; an exterior lift r ~ inner k^s iff r_k = s;
  for u in X: u+ = r_u is adjacent to -N_uw r_w (w in row u), u- to +N_uw r_w, and u+- to both lifts of pi u.
Then for every centre lift c (the 8 lifts of x, y, z, o) and every other vertex p it counts the common
neighbours of c and p that are certainly present (all of N(c) is known; adjacency of p to a member q of
N(c) is known when p or q is a centre lift, an inner vertex or v0). It requires
  count = 1 (c ~ p) or 2 (c !~ p) when the neighbourhood of p is fully known (p centre, inner, v0),
  count <= 1 resp. <= 2 otherwise,
plus degree 14 for every centre lift. This is lambda = 1, mu = 2 restricted to what the four rows know,
written independently of the (E+-) bookkeeping of c09. Bounds: one process, < 5 s, < 100 MB.
"""
import importlib.util, sys, os

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('c09', os.path.join(here, 'c09_apex_hole_system.py'))
c09 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c09)
ORB, r, P = c09.ORB, c09.r, c09.parse


def lift_check(name, rows, pi):
    X = list(rows)
    V = ['v0'] + [('I', k, s) for k in range(1, 8) for s in (1, -1)]
    V += [('E', o, e) for o in ORB for e in (1, -1)]           # lift e*r_o

    def vec(v):
        o, e = v[1], v[2]
        return [e * t for t in r(o)]
    known = {}                                                # adjacency known to exist / not exist

    def setadj(a, b, val):
        known[(a, b)] = val
        known[(b, a)] = val
    inner = [v for v in V if v != 'v0' and v[0] == 'I']
    ext = [v for v in V if v != 'v0' and v[0] == 'E']
    for a in inner:
        setadj('v0', a, True)
        for b in inner:
            if a != b:
                setadj(a, b, a[1] == b[1])
    for a in ext:
        setadj('v0', a, False)
        va = vec(a)
        for b in inner:
            setadj(a, b, va[b[1]] == b[2])
    centre = [('E', u, 1) for u in X] + [('E', u, -1) for u in X]
    for u in X:
        nb = set()
        for w, n in rows[u].items():
            nb.add(('E', w, -n))
        nb.add(('E', pi[u], 1)); nb.add(('E', pi[u], -1))
        for e in (1, -1):
            c = ('E', u, e)
            cn = {('E', q[1], q[2] * e) for q in nb}
            for q in ext:
                if q != c:
                    setadj(c, q, q in cn)
    viol = []
    for c in centre:
        N_c = [v for v in V if v != c and known.get((c, v)) is True]
        if len(N_c) != 14:
            viol.append(f'deg {c} = {len(N_c)}')
        for p in V:
            if p == c:
                p_known = False
                continue
            p_full = p == 'v0' or p[0] == 'I' or p in centre
            cnt = 0
            for q in N_c:
                if q == p:
                    continue
                if known.get((p, q)) is True:
                    cnt += 1
            adj = known.get((c, p)) is True
            want = 1 if adj else 2
            if p_full and cnt != want:
                viol.append(f'{c} vs {p}: {cnt} common, want {want}')
            if not p_full and cnt > want:
                viol.append(f'{c} vs {p}: {cnt} common > {want}')
    print(f'== {name}: {len(viol)} lift-level violations')
    for s in viol[:12]:
        print('   ', s)
    return viol


if __name__ == '__main__':
    import io, contextlib
    x, y, z, o = (1, 3, 1), (2, 3, 1), (4, 5, 1), (6, 7, 1)
    pi = {x: y, y: x, z: o, o: z}
    # re-read the configurations from c09 by executing its main block with a capturing check()
    configs = []
    orig = c09.check
    c09.check = lambda name, rows, pi_: configs.append((name, rows, pi_)) or []
    src = open(os.path.join(here, 'c09_apex_hole_system.py'), encoding='utf-8').read()
    main = src.split("if __name__ == '__main__':", 1)[1]
    ns = dict(vars(c09)); ns['check'] = c09.check
    exec('if True:' + main, ns)
    c09.check = orig
    for name, rows, pi_ in configs:
        lift_check(name, rows, pi_)
