# Candidate input formats

## Signed core

Use a JSON object with key `N` and a 42×42 matrix of integer entries −1,0,1. Its label order is:

- cells {i,j}, with 1≤i<j≤7, in lexicographic order;
- within each cell, the row e_i+e_j first and e_i−e_j second.

The code uses 0-based internal indices but the same order. `N` must be complete and satisfy the exact signed equations. An all-zero 42×42 matrix is NOT a valid example or a starting witness.

## Signed core plus integral completion

Use an object with keys `N` and `D`. Both are 42×42, in the same orbit order. D must have binary entries, zero diagonal, symmetry, one 1 per row, and no overlap with |N|.

## Full graph

Use a matrix, or an object with keys `A` and optionally `permutation`. A is 99×99 binary. `permutation` is a list of 99 zero-based vertex images. The supplied reconstruction code uses the vertex order in `GRAPH_RECONSTRUCTION.md`.

No valid m=7 candidate input is supplied: none was found in this investigation. The actual example under `checks/positive_control_m2.json` is a clearly marked 9-vertex positive control and requires `--m 2`.
