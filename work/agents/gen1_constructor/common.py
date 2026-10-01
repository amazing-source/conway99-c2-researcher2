# Memory bound: < 200 MB. Single process. Exact integer arithmetic (numpy int64).
import numpy as np, itertools
def model(m):
    cells=list(itertools.combinations(range(m),2))
    orbs=[]; R=[]
    for (i,j) in cells:
        for s in (1,-1):
            r=np.zeros(m,dtype=np.int64); r[i]=1; r[j]=s
            orbs.append((i,j,s)); R.append(r)
    R=np.array(R); M=np.abs(R); H=R@R.T; K=M@M.T
    return cells,orbs,R,M,H,K
def overlap(o1,o2):
    return len({o1[0],o1[1]}&{o2[0],o2[1]})
