# NEVER-DO — CCTV Intelligence Processing MVP v0.1 (DRAFT, not frozen)

These rules override any convenience, demo pressure, or model output.
Breaking one is a spec violation, not a bug to fix quietly — stop,
report it, and wait for a new spec version + Shekar's word.

## Never, in product or in the repo
- Never connect to a live CCTV stream, RTSP URL, or camera feed.
- Never add IoT control (siren, relay, gate, or any actuator).
- Never add facial recognition or identification of individuals.
- Never label a detection or candidate event as theft, trespassing,
  intrusion, or a confirmed incident. Candidate events only.
- Never infer intent, identity, or an event that was not detected
  and stored. The assistant must say insufficient evidence instead.
- Never send the full 24-hour video to an LLM. The event DB is the
  only source for answers.
- Never mark a failed or partial job as complete.
- Never assume analysis time = recording time, or infer recording
  start from upload/analysis time. Never fabricate a UTC timestamp
  when recording start is unknown — use relative video timestamps.
- Never imply complete observation when footage or analysis is
  incomplete. Coverage gaps are shown, always.
- Never claim an accuracy figure (e.g. "95% accurate") without the
  manually reviewed test set behind it.
- Never commit secrets, API keys, camera credentials, RTSP URLs,
  real footage, faces, or personal data to the repo — even as test
  samples — unless Shekar approves a synthetic sample set.
- Never publish, deploy, or share anything publicly without Shekar's
  explicit word for that specific item (repo is private; Claude
  artifacts are Share = Only you).
- Never use client or employer names in public content, and never
  put the signature rule aside: "Shekar Kaki" on code headers,
  images, architectures, and flow diagrams Mitra builds.
- Never overwrite a delivered file. New versions are v2, v3, etc.
- Never treat a plan, a wireframe, or this DRAFT packet as frozen.
  Only Shekar's spec-freeze approval freezes it, and only a new
  version with his word changes it after that.
