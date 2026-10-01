# verify_sym.py -- independent re-check of the symmetric exclusions.
# Classes rebuilt by signed union-find over GENERATORS only (no group closure). For groups with <= 13 free
# classes: brute force over all 3^f class values, direct test of N in S (no filters). For the others:
# re-enumerate supports and apply only the filter BM = 0 mod 2 (from NR=0), then exact NR by meet-in-middle
# and the exact quadratic test (the square-parity filter of symS.py is NOT used here).
# Memory bound: < 800 MB. Single process; < 5 min.
import numpy as np, itertools, time
from symS import coord_elem, n, R, M, H
import unsigned_sym as US
I=np.eye(n,dtype=np.int64); tgt=12*I-H
iu=[(x,y) for x in range(n) for y in range(x+1,n)]; pos={p:i for i,p in enumerate(iu)}
def uf_classes(gens):
    par=list(range(len(iu))); sg=[1]*len(iu); bad=set()
    def find(a):
        if par[a]==a: return a,1
        r,s=find(par[a]); par[a]=r; sg[a]*=s; return r,sg[a]
    for (img,s) in gens:
        for i,(x,y) in enumerate(iu):
            a,b=int(img[x]),int(img[y]); j=pos[(min(a,b),max(a,b))]; rel=int(s[x]*s[y])
            ri,si=find(i); rj,sj=find(j)
            if ri==rj:
                if si*sj!=rel: bad.add(ri)
            else: par[rj]=ri; sg[rj]=si*rel*sj
    cl={}; 
    for i in range(len(iu)):
        r,s=find(i); cl.setdefault(r,[]).append((i,s))
    badroots={find(b)[0] for b in bad}
    mats=[]
    for r,mem in cl.items():
        if r in badroots: continue
        A=np.zeros((n,n),dtype=np.int64)
        for i,s in mem: x,y=iu[i]; A[x,y]=A[y,x]=s
        mats.append(A)
    return mats,len(cl)
def inS(N): return np.all(N@R==0) and np.array_equal(N@N,N+tgt)
groups=[('PSL(2,7)',[US.c7,US.m2,(US.fano[1],US.one)]),('AGL(1,7)',[US.c7,US.m3])]+[(a,b) for a,b in US.SW.groups]
from symS import closure
for name,gens in groups:
    t0=time.time(); G=[coord_elem(p,e) for (p,e) in gens]; mats,ncl=uf_classes(G); f=len(mats); found=0
    if f<=13:
        V=np.array([(A@R).ravel() for A in mats]); cnt=0
        for c in itertools.product((0,1,-1),repeat=f):
            c=np.array(c)
            if np.any(c@V): continue
            cnt+=1; N=sum(ci*A for ci,A in zip(c,mats))
            if inS(N): found+=1
        print(f'{name}: classes={ncl} free={f} brute-force 3^{f}: NR-solutions={cnt} inS={found} t={time.time()-t0:.1f}',flush=True)
    else:
        Bm=[np.abs(A) for A in mats]; reps=[]; seen=set()
        Gc=closure(G)
        for x in range(n):
            if x in seen: continue
            reps.append(x); seen|={int(g[0][x]) for g in Gc}
        mv=np.array([[int(A[xr].sum()) for xr in reps] for A in Bm]); sups=[]
        def dfs(i,rem,ch):
            if not rem.any(): sups.append(list(ch)); return
            if i==f or np.any(mv[i:].sum(0)<rem) or time.time()-t0>60: return
            if np.all(mv[i]<=rem): ch.append(i); dfs(i+1,rem-mv[i],ch); ch.pop()
            dfs(i+1,rem,ch)
        dfs(0,np.full(len(reps),10,dtype=np.int64),[]); passBM=0; nr=0
        for sup in sups:
            B=sum(Bm[k] for k in sup)
            if np.any((B@M)%2): continue
            passBM+=1; V=[(mats[k]@R).ravel() for k in sup]; h=len(sup)//2
            def sums(idx):
                o={}
                for sg in itertools.product((1,-1),repeat=len(idx)):
                    v=np.zeros(n*7,dtype=np.int64)
                    for a,i in zip(sg,idx): v=v+a*V[i]
                    o.setdefault(v.tobytes(),[]).append(sg)
                return o
            L=sums(range(h)); Rr=sums(range(h,len(sup)))
            for kb,ls in L.items():
                ng=(-np.frombuffer(kb,dtype=np.int64)).tobytes()
                for a in ls:
                    for b in Rr.get(ng,[]):
                        nr+=1; N=sum(ci*mats[k] for ci,k in zip(list(a)+list(b),sup)); found+=inS(N)
        print(f'{name}: classes={ncl} free={f} supports={len(sups)}{"(TIMEOUT)" if time.time()-t0>60 else ""} BMeven={passBM} NRsol={nr} inS={found} t={time.time()-t0:.1f}',flush=True)
