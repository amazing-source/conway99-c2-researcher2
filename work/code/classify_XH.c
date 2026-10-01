/* classify_XH.c -- surviving sets X of non-type-2 cells under:
   (H)  Lemma H: for overlapping type-2 cells c,d, W=[7]\(c cup d) contains two DISJOINT X-cells;
   (G4) per-orbit degree realisability (see classify_X.c);
   (PI) pi on X-orbits = perfect matching on 2|X| orbit vertices over pairs feasible both ways.
   Exhaustive over 2^21 labelled X; canonical forms by degree-refined relabelling. Memory ~ 20 MB. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int ca[21], cb[21], cellid[7][7]; static unsigned cellmask[21];
static int X[21], nX, Xl[21], req[7], capv[21], orderF[21], nF, suffcap[22][7];
static int dfs(int i){ int k;
  if(i==nF){ for(k=0;k<7;k++) if(req[k]) return 0; return 1; }
  for(k=0;k<7;k++) if(req[k] > suffcap[i][k]) return 0;
  int f=orderF[i];
  for(int m=capv[f]; m>=0; m--){ int a=ca[f], b=cb[f]; if(req[a]<m||req[b]<m) continue;
    req[a]-=m; req[b]-=m; int ok=dfs(i+1); req[a]+=m; req[b]+=m; if(ok) return 1; }
  return 0; }
static int feasible(int e,int d){ int k, t=__builtin_popcount(cellmask[e]&cellmask[d]);
  for(k=0;k<7;k++) req[k]=4-2*((cellmask[e]>>k)&1)-2*((cellmask[d]>>k)&1);
  for(int c=0;c<21;c++) if(!X[c] && !(cellmask[c]&cellmask[e])){ req[ca[c]]--; req[cb[c]]--; }
  for(k=0;k<7;k++) if(req[k]<0) return 0;
  nF=0; for(int f=0;f<21;f++) if(X[f]){ int cp=2; if(f==d) cp=1; if(f==e) cp=(t==0)?1:0; if(cp>0){ capv[f]=cp; orderF[nF++]=f; } }
  for(k=0;k<7;k++) suffcap[nF][k]=0;
  for(int i=nF-1;i>=0;i--){ for(k=0;k<7;k++) suffcap[i][k]=suffcap[i+1][k]; int f=orderF[i]; suffcap[i][ca[f]]+=capv[f]; suffcap[i][cb[f]]+=capv[f]; }
  return dfs(0); }
#define MV 42
static int nv, adj[MV][MV], match_[MV], p_[MV], base_[MV], q_[MV], usedv[MV], blossom[MV];
static int lca(int a,int b){ int u2[MV]; memset(u2,0,sizeof u2);
  for(;;){ a=base_[a]; u2[a]=1; if(match_[a]==-1) break; a=p_[match_[a]]; }
  for(;;){ b=base_[b]; if(u2[b]) return b; b=p_[match_[b]]; } }
static void markpath(int v,int b,int ch){ while(base_[v]!=b){ blossom[base_[v]]=blossom[base_[match_[v]]]=1; p_[v]=ch; ch=match_[v]; v=p_[match_[v]]; } }
static int findpath(int root){ memset(usedv,0,sizeof usedv); for(int i=0;i<nv;i++){ p_[i]=-1; base_[i]=i; }
  usedv[root]=1; int qh=0,qt=0; q_[qt++]=root;
  while(qh<qt){ int v=q_[qh++];
    for(int to=0;to<nv;to++){ if(!adj[v][to]) continue; if(base_[v]==base_[to]||match_[v]==to) continue;
      if(to==root||(match_[to]!=-1&&p_[match_[to]]!=-1)){ int cb2=lca(v,to); memset(blossom,0,sizeof blossom); markpath(v,cb2,to); markpath(to,cb2,v);
        for(int i=0;i<nv;i++) if(blossom[base_[i]]){ base_[i]=cb2; if(!usedv[i]){ usedv[i]=1; q_[qt++]=i; } } }
      else if(p_[to]==-1){ p_[to]=v; if(match_[to]==-1) return to; usedv[match_[to]]=1; q_[qt++]=match_[to]; } } }
  return -1; }
static int perfect(void){ for(int i=0;i<nv;i++) match_[i]=-1; int cnt=0;
  for(int i=0;i<nv;i++) if(match_[i]==-1){ int v=findpath(i); if(v!=-1){ cnt++; while(v!=-1){ int pv=p_[v], ppv=match_[pv]; match_[v]=pv; match_[pv]=v; v=ppv; } } }
  return 2*cnt==nv; }
static int hasdisjpair(unsigned m){ for(int f=0;f<21;f++) if(m>>f&1) for(int g=f+1;g<21;g++) if((m>>g&1)&&!(cellmask[f]&cellmask[g])) return 1; return 0; }
/* canonical form: min over relabellings that sort vertices by degree (ties permuted) */
static int perms[5040][7], np=0;
static unsigned canon(unsigned m){ int deg[7]={0}; for(int f=0;f<21;f++) if(m>>f&1){ deg[ca[f]]++; deg[cb[f]]++; }
  unsigned best=0xFFFFFFFFu;
  for(int q=0;q<np;q++){ /* perms[q][v] = new label of v; require new labels sorted by degree: deg(v)<deg(w) => label(v)<label(w) */
    int ok=1; for(int v=0;v<7&&ok;v++) for(int w=0;w<7;w++) if(deg[v]<deg[w] && perms[q][v]>perms[q][w]){ ok=0; break; }
    if(!ok) continue;
    unsigned r=0; for(int f=0;f<21;f++) if(m>>f&1) r|=1u<<cellid[perms[q][ca[f]]][perms[q][cb[f]]];
    if(r<best) best=r; }
  return best; }
int main(void){
  int c=0; for(int i=0;i<7;i++) for(int j=i+1;j<7;j++){ ca[c]=i; cb[c]=j; cellid[i][j]=cellid[j][i]=c; cellmask[c]=(1u<<i)|(1u<<j); c++; }
  { int perm[7]={0,1,2,3,4,5,6}, cidx[7]={0}; memcpy(perms[np++],perm,sizeof perm); int i=0;
    while(i<7){ if(cidx[i]<i){ if(i%2==0){int t=perm[0];perm[0]=perm[i];perm[i]=t;} else {int t=perm[cidx[i]];perm[cidx[i]]=perm[i];perm[i]=t;} memcpy(perms[np++],perm,sizeof perm); cidx[i]++; i=0; } else { cidx[i]=0; i++; } } }
  static unsigned inside4[21][21];
  for(int a=0;a<21;a++) for(int b=0;b<21;b++){ unsigned m=0, used=cellmask[a]|cellmask[b]; for(int f=0;f<21;f++) if(!(cellmask[f]&used)) m|=1u<<f; inside4[a][b]=m; }
  long hpass=0, surv=0; static long hist[22];
  static unsigned cls[2048]; static long clscnt[2048]; int ncls=0;
  for(unsigned Xm=0; Xm<(1u<<21); Xm++){
    int ok=1;
    for(int a=0;a<21&&ok;a++){ if(Xm>>a&1) continue;
      for(int b=a+1;b<21;b++){ if(Xm>>b&1) continue; if(__builtin_popcount(cellmask[a]&cellmask[b])!=1) continue;
        if(!hasdisjpair(inside4[a][b]&Xm)){ ok=0; break; } } }
    if(!ok) continue; hpass++;
    nX=0; for(int f=0;f<21;f++){ X[f]=(Xm>>f)&1; if(X[f]) Xl[nX++]=f; }
    if(nX==0) continue;
    static int fe[21][21];
    for(int i=0;i<nX;i++) for(int j=0;j<nX;j++) fe[i][j] = (i==j)?0:feasible(Xl[i],Xl[j]);
    nv=2*nX; memset(adj,0,sizeof adj);
    for(int i=0;i<nX;i++) for(int j=0;j<nX;j++) if(i!=j&&fe[i][j]&&fe[j][i]) for(int s=0;s<2;s++) for(int u=0;u<2;u++) adj[2*i+s][2*j+u]=1;
    if(!perfect()) continue;
    surv++; hist[nX]++;
    unsigned cf=canon(Xm); int found=-1; for(int k=0;k<ncls;k++) if(cls[k]==cf){found=k;break;}
    if(found<0){ cls[ncls]=cf; clscnt[ncls]=1; ncls++; } else clscnt[found]++;
  }
  printf("Lemma-H pass: %ld   survivors (H+G4+PI): %ld   classes: %d\n",hpass,surv,ncls);
  printf("labelled survivors by |X|:"); for(int k=0;k<=21;k++) if(hist[k]) printf(" %d:%ld",k,hist[k]); printf("\n");
  /* print classes sorted by size */
  for(int sz=0; sz<=21; sz++) for(int k=0;k<ncls;k++) if(__builtin_popcount(cls[k])==sz){
    int deg[7]={0}; for(int f=0;f<21;f++) if(cls[k]>>f&1){deg[ca[f]]++;deg[cb[f]]++;}
    printf("|X|=%2d labelled=%6ld degs=",sz,clscnt[k]); for(int v=0;v<7;v++) printf("%d",deg[v]); printf("  Y(type-2 cells):");
    for(int f=0;f<21;f++) if(!(cls[k]>>f&1)) printf(" %d%d",ca[f]+1,cb[f]+1); printf("\n"); }
  return 0; }
