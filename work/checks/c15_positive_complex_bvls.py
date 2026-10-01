r"""c15 microscope (one process, < 10 s, < 100 MB). Exact question: in BvLS (m = 11), with the edge census of
OVERLAP_EXPLORATION.md s.2, (a) does every B-edge have neg = 1 and pos = 2 (all edges there have s = 0, beta = 0)?
(b) is every vertex link of the positive-triangle complex P a single cycle (P a closed surface)?
(c) is P orientable?  (d) chi(P).  Structural exploration only; not used to reject any m = 7 statement."""
import numpy as np, itertools, collections
N = np.load('data/bvls_m11_N.npy'); D = np.load('data/bvls_m11_D.npy'); n = N.shape[0]
B = np.abs(N)
edges = [(x, y) for x in range(n) for y in range(x + 1, n) if B[x, y]]
tri_pos, tri_neg = [], []
for x, y in edges:
    for z in range(y + 1, n):
        if B[x, z] and B[y, z]:
            (tri_pos if N[x, y] * N[y, z] * N[x, z] == 1 else tri_neg).append((x, y, z))
pos = collections.Counter(); neg = collections.Counter()
for t in tri_pos:
    for e in itertools.combinations(t, 2): pos[e] += 1
for t in tri_neg:
    for e in itertools.combinations(t, 2): neg[e] += 1
census = collections.Counter((neg[e], pos[e]) for e in edges)
print('n', n, 'edges', len(edges), 'pos triangles', len(tri_pos), 'neg triangles', len(tri_neg))
print('(neg,pos) census over edges:', dict(census))
# links
link_shapes = collections.Counter()
for x in range(n):
    adj = collections.defaultdict(set)
    for t in tri_pos:
        if x in t:
            a, b = [v for v in t if v != x]
            adj[a].add(b); adj[b].add(a)
    seen, comps = set(), []
    for v in adj:
        if v in seen: continue
        stack, comp = [v], []
        seen.add(v)
        while stack:
            u = stack.pop(); comp.append(u)
            for w in adj[u]:
                if w not in seen: seen.add(w); stack.append(w)
        comps.append(len(comp))
    link_shapes[tuple(sorted(comps))] += 1
print('vertex link component sizes (multiset -> #vertices):', dict(link_shapes))
# orientability: orient faces so that each shared edge is traversed oppositely
faces = tri_pos
edge_faces = collections.defaultdict(list)
for i, (a, b, c) in enumerate(faces):
    for e in ((a, b), (b, c), (a, c)): edge_faces[e].append(i)
orient = {}
def dir_edges(face, o):
    a, b, c = face
    cyc = [(a, b), (b, c), (c, a)] if o == 1 else [(b, a), (c, b), (a, c)]
    return set(cyc)
ok = True
for start in range(len(faces)):
    if start in orient: continue
    orient[start] = 1; queue = [start]
    while queue and ok:
        f = queue.pop()
        de = dir_edges(faces[f], orient[f])
        for (u, v) in de:
            e = (min(u, v), max(u, v))
            for g in edge_faces[e]:
                if g == f: continue
                want = -1 if (u, v) in dir_edges(faces[g], 1) else 1
                if g in orient:
                    if orient[g] != want: ok = False
                else:
                    orient[g] = want; queue.append(g)
print('orientable:', ok)
V = n; E = len(edges); F = len(faces)
print('chi(P) = V - E + F =', V - E + F)
