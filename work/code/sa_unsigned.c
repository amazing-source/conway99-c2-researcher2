/* sa_unsigned.c -- simulated annealing for the UNSIGNED sigma-quotient system (pi, B).
   Unknowns: pi = fixed-point-free involution on the 42 orbits; B = 10-regular simple graph, B cap pi = 0.
   Constraints (exact integers):
     r1[x][k] = f_x(k) - (4 - 2[k in supp x] - 2[k in supp pi x])                       (R2')
     r2[x][y] = (B^2)_xy + B_xy + s(x,y) + 2(B_{x,pi y} + B_{pi x,y} + [y = pi x]) - 4, x<y  ((E+)+(E-))
   Energy = sum r1^2 + sum_{x<y} r2^2.  A zero-energy state is written to the output file.
   Usage: sa_unsigned seed steps T0 T1 maxrestarts outfile [fixpi(0/1)] [pifile]
   Memory: < 1 MB.  Single process. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#define NN 42
typedef long long ll;
static int Ms[NN][7], Sov[NN][NN], pi_[NN];
static int Bm[NN][NN], B2[NN][NN], BMc[NN][7];
static int r1[NN][7], r2[NN][NN];
static ll E;
static unsigned long long rs;
static inline unsigned long long rnd64(void){ rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline int rndint(int n){ return (int)(rnd64() % (unsigned long long)n); }
static inline double rnd01(void){ return (rnd64() >> 11) * (1.0/9007199254740992.0); }
static inline int tgt1(int x,int k){ return 4 - 2*Ms[x][k] - 2*Ms[pi_[x]][k]; }
static inline int c2(int x,int y){ return B2[x][y] + Bm[x][y] + Sov[x][y] + 2*(Bm[x][pi_[y]] + Bm[pi_[x]][y] + (y==pi_[x])) - 4; }
static int mark[NN];
/* energy contribution of all terms touching vertex set L (pairs counted once) */
static ll part(const int *L, int nl){
  ll s = 0; int i,k,w;
  for(i=0;i<nl;i++) mark[L[i]] = 1;
  for(i=0;i<nl;i++){ int x=L[i];
    for(k=0;k<7;k++) s += (ll)r1[x][k]*r1[x][k];
    for(w=0;w<NN;w++){ if(w==x) continue; if(mark[w] && w<x) continue; s += (ll)r2[x][w]*r2[x][w]; } }
  for(i=0;i<nl;i++) mark[L[i]] = 0;
  return s;
}
static void recomp(const int *L, int nl){
  int i,k,w;
  for(i=0;i<nl;i++){ int x=L[i];
    for(k=0;k<7;k++) r1[x][k] = BMc[x][k]-tgt1(x,k);
    for(w=0;w<NN;w++){ if(w==x) continue; r2[x][w] = r2[w][x] = c2(x,w); } }
}
static void rawtoggle(int u,int v,int d){
  int k,w;
  Bm[u][v]+=d; Bm[v][u]+=d;
  for(k=0;k<7;k++){ BMc[u][k]+=d*Ms[v][k]; BMc[v][k]+=d*Ms[u][k]; }
  for(w=0;w<NN;w++){ if(w==u||w==v) continue;
    if(Bm[v][w]){ B2[u][w]+=d; B2[w][u]+=d; }
    if(Bm[u][w]){ B2[v][w]+=d; B2[w][v]+=d; } }
  B2[u][u]+=d; B2[v][v]+=d;
}
static void toggle(int u,int v,int d){ int L[2]={u,v}; E -= part(L,2); rawtoggle(u,v,d); recomp(L,2); E += part(L,2); }
static void setpi(int a,int b,int c,int dd){ /* re-pair: pi(a)=b, pi(c)=dd */
  int L[4]={a,b,c,dd}; E -= part(L,4); pi_[a]=b; pi_[b]=a; pi_[c]=dd; pi_[dd]=c; recomp(L,4); E += part(L,4); }
static ll fullE(void){ ll s=0; int x,y,k;
  for(x=0;x<NN;x++){ for(k=0;k<7;k++){ int r=BMc[x][k]-tgt1(x,k); s+=(ll)r*r; } for(y=x+1;y<NN;y++){ int r=c2(x,y); s+=(ll)r*r; } }
  return s; }
static void rebuild(void){ int x,y,z,k; memset(B2,0,sizeof B2); memset(BMc,0,sizeof BMc);
  for(x=0;x<NN;x++) for(y=0;y<NN;y++){ int s=0; for(z=0;z<NN;z++) s+=Bm[x][z]*Bm[z][y]; B2[x][y]=s; }
  for(x=0;x<NN;x++) for(k=0;k<7;k++){ int s=0; for(z=0;z<NN;z++) s+=Bm[x][z]*Ms[z][k]; BMc[x][k]=s; }
  for(x=0;x<NN;x++){ for(k=0;k<7;k++) r1[x][k]=BMc[x][k]-tgt1(x,k); for(y=0;y<NN;y++) if(y!=x) r2[x][y]=c2(x,y); }
  E = fullE(); }
int main(int argc,char**argv){
  if(argc<7){ fprintf(stderr,"usage\n"); return 1; }
  rs = 0x9E3779B97F4A7C15ULL ^ (unsigned long long)atoll(argv[1])*2654435761ULL; if(!rs) rs=1;
  ll steps = atoll(argv[2]); double T0=atof(argv[3]), T1=atof(argv[4]); int maxr=atoi(argv[5]);
  const char* out=argv[6]; int fixpi = argc>7 ? atoi(argv[7]) : 0;
  int x,y,i,j,k,c=0;
  int ca[21],cb[21];
  for(i=0;i<7;i++) for(j=i+1;j<7;j++){ ca[c]=i; cb[c]=j; c++; }
  for(x=0;x<NN;x++){ memset(Ms[x],0,sizeof Ms[x]); Ms[x][ca[x/2]]=1; Ms[x][cb[x/2]]=1; }
  for(x=0;x<NN;x++) for(y=0;y<NN;y++){ int s=0; for(k=0;k<7;k++) s+=Ms[x][k]*Ms[y][k]; Sov[x][y]=s; }
  for(i=0;i<8;i++) rnd64();
  clock_t t0=clock();
  for(int rr=0; rr<maxr; rr++){
    /* init: circulant(1..5) graph; pi = x <-> x+21 (or read from file) */
    memset(Bm,0,sizeof Bm);
    for(x=0;x<NN;x++) for(int d=1; d<=5; d++){ y=(x+d)%NN; Bm[x][y]=Bm[y][x]=1; }
    for(x=0;x<NN;x++) pi_[x]=(x+21)%NN;
    if(fixpi && argc>8){ FILE*f=fopen(argv[8],"r"); for(x=0;x<NN;x++) if(fscanf(f,"%d",&pi_[x])!=1) return 2; fclose(f);
      /* remove B-edges that collide with pi by swapping later: just clear conflicts via random swaps */ }
    rebuild();
    ll best=E;
    for(ll st=0; st<steps; st++){
      double T = T0*pow(T1/T0,(double)st/(double)steps);
      if(!fixpi && rnd01()<0.05){ /* pi move */
        int a=rndint(NN), b=rndint(NN); int pa=pi_[a], pb=pi_[b];
        if(b==a||b==pa) continue;
        int opt=rndint(2); int u1=a,v1=(opt?b:pb), u2=pa, v2=(opt?pb:b);
        if(Bm[u1][v1]||Bm[u2][v2]) continue;
        ll e0=E; setpi(u1,v1,u2,v2);
        ll dE=E-e0; if(dE<=0 || rnd01()<exp(-(double)dE/T)) { } else { setpi(a,pa,b,pb); }
      } else { /* double edge swap */
        int a=rndint(NN), cc=rndint(NN); int b,d;
        { int nb[NN],m=0; for(y=0;y<NN;y++) if(Bm[a][y]) nb[m++]=y; if(!m) continue; b=nb[rndint(m)]; }
        { int nb[NN],m=0; for(y=0;y<NN;y++) if(Bm[cc][y]) nb[m++]=y; if(!m) continue; d=nb[rndint(m)]; }
        if(a==cc||a==d||b==cc||b==d) continue;
        if(Bm[a][cc]||Bm[b][d]||pi_[a]==cc||pi_[b]==d) continue;
        ll e0=E; toggle(a,b,-1); toggle(cc,d,-1); toggle(a,cc,1); toggle(b,d,1);
        ll dE=E-e0;
        if(!(dE<=0 || rnd01()<exp(-(double)dE/T))){ toggle(b,d,-1); toggle(a,cc,-1); toggle(cc,d,1); toggle(a,b,1); }
      }
      if(E<best) best=E;
      if(E==0) break;
    }
    /* pi-B conflicts check */
    int conf=0; for(x=0;x<NN;x++) if(Bm[x][pi_[x]]) conf++;
    ll chk=fullE();
    { ll e1=0,e2=0; int hist[16]={0}; int ty[3]={0};
      for(x=0;x<NN;x++){ for(k=0;k<7;k++) e1+=(ll)r1[x][k]*r1[x][k];
        for(y=x+1;y<NN;y++){ e2+=(ll)r2[x][y]*r2[x][y]; int v=r2[x][y]+8; if(v<0)v=0; if(v>15)v=15; hist[v]++; }
        ty[Sov[x][pi_[x]]]++; }
      printf("  E1(profile)=%lld E2(pairs)=%lld types(t0,t1,t2 orbits)=%d,%d,%d\n  r2 hist:",e1,e2,ty[0],ty[1],ty[2]);
      for(i=0;i<16;i++) if(hist[i]) printf(" %d:%d",i-8,hist[i]); printf("\n"); }
    printf("restart %d: final E=%lld (recheck %lld) best=%lld conflicts=%d time=%.1fs\n",rr,E,chk,best,conf,(double)(clock()-t0)/CLOCKS_PER_SEC);
    fflush(stdout);
    if(E==0 && chk==0 && conf==0){
      FILE*f=fopen(out,"w"); fprintf(f,"pi"); for(x=0;x<NN;x++) fprintf(f," %d",pi_[x]); fprintf(f,"\n");
      for(x=0;x<NN;x++){ for(y=0;y<NN;y++) fprintf(f,"%d",Bm[x][y]); fprintf(f,"\n"); } fclose(f);
      printf("SOLUTION written to %s\n",out); return 0; }
    if((double)(clock()-t0)/CLOCKS_PER_SEC > 240.0){ printf("time budget reached\n"); return 0; }
  }
  return 0;
}
