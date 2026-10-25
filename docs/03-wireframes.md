# Wireframes — CCTV Intelligence Processing (MVP)

Source: polished PRD `docs/02-prd-polished.md` (spec source; spec freeze NOT done).
Tool: Claude desktop app, chat "Lo-fi wireframes for local CCTV", account
Shekar Pro, model Sonnet 5.5 Low. All artifacts Share = Only you (private,
not published). No real footage, faces, camera URLs, live feed, IoT, or
facial recognition. Evidence frames are grey placeholders (hi-fi: dashed
gold region box). No production code.

## Lo-fi (approved 2026-10-25, Shekar: "Lo-fi structure looks good, do hi-fi now")
1. Wireframe 1: Upload and analysis jobs
2. Wireframe 2: Event timeline and investigation
3. Wireframe 3: Event detail
4. Wireframe 4: Six-hour and 24-hour summaries
5. Wireframe 5: Evidence-grounded assistant

Lo-fi notes carried forward: stacked event detail layout, one analysis job
at a time, coverage visible on every screen.

## Hi-fi (built 2026-10-25, verified in Claude Artifacts list, all Private)
1. Hi-fi 1: Upload and analysis jobs
2. Hi-fi 2: Event timeline and investigation
3. Hi-fi 3: Event detail
4. Hi-fi 4: Six-hour and 24-hour summaries
5. Hi-fi 5: Evidence-grounded assistant

Style (Claude summary, Message 6 of 6): navy headers and primary buttons,
gold underline on the active tab, gold key actions and evidence links
("Jump to recording", "Open evidence"), darker gold links on the light
theme for readability, Source Sans 3 (system-font fallback), light/dark
mode automatic, pages are static mocks with no working buttons.
States: job badges running / queued / complete / complete with gaps /
failed; errors red; coverage gaps amber hatching; insufficient evidence
and evidence unavailable each have their own panel; coverage strip under
every page title, screens 2-5 also show gaps in their own panels.
Candidate events only: no theft/intrusion wording, no live view, no IoT,
no face recognition, no real footage.

Note: Claude's Artifacts page also says "Claude Design lives here now" —
Design projects are created as artifacts in the desktop app. The hi-fi
above was built as HTML artifacts in Chat, not as a separate Design
project; that route is available if Shekar wants a Design project next.

## Per-screen picks — APPROVED 2026-10-25, Shekar: "Hi-fi looks good, pick all 5 as approved"
- [x] Screen 1 Upload and analysis jobs: Hi-fi 1 approved
- [x] Screen 2 Event timeline and investigation: Hi-fi 2 approved
- [x] Screen 3 Event detail: Hi-fi 3 approved
- [x] Screen 4 Six-hour and 24-hour summaries: Hi-fi 4 approved
- [x] Screen 5 Evidence-grounded assistant: Hi-fi 5 approved

All 5 hi-fi screens are the approved design direction. Unpicked variants:
none — there was one hi-fi version per screen, and all 5 were picked.
Lo-fi versions remain as superseded design history in the Claude chat.

Open items Claude raised that are NOT approved yet: confidence threshold
default (Claude used 0.60 as a placeholder); clickable prototype; event /
job / coverage data model. None of these are part of the wireframe pick
until Shekar says so. Spec freeze DONE 2026-10-25 (spec/SPEC-PACKET.md,
FROZEN v0.1); build starts only on Shekar's separate word for it.
