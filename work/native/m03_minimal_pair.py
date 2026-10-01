r"""m03 (one process, < 2 min, < 300 MB). Exact questions on the m02 solution set (rebuilt by importing m02):
(a) the minimum number of disjoint-cell relations in which two distinct realizations differ, with an example;
(b) the kind of that minimal difference (support change or sign change), described in port-graph terms;
(c) how many realizations share the same UNSIGNED disjoint support (do supports determine signs at this scale?)."""
import importlib.util, itertools, collections, sys, io, contextlib
spec = importlib.util.spec_from_file_location('m02', 'native/m02_link_determinacy.py'); m02 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m02)
y, w, sols = m02.y, m02.w, m02.sols
keys = sorted({(x, z) for dy, dw in sols for x, d in ((y, dy), (w, dw)) for z in d} |
              {(x, z) for x in (y, w) for z in m02.L if not (m02.supp(z) & m02.supp(x)) and z != m02.pi[x]}, key=str)
vec = [tuple((dy if x == y else dw).get(z, 'n') for (x, z) in keys) for dy, dw in sols]
best = (99, None)
for a, b in itertools.combinations(range(len(vec)), 2):
    dist = sum(1 for u, v in zip(vec[a], vec[b]) if u != v)
    if dist < best[0]: best = (dist, (a, b))
d, (a, b) = best
print('(a) minimum number of differing disjoint relations between two realizations:', d)
diff = [(keys[t], vec[a][t], vec[b][t]) for t in range(len(keys)) if vec[a][t] != vec[b][t]]
for (x, z), u, v in diff: print('    pair', ('y' if x == y else 'w'), z, ':', u, '->', v)
kinds = {'sign' if {u, v} == {'m', 'p'} else 'support' for _, u, v in diff}
print('(b) kind of the minimal difference:', kinds)
supp_cls = collections.Counter(tuple(s != 'n' for s in v) for v in vec)
print('(c) realizations per unsigned disjoint support: max', max(supp_cls.values()), '| #supports', len(supp_cls),
      '| histogram', dict(collections.Counter(supp_cls.values())))
# sign freedom with support fixed: describe one class with >1 member
for sup, cnt in supp_cls.items():
    if cnt > 1:
        mem = [v for v in vec if tuple(s != 'n' for s in v) == sup]
        dd = [(keys[t], mem[0][t], mem[1][t]) for t in range(len(keys)) if mem[0][t] != mem[1][t]]
        print('    example sign-only ambiguity:', [(('y' if x == y else 'w'), z, u, v) for (x, z), u, v in dd]); break
