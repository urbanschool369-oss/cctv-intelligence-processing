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

## 005 — PENDING — Claude Design wireframes after PRD approval
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
