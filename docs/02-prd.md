# PRD — CCTV Intelligence Processing

Author: Shekar Kaki
Status: RECEIVED FROM CHATGPT 2026-10-25 — NOT YET APPROVED BY SHEKAR. DO NOT BUILD FROM THIS FILE UNTIL SHEKAR APPROVES IT.

Source: Shekar's existing ChatGPT thread "CCTV Intelligence Processing", via the
ChatGPT desktop app on his Mac (Mac computer-use session cc-33, 2026-10-25 ~03:07 CT).
Question posted in that thread, in Shekar's voice, on his tap:

> If we move forward and build this as a service, what are the top 5 features
> we need to roll out in the MVP of this project? Please give a PRD or whatever
> requirements are enough to start building from this side, based on the prototype
> scope we discussed: 1 day of CCTV footage, 1 or more cameras, 6-hour or 24-hour
> window summaries, all events and actions, and a talkative AI layer that answers
> on request.

ChatGPT stayed in Chat mode (it offered Work mode for a polished PRD document;
that offer was NOT taken — the reply stayed in Chat, per the standing rule).
The full reply was copied from ChatGPT and saved verbatim on his Mac at
`/Users/skaki/Documents/cctv-chatgpt-prd.txt` (14,473 bytes, 285 lines,
saved 2026-10-25 ~03:10 CT), then copied below without edits, except this header.

Original thread scope (from earlier messages in the same thread, voice transcript):
no CCTV integration for now; feed 1 day of CCTV record from at least one camera
or multiple cameras; analyse to provide 6-hour window summaries or a complete
24-hour window summary, stating all events, actions, and major summaries; the AI
layer is the major emphasis — talkative, giving summaries on request for the
total 24-hour feed. ChatGPT had suggested: prototype first, not a full product
build; process one day's footage locally; detect people, vehicles, plus one
animal class.

---

For this project, I recommend a local-first CCTV Intelligence MVP with five core features—not a full surveillance platform yet.
The product should take one day of recorded CCTV footage from one or more cameras, identify observable events, preserve evidence, generate six-hour and 24-hour summaries, and let a user ask questions in natural language.
The most important design principle is that the AI assistant must answer from detected events and supporting evidence, rather than inventing a story about what happened.
PRD: Local CCTV Intelligence MVP
Product requirements
Version 0.1
Product type: Local-first video analysis service • Initial domain: Farms and private properties • Input: Recorded CCTV files • Deployment: One computer, offline-capable

Primary user
Property / farm owner
Initial scale
1–10 recordings/cameras
Analysis windows
6 hours / 24 hours
Core interaction
Ask questions about footage
The top 5 MVP features

1. Video ingestion and analysis jobs
Upload one or more recordings, associate each with a camera, and process the footage locally. Track job progress, duration, errors, and processing status.
Must support common video formats, resumable operational workflows where feasible, and clear error messages for invalid or unreadable files.

2. Event detection and evidence indexing
Detect supported objects such as people, vehicles, and common animals. Record timestamps, object class, confidence, camera, and evidence references. Group nearby detections into candidate events.
Do not label a detection as theft or an intrusion solely because a person or animal appears in the video.

3. Historical event timeline and investigation
Browse events by camera, time window, and detected class. Open the evidence frame and, when available, jump to the corresponding section of the source recording.
Every event must link back to its source video and timestamp so users can verify the model's findings.

4. Six-hour and 24-hour summaries
Produce summaries for selectable time windows, including activity counts, notable events, chronological highlights, and links to supporting evidence.
Summaries must distinguish confirmed model detections from user-verified incidents and explicitly state gaps in analysis.

5. Talkative, evidence-grounded AI assistant
Answer questions such as “What animals were detected overnight?”, “When did a vehicle appear?”, and “Summarize activity between midnight and 6 AM.” Include relevant timestamps, event counts, and evidence links.
Use a local LLM where possible. The assistant queries the event index and must not claim to have seen details that were never detected or stored.

1. Product goals and non-goals
Goals
- Analyze a full day of recorded video from one camera initially, with a data model that supports multiple cameras.
- Store searchable event metadata locally.
- Generate six-hour and 24-hour reports.
- Answer natural-language questions about indexed activity.
- Operate without mandatory cloud services or external API calls.

Not in the first MVP
- Direct integration with live CCTV cameras.
- Automatic siren, relay, gate, or other IoT control.
- Facial recognition or identification of individuals.
- Guaranteed theft, trespassing, or intent classification.
- Cloud-hosted customer management, billing, or multi-tenant SaaS.
- Complex agent workflows or a large distributed architecture.

These can be future phases after the recorded-video pipeline is reliable.

2. Functional requirements

| ID | Requirement | Priority |
| FR-01 | Upload video files and assign camera IDs | Must |
| FR-02 | Extract video duration, frame rate, dimensions, and timestamps | Must |
| FR-03 | Sample frames and run local object detection | Must |
| FR-04 | Store timestamped detections and confidence scores | Must |
| FR-05 | Group detections into candidate events | Must |
| FR-06 | Save evidence frames and retain the source-video reference | Must |
| FR-07 | Filter events by camera, time window, and class | Must |
| FR-08 | Generate six-hour and 24-hour summaries | Must |
| FR-09 | Support natural-language questions over indexed events | Must |
| FR-10 | Return supporting timestamps and evidence references with answers | Must |
| FR-11 | Report processing failures and incomplete coverage | Must |
| FR-12 | Export a report and event list | Should |
| FR-13 | Allow users to correct or dismiss false detections | Should |
| FR-14 | Configure custom zones and event rules | Later |

3. Critical requirement: correct time handling
A 24-hour report is only useful if its timestamps are accurate.
Every uploaded recording should capture:
- Recording start date and time, supplied by the user if the file doesn't contain reliable metadata.
- Timezone, such as America/Chicago or the relevant local timezone.
- Camera identifier and original filename.
- Video duration and analysis coverage.
- Whether the recording contains gaps or the analysis failed on any section.

The system must not assume that analysis time equals recording time. If the recording's original start time is unknown, it should label timestamps as relative to the video rather than presenting misleading clock times.
The default six-hour windows should be selectable, for example midnight–6 AM, 6 AM–noon, noon–6 PM, and 6 PM–midnight. Users must also be able to choose a custom six-hour range.

4. Recommended architecture
Keep the first implementation as a modular Python application on a single machine. It should be easy to run locally and later evolve into a service.
Recorded video files: MP4, AVI, MOV, and other verified supported formats
Video processing pipeline: OpenCV / FFmpeg → frame sampling → local YOLO inference
Event database: SQLite initially; PostgreSQL if needed later
Evidence storage: Local folders for frames, clips, and reports
Event query and summary service: Time-window filters, counts, chronological event lists
Local AI assistant and web dashboard: Natural-language questions, summaries, evidence links, and processing status

Technology choices:
- Backend API: Python + FastAPI — Fast to build and test
- Video processing: OpenCV, FFmpeg — Read video, sample frames, extract evidence
- Object detection: YOLO-family model — Local detection of supported classes
- Database: SQLite — Minimal setup for a single-user prototype
- Evidence storage: Local filesystem — Simple, transparent, offline-capable
- AI assistant: Ollama-compatible local LLM endpoint, optional — Natural-language responses without mandatory cloud processing
- Frontend: Simple React dashboard or server-rendered UI — Upload, timeline, summaries, and chat
- Deployment: One Python environment or Docker Compose — Reproducible local installation

Use the AI assistant to interpret a question, retrieve the relevant event records, and turn them into a readable answer. Do not send the entire 24-hour video to an LLM. That would be expensive, slow, and unnecessary for the first version.

5. Data model
The initial database needs only four primary entities.

Video: id, camera_id, filename, stored_path, recording_start, timezone, duration_seconds, analysis_status, coverage

Detection: id, video_id, timestamp_seconds, timestamp_utc, class_name, confidence, bounding_box, frame_reference

Event: id, video_id, camera_id, event_type, start_time, end_time, observation_count, max_confidence, evidence_reference, review_status

Report: id, period_start, period_end, camera_filter, summary_text, event_ids, created_at, model_version

Store source recordings separately from evidence. A practical folder layout could be:

```
data/
  recordings/
    camera-01/
      2026-10-24-recording.mp4
  evidence/
    camera-01/
      2026-10-24/
        event-0001.jpg
        event-0002.jpg
  reports/
    2026-10-24/
      summary-0000-0600.json
      summary-24h.json
  cctv_intelligence.sqlite3
```

The folder date should reflect the recording date, not the date the analysis happened. Evidence records should include the original video ID and time offset so a later version can generate short video clips around an event.

6. AI assistant requirements
The assistant is a key product feature, so treat its behavior as an explicit requirement—not simply an LLM API call.
It must:
- Understand questions about a defined recording period and camera.
- Query the event database before answering.
- Summarize counts and timelines by class and time window.
- Link answers to evidence frames and, when available, clips.
- Distinguish detected objects from verified incidents.
- State when video coverage or detection data is incomplete.
- Say “I don't have enough evidence to determine that” when the question goes beyond stored observations.
- Avoid inventing identities, intent, theft, or events that the detector did not establish.

Example questions:
- “Summarize the last 24 hours.”
- “What happened between midnight and 6 AM?”
- “At what times were people detected?”
- “How many vehicle detection events were recorded?”
- “Show animal detections from the evening window.”
- “What were the three longest detected activity events?”
- “Did anyone steal something?”

For the final question, the correct response must explain that detections alone cannot establish theft. It can provide relevant observations for a human to review.

7. API contract
The following endpoints are enough to start implementation without designing a large platform.

| Endpoint | Purpose |
| POST /videos | Upload a recording with camera ID, recording start time, and timezone |
| GET /videos/{id} | Get metadata, analysis status, and coverage |
| POST /videos/{id}/analyze | Start or retry local analysis |
| GET /events | Filter events by camera, class, and time range |
| GET /events/{id} | Retrieve one event and its evidence metadata |
| GET /evidence/{id} | Retrieve an authorized evidence image or clip |
| GET /summaries | Generate a six-hour, 24-hour, or custom-window summary |
| POST /assistant/ask | Ask a natural-language question about indexed events |
| GET /health | Check API and local processing health |

Example request to generate a report:
`GET /summaries?camera_id=camera-01&start=2026-10-24T00:00:00-05:00&end=2026-10-24T06:00:00-05:00`

Example request to the AI assistant:
```json
{
  "question": "Summarize all activity overnight and highlight animal detections.",
  "camera_ids": ["camera-01"],
  "start": "2026-10-24T18:00:00-05:00",
  "end": "2026-10-25T06:00:00-05:00"
}
```

The API should return an answer, the period analyzed, the event IDs used as evidence, and any coverage limitations. The timestamps above are examples; the application should accept explicit offsets or use the recording's configured timezone.

8. Acceptance criteria
The MVP is ready for a controlled pilot when it passes these checks.
Pilot readiness checklist:
- A user can upload a supported recording and assign a camera ID.
- The system records video duration, supplied recording start time, and timezone.
- Analysis status and errors are visible; failed jobs are not reported as complete.
- Detections include timestamps, class labels, confidence, and source-video references.
- Candidate events are stored and can be filtered by camera and time window.
- Every displayed event has an accessible evidence frame or an explicit evidence-unavailable status.
- Six-hour and 24-hour reports use the selected recording time window correctly.
- AI answers cite stored event IDs or timestamps and do not invent events.
- The system works with network access disabled after dependencies and model weights are installed.
- A test report identifies false positives, missed events, processing time, and unprocessed portions.

For detection quality, don't choose an arbitrary “95% accurate” claim. Build a manually reviewed test set and measure precision and recall separately for people, vehicles, and each animal class. Define acceptable thresholds based on the intended use and consequences of missed detections.

9. Implementation roadmap
1. Phase 1 — Upload and local detection: Build the upload API, metadata extraction, frame sampler, detector, and event database. Test on a short recording.
2. Phase 2 — Event evidence and timeline: Save evidence frames, group detections into candidate events, and create filters for camera, class, and time range.
3. Phase 3 — Six-hour and 24-hour summaries: Generate structured reports directly from event records. Validate timestamp handling and coverage before adding free-form language generation.
4. Phase 4 — Conversational AI: Connect a local LLM to the event-query layer. Add evidence-grounded responses, clear uncertainty statements, and source references.
5. Phase 5 — Pilot and reliability validation: Run a full-day recording, review false detections, measure processing time, and test operation with the network disconnected.

A focused prototype could be attempted over several weeks, but a reliable full-day analysis workflow depends on footage size, available hardware, model performance, and the time needed to fix detection and timestamp issues.

10. Definition of done for the first end-to-end demo
Use one recorded day from one camera as the first milestone. Multiple camera support should be designed into the schema, but it does not need to block the first demo.
The demo should work like this:
1. Upload a recording and enter its actual start time and timezone.
2. Run local object detection and save timestamped observations.
3. Group detections into candidate events with evidence frames.
4. Generate a six-hour report and a complete 24-hour report.
5. Ask the AI assistant questions about the recording and receive a grounded answer with evidence references.

My recommendation: implement the event database and evidence pipeline first, then summaries, then conversational AI. The talkative AI experience is the visible differentiator, but trustworthy event data is what makes it useful.
One final product distinction: the first version is an offline-capable analysis application, not yet a production-ready service. Before customer deployment, add authentication, access controls, file-size limits, safe upload handling, retention and deletion policies, backup/recovery, and proper job management.
This PRD is enough to start building the prototype without making live CCTV integration, IoT controls, or a large-scale architecture prerequisites.
