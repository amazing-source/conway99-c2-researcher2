# qsearch.py -- tabu search for a complete UNSIGNED pair (B,D): Q=B+2D, C3: Q^2+Q+K=12I+4J, C4: QM=4J-2M.
# D = fixed perfect matching (random, or random with prescribed type); single-pair toggles of B, exact O(1)
# vectorised delta (derived in NOTES s.4). If F=0: exact re-verification + signing CSP (unsigned_all.signings).
# Memory bound: < 300 MB. Single process. Wall-time cap from argv (<= 280 s).
import numpy as np, sys, time
from symS import n, R, M, H, K, orbs
seed=int(sys.argv[1]); tcap=float(sys.argv[2]); mode=sys.argv[3]
rng=np.random.default_rng(seed); I=np.eye(n); Jm=np.ones((n,n)); T4=4*np.ones((n,7))-2*M
def ov(x,y): return len({orbs[x][0],orbs[x][1]}&{orbs[y][0],orbs[y][1]})
def randD():
    while True:
        p=list(rng.permutation(n)); D=np.zeros((n,n)); ok=True; used=set()
        for x in p:
            if x in used: continue
            c=[y for y in p if y!=x and y not in used and (mode=='any' or ov(x,y)==int(mode))]
            if not c: ok=False; break
            y=c[0]; D[x,y]=D[y,x]=1; used|={x,y}
        if ok: return D
D=randD(); Mf=M.astype(float); Kf=K.astype(float)
B=np.zeros((n,n))
allowed=(1-D-I)
iu=np.triu_indices(n,1); al=allowed[iu]>0
def resid(B):
    Q=B+2*D; Rq=Q@Q+Q+Kf-12*I-4*Jm; Rm=Q@Mf-T4; return Q,Rq,Rm
# greedy start: random 10-regular-ish
for x in range(n):
    c=[y for y in rng.permutation(n) if allowed[x,y] and B[x].sum()<10 and B[y].sum()<10]
    for y in c[:max(0,10-int(B[x].sum()))]: B[x,y]=B[y,x]=1
Q,Rq,Rm=resid(B); F=(Rq**2).sum()+(Rm**2).sum(); best=F; bestB=B.copy()
tabu=np.zeros((n,n)); it=0; t0=time.time(); last=0
while time.time()-t0<tcap and F>0:
    it+=1
    d=np.where(B>0,-1.0,1.0)
    RQ=Rq@Q; q2=(Q**2).sum(1); RM=Rm@Mf.T
    dq=2*d*(2*(RQ+RQ.T)+2*Rq)+2*(np.diag(Rq)[:,None]+np.diag(Rq)[None,:])+2*(q2[:,None]+q2[None,:])+4*Q**2+4+8*d*Q
    dm=2*d*(RM+RM.T)+4
    dF=(dq+dm)[iu]; dF[~al]=np.inf
    tb=tabu[iu]>it; cand=np.where(tb & (F+dF>=best), np.inf, dF)
    k=int(np.argmin(cand + rng.random(len(cand))*1e-3))
    x,y=iu[0][k],iu[1][k]
    B[x,y]=B[y,x]=1-B[x,y]; tabu[x,y]=it+10+rng.integers(0,10)
    Q,Rq,Rm=resid(B); F=(Rq**2).sum()+(Rm**2).sum()
    if F<best: best=F; bestB=B.copy(); last=it
    if it-last>4000:  # perturb
        for _ in range(6):
            k=rng.integers(len(dF)); 
            if al[k]: x,y=iu[0][k],iu[1][k]; B[x,y]=B[y,x]=1-B[x,y]
        Q,Rq,Rm=resid(B); F=(Rq**2).sum()+(Rm**2).sum(); last=it
print(f'seed={seed} mode={mode} it={it} t={time.time()-t0:.0f}s best F={best:.0f} final F={F:.0f}')
Bi=bestB.astype(np.int64); Di=D.astype(np.int64); np.save(f'qsearch_best_s{seed}_{mode}.npy',np.stack([Bi,Di]))
if best==0:
    Q=Bi+2*Di; print('EXACT unsigned check C3',np.array_equal(Q@Q+Q+K,12*np.eye(n,dtype=np.int64)+4*np.ones((n,n),dtype=np.int64)),'C4',np.array_equal(Q@M,4*np.ones((n,7),dtype=np.int64)-2*M))
    from unsigned_all import signings
