# What the independent review actually establishes in the supplied record

Source: user-supplied `Texte collé(5).txt`, audit section reproduced in `provenance/REVIEWER_AUDIT_EXCERPT.txt`.
The line references below refer to the displayed source transcript in the conversation, citation base turn233file0.

## Reported positive findings

- T4 verified: fixed complete N gives an empty real completion set or one integral fixed-point-free matching (lines 8-9).
- Graph reconstruction and extraction for the one-fixed-point model verified (lines 11-16).
- Reviewer reports a second reconstruction derivation using a full 99x99 block identity (lines 38-43).
- Reviewer reports independent small tests, including 900 synthetic systems (lines 45-57).

## Limits that must remain attached

- One independent model-based hand review is reported; this is not a Lean proof (lines 74-84).
- F0 was not verified or sourced independently by that reviewer (lines 22-30, 79-81).
  This does not mean F0 is false or absent elsewhere in the project; it means this audit does not supply its verification.
- No existence or nonexistence result for the full candidate set was obtained (lines 59-60, 85-86).
- Older T2/T3 were not audited, and T4 does not depend on them (lines 59-60).
- The later ternary projector/capacity note is outside the reviewed package described in this transcript. Do not inherit T4's reviewed status for it.

## Actual evidence held here

This packet contains the reviewer's conversation report and the original T4 exposition. It does not contain the actual named review/AUDIT_REPORT.md, independent_checks.py or independent_checks_output.json; the user may archive those separately.
The packager has not reproduced the reviewer's independent runs. The included witness checker is copied from the original theorem handoff, not from the reviewer.

## Wording corrections

The reviewer reports two harmless wording issues: the diagonal value in the trace lemma is 8, congruent to 0 modulo 2, not literally 0; and an impossible 2+2 matching block must be allowed to give an infeasible case. See reference/ERRATA.md.

## Research-strategy status

The subsequent proposed row enumeration, symmetry, Cayley, lattice and invariant routes were explicitly described by the reviewer as strategy only, not attempted research (source lines 214-251). Their appearance does not prove that auto-loaded memory influenced the report. Neither their feasibility nor their runtime was established by the audit.
