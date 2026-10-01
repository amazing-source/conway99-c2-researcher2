"""Positive controls adapted from the supplied handoff, not new constructions."""
import numpy as np, itertools

def labels(m):
 cells=list(itertools.combinations(range(m),2))
 R=np.zeros((2*len(cells),m),dtype=np.int64)
 for c,(i,j) in enumerate(cells):
  R[2*c,i]=R[2*c+1,i]=1
  R[2*c,j]=1; R[2*c+1,j]=-1
 return cells,R

def control(m):
 if m==2: C=np.eye(2,dtype=np.int64)
 elif m==11:
  v=np.array([1,0,0,0,0],dtype=np.int64); cols=[]; red=np.array([1,1,2,1,0])
  for _ in range(m):
   cols.append(v.copy());lead=v[-1];v=(np.r_[0,v[:-1]]+lead*red)%3
  C=np.array(cols)
 else:raise ValueError
 verts=np.array(list(itertools.product(range(3),repeat=C.shape[1]))); ids={tuple(v):i for i,v in enumerate(verts)}
 A=np.zeros((len(verts),len(verts)),dtype=np.int64)
 for i,v in enumerate(verts):
  for d in np.vstack([C,-C]):A[i,ids[tuple((v+d)%3)]]=1
 cells,R=labels(m); M=abs(R)
 ii=[ids[tuple((C[i]+s*C[j])%3)] for i,j in cells for s in (1,-1)]
 jj=[ids[tuple((-verts[i])%3)] for i in ii]
 a=A[np.ix_(ii,ii)];b=A[np.ix_(ii,jj)];N=b-a;B=abs(N);D=a*b;Q=a+b
 assert np.array_equal(N@N,N+(2*m-2)*np.eye(len(N),dtype=int)-R@R.T)
 assert not (N@R).any()
 return A,N,B,D,Q,R,M
