# Lattice parity of the 7-rank (P7): proved, already known, no leverage — STOPPED

## Statement (PROVED HERE; rediscovery, see Comparison)

Let N be any symmetric integer 42x42 matrix with zero diagonal such that NR = 0 and N^2 = N + 12I - RR^T
(R = the 42 positive roots of D7). Then rank_F7(N - 4I) = 7 + g with g = dim D_7(L_{-3}) ODD.
In particular rank_F7(N - 4I) = rank_F7(N + 3I) is even.

Hypotheses actually used: integrality of N and the two equations of (S). Not used: D, L_N, T4, F0,
entries in {0, +-1} (beyond integrality), any type or branch assumption.
External inputs (EXTERNAL INPUT, standard): the oddity formula of Conway-Sloane (signature + sum of p-excesses
over odd p = oddity mod 8; checked here on A_2 and A_6), and the anti-isometry of the discriminant forms of two
mutually orthogonal primitive complements in a p-unimodular lattice (Nikulin).

## Proof

Eigenvalues of N: 4 (15), -3 (20), 0 (7, eigenspace col R); Pi_4 = (N^2+3N)/28, Pi_{-3} = (N^2-4N)/21,
Pi_0 = H/12; L_lambda = Z^42 cap V_lambda.
 (i)  L_0 = R(D7*) (saturation of col R): Gram 12 Gram(D7*), det 2^12 3^7; 3-adically 3^{+7} (unit form 4I_7).
 (ii) 2-adic. Pi_{-3} is 2-integral, so L_{-3} (x) Z_2 is an orthogonal summand of Z_2^42: unimodular. It is even:
      v in L_{-3} gives v = P2 v mod 2 with P2 = Pi_{-3} mod 2 = N + H mod 2, and P2 1 = N1 + H1 = 0 mod 2
      (row sums of N are = sum of squares = 10 mod 2; H1 = R(12,10,8,6,4,2,0)^T is even), so v.v = v.1 = 0 mod 2.
 (iii) 3-adic. Pi_4 is 3-integral, so L_4^perp is 3-unimodular; L_{-3} and L_0 are orthogonal primitive
      complements in it, so D_3(L_{-3}) = -D_3(L_0): component 3^{-7} ((-1/3)^7 = -1). 3-excess = 14 + 4 = 2 mod 8.
 (iv) 7-adic. Pi_0 is 7-integral, so Lambda = L_0^perp is 7-unimodular; 7z = (N+3)z - (N-4)z shows
      Lambda/(L_4 + L_{-3}) = (Z/7)^g; L_{-3} (x) Z_7 = 1^{20-g} + 7^{+-g}; 7-excess = 6g + 4k_7. N - 4I is
      invertible on L_0 mod 7 and has rank g on Lambda mod 7, so rank_F7(N - 4I) = 7 + g.
 (v)  Oddity formula for L_{-3} (positive definite, rank 20, oddity 0): 20 + 2 + 6g + 4k_7 = 0 mod 8,
      so 6g + 4k_7 = 2 mod 8, which forces g odd.

## Comparison and leverage

 - c2_experimental note 10 s.3 item 4 (note read in full, 67 lines): "dim D7(M_out) impair, donc
   rang7(S_out - 3I) = 7 + dim D7(M_out) est pair", with S_out = -N and M_out = Z^42 cap ker(S_out - 3I) = L_{-3},
   derived by the same oddity-formula argument (D3(M_out) = -(Z/3)^7). Status there: DERIVE, framework validated on
   Paley(9), L2(7), Paley(49). P7 is a rediscovery.
 - Note 10 s.4: these parities hold for every integer solution of the S-stage, cannot filter, and would kill C2
   only together with an independent computation of a 7-rank. Note 22 (review): genus/Brown/discriminants CLOSED.
 - Admissible objects: none at m = 7 carries an integral N; every integral solution satisfies P7; no branch's
   defining data (Sigma, unsigned pair, F2/F3 data) determines rank_F7(N - 4I). It excludes nothing.
 - Companion F3 statement (disc(im P) is a square, since det L_4 = 2^12 7^g = 1 mod 3): automatic for (B, D, P),
   because a projector with the right support and caps lifts to an integral N (Lemma 2.1, Thm 3.1).
 - BvLS check: not run. The stop rule (already known) was met first.

Verdict: automatic and already known. No leverage. Stopped here.
