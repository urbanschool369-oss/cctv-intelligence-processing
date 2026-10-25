# Claude Pro — Design Mode and Skills Plan for CCTV Intelligence Processing

Author: Shekar Kaki
Status: PLAN ONLY, 2026-10-25. No Claude Design project created yet, no skill installed yet.
Sources checked 2026-10-25 are web summaries, not Anthropic's own docs in this session.
Verify in Claude / Claude Code before paying or installing anything new.

## What Shekar already has, and how we will use it
Shekar stated 2026-10-25: Claude Pro subscription, plus ChatGPT Pro subscription.
Claude Pro (per sources checked) includes Claude Code and Claude Design in research
preview, with a separate weekly usage limit for Design, independent from chat and
Claude Code usage. Pro is enough for quick explorations; Max gives significantly more.

## 1. Claude Design — pre-production picture before code
What it is, per sources checked:
- Launched 17 April 2026 as a research preview, at claude.ai/design, powered by Opus 4.7.
- Chat on the left, live canvas on the right. Describe a screen, refine in conversation.
- Exports: PDF, PowerPoint, Canva, standalone HTML, or handoff to Claude Code for a working site.
- In Claude Code, `/design` (artboards, research preview, announced 17 August 2026)
  gives several editable graphic variants side by side, not a code file right away.
  Change colour, move a block, widen a gap, and only when the draft convinces you,
  ask Claude to turn it into real code.

How we will use it for CCTV, in order, with gates:
1. After PRD approval, create a Claude Design project named "CCTV Intelligence Processing".
2. Feed it ONLY the approved PRD + brand notes (Shekar Kaki signature rule, no client names).
   No camera footage, no real faces, no real RTSP URLs as design inputs.
3. Lo-fi first: black-and-white wireframes for structure and flow. If a screen does not
   make sense in black and white, colour will not fix it.
4. Then hi-fi for the MVP screens only: live camera/event dashboard, event detail with
   clip and timeline, alerts inbox, camera onboarding, and settings/access. Exact screen
   list is finalised from the ChatGPT PRD, not guessed here.
5. Shekar picks ONE artboard direction per screen. That pick is recorded in
   `docs/03-wireframes.md` with export links/paths and date.
6. Only the picked direction goes to Claude Code for implementation. Unpicked variants
   stay in `design/` as rejected alternatives, with a note why, so we do not re-litigate them.

What Design does NOT do:
- It does not prove the video pipeline works, the detection is accurate, or the
  deployment is secure. Those are build-phase tests, not design approval.
- It does not replace the spec freeze. A pretty screen is not an API contract.

## 2. Claude Code capabilities, layered properly
Do not dump everything into CLAUDE.md. Use each mechanism for what it is for:

- CLAUDE.md (always on): stack, folder ownership, build/test commands, never-do list,
  signature rule, no secrets rule. Keep it lean.
- Skills (on demand, `.claude/skills/<name>/SKILL.md`): reusable workflows that kick in
  when relevant. Planned for CCTV:
  - `cctv-design-review`: wireframe to code checklist, accessibility, empty/error states
  - `cctv-event-review`: event, clip, and alert data checks before Verdict
  - `cctv-release`: staging checklist, rollback, and BUILD-REPORT format
- Slash commands (typed): shortcuts for repeated prompts, for example `/verdict-check`.
- Subagents (isolated context, `.claude/agents/*.md`): Lead, Architect, Backend, Frontend,
  QA, Reviewer/Security, DevOps, as in the Berd front-door design. Use for work that
  would flood the main context, like code review or deep file scans.
- Hooks (deterministic, `settings.json`): formatter/linter after edits, test gate before
  commit, block writes to production config or secrets files. Hooks are guarantees,
  CLAUDE.md is advisory. Never use bypassPermissions outside an isolated container.
- MCP (external tools, `.mcp.json`): only the servers actually needed, narrowest scope
  first, for example GitHub and database. Prove each server removes a real context switch
  before adding another.
- Plugins (bundles, `/plugin`): one install can bring skills, subagents, hooks, and MCP
  servers together. Candidates to evaluate in the pilot, not install blindly:
  - Anthropic official `frontend-design` skill: commits to an aesthetic direction, type
    system, colour, and motion before writing UI, instead of AI-default styling.
  - `ui-ux-pro-max`: design judgement, visual hierarchy, spacing, and a full design system
    from a rough brief. Third-party, so review its permissions before installing.
- Agent Teams (experimental, peers sharing a task list): NOT default. Subagents first.
  Agent Teams only if subagents genuinely need to message each other, with cost approved.

## 3. Claude + ChatGPT, kept separate
- ChatGPT Pro thread is the SOURCE for the idea and PRD. It stays the source of truth
  for scope until the PRD is copied and frozen here.
- Claude Pro is the DESIGN and BUILD surface. It does not overwrite the ChatGPT thread.
- Any answer ChatGPT gives on top-5 MVP features is copied into `docs/02-prd.md` with
  source, date, and thread link, then reviewed by Berd Forge/Verdict, then approved by
  Shekar. It is not treated as approved just because ChatGPT wrote it.

## 4. Order of work, no shortcuts
1. ChatGPT PRD lands and is copied here.
2. Shekar approves PRD.
3. Claude Design wireframes, Shekar picks direction.
4. Spec freeze: PRD + architecture + API contract + acceptance tests.
5. Claude Code build, with skills, subagents, hooks, and MCP as above.
6. Verdict gate, then Shekar word per merge / staging / production move.
