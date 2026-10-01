r"""m04 (one process, < 1 min). Saves the minimal pair found by m03 and verifies it FROM SCRATCH with code written
independently of m02/m03: for both realizations, rebuild the complete rows of y = (01,+) and w = (02,+) and check
(1) row counts, (2) all 14 port rules (degree quotas and charge balance), (3) the exact pair rule (y,w),
(4) every partially visible pair rule (y,u), (w,u), (5) identical R0 data (D, link/anti at all ports of y and w),
(6) the set of differing relations."""
import importlib.util, io, contextlib, itertools, json
spec = importlib.util.spec_from_file_location('m03', 'native/m03_minimal_pair.py'); m03 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m03)
m02 = m03.m02; a, b = m03.best[1]
P = [m03.sols[a], m03.sols[b]]
dump = [{'y_disjoint': {f'{z[0][0]+1}{z[0][1]+1}{"+" if z[1] > 0 else "-"}': st for z, st in dy.items()},
         'w_disjoint': {f'{z[0][0]+1}{z[0][1]+1}{"+" if z[1] > 0 else "-"}': st for z, st in dw.items()}} for dy, dw in P]
json.dump({'R0': {'y=(12,+) D': '(45,+)', 'w=(13,+) D': '(46,+)',
                  'y R0 partners': {'(13,+)': 'm link_1', '(14,+)': 'p anti_1', '(25,-)': 'm link_2', '(26,+)': 'p anti_2'},
                  'w R0 partners': {'(12,+)': 'm link_1', '(15,+)': 'p anti_1', '(37,+)': 'm link_3', '(23,-)': 'm anti_3'}},
           'realizations': dump}, open('native/m04_minimal_pair.json', 'w'), indent=1)
# ---------------- independent verification (1-indexed, own helpers) ----------------
def rt(lab):  # lab = 'ij+' -> root vector
    i, j, s = int(lab[0]) - 1, int(lab[1]) - 1, (1 if lab[2] == '+' else -1); v = [0] * 7; v[i] = 1; v[j] = s; return v
ALL = [f'{i}{j}{s}' for i in range(1, 8) for j in range(i + 1, 8) for s in '+-']
Qv = {'n': 0, 'd': 2, 'm': 1, 'p': 1}; Sv = {'n': 0, 'd': 0, 'm': -1, 'p': 1}
Y, Wl = '12+', '13+'
R0y = {'13+': 'm', '14+': 'p', '25-': 'm', '26+': 'p', '46+': 'n'}; R0w = {'12+': 'm', '15+': 'p', '37+': 'm', '23-': 'm'}
def build(center, dpart, r0, dis):
    row = {u: 'n' for u in ALL if u != center}
    for u, st in r0.items(): row[u] = st
    row[dpart] = 'd'
    for u, st in dis.items(): row[u] = st
    return row
errs = []
rows = []
for rz in dump:
    ry = build(Y, '45+', {k: v for k, v in R0y.items() if v != 'n'}, rz['y_disjoint'])
    rw = build(Wl, '46+', R0w, rz['w_disjoint'])
    rows.append((ry, rw))
    for c, row in ((Y, ry), (Wl, rw)):
        cnt = {st: sum(1 for v in row.values() if v == st) for st in 'ndmp'}
        if (cnt['d'], cnt['m'] + cnt['p'], cnt['n']) != (1, 10, 30): errs.append(f'counts {c} {cnt}')
        rc, mc = rt(c), [abs(t) for t in rt(c)]
        for a_ in range(7):
            quota = sum(Qv[st] * abs(rt(u)[a_]) for u, st in row.items())
            bal = sum(Sv[st] * rt(u)[a_] for u, st in row.items())
            if quota != (2 if mc[a_] else 4) or bal != 0: errs.append(f'port {c} coord {a_+1}: quota {quota} bal {bal}')
    if ry[Wl] != rw[Y]: errs.append('asymmetric y-w')
    sq = sum(Qv[ry[u]] * Qv[rw[u]] for u in ALL if u not in (Y, Wl))
    ss = sum(Sv[ry[u]] * Sv[rw[u]] for u in ALL if u not in (Y, Wl))
    k = sum(abs(p) * abs(q_) for p, q_ in zip(rt(Y), rt(Wl))); h = sum(p * q_ for p, q_ in zip(rt(Y), rt(Wl)))
    if (sq, ss) != (4 - k - Qv[ry[Wl]], Sv[ry[Wl]] - h): errs.append(f'pair rule (y,w): {(sq, ss)}')
    for c, o, rc_, ro in ((Y, Wl, ry, rw), (Wl, Y, rw, ry)):
        for u in ALL:
            if u in (Y, Wl): continue
            k = sum(abs(p) * abs(q_) for p, q_ in zip(rt(c), rt(u))); h = sum(p * q_ for p, q_ in zip(rt(c), rt(u)))
            T, S = 4 - k - Qv[rc_[u]], Sv[rc_[u]] - h
            kq, ks = Qv[rc_[o]] * Qv[ro[u]], Sv[rc_[o]] * Sv[ro[u]]
            if kq > T or abs(S - ks) > T - kq or (S - ks - (T - kq)) % 2: errs.append(f'partial ({c},{u})')
diff = [(c, u, rows[0][i][u], rows[1][i][u]) for i, c in enumerate((Y, Wl)) for u in ALL if u != c and rows[0][i][u] != rows[1][i][u]]
print('independent verification errors:', len(errs), errs[:5])
print('differing relations:', diff)
print('R0 parts identical:', all(rows[0][i][u] == rows[1][i][u] for i, (c, r0) in enumerate(((Y, R0y), (Wl, R0w))) for u in list(r0) + (['45+'] if c == Y else ['46+'])))
