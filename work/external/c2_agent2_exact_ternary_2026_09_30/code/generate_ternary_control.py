"""A finite-field control, not a Conway graph: exact arithmetic over F_3."""
import numpy as np, sys, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
from controls import labels
P=3

def rref(a):
 a=np.array(a,dtype=np.int64)%3; piv=[];i=0
 for j in range(a.shape[1]):
  rows=np.flatnonzero(a[i:,j])
  if not len(rows):continue
  k=i+rows[0];a[[i,k]]=a[[k,i]];a[i]=(a[i]*int(a[i,j]))%3
  for k in range(len(a)):
   if k!=i and a[k,j]:a[k]=(a[k]-a[k,j]*a[i])%3
  piv.append(j);i+=1
  if i==len(a):break
 return a,piv

def nullspace(a):
 rr,piv=rref(a);free=[j for j in range(a.shape[1]) if j not in piv];out=[]
 for j in free:
  x=np.zeros(a.shape[1],dtype=np.int64);x[j]=1
  for i,k in enumerate(piv):x[k]=-rr[i,j]
  out.append(x%3)
 return np.array(out,dtype=np.int64).T

def solve(a,b):
 aug,piv=rref(np.column_stack([a,b])); n=a.shape[1]
 if n in piv:return None
 x=np.zeros(n,dtype=np.int64)
 for i,j in enumerate(piv):x[j]=aug[i,-1]
 return x%3

rng=np.random.default_rng(20260930)
cells,R=labels(7); R3=R%3;O=R[1::2];PC=(np.eye(21,dtype=np.int64)-O@O.T)%3
assert np.array_equal(PC@PC%3,PC) and not(PC@O%3).any()
base=nullspace(O.T%3)
assert base.shape==(21,15)
remaining=base.copy(); us=[];vs=[]
for step in range(6):
 for it in range(10000):
  x=remaining@rng.integers(0,3,size=remaining.shape[1])%3
  if x.any() and x@x%3==0:break
 else:raise RuntimeError('no isotropic vector')
 dots=x@remaining%3; j=np.flatnonzero(dots)[0];y=remaining[:,j]*int(dots[j])%3
 y=(y-2*int(y@y%3)*x)%3
 assert x@y%3==1 and y@y%3==0
 us.append(x);vs.append(y)
 remaining=remaining@nullspace(np.stack([x@remaining,y@remaining])%3)%3
assert remaining.shape[1]==3
for it in range(10000):
 t=remaining@rng.integers(0,3,size=3)%3
 if t@t%3==1:break
U=np.array(us).T
assert not(U.T@U%3).any() and not(U.T@t%3).any()
A=np.zeros((21,42),dtype=np.int64)
for e,(i,j) in enumerate(cells):A[e,6*i:6*i+6]=U[e];A[e,6*j:6*j+6]=-U[e]
co=solve(A%3,np.ones(21,dtype=np.int64))
if co is None:raise RuntimeError('inconsistent chosen U')
Z=co.reshape(7,6)@U.T%3
T=(Z+t)%3
F0=np.zeros((42,21),dtype=np.int64);F0[1::2]=PC
F=(F0+R@T)%3
proj=F@F.T%3
assert np.array_equal(proj,proj.T)
assert np.array_equal(proj@proj%3,proj)
assert not(proj@R%3).any()
assert (np.diag(proj)==1).all()
assert len(rref(proj)[1])==15
H=R@R.T
N3=(proj+H)%3
N=np.where(N3==2,-1,N3)
B=abs(N);M=abs(R)
assert not (N@R%3).any()
assert not ((N@N-N-12*np.eye(42,dtype=np.int64)+H)%3).any()
report={'meaning':'Finite-field projector control only. NOT a C2 graph or a full signed N.',
 'seed':20260930,'symmetric_idempotent':True,'rank':15,'all_diagonal_entries_one':True,'annihilates_R_mod3':True,
 'centered_lift_diagonal_zero':bool(not np.diag(N).any()),
 'centered_lift_satisfies_signed_equations_mod3':True,
 'row_weights':dict(zip(*[list(map(int,x)) for x in np.unique(B.sum(axis=1),return_counts=True)])),
 'integer_NR_zero':bool(not(N@R).any()),
 'integer_quadratic_residual_zero':bool(not (N@N-N-12*np.eye(42,dtype=np.int64)+H).any()),
 'equilibrium_linear_system_rank':len(rref(A%3)[1])}
json.dump({'report':report,'P':proj.tolist(),'N_centered':N.tolist()},open(ROOT/'data/ternary_projector_control.json','w'),indent=2)
print(json.dumps(report,indent=2))
