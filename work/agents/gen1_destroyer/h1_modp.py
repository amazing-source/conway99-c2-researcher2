# gen1_destroyer: dim H_1(Xhat; F_p) of the triangle+square complex for m=2 (Paley 9) and m=11 (BvLS).
# rank_p(d2) via a random F_p projection (d2 G, G uniform, 40 spare columns; equality w.h.p., lower bound always).
# Single process, memory < 900 MB, runtime target < 4 min.
import numpy as np, sys, time
from calib_m11 import load, check_kernel, exterior
def complex_mats(A):
    V=len(A); edges=[(i,j) for i in range(V) for j in range(i+1,V) if A[i,j]]; eid={e:t for t,e in enumerate(edges)}
    def se(u,w): return (eid[(u,w)],1) if u<w else (eid[(w,u)],-1)
    cells=[]; seen=set()
    for (u,w) in edges:
        for z in np.nonzero(A[u]&A[w])[0]:
            if z>w: cells.append([u,w,z])
    for u in range(V):
        for w in range(u+1,V):
            if not A[u,w]:
                c=np.nonzero(A[u]&A[w])[0]; key=frozenset([u,w,c[0],c[1]])
                if key not in seen: seen.add(key); cells.append([u,c[0],w,c[1]])
    d2=np.zeros((len(edges),len(cells)),np.float32)
    for t,c in enumerate(cells):
        for i in range(len(c)):
            e,s=se(c[i],c[(i+1)%len(c)]); d2[e,t]=s
    return V,len(edges),d2
def rank_mod(Mt,p):
    A=(np.asarray(Mt,dtype=np.int64)%p); r=0; R,C=A.shape
    for c in range(C):
        if r==R: break
        nz=np.nonzero(A[r:,c])[0]
        if len(nz)==0: continue
        piv=r+nz[0]
        if piv!=r: A[[r,piv]]=A[[piv,r]]
        inv=pow(int(A[r,c]),p-2,p); A[r,c:]=(A[r,c:]*inv)%p
        rows=r+1+np.nonzero(A[r+1:,c])[0]
        if len(rows): A[rows,c:]=(A[rows,c:]-np.outer(A[rows,c],A[r,c:]))%p
        r+=1
    return r
rng=np.random.default_rng(1)
for m in (2,11):
    if m==2:
        R=np.array([[1,1],[1,-1]]); N=np.zeros((2,2),int); D=np.array([[0,1],[1,0]])
    else:
        N,D=load(11); ok,R,Q,H,K,M=check_kernel(11,N,D)
    Q=np.abs(N)+2*D; ok,X,roots,Inc,L,A=exterior(m,R,Q,N)
    V,E,d2=complex_mats(A); z1=E-(V-1)
    for p in ((2,3) if m==11 else (2,3,5,7)):
        t=time.time()
        if d2.shape[1]<=z1+40: Mt=d2
        else:
            G=rng.integers(0,p,size=(d2.shape[1],z1+40)).astype(np.float32)
            Mt=np.rint(d2.astype(np.float64)@G.astype(np.float64))
        rk=rank_mod(Mt,p)
        print(f"m={m} p={p}: dim Z1={z1}, rank_p(d2)>={rk}, dim H1(F_p)<={z1-rk}  ({time.time()-t:.1f}s)",flush=True)
