# Route C: can it be resumed? (read-only check, 2026-10-01)

**Answer: YES.** The restart procedure is documented and the partial results are saved.

## Where the restart procedure is documented
- On this PC:
  - `Desktop\c2_experimental\PLAN_AWS.md` (§ "Machine interrompue" / "Reprise d'une machine disparue");
  - `c2_experimental\c2_cloud_run\README_RUN.md` (relaunch command 2 with the same `--slice`);
  - `c2_experimental\aws_repo\README.md`;
  - `c2_experimental\moniteur_aws\LISEZMOI.txt`.
- On GitHub: `amazing-source/conway99-c2-aws`.
  - README §3: state SILENCIEUSE / ERREUR -> "coller la même ligne", which resumes.
  - `machine.sh` line 9: "Re-running the same command on a NEW machine resumes the slice: the results already on the branch are restored, finished jobs are skipped."

## Restart line (one per slice, on any Linux machine)
    git clone https://x-access-token:TOKEN@github.com/amazing-source/conway99-c2-aws.git && bash conway99-c2-aws/machine.sh i/54 NAME

- Use **/54**, the plan actually launched (`machines.json` on GitHub), NOT the /18 table of the README. Another slicing changes the job sets, and the saved results would not be reused.
- Slice names:
  - slices 0-17 use the names in `machines.json` (frere-eun1-0, pere-eun1-0, toi-eun1-0, ...);
  - slices 18-53 use `slice-<i>` (branches run/slice-19 .. run/slice-44 already exist).
- TOKEN: a GitHub fine-grained token, Contents read/write, on conway99-c2-aws only.

## What was saved before the AWS account problem (GitHub run branches, last push 2026-09-30 05:15 UTC)
- 399 of 3427 jobs are finished and saved. That is about 818 of 6712 estimated core-hours (12 %).
- Remaining: about 5900 core-hours (the plan's estimate is ±x2).
- Lattices in the batch: 58. Fully finished: 1 (061).
- Slices with no saved result: 7, 10, 18, 29-31, 34, 36, 39-53. These restart from zero, with the same line.

## After the batch
- In the lab: `scripts/cloud/import_results.py` checks the engine provenance, then `stream_finish` recomputes the exclusions.
- PLAN_AWS target: 93 + 57 + 058 (once its twins are done) = 151/156.
- Not in this batch, and needing code first:
  - the Golay family 001, 002, 004, 010 (orbit reduction from generators);
  - 000 (O24), its own route, about 47 classes, about 20 h.

Check script (read-only, GitHub API only): scratchpad `routec_progress.py`. Nothing was launched.

## AWS budget check (2026-10-01; read-only CLI queries, the user's account only, $120 left)
- Spot vCPU quota of 128 APPROVED in eu-north-1, us-east-2, us-east-1, us-west-2, eu-west-2 and eu-central-1 (each case closed, value 128). That allows 4 c7a.8xlarge per region.
- On-demand requests to 128 are still pending (current 32). eu-west-1 and ap-northeast-1 are still pending (current 5).
- No instance running or pending in any of these regions.
- c7a.8xlarge spot price now (cheapest zone): eu-north-1 0.300, us-east-2 0.376, us-east-1 0.534, us-west-2 0.548, eu-west-2 0.668, eu-central-1 0.726 $/h.
- Remaining work: about 5,900 job-h, i.e. about 227 machine-h at 26 jobs per machine (plan estimate ±x2, so 113-454).

| Option | Machines | Cost (central) | Wall time (central) | Cost if x2 |
|---|---|---|---|---|
| eu-north-1 only | 4 | ~$68 | ~57 h | ~$136 |
| eu-north-1 + us-east-2 | 8 | ~$77 | ~28 h | ~$153 |
| all 6 regions | 24 | ~$119 | ~10 h | ~$238 |

Local alternative: the PC alone, about 3 weeks (`sched.py`).

## Local run started (2026-10-01 19:48, on the user's request, 4 threads max while gaming)
- `sched.py 4` (PID 34380) and `tracker_loop.sh` (PID 3652) started from the lab folder through `scratchpad/start_pc_run.ps1`.
- Affinity mask 0xF000 (logical CPUs 12-15, the last 2 cores of the 7800X3D) and BelowNormal priority. Every child process inherited both (checked).
- First launches: 061 chunks 4-7/8. These are exactly the 4 package jobs AWS had already finished, which are not yet imported, so this is duplicate work.
- Fragility: the engine's C1 clone lives in an old Claude temp folder (`stream_lattice.py` CLONE = ...\AppData\Local\Temp\claude\C--Users-bfhdh-Desktop\19a7c411...\scratchpad\ext\conway99-c1). Cleaning Temp would break the run.
- To stop the run: kill PID 34380 (the scheduler) and its run_chunk children. Chunks are resumable.

## AWS results imported (2026-10-01 19:50, on the user's request)
- `aws_repo/monitor_git.py --once --fetch` pulled the 399 result files from 31 run branches.
- `scripts/cloud/import_results.py c2_cloud_run aws_repo/resultats/*/results` reported: imported 399, duplicates 0, refused 0, no resolve_incomplete needed.
- The 4 duplicate local chunks (061, chunks 4-7) were stopped, process trees killed.
- `stream_finish.py`: newly excluded [61]. Tracker: **94 excluded**, 61 open, 1 partial.
- The scheduler then moved on by itself to 062 chunks 0-3. It is still at 4 slots, mask 0xF000, BelowNormal.

## Local run stopped (2026-10-01 19:53, on the user's request)
- sched.py, tracker_loop and all chunk processes killed; 0 lab processes remain (checked).
- The 4 in-progress chunks (062, chunks 0-3) were interrupted and will restart from scratch next time.
- The imported results and the tracker (94/156) are saved on disk.
- To restart with the same cap: `powershell -ExecutionPolicy Bypass -File <scratchpad>\start_pc_run.ps1` (edit the 4 inside it), or the Git Bash commands above.

## Cost model from the 399 real AWS jobs (2026-10-01)
- Actual / estimated hours per job: median 1.01, p10 0.24, p90 2.98. Weighted total: 1062 h actual vs 818 h estimated, so **x1.30**.
- Remaining 5,894 estimated job-h x 1.30 = about 7,660 job-h, i.e. about 295 machine-h at 26 jobs per machine.
- Cost:
  - eu-north-1 only ($0.30/h): about $88, plus about $2 of disk and IP overhead, so **about $91**. With 4 machines, about 3 days of wall time.
  - us-east-2 ($0.376/h): about $111.
- Decision (user): spend the whole $120. The hard cap is enforced by the machines themselves through a spend ledger, at about $115, priced at the max spot price. The AWS budget is only a backstop.

## Adaptive AWS run built (2026-10-01, on the user's request: user's account only, whole budget, surgical)
- Repo amazing-source/conway99-c2-aws, folder `q/` and README.md. The old 54-slice plan is archived in `OLD_README_54_TRANCHES.md`.
- Engine untouched: the agent starts every job with the package's own `run_jobs.start`, after the MANIFEST check. Calibration must be EQUIVALENT.
- Branch `queue`: atomic claims (non-forced push), a lease of 30 min, and a result is pushed before its done event.
- Spend ledger at the max spot price, cap $115.
- Dead-man switch: 20 min (60 min during setup).
- Instances that are not Spot, or not c7a.8xlarge, are refused.
- AWS budget `c2-route-c-backstop`: $120/month, gross of credits, alerts at 50/80/95/100 % to dilandjematene@gmail.com (created via CLI).
- Bugs caught BEFORE any AWS spend:
  - double claim (stale liveness) in rehearsal 36905706691;
  - fleet listing empty (`for-each-ref` without glob) in rehearsal 36906093798. That bug also blinded the ledger.
  - Both fixed. A local 4-agent / 20-job concurrency test passes. An agent self-check was added.

## Ready to launch (2026-10-01 21:27)
- Rehearsals:
  - 36906558940 (S1, partial): two agents, no double claim, real job 028:0:8 done. Its result was pushed (19:19:56) before the done event (19:19:57). Engine sha identical. Imported into the lab.
  - 36914064111: cap -> STOP, remote stop -> STOP, drain -> DRAINED, nothing claimed. **PASS.**
- Real queue `queue`: 3026 jobs (est 5,894 h x 1.30), cap $115, campaign c2q-20261001. Order: 062 first, 003 last. The monitor reads it.
- Next step: a pilot, 1 c7a.8xlarge Spot in eu-north-1, max price 0.34. Check EN_COURS with 26 jobs and `--aws` OK, then launch 3 more.
- Azure: subscription upgraded (PayAsYouGo, spending limit off); providers registered. Spot quota is 3 vCPU. Auto-requests (480, 120) were refused, so a support ticket is in progress. HB120rs_v2/v3 are allowed in East US at $0.665/h spot. The Azure layer (self-delete, per-pool cap, direction) is not built yet.
