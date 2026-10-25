# Public-dataset pilot — VIRAT sample, use case completed end to end

Author: Shekar Kaki
Date: 2026-10-25. This pilot uses a PUBLIC dataset clip, NOT
Shekar's private footage, and NOT a farm clip. It completes the
MVP use case end to end on real surveillance video, with the
limitations below stated plainly. Footage itself is NOT committed
to the repo (data/ is git-ignored); only this report, counts, and
event IDs are recorded.

## Dataset research (public, 2026-10-25)
- VIRAT Video Dataset (viratdata.org, CVPR 2011, Oh et al.):
  stationary ground surveillance, people + vehicles, 23 event
  types, 2–30 Hz, multiple US sites. Ground data is available
  under a VIRAT Protection Agreement; the two sample MP4s on the
  homepage download directly without a form. Citation required
  if the dataset is used in a publication (see viratdata.org).
  Chosen for the pilot because it is the closest public match
  to the MVP: static camera, people walking, person+vehicle
  interactions. NOT farm footage — that gap remains.
- ShanghaiTech Campus: public surveillance, people, normal +
  anomaly, via benchmark mirrors. Good second source, campus
  not farm.
- UCF-Crime: public, but NOT used for this pilot — its anomaly
  classes (including stealing, burglary, etc.) conflict with the
  MVP never-do rule (never label theft/intent), and it has
  video-level labels only, not detection boxes.
- TSBOW traffic benchmark: public, 32h, vehicles + pedestrians,
  traffic only, not farm/private property.
- Farm animals: SideCow-VSS (921 side-view dairy cow clips,
  public), CBVD-5 (687 cow behaviour segments, 7 cameras),
  cow_plos (YOLOv8 CCTV cow behaviour, GitHub, CC-BY article).
  None was run in this pilot; they are the next source for an
  animal-class test set, once access terms are checked per source.

## Pilot clip used
- File: VIRAT_S_010204_05_000856_000890.mp4, from viratdata.org
  homepage sample links. 24.36 seconds, 1280x720, h264.
- Camera ID in MVP: CAM-VIRAT. Recording start: UNKNOWN from
  the filename alone, so the MVP used RELATIVE video timestamps
  (0.0–24.0s), per frozen spec timestamp rules — never assumed.
- Video id in MVP: 9143355fd0b1. Duration recorded: 24.363788s,
  timezone America/Chicago (upload form value, not recording
  time — recording start itself remains unknown).

## End-to-end run (commands + outputs, server port 8005, stopped after)
- POST /videos -> id 9143355fd0b1, CAM-VIRAT, queued.
- POST /videos/9143355fd0b1/analyze -> complete, sampled_frames
  25 (1 fps test rate), detections 233, events 4, errors [].
- GET /events?camera_id=CAM-VIRAT -> 4 candidate events:
  person 0.0–24.03s, 220 observations, max conf 0.911;
  potted plant 4.0–24.03s, 10 observations, max conf 0.502;
  backpack 0.0–2.00s, 2 observations, max conf 0.482;
  chair 17.02s, 1 observation, max conf 0.360.
- GET /summaries CAM-VIRAT 0–24 -> 4 events, 233 observations,
  bus 0 (this clip), person 1, potted plant 1, backpack 1,
  chair 1 (event counts, not observation counts).
- POST /assistant/ask "What happened in this recording?" ->
  grounded answer with 6 events total across both videos in DB
  (this clip + Phase 1 bus video, because no camera filter was
  passed — noted as a query-scope lesson: always pass camera_ids
  for a single-camera answer).

## Manual review (Mitra, evidence frames frame-0000 and frame-0017)
- Scene: outdoor plaza, "STUDENT SERVICES" building, many
  people walking. Frame 0 shows ~8–10 people, several with
  backpacks, and a large potted plant centre-frame — person,
  backpack, and potted plant detections are PLAUSIBLE true
  positives, and ~8.8 person detections per sampled frame
  matches the visible crowd.
- Chair event (1 observation, conf 0.360, at 17s): NO chair
  visible in frame 0017 — likely a FALSE POSITIVE (kiosk or
  other street furniture misclassified). This is the pilot's
  clearest false-positive example, and it is why the MVP keeps
  events as candidates, not verified incidents.
- Static-object lesson: potted plant is a real object but a
  STATIC one — it appears as a 20-second "event" because the
  MVP groups any repeated detection, moving or not. A future
  improvement (not in MVP scope) is motion filtering so static
  objects do not become events.
- No precision/recall numbers are claimed here: a full
  precision/recall set needs per-frame ground-truth boxes for
  this clip, which VIRAT annotations provide under the
  Protection Agreement, not from the two sample MP4s alone.
  Do NOT quote an accuracy figure from this pilot.

## 10-item checklist vs this pilot (honest status)
1. Upload + camera ID: PASS (CAM-VIRAT).
2. Duration, start, timezone recorded: PARTIAL — duration and
   timezone recorded, recording start explicitly UNKNOWN
   (relative timestamps used, correctly).
3. Status/errors visible, failed not complete: PASS, including
   the Phase 5 failed-job fix (unreadable -> failed).
4. Detections timestamped, labelled, scored, source-referenced:
   PASS (233 detections, all with video id + timestamp + box).
5. Events stored, filterable by camera/time: PASS.
6. Evidence frame or explicit unavailable: PASS (frames exist
   for all 4 events in this clip).
7. 6h/24h reports use the window correctly: PARTIAL — seconds
   and ISO windows tested on the synthetic video; this 24s clip
   is far shorter than 6h, so a true 6h window was not exercised.
8. Assistant cites event IDs/timestamps, does not invent:
   PASS for the theft and no-event tests; single-camera scope
   lesson noted above.
9. Works offline after dependencies/weights installed: NOT
   TESTED in this pilot (network was on; weights were already
   local, no cloud call is made by the code, but a disabled-
   network run is still required for a full PASS).
10. Report identifies false positives, missed events, processing
    time, unprocessed portions: PARTIAL — false positive
    (chair) identified, processing time for analyze was ~88
    seconds for 25 frames on this VM (includes model load),
    unprocessed portions none in this clip; missed events NOT
    measured (needs ground truth).

## What this completes, and what it does not
- COMPLETES: the MVP use case end to end on real surveillance
  video — upload, detect, group, timeline, summaries, assistant
  — with a public, citable source, and a manual review.
- DOES NOT complete: farm/private-property footage, animal
  classes, a true 6h/24h window, offline-disabled test, or a
  precision/recall evaluation. Those still need Shekar's real
  footage, or a VIRAT full-release agreement + annotations,
  or a farm animal dataset run.
- Confidence threshold: STILL TBD, as before. No threshold is
  set from this pilot alone.
