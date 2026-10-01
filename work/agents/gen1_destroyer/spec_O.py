# gen1_destroyer: spectrum of the Hodge Laplacian Delta_1 of the triangle+square complex for the two known
# srg(1+2m^2,2m,1,2) with one-fixed-point involution (m=2 Paley(9), m=11 BvLS). Single process, < 400 MB, < 2 min.
import numpy as np, collections
from calib_m11 import load, check_kernel, exterior
def lap(A, m):
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
    d2=np.zeros((len(edges),len(cells)),np.int8)
    for t,c in enumerate(cells):
        for i in range(len(c)):
            e,s=se(c[i],c[(i+1)%len(c)]); d2[e,t]=s
    d1=np.zeros((V,len(edges)),np.int8)
    for t,(u,w) in enumerate(edges): d1[u,t]=-1; d1[w,t]=1
    D1=d1.T.astype(np.int32)@d1.astype(np.int32); U=d2.astype(np.int32)@d2.T.astype(np.int32)
    return D1, U
def spec(Mx):
    ev=np.linalg.eigvalsh(Mx.astype(float)); c=collections.Counter(np.round(ev,6)); return sorted(c.items())
# m=2 Paley(9) in the CP model: X = 4-cycle on roots of D2
m=2; R=np.array([[1,1],[1,-1]]); N=np.array([[0,0],[0,0]]); D=np.array([[0,1],[1,0]])
Q=np.abs(N)+2*D; ok,X,roots,Inc,L,A=exterior(m,R,Q,N); print("m=2 srg ok",ok)
D1,U=lap(A,m); print("m=2 up-Laplacian on edges:",spec(U)); print("m=2 Delta_1:",spec(D1+U))
m=11; N,D=load(m); ok0,R,Q,H,K,M=check_kernel(m,N,D); ok,X,roots,Inc,L,A=exterior(m,R,Q,N)
D1,U=lap(A,m); print("m=11 Delta_1:",spec(D1+U)); print("m=11 up-Laplacian:",spec(U))
