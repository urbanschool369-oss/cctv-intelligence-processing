# Phase 2 decisions — recorded, NOT a spec v0.1 edit

Author: Shekar Kaki
Frozen spec v0.1 (spec/SPEC-PACKET.md) is NOT edited in place.
This file records decisions that fill TBDs for Phase 2 only, with
Shekar's word, so a builder does not have to guess them.

## Gap threshold — DECIDED 2026-10-25 ~07:26 CT
- Value: 30 seconds.
- Meaning: successive detections of the same class on the same camera
  belong to the same candidate event if the gap between them is
  30 seconds or less; a gap over 30 seconds starts a new candidate event.
- Scope: Phase 2 only. Tuning from real test footage may change it
  later, as a new decision, not a silent edit.
- Approved by: Shekar, tap "Approve 30 seconds as the gap threshold
  for Phase 2" (2026-10-25).

## Other Phase 2 inputs already decided
- Model: YOLOv8s (Shekar, 2026-10-25).
- Sampling for the short-recording test: 1 fps (Shekar, 2026-10-25).
  Sampling rate for 24h footage is still TBD.
- Frontend: API only for Phase 1; frontend choice still TBD for
  later phases.
- Confidence threshold: still TBD — 0.25 in the Phase 1 test is a
  test parameter only, 0.60 in the wireframes is a placeholder only.
  Neither is a frozen spec value.

## Blockers cleared 2026-10-25
- Mac clone verified: ~/Documents/cctv-intelligence-processing,
  created 2026-10-25T12:21:12Z, spec files present.
- Claude Code sign-in check done by Shekar on the Mac.
- Gap threshold: decided above.
