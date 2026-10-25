# CLAUDE.md — CCTV Intelligence Processing MVP

Author: Shekar Kaki

## Project memory (read every session)
- Frozen spec: spec/SPEC-PACKET.md v0.1, frozen 2026-10-25. If this
  file and the spec disagree, the spec wins. Stop and ask Shekar.
- Sources: polished PRD docs/02-prd-polished.md; approved hi-fi
  wireframes docs/03-wireframes.md (all 5 screens, navy/gold).
- Phase 1 DONE (direct build by Mitra, not by this team — see
  BUILD-REPORT.md): FastAPI upload + YOLOv8s 1 fps detection + SQLite
  Video/Detection, tested on synthetic bus video, 25 detections.
  Next is Phase 2: event evidence + timeline.
- Stack: Python + FastAPI, OpenCV/FFmpeg, YOLOv8s, SQLite, local
  filesystem, optional Ollama-compatible LLM (Phase 4 only).
  Frontend choice still TBD — do not build a UI until Shekar picks it.

## Folder ownership (one owner per folder, Lead merges only)
- Backend subagent: app/ only (FastAPI, detection, storage).
- Frontend subagent: web/ only — NOT CREATED YET, do not create it
  until the frontend choice is decided.
- QA subagent: tests/ only, plus the test report.
- DevOps subagent: deploy/ and CI only. No production deploy ever
  without Shekar's separate word.
- Lead: reads spec + BUILD-REPORT at session start, spawns subagents,
  merges, writes BUILD-REPORT.md (never overwrite in place — new
  version, note what changed).

## Hard rules (spec/never-do.md governs)
- No live CCTV, no RTSP, no IoT, no facial recognition.
- Candidate events only — never theft, trespass, intrusion, or a
  confirmed incident. Never invent identities, intent, or events.
- Never mark a failed/partial job complete. Never fabricate a UTC
  timestamp. Coverage gaps always shown.
- No secrets, keys, passwords, footage, faces, or personal data in
  the repo. Env vars / provider settings only.
- Signature "Shekar Kaki" on all code headers, architectures, diagrams.
- No accuracy claim without a manually reviewed test set.
- Subagents by default, NOT Agent Teams, unless Shekar approves the
  cost separately. Plan mode first for new work. Never bypassPermissions
  outside an isolated container.
- Test confidence 0.25 was a Phase 1 TEST parameter only, not a spec
  value. Thresholds must come from observed precision/recall.

## How to run / test (Phase 1, verified)
- venv: .venv (local only, not committed), Python 3.12.
- Server: .venv/bin/uvicorn app.main:app --port 8001
- Health: GET /health. Upload: POST /videos (camera_id, recording_start,
  timezone). Analyze: POST /videos/{id}/analyze.
- QA reports command + output verbatim, not just "tests pass".
  A feature without a run is not done.
