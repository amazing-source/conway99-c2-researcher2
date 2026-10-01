# unsigned_sym.py -- for each group G: (1) independent check that #free classes = dim of the G-commutant
# (symmetric, zero diagonal) via SVD; (2) collect G-invariant unsigned supports B (row weight 10,
# B^2 = B + H mod 2 off-diag, (B^2)_xy >= |H_xy| on non-edges); (3) test the UNSIGNED joint system:
# exists perfect matching D with Q = B+2D satisfying C3, C4 (same linear system as L_N, using |N| only).
# Memory bound: < 800 MB. Single process; < 5 min.
import numpy as np, itertools, time
from symS import *
import sweep as SW   # reuses group generator lists (sweep.py main body is guarded below)
one=[1]*7; ident=list(range(7))
c7=([(t+1)%7 for t in range(7)],one); m2=([(2*t)%7 for t in range(7)],one); m3=([(3*t)%7 for t in range(7)],one)
mneg=([(-t)%7 for t in range(7)],one)
lines={frozenset({i%7,(i+1)%7,(i+3)%7}) for i in range(7)}
fano=[list(p) for p in itertools.permutations(range(7)) if {frozenset(p[t] for t in L) for L in lines}==lines]
groups=[('PSL(2,7)',[(p,one) for p in fano]),('AGL(1,7)',[c7,m3])]+SW.groups
def commutant_dim(G):
    iu=[(x,y) for x in range(n) for y in range(x+1,n)]; pos={p:i for i,p in enumerate(iu)}
    rows=[]
    for (img,sg) in G[:min(len(G),12)]:
        A=np.zeros((len(iu),len(iu)))
        for i,(x,y) in enumerate(iu):
            a,b=int(img[x]),int(img[y]); j=pos[(min(a,b),max(a,b))]; A[j,i]+=sg[x]*sg[y]
        rows.append(A-np.eye(len(iu)))
    S=np.linalg.svd(np.vstack(rows),compute_uv=False); return int((S<1e-9).sum())
def main():
    t00=time.time()
    for name,gens in groups:
        t0=time.time(); G=closure([coord_elem(p,e) for (p,e) in gens]); cls,sgn,info=classes(G); reps=row_reps(G)
        free=[k for k in range(len(info)) if not info[k]]
        # commutant check uses a generating subset: closure elements include generators' products; use all if small
        cd=commutant_dim(G if len(G)<=12 else [coord_elem(p,e) for (p,e) in gens])
        mv=np.array([[int((cls[xr]==k).sum()) for xr in reps] for k in free]).reshape(len(free),len(reps))
        sups=[]
        def dfs(i,rem,ch):
            if not rem.any(): sups.append(list(ch)); return
            if i==len(free) or np.any(mv[i:].sum(0)<rem) or len(sups)>200000 or time.time()-t0>25: return
            if np.all(mv[i]<=rem): ch.append(free[i]); dfs(i+1,rem-mv[i],ch); ch.pop()
            dfs(i+1,rem,ch)
        dfs(0,np.full(len(reps),10,dtype=np.int64),[])
        cand=0; unsigned=0
        for sup in sups:
            B=np.zeros((n,n),dtype=np.int64)
            for k in sup: B+=(cls==k)
            B2=B@B; off=(B2-B-H)%2; np.fill_diagonal(off,0)
            if off.any() or np.any((B==0)&(B2<np.abs(H))): continue
            cand+=1; sols,msg=LN_check(B)
            if sols:
                unsigned+=len(sols)
                for D in sols:
                    Q=B+2*D; ok=np.array_equal(Q@Q+Q+K,12*np.eye(n,dtype=np.int64)+4*np.ones((n,n),dtype=np.int64)) and np.array_equal(Q@M,4*np.ones((n,7),dtype=np.int64)-2*M)
                    np.save('unsigned_%s_%d.npy'%(name.replace(' ','_').replace('(','').replace(')','').replace(',','_').replace(':','_'),unsigned),np.stack([B,D]))
                    print('   UNSIGNED CANDIDATE',name,'C3&C4',ok,flush=True)
            else:
                print('   ',name,'support passes parity; unsigned joint system:',msg if sols is None else 'no matching',flush=True)
        print(f'{name}: |G|={len(G)} free={len(free)} commutant_dim={cd} supports={len(sups)} parity_ok={cand} unsigned_solutions={unsigned} t={time.time()-t0:.1f}',flush=True)
    print('total time',time.time()-t00)

if __name__=="__main__":
    main()
