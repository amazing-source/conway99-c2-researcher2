# rrr.py -- RRR (Elser difference-map) search for N in S_m: symmetric {0,+-1} zero-diag N, NR=0,
# N^2 = N + (2m-2)I - RR^T.  Spectral projection onto {XR=0, spec on R^perp = {lam_hi^a, lam_lo^b}}.
# Memory bound: < 300 MB. Single process. Wall time cap from argv (<= 280 s).
import numpy as np, sys, time
from common import model
m=int(sys.argv[1]); tcap=float(sys.argv[2]); beta=float(sys.argv[3]); seed=int(sys.argv[4])
cells,orbs,R,M,H,K=model(m); n=len(orbs); dim=n-m
s8=np.sqrt(8*m-7); lh=(1+s8)/2; ll=(1-s8)/2; a=int(round(-dim*ll/(lh-ll)))
Uf,_,_=np.linalg.svd(R.astype(float),full_matrices=True); U=Uf[:,m:]
d=np.full(dim,ll); d[dim-a:]=lh
Iint=np.eye(n,dtype=np.int64); tgt=(2*m-2)*Iint-H
def PB(X):
    Z=U.T@X@U; w,V=np.linalg.eigh((Z+Z.T)/2); return U@((V*d)@V.T)@U.T
def PA(X):
    Y=np.round(np.clip(X,-1,1)); np.fill_diagonal(Y,0); return Y
rng=np.random.default_rng(seed); x=rng.normal(size=(n,n))*0.5; x=(x+x.T)/2
t0=time.time(); it=0; best=1e9
while time.time()-t0<tcap:
    pb=PB(x); pa=PA(2*pb-x); x=x+beta*(pa-pb); it+=1
    err=np.linalg.norm(pa-pb); best=min(best,err)
    if it%5==0:
        N=PA(pb).astype(np.int64)
        if np.all(N@R==0) and np.array_equal(N@N,N+tgt):
            print('FOUND m=%d it=%d t=%.1f'%(m,it,time.time()-t0),flush=True)
            np.save('rrr_found_m%d_seed%d.npy'%(m,seed),N); break
    if it%10000==0: print(' m=%d it=%d best=%.3f err=%.3f t=%.0f'%(m,it,best,err,time.time()-t0),flush=True)
print('end m=%d it=%d best=%.3f'%(m,it,best))
