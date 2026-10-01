# C2 — Researcher 2 starting packet

**Purpose:** investigate existence, after the reported independent hand audit of the exact real-linear completion theorem T4.
**Not a nonexistence proof; not a new verification of the auditor's work.**

## Begin

Use this as a separate research folder, not as the original referee workspace. The original handoff's `CLAUDE.md` asks for an audit; the `CLAUDE.md` here asks for existence research.

Start by reading `CLAUDE.md`, `MODEL.md`, `AUDIT_STATUS.md`, and `TASK.md`.
These contain the exact problem and the working status of its prerequisites.

The operator can send:

> Begin the Researcher 2 task in CLAUDE.md and TASK.md. Use MODEL.md and AUDIT_STATUS.md as the initial project-specific basis. First record your own mathematical starting observations and choose a mechanism to investigate. Then read DUPLICATION_NOTES.md before investing substantial work in it. Do actual mathematical research, not just a strategy report. Treat the supplied T4 as independently hand-reviewed, not formally verified. Do not assume existence or nonexistence. Keep work in work/. No paid compute, external messages, or massive searches.

## Contents and staged use

- `MODEL.md`: exact quantified target, T4 statement, and reconstruction.
- `AUDIT_STATUS.md`: what the supplied reviewer transcript actually reports; F0 and proof-status limits.
- `TASK.md`: research task and evidentiary standards, without a prescribed mathematical route.
- `DUPLICATION_NOTES.md`: short project-context disclosure to consult after the initial independent derivation.
- `reference/PROOF_CURRENT.md`, `reference/GRAPH_RECONSTRUCTION.md`: original exposition copied byte-for-byte from the theorem handoff; consult when needed.
- `reference/ERRATA.md`: the reviewer's two wording corrections, not silently applied to the originals.
- `provenance/REVIEWER_AUDIT_EXCERPT.txt`: the audit section of the user-supplied transcript. Its later research suggestions are not included in this starting packet.
- `code/verify_witness.py`: the original handoff's exact supplied-witness checker. This is **not** the independent reviewer's program.
- `data/INPUT_FORMAT.md`, `data/positive_control_m2.json`: original input specification and nine-vertex control.
- `work/`: the new researcher's output directory.
- `MANIFEST.json`: hashes and source records.

## Research target

Find a complete N satisfying the signed equations with feasible L_N, or prove that no such N exists.
A positive explicit pair reconstructs a Conway graph with a one-fixed-point involution.
A universal negative proof excludes one-fixed-point involutions; F0 extends that exclusion to all involutions.

T4 itself supplies neither answer. Its linearity is conditional on N being fixed.
No full m=7 N, no feasible m=7 pair, and no universal infeasibility certificate is supplied here.

## What is deliberately not included

The full discovery chronology, the reviewer's speculative route recommendations, the older two-completion/unsigned-uniqueness proofs, and the later ternary-projector research note are not part of the initial packet.
The later ternary note was not covered by the supplied T4 audit. It can be introduced later as an unreviewed research candidate, not as a certified consequence package.

The user's actual files `review/AUDIT_REPORT.md`, `review/independent_checks.py`, and `review/independent_checks_output.json` were named in the transcript but were not attached here. The packet does not fabricate them. Archive those originals when available.

## Local witness-control command

The witness checker requires NumPy. With it already available:

    python code/verify_witness.py --pair data/positive_control_m2.json --m 2

This checks a nine-vertex positive control, not Conway 99. It does not rerun or certify the independent referee's checks.
