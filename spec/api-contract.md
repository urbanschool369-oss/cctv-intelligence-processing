# API Contract — CCTV Intelligence Processing MVP v0.1 (DRAFT, not frozen)

Source: polished PRD §11. Base: local FastAPI service. All times carry
an explicit UTC offset or are interpreted in the recording timezone.
Relative video timestamps are used when recording start is unknown.
Field names below follow PRD §8; types and error shapes are to be
confirmed at freeze where marked TBD.

## Endpoints (9, exactly as PRD)
| Method | Endpoint | Purpose |
| POST | /videos | Upload a recording with camera ID, recording start time, timezone |
| GET | /videos/{id} | Video metadata, analysis status, coverage |
| POST | /videos/{id}/analyze | Start or retry local analysis |
| GET | /events | Events filtered by camera, class, time |
| GET | /events/{id} | Event details + evidence metadata |
| GET | /evidence/{id} | Evidence image or clip |
| GET | /summaries | 6h, 24h, or custom-window summary |
| POST | /assistant/ask | Natural-language question over indexed footage |
| GET | /health | API + local processing health |

## POST /videos
Request (multipart/form-data): file (MP4/AVI/MOV, verified formats
only); camera_id (required); recording_start (required when known,
else explicitly unknown); timezone (required, e.g. America/Chicago).
Response: Video object (see architecture.md) with analysis_status
(e.g. queued) and coverage (initially unprocessed). Invalid,
unsupported, or unreadable files return a clear error — never a
silent success.

## GET /videos/{id}
Response: Video object including duration_seconds, recording_start,
timezone, analysis_status, coverage (processed sections + known gaps).
A failed or partial job must NOT be reported as complete.

## POST /videos/{id}/analyze
Starts or retries local analysis for that video. Response: job status.
Wireframe default to confirm at freeze: one analysis job at a time.

## GET /events
Query params: camera_id, class_name, start, end (recording-time
window, with explicit offset or recording timezone).
Response: list of Event objects (id, video_id, camera_id, event_type,
start_time, end_time, observation_count, max_confidence,
evidence_reference, review_status). No event may be returned without
its source-video reference.

## GET /events/{id}
Response: single Event + its Detection list (timestamp_seconds,
timestamp_utc if known, class_name, confidence, bounding_box,
frame_reference) + evidence metadata. If evidence is unavailable,
the response states that explicitly — never a broken reference.

## GET /evidence/{id}
Response: evidence image (frame) or clip where available; otherwise
an explicit evidence-unavailable status (TBD: exact status code /
body at freeze — the PRD rule is the status must be explicit).

## GET /summaries
Query example (PRD §11.1):
GET /summaries?camera_id=camera-01&start=2026-10-24T00:00:00-05:00&end=2026-10-24T06:00:00-05:00
Response: Report object (id, period_start, period_end, camera_filter,
summary_text, event_ids, created_at, model_version) PLUS coverage
information for that window. Default windows: midnight–6, 6–noon,
noon–6, 6–midnight; custom ranges supported. Summaries are generated
from indexed data only and must not imply complete observation when
footage or analysis is incomplete. Detections are distinguished from
user-verified incidents.

## POST /assistant/ask
Request example (PRD §11.2):
{ "question": "Summarize all activity overnight and highlight animal detections.",
  "camera_ids": ["camera-01"],
  "start": "2026-10-24T18:00:00-05:00", "end": "2026-10-25T06:00:00-05:00" }
Response MUST include: generated answer, period covered, event IDs
used as evidence, relevant timestamps + evidence references where
available, coverage limitations / uncertainty. The service queries
the event DB before generating any answer. It must NOT invent
identities, intent, theft, timestamps, counts, or evidence. For
"Did anyone steal something?" it must explain detections alone cannot
establish theft and offer observations for human review. Insufficient
evidence is stated, not filled in.

## GET /health
Response: API status + local processing health (TBD: exact fields at
freeze; must cover whether the local pipeline/model is available,
without requiring any cloud call).
