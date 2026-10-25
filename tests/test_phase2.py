# Author: Shekar Kaki
"""Phase 2 tests: 30s gap grouping, timeline filters, event detail, evidence.

Uses a synthetic video id (TEST-VIDEO-1) with hand-inserted detections,
so no YOLO run is needed. The synthetic video is removed at the end.
Gap rule (Shekar, 2026-10-25): gap <= 30s merges, gap > 30s splits.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient

from app.db import connect, init_db
from app.main import app, group_detections_into_events

VID = "TEST-VIDEO-1"
CAM = "CAM-TEST"


def setup():
    init_db()
    with connect() as conn:
        conn.execute("DELETE FROM events WHERE video_id=?", (VID,))
        conn.execute("DELETE FROM detections WHERE video_id=?", (VID,))
        conn.execute("DELETE FROM videos WHERE id=?", (VID,))
        conn.execute(
            "INSERT INTO videos VALUES (?,?,?,?,?,?,?,?,?)",
            (VID, CAM, "test.mp4", "/tmp/test.mp4", "2026-06-12T18:00:00-05:00",
             "America/Chicago", 100.0, "complete", json.dumps({})),
        )
        # person: 10, 12, 40 (gap 28 merges), 80 (gap 40 splits) -> 2 events
        # vehicle: 20, 25 -> 1 event
        for t, cls in [(10, "person"), (12, "person"), (40, "person"),
                       (80, "person"), (20, "vehicle"), (25, "vehicle")]:
            conn.execute(
                "INSERT INTO detections (video_id, timestamp_seconds, timestamp_utc,"
                " class_name, confidence, bounding_box, frame_reference)"
                " VALUES (?,?,?,?,?,?,?)",
                (VID, float(t), None, cls, 0.9, "[0,0,10,10]", "/tmp/frame.jpg"),
            )


def teardown():
    with connect() as conn:
        conn.execute("DELETE FROM events WHERE video_id=?", (VID,))
        conn.execute("DELETE FROM detections WHERE video_id=?", (VID,))
        conn.execute("DELETE FROM videos WHERE id=?", (VID,))


def main():
    setup()
    try:
        events = group_detections_into_events(VID, CAM)
        assert len(events) == 3, f"expected 3 events, got {len(events)}: {events}"
        person_events = sorted([e for e in events if e["event_type"] == "person"],
                               key=lambda e: e["start_seconds"])
        assert len(person_events) == 2, person_events
        assert (person_events[0]["start_seconds"], person_events[0]["end_seconds"],
                person_events[0]["observation_count"]) == (10.0, 40.0, 3), person_events[0]
        assert (person_events[1]["start_seconds"], person_events[1]["end_seconds"],
                person_events[1]["observation_count"]) == (80.0, 80.0, 1), person_events[1]
        # Idempotent regrouping.
        again = group_detections_into_events(VID, CAM)
        assert len(again) == 3, again

        client = TestClient(app)
        r = client.get("/events", params={"camera_id": CAM})
        assert r.status_code == 200 and len(r.json()) == 3, r.text
        r = client.get("/events", params={"camera_id": CAM, "class_name": "vehicle"})
        assert len(r.json()) == 1, r.text
        r = client.get("/events", params={"camera_id": CAM, "start": 50, "end": 90})
        assert len(r.json()) == 1 and r.json()[0]["event_type"] == "person", r.text
        ev_id = person_events[0]["id"]
        r = client.get(f"/events/{ev_id}")
        assert r.status_code == 200, r.text
        assert r.json()["review_status"] == "candidate", r.json()
        assert len(r.json()["detections"]) == 3, r.json()
        assert r.json()["evidence_status"] == "available", r.json()
        r = client.get("/events/EVT-DOES-NOT-EXIST")
        assert r.status_code == 404, r.text
        # Evidence file /tmp/frame.jpg does not exist -> explicit unavailable, not a crash.
        r = client.get(f"/evidence/{ev_id}")
        assert r.status_code == 404, r.text
        print("Phase 2 tests: PASS (3 events, filters, detail, evidence-unavailable)")
    finally:
        teardown()


if __name__ == "__main__":
    main()
