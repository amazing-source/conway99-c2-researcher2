# unsigned_all.py -- G-invariant UNSIGNED supports B (all pair orbits, signs ignored) -> unsigned joint system
# (B,D) [C3,C4 via the L_N linear system, which depends on B only] -> exact signing CSP for N in S.
# Note: L_N depends only on B=|N|; so EX <=> exists unsigned (B,D) plus a signing N of B in S.
# Memory bound: < 800 MB. Single process; per-group cap 20 s; total < 5 min.
import numpy as np, itertools, time
from symS import closure, coord_elem, row_reps, LN_check, n, R, M, H, K, I, J, orbs
import unsigned_sym as US
def uclasses(G):
    cls=-np.ones((n,n),dtype=np.int64); k=0
    for x in range(n):
        for y in range(x+1,n):
            if cls[x,y]>=0: continue
            for (img,sg) in G: a,b=int(img[x]),int(img[y]); cls[a,b]=cls[b,a]=k
            k+=1
    return cls,k
def signings(B,tcap):
    t0=time.time(); nb=[list(np.nonzero(B[x])[0]) for x in range(n)]; dom=[]
    for x in range(n):
        V=R[nb[x]]; ok=[s for s in itertools.product((1,-1),repeat=len(nb[x])) if not np.any(np.array(s)@V)]
        if not ok: return 'row %d has no zero-sum signing'%x, []
        dom.append(ok)
    order=sorted(range(n),key=lambda x:len(dom[x])); N=np.zeros((n,n),dtype=np.int64); done=[]; out=[]
    tgt=12*np.eye(n,dtype=np.int64)-H
    def dfs(i):
        if time.time()-t0>tcap or len(out)>=5: return
        if i==n: out.append(N.copy()); return
        x=order[i]
        for s in dom[x]:
            if any(N[x,y]!=0 and N[x,y]!=sv for y,sv in zip(nb[x],s)): continue
            old=N[x].copy(); 
            for y,sv in zip(nb[x],s): N[x,y]=N[y,x]=sv
            good=True
            for y in done+[x]:
                if (N[x]@N[y])!=(N[x,y]+tgt[x,y]): good=False; break
            if good: done.append(x); dfs(i+1); done.pop()
            for y,sv in zip(nb[x],s):
                if y not in done: N[x,y]=N[y,x]=0
            N[x]=old; N[:,x]=old
    dfs(0); return ('complete' if time.time()-t0<=tcap else 'timeout'), out
def _main():
    c7,m2,mneg=US.c7,US.m2,US.mneg
    groups=[('PSL(2,7)',[c7,m2,(US.fano[1],US.one)]),('7:3',[c7,m2]),('AGL(1,7)',[c7,US.m3]),('D7',[c7,mneg])]+US.SW.groups
    for name,gens in groups:
        t0=time.time(); G=closure([coord_elem(p,e) for (p,e) in gens]); cls,nc=uclasses(G); reps=row_reps(G)
        mv=np.array([[int((cls[xr]==k).sum()) for xr in reps] for k in range(nc)])
        sups=[]; capped=[False]
        def dfs(i,rem,ch):
            if not rem.any(): sups.append(list(ch)); return
            if i==nc or np.any(mv[i:].sum(0)<rem): return
            if len(sups)>100000 or time.time()-t0>20: capped[0]=True; return
            if np.all(mv[i]<=rem): ch.append(i); dfs(i+1,rem-mv[i],ch); ch.pop()
            dfs(i+1,rem,ch)
        dfs(0,np.full(len(reps),10,dtype=np.int64),[])
        par=0; uns=0
        for sup in sups:
            B=np.zeros((n,n),dtype=np.int64)
            for k in sup: B+=(cls==k)
            B2=B@B; off=(B2-B-H)%2; np.fill_diagonal(off,0)
            if off.any() or np.any((B==0)&(B2<np.abs(H))) or np.any((B@M)%2): continue
            par+=1; sols,msg=LN_check(B)
            if sols:
                for D in sols:
                    uns+=1; np.save('unsignedQ_%s_%d.npy'%(name.replace(' ','').replace('(','').replace(')','').replace(',','').replace(':',''),uns),np.stack([B,D]))
                    tdist=[len({o for o in (orbs[x][0],orbs[x][1])}&{orbs[y][0],orbs[y][1]}) for x in range(n) for y in range(x+1,n) if D[x,y]]
                    st,Ns=signings(B,30); print('   UNSIGNED (B,D) FOUND',name,'D-types',sorted(tdist),'signing:',st,len(Ns),flush=True)
                    for N in Ns:
                        print('   >>> N in S with D in L_N:',np.all(N@R==0),np.array_equal(N@N,N+12*I-H)); np.save('WITNESS_N_%s.npy'%name.replace(' ',''),N); np.save('WITNESS_D_%s.npy'%name.replace(' ',''),D)
        print(f'{name}: |G|={len(G)} uclasses={nc} supports={len(sups)}{"(capped)" if capped[0] else ""} parity+BM_ok={par} unsigned_solutions={uns} t={time.time()-t0:.1f}',flush=True)

if __name__=="__main__":
    _main()
