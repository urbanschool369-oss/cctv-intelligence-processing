# Author: Shekar Kaki
"""Phase 3 tests: summaries from indexed events only, coverage explicit.

Reuses the Phase 1 synthetic video (CAM-01, bus + person events,
0-4s) grouped by the Phase 2 rule, plus an empty-window case.
No YOLO run, no LLM call: summary_text is a template over counts.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient

from app.main import app, group_detections_into_events


def main():
    group_detections_into_events("b9b06a949b6e", "CAM-01")
    client = TestClient(app)
    r = client.get("/summaries", params={"camera_id": "CAM-01", "start": "0", "end": "21600"})
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["event_count"] == 2, body
    assert body["counts_by_class"] == {"bus": 1, "person": 1}, body
    assert body["observation_count"] == 25, body
    assert len(body["event_ids"]) == 2, body
    assert "candidate" in body["summary_text"].lower(), body
    assert "not user-verified" in body["summary_text"], body
    assert body["coverage"]["coverage_status"] == "covered", body
    # ISO window: recording_start 2026-06-12T18:00:00-05:00, so
    # 18:00-19:00 covers offsets 0-3600, which include both events.
    r = client.get("/summaries", params={
        "camera_id": "CAM-01",
        "start": "2026-06-12T18:00:00-05:00",
        "end": "2026-06-12T19:00:00-05:00"})
    assert r.status_code == 200 and r.json()["event_count"] == 2, r.text
    # Empty window: no events, and the text must NOT claim nothing happened.
    r = client.get("/summaries", params={"camera_id": "CAM-01", "start": "10000", "end": "20000"})
    assert r.status_code == 200, r.text
    assert r.json()["event_count"] == 0, r.json()
    assert "does NOT mean nothing happened" in r.json()["summary_text"], r.json()
    # Unknown camera: no footage coverage status.
    r = client.get("/summaries", params={"camera_id": "CAM-NOPE"})
    assert r.json()["coverage"]["coverage_status"] == "no_footage", r.json()
    print("Phase 3 tests: PASS (counts, ISO window, empty-window coverage)")


if __name__ == "__main__":
    main()
