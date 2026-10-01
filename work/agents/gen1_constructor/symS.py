# symS.py -- exact search for G-invariant N in S (signed system only), then L_N test.
# Memory bound: < 800 MB. Single process. Per-group time cap; total < 5 min.
import numpy as np, itertools, time, sys
from common import model
m=7; cells,orbs,R,M,H,K=model(m); n=42
I=np.eye(n,dtype=np.int64); J=np.ones((n,n),dtype=np.int64)
lookup={}
for x in range(n):
    lookup[tuple(R[x])]=(x,1); lookup[tuple(-R[x])]=(x,-1)
def coord_elem(p,eps):
    img=np.zeros(n,dtype=np.int64); sg=np.zeros(n,dtype=np.int64)
    for x in range(n):
        r2=[0]*m
        for t in range(m): r2[p[t]]=eps[p[t]]*R[x][t]
        y,s=lookup[tuple(r2)]; img[x]=y; sg[x]=s
    return (img,sg)
def compose(g,h): return (g[0][h[0]], h[1]*g[1][h[0]])
def closure(gens,cap=30000):
    e=(np.arange(n),np.ones(n,dtype=np.int64)); key=lambda g:g[0].tobytes()+g[1].tobytes()
    seen={key(e):e}; fr=[e]
    while fr:
        nf=[]
        for g in fr:
            for h in gens:
                k=compose(h,g); kk=key(k)
                if kk not in seen:
                    seen[kk]=k; nf.append(k)
                    if len(seen)>cap: raise Exception('group too big')
        fr=nf
    return list(seen.values())
def classes(G):
    cls=-np.ones((n,n),dtype=np.int64); sgn=np.zeros((n,n),dtype=np.int64); info=[]
    for x in range(n):
        for y in range(x+1,n):
            if cls[x,y]>=0: continue
            k=len(info); mem={}; forced=False
            for (img,sg) in G:
                a,b=int(img[x]),int(img[y]); s=int(sg[x]*sg[y]); key=(min(a,b),max(a,b))
                if key in mem:
                    if mem[key]!=s: forced=True
                else: mem[key]=s
            for (a,b),s in mem.items(): cls[a,b]=cls[b,a]=k; sgn[a,b]=sgn[b,a]=s
            info.append(forced)
    return cls,sgn,info
def row_reps(G):
    seen=set(); reps=[]
    for x in range(n):
        if x in seen: continue
        reps.append(x)
        for (img,sg) in G: seen.add(int(img[x]))
    return reps
def LN_check(N):
    B=np.abs(N); BM=B@M
    if np.any(BM%2): return None,'BM odd'
    T=2*np.ones((n,m),dtype=np.int64)-M-BM//2
    E2=8*I+4*J-K-B@B-B
    if np.any(E2%2): return None,'E odd'
    E=E2//2; cand=[]
    for x in range(n):
        t=T[x]
        if not(np.all((t==0)|(t==1)) and t.sum()==2): return None,'T row %d not a cell'%x
        cand.append([y for y in range(n) if y!=x and np.array_equal(M[y],t) and B[x,y]==0])
    sols=[]
    def bt(D,used):
        free=[x for x in range(n) if x not in used]
        if not free:
            if np.array_equal(B@D+D@B+D,E) and np.array_equal(D@M,T): sols.append(D.copy())
            return
        x=free[0]
        for y in cand[x]:
            if y in used or x not in cand[y]: continue
            D[x,y]=D[y,x]=1; used|={x,y}; bt(D,used); used-={x,y}; D[x,y]=D[y,x]=0
    bt(np.zeros((n,n),dtype=np.int64),set())
    return sols,'matchings tried'
def search(name,gens,tcap=40,supcap=300000):
    t0=time.time()
    try: G=closure([coord_elem(p,e) for (p,e) in gens])
    except Exception as e: print(name,'skip',e); return []
    cls,sgn,info=classes(G); reps=row_reps(G)
    free=[k for k in range(len(info)) if not info[k]]
    mv=np.array([[int((cls[xr]==k).sum()) for xr in reps] for k in free]).reshape(len(free),len(reps))
    order=sorted(range(len(free)),key=lambda i:-mv[i].max())
    mvo=mv[order]; suf=np.zeros((len(free)+1,len(reps)),dtype=np.int64)
    for i in range(len(free)-1,-1,-1): suf[i]=suf[i+1]+mvo[i]
    sups=[]; stop=[False]
    def dfs(i,rem,chosen):
        if stop[0]: return
        if not rem.any(): sups.append([free[order[j]] for j in chosen]); 
        if not rem.any():
            if len(sups)>=supcap or time.time()-t0>tcap: stop[0]=True
            return
        if i==len(free) or np.any(suf[i]<rem): return
        if np.all(mvo[i]<=rem): chosen.append(i); dfs(i+1,rem-mvo[i],chosen); chosen.pop()
        dfs(i+1,rem,chosen)
    dfs(0,np.full(len(reps),10,dtype=np.int64),[])
    Amat={k:((cls==k)*sgn).astype(np.int64) for k in free}
    n2=0; nNR=0; found=[]
    for sup in sups:
        if time.time()-t0>tcap: stop[0]=True; break
        B=sum(np.abs(Amat[k]) for k in sup); B2=B@B
        off=(B2-B-H)%2; np.fill_diagonal(off,0)
        if off.any(): continue
        if np.any((B==0)&(B2<np.abs(H))): continue
        n2+=1
        V=[ (Amat[k]@R).ravel() for k in sup]; s=len(sup); h=s//2
        def sums(idx):
            out={}
            for signs in itertools.product((1,-1),repeat=len(idx)):
                v=sum((sg*V[i] for sg,i in zip(signs,idx)),np.zeros(n*m,dtype=np.int64))
                out.setdefault(v.tobytes(),[]).append(signs)
            return out
        L=sums(list(range(h))); Rr=sums(list(range(h,s)))
        for kb,ls in L.items():
            neg=(-np.frombuffer(kb,dtype=np.int64)).tobytes()
            if neg in Rr:
                for a in ls:
                    for b in Rr[neg]:
                        nNR+=1; c=list(a)+list(b)
                        N=sum(ci*Amat[k] for ci,k in zip(c,sup))
                        if np.array_equal(N@N,N+12*I-H): found.append(N)
    print(f'{name}: |G|={len(G)} rowtypes={len(reps)} classes={len(info)} free={len(free)} '
          f'supports={len(sups)}{"(capped)" if stop[0] else ""} mod2ok={n2} NRsol={nNR} inS={len(found)} t={time.time()-t0:.1f}s',flush=True)
    return found
if __name__=='__main__':
    ident=list(range(7)); one=[1]*7
    c7=([ (t+1)%7 for t in range(7)],one); m2=([(2*t)%7 for t in range(7)],one); m3=([(3*t)%7 for t in range(7)],one)
    mneg=([(-t)%7 for t in range(7)],one)
    lines={frozenset({i%7,(i+1)%7,(i+3)%7}) for i in range(7)}
    fano=[list(p) for p in itertools.permutations(range(7)) if {frozenset(p[t] for t in L) for L in lines}==lines]
    # Fano point i <-> alpha^i in F_8, alpha^3=alpha+1, as bit vectors
    vec=[];v=1
    for i in range(7): vec.append(v); v<<=1; v^= (0b1011 if v&8 else 0)
    fsig=[[(-1)**bin(a&vec[t]).count('1') for t in range(7)] for a in (1,2,4)]
    flip0=(ident,[-1]+[1]*6)
    groups=[('PSL(2,7)',[(p,one) for p in fano[:]]), ('2^3:PSL(2,7)',[(p,one) for p in fano]+[(ident,s) for s in fsig]),
            ('7:3',[c7,m2]),('AGL(1,7)',[c7,m3]),('D7',[c7,mneg]),('2^3:7:3',[c7,m2]+[(ident,s) for s in fsig]),
            ('2^3:7',[c7]+[(ident,s) for s in fsig]),('2^7:7',[c7,flip0]),('2^7:7:3',[c7,m2,flip0])]
    allfound=[]
    for name,gens in groups:
        f=search(name,gens); allfound+= [(name,N) for N in f]
    print('total N in S found:',len(allfound))
    for k,(name,N) in enumerate(allfound[:20]):
        sols,msg=LN_check(N); print(name,k,'L_N:',msg, 'solutions' if sols is None else len(sols))
        np.save(f'symS_found_{k}.npy',N)
