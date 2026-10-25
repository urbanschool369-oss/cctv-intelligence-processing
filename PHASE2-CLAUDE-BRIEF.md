# Phase 2 brief for Claude Code Lead (ready, NOT started)

Author: Shekar Kaki
Read first, in order: CLAUDE.md, spec/SPEC-PACKET.md (FROZEN v0.1),
spec/phase2-decisions.md, VERDICT-PHASE1.md, BUILD-REPORT.md.
Frozen spec wins over chat if they disagree. Stop and ask on any
conflict or TBD — do not guess.

## Goal (PRD Phase 2 exit)
A user can browse candidate events and trace each event to its
evidence and source recording.

## Build
- Group detections into candidate events: same camera, same class,
  gap 30 seconds or less merges, over 30 seconds splits.
  Candidate events only — never label theft, intrusion, or intent.
- Add endpoints per spec/api-contract.md: GET /events (filters:
  camera, time window, object class), GET /events/{id},
  GET /evidence/{id}. Keep Phase 1 endpoints unchanged.
- Evidence: each event links to its detections, timestamps, and
  source video id + timestamp. If evidence is unavailable, state
  that explicitly — never invent a frame or timestamp.
- Never report a failed or partial job as complete. Coverage and
  gaps must be reported, per frozen spec.
- Folder ownership: Backend owns app/ only, QA owns tests/ only,
  Architect owns layout, Reviewer second pass, DevOps deploy/ + CI
  only if a ship move is approved separately (none is approved here).

## Deliver
Code + tests + BUILD-REPORT update with branch/commits, per-test
results, commands + outputs verbatim, coverage, security +
dependency + secrets scan results, known limits, items needing
Shekar's word listed separately. No merge, staging, production, or
publish move without Shekar's separate approval for that move.

## How to run this on the Mac (Shekar's step, Mitra cannot run Mac Terminal)
cd ~/Documents/cctv-intelligence-processing
claude
Then paste this brief's goal and the "Read first" list. Work in
Chat mode on the Mac desktop apps only where applicable; for Claude
Code CLI, follow the signed-in Pro account Shekar verified.
