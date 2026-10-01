/* classify_X.c -- which sets X of NON-type-2 cells survive necessary conditions (G4),(G5)?
   Cells = edges of K7 (21). Y = complement of X = type-2 cells (pi pairs the two orbits of the cell).
   (G5) Lemma F: for overlapping c,d in Y, X has a cell inside [7] minus (c cup d).
   (G4) degree realisability for an X-orbit z in cell e whose pi-partner lies in X-cell d != e:
        f_z(k) = 4 - 2[k in e] - 2[k in d];  Y-cells disjoint from e contribute exactly 1 each,
        Y-cells meeting e contribute 0; remaining degrees must be realised by X-cells f with
        multiplicity m_f in {0,1,2}, m_d <= 1 (z not adjacent to pi z), m_e <= 1 and m_e = 0 unless
        |e cap d| = 0 (cell-mate adjacency forces type 0).
   pi on X-orbits <-> loopless 2-regular multigraph on X-cells using pairs (e,d) feasible both ways;
   tested as a perfect matching (Edmonds blossom) on the 2|X| orbit-vertices.
   Exhaustive over all 2^21 subsets X. Memory < 10 MB. Single process. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int ca[21], cb[21], cellid[7][7];
static unsigned cellmask[21]; /* bit per vertex */
static int X[21], nX, Xl[21];
static int req[7];
static int capv[21];
static int orderF[21], nF;
static int suffcap[22][7];
static int dfs(int i){
  int k;
  if(i==nF){ for(k=0;k<7;k++) if(req[k]) return 0; return 1; }
  for(k=0;k<7;k++) if(req[k] > suffcap[i][k]) return 0;
  int f = orderF[i];
  for(int m = capv[f]; m >= 0; m--){
    int a=ca[f], b=cb[f];
    if(req[a] < m || req[b] < m) continue;
    req[a]-=m; req[b]-=m;
    int ok = dfs(i+1);
    req[a]+=m; req[b]+=m;
    if(ok) return 1;
  }
  return 0;
}
static int feasible(int e, int d){ /* orbit in X-cell e with partner in X-cell d */
  int k, t = __builtin_popcount(cellmask[e] & cellmask[d]);
  for(k=0;k<7;k++){ req[k] = 4 - 2*((cellmask[e]>>k)&1) - 2*((cellmask[d]>>k)&1); }
  for(int c=0;c<21;c++) if(!X[c] && !(cellmask[c] & cellmask[e])){ req[ca[c]]--; req[cb[c]]--; }
  for(k=0;k<7;k++) if(req[k] < 0) return 0;
  nF = 0;
  for(int f=0; f<21; f++) if(X[f]){
    int cp = 2; if(f==d) cp = 1; if(f==e) cp = (t==0) ? 1 : 0;
    if(cp>0){ capv[f]=cp; orderF[nF++]=f; } }
  for(k=0;k<7;k++) suffcap[nF][k]=0;
  for(int i=nF-1;i>=0;i--){ for(k=0;k<7;k++) suffcap[i][k]=suffcap[i+1][k]; int f=orderF[i]; suffcap[i][ca[f]]+=capv[f]; suffcap[i][cb[f]]+=capv[f]; }
  return dfs(0);
}
/* Edmonds blossom for general matching on up to 42 vertices */
#define MV 42
static int nv, adj[MV][MV], match_[MV], p_[MV], base_[MV], q_[MV], usedv[MV], blossom[MV];
static int lca(int a,int b){ int used2[MV]; memset(used2,0,sizeof used2);
  for(;;){ a=base_[a]; used2[a]=1; if(match_[a]==-1) break; a=p_[match_[a]]; }
  for(;;){ b=base_[b]; if(used2[b]) return b; b=p_[match_[b]]; } }
static void markpath(int v,int b,int ch){ while(base_[v]!=b){ blossom[base_[v]]=blossom[base_[match_[v]]]=1; p_[v]=ch; ch=match_[v]; v=p_[match_[v]]; } }
static int findpath(int root){
  memset(usedv,0,sizeof usedv); for(int i=0;i<nv;i++){ p_[i]=-1; base_[i]=i; }
  usedv[root]=1; int qh=0, qt=0; q_[qt++]=root;
  while(qh<qt){ int v=q_[qh++];
    for(int to=0; to<nv; to++){ if(!adj[v][to]) continue;
      if(base_[v]==base_[to] || match_[v]==to) continue;
      if(to==root || (match_[to]!=-1 && p_[match_[to]]!=-1)){
        int cb2=lca(v,to); memset(blossom,0,sizeof blossom); markpath(v,cb2,to); markpath(to,cb2,v);
        for(int i=0;i<nv;i++) if(blossom[base_[i]]){ base_[i]=cb2; if(!usedv[i]){ usedv[i]=1; q_[qt++]=i; } }
      } else if(p_[to]==-1){ p_[to]=v; if(match_[to]==-1) return to; usedv[match_[to]]=1; q_[qt++]=match_[to]; } } }
  return -1; }
static int perfect(void){ for(int i=0;i<nv;i++) match_[i]=-1; int cnt=0;
  for(int i=0;i<nv;i++) if(match_[i]==-1){ int v=findpath(i); if(v!=-1){ cnt++; while(v!=-1){ int pv=p_[v], ppv=match_[pv]; match_[v]=pv; match_[pv]=v; v=ppv; } } }
  return 2*cnt==nv; }
int main(void){
  int c=0; for(int i=0;i<7;i++) for(int j=i+1;j<7;j++){ ca[c]=i; cb[c]=j; cellid[i][j]=cellid[j][i]=c; cellmask[c]=(1u<<i)|(1u<<j); c++; }
  /* precompute for G5: list of overlapping pairs and the mask of cells inside the complement 4-set */
  static unsigned inside4[21][21];
  for(int a=0;a<21;a++) for(int b=0;b<21;b++){ unsigned m=0; unsigned used=cellmask[a]|cellmask[b];
    for(int f=0;f<21;f++) if(!(cellmask[f]&used)) m|=1u<<f; inside4[a][b]=m; }
  long survivors=0; long g5pass=0;
  static unsigned surv[1<<16]; int ns=0;
  for(unsigned Xm=0; Xm < (1u<<21); Xm++){
    /* G5 */
    int ok=1;
    for(int a=0;a<21 && ok;a++){ if(Xm>>a&1) continue;
      for(int b=a+1;b<21;b++){ if(Xm>>b&1) continue;
        if(__builtin_popcount(cellmask[a]&cellmask[b])!=1) continue;
        if(!(inside4[a][b] & Xm)){ ok=0; break; } } }
    if(!ok) continue;
    g5pass++;
    nX=0; for(int f=0;f<21;f++){ X[f]=(Xm>>f)&1; if(X[f]) Xl[nX++]=f; }
    if(nX==0) continue;
    /* feasibility matrix */
    static int fe[21][21];
    for(int i=0;i<nX;i++) for(int j=0;j<nX;j++){ if(i==j){ fe[i][j]=0; continue; } fe[i][j]=feasible(Xl[i],Xl[j]); }
    nv=2*nX; memset(adj,0,sizeof adj);
    for(int i=0;i<nX;i++) for(int j=0;j<nX;j++) if(i!=j && fe[i][j] && fe[j][i]){
      for(int s=0;s<2;s++) for(int u=0;u<2;u++){ adj[2*i+s][2*j+u]=1; } }
    if(!perfect()) continue;
    survivors++;
    if(ns < (1<<16)) surv[ns++]=Xm;
  }
  printf("G5-pass: %ld   survivors (G5+G4+pi): %ld\n", g5pass, survivors);
  /* isomorphism classes of survivors via canonical form over S7 */
  int perm[7]={0,1,2,3,4,5,6};
  static int perms[5040][7]; int np=0;
  /* generate permutations (Heap) */
  int cidx[7]={0}; memcpy(perms[np++],perm,sizeof perm); int i=0;
  while(i<7){ if(cidx[i]<i){ if(i%2==0){int tmp=perm[0];perm[0]=perm[i];perm[i]=tmp;} else {int tmp=perm[cidx[i]];perm[cidx[i]]=perm[i];perm[i]=tmp;} memcpy(perms[np++],perm,sizeof perm); cidx[i]++; i=0; } else { cidx[i]=0; i++; } }
  static unsigned canon[1<<16]; int ncls=0; static unsigned cls[4096]; static int clscount[4096];
  for(int s=0;s<ns;s++){ unsigned best=0xFFFFFFFF;
    for(int q=0;q<np;q++){ unsigned m=0; for(int f=0;f<21;f++) if(surv[s]>>f&1){ int a=perms[q][ca[f]], b=perms[q][cb[f]]; m|=1u<<cellid[a][b]; } if(m<best) best=m; }
    canon[s]=best; int found=-1; for(int k=0;k<ncls;k++) if(cls[k]==best){found=k;break;}
    if(found<0){ cls[ncls]=best; clscount[ncls]=1; ncls++; } else clscount[found]++; }
  printf("isomorphism classes of surviving X: %d\n", ncls);
  for(int k=0;k<ncls;k++){ int ne=__builtin_popcount(cls[k]); printf("class %d: |X|=%d  (#labelled=%d)  edges:",k,ne,clscount[k]);
    for(int f=0;f<21;f++) if(cls[k]>>f&1) printf(" %d%d",ca[f]+1,cb[f]+1); printf("\n"); }
  return 0;
}
