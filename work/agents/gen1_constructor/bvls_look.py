# Memory bound: < 200 MB. Inspect BvLS m=11 calibration data in normalized form.
import numpy as np
from common import *
N=np.load('../../data/bvls_m11_N.npy').astype(np.int64); D=np.load('../../data/bvls_m11_D.npy').astype(np.int64)
m=11; cells,orbs,R,M,H,K=model(m); n=len(orbs); I=np.eye(n,dtype=np.int64); J=np.ones((n,n),dtype=np.int64)
B=np.abs(N); Q=B+2*D
print('shape',N.shape, 'NR=0',np.all(N@R==0),'N2',np.all(N@N==N+(2*m-2)*I-H))
print('C3',np.all(Q@Q+Q+K==(2*m-2)*I+4*J),'C4',np.all(Q@M==4*np.ones((n,m),dtype=np.int64)-2*M))
from collections import Counter
dt=Counter(); st=Counter()
for x in range(n):
    for y in range(x+1,n):
        ov=overlap(orbs[x],orbs[y]); 
        s={(0,0):'n',(2,0):'d',(1,-1):'m',(1,1):'p'}[(Q[x,y],N[x,y])]
        st[(ov,s)]+=1
        if D[x,y]: dt[ov]+=1
print('D types',dict(dt)); print('states by overlap',sorted(st.items()))
