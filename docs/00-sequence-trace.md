# Sequence Trace — CCTV Intelligence Processing

Author: Shekar Kaki
Rule: one entry per step, in order, never backdated, never marked done from a plan alone.
Each entry: date/time CT, what, evidence (file / commit / link), checked, still needs Shekar's word.

## 001 — 2026-10-25, ~02:57 CT — Design approved to start
- What: Shekar approved "Design Berd as front door, Claude Code as engine" and then
  asked to track everything as a sequence trace in a GitHub repo, use Claude Pro
  design mode for wireframes before code, use Claude skills and other capabilities,
  and work on "CCTV Intelligence Processing" from his ChatGPT thread.
- Evidence: design doc at `~/workspace/berd-workspace/design-berd-frontdoor-claude-engine.md`.
- Checked: Berd team exists (Atlas, Scout, Scribe, Forge, Lens, Verdict, Bridge, Goose/NVIDIA).
- Still needs: ChatGPT thread result, PRD approval, repo name/visibility confirmation (see 003).

## 002 — 2026-10-25, ~02:57 CT — ChatGPT thread lookup started
- What: Browser task started to open ChatGPT, find the thread "CCTV Intelligence Processing",
  read it in full, and, only if the thread does not already give a clear top-5 MVP list
  plus PRD/requirements, post one question in that same thread asking for top-5 MVP
  features and a PRD/requirements enough to start building.
- Evidence: browser task accepted (result arrives as a handoff, not polled).
- Checked: User has ChatGPT Pro subscription (stated 2026-10-25). No CCTV material found
  in local workspace by grep, so the thread is the sole source for scope until PRD lands.
- Still needs: thread summary, top-5 list, PRD. Do not invent features before this lands.

## 003 — 2026-10-25, ~02:57 CT — GitHub connection checked, repo NOT yet created
- What: GitHub MCP status checked. Connected, authenticated.
- Evidence: `get_me` returned login `urbanschool369-oss`, not `shekar369` personal.
  That account currently has 2 repos: `ai-school-369-projects` (public) and
  `urbanschool369-site` (private). No CCTV repo exists there.
- Checked: No CCTV repo to reuse. Proposed new repo: `urbanschool369-oss/cctv-intelligence-processing`, PRIVATE
  initially (business/service asset, same pattern as urbanschool369-site private),
  flippable to public later on his word.

## 003b — 2026-10-25, 03:00 CT — Repo account/visibility CONFIRMED by Shekar
- What: Shekar tapped "Create it private under urbanschool369-oss".
- Evidence: options widget choice in this chat, 2026-10-25 03:00 CT.
- Action: Create private repo `urbanschool369-oss/cctv-intelligence-processing`
  with autoInit off, then push README + trace + Claude plan as trace commit 001.
  ChatGPT sign-in is still pending separately (browser task waiting on secure entry
  card); that does not block repo creation, but it does block PRD step 004.
- Still needs: ChatGPT PRD (step 004), then PRD approval, wireframes, spec freeze.

## 003c — 2026-10-25, 03:00 CT — GitHub MCP repo creation FAILED, browser fallback started
- What: create_repository via GitHub MCP was approved by Shekar, then failed:
  user/repos returned 403 "Resource not accessible by integration".
  A second attempt with organization=urbanschool369-oss returned 404, confirming
  urbanschool369-oss is a user account, not an org, and the GitHub App integration
  does not have repo-creation permission for it.
- Action: Same fallback that worked for urbanschool369-site on 2026-10-23: a new
  browser task to create the private repo via github.com web UI and upload
  README.md, docs/00-sequence-trace.md, docs/01-claude-design-and-skills-plan.md,
  docs/02-prd.md, and .gitignore, with commit message starting "trace: 001 -".
- Still needs: browser task result with repo URL, visibility confirmation, and
  file/commit verification. Do not report the repo as created until that verification lands.

## 003d — 2026-10-25, 03:03 CT — ChatGPT route CHANGED by Shekar: Mac app, no full account
- What: Shekar said: use the opened ChatGPT app here on his Mac, he wants to monitor
  how Mitra is doing, and he does NOT want to give full account access.
- Action: Browser ChatGPT task (browser-task:13587f06) CLOSED and stopped. No login
  card asked again, no password requested in chat. GitHub browser task left running, untouched.
- Action: Mac computer-use session started (session cc-30, preview visible to Shekar).
  ChatGPT app on his MacBook Pro opened in background control, window already on
  "CCTV Intelligence Processing" (bundle com.openai.codex). Thread fragments seen so far:
  no CCTV integration for now, feed 1 day of CCTV record from at least one or multiple
  cameras, analyse to provide 6-hour window summaries or complete 24-hour window summary,
  stating all events, actions, major summaries; AI layer integration is the major emphasis,
  talkative summaries on request for the total 24-hour feed. ChatGPT fragment seen:
  recommend scoping as a prototype first, not a full product build, simplest next step
  process one day's footage locally, detect people and vehicles, plus one animal class.
- Still needs: full thread read (accessibility tree truncates long messages), then
  post the top-5 MVP question in that same Mac thread if not already answered, with
  Shekar monitoring via preview and able to Stop in the chat composer.

## 004 — 2026-10-25, ~03:07 CT — ChatGPT top-5 + PRD RECEIVED (Mac app, Shekar monitoring)
- Question posted in the "CCTV Intelligence Processing" thread on his Mac
  (session cc-33, on his tap) and ChatGPT replied in Chat mode. Its Work-mode
  offer for a polished PRD document was NOT taken; reply stayed in Chat.
- Full reply copied from ChatGPT, pasted into TextEdit on his Mac, saved as
  plain text at /Users/skaki/Documents/cctv-chatgpt-prd.txt (14,473 bytes),
  then copied verbatim into docs/02-prd.md in this repo scaffold.
- Top 5 (ChatGPT v0.1, local-first, farms/private properties, 1 computer offline):
  1) video ingestion + analysis jobs; 2) event detection + evidence indexing
  (people, vehicles, common animals, no theft/intrusion labelling from appearance
  alone); 3) historical event timeline + investigation; 4) 6-hour + 24-hour
  summaries; 5) talkative, evidence-grounded AI assistant (local LLM where possible).
- Stack in PRD: Python + FastAPI, OpenCV/FFmpeg, YOLO, SQLite, local filesystem,
  Ollama-compatible LLM, simple React or server-rendered dashboard, Docker Compose.
  NOT in MVP: live CCTV integration, IoT controls, facial recognition, theft/intent
  classification, cloud billing/multi-tenant SaaS, large distributed architecture.
- Status: RECEIVED, NOT YET APPROVED BY SHEKAR. No building from it until he approves.
  Next: Shekar approves PRD (or names fixes) → Claude Design wireframes → spec freeze.

## 004b — 2026-10-25, 03:15 CT — GitHub repo VERIFIED CREATED + ALL FILES IN PLACE
- Repo: https://github.com/urbanschool369-oss/cctv-intelligence-processing
  PRIVATE, owner urbanschool369-oss, created empty (no GitHub README/.gitignore/license).
- Files opened + confirmed on GitHub: README.md, docs/00-sequence-trace.md
  (incl. 003d, 004), docs/01-claude-design-and-skills-plan.md,
  docs/02-prd.md (full ChatGPT PRD, NOT YET APPROVED), .gitignore (12 lines).
- Commits, all direct to main, all starting "trace: 001 -":
  cc6223c initial trace files; 36abeab move design plan into docs/;
  aecb745 add docs/00-sequence-trace.md (updated incl. 003d, 004);
  7e2e45e add docs/02-prd.md (ChatGPT PRD, not yet approved).
- No secrets/camera credentials/RTSP URLs, no collaborators, no other repo touched.
- Note: this 004b entry itself is recorded locally after verification; syncing it
  to GitHub is a follow-up commit, not yet done.

## 005 — 2026-10-25, 03:17 CT — PRD APPROVED by Shekar + polished version authorized
- Shekar approved the PRD (docs/02-prd.md, ChatGPT v0.1 received 03:07 CT).
- He also confirmed the GitHub repo himself by logging into GitHub in his Mac
  local browser (matches the 03:15 CT browser-task verification).
- He said: if Mitra wants a polished version from ChatGPT, take it.
  Interpretation recorded: take the polished version, save it SEPARATELY
  (docs/02-prd-polished.md), leave the approved original untouched, and bring
  the polished version back before it becomes the spec source. No code yet.
- Next: polished PRD from ChatGPT (Mac app, same thread), then Claude Design
  wireframes, then spec freeze — each with Shekar's separate word where the
  standing rules require it.

## 006 — 2026-10-25, ~03:18-03:25 CT — Polished PRD attempt, IN PROGRESS, control paused
- ChatGPT Work ("Create Local CCTV MVP PRD") was started on Shekar's polish
  authorization, but Work said it could not create the DOCX faithfully: the
  referenced conversation exposed only a pointer, not the PRD text, and no copy
  was in its workspace. It asked for the PRD to be pasted/uploaded.
- File-upload picker in Work did not open a selectable file dialog in the
  observed window; pasting the Mac TextEdit copy into the Work textarea did
  not insert text (typing did work, paste did not). No Work document delivered.
- Fallback used: back in the original "CCTV Intelligence Processing" Chat
  thread, asked ChatGPT to output the polished PRD as full text in chat,
  same approved scope, no new features. ChatGPT IS generating that text
  (sections seen up to 15 Reliability/security/deployment, 16 Final
  implementation direction).
- PAUSED: a Mac control wait timed out (120s), leaving an unresolved input
  outcome; the device now requires a new local user submission before input
  can resume. Polished text NOT yet copied/saved. Approved original PRD
  untouched. Next on Shekar's resume word: copy polished chat response,
  save as docs/02-prd-polished.md separately, bring back diff summary,
  then Claude Design wireframes.

## 007 — 2026-10-25, ~03:26 CT — Polished PRD CAPTURED, separately, NOT yet adopted
- On Shekar's "Continue capturing the polished PRD" tap, Mac session cc-38
  resumed control. Original Chat thread polished response was finished
  (sections to 16 Final implementation direction, Copy/Regenerate present,
  no Working/Stop).
- Copied via Copy button, pasted into a new TextEdit doc, made plain text,
  saved on his Mac as /Users/skaki/Documents/cctv-chatgpt-prd-polished.txt
  (26,486 bytes, 543 lines), uploaded to VM, saved verbatim in this scaffold
  as docs/02-prd-polished.md with a header warning.
- Polished vs original: original 14,473 bytes / 285 lines, 10 sections + top-5;
  polished 16 numbered sections, expanded goals (8), phase exit objectives,
  gap-based event-grouping heuristic note. Same 5 features, FR-01..FR-14,
  stack, non-goals in substance, per ChatGPT's no-new-features instruction —
  NOT line-checked by Shekar yet.
- FLAG: polished text says "Scope: Approved for specification freeze" — that
  is ChatGPT wording, NOT Shekar's spec-freeze approval. Spec freeze NOT done.
  Original approved docs/02-prd.md untouched.
- Next: Shekar decides: adopt polished as spec source, or wireframe from
  original approved PRD — then Claude Design wireframes.

## 008 — 2026-10-25, 03:30 CT — Polished PRD ADOPTED as spec source
- Shekar tapped "Adopt the polished PRD as the spec source".
- Spec source is now docs/02-prd-polished.md (ChatGPT polished v0.1, 16 sections).
  Original approved docs/02-prd.md stays as history, untouched.
- Spec freeze still NOT done. Wireframes are pre-freeze design, not an API contract.
- CORRECTION to docs/01 plan's illustrative hi-fi list: live camera dashboard,
  alerts inbox, and camera onboarding are NOT in the polished PRD (no live CCTV,
  no IoT/alerting in MVP). Wireframe screens finalised from polished PRD are:
  (1) Upload + analysis jobs, (2) Event timeline / investigation,
  (3) Event detail with evidence frame + source jump, (4) 6-hour / 24-hour
  summaries, (5) Evidence-grounded AI assistant chat. A simple local home /
  navigation shell may tie them together, but it must NOT show a live camera feed.
- Next: Claude Design project "CCTV Intelligence Processing", lo-fi first,
  then hi-fi for those 5 screens only, Shekar picks one direction per screen,
  recorded in docs/03-wireframes.md. No code, no spec freeze yet.

## 009 — 2026-10-25, 03:32 CT — Claude route CHANGED by Shekar: Mac desktop, browser stopped
- Shekar: "I want you to use Desktop version opened in here in Mac".
- Browser Claude task (browser-task:913cd586) CLOSED and stopped. No Claude
  login card asked again. Browser Design work did NOT proceed past the login page.
- Mac session cc-39 started, preview visible. Claude desktop app found on his
  Mac (bundle com.anthropic.claudefordesktop, window 39903, 1200x800 at
  x=1536, y=1030), BUT its window returns NO accessibility content and NO
  painted content in background control, even after a wait. Chats, sign-in
  state, and Design mode cannot be seen from here yet.
- BLOCKER: needs Shekar to bring the Claude window to the front / confirm
  it is open and signed in to Claude Pro on his Mac, or confirm whether
  Design lives in that desktop app or only at claude.ai/design on the web.
  Wireframes NOT yet started in Claude.

## 010 — 2026-10-25, 03:34 CT — Claude desktop visible, wireframe prompt SENT, generating
- Shekar brought Claude window to front. Mac sessions cc-40/cc-41: Claude
  desktop now exposes its UI in background control (earlier blank window fixed
  by bringing it to front). Account shown "Shekar Pro", signed in.
- Note: desktop navigation shows Home/Code/New/Projects/Artifacts, NO separate
  "Design" button — Design canvas lives at claude.ai/design on the web, not
  as a desktop button found here. Work therefore proceeded in desktop Chat
  mode (Cowork switched off) as HTML artifacts, which is the desktop
  equivalent Shekar can view/pick from, NOT the web Design canvas.
- Prompt sent in Chat mode, Sonnet 5.5 Low, chat renamed by Claude to
  "Lo-fi wireframes for local CCTV": lo-fi, black/white/grey, 5 PRD screens
  only (Upload+jobs, Timeline, Event detail, 6h/24h summaries, Assistant chat),
  placeholder shapes/synthetic labels only, no live feed, no IoT, no facial
  recognition, no real footage/faces/URLs, no production code.
- Status at last check: Claude still streaming / "Running a command" (1m12s+),
  artifacts NOT yet visible in the observation. Mac sessions expire between
  turns, so capture of the finished artifacts is a follow-up step.
- Next: re-open Claude chat, wait for completion, open each artifact,
  record picks in docs/03-wireframes.md, bring back to Shekar for per-screen pick.

## 011 — 2026-10-25, ~03:37 CT — Lo-fi wireframes BUILT in Claude desktop (5/5)
- Claude chat "Lo-fi wireframes for local CCTV" (Sonnet 5.5 Low, Shekar Pro),
  Message 2 of 2, streaming finished, no Stop button at last check.
- Artifacts, all Share = Only you (private, not published), View/Share/Open
  buttons present in chat:
  1) Wireframe 1: Upload and analysis jobs
  2) Wireframe 2: Event timeline and investigation
  3) Wireframe 3: Event detail
  4) Wireframe 4: Six-hour and 24-hour summaries
  5) Wireframe 5: Evidence-grounded assistant (artifact panel open at check)
- Artifact content is in Claude's app, not yet exported to this repo's design/
  folder. Exporting/copying artifact HTML is a follow-up step if Shekar wants
  files in the repo; otherwise the Claude chat is the source of record for lo-fi.
- RE-CHECKED 2026-10-25 ~03:40 CT (session cc-43, on Shekar's tap "Check again"):
  all 5 still present, Share = Only you. Wireframe 1 opened: Upload and
  analysis jobs, Camera ID (required, CAM-01 synthetic label, Barn door),
  Recording start date/time (required, 2026-06-12 18:00:00), Timezone
  (required, America/Chicago), Queue for analysis. Wireframe 5 opened:
  Evidence-grounded assistant, nav 1-5, "Local only / Offline-ready /
  Recorded video only / Synthetic labels, no real footage", question
  "What happened near the barn door between 6 and 7 pm on June 12?",
  answer "from indexed events only", 1 candidate event CAM-01 18:29:10 CDT
  confidence 0.91, "Indexed so far: 3 cameras, 41 candidate events,
  5 recordings", Evidence EVT-000412, Coverage: CAM-01 whole window,
  CAM-02 not uploaded before 18:42, "This does not say what the person
  was doing", second question answered with "Insufficient evidence".
  Both are PRD-faithful (candidate events only, no intent/theft claim).
- Next: Shekar reviews lo-fi structure in Claude app (structure/flow check,
  per plan: if it does not make sense in black/white, colour will not fix it),
  then hi-fi for the same 5 screens, then one pick per screen recorded in
  docs/03-wireframes.md. No spec freeze, no build yet.

## 012 — 2026-10-25, 03:47 CT — Lo-fi APPROVED, hi-fi STARTED (not yet finished)
- Shekar tapped "Lo-fi structure looks good, do hi-fi now".
- Same Claude chat: hi-fi prompt sent for the same 5 screens as NEW HTML
  artifacts, lo-fi structure kept exactly, plus Claude's own lo-fi notes
  (stacked event detail, one analysis job at a time, coverage visible on
  every screen) and style: dark navy headers/primary buttons, gold accent
  for key actions/evidence links, clear states for progress/errors/coverage
  gaps/evidence unavailable/insufficient evidence. Placeholder/synthetic
  only; no live feed, IoT, facial recognition, real footage/faces/URLs, no code.
- Note from chat at hi-fi start: Claude's lo-fi follow-up (Message 4 of 4)
  had also asked about a confidence threshold default (it used 0.60 as a
  placeholder) and offered a clickable prototype or data model next — those
  are NOT approved; hi-fi only, no prototype/data-model build yet.
- Status at last check: Claude streaming, "Choosing accessible gold tones
  and planning linked navigation across pages", then "Running a command
  25s". Hi-fi artifacts NOT yet visible.
- Next: re-check Claude chat, verify 5 hi-fi artifacts, Shekar picks one
  direction per screen, record in docs/03-wireframes.md.

## 013 — 2026-10-25, ~03:52 CT — Hi-fi BUILT, verified 5/5 in Claude Artifacts
- Re-checked on Shekar's tap "Check the hi-fi wireframes again now"
  (session cc-46). Claude chat Message 6 of 6, hi-fi summary present.
- Artifacts list (all Private): Hi-fi 1 Upload and analysis jobs,
  Hi-fi 2 Event timeline and investigation, Hi-fi 3 Event detail,
  Hi-fi 4 Six-hour and 24-hour summaries, Hi-fi 5 Evidence-grounded
  assistant (Hi-fi 3 marked Opened, 2m ago at check).
- Style/states as recorded in docs/03-wireframes.md (new file): navy/gold,
  coverage strip every screen, job badges running/queued/complete/
  complete-with-gaps/failed, errors red, gaps amber hatching, insufficient
  evidence / evidence unavailable own panels, candidate events only,
  static mocks, no working buttons.
- Correction: Claude Artifacts page says "Claude Design lives here now" —
  Design projects are created as artifacts in the desktop app. Hi-fi was
  built as HTML artifacts in Chat, not a separate Design project.
- Next: Shekar per-screen picks, recorded in docs/03-wireframes.md, then
  spec freeze, then build. Claude's open items (0.60 confidence placeholder,
  clickable prototype, data model) are NOT approved.

## 014 — 2026-10-25, 03:54 CT — Hi-fi PICKS APPROVED (all 5)
- Shekar tapped "Hi-fi looks good, pick all 5 as approved".
- Recorded in docs/03-wireframes.md: Hi-fi 1-5 all approved as the design
  direction. No unpicked hi-fi variants (one version per screen).
- Wireframe stage COMPLETE. Spec freeze is next and needs a separate
  Shekar approval (Gate 1: PRD + architecture + API contract + acceptance
  tests, contract frozen, changes become a new version with his word).
  Build does not start before spec freeze.

## 015 — 2026-10-25, 03:55 CT — Spec freeze packet PREPARED (DRAFT, NOT FROZEN)
- Shekar tapped "Prepare the spec freeze packet for my approval".
- New folder spec/ (local only, not yet on GitHub): SPEC-PACKET.md,
  architecture.md, api-contract.md, acceptance-tests.md, never-do.md.
- Packet is faithful to polished PRD §3/§6-§14 + approved hi-fi
  wireframes; open items left TBD on purpose (exact YOLO model,
  sampling rate, gap threshold, confidence threshold — 0.60 wireframe
  placeholder explicitly NOT approved, frontend React vs
  server-rendered, export format, FR-13 UX, one-job-at-a-time confirm).
  FR-14 zones/rules Later, out of MVP demo. No code, no build.
- Next: Shekar approves this packet as the freeze, or names fixes.
  Until then it is a DRAFT and build stays blocked.

## 016 — 2026-10-25, 04:01 CT — SPEC FROZEN (v0.1)
- Shekar tapped "Freeze this packet as the spec".
- spec/SPEC-PACKET.md status changed DRAFT → FROZEN 2026-10-25.
  architecture.md, api-contract.md, acceptance-tests.md, never-do.md
  are part of the frozen packet as drafted (their DRAFT headers refer
  to pre-freeze preparation; the packet status governs).
- TBDs remain TBD, frozen as open items: exact YOLO model, sampling
  rate, gap threshold, confidence threshold, frontend choice, export
  format, FR-13 UX, one-job-at-a-time confirm. Builder must ask, not guess.
- Build NOT started by this freeze alone — starting the build is the
  next separate decision (Berd design Gate 2, Claude Code engine,
  pilot repo — none installed/created yet).

## 017 — 2026-10-25, 04:14 CT — Phase 1 BUILD STARTED (Shekar's word)
- Shekar tapped "Start Phase 1 build now", then picked "YOLOv8s, 1 fps
  sampling, API only for Phase 1".
- Environment check: Python 3.12.3, no FastAPI/OpenCV/YOLO, no Claude Code
  CLI in this VM. First venv install failed "No space left on device"
  (pip temp on 512M /tmp); retry with TMPDIR under home + --no-cache-dir
  succeeded for FastAPI + OpenCV 5.0.0.
- Code written (local workspace only, not yet on GitHub): app/main.py
  (POST /videos, GET /videos/{id}, POST /videos/{id}/analyze, GET /health;
  1 fps sampling; YOLOv8s; SQLite via app/db.py Video + Detection tables),
  app/db.py, app/__init__.py. Events/summaries/assistant deferred to
  Phases 2-4 per PRD. Test confidence 0.25 is the Ultralytics default,
  recorded as a TEST parameter only — NOT a frozen spec value.
- Status at last check: ultralytics/torch install still downloading
  (quiet pip, no output yet). Phase 1 test run NOT yet done.
- Next: finish install, download yolov8s.pt weights, run API + short
  test recording, record command/output in BUILD-REPORT.md, then Phase 1
  exit check.

## 018 — 2026-10-25, ~04:43 CT — Phase 1 TEST PASSED (synthetic input)
- ultralytics install completed ("ultralytics ok", ~25 min total).
- Test: bus-5s.mp4 (Ultralytics sample bus.jpg repeated, 5s, 30fps).
  Upload CAM-01, 2026-06-12T18:00:00-05:00, America/Chicago →
  id b9b06a949b6e, 5.0s, queued. Analyze → complete, sampled_frames 5
  (1 fps), detections 25 (1 bus + 4 persons per frame), errors [].
  SQLite stores timestamps 0.0–4.0s, e.g. t=0 bus 0.916, persons
  0.892/0.878/0.874/0.510. Coverage processed 5.0s, gaps [], errors [].
- BUILD-REPORT.md written. Phase 1 exit MET on synthetic input only —
  NOT real CCTV accuracy, NOT full acceptance set.
- Route question pending: Shekar asked 2026-10-25 if the Agents team
  dev approach is still followed. Answer given: gates + files yes,
  Berd team / Claude Code engine not yet engaged; code written directly
  by Mitra. His route choice (direct vs Berd+Claude Code) still pending.

## 019 — 2026-10-25, 04:49 CT — Route CHOSEN: Berd + Claude Code team route
- Shekar tapped "Move the build into the Berd + Claude Code team route"
  (from iOS app; Mac device offline at that time, no wake-up path).
- Setup done in VM workspace (not yet on Mac, not yet on GitHub):
  CLAUDE.md, .claude/agents/ (Architect, Backend, Frontend-not-active,
  QA, Reviewer, DevOps), .claude/settings.json (plan mode first,
  no bypassPermissions outside a container, subagents not Agent Teams).
- Berd handoff prepared: ~/workspace/berd-workspace/cctv-phase2-handoff.md
  for Atlas (Phase 1 report to gate, Phase 2 scope, Forge TBDs, Verdict
  checklist, items needing Shekar's word).
- NOT done: Claude Code CLI install/auth (needs Shekar on his Mac, Pro
  account, monitored — no full account access, no VM auth without his
  separate word). Berd agents on Mac NOT yet briefed (Mac offline).
- Next, in order: (1) Mac back online, deliver handoff to Atlas;
  (2) Shekar installs/auths Claude Code on Mac; (3) gap threshold
  decision for Phase 2 grouping; (4) Phase 2 via Claude Lead → QA →
  Reviewer → Berd Verdict. No Phase 2 code written in this setup step.

## 020 — 2026-10-25, ~06:10 CT — Berd handoff DELIVERED on Mac
- Shekar tapped "Deliver the Berd handoff on the Mac now" (iOS app).
- Written + verified on Mac: /Users/skaki/Documents/berd-workspace/
  tasks/04-cctv-phase2-handoff.md (3,084 bytes, 30 lines, read back).
- Content: Atlas brief, Phase 1 report to gate, Phase 2 scope, Forge
  TBDs (gap threshold first), Verdict checklist, items needing
  Shekar's word, plus notes: Claude binary found at
  /Users/skaki/.local/bin/claude (auth NOT verified, no sign-in by
  Mitra), and project code/config not yet on the Mac (VM + partial
  GitHub only) — project must be present on Mac before Claude Code
  there can build Phase 2, via a route Shekar approves.
- Next: Claude Code sign-in check (Shekar, monitored), gap threshold
  decision, project-on-Mac route, then Phase 2 via Claude Lead → QA →
  Reviewer → Berd Verdict. No Phase 2 code yet.

## 021 — 2026-10-25, 06:11 CT — STANDING RULE: Chat mode only on Mac
- Shekar (iOS app): "whenever you are accessing ChatGPT, Claude in my
  Mac stick to cloud chat mode don't use work mode. I wouldn't be able
  access full chat context from other devices like my mobile."
- Rule recorded in MEMORY.md: ChatGPT = Chat mode only, never Work mode;
  Claude = Chat mode only, never Cowork mode. This supersedes the single
  Work-mode attempt for the polished PRD (2026-10-25); do not use
  Work/Cowork again unless he explicitly changes the rule.
- Applies to all future Mac ChatGPT/Claude work, not just CCTV.

## 022 — PENDING — Claude auth + gap threshold + project on Mac → Phase 2
- To be filled when the browser handoff arrives: thread link, original scope summary,
  top-5 MVP features verbatim in summary, PRD/requirements, open questions.
- Then: copy to `docs/02-prd.md`, commit as `trace: 004 - PRD from ChatGPT thread`.

## 005 — PENDING — Claude Design wireframes
- To be filled after PRD approval: screens designed in Claude Design / `/design`,
  artboard variants, Shekar's pick, exports in `design/`, notes in `docs/03-wireframes.md`.
- Rule: wireframe approval is separate from code approval. No code from a wireframe
  until Shekar picks it.

## 006 — PENDING — Spec freeze and build
- To be filled after wireframe approval: PRD + architecture + API contract +
  acceptance tests frozen, then Claude Code build phase, with BUILD-REPORT.md per build.
