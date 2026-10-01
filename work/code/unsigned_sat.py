"""unsigned_sat.py -- exact CNF encoding of the UNSIGNED sigma-quotient system (m = 7).

Unknowns: B (symmetric 0/1, zero diagonal) and D (perfect matching = pi) on the 42 orbits.
Constraints (exactly the facts (Deg), (P), (Q) of LEMMA_H.md section 0, plus D a perfect matching
disjoint from B):
  (Deg)  sum_y B_xy = deg[x]                                   (real problem: 10)
  (P)    #{y : B_xy = 1, k in supp y} = base(x,k) - 2*[k in supp pi(x)]   (real: base = 4 - 2[k in supp x])
  (Q)    K_xy + 2 L_xy = c(x,y)  for x < y, where
         K_xy = (B^2)_xy + B_xy,  L_xy = (BD)_xy + (DB)_xy + D_xy          (real: c = 4 - s(x,y))
The right-hand sides are parameters so that the same code can be validated on planted instances.
Nothing about signs / N is encoded: this is a relaxation of feasibility of (N, D).
"""
import itertools
from pysat.formula import IDPool
from pysat.card import CardEnc, EncType

CELLS = list(itertools.combinations(range(7), 2))
NORB = 42
SUPP = [set(CELLS[x // 2]) for x in range(NORB)]


def s_ov(x, y):
    return len(SUPP[x] & SUPP[y])


class Enc:
    def __init__(self):
        self.pool = IDPool()
        self.clauses = []
        self.T = self.pool.id('TRUE')
        self.clauses.append([self.T])

    def v(self, name):
        return self.pool.id(name)

    def add(self, lits):
        """add a clause, simplifying the constant literals +-T"""
        out = []
        for l in lits:
            if l == self.T:
                return
            if l == -self.T:
                continue
            out.append(l)
        self.clauses.append(out)   # an empty clause makes the formula UNSAT (intended)

    def b(self, x, y):
        if x > y:
            x, y = y, x
        return self.v(('b', x, y))

    def d(self, x, y):
        if x > y:
            x, y = y, x
        return self.v(('d', x, y))

    def AND(self, a, c, name):
        t = self.v(name)
        self.add([-t, a]); self.add([-t, c]); self.add([t, -a, -c])
        return t

    def OR(self, lits, name):
        o = self.v(name)
        for l in lits:
            self.add([-l, o])
        self.add([-o] + list(lits))
        return o

    def counter(self, lits, kmax, name):
        """unary sequential counter with full equivalence: returns out[0..kmax], out[j] <-> (sum >= j)."""
        T, F = self.T, -self.T
        prev = [T] + [F] * kmax
        for i, x in enumerate(lits, start=1):
            cur = [T]
            for j in range(1, kmax + 1):
                a, c = prev[j], prev[j - 1]          # s = a OR (x AND c)
                if a == T:
                    cur.append(T); continue
                if c == F:
                    cur.append(a); continue
                s = self.v((name, i, j))
                if a != F:
                    self.add([-a, s])
                self.add([-x, -c, s])                 # (c may be T: then clause is [-x, s])
                self.add([-s, a, x])                  # s -> a or x
                self.add([-s, a, c])                  # s -> a or c
                cur.append(s)
            prev = cur
        return prev

    def eq_const(self, out, t, conds):
        """(AND of conds) -> sum == t, given counter outputs out[0..kmax]."""
        kmax = len(out) - 1
        pre = [-c for c in conds]
        if t < 0:
            self.add(pre); return
        if t >= 1:
            if t > kmax:
                raise ValueError('kmax too small')
            self.add(pre + [out[t]])
        if t + 1 > kmax:
            raise ValueError('kmax too small for upper bound')
        self.add(pre + [-out[t + 1]])


def build(deg, base, crhs, kmaxK=5, kmaxF=5):
    E = Enc()
    n = NORB
    for x in range(n):   # D perfect matching
        cnf = CardEnc.equals(lits=[E.d(x, y) for y in range(n) if y != x], bound=1,
                             vpool=E.pool, encoding=EncType.seqcounter)
        for cl in cnf.clauses:
            E.add(cl)
    for x in range(n):   # D disjoint from B
        for y in range(x + 1, n):
            E.add([-E.d(x, y), -E.b(x, y)])
    for x in range(n):   # (Deg)
        cnf = CardEnc.equals(lits=[E.b(x, y) for y in range(n) if y != x], bound=deg[x],
                             vpool=E.pool, encoding=EncType.seqcounter)
        for cl in cnf.clauses:
            E.add(cl)
    P = {}
    for x in range(n):   # P(x,y) = (BD)_xy = OR_w (B_xw and D_wy)
        for y in range(n):
            if x == y:
                continue
            ts = [E.AND(E.b(x, w), E.d(w, y), ('t', x, y, w)) for w in range(n) if w not in (x, y)]
            P[(x, y)] = E.OR(ts, ('P', x, y))
    for x in range(n):   # (Q)
        for y in range(x + 1, n):
            ks = [E.AND(E.b(x, w), E.b(w, y), ('a', x, y, w)) for w in range(n) if w not in (x, y)]
            ks.append(E.b(x, y))
            K = E.counter(ks, kmaxK, ('K', x, y))
            L = E.counter([P[(x, y)], P[(y, x)], E.d(x, y)], 3, ('L', x, y))
            E.add([-L[3]])
            c = crhs(x, y)
            E.eq_const(K, c, [-L[1]])          # L = 0
            E.eq_const(K, c - 2, [L[1], -L[2]])  # L = 1
            E.eq_const(K, c - 4, [L[2]])       # L = 2
    for x in range(n):   # (P)
        for k in range(7):
            ys = [y for y in range(n) if y != x and k in SUPP[y]]
            cnt = E.counter([E.b(x, y) for y in ys], kmaxF, ("F", x, k))
            e = E.OR([E.d(x, y) for y in ys], ('e', x, k))
            E.eq_const(cnt, base(x, k), [-e])
            E.eq_const(cnt, base(x, k) - 2, [e])
    return E


def build_real():
    return build(deg=[10] * NORB,
                 base=lambda x, k: 4 - 2 * (k in SUPP[x]),
                 crhs=lambda x, y: 4 - s_ov(x, y))


def class_assumptions(E, Ycells):
    """type-2 cells Ycells (indices into CELLS): D pairs (c,+),(c,-) iff c in Ycells."""
    return [E.d(2 * c, 2 * c + 1) if c in Ycells else -E.d(2 * c, 2 * c + 1) for c in range(21)]


def decode(E, model):
    import numpy as np
    pos = set(l for l in model if l > 0)
    B = np.zeros((NORB, NORB), dtype=np.int64); D = np.zeros((NORB, NORB), dtype=np.int64)
    for x in range(NORB):
        for y in range(x + 1, NORB):
            if E.b(x, y) in pos: B[x, y] = B[y, x] = 1
            if E.d(x, y) in pos: D[x, y] = D[y, x] = 1
    return B, D


def verify_unsigned(B, D):
    """independent numpy check of the unsigned system (real right-hand sides). Returns list of failures."""
    import numpy as np
    fails = []
    Mm = np.zeros((NORB, 7), dtype=np.int64)
    for x in range(NORB):
        for k in SUPP[x]:
            Mm[x, k] = 1
    I = np.eye(NORB, dtype=np.int64)
    if not ((B == B.T).all() and (np.diag(B) == 0).all() and set(np.unique(B)) <= {0, 1}): fails.append('B shape')
    if not ((D == D.T).all() and (D.sum(1) == 1).all() and (np.diag(D) == 0).all()): fails.append('D matching')
    if (B * D).any(): fails.append('B meets D')
    if not (B.sum(1) == 10).all(): fails.append('degree')
    if not (B @ Mm == 4 - 2 * Mm - 2 * (D @ Mm)).all(): fails.append('profile P')
    lhs = B @ B + B + Mm @ Mm.T + 2 * (B @ D + D @ B + D)
    off = ~np.eye(NORB, dtype=bool)
    if not (lhs[off] == 4).all(): fails.append('Q equations (%d bad)' % int((lhs[off] != 4).sum()))
    return fails
