r"""c09: checker for the apex/hole system Sigma_AH of ONE_CANDIDATE_T1S.md.  NOT a search.

It takes explicit, hand-written configurations (pi z, pi o and the signed rows of x, y, z, o) and reports
every violated equation of (R), (I), (Bd), (A0).  Bounds: one process, < 1 s, < 50 MB.

Orbit (i, j, s), i < j, positive root r = e_i + s e_j.  Row of u: dict orbit -> N_uw in {+1, -1}.
"""
import sys
from itertools import combinations

ORB = [(i, j, s) for i in range(1, 8) for j in range(i + 1, 8) for s in (1, -1)]


def r(o):
    v = [0] * 8
    v[o[0]] = 1
    v[o[1]] = o[2]
    return v


def supp(o):
    return {o[0], o[1]}


def parse(tok):
    i, j, s = tok.strip('[]').split(',')
    return (int(i), int(j), 1 if s == '+' else -1)


def gd(u, v):
    ru, rv = r(u), r(v)
    g = sum(1 for k in range(1, 8) if ru[k] and rv[k] and ru[k] == rv[k])
    d = sum(1 for k in range(1, 8) if ru[k] and rv[k] and ru[k] != rv[k])
    return g, d


def check(name, rows, pi, verbose=True):
    """rows: dict u -> {w: N}; pi: dict u -> partner for u in X."""
    X = list(rows)
    x, y, z, o = X
    viol = []
    # (R)
    for u in X:
        row = rows[u]
        if u in row:
            viol.append(f'(R) {u}: N_uu != 0')
        if len(row) != 10:
            viol.append(f'(R) deg {u} = {len(row)}')
        if pi[u] in row:
            viol.append(f'(R) {u} adjacent to its partner')
        for k in range(1, 8):
            f = sum(1 for w in row if k in supp(w))
            want = 4 - 2 * (k in supp(u)) - 2 * (k in supp(pi[u]))
            if f != want:
                viol.append(f'(R) profile {u} at {k}: {f} != {want}')
        s = [0] * 8
        for w, n in row.items():
            rw = r(w)
            for k in range(1, 8):
                s[k] += n * rw[k]
        if any(s[1:]):
            viol.append(f'(R) NR row {u}: {s[1:]}')
    for u, v in combinations(X, 2):
        if rows[u].get(v, 0) != rows[v].get(u, 0):
            viol.append(f'(R) asymmetric N on ({u},{v})')

    def B(u, w):
        if u in rows:
            return 1 if w in rows[u] else 0
        if w in rows:
            return 1 if u in rows[w] else 0
        return None
    # (I)
    for u, v in combinations(X, 2):
        Y = sum(1 for w in rows[u] if w in rows[v] and rows[u][w] * rows[v][w] == 1)
        Z = sum(1 for w in rows[u] if w in rows[v] and rows[u][w] * rows[v][w] == -1)
        n = rows[u].get(v, 0)
        P, Pp = int(n == 1), int(n == -1)
        g, d = gd(u, v)
        beta = B(u, pi[v]) + B(pi[u], v)
        D = int(v == pi[u])
        if Y + Pp + g + beta + D != 2:
            viol.append(f'(I) E+ ({u},{v}): {Y}+{Pp}+{g}+{beta}+{D}')
        if Z + P + d + beta + D != 2:
            viol.append(f'(I) E- ({u},{v}): {Z}+{P}+{d}+{beta}+{D}')
    # (Bd)
    partner_of = {pi[t]: t for t in X}      # orbits w with pi w known: w = pi t  =>  pi w = t
    for u in X:
        for w in ORB:
            if w in X:
                continue
            n = rows[u].get(w, 0)
            P, Pp = int(n == 1), int(n == -1)
            g, d = gd(u, w)
            D = int(w == pi[u])
            bk = 0
            if pi[u] in rows:
                bk += 1 if w in rows[pi[u]] else 0
            if w in partner_of and partner_of[w] in X:     # pi w = partner_of[w]
                bk += 1 if partner_of[w] in rows[u] else 0
            conc = sum(1 for t in X if t != u and t in rows[u] and w in rows[t] and rows[u][t] * rows[t][w] == 1)
            disc = sum(1 for t in X if t != u and t in rows[u] and w in rows[t] and rows[u][t] * rows[t][w] == -1)
            if Pp + g + D + bk + conc > 2:
                viol.append(f'(Bd) E+ ({u},{w}): {Pp}+{g}+{D}+{bk}+{conc} > 2')
            if P + d + D + bk + disc > 2:
                viol.append(f'(Bd) E- ({u},{w}): {P}+{d}+{D}+{bk}+{disc} > 2')
    # (A0)
    W = {4, 5, 6, 7}
    for u in (x, y):
        for w in rows[u]:
            if 3 in supp(w) or supp(w) == {1, 2}:
                viol.append(f'(A0) {u} has neighbour {w}')
        if sum(1 for w in rows[u] if supp(w) <= W) != 6:
            viol.append(f'(A0) {u} does not have 6 W-cell neighbours')
    if set(rows[x]) & set(rows[y]) != {z}:
        viol.append(f'(A0) B(x) cap B(y) = {set(rows[x]) & set(rows[y])}')
    if rows[x].get(z) != -1 or rows[y].get(z) != 1:
        viol.append('(A0) N_xz, N_yz not normalized')
    Wo = [w for w in ORB if supp(w) <= W]
    for w in Wo:
        m = (w in rows[x]) + (w in rows[y])
        want = 2 if w == z else (0 if w == o else 1)
        if m != want:
            viol.append(f'(A0) m({w}) = {m} != {want}')
    case = 'iii' if pi[z] == o else ('ii' if o in rows[z] else 'i')
    if verbose:
        print(f'== {name}: case ({case}); {len(viol)} violations')
        for s in viol:
            print('   ', s)
    return viol




if __name__ == '__main__':
    x, y, z = (1, 3, 1), (2, 3, 1), (4, 5, 1)
    P = parse
    # ---- R0 (selection note): bare row solution, case (iii)
    o = (6, 7, 1)
    rows = {
        x: {P('[1,4,-]'): -1, P('[1,5,+]'): 1, P('[2,6,+]'): -1, P('[2,7,+]'): 1, z: -1,
            P('[6,7,-]'): -1, P('[4,6,+]'): 1, P('[4,7,+]'): -1, P('[5,6,+]'): 1, P('[5,7,+]'): -1},
        y: {P('[2,6,-]'): -1, P('[2,7,-]'): 1, P('[1,6,+]'): -1, P('[1,7,-]'): 1, z: 1,
            P('[4,5,-]'): 1, P('[4,6,-]'): -1, P('[4,7,-]'): -1, P('[5,6,-]'): 1, P('[5,7,-]'): -1},
        z: {x: -1, y: 1, P('[1,5,+]'): -1, P('[2,6,-]'): -1, P('[1,4,+]'): 1, P('[1,7,+]'): 1,
            P('[2,4,-]'): 1, P('[2,5,-]'): -1, P('[3,6,-]'): 1, P('[3,7,+]'): -1},
        o: {P('[1,3,-]'): -1, P('[2,3,-]'): 1, P('[1,5,+]'): 1, P('[2,7,+]'): -1, P('[2,6,-]'): -1,
            P('[1,7,-]'): -1, P('[1,6,-]'): 1, P('[2,4,+]'): 1, P('[3,4,-]'): 1, P('[3,5,+]'): -1},
    }
    pi = {x: y, y: x, z: o, o: z}
    check('R0 (bare row solution from the selection note)', rows, pi)

    # ---- K1: hand-built attempt at the pre-registered level (case (iii)); signs solved by hand from the
    #      linear balance equations written in ONE_CANDIDATE_T1S.md, section "Attempt".
    rows = {
        x: {P('[1,4,-]'): -1, P('[1,5,+]'): 1, P('[2,6,+]'): 1, P('[2,7,+]'): -1, z: -1,
            P('[6,7,-]'): -1, P('[4,6,+]'): 1, P('[4,7,+]'): -1, P('[5,6,-]'): 1, P('[5,7,-]'): -1},
        y: {P('[2,6,-]'): -1, P('[2,7,-]'): 1, P('[1,7,+]'): 1, P('[1,6,-]'): -1, z: 1,
            P('[4,5,-]'): -1, P('[4,6,-]'): 1, P('[4,7,-]'): -1, P('[5,6,+]'): -1, P('[5,7,+]'): -1},
        z: {x: -1, y: 1, P('[2,6,+]'): -1, P('[1,7,+]'): 1, P('[1,4,+]'): 1, P('[1,5,-]'): -1,
            P('[2,4,-]'): 1, P('[2,5,+]'): -1, P('[3,6,-]'): -1, P('[3,7,-]'): 1},
        o: {P('[2,6,+]'): 1, P('[1,7,+]'): 1, P('[3,6,+]'): -1, P('[3,7,+]'): -1, P('[4,5,-]'): 1,
            P('[1,4,-]'): 1, P('[1,2,-]'): -1, P('[1,3,-]'): -1, P('[2,3,-]'): -1, P('[2,5,-]'): -1},
    }
    check('K1 (attempt, case (iii))', rows, pi)

    # ---- K2: K1 with the hole's second y-common neighbour moved from kappa z to h' = [1,6,+]
    #      (K1 failed (E-) at the cell-mate pair (z, kappa z)); signs re-solved by hand.
    rows = {
        x: {P('[1,4,-]'): -1, P('[1,5,+]'): 1, P('[2,6,+]'): 1, P('[2,7,-]'): -1, z: -1,
            P('[6,7,-]'): 1, P('[4,6,-]'): 1, P('[4,7,-]'): -1, P('[5,6,+]'): -1, P('[5,7,-]'): 1},
        y: {P('[2,6,-]'): -1, P('[2,7,+]'): 1, P('[1,7,-]'): -1, P('[1,6,+]'): 1, z: 1,
            P('[4,5,-]'): 1, P('[4,6,+]'): -1, P('[4,7,+]'): -1, P('[5,6,-]'): 1, P('[5,7,+]'): -1},
        z: {x: -1, y: 1, P('[2,6,+]'): -1, P('[1,7,-]'): -1, P('[1,4,+]'): 1, P('[1,5,-]'): 1,
            P('[2,4,-]'): 1, P('[2,5,-]'): -1, P('[3,6,+]'): 1, P('[3,7,+]'): -1},
        o: {P('[2,6,+]'): 1, P('[1,7,-]'): -1, P('[1,6,+]'): -1, P('[3,7,-]'): 1, P('[1,4,-]'): 1,
            P('[2,3,-]'): -1, P('[1,3,-]'): 1, P('[2,4,+]'): 1, P('[2,5,+]'): -1, P('[3,5,-]'): -1},
    }
    check('K2 (attempt, case (iii))', rows, pi)

    # ---- K3: rebuilt respecting the relations forced by the K1/K2 failures:
    #      o not adjacent to kappa z; S_z-apexes u1 = x's antistar [1,6,+], u2 = y's antistar [2,7,+];
    #      p1 = [4,6,+] (x's W-neighbour, o's star at 6), p2 = [5,7,-] (y's, o's star at 7).
    rows = {
        x: {P('[1,6,+]'): 1, P('[1,4,-]'): -1, P('[2,5,+]'): 1, P('[2,7,-]'): -1, z: -1,
            P('[6,7,-]'): -1, P('[4,6,+]'): 1, P('[4,7,+]'): -1, P('[5,6,-]'): 1, P('[5,7,+]'): -1},
        y: {P('[2,7,+]'): 1, P('[2,6,-]'): -1, P('[1,6,-]'): 1, P('[1,7,+]'): -1, z: 1,
            P('[4,5,-]'): -1, P('[4,6,-]'): -1, P('[4,7,-]'): 1, P('[5,6,+]'): -1, P('[5,7,-]'): -1},
        z: {x: -1, y: 1, P('[1,6,+]'): -1, P('[2,7,+]'): 1, P('[1,4,+]'): 1, P('[1,5,-]'): 1,
            P('[2,4,+]'): -1, P('[2,5,-]'): -1, P('[3,6,+]'): 1, P('[3,7,+]'): -1},
        o: {P('[1,6,+]'): 1, P('[2,7,+]'): 1, P('[4,6,+]'): -1, P('[5,7,-]'): 1, P('[1,2,+]'): -1,
            P('[1,2,-]'): 1, P('[1,3,-]'): -1, P('[2,3,-]'): 1, P('[3,4,+]'): 1, P('[3,5,+]'): -1},
    }
    check('K3 (attempt, case (iii))', rows, pi)
