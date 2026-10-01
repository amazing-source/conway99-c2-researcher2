"""c11: parameter-determined substructure counts used in the Burnside parity check (one process, < 2 s, < 50 MB).
Formula for an srg(n,k,1,mu): closed 5-walks = 10*c5 + 5*2*T*(3k-3) (triangle + one back-and-forth step, the
3 double-counted words removed); 5-cycles with a chord = |E|*(k-2); induced pentagons = c5 - |E|*(k-2).
Validated by brute force on Paley(9) = K3 x K3, then evaluated for srg(99,14,1,2)."""
import itertools, numpy as np

def formula(n, k, lam, mu, ev):
    E = n * k // 2; T = n * k * lam // 6
    tr5 = sum(m * t ** 5 for t, m in ev)
    c5 = (tr5 - 5 * 2 * T * (3 * k - 3)) // 10
    return dict(tr5=tr5, T=T, E=E, c5=c5, induced5=c5 - E * (k - 2),
                induced4=(n * (n - 1) // 2 - E) // 2)

# brute force on K3 x K3
V = [(i, j) for i in range(3) for j in range(3)]
adj = {(u, v) for u in V for v in V if u != v and (u[0] == v[0] or u[1] == v[1])}
A = np.array([[1 if (u, v) in adj else 0 for v in V] for u in V])
c5 = set(); ind5 = 0
for cyc in itertools.permutations(range(9), 5):
    if cyc[0] != min(cyc) or cyc[1] > cyc[4]:
        continue
    if all(A[cyc[i], cyc[(i + 1) % 5]] for i in range(5)):
        c5.add(cyc)
        chords = sum(A[cyc[i], cyc[j]] for i in range(5) for j in range(i + 2, 5) if not (i == 0 and j == 4))
        ind5 += chords == 0
print('Paley(9) brute force: tr(A^5) =', int(np.trace(np.linalg.matrix_power(A, 5))), ' c5 =', len(c5), ' induced5 =', ind5)
print('Paley(9) formula    :', formula(9, 4, 1, 2, [(4, 1), (1, 4), (-2, 4)]))
print('srg(99,14,1,2)      :', formula(99, 14, 1, 2, [(14, 1), (3, 54), (-4, 44)]))
