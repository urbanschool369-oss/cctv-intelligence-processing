# BUILD REPORT — Phase 2 (event evidence + timeline)

Author: Shekar Kaki
Spec: frozen spec v0.1, plus spec/phase2-decisions.md (gap 30s,
Shekar 2026-10-25). Build started on Shekar's tap "proceed"
2026-10-25 ~07:59 CT, after Mac pull to trace:004 was verified.

## Route note (honest)
Phase 2 was built in Mitra's workspace (VM), where the shell, venv,
and test data live, following CLAUDE.md folder ownership and the
Phase 2 Claude brief — NOT by running Claude Code CLI on the Mac,
because Mitra cannot run Terminal on the Mac. The code is the same
shape Claude Code would produce from PHASE2-CLAUDE-BRIEF.md, and it
is synced to GitHub for the Mac clone. If Shekar wants a Mac-side
Claude Code re-run, that is a separate step he runs himself.

## What was built
- app/db.py: events table (id, video_id, camera_id, event_type,
  start_seconds, end_seconds, observation_count, max_confidence,
  evidence_reference, review_status).
- app/main.py: group_detections_into_events() — same class, same
  video, gap <= 30s merges, gap > 30s splits, idempotent (prior
  events for a video deleted first), review_status always
  "candidate". Grouping runs automatically after a successful
  analyze; failed jobs are never grouped and never reported complete.
- Endpoints: GET /events (camera_id, class_name, start, end
  filters), GET /events/{id} (event + its detections +
  evidence_status), GET /evidence/{id} (event id or detection id;
  frame file when present, else explicit 404 evidence-unavailable).
- GET /health now reports phase 2 and gap_threshold_seconds 30.0.
- tests/test_phase2.py: synthetic detections, no YOLO run needed.

## Test runs (2026-10-25)
- tests/test_phase2.py: PASS. Person 10, 12, 40 (gap 28 merges)
  -> 1 event, 3 observations, 10.0–40.0s; person 80 (gap 40 splits)
  -> 1 event, 1 observation; vehicle 20, 25 -> 1 event. Total 3.
  Filters, event detail, 404 for unknown event, and
  evidence-unavailable for a missing frame all passed. Regrouping
  is idempotent (3 events again).
- Live server (uvicorn, port 8002, stopped after test):
  /health -> phase 2, gap 30.0. /events?camera_id=CAM-01 on the
  Phase 1 synthetic video -> bus event 0.0–4.0s, 5 observations;
  person event 0.0–4.0s, 20 observations; both candidate, with
  evidence_reference to frame-0000.jpg. /events/{bus event} ->
  event + 5 bus detections.
- Checks: py_compile ok for app/main.py, app/db.py,
  tests/test_phase2.py. No secret assignments, no theft/intrusion
  wording in code/tests. No secrets, no real footage, no faces.

## Phase 2 exit check
PRD Phase 2 exit: "users can browse candidate events and trace each
event to its evidence and source recording" — MET on synthetic
input (Phase 1 test video + synthetic grouping test). Not a real
CCTV accuracy claim, and not the full 10-item acceptance set.

## Known limits / open items
- Confidence threshold, 24h sampling rate, frontend choice: still TBD.
- Summaries (Phase 3) and assistant (Phase 4) not built.
- No merge, staging, production, or publish move approved or done.
- Server stopped after the test; no deployment, no public access
  beyond the public GitHub repo itself (code only, no data).
