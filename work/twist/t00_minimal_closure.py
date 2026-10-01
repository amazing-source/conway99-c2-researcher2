r"""C-T0 (pre-registered in TWIST_CALCULUS.md s.1a/1b).

Start from kappa: every cell is type 2 (its two labels are D-paired).
Break t <= 4 cells and re-pair their 2t labels with no sibling pair. All other cells keep type 2.

Tests:
 (O)   Law O by counting: |Open_k| in {0, 4, 6, ..., 12} for all k.
 (K22) C2 Lemma 19.1, K_{2,2} form. Assume |Open_k| = 4 and the open labels at k are exactly the 4 labels
       of two cells, each of which has a type-1 label (this forces n_s = 0). Then the configuration dies.

Output: survivor counts for (O) and for (O)+(K22), and the survivor types up to S7.
Skeleton symmetry: S7 on coordinates, together with label swaps inside cells. A configuration is therefore
determined by its D-graph on cells (a multigraph of cell pairs).

Bounds: one process, < 10 s, < 50 MB.
"""
import itertools
from collections import Counter

CELLS = list(itertools.combinations(range(7), 2))
CID = {c: i for i, c in enumerate(CELLS)}


def matchings(labels):
    """Perfect matchings of a list of labels; label = 2*cell + s; sibling pairs are excluded."""
    if not labels:
        yield []
        return
    a = labels[0]
    for k in range(1, len(labels)):
        b = labels[k]
        if a // 2 == b // 2:
            continue
        rest = labels[1:k] + labels[k + 1:]
        for m in matchings(rest):
            yield [(a, b)] + m


def analyse(cells, M):
    pi = {}
    for a, b in M:
        pi[a] = b
        pi[b] = a
    openk = [[] for _ in range(7)]
    typ = {}
    for x, px in pi.items():
        cx, cp = set(CELLS[x // 2]), set(CELLS[px // 2])
        typ[x] = len(cx & cp)
        for k in cx - cp:
            openk[k].append(x)
    lawO = all(len(o) in (0, 4, 6, 8, 10, 12) for o in openk)
    k22 = False
    for k in range(7):
        o = openk[k]
        if len(o) == 4:
            cs = Counter(x // 2 for x in o)
            if len(cs) == 2 and all(v == 2 for v in cs.values()):
                if all(any(typ[2 * c + s] == 1 for s in (0, 1)) for c in cs):
                    k22 = True
    return lawO, k22


PERMS = list(itertools.permutations(range(7)))
_CACHE = {}


def canon(M):
    raw = tuple(sorted(tuple(sorted((a // 2, b // 2))) for a, b in M))   # cell-level D-graph
    if raw in _CACHE:
        return _CACHE[raw]
    best = None
    for p in PERMS:
        key = []
        for a, b in M:
            ca = tuple(sorted((p[CELLS[a // 2][0]], p[CELLS[a // 2][1]])))
            cb = tuple(sorted((p[CELLS[b // 2][0]], p[CELLS[b // 2][1]])))
            key.append(tuple(sorted((ca, cb))))
        key = tuple(sorted(key))
        if best is None or key < best:
            best = key
    _CACHE[raw] = best
    return best


for t in range(1, 5):
    nO = nOK = tot = 0
    typesO, typesOK = Counter(), Counter()
    for cells in itertools.combinations(range(21), t):
        labels = [2 * c + s for c in cells for s in (0, 1)]
        for M in matchings(labels):
            tot += 1
            lawO, k22 = analyse(cells, M)
            if lawO:
                nO += 1
                key = canon(M)
                typesO[key] += 1
                if not k22:
                    nOK += 1
                    typesOK[key] += 1
    print(f"t={t}: re-pairings {tot}, pass (O) {nO} [{len(typesO)} S7-types], pass (O)+(K22) {nOK} [{len(typesOK)} S7-types]")
    for key, n in sorted(typesO.items()):
        tag = 'survives K22' if key in typesOK else 'killed by K22'
        print('   ', key, n, tag)
