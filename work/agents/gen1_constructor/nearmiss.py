# nearmiss.py -- AGL(1,7)-invariant N with NR = 0 and row weight 10 (exact objects): size of the C2b defect.
# Memory bound: < 500 MB; single process; < 1 min.
import numpy as np, itertools
from symS import coord_elem, n, R, M, H
import unsigned_sym as US
from verify_sym import uf_classes
I=np.eye(n,dtype=np.int64)
mats,_=uf_classes([coord_elem(p,e) for (p,e) in [US.c7,US.m3]]); f=len(mats); Bm=[np.abs(A) for A in mats]
reps=[0,1]; mv=np.array([[int(A[r].sum()) for r in reps] for A in Bm]); sups=[]
def dfs(i,rem,ch):
    if not rem.any(): sups.append(list(ch)); return
    if i==f or np.any(mv[i:].sum(0)<rem): return
    if np.all(mv[i]<=rem): ch.append(i); dfs(i+1,rem-mv[i],ch); ch.pop()
    dfs(i+1,rem,ch)
dfs(0,np.array([10,10]),[]); res=[]
for sup in sups:
    B=sum(Bm[k] for k in sup)
    if np.any((B@M)%2) or not np.all(B.sum(1)==10): continue
    for sg in itertools.product((1,-1),repeat=len(sup)):
        N=sum(a*mats[k] for a,k in zip(sg,sup))
        if np.any(N@R): continue
        Dm=N@N-N-12*I+H; res.append((int((Dm!=0).sum()),int(np.abs(Dm).sum()),N,Dm))
res.sort(key=lambda t:(t[0],t[1]))
print('AGL(1,7)-invariant N with NR=0, weight 10:',len(res))
print('defect (#nonzero entries of N^2-N-12I+H, L1) of best 5:',[(a,b) for a,b,_,_ in res[:5]])
a,b,N,Dm=res[0]; np.save('nearmiss_AGL17_N.npy',N)
vals,cnt=np.unique(Dm[~np.eye(n,dtype=bool)],return_counts=True); print('best: off-diag defect values',dict(zip(vals.tolist(),cnt.tolist())),'diag',np.unique(np.diag(Dm)))
ev=np.linalg.eigvalsh(N.astype(float)); print('best: spectrum (rounded)',np.unique(np.round(ev,3),return_counts=True))
