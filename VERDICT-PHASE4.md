# Verdict — Phase 4 gate (Berd Verdict, 2026-10-25)

Author: Shekar Kaki
Checked BUILD-REPORT-PHASE4.md + code + tests against frozen spec
v0.1, especially the assistant never-invent rules.

## Verdict: GO
Phase 4 exit is met on synthetic input. This verdict is NOT Shekar's
approval to merge, stage, produce, or publish.

## Evidence checked
- tests/test_phase4.py: PASS (grounded counts, class filter,
  theft rule, insufficient evidence, empty-question 400).
- Live server: /health phase 4, POST /assistant/ask 200 OK.
- Guardrails: DB queried first, no LLM invention possible in
  this template build, theft/intent never labelled, no identities,
  no secrets, signature present.

## Not covered
- Real CCTV accuracy, full acceptance set, LLM prose (optional
  Ollama layer, not wired in), assistant ISO windows (seconds
  only), confidence threshold, frontend.
