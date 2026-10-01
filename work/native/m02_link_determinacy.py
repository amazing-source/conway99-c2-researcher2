r"""m02 microscope (one process, < 2 min, < 300 MB). Exact question: at the scale of ONE twisted link pair
(y, w) at coordinate 1 with complete rows and FIXED R0 data (D-partners, link/anti partners at all four ports of y
and w), are the disjoint-cell partners of y and w determined by the visible exact equations?
Visible equations: row and port rules of y and w (exact); the pair rule (y, w) (exact: both rows complete);
for every other label u the terms of pairs (y,u) and (w,u) that are already known (via z = w resp. z = y) must not
exceed the weight target and must leave the sign target reachable.
Labels: ((i,j), s) with root e_i + s e_j (0-indexed coordinates)."""
import itertools, collections, json
L = [((i, j), s) for (i, j) in itertools.combinations(range(7), 2) for s in (1, -1)]
def root(l):
    (i, j), s = l; r = [0] * 7; r[i] = 1; r[j] = s; return r
def supp(l): return set(l[0])
q = {'n': 0, 'd': 2, 'm': 1, 'p': 1}; sv = {'n': 0, 'd': 0, 'm': -1, 'p': 1}
y, w = ((0, 1), 1), ((0, 2), 1)
pi = {y: ((3, 4), 1), w: ((3, 5), 1)}
R0 = {y: {w: 'm', ((0, 3), 1): 'p', ((1, 4), -1): 'm', ((1, 5), 1): 'p'},       # link_0, anti_0, link_1, anti_1
      w: {y: 'm', ((0, 4), 1): 'p', ((2, 6), 1): 'm', ((1, 2), -1): 'm'}}       # link_0, anti_0, link_2, anti_2
# sanity: link/anti charges
for x in (y, w):
    for i in supp(x):
        ch = sorted(sv[R0[x][z]] * root(z)[i] for z in R0[x] if i in supp(z))
        assert ch == [-1, 1], (x, i, ch)
        assert any(sv[R0[x][z]] * root(z)[i] == -root(x)[i] for z in R0[x] if i in supp(z))
def disjoint_rows(x):
    tgt = [4 - 2 * (a in supp(x)) - 2 * (a in supp(pi[x])) for a in range(7)]
    deg = [0] * 7; ch = [0] * 7
    for z, st in R0[x].items():
        for a in supp(z):
            deg[a] += 1; ch[a] += sv[st] * root(z)[a]
    res_d = [tgt[a] - deg[a] for a in range(7)]; res_c = [-ch[a] for a in range(7)]
    cand = [z for z in L if not (supp(z) & supp(x)) and z != pi[x]]
    out = []
    def rec(k, d, c, chosen):
        if k == len(cand):
            if all(v == 0 for v in d) and all(v == 0 for v in c): out.append(dict(chosen))
            return
        z = cand[k]; a, b = z[0]
        rest = cand[k + 1:]
        rec(k + 1, d, c, chosen)
        if d[a] >= 1 and d[b] >= 1:
            for st in ('p', 'm'):
                d2 = d[:]; c2 = c[:]
                d2[a] -= 1; d2[b] -= 1; c2[a] -= sv[st] * root(z)[a]; c2[b] -= sv[st] * root(z)[b]
                chosen[z] = st; rec(k + 1, d2, c2, chosen); del chosen[z]
    rec(0, res_d, res_c, {})
    return out, res_d, res_c
Ry, rdy, rcy = disjoint_rows(y); Rw, rdw, rcw = disjoint_rows(w)
print('residual ports y: deg', rdy, 'charge', rcy, '| admissible disjoint rows of y:', len(Ry))
print('residual ports w: deg', rdw, 'charge', rcw, '| admissible disjoint rows of w:', len(Rw))
def full(x, dis):
    row = dict(R0[x]); row.update(dis); row[pi[x]] = 'd'; return row
def k_(a, b): return len(supp(a) & supp(b))
def h_(a, b): return sum(p * r for p, r in zip(root(a), root(b)))
def visible_ok(rowy, roww):
    # exact pair rule (y,w)
    Wq = Ws = 0
    for z in L:
        if z in (y, w): continue
        cy, cw = rowy.get(z, 'n'), roww.get(z, 'n')
        Wq += q[cy] * q[cw]; Ws += sv[cy] * sv[cw]
    if (Wq, Ws) != (4 - k_(y, w) - q['m'], sv['m'] - h_(y, w)): return False
    # partial pair rules (x,u) with the single known intermediate (the other centre)
    for x, o, rowx, rowo in ((y, w, rowy, roww), (w, y, roww, rowy)):
        for u in L:
            if u in (y, w): continue
            cxu = rowx.get(u, 'n'); T = 4 - k_(x, u) - q[cxu]; S = sv[cxu] - h_(x, u)
            kq = q[rowx[o]] * q[rowo.get(u, 'n')]; ks = sv[rowx[o]] * sv[rowo.get(u, 'n')]
            if kq > T or abs(S - ks) > T - kq or (S - ks - (T - kq)) % 2: return False
    return True
sols = []
for dy in Ry:
    for dw in Rw:
        ry_, rw_ = full(y, dy), full(w, dw)
        if visible_ok(ry_, rw_): sols.append((dy, dw))
by_wit = collections.defaultdict(list)
for dy, dw in sols:
    ry_, rw_ = full(y, dy), full(w, dw)
    wit = tuple(sorted((z for z in L if z not in (y, w) and ry_.get(z, 'n') != 'n' and rw_.get(z, 'n') != 'n'), key=str))
    by_wit[wit].append((dy, dw))
print('joint realizations (y,w) satisfying every visible equation:', len(sols))
print('distinct witness pairs of the link:', len(by_wit))
for wit, lst in sorted(by_wit.items(), key=lambda t: -len(t[1]))[:6]:
    print('  witnesses', wit, '-> realizations', len(lst))
json.dump({'n_sols': len(sols), 'witness_classes': {str(k): len(v) for k, v in by_wit.items()},
           'example_two_witness_pairs': [[{str(k): v for k, v in s[0].items()}, {str(k): v for k, v in s[1].items()}]
                                         for s in [list(by_wit.values())[0][0], list(by_wit.values())[1][0]]] if len(by_wit) > 1 else []},
          open('native/m02_result.json', 'w'), indent=1)
