# C06: analysis of the first SAT pass (no new SAT calls). Cores from data/sat_pass_133_budget20000.json
# are sufficient conditions for UNSAT: (cells in core_type2 all type 2) and (cells in core_nontype2 all
# non-type-2). By S7-invariance any image of a core is also forbidden. We canonicalise the cores and test
# which of the 133 classes contain an image of some core.
import json, itertools
BASE = r"C:\Users\bfhdh\Downloads\conway_c2_researcher2_start_2026_09_30\conway_c2_researcher2_start_2026_09_30\work"
res = json.load(open(BASE + r"\data\sat_pass_133_budget20000.json"))
import itertools as _it
_CELLS = list(_it.combinations(range(7), 2))
cellset = lambda lst: frozenset((_CELLS[p] if isinstance(p, int) else tuple(sorted((int(p[0]) - 1, int(p[1]) - 1)))) for p in lst)
perms = list(itertools.permutations(range(7)))
def img(S, p): return frozenset(tuple(sorted((p[a], p[b]))) for a, b in S)
def canon(S, T=frozenset()):
    return min((tuple(sorted(img(S, p))), tuple(sorted(img(T, p)))) for p in perms)
cores = {}
for r in res:
    if r["status"] != "UNSAT": continue
    S, T = cellset(r["core_type2"]), cellset(r["core_nontype2"])
    cores.setdefault(canon(S, T), []).append(r["idx"])
print("distinct cores (up to S7):", len(cores))
for (S, T), idxs in sorted(cores.items(), key=lambda kv: (len(kv[0][0]) + len(kv[0][1]), kv[0])):
    degs = [0]*7
    for a, b in S: degs[a] += 1; degs[b] += 1
    print(f"  |type2|={len(S)} |non2|={len(T)} type2={[f'{a+1}{b+1}' for a,b in S]} non2={[f'{a+1}{b+1}' for a,b in T]} from classes {idxs[:6]}{'...' if len(idxs)>6 else ''}")
# which unresolved classes contain an image of a core?
all_cells = frozenset(itertools.combinations(range(7), 2))
unres = [r for r in res if r["status"] != "UNSAT"]
core_list = list(cores.keys())
# precompute images of each core
core_imgs = []
for S, T in core_list:
    ims = set((img(frozenset(S), p), img(frozenset(T), p)) for p in perms)
    core_imgs.append(ims)
killed = 0
for r in unres:
    Y = cellset(r["Y"]); X = all_cells - Y
    hit = None
    for ci_, ims in enumerate(core_imgs):
        for S, T in ims:
            if S <= Y and T <= X: hit = ci_; break
        if hit is not None: break
    if hit is not None: killed += 1
    print(f"class {r['idx']:3d} status={r['status']:8s} n2={len(Y)} Y={sorted(f'{a+1}{b+1}' for a,b in Y)}  "
          + (f"contains core #{hit} {[f'{a+1}{b+1}' for a,b in core_list[hit][0]]}" if hit is not None else "NO known core"))
print("unresolved:", len(unres), " killed by known cores:", killed)
