# sweep.py -- G-invariant N in S for further coordinate groups (subgroups of W(B7)); exhaustive unless "capped".
# Memory bound: < 800 MB. Single process; per-group cap 25 s; total < 5 min.
import numpy as np, time
from symS import search, LN_check
def perm(*cycles):
    p=list(range(7))
    for c in cycles:
        for a,b in zip(c,c[1:]+c[:1]): p[a]=b
    return p
one=[1]*7
def U(*ps): return [(p,one) for p in ps]
def flip(*ts): return (list(range(7)),[(-1 if t in ts else 1) for t in range(7)])
S6=U(perm((0,1)),perm((0,1,2,3,4,5)))
A6=U(perm((0,1,2)),perm((1,2,3,4,5)))
PGL25=U(perm((0,1,2,3,4)),perm((1,2,4,3)),perm((0,5),(1,4)))
PSL25=U(perm((0,1,2,3,4)),perm((1,4),(2,3)),perm((0,5),(1,4)))
S5S2=U(perm((0,1)),perm((0,1,2,3,4)),perm((5,6)))
S4S3=U(perm((0,1)),perm((0,1,2,3)),perm((4,5)),perm((4,5,6)))
S3wrS2=U(perm((0,1)),perm((0,1,2)),perm((0,3),(1,4),(2,5)))
A7=U(perm((0,1,2)),perm((0,1,2,3,4,5,6)))
S5=U(perm((0,1)),perm((0,1,2,3,4)))
groups=[('A7',A7),('S6',S6),('A6',A6),('PGL(2,5) on 6',PGL25),('PSL(2,5) on 6',PSL25),('S5xS2',S5S2),('S4xS3',S4S3),
        ('S3wrS2',S3wrS2),('S5 (fix 2)',S5),('S6 x flip6',S6+[flip(6)]),('PGL25 x flip6',PGL25+[flip(6)]),
        ('S5xS2 x flip56',S5S2+[flip(5,6)]),('S4xS3 x flip456',S4S3+[flip(4,5,6)]),('S6 x evenflips',S6+[flip(0,1)]),
        ('PGL25 x evenflips6',PGL25+[flip(0,1)]),('S3wrS2 x flip6',S3wrS2+[flip(6)])]
if __name__=="__main__":
  tot=[]
  for name,g in groups:
      f=search(name,g,tcap=25,supcap=200000); tot+=[(name,N) for N in f]
  print("found",len(tot))
  for k,(name,N) in enumerate(tot[:10]):
      sols,msg=LN_check(N); print(name,"L_N:",msg,None if sols is None else len(sols)); np.save("sweep_found_%d.npy"%k,N)
