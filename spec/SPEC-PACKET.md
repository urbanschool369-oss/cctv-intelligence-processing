# SPEC PACKET — CCTV Intelligence Processing MVP v0.1

Author: Shekar Kaki
Status: FROZEN 2026-10-25, on Shekar's tap "Freeze this packet as the spec".
This packet is now the build contract for MVP v0.1. Changes after this
point become a new version (v0.2, etc.) with Shekar's separate approval;
this version is not edited in place. Items marked TBD in this packet
are frozen AS OPEN ITEMS — a builder must stop and ask Shekar before
filling them, not guess a value.

## Sources (in order of authority for this draft)
1. Polished PRD `docs/02-prd-polished.md` — adopted as spec source
   2026-10-25. Original approved PRD `docs/02-prd.md` remains as history.
   Where the polished PRD and this packet disagree, the packet is wrong
   until Shekar corrects it — flag it, do not silently fix the PRD.
2. Approved hi-fi wireframes `docs/03-wireframes.md` — all 5 screens
   approved 2026-10-25: Upload+jobs, Timeline, Event detail, 6h/24h
   summaries, Assistant chat. Style: navy/gold, coverage strip on every
   screen, candidate events only, static mocks (no working buttons yet).
3. Berd front-door design `~/workspace/berd-workspace/
   design-berd-frontdoor-claude-engine.md` — gates only (Gate 1 spec
   freeze, Gate 2 build, Gate 3 review, Gate 4 ship). No Berd agent
   changes, no Claude Code install, and no build have been approved yet.

## Product in one paragraph
Local-first, single-computer, offline-capable (after dependencies and
model weights are installed) analysis of RECORDED CCTV files for farms
and private properties. Upload a recording, run local object detection,
index candidate events with evidence frames, generate 6-hour and
24-hour summaries, and ask a talkative assistant questions that are
answered only from indexed events. First demo: one recorded day, one
camera. Data model must support 1–10 recordings/cameras, but
multi-camera processing is not required for the first demo.

## The 5 MVP features (PRD §3, FR-01..FR-11 Must)
1. Video ingestion + analysis jobs — upload, camera ID, metadata,
   job status/progress/errors/coverage. A failed or partial job is
   NEVER reported as complete.
2. Event detection + evidence indexing — people, vehicles, common
   animals (model-supported classes only); detections timestamped,
   classed, scored, camera-linked, evidence-referenced; nearby
   detections grouped into candidate events.
3. Historical timeline + investigation — browse by camera, time
   window, object class; evidence frame; jump to source recording
   + timestamp; evidence-unavailable stated explicitly.
4. Six-hour + 24-hour summaries — default windows midnight–6, 6–noon,
   noon–6, 6–midnight, plus custom ranges; counts, highlights,
   evidence links, coverage gaps stated; detections distinguished
   from user-verified incidents.
5. Talkative, evidence-grounded assistant — queries the event DB
   BEFORE answering; returns timestamps, event IDs, evidence links;
   states coverage limits and insufficient evidence; never invents
   identities, intent, theft, or events.

## Files in this packet
- `architecture.md` — components, processing flow, data model, storage.
- `api-contract.md` — the 9 PRD endpoints, frozen request/response
  shapes (fields marked TBD are NOT frozen until Shekar decides them).
- `acceptance-tests.md` — the 10-item PRD checklist, detection-quality
  rules, and the first-demo definition of done, as testable checks.
- `never-do.md` — explicit non-goals and hard rules that no build
  step may override without a new spec version + Shekar's word.

## Decisions this draft does NOT make (open items — Shekar's word needed)
These are left TBD on purpose, not filled with guesses:
- Exact YOLO-family model + version, and the classes it supports.
  PRD says "YOLO-family, verified to support the required classes".
- Frame sampling rate / strategy, and the gap-based event-grouping
  threshold (PRD says "initial gap-based heuristic", no seconds given).
- Confidence threshold default. Claude used 0.60 as a PLACEHOLDER in
  wireframes — that is NOT approved and NOT in this packet as a value.
  PRD says thresholds must be based on observed precision/recall.
- Frontend choice: PRD allows "simple React dashboard OR
  server-rendered UI" — one must be picked before build.
- Export format for FR-12 (Should: export reports/event lists) and
  the correct/dismiss UX for FR-13 (Should). Both are Should, not
  required for the first end-to-end demo.
- FR-14 custom zones/rules is Later — explicitly OUT of the MVP demo.
- Job queue: wireframe note "one analysis job at a time" is the
  safest default for a single offline computer, but the PRD does not
  state it as a hard rule — confirm or drop it at freeze.
- No auth, billing, multi-tenancy, or customer hardening in MVP.
  PRD §15 lists those as pre-customer-deployment work, not MVP scope.

## What "frozen" means (Gate 1 — now in effect)
The API contract, data model, timestamp rules, and acceptance tests
above are frozen for the build. A builder that finds a conflict must
stop and ask, not improvise a change. Any change after freeze is a
new packet version (v0.2, etc.) with Shekar's separate approval, and
this version is kept unchanged. Build itself has NOT yet been
authorized by this freeze alone — starting the build is the next
separate decision.
