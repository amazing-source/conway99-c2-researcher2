r"""c13 microscope (exact question in R2_OMEGA1_USEFULNESS.md, Stage B, case (alpha, alpha)).

Q layer only: rows are sets of B-neighbours plus a matching partner; the checks are (Deg), (P), (Q).
Centres x = (12,+), pi x = (34,+), w1 = (15,+), w2 = (16,+)  (1-indexed cells; 0-indexed below).
Wanted: complete rows for the four centres (partners pi w1, pi w2 chosen by the search) with (P) for every centre,
(Q) exact for every pair of centres, local consistency for every (centre, other orbit) pair, (P)/degree bounds for
every other orbit, and beta(x,w1) = beta(x,w2) = 1 (both C_1^B edges at x are apex edges).
Depth-first, stops at the first solution. Bounds: one process, time cap 240 s, < 200 MB.
"""
import itertools, time, sys, json

CELLS = list(itertools.combinations(range(7), 2))
NORB = 42
CID = {c: i for i, c in enumerate(CELLS)}


def cell(o):
    return CELLS[o // 2]


def orb(i, j, sg):
    return 2 * CID[(i, j)] + sg


def s_ov(a, b):
    return len(set(cell(a)) & set(cell(b)))


def name(o):
    i, j = cell(o)
    return f"({i+1}{j+1},{'+' if o % 2 == 0 else '-'})"


X, PX, W1, W2 = orb(0, 1, 0), orb(2, 3, 0), orb(0, 4, 0), orb(0, 5, 0)
T0 = time.time()
CAP = 240.0


def target(u, p):
    return [4 - 2 * (k in cell(u)) - 2 * (k in cell(p)) for k in range(7)]


def cover(rows):
    f = [0] * 7
    for o in rows:
        for k in cell(o):
            f[k] += 1
    return f


def rows_with(u, p, required, allowed, need, extra_ok=None, canon_cells=()):
    """All 10-sets R: required <= R, R - required <= allowed, coverage(R) = target(u,p).
    canon_cells: cells where, if exactly one orbit is used and both are allowed, use sign 0 (symmetry)."""
    allowed = set(allowed) - set(required)
    tgt = target(u, p)
    rem = tgt[:]
    for o in required:
        for k in cell(o):
            rem[k] -= 1
    if min(rem) < 0:
        return
    nfree = 10 - len(required)
    cand_cells = sorted({o // 2 for o in allowed})
    res = []

    def rec(ci, chosen, rem, left):
        if time.time() - T0 > CAP:
            raise TimeoutError
        if left == 0:
            if all(r == 0 for r in rem):
                R = set(required) | set(chosen)
                if extra_ok is None or extra_ok(R):
                    yield R
            return
        if ci == len(cand_cells):
            return
        if sum(rem) != 2 * left:
            return
        c = cand_cells[ci]
        i, j = CELLS[c]
        opts = [o for o in (2 * c, 2 * c + 1) if o in allowed]
        # choose 0, 1 or 2 orbits of this cell
        yield from rec(ci + 1, chosen, rem, left)
        if rem[i] >= 1 and rem[j] >= 1 and left >= 1:
            r2 = rem[:]
            r2[i] -= 1
            r2[j] -= 1
            singles = opts
            if c in canon_cells and len(opts) == 2:
                singles = [opts[0]]
            for o in singles:
                yield from rec(ci + 1, chosen + [o], r2, left - 1)
        if len(opts) == 2 and rem[i] >= 2 and rem[j] >= 2 and left >= 2:
            r2 = rem[:]
            r2[i] -= 2
            r2[j] -= 2
            yield from rec(ci + 1, chosen + opts, r2, left - 2)
    yield from rec(0, [], rem, nfree)


def local_ok(R, P):
    """Local consistency of every (centre, other orbit) pair and bounds for other orbits.
    R: dict centre -> row (set), P: dict centre -> partner. Partners of non-centres known only for pi w_i."""
    centres = set(R)
    known_partner = dict(P)
    for c, p in P.items():
        known_partner[p] = c
    for u in centres:
        for v in range(NORB):
            if v == u or v in centres:
                continue
            Buv = 1 if v in R[u] else 0
            Duv = 1 if P[u] == v else 0
            pu = P[u]
            # B(pi u, v)
            if pu in centres:
                a_opts = [1 if v in R[pu] else 0]
            else:
                a_opts = [0, 1] if v != pu else [0]
            # B(u, pi v)
            if v in known_partner:
                pv = known_partner[v]
                b_opts = [1 if pv in R[u] else 0]
            else:
                free = [z for z in R[u] if z not in known_partner and z != v]
                b_opts = [0, 1] if free else [0]
            lb = sum(1 for c in centres if c in R[u] and v in R[c])
            ub = len(R[u]) - sum(1 for c in centres if c in R[u] and v not in R[c])
            ok = False
            for a in a_opts:
                for b in b_opts:
                    beta = a + b
                    if Buv == 1 and beta > 1:
                        continue
                    req = 4 - Buv - s_ov(u, v) - 2 * Duv - 2 * beta
                    if req >= 0 and lb <= req <= ub:
                        ok = True
            if not ok:
                return False, f"pair {name(u)},{name(v)}"
    for v in range(NORB):
        if v in centres:
            continue
        nb = [c for c in centres if v in R[c]]
        if len(nb) > 10:
            return False, f"degree {name(v)}"
        pv = known_partner.get(v)
        for k in range(7):
            cnt = sum(1 for c in nb if k in cell(c))
            mx = 4 - 2 * (k in cell(v)) - (2 * (k in cell(pv)) if pv is not None else 0)
            if cnt > mx:
                return False, f"P-bound {name(v)} k={k+1}"
    return True, ""


def search():
    ALL = set(range(NORB))
    zero_cells = {o for o in ALL if 0 in cell(o)}
    canon = {c for c in range(len(CELLS)) if c not in (X // 2, PX // 2, W1 // 2, W2 // 2)}
    allowed_x = ALL - zero_cells - {PX}
    nx = 0
    for Rx in rows_with(X, PX, {W1, W2}, allowed_x, None, canon_cells=canon):
        nx += 1
        allowed_px = ALL - zero_cells - {X} - (Rx - {W1, W2})
        for Rpx in rows_with(PX, X, {W1, W2}, allowed_px, None,
                             extra_ok=lambda R: R & Rx == {W1, W2}):
            # pi w1: not adjacent to x or pi x, no coordinate 1 (index 0)
            for pw1 in sorted(ALL - zero_cells - Rx - Rpx - {X, PX, W1, W2}):
                allowed_w1 = ALL - Rx - {W1, W2, pw1}
                for Rw1 in rows_with(W1, pw1, {X, PX}, allowed_w1, None,
                                     extra_ok=lambda R: len(R & (Rpx - {W1, W2})) == 1):
                    for pw2 in sorted(ALL - zero_cells - Rx - Rpx - Rw1 - {X, PX, W1, W2, pw1}):
                        allowed_w2 = ALL - Rx - {W1, W2, pw2, pw1}
                        for Rw2 in rows_with(W2, pw2, {X, PX}, allowed_w2, None,
                                             extra_ok=lambda R: len(R & (Rpx - {W1, W2})) == 1
                                             and len(R & Rw1) == 3 and pw2 not in Rw1):
                            R = {X: Rx, PX: Rpx, W1: Rw1, W2: Rw2}
                            P = {X: PX, PX: X, W1: pw1, W2: pw2}
                            ok, why = local_ok(R, P)
                            if ok:
                                return R, P, nx
    return None, None, nx


if __name__ == '__main__':
    try:
        R, P, nx = search()
    except TimeoutError:
        print(f"TIMEOUT after {CAP} s (no conclusion)")
        sys.exit(0)
    print(f"time {time.time()-T0:.1f} s, first-row candidates visited: {nx}")
    if R is None:
        print("NO configuration in case (alpha,alpha) at this radius")
    else:
        for c in (X, PX, W1, W2):
            print(name(c), "partner", name(P[c]), "row", sorted(name(o) for o in R[c]))
        out = {name(c): {"partner": name(P[c]), "row": sorted(name(o) for o in R[c])} for c in R}
        json.dump(out, open('data/c13_config_alpha_alpha.json', 'w'), indent=1)
        print("saved data/c13_config_alpha_alpha.json")
