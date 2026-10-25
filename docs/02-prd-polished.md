# PRD (Polished) — CCTV Intelligence Processing

Author: Shekar Kaki
Status: POLISHED VERSION RECEIVED FROM CHATGPT 2026-10-25 — NOT YET ADOPTED AS THE SPEC SOURCE. DO NOT BUILD FROM THIS FILE UNTIL SHEKAR SAYS IT REPLACES THE APPROVED ORIGINAL.

Source: Same ChatGPT thread "CCTV Intelligence Processing", Mac app, Chat mode.
Shekar approved the original PRD 2026-10-25 03:17 CT and authorized taking a
polished version if Mitra wanted it. ChatGPT Work DOCX attempt failed (pointer
only, no PRD text in its workspace; file picker did not open; paste into Work
textarea did not insert). Fallback: ChatGPT output the polished PRD as full
text in the original Chat thread, copied via Copy button, pasted into TextEdit
on his Mac, saved as /Users/skaki/Documents/cctv-chatgpt-prd-polished.txt
(26,486 bytes, 543 lines), then copied verbatim below, except this header.

IMPORTANT — READ BEFORE ADOPTING:
- The polished text itself says "Scope: Approved for specification freeze".
  That is ChatGPT's wording, NOT Shekar's spec-freeze approval. Spec freeze
  is still a separate step and has NOT happened.
- Original approved PRD remains docs/02-prd.md (14,473 bytes, 285 lines).
  This polished version is longer and restructured (16 numbered sections vs
  the original's 10 sections + top-5 list): it adds a product overview, goals
  expanded to 8, phase exit objectives, a gap-based heuristic note for event
  grouping, and clearer timestamp/storage/API wording. It claims no new MVP
  features, and the 5 features, FR-01..FR-14, stack, and non-goals match the
  original in substance — but that claim has NOT been line-checked by Shekar.
- If Shekar adopts this polished version, it becomes the spec source for
  Claude Design wireframes; if not, wireframes use the original approved PRD.

---


PRD: Local CCTV Intelligence MVP
Version 0.1 · Product Requirements Document · Scope: Approved for specification freeze
1. Product overview
1.1 Product definition
The Local CCTV Intelligence MVP is a local-first video analysis application that processes recorded CCTV footage, detects supported objects and activity, indexes candidate events, generates time-based summaries, and answers natural-language questions grounded in the indexed evidence.
The initial target domain is farms and private properties, where users need to review recorded footage to understand activity involving people, vehicles, and common animals.
The application will run on a single computer and be capable of operating offline after the required software dependencies and model weights have been installed.
1.2 Product scope
Attribute
Specification
Product type
Local-first video analysis service
Initial domain
Farms and private properties
Input
Recorded CCTV video files
Deployment
Single computer
Network requirement
No mandatory cloud services or external API calls
Initial scale
1–10 recordings/cameras
Analysis windows
6 hours and 24 hours
Primary user
Farm or property owner
Core interaction
Ask questions about recorded footage
1.3 Primary objective
Enable a property owner to upload recorded CCTV footage, analyze it locally, review detected activity, generate six-hour and 24-hour summaries, and ask questions about the footage without manually reviewing the entire recording.
The initial end-to-end demonstration will focus on a single camera and one recorded day. The data model must support multiple cameras, but multi-camera operation is not a prerequisite for the first demonstration.
2. Goals and non-goals
2.1 Goals
The MVP must:
	1	Analyze a full day of recorded CCTV footage from one camera.  
	2	Detect supported object classes, including people, vehicles, and common animals.  
	3	Store searchable detection and event metadata locally.  
	4	Preserve evidence references linking detected events to the original recording and timestamp.  
	5	Generate six-hour and 24-hour summaries for a selected recording-time window.  
	6	Answer natural-language questions using indexed event data.  
	7	Report processing failures, incomplete analysis, and video coverage gaps.  
	8	Operate without mandatory cloud services or external API calls.  
2.2 Non-goals
The following capabilities are explicitly outside the initial MVP scope:
	•	Direct integration with live CCTV streams.  
	•	Automatic siren, relay, gate, or other IoT control.  
	•	Facial recognition or identification of individuals.  
	•	Guaranteed classification of theft, trespassing, or intent.  
	•	Cloud-hosted customer management, billing, or multi-tenant SaaS.  
	•	Complex agent workflows or distributed architecture.  
The first version is a recorded-video analysis application. It is not a live surveillance platform or an automated security-response system.
3. MVP features
The MVP consists of five features.
3.1 Feature 1 — Video ingestion and analysis jobs
Objective: Allow users to upload recorded CCTV files and process them locally.
Requirements:
	•	Upload one or more video recordings.  
	•	Associate each recording with a camera ID.  
	•	Process recordings using the local video-analysis pipeline.  
	•	Track job status, progress, processing duration, errors, and completion state.  
	•	Extract available video metadata, including duration, frame rate, dimensions, and relevant timestamps.  
	•	Support common video formats, including MP4, AVI, and MOV, subject to verification in the implementation.  
	•	Display clear errors for invalid, unsupported, or unreadable files.  
	•	Report failed or incomplete processing accurately.  
The system must not mark a job as successfully completed if analysis has failed or portions of the recording remain unprocessed.
3.2 Feature 2 — Event detection and evidence indexing
Objective: Detect supported objects and organize observations into searchable candidate events.
Requirements:
	•	Run local object detection on sampled video frames.  
	•	Support people, vehicles, and common animals supported by the selected model.  
	•	Store each detection with its timestamp, object class, confidence score, camera association, and evidence reference.  
	•	Group nearby detections into candidate events using an initial gap-based heuristic.  
	•	Store candidate-event start and end times, observation counts, confidence information, and evidence references.  
	•	Preserve a reference to the original video and the corresponding video-time offset.  
	•	Make detection and event data available to the timeline, summary, and assistant features.  
A detected person, vehicle, or animal must not automatically be classified as an intruder, theft, or other confirmed incident. Detections are model observations that may require human review.
3.3 Feature 3 — Historical event timeline and investigation
Objective: Enable users to review indexed activity without manually watching the complete recording.
Requirements:
	•	Browse candidate events by camera, time window, and detected object class.  
	•	Display event timestamps and relevant detection metadata.  
	•	Open the associated evidence frame.  
	•	Link each event to its source recording and timestamp.  
	•	Allow users to navigate to the corresponding time in the source recording.  
	•	Make unavailable evidence explicit rather than presenting a broken or misleading reference.  
Every displayed event must retain traceability to its source recording and video-time offset.
3.4 Feature 4 — Six-hour and 24-hour summaries
Objective: Provide concise summaries of detected activity during selected recording-time windows.
Requirements:
	•	Generate six-hour summaries.  
	•	Generate 24-hour summaries.  
	•	Support the default six-hour windows:
	◦	Midnight–6 AM  
	◦	6 AM–noon  
	◦	Noon–6 PM  
	◦	6 PM–midnight  
	•	 
	•	Support custom six-hour ranges.  
	•	Include activity counts, notable candidate events, and chronological highlights.  
	•	Include evidence references where available.  
	•	Distinguish model detections from user-verified incidents.  
	•	Indicate when video coverage or analysis is incomplete.  
Summaries must be generated from indexed detection and event data. The system must not imply complete observation of a period when the underlying footage or analysis is incomplete.
3.5 Feature 5 — Talkative, evidence-grounded AI assistant
Objective: Allow users to ask natural-language questions about indexed CCTV footage.
Requirements:
	•	Accept natural-language questions about activity during a defined time window and, where applicable, selected cameras.  
	•	Query the event database before generating an answer.  
	•	Summarize event counts and timelines by object class and time period.  
	•	Return relevant timestamps and event identifiers.  
	•	Link answers to evidence frames or clips where available.  
	•	Use a local LLM where possible, through an optional Ollama-compatible local endpoint.  
	•	Identify relevant limitations in recording coverage or analysis.  
	•	State when the indexed evidence is insufficient to answer a question.  
	•	Avoid inventing identities, intentions, or events that are not established by stored observations.  
The LLM must not be treated as a substitute for the video-processing pipeline or event database. It should interpret questions and explain retrieved evidence, not claim to have directly inspected details that were never detected or stored.
Example questions:
	•	“What happened between midnight and 6 AM?”  
	•	“How many vehicle detection events were recorded?”  
	•	“Show animal detections from the evening window.”  
	•	“What were the three longest detected activity events?”  
	•	“Did anyone steal something?”  
For a question such as “Did anyone steal something?”, the assistant must explain that object detections alone cannot establish theft and provide relevant observations for human review.
4. Functional requirements
The following requirements define the functional scope of the MVP.
ID
Requirement
Priority
FR-01
Upload video files and assign camera IDs.
Must
FR-02
Extract video duration, frame rate, dimensions, and available timestamps.
Must
FR-03
Sample frames and run local object detection.
Must
FR-04
Store timestamped detections and confidence scores.
Must
FR-05
Group detections into candidate events.
Must
FR-06
Save evidence frames and source-video references.
Must
FR-07
Filter events by camera, time window, and object class.
Must
FR-08
Generate six-hour and 24-hour summaries.
Must
FR-09
Support natural-language questions over indexed events.
Must
FR-10
Return supporting timestamps and evidence references with answers.
Must
FR-11
Report processing failures and incomplete coverage.
Must
FR-12
Export reports and event lists.
Should
FR-13
Allow users to correct or dismiss false detections.
Should
FR-14
Configure custom zones and event rules.
Later
The “Should” and “Later” priorities do not expand the mandatory first end-to-end demonstration beyond the approved MVP scope.
5. Time handling and recording metadata
Correct time handling is essential to reliable historical investigation.
5.1 Required metadata
For each recording, the system must retain:
	•	Camera ID.  
	•	Original filename and stored file path.  
	•	Recording start date and time, supplied by the user when reliable metadata is unavailable.  
	•	Recording timezone, such as America/Chicago or the applicable local timezone.  
	•	Video duration.  
	•	Analysis status.  
	•	Analysis coverage, including any unprocessed sections or known gaps.  
5.2 Timestamp rules
	•	Do not assume that the analysis time is the recording time.  
	•	Do not infer a recording start time from the time at which the file is uploaded or analyzed.  
	•	When a reliable recording start time is available, derive displayed clock times from the recording start time, video offset, and configured timezone.  
	•	When the recording start time is unknown, display relative video timestamps rather than misleading clock times.  
	•	Preserve timestamp offsets and timezone information consistently throughout event indexing, summaries, and assistant queries.  
	•	Report coverage gaps and analysis failures so users can distinguish an uneventful period from a period with missing or incomplete data.  
5.3 Default analysis windows
The default six-hour windows are:
Window
Recording-time range
1
12:00 AM–6:00 AM
2
6:00 AM–12:00 PM
3
12:00 PM–6:00 PM
4
6:00 PM–12:00 AM
Users must also be able to select custom six-hour ranges and 24-hour periods.
6. Architecture
6.1 Architectural principles
	•	Local-first processing and storage.  
	•	Offline operation after dependencies and model weights are installed.  
	•	A single-computer deployment for the MVP.  
	•	Clear separation between video processing, event storage, querying, and answer generation.  
	•	Evidence traceability from each displayed event or answer to the original recording.  
	•	No mandatory external AI service or cloud dependency.  
6.2 Processing flow
Recorded CCTV files
MP4, AVI, MOV, and other verified supported formats
Video metadata and frame extraction
OpenCV / FFmpeg
Local object detection
YOLO-family model and sampled frames
Detection and candidate-event indexing
SQLite metadata and local evidence files
Timeline and reports
Six-hour and 24-hour summaries
AI assistant
Answers grounded in indexed events
6.3 Component responsibilities
Video ingestion and processing
	•	Accept uploaded recordings.  
	•	Extract metadata and sample frames.  
	•	Run local object detection.  
	•	Record processing status, failures, and coverage.  
Event query and summary service
	•	Query detections and candidate events.  
	•	Filter by camera, object class, and recording-time window.  
	•	Calculate counts and produce chronological event lists.  
	•	Assemble structured data for summaries and assistant responses.  
Database and evidence storage
	•	Store video metadata, detections, candidate events, and reports.  
	•	Store evidence frames on the local filesystem.  
	•	Maintain references connecting events to their source recordings and offsets.  
AI assistant
	•	Interpret user questions.  
	•	Retrieve relevant indexed event data.  
	•	Generate evidence-grounded explanations.  
	•	Return source references and communicate uncertainty or coverage limitations.  
User interface
- Provide a simple local interface for uploading recordings, reviewing processing status, browsing events, viewing summaries, and asking questions.
7. Technology choices
Component
Approved technology direction
API
Python + FastAPI
Video processing
OpenCV / FFmpeg
Object detection
YOLO-family model
Database
SQLite initially
Evidence storage
Local filesystem
AI assistant
Optional local LLM through an Ollama-compatible endpoint
Frontend
Simple React dashboard or server-rendered UI
Deployment
Single Python environment or Docker Compose
The initial implementation should favor the simplest workable setup. PostgreSQL may be considered later if required; it is not mandatory for the initial MVP.
The selected object-detection model must be verified to support the object classes required by the application.
8. Data model
The data model must preserve relationships between recordings, detections, candidate events, evidence, and reports.
8.1 Video
Represents an uploaded CCTV recording.
Field
Description
id
Unique video identifier
camera_id
Associated camera identifier
filename
Original filename
stored_path
Local path to the stored recording
recording_start
Recording start date and time, when known
timezone
Configured recording timezone
duration_seconds
Recording duration
analysis_status
Current analysis status
coverage
Analysis coverage and known gaps
8.2 Detection
Represents an individual object-detection observation.
Field
Description
id
Unique detection identifier
video_id
Source recording identifier
timestamp_seconds
Time offset within the recording
timestamp_utc
UTC timestamp when a reliable recording start time is available
class_name
Detected object class
confidence
Model confidence score
bounding_box
Detected object's bounding-box coordinates
frame_reference
Reference to the associated evidence frame
When the recording's absolute start time is unknown, the relative video offset remains the authoritative timestamp. The system must not fabricate an absolute UTC timestamp.
8.3 Event
Represents a candidate event grouped from related detections.
Field
Description
id
Unique event identifier
video_id
Source recording identifier
camera_id
Associated camera identifier
event_type
Candidate event or detected activity type
start_time
Event start time or relative offset
end_time
Event end time or relative offset
observation_count
Number of associated observations
max_confidence
Highest associated detection confidence
evidence_reference
Reference to supporting evidence
review_status
Review state, where applicable
Events are candidate groupings of detections, not automatically verified security incidents.
8.4 Report
Represents a generated summary.
Field
Description
id
Unique report identifier
period_start
Start of the summarized period
period_end
End of the summarized period
camera_filter
Camera selection used for the report
summary_text
Generated summary text
event_ids
Event identifiers included in the report
created_at
Report creation time
model_version
Model version used, where applicable
Reports must preserve their relationship to the selected period and the event records used to generate them.
9. Local storage layout
The following folder layout defines the intended organization of recordings, evidence, reports, and the initial database.
data/
├── recordings/
│   └── camera-01/
│       └── 2026-10-24-recording.mp4
├── evidence/
│   └── camera-01/
│       └── 2026-10-24/
│           ├── event-0001.jpg
│           └── event-0002.jpg
├── reports/
│   └── 2026-10-24/
│       ├── summary-0000-0600.json
│       └── summary-24h.json
└── cctv_intelligence.sqlite3
Storage requirements:
	•	Recording files must be retained at stable local paths.  
	•	Evidence frames must be associated with their source video and time offset.  
	•	Report files must reflect the period summarized.  
	•	The folder date must represent the recording date, not the analysis date.  
	•	Evidence metadata must retain sufficient source references for a later implementation to generate short clips from the original recording.  
10. AI assistant requirements
The assistant is a natural-language interface over indexed video-analysis results.
10.1 Query behavior
The assistant must:
	•	Interpret questions involving defined periods and, where applicable, camera selection.  
	•	Query the event database before generating answers.  
	•	Summarize counts and timelines by object class and time.  
	•	Return relevant event identifiers and timestamps.  
	•	Link to evidence frames or clips when available.  
	•	State when the underlying recording or analysis coverage is incomplete.  
	•	Say when the indexed evidence is insufficient to answer a question.  
10.2 Grounding and limitations
The assistant must distinguish between:
	•	A model detection.  
	•	A candidate event grouped from detections.  
	•	An incident verified by a user.  
It must not claim that theft, trespassing, or malicious intent occurred solely because a person, vehicle, or animal was detected.
It must not invent identities, events, timestamps, counts, or evidence references. Where the database does not contain enough information, it must clearly communicate that limitation.
10.3 Local execution
The assistant should use a local LLM through an Ollama-compatible endpoint where available.
The event database remains the source of truth for indexed observations. The application must not send entire 24-hour recordings to the LLM to answer questions about indexed activity.
11. API contract
The API must expose the following endpoints.
Method
Endpoint
Purpose
POST
/videos
Upload a recording with camera ID, recording start time, and timezone
GET
/videos/{id}
Retrieve video metadata, analysis status, and coverage
POST
/videos/{id}/analyze
Start or retry local analysis
GET
/events
Retrieve events filtered by camera, class, and time
GET
/events/{id}
Retrieve event details and evidence metadata
GET
/evidence/{id}
Retrieve an evidence image or clip
GET
/summaries
Generate or retrieve a six-hour, 24-hour, or custom-window summary
POST
/assistant/ask
Ask a natural-language question about indexed footage
GET
/health
Check API and local processing health
11.1 Summary request example
GET /summaries?camera_id=camera-01&start=2026-10-24T00:00:00-05:00&end=2026-10-24T06:00:00-05:00
The service must use the requested recording-time window and return the corresponding summary and relevant coverage information.
11.2 Assistant request example
POST /assistant/ask
Content-Type: application/json
{
  "question": "Summarize all activity overnight and highlight animal detections.",
  "camera_ids": ["camera-01"],
  "start": "2026-10-24T18:00:00-05:00",
  "end": "2026-10-25T06:00:00-05:00"
}
11.3 Assistant response requirements
The response must include:
	•	The generated answer.  
	•	The period covered by the answer.  
	•	The event IDs used as supporting evidence.  
	•	Relevant timestamps and evidence references, where available.  
	•	Coverage limitations or other relevant uncertainty.  
11.4 Timestamp handling
	•	Accept timestamps containing explicit UTC offsets or timestamps interpreted using the configured recording timezone.  
	•	Apply the same time-handling rules to filtering, summaries, and assistant queries.  
	•	Use relative video timestamps when the recording start time is unknown.  
	•	Do not silently reinterpret timestamps or substitute the analysis time for the recording time.  
12. Acceptance criteria
The MVP will be evaluated against the following acceptance criteria.
Verification checklist
0 of 10 verified
1. A supported recording can be uploaded and assigned a camera ID.
2. The system records the video duration, supplied recording start time, and timezone.
3. Analysis status and errors are visible; failed jobs are not reported as complete.
4. Detections include timestamps, labels, confidence scores, and source-video references.
5. Candidate events are stored and can be filtered by camera and time.
6. Every displayed event has an accessible evidence frame or an explicit evidence-unavailable status.
7. Six-hour and 24-hour reports use the selected recording-time window correctly.
8. AI answers cite stored event IDs or timestamps and do not invent events.
9. The application works with network access disabled after dependencies and model weights are installed.
10. A test report identifies false positives, missed events, processing time, and unprocessed portions.
12.1 Detection-quality evaluation
The MVP must not make an arbitrary accuracy claim, such as “95% accurate,” without supporting evaluation evidence.
Evaluation must use a manually reviewed test set and measure precision and recall separately for:
	•	People.  
	•	Vehicles.  
	•	Each supported animal class.  
The selected confidence thresholds should be based on observed performance and the consequences of missed detections and false positives.
The test report must document the evaluation results and identify relevant limitations.
13. Implementation roadmap
Implementation must proceed through the following phases, with each phase building on the previous one.
Phase 1 — Upload and local detection
Scope:
	•	Implement the upload API.  
	•	Extract video metadata.  
	•	Implement frame sampling.  
	•	Integrate the local object-detection model.  
	•	Store detections in the event database.  
	•	Process a short recording first.  
Exit objective: A short recording can be processed locally, with timestamped detection observations stored and associated with the source video.
Phase 2 — Event evidence and timeline
Scope:
	•	Save evidence frames.  
	•	Group related detections into candidate events.  
	•	Implement event filters.  
	•	Display candidate events with source-video references.  
Exit objective: Users can browse candidate events and trace each event to its evidence and source recording.
Phase 3 — Six-hour and 24-hour summaries
Scope:
	•	Generate structured summaries.  
	•	Implement the default six-hour windows and 24-hour summaries.  
	•	Support custom windows.  
	•	Validate timestamp handling and coverage reporting before free-form summary generation.  
Exit objective: Summaries accurately reflect the selected recording-time window, indexed events, and known coverage limitations.
Phase 4 — Conversational AI
Scope:
	•	Connect the local LLM to the event-query layer.  
	•	Retrieve relevant event records before answer generation.  
	•	Implement evidence-grounded responses.  
	•	Include timestamps, source references, and uncertainty.  
Exit objective: Users can ask natural-language questions and receive answers grounded in stored event data.
Phase 5 — Pilot and reliability validation
Scope:
	•	Process a full-day recording.  
	•	Review false detections and missed events.  
	•	Measure processing time.  
	•	Check for unprocessed sections and coverage gaps.  
	•	Verify operation with network access disabled after dependencies and model weights have been installed.  
Exit objective: The end-to-end pipeline has been exercised on a full-day recording, with documented results and limitations.
14. Definition of done: First end-to-end demonstration
The first end-to-end demonstration is complete when all five steps below work together:
	1	Upload a recorded CCTV file and enter its actual recording start time and timezone, when known.  
	2	Run local object detection and save timestamped observations.  
	3	Group observations into candidate events and save evidence frames.  
	4	Generate six-hour and full 24-hour reports.  
	5	Ask the AI assistant questions and receive grounded answers with supporting evidence references.  
The initial demonstration must start with one recorded day from one camera. The data schema must support multiple cameras, but multi-camera processing is not required to complete the first demonstration.
15. Reliability, security, and deployment considerations
The first version is an offline-capable analysis application, not a production-ready service for unrestricted customer deployment.
Before deploying it for customer use, additional hardening will be required, including:
	•	Authentication and access controls.  
	•	File-size limits and safe upload handling.  
	•	Retention and deletion policies.  
	•	Backup and recovery procedures.  
	•	Proper job management.  
These are deployment-hardening considerations, not additions to the five-feature MVP scope.
16. Final implementation direction
The implementation priority is:
	1	Build the event database and evidence pipeline first.  
	2	Add the historical event timeline and summaries.  
	3	Add the conversational AI assistant on top of the indexed event data.  
The conversational assistant is a visible differentiator, but its usefulness depends on trustworthy event data, accurate timestamps, traceable evidence, and honest reporting of coverage limitations.
The first objective is to prove the complete pipeline using a short recording, then a full day of recorded footage. The MVP must remain local-first, evidence-grounded, and limited to recorded-video analysis. No live CCTV integration, automatic IoT control, or additional product scope is introduced by this PRD.
