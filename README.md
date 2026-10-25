# CCTV Intelligence Processing

Author: Shekar Kaki

Status: PUBLIC repo (made public by Shekar 2026-10-25).
PRE-PRODUCTION. Spec frozen v0.1, Phase 1 built and tested on
synthetic input only, Phase 2 (event evidence + timeline) pending.
No camera access, no production deploy yet.

## What this is
A service built from Shekar's existing ChatGPT thread "CCTV Intelligence Processing".
The MVP scope, top-5 features, and PRD come from that thread, via a ChatGPT question
asked in-thread on 2026-10-25. Until that PRD lands, this repo is a trace and design
scaffold only. Do not treat any feature list here as final until it is copied from
that thread and marked as source-verified in docs/.

## How work is tracked here (sequence trace)
Every step is a dated entry in `docs/00-sequence-trace.md`, in order, with:
what was done, what file or commit it produced, what was checked, and what still
needs Shekar's word. No step is backdated. No step is marked done from a plan alone.

Git history is the second trace. Each commit is one step, with a message starting
`trace:` and naming the step number, for example `trace: 003 - spec packet frozen`.

## Team model (Berd front door, Claude Code engine)
- Berd (front door): Atlas plans and gates, Scout researches, Forge writes the
  spec (PRD, architecture, API contract, acceptance tests), Verdict gates.
  Nothing publishes, merges, or deploys without Shekar's separate word per move.
- Claude Code (engine room): Lead, Architect, Backend (FastAPI, `api/` only),
  Frontend (Next.js, `web/` only), QA, Reviewer/Security, DevOps. Subagents by
  default, not Agent Teams, unless cost is approved separately.
- Full design: `~/workspace/berd-workspace/design-berd-frontdoor-claude-engine.md`
- Claude Pro resources used here: Claude Design / `/design` artboards for
  wireframes before code, Claude Code skills, subagents, hooks, MCP, and plugins
  (see `docs/01-claude-design-and-skills-plan.md`). Design is approved before
  it becomes code, same gate rule as everything else.

## Repo layout (planned, not yet all built)
```
.
├── README.md
├── docs/
│   ├── 00-sequence-trace.md      # The ordered log, this project's memory
│   ├── 01-claude-design-and-skills-plan.md
│   ├── 02-prd.md                 # Filled ONLY from the ChatGPT thread, source-noted
│   ├── 03-wireframes.md          # Claude Design artboards, approved versions only
│   └── 04-architecture.md        # Filled after PRD freeze
├── design/                       # Wireframe exports and approved artboard notes
├── api/                          # FastAPI backend, created in build phase only
├── web/                          # Next.js frontend, created in build phase only
├── tests/                        # QA-owned, created in build phase only
└── deploy/                       # DevOps-owned, created in build phase only
```

## Standing rules
- Nothing merges, deploys, publishes, or sends without Shekar's explicit word
  for that item. "Draft it" means draft only.
- No secrets, API keys, camera credentials, or RTSP URLs in this repo. Env vars
  and provider settings only, named but never valued in files.
- No client or employer names in public content.
- Signature: "Shekar Kaki" on code headers, architectures, and flow diagrams.
- Phone is private. Camera footage, faces, and personal data are never committed
  to this repo, even as test samples, unless Shekar approves a synthetic sample set.
- Never overwrite a delivered file in place. Write v2, v3, and note what changed.

## Next steps, in order
1. Phase 2: event evidence + timeline, gap threshold 30 seconds
   (see spec/phase2-decisions.md and PHASE2-CLAUDE-BRIEF.md).
2. Phase 2 Verdict gate, then Shekar's separate word per ship move.
3. Phases 3–4: summaries, then evidence-grounded assistant.
4. Phase 5: full 10-item acceptance set on a manually reviewed test set.

## Public-repo note
This repo is public. Nothing in it contains secrets, API keys,
camera credentials, RTSP URLs, phone numbers, email addresses,
client or employer names, real footage, or faces. Model weights
(yolov8s.pt), virtualenvs, local data, and test videos are
git-ignored and never committed. If a future file would contain
any of those, do not commit it — stop and ask Shekar first.
