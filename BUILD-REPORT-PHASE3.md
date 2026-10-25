# BUILD REPORT — Phase 3 (6h / 24h summaries)

Author: Shekar Kaki
Spec: frozen spec v0.1, plus spec/phase2-decisions.md (gap 30s).
Build started on Shekar's tap "Start Phase 3 summaries now"
2026-10-25 ~08:04 CT, in Mitra's VM workspace (same route note as
Phase 2: Mac Terminal cannot be driven by Mitra, so no Mac-side
Claude Code CLI run; code is synced to GitHub for the Mac clone).

## What was built
- app/main.py: GET /summaries (camera_id, start, end).
  start/end accept video-offset seconds OR ISO datetimes with an
  offset. ISO windows convert per video via recording_start; a
  video with no reliable recording_start is excluded from an ISO
  window and named in coverage, never silently assumed.
- Summary is computed from indexed events only, no LLM call in
  Phase 3: event_count, observation_count, counts_by_class,
  event_ids, full event list, summary_text template. Text states
  events are candidates, not user-verified incidents.
- Coverage validated first: videos in scope with analysis_status,
  duration, processed_seconds, gaps, errors; coverage_status
  "covered" or "no_footage". Empty window text says "No candidate
  events indexed in this window. This does NOT mean nothing
  happened" plus coverage, never a clean bill.
- GET /health now reports phase 3.
- tests/test_phase3.py: no YOLO run needed.

## Test runs (2026-10-25)
- tests/test_phase2.py: PASS (regression).
- tests/test_phase3.py: PASS. Seconds window 0–21600, CAM-01 ->
  2 events, bus 1, person 1, 25 observations. ISO window
  2026-06-12T18:00–19:00-05:00 -> same 2 events. Empty window
  10000–20000 -> 0 events, with the does-NOT-mean-nothing-happened
  text. Unknown camera -> coverage_status no_footage.
- Live server (uvicorn, port 8003, stopped after test): /health
  phase 3, gap 30.0; /summaries CAM-01 0–21600 -> same counts and
  text as the test.
- Checks: py_compile ok. No secrets, no real footage, no faces,
  no theft/intrusion wording in the summary template.

## Phase 3 exit check
PRD Phase 3 exit (summaries from indexed data, with coverage):
MET on synthetic input (Phase 1 test video events). Default 6h
windows are covered by the custom-range endpoint: a caller passes
midnight–6, 6–noon, noon–6, or 6–midnight as start/end; a named
6h/24h preset is not yet a separate parameter (open, minor).
Not a real CCTV accuracy claim, not the full acceptance set.

## Known limits / open items
- Assistant (Phase 4) not built; summaries here are template text,
  not free-form LLM prose, by design for Phase 3.
- Confidence threshold, 24h sampling rate, frontend choice: still TBD.
- No merge, staging, production, or publish move approved or done.
- Server stopped after the test; no deployment.
