# Author: Shekar Kaki
"""Phase 4 tests: assistant answers only from indexed events.

Uses the Phase 1 synthetic video events (CAM-01, bus + person).
No LLM call: answers are templates over the event DB.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient

from app.main import app, group_detections_into_events


def main():
    group_detections_into_events("b9b06a949b6e", "CAM-01")
    client = TestClient(app)
    # Generic question: counts + event ids + timestamps, no invention.
    r = client.post("/assistant/ask", json={"question": "What happened in this recording?"})
    assert r.status_code == 200, r.text
    body = r.json()
    assert len(body["event_ids"]) == 2, body
    assert body["counts_by_class"] == {"bus": 1, "person": 1}, body
    assert len(body["timestamps"]) == 2, body
    assert "candidate" in body["answer"].lower(), body
    # Class-filtered question.
    r = client.post("/assistant/ask", json={"question": "Show me person detections"})
    assert r.json()["counts_by_class"] == {"person": 1}, r.json()
    # Theft question: must NOT label theft, must offer observations.
    r = client.post("/assistant/ask", json={"question": "Did anyone steal something?"})
    body = r.json()
    assert "cannot establish theft" in body["answer"].lower(), body
    assert "steal" not in body["answer"].lower().replace("cannot establish theft", ""), body
    # No-match question: insufficient evidence, not a fabrication.
    r = client.post("/assistant/ask", json={"question": "Show me horse detections"})
    body = r.json()
    assert body["event_ids"] == [], body
    assert "insufficient evidence" in body["answer"].lower(), body
    # Empty question: 400.
    r = client.post("/assistant/ask", json={"question": ""})
    assert r.status_code == 400, r.text
    print("Phase 4 tests: PASS (grounded counts, theft rule, insufficient evidence)")


if __name__ == "__main__":
    main()
