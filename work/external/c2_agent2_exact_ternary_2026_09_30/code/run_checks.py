"""Small exact controls for PROOF.md; NOT an exhaustive C2 search.

Run: python code/run_checks.py
Requires NumPy. Uses only integer arithmetic, including finite-field rank.
"""
from __future__ import annotations
import itertools
import json
from pathlib import Path
import numpy as np
from controls import labels, control

ROOT = Path(__file__).resolve().parents[1]


def rank_mod(a: np.ndarray, prime: int) -> int:
    a = np.asarray(a, dtype=np.int64).copy() % prime
    r = 0
    for c in range(a.shape[1]):
        where = np.flatnonzero(a[r:, c])
        if not len(where):
            continue
        k = r + int(where[0])
        a[[r, k]] = a[[k, r]]
        a[r] = a[r] * pow(int(a[r, c]), -1, prime) % prime
        for k in range(a.shape[0]):
            if k != r and a[k, c]:
                a[k] = (a[k] - a[k, c] * a[r]) % prime
        r += 1
        if r == a.shape[0]:
            break
    return r


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def capacity_values(n: np.ndarray, r: np.ndarray, kappa: int) -> dict:
    b = abs(n); m = abs(r); size = len(n)
    # Store twice T and E so no floating-point values occur.
    t2 = 4 * np.ones((size, r.shape[1]), dtype=np.int64) - 2 * m - b @ m
    e2 = ((kappa - 4) * np.eye(size, dtype=np.int64)
          + 4 * np.ones((size, size), dtype=np.int64) - m @ m.T - b @ b - b)
    tcap = bool(np.isin(t2, (0, 2)).all() and (t2.sum(1) == 4).all())
    ecap = bool((e2 >= 0).all() and (e2 % 2 == 0).all())
    return {'T_cap': tcap, 'E_cap': ecap,
            'T_twice_min': int(t2.min()), 'E_twice_min': int(e2.min())}


def scalar_windows() -> dict:
    linear = 0
    for number in (0, 2, 4):
        for signs in itertools.product((-1, 1), repeat=number):
            s = sum(signs)
            require(s % 2 == 0 and abs(s) <= 4, 'linear window')
            if s % 3 == 0:
                require(s == 0, 'nonzero linear lift error')
            linear += 1
    quadratic = accepted = 0
    # h here is allowed to range more widely than actual root inner products:
    # this tests a superset of the scalar cases used by the proof.
    for c in range(3):
        for h in range(-c, c + 1):
            if (h-c) % 2:
                continue
            for b in (0, 1):
                for ell in range(5):
                    if ell + b + c > 4 or (ell + b + c) % 2:
                        continue
                    for n_uv in ((0,) if b == 0 else (-1, 1)):
                        for walk_sum in range(-ell, ell + 1, 2):
                            f = walk_sum - n_uv + h
                            require(f % 2 == 0 and abs(f) <= 4, 'quadratic window')
                            if f % 3 == 0:
                                require(f == 0, 'nonzero quadratic lift error')
                                accepted += 1
                            quadratic += 1
    return {'linear_sign_assignments': linear, 'quadratic_scalar_cases': quadratic,
            'quadratic_cases_divisible_by_three': accepted, 'all_checks_pass': True}


def positive_controls() -> list[dict]:
    reports = []
    for m in (2, 11):
        a, n, b, d, q, r, mat = control(m)
        v = 2*m*m+1; kappa = 2*m-2
        require(a.shape == (v, v), 'control size')
        require(np.array_equal(a, a.T) and not np.diag(a).any(), 'simple graph')
        require(np.isin(a, (0, 1)).all(), 'boolean graph')
        require((a.sum(1) == 2*m).all(), 'degree')
        require(np.array_equal(a @ a + a, kappa * np.eye(v, dtype=np.int64)
                               + 2*np.ones((v, v), dtype=np.int64)), 'SRG identity')
        cv = capacity_values(n, r, kappa)
        require(cv['T_cap'] and cv['E_cap'], 'positive capacities')
        require(not (n @ r).any(), 'signed linear control')
        require(not (n @ n - n - kappa*np.eye(len(n), dtype=np.int64) + r @ r.T).any(),
                'signed quadratic control')
        require(np.array_equal(d @ d, np.eye(len(n), dtype=np.int64)), 'matching control')
        reports.append({'m': m, 'vertices': v, 'exterior_orbits': len(n),
                        'SRG_and_integer_signed_equations_verified': True,
                        **cv,
                        'scope': 'General bounded-window lemma, NOT the m=7 projector theorem.'})
    return reports


def finite_field_countermodel() -> dict:
    data = json.loads((ROOT/'data/ternary_projector_control.json').read_text())
    p = np.asarray(data['P'], dtype=np.int64)
    cells, r = labels(7); h = r @ r.T
    require(p.shape == (42,42) and np.isin(p, (0,1,2)).all(), 'P input')
    require(np.array_equal(p, p.T), 'P symmetric')
    require(np.array_equal(p @ p % 3, p), 'P idempotent')
    require(not (p @ r % 3).any(), 'PR=0')
    require((np.diag(p) == 1).all(), 'P diagonal')
    require(rank_mod(p, 3) == 15, 'P rank')
    n3 = (p+h) % 3; n = np.where(n3 == 2, -1, n3)
    require(np.array_equal(n, np.asarray(data['N_centered'])), 'centered lift')
    require(not np.diag(n).any(), 'N diagonal')
    require(not (n @ r % 3).any(), 'NR mod3')
    residual = n @ n - n - 12*np.eye(42, dtype=np.int64) + h
    require(not (residual % 3).any(), 'quadratic mod3')
    cv = capacity_values(n, r, 12)
    require(not cv['T_cap'], 'control should fail target capacity')
    require((n @ r).any() and residual.any(), 'control must not be full integer N')
    weights, counts = np.unique(abs(n).sum(1), return_counts=True)
    return {'all_five_ternary_projector_conditions_verified': True,
            'integer_linear_error_nonzero': True, 'integer_quadratic_error_nonzero': True,
            'row_weight_histogram': {str(int(x)): int(y) for x,y in zip(weights, counts)},
            **cv, 'is_C2_witness': False}


def zero_formula(x: int, y: int, z: int, a: int, b: int) -> int:
    choose2 = lambda n: n*(n-1)//2
    a,b = sorted((a,b))
    if (a,b) == (0,0): return 2*y+(x-2)*z+choose2(y)
    if (a,b) == (1,1): return 2*x+(y-2)*z+choose2(x)
    if (a,b) in ((2,2),(0,1)): return x*y+choose2(z)-1
    if (a,b) == (0,2): return z*(y+1)-1+choose2(x-1)
    if (a,b) == (1,2): return z*(x+1)-1+choose2(y-1)
    raise ValueError('invalid endpoint type')


def family_arithmetic() -> dict:
    cells,r = labels(7); u = r[::2]
    supports=[]; direct_formula_checks=0
    for vals in itertools.product(range(3), repeat=7):
        x,y,z = (vals.count(i) for i in range(3))
        n = np.zeros((21,21), dtype=np.int64)
        for row,(i,j) in enumerate(cells):
            for col,(k,l) in enumerate(cells):
                if row == col: continue
                common = set((i,j)) & set((k,l))
                if common:
                    other = list(set((i,j)) ^ set((k,l)))
                    n[row,col] = (1-vals[other[0]]-vals[other[1]]) % 3
                else:
                    n[row,col] = (-vals[i]-vals[j]-vals[k]-vals[l]-1) % 3
        degree = (n != 0).sum(1)
        for row,(i,j) in enumerate(cells):
            require(20-int(degree[row]) == zero_formula(x,y,z,vals[i],vals[j]), 'zero-count formula')
            direct_formula_checks += 1
        if (degree <= 10).all(): supports.append(vals)
    require(supports == [(2,)*7], 'unexpected surviving seven-value pattern')
    gg = 12*np.eye(21, dtype=np.int64)-u @ u.T
    require(not (gg @ np.ones(21, dtype=np.int64)).any(), 'kernel upper bound')
    require(rank_mod(gg,101) == 20, 'integer Gram rank lower bound')
    require(np.array_equal(u.T @ u, 5*np.eye(7,dtype=np.int64)+np.ones((7,7),dtype=np.int64)), 'U Gram')
    return {'seven_value_assignments_checked': 3**7,
            'individual_zero_count_formulas_checked': direct_formula_checks,
            'surviving_value_patterns': [list(v) for v in supports],
            'integer_Gram_rank': 20,
            'scope': 'Checks of the written hand proof, NOT enumeration of the 3^105 lifts.'}


def main() -> None:
    report = {'date': '2026-09-30', 'status': 'ALL_BOUNDED_CHECKS_PASS',
              'not_a_proof_of_C2_nonexistence': True,
              'scalar_windows': scalar_windows(),
              'positive_graph_controls': positive_controls(),
              'finite_field_countermodel': finite_field_countermodel(),
              'excluded_family_arithmetic': family_arithmetic(),
              'newly_excluded_original_envelope_ids': [],
              'newly_excluded_original_rank17_pair_ids': []}
    (ROOT/'checks').mkdir(exist_ok=True)
    (ROOT/'checks/results.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
