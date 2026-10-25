# BUILD REPORT — Phase 4 (evidence-grounded assistant)

Author: Shekar Kaki
Spec: frozen spec v0.1, PRD §11.2 / §14 (assistant rules).
Build started on Shekar's tap "continue next" 2026-10-25
~08:30 CT, in Mitra's VM workspace (same route note as Phases
2–3: Mac Terminal cannot be driven by Mitra, so no Mac-side
Claude Code CLI run; code is synced to GitHub for the Mac clone).

## What was built
- app/main.py: POST /assistant/ask (question, camera_ids, start,
  end). Time window filters when start/end are video-offset
  seconds; ISO windows for the assistant are not yet converted
  (open, minor — seconds windows work, ISO returns unfiltered
  by time, stated here plainly).
- Assistant queries the event DB FIRST, then answers. No LLM call
  in this build: the answer is a template over indexed events
  only, so it cannot invent identities, intent, theft, timestamps,
  counts, or evidence. Response includes answer, question,
  period_covered, event_ids, timestamps, evidence references,
  counts_by_class, and coverage limitations.
- Hard theft/intent rule: any question containing steal, theft,
  trespass, intruder, break-in, or burglar gets "Detections alone
  cannot establish theft, trespass, or intent" plus the matching
  observations for human review — never a theft label.
- No-match rule: "Insufficient evidence" when no indexed events
  match, never a fabrication. Empty question returns 400.
- GET /health now reports phase 4.
- tests/test_phase4.py: no YOLO run, no LLM call needed.

## Test runs (2026-10-25)
- tests/test_phase2.py: PASS (regression).
- tests/test_phase3.py: PASS (regression).
- tests/test_phase4.py: PASS. Generic question -> 2 events,
  bus 1, person 1, timestamps present, candidate wording.
  Person question -> person 1 only. Theft question ->
  "cannot establish theft" wording, no theft label in answer.
  Horse question -> 0 events, "insufficient evidence".
  Empty question -> 400.
- Live server (uvicorn, port 8004, stopped after test):
  /health phase 4, POST /assistant/ask 200 OK.
- Checks: py_compile ok. No secrets, no real footage, no faces.

## Phase 4 exit check
PRD Phase 4 exit (talkative assistant grounded in indexed events):
MET on synthetic input, with the template-answer limitation
above. A local LLM (Ollama-compatible, PRD optional) would add
free-form prose over the same evidence set; it is not wired in
yet, and no answer in this build comes from an LLM.

## Known limits / open items
- Template answers, not LLM prose (see above).
- Assistant ISO time windows not yet converted (seconds only).
- Confidence threshold, 24h sampling rate, frontend choice: still TBD.
- No merge, staging, production, or publish move approved or done.
- Server stopped after the test; no deployment.
