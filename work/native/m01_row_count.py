r"""Microscope m01 (one process, < 3 min, < 500 MB). Exact question: for the label x = (12,+) and a double partner
pi x of each type, how many state assignments to the other 40 labels satisfy the row rules and all port rules
(A1 degree profile + A2 charge balance)? (Ten signed partners follow from A1.)"""
import itertools, collections, time
cells = list(itertools.combinations(range(7), 2))
labels = [(c, s) for c in cells for s in (1, -1)]          # root r = e_i + s e_j
def root(l):
    (i, j), s = l; r = [0] * 7; r[i] = 1; r[j] = s; return r
X = ((0, 1), 1)
def count(pix):
    supp = lambda l: set(l[0])
    tgt = [4 - 2 * (a in supp(X)) - 2 * (a in supp(pix)) for a in range(7)]
    cand = [l for l in labels if l not in (X, pix)]
    states = {(tuple([0] * 7), tuple([0] * 7)): 1}
    for idx, y in enumerate(cand):
        ry = root(y); new = collections.defaultdict(int)
        for (dg, ch), cnt in states.items():
            new[(dg, ch)] += cnt                               # state n
            i, j = y[0]
            if dg[i] + 1 > tgt[i] or dg[j] + 1 > tgt[j]: continue
            for sgn in (1, -1):                                # states p, m
                d2 = list(dg); c2 = list(ch)
                d2[i] += 1; d2[j] += 1; c2[i] += sgn * ry[i]; c2[j] += sgn * ry[j]
                new[(tuple(d2), tuple(c2))] += cnt
        # prune: charge must be completable: |charge| <= remaining degree
        rem_cells = cand[idx + 1:]
        cap = [0] * 7
        for l in rem_cells:
            for a in l[0]: cap[a] += 1
        states = {k: v for k, v in new.items()
                  if all(abs(k[1][a]) <= min(cap[a], tgt[a] - k[0][a]) for a in range(7))
                  and all(tgt[a] - k[0][a] <= cap[a] for a in range(7))}
    return states.get((tuple(tgt), tuple([0] * 7)), 0)
t0 = time.time()
for name, pix in [('type 0 (pi x = (34,+))', ((2, 3), 1)), ('type 1 (pi x = (13,+))', ((0, 2), 1)),
                  ('type 1 (pi x = (13,-))', ((0, 2), -1)), ('type 2 (pi x = (12,-))', ((0, 1), -1))]:
    print(f'{name}: admissible rows = {count(pix)}   ({time.time()-t0:.1f}s)')
