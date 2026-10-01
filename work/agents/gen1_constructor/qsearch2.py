# qsearch2.py -- tabu search for unsigned (B,D) for general m: Q=B+2D, Q^2+Q+K=(2m-2)I+4J, QM=4J-2M.
# Validates the O(1) delta formula against recomputation first. D modes: 'cell' (same-cell matching,
# all type 2: BvLS calibration at m=11), 'any' (random matching).  Memory < 500 MB; one process; cap argv.
import numpy as np, sys, time
from common import model
m=int(sys.argv[1]); seed=int(sys.argv[2]); tcap=float(sys.argv[3]); mode=sys.argv[4]
cells,orbs,R,M,H,K=model(m); n=len(orbs); rng=np.random.default_rng(seed)
I=np.eye(n); Jm=np.ones((n,n)); Mf=M.astype(float); Kf=K.astype(float); T4=4*np.ones((n,m))-2*Mf; k2=2*m-2
D=np.zeros((n,n))
if mode=='cell':
    for x in range(0,n,2): D[x,x+1]=D[x+1,x]=1
else:
    p=rng.permutation(n)
    for a,b in zip(p[::2],p[1::2]): D[a,b]=D[b,a]=1
allowed=1-D-I; iu=np.triu_indices(n,1); al=allowed[iu]>0
def state(B):
    Q=B+2*D; Rq=Q@Q+Q+Kf-k2*I-4*Jm; Rm=Q@Mf-T4; return Q,Rq,Rm,(Rq**2).sum()+(Rm**2).sum()
def deltas(B,Q,Rq,Rm):
    d=np.where(B>0,-1.0,1.0); RQ=Rq@Q; q2=(Q**2).sum(1); RM=Rm@Mf.T; dg=np.diag(Rq)
    return (2*d*(2*(RQ+RQ.T)+2*Rq)+2*(dg[:,None]+dg[None,:])+2*(q2[:,None]+q2[None,:])+4*Q**2+4+8*d*Q
            +2*d*(RM+RM.T)+4)
B=(rng.random((n,n))<(k2-2)/n).astype(float); B=np.triu(B,1); B=(B+B.T)*allowed
Q,Rq,Rm,F=state(B); dd=deltas(B,Q,Rq,Rm)
for _ in range(5):   # formula validation
    x,y=rng.choice(n,2,replace=False)
    if not allowed[x,y]: continue
    B2=B.copy(); B2[x,y]=B2[y,x]=1-B2[x,y]; assert abs(state(B2)[3]-F-dd[x,y])<1e-6, 'delta formula wrong'
print('delta formula validated', flush=True)
best=F; bestB=B.copy(); tabu=np.zeros((n,n)); it=0; t0=time.time(); last=0
while time.time()-t0<tcap and F>0:
    it+=1; dF=deltas(B,Q,Rq,Rm)[iu]; dF[~al]=np.inf
    cand=np.where((tabu[iu]>it)&(F+dF>=best),np.inf,dF)+rng.random(len(dF))*0.5
    k=int(np.argmin(cand)); x,y=iu[0][k],iu[1][k]
    if not np.isfinite(cand[k]): continue
    B[x,y]=B[y,x]=1-B[x,y]; tabu[x,y]=it+n//3+rng.integers(0,n//3)
    Q,Rq,Rm,F=state(B)
    if F<best: best=F; bestB=B.copy(); last=it
    if it-last>20000: B=bestB.copy(); Q,Rq,Rm,F=state(B); last=it
    if it%50000==0: print(f'  it={it} F={F:.0f} best={best:.0f} t={time.time()-t0:.0f}',flush=True)
Bi=bestB.astype(np.int64); Di=D.astype(np.int64); np.save(f'qs2_m{m}_s{seed}_{mode}.npy',np.stack([Bi,Di]))
off=np.abs(state(bestB)[1]); print(f'm={m} mode={mode} seed={seed} it={it} best F={best:.0f}; #nonzero C3 residual entries={int((off>0).sum())}; C4 residual L1={np.abs(state(bestB)[2]).sum():.0f}')
if best==0:
    Q=Bi+2*Di; print('EXACT C3',np.array_equal(Q@Q+Q+K,k2*np.eye(n,dtype=np.int64)+4*np.ones((n,n),dtype=np.int64)),'C4',np.array_equal(Q@M,4*np.ones((n,m),dtype=np.int64)-2*M))
