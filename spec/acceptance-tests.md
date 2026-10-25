# Acceptance Tests — CCTV Intelligence Processing MVP v0.1 (DRAFT, not frozen)

Source: polished PRD §12 and §14. Every check must be demonstrated
against a real run, with the command + output recorded in the build
report. A check without evidence is NOT passed.

## PRD 10-item checklist (each = one test)
1. A supported recording uploads and is assigned a camera ID.
2. Duration, supplied recording start time, and timezone are recorded.
3. Analysis status and errors are visible; failed jobs are NOT
   reported as complete.
4. Detections include timestamps, labels, confidence scores, and
   source-video references.
5. Candidate events are stored and filterable by camera and time.
6. Every displayed event has an accessible evidence frame OR an
   explicit evidence-unavailable status.
7. Six-hour and 24-hour reports use the selected recording-time
   window correctly (test all 4 default windows + one custom window).
8. AI answers cite stored event IDs or timestamps and do not invent
   events (test: a question about a period with no events, and the
   "Did anyone steal something?" question).
9. The application works with network access disabled after
   dependencies and model weights are installed.
10. A test report identifies false positives, missed events,
    processing time, and unprocessed portions.

## Detection-quality rules (PRD §12.1 — hard)
- NO arbitrary accuracy claim (e.g. "95% accurate") without
  supporting evaluation evidence. The build report must NOT contain
  such a claim unless the test set backs it.
- Evaluation uses a MANUALLY REVIEWED test set.
- Precision and recall measured SEPARATELY for: people, vehicles,
  and EACH supported animal class.
- Confidence thresholds are set from observed performance and the
  consequences of missed vs false detections — not from the 0.60
  wireframe placeholder, which is unapproved.
- The test report documents results AND limitations.

## First end-to-end demo — definition of done (PRD §14)
All five, in order, on one recorded day from one camera:
1. Upload a recorded file, enter its actual recording start time
   and timezone when known.
2. Run local detection, save timestamped observations.
3. Group observations into candidate events, save evidence frames.
4. Generate six-hour AND full 24-hour reports.
5. Ask the assistant questions, receive grounded answers with
   supporting evidence references.
Multi-camera schema support is required; multi-camera processing is
not required for this demo.

## UI checks (from approved hi-fi wireframes)
- All 5 screens present, navy/gold style, coverage strip on every
  screen, coverage gaps shown in their own panels on screens 2–5.
- Job badges: running, queued, complete, complete with gaps, failed.
- Errors red; gaps amber hatching; insufficient-evidence and
  evidence-unavailable each have their own panel.
- No live view, no IoT controls, no face recognition, no real
  footage, no theft/intrusion wording anywhere in the UI.
- Pages are the approved design direction; working buttons are a
  build outcome, not a wireframe claim.

## Out of scope for this acceptance set (do not test for them)
Live CCTV, IoT control, facial recognition, theft/trespass/intent
classification, cloud billing/multi-tenant SaaS, complex agent
workflows, distributed architecture, authentication hardening
(PRD §15 — pre-customer work, not MVP). FR-14 zones/rules is Later.
FR-12 export and FR-13 correct/dismiss are Should — test them only
if the frozen packet includes them.
