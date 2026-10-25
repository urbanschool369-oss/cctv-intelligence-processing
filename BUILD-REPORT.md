# BUILD REPORT — Phase 1 (upload + local detection)

Author: Shekar Kaki
Spec: frozen spec v0.1 (spec/SPEC-PACKET.md, frozen 2026-10-25).
Build route note: this Phase 1 code was written directly by Mitra in
this workspace, NOT by the Berd agent team / Claude Code engine.
Shekar asked 2026-10-25 whether the Agents team dev approach is still
being followed; the route decision for later phases is still pending
at the time of this report (options: keep direct build with Berd gates
only, or move to Berd + Claude Code team route).

## What was built
- app/main.py: POST /videos, GET /videos/{id}, POST /videos/{id}/analyze,
  GET /health. 1 fps sampling, YOLOv8s (Shekar's pick 2026-10-25).
- app/db.py: SQLite Video + Detection tables (spec architecture.md).
- Not built in Phase 1 (by design, PRD phases 2–4): event grouping,
  summaries, assistant, UI. Frontend choice still TBD.

## Environment / commands
- Python 3.12.3, venv .venv (local only, not committed).
- FastAPI + OpenCV 5.0.0 installed after moving pip temp off /tmp
  (first install failed "No space left on device" on the 512M /tmp).
- ultralytics install took ~25 minutes (torch download, quiet pip),
  completed with "ultralytics ok".
- Server: `.venv/bin/uvicorn app.main:app --port 8001`
- Health: {"status":"ok","phase":1,"model":"yolov8s.pt","sampling_fps":1.0}

## Test run (2026-10-25)
- Test input: testdata/bus-5s.mp4 — a 5-second video made by repeating
  the Ultralytics sample bus.jpg image. This is a SYNTHETIC pipeline
  test, NOT real CCTV footage and NOT a detection-quality evaluation.
- Upload: POST /videos, camera_id CAM-01,
  recording_start 2026-06-12T18:00:00-05:00, timezone America/Chicago
  → id b9b06a949b6e, duration_seconds 5.0, status queued.
- Analyze: POST /videos/b9b06a949b6e/analyze
  → {"analysis_status":"complete","sampled_frames":5,"detections":25,"errors":[]}
- Stored: 25 detections in SQLite, 5 per sampled frame (1 bus + 4 persons
  per frame, timestamps 0.0–4.0s at 1 fps). Example: t=0.0 bus 0.916,
  person 0.892 / 0.878 / 0.874 / 0.510.
- Coverage after run: processed_seconds 5.0, sampled_frames 5, gaps [],
  errors [].
- Test confidence: 0.25 (Ultralytics default, test parameter ONLY —
  not a frozen spec value; spec requires thresholds from observed
  precision/recall).

## Phase 1 exit check
PRD Phase 1 exit: "A short recording can be processed locally, with
timestamped detection observations stored and associated with the
source video." — MET by the test above, on synthetic test input.
This is NOT a claim about real CCTV accuracy, and NOT the full
10-item acceptance set (those are Phase 5 / full-demo checks).

## Addendum — 2026-10-25 (Verdict fix, history above untouched)
- Route decision: Berd + Claude Code team route, chosen by Shekar
  2026-10-25. Phase 1 above was a direct build; later phases use
  the team route.
- GitHub sync: done 2026-10-25, commit
  6f652d400f76137b6f163ea1d2b7c26de897c72c (private repo
  urbanschool369-oss/cctv-intelligence-processing). The "not done"
  line above is superseded by this addendum.
- Gap threshold: DECIDED 30 seconds for Phase 2 (Shekar, 2026-10-25),
  recorded in spec/phase2-decisions.md. The "still TBD" line above
  for gap threshold is superseded; other TBDs remain open.
- Mac clone verified 2026-10-25 ~07:25 CT; Claude Code sign-in
  check done by Shekar on the Mac.

## Known limits / open items
- Exact YOLO model now decided (yolov8s); still TBD: sampling rate
  for 24h footage, gap threshold, confidence threshold, frontend.
- Weights yolov8s.pt download on first model use (local after).
- Server stopped after the test run; no deployment, no public access.
- Code is in this workspace only; GitHub sync is a separate step
  (browser upload route, as before) and has NOT been done for app/.
