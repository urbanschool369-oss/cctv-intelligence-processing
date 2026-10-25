# Architecture — CCTV Intelligence Processing MVP v0.1 (DRAFT, not frozen)

Source: polished PRD §6–§9. Stack: Python + FastAPI, OpenCV/FFmpeg,
YOLO-family model (exact model TBD), SQLite, local filesystem,
optional Ollama-compatible local LLM endpoint, simple React dashboard
OR server-rendered UI (pick one at freeze), single Python environment
OR Docker Compose. PostgreSQL is later-only, not MVP.

## Principles
Local-first storage and processing. Offline after dependencies and
model weights are installed. Single computer. Separation between
video processing, event storage, querying, and answer generation.
Every displayed event or answer traces to its source recording and
video-time offset. No mandatory external AI service or cloud call.

## Processing flow
1. Recorded file (MP4, AVI, MOV, other verified formats) uploaded
   with camera ID, recording start date/time (user-supplied when
   metadata is unreliable), timezone (e.g. America/Chicago).
2. Metadata extraction + frame sampling (OpenCV/FFmpeg).
3. Local object detection (YOLO-family, sampled frames).
4. Detections + candidate events indexed in SQLite; evidence frames
   saved to the local filesystem.
5. Timeline, summaries, and assistant all read the SAME indexed data.
   Nothing in a summary or answer may come from anywhere else.
   The full 24-hour video is NEVER sent to the LLM.

## Components
- Ingestion + processing: accept uploads, extract metadata, sample
  frames, run detection, record status, failures, coverage.
- Event query + summary service: filter by camera, class, recording-
  time window; counts; chronological event lists; structured data
  for summaries and assistant responses.
- Database + evidence storage: SQLite for video/detection/event/
  report metadata; filesystem for recordings and evidence frames.
- AI assistant: interpret question, query event DB first, generate
  evidence-grounded explanation, return references + uncertainty.
- UI: upload, job status, event browsing, summaries, assistant chat
  — matching the approved hi-fi wireframes (navy/gold, coverage
  strip on every screen, candidate events only).

## Data model (PRD §8 — fields are frozen candidates, types TBD at build)
- Video: id, camera_id, filename, stored_path, recording_start,
  timezone, duration_seconds, analysis_status, coverage.
- Detection: id, video_id, timestamp_seconds (offset, authoritative
  when start is unknown), timestamp_utc (only when a reliable start
  exists — never fabricated), class_name, confidence, bounding_box,
  frame_reference.
- Event: id, video_id, camera_id, event_type, start_time, end_time,
  observation_count, max_confidence, evidence_reference, review_status.
  Events are candidate groupings, NOT verified incidents.
- Report: id, period_start, period_end, camera_filter, summary_text,
  event_ids, created_at, model_version (where applicable).

## Timestamp rules (hard — see also never-do.md)
- Never assume analysis time = recording time. Never infer recording
  start from upload/analysis time.
- Clock times = recording start + video offset + timezone, only when
  a reliable start exists. Otherwise show RELATIVE video timestamps.
- Preserve offsets + timezone through indexing, summaries, assistant.
- Report gaps/failures so an empty period is never read as "nothing
  happened".

## Storage layout (PRD §9)
data/recordings/<camera-id>/<recording-date>-<file>
data/evidence/<camera-id>/<recording-date>/event-####.jpg
data/reports/<recording-date>/summary-*.json
data/cctv_intelligence.sqlite3
Folder date = recording date, NOT analysis date. Recording paths
stable. Evidence metadata must retain enough source reference for a
later implementation to generate short clips from the original.

## Build order (PRD §13, phases 1–5)
1. Upload + local detection (short recording first).
2. Event evidence + timeline.
3. 6h/24h summaries (validate timestamp + coverage BEFORE free-form
   summary generation).
4. Conversational AI on top of indexed data.
5. Pilot + reliability validation (full-day recording, false/missed
   review, processing time, gaps, offline check).
