"""Exact finite witness checks and explicit graph reconstruction.

This module does not search for N and does not assume the real-integrality theorem
when checking an integral N,D pair. m=2 and m=11 are supported solely for bounded
positive controls; the theorem dossier concerns m=7.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np


class VerificationError(ValueError):
    """The supplied object fails an explicitly checked condition."""


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def _matrix(value: Any, size: int, allowed: set[int], name: str) -> np.ndarray:
    if isinstance(value, np.ndarray):
        value = value.tolist()
    _check(isinstance(value, list) and len(value) == size, f'{name}: wrong row count')
    for row in value:
        _check(isinstance(row, list) and len(row) == size, f'{name}: wrong column count')
        _check(all(type(x) in (int, bool) and x in allowed for x in row),
               f'{name}: use exact JSON integer entries in {sorted(allowed)}')
    return np.array(value, dtype=np.int64)


def labels(m: int) -> tuple[list[tuple[int, int]], np.ndarray]:
    _check(type(m) is int and m in (2, 7, 11), 'm must be 2, 7, or 11; 2 and 11 are controls')
    cells = [(i, j) for i in range(m) for j in range(i + 1, m)]
    R = np.zeros((2 * len(cells), m), dtype=np.int64)
    for c, (i, j) in enumerate(cells):
        R[2*c, i] = R[2*c+1, i] = 1
        R[2*c, j], R[2*c+1, j] = 1, -1
    return cells, R


def validate_signed(N: Any, m: int = 7) -> np.ndarray:
    _, R = labels(m)
    n = len(R)
    N = _matrix(N, n, {-1, 0, 1}, 'N')
    _check(np.array_equal(N, N.T), 'N must be symmetric')
    _check(not np.diag(N).any(), 'N must have zero diagonal')
    _check(not (N @ R).any(), 'NR is not zero')
    _check(np.array_equal(N @ N, N + (2*m-2)*np.eye(n, dtype=np.int64) - R @ R.T),
           'The COMPLETE signed quadratic equation fails')
    return N


def validate_pair(N: Any, D: Any, m: int = 7) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    N = validate_signed(N, m)
    n = len(N)
    _, R = labels(m)
    M, B = abs(R), abs(N)
    D = _matrix(D, n, {0, 1}, 'D')
    _check(np.array_equal(D, D.T), 'D must be symmetric')
    _check(not np.diag(D).any(), 'D must have zero diagonal')
    _check(bool((D.sum(axis=1) == 1).all()), 'D must have row sum one')
    _check(not (D * B).any(), 'D and B have intersecting support')
    _check(np.array_equal(D @ D, np.eye(n, dtype=np.int64)), 'D squared is not identity')
    Q = B + 2 * D
    _check(np.array_equal(Q @ M, 4*np.ones((n, m), dtype=np.int64) - 2*M),
           'Ordinary block equation fails')
    _check(np.array_equal(Q @ Q + Q, (2*m-2)*np.eye(n, dtype=np.int64)
                        + 4*np.ones((n, n), dtype=np.int64) - M @ M.T),
           'Ordinary quadratic equation fails')
    E2 = (2*m-6)*np.eye(n, dtype=np.int64) + 4*np.ones_like(B) - M@M.T - B@B - B
    _check(np.array_equal(2*(B@D+D@B+D), E2), 'Expanded linear equation fails')
    return N, D, Q


def build_graph(N: Any, D: Any, m: int = 7) -> tuple[np.ndarray, list[int]]:
    N, D, Q = validate_pair(N, D, m)
    _, R = labels(m)
    M = abs(R)
    rp, rm = (M+R)//2, (M-R)//2
    a, b = (Q-N)//2, (Q+N)//2
    K = np.block([[rp.T, rm.T], [rm.T, rp.T]])
    H = np.block([[a, b], [b, a]])
    Im = np.eye(m, dtype=np.int64)
    F = np.block([[np.zeros_like(Im), Im], [Im, np.zeros_like(Im)]])
    n, v = len(N), 1 + 2*m*m
    A = np.zeros((v, v), dtype=np.int64)
    start = 1+2*m
    A[0, 1:start] = A[1:start, 0] = 1
    A[1:start, 1:start] = F
    A[1:start, start:] = K
    A[start:, 1:start] = K.T
    A[start:, start:] = H
    p = list(range(v))
    for i in range(m):
        p[1+i], p[1+m+i] = 1+m+i, 1+i
    for u in range(n):
        p[start+u], p[start+n+u] = start+n+u, start+u
    verify_graph(A, m, p)
    return A, p


def verify_graph(A: Any, m: int = 7, permutation: Any = None) -> dict[str, Any]:
    labels(m)
    v = 1+2*m*m
    A = _matrix(A, v, {0, 1}, 'A')
    _check(np.array_equal(A, A.T), 'A must be symmetric')
    _check(not np.diag(A).any(), 'A must have zero diagonal')
    _check(bool((A.sum(axis=1) == 2*m).all()), 'Incorrect vertex degree')
    _check(np.array_equal(A @ A + A, (2*m-2)*np.eye(v, dtype=np.int64) + 2*np.ones_like(A)),
           'The full exact SRG identity fails')
    out: dict[str, Any] = {'vertices': v, 'parameters': [v, 2*m, 1, 2],
                          'binary_symmetric_simple': True, 'exact_SRG_identity': True,
                          'involution_checked': permutation is not None,
                          'scope': 'C2 witness check' if m == 7 else 'positive control, not Conway 99'}
    if permutation is not None:
        if isinstance(permutation, np.ndarray):
            permutation = permutation.tolist()
        _check(isinstance(permutation, list) and len(permutation) == v, 'Wrong permutation size')
        _check(all(type(x) is int for x in permutation), 'Permutation entries must be integers')
        _check(sorted(permutation) == list(range(v)), 'Not a permutation of 0,...,v-1')
        p = np.array(permutation, dtype=np.int64)
        _check(np.array_equal(p[p], np.arange(v)), 'Permutation is not involutory')
        _check(not np.array_equal(p, np.arange(v)), 'Permutation is the identity')
        _check(np.array_equal(A[np.ix_(p,p)], A), 'Permutation does not preserve adjacency')
        out['nontrivial_involution_verified'] = True
        out['fixed_vertices'] = int(np.count_nonzero(p == np.arange(v)))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--graph', type=Path, help='JSON matrix, or object with A and optional permutation')
    group.add_argument('--pair', type=Path, help='JSON object with complete integer N and D')
    parser.add_argument('--m', type=int, choices=(2, 7, 11), default=7)
    parser.add_argument('--output', type=Path, help='Write a reconstructed witness only in --pair mode')
    args = parser.parse_args()
    try:
        payload = json.loads((args.graph or args.pair).read_text(encoding='utf-8'))
        if args.graph:
            result = verify_graph(payload['A'] if isinstance(payload, dict) else payload, args.m,
                                  payload.get('permutation') if isinstance(payload, dict) else None)
        else:
            _check(isinstance(payload, dict) and 'N' in payload and 'D' in payload,
                   'Pair input requires keys N and D')
            A, p = build_graph(payload['N'], payload['D'], args.m)
            result = verify_graph(A, args.m, p)
            if args.output:
                args.output.write_text(json.dumps({'m': args.m, 'A': A.tolist(),
                                                   'permutation': p, 'verification': result}, indent=2)+'\n',
                                       encoding='utf-8')
        print(json.dumps({'status': 'VERIFIED_SUPPLIED_WITNESS', **result}, indent=2))
        return 0
    except (OSError, json.JSONDecodeError, KeyError, VerificationError) as exc:
        print(json.dumps({'status': 'INPUT_OR_WITNESS_REJECTED', 'reason': str(exc),
                          'not_a_C2_nonexistence_result': True}, indent=2))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
