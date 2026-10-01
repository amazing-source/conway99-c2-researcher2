# C05: single bounded diagnostic SAT pass of the UNSIGNED system over the 133 support classes
# (data/classify_XH_v1.txt), one representative per S7-class.  Class = assumptions on the 21
# cell-diagonal D variables (type 2 iff in Y).  Conflict budget per class; global guard 270 s.
# Records status, time, and the failed-assumption core (subset of the 21 cell assumptions).
# One process, memory < 2 GB.  SAT models are re-verified independently with numpy.
import sys, time, re, json
import numpy as np
BASE = r"C:\Users\bfhdh\Downloads\conway_c2_researcher2_start_2026_09_30\conway_c2_researcher2_start_2026_09_30\work"
sys.path.insert(0, BASE + r"\code")
import unsigned_sat as U
from pysat.solvers import Cadical153

BUDGET = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
GUARD = 270.0
t0 = time.time()
ci = {c: i for i, c in enumerate(U.CELLS)}
classes = []
for line in open(BASE + r"\data\classify_XH_v1.txt"):
    if not line.startswith("|X|="): continue
    ys = line.split("Y(type-2 cells):")[1].split()
    Y = {ci[(int(p[0]) - 1, int(p[1]) - 1)] for p in ys}
    lab = int(re.search(r"labelled=\s*(\d+)", line).group(1))
    classes.append((Y, lab))
print(f"{len(classes)} classes parsed; budget {BUDGET} conflicts/class", flush=True)
E = U.build_real()
print(f"encoding built: vars={E.pool.top} clauses={len(E.clauses)} t={time.time()-t0:.1f}s", flush=True)
res = []
with Cadical153(bootstrap_with=E.clauses) as S:
    for idx, (Y, lab) in enumerate(classes):
        if time.time() - t0 > GUARD:
            res.append(dict(idx=idx, Y=sorted(Y), status="NOT_RUN")); continue
        assum = U.class_assumptions(E, Y)
        t1 = time.time()
        S.conf_budget(BUDGET)
        r = S.solve_limited(assumptions=assum)
        dt = time.time() - t1
        rec = dict(idx=idx, n2=len(Y), labelled=lab, Y=[f"{U.CELLS[c][0]+1}{U.CELLS[c][1]+1}" for c in sorted(Y)], time=round(dt, 2))
        if r is True:
            B, D = U.decode(E, S.get_model()); fails = U.verify_unsigned(B, D)
            rec["status"] = "SAT"; rec["verify_fails"] = fails
            np.save(BASE + rf"\data\unsigned_model_class{idx}_B.npy", B); np.save(BASE + rf"\data\unsigned_model_class{idx}_D.npy", D)
        elif r is False:
            core = S.get_core() or []
            cs = set(abs(l) for l in core)
            rec["status"] = "UNSAT"
            rec["core_type2"] = [f"{U.CELLS[c][0]+1}{U.CELLS[c][1]+1}" for c in range(21) if E.d(2*c, 2*c+1) in cs and c in Y]
            rec["core_nontype2"] = [f"{U.CELLS[c][0]+1}{U.CELLS[c][1]+1}" for c in range(21) if E.d(2*c, 2*c+1) in cs and c not in Y]
        else:
            rec["status"] = "UNKNOWN"
        res.append(rec)
        print(idx, rec["status"], "n2=", len(Y), f"{dt:.1f}s", rec.get("core_type2", ""), rec.get("core_nontype2", ""), flush=True)
json.dump(res, open(BASE + rf"\data\sat_pass_133_budget{BUDGET}.json", "w"), indent=1)
from collections import Counter
print("summary:", Counter(r["status"] for r in res), f"total {time.time()-t0:.1f}s")
