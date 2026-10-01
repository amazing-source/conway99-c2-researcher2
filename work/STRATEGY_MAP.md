# Strategy map: C2 branch (involution of srg(99,14,1,2)), 2026-10-01

Question: what actually moves EX / NO-EX, and what should be done next?

## 1. The map

| Route | What it is | Status (last seen) | Converging? | Bottleneck |
|---|---|---|---|---|
| **C: rank-24 envelopes** | Finite case split into 156 odd unimodular lattices (Borcherds), then exact frame/pair checks | ~91-93/156 excluded (9 on 27/09, 58 on 29/09 morning, ~92 on 29/09 evening). Remaining ~6600 CPU-h (campaign estimate). AWS run aborted (account problem). | **YES**: monotone, certificate-based, has a finish line | compute for the hard tail (small root systems, O24 partial); the reduction (Part I) still needs written proofs and checks |
| **Rank-17** | Second finite route (U -> Z^7 + V, 9 unimodular V) | 228/751 classes closed (29/09); now on the "even-sector hard core" (k = 28, 13 classes) | **YES**, slowly | same type: finite tail plus lemmas |
| **C2 notebook, dense side** | Classify the D-structure (siblings, anchored, twisted, disjoint squares, mixtures) | Anchored dead, pure twisted dead, M1 mostly dead. Mixtures (10^4 to 2*10^5 skeleton classes per family) and disjoint squares open | **Stalled** ("needs a new structural lever") | no lever found |
| **Researcher-2 campaign (this record)** | Native/conceptual: Theorem C, objects, overlaps, representations, Z[C2], twist calculus, odd eigenspace | R1-R21 are reformulations, local lemmas and rediscoveries. 0 cases closed. | **NO** | no objective tied to cases; frames kept changing |
| **EX (construction)** | Find (Q, N) | No candidate. Heuristic searches fail even to rediscover BvLS at m = 11. | **NO** | no credible constructive method |

## 2. Why the conceptual loop did not converge (honest diagnosis)
- Every round proposed a new frame with good hygiene (pre-registration, duplication checks, stop rules). But no round was required to close a named case, so "success" meant "new representation" rather than "fewer open cases".
- Most frames re-derived content of the C2 notebook (§8 Sym/Alt, §14, §19, §24) in new vocabulary. My duplication checks caught this late. I read §14 early but did not connect it until the twist round.
- The campaign's own STATUS says it: local extendability is high everywhere, and a missing obstruction would have to be global. Global obstructions in this problem have so far come only from finite exhaustion (Route C, rank-17) and from hand lemmas that close whole families (§24, §32).

## 3. Recommendation
1. **Stop open-ended idea rounds** (from any model, including me) unless they pass the rule in s.4.
2. **Make Route C the master ledger** (one canonical tracker). Treat rank-17 as the second ledger.
3. **Spend the math on the Route C hard tail.** Promote the repeated computational reason into family-level lemmas, as ROUTE_C.md already says.
   - The best current candidate: the fractional tight-frame LP of c2_experimental note 57. It killed all 16 trap survivors and one whole y1 orbit with one LP.
   - Turning it into exact per-orbit or per-envelope certificates could cut the ~6600 CPU-h by a large factor.
   - Measure progress only as envelopes closed and CPU-h saved.
4. **Restore compute** for whatever remains (fix the account or another provider). Before any run: a cost and exhaustiveness plan, with the manifest standard of ROUTE_C.md.
5. **In parallel, make 156/156 a proof.** Write and independently check Part I of the reduction:
   - the envelope theorem (min U >= 2);
   - the frame identity;
   - completeness of the pair enumeration.
   - Without this, 156/156 is only a computation.
6. **Researcher-2 line:** freeze it. Keep Theorem C, the T4 reconstruction and the failure memory as reference. Do not open new representations.

## 4. Rule for any proposed next step
Accept a step only if it states, before it starts:
- which open envelopes, classes or families it closes, or how many CPU-h it saves;
- how that is verified (certificate, second reader, manifest);
- what result would make us stop it.

A step that can only promise "insight" or "a new representation" is declined.
