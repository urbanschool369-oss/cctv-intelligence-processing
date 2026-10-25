# Author: Shekar Kaki
"""CCTV Intelligence Processing MVP — Phases 1-2 API.

Frozen spec v0.1. Phase 1: upload, 1 fps sampling, local YOLOv8s
detection, timestamped detections in SQLite. Phase 2: candidate
event grouping + timeline endpoints. No summaries (Phase 3), no
assistant (Phase 4), no UI (frontend choice still TBD). No live
CCTV, no IoT, no facial recognition.

Phase 2 decision (Shekar, 2026-10-25, spec/phase2-decisions.md):
gap threshold 30 seconds — successive detections of the same class
on the same video merge into one candidate event if the gap between
them is 30 seconds or less; over 30 seconds starts a new event.

Test-run parameter, NOT a frozen spec value: detection confidence
threshold 0.25 (the Ultralytics model default) is used for test runs
only. The frozen spec requires thresholds to be set from observed
precision/recall; 0.25 is not approved as the product default.
"""
import json
import shutil
import uuid
from pathlib import Path

import cv2
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse

from .db import DB_PATH, connect, init_db

BASE = Path(__file__).resolve().parent.parent
RECORDINGS = BASE / "data" / "recordings"
EVIDENCE = BASE / "data" / "evidence"
MODEL_NAME = "yolov8s.pt"
SAMPLING_FPS = 1.0
TEST_CONFIDENCE = 0.25
GAP_THRESHOLD_SECONDS = 30.0

app = FastAPI(title="CCTV Intelligence Processing — Phase 2")
init_db()
_model = None


def group_detections_into_events(video_id: str, camera_id: str):
    """Group a video's detections into candidate events, 30s gap rule.

    Returns the list of event dicts inserted. Idempotent: prior events
    for this video are deleted first, so regrouping the same detections
    produces the same events. Events are candidate groupings only.
    """
    with connect() as conn:
        rows = conn.execute(
            "SELECT * FROM detections WHERE video_id=? ORDER BY class_name, timestamp_seconds, id",
            (video_id,),
        ).fetchall()
        conn.execute("DELETE FROM events WHERE video_id=?", (video_id,))
        events = []
        current = None

        def flush(cur):
            if not cur:
                return
            ev_id = f"EVT-{video_id}-{cur['class_name']}-{int(cur['start_seconds'])}"
            # Disambiguate if two groups of one class start in the same second.
            base = ev_id
            n = 2
            while any(e["id"] == ev_id for e in events):
                ev_id = f"{base}-{n}"
                n += 1
            ev = {
                "id": ev_id,
                "video_id": video_id,
                "camera_id": camera_id,
                "event_type": cur["class_name"],
                "start_seconds": cur["start_seconds"],
                "end_seconds": cur["end_seconds"],
                "observation_count": cur["count"],
                "max_confidence": cur["max_conf"],
                "evidence_reference": cur["first_frame"],
                "review_status": "candidate",
            }
            events.append(ev)
            conn.execute(
                "INSERT INTO events VALUES (?,?,?,?,?,?,?,?,?,?)",
                (ev["id"], video_id, camera_id, ev["event_type"],
                 ev["start_seconds"], ev["end_seconds"], ev["observation_count"],
                 ev["max_confidence"], ev["evidence_reference"], ev["review_status"]),
            )

        for row in rows:
            t = float(row["timestamp_seconds"])
            if (current is None or current["class_name"] != row["class_name"]
                    or t - current["last_seconds"] > GAP_THRESHOLD_SECONDS):
                flush(current)
                current = {
                    "class_name": row["class_name"],
                    "start_seconds": t,
                    "end_seconds": t,
                    "last_seconds": t,
                    "count": 1,
                    "max_conf": float(row["confidence"]),
                    "first_frame": row["frame_reference"],
                }
            else:
                current["end_seconds"] = t
                current["last_seconds"] = t
                current["count"] += 1
                current["max_conf"] = max(current["max_conf"], float(row["confidence"]))
        flush(current)
        return events


def event_row(row):
    d = dict(row) if row else None
    if d:
        # Contract field names (api-contract.md) alongside seconds.
        d["start_time"] = d["start_seconds"]
        d["end_time"] = d["end_seconds"]
    return d


def get_model():
    global _model
    if _model is None:
        from ultralytics import YOLO

        _model = YOLO(MODEL_NAME)  # downloads weights on first use, local after
    return _model


def video_row(row):
    return dict(row) if row else None


@app.get("/health")
def health():
    return {"status": "ok", "phase": 2, "model": MODEL_NAME, "sampling_fps": SAMPLING_FPS,
            "gap_threshold_seconds": GAP_THRESHOLD_SECONDS}


@app.get("/events")
def list_events(camera_id: str = "", class_name: str = "", start: float = None, end: float = None):
    """Timeline: candidate events, filtered by camera, class, time window.

    start/end are video-offset seconds (relative timestamps when the
    recording start is unknown, per frozen spec timestamp rules).
    """
    query = "SELECT * FROM events WHERE 1=1"
    params = []
    if camera_id:
        query += " AND camera_id=?"
        params.append(camera_id)
    if class_name:
        query += " AND event_type=?"
        params.append(class_name)
    if start is not None:
        query += " AND end_seconds>=?"
        params.append(start)
    if end is not None:
        query += " AND start_seconds<=?"
        params.append(end)
    query += " ORDER BY start_seconds, id"
    with connect() as conn:
        rows = conn.execute(query, params).fetchall()
        return [event_row(r) for r in rows]


@app.get("/events/{event_id}")
def get_event(event_id: str):
    with connect() as conn:
        row = conn.execute("SELECT * FROM events WHERE id=?", (event_id,)).fetchone()
        if not row:
            raise HTTPException(404, "Event not found")
        ev = event_row(row)
        dets = conn.execute(
            "SELECT * FROM detections WHERE video_id=? AND class_name=? "
            "AND timestamp_seconds>=? AND timestamp_seconds<=? ORDER BY timestamp_seconds, id",
            (ev["video_id"], ev["event_type"], ev["start_seconds"], ev["end_seconds"]),
        ).fetchall()
        ev["detections"] = [dict(d) for d in dets]
        ev["evidence_status"] = "available" if ev["evidence_reference"] else "unavailable"
        return ev


@app.get("/evidence/{evidence_id}")
def get_evidence(evidence_id: str):
    """Evidence frame for an event id or a detection id (integer).

    Returns the frame image when it exists on disk; otherwise an
    explicit evidence-unavailable response — never a broken reference.
    """
    frame_path = None
    with connect() as conn:
        row = conn.execute("SELECT evidence_reference FROM events WHERE id=?", (evidence_id,)).fetchone()
        if row:
            frame_path = row["evidence_reference"]
        elif evidence_id.isdigit():
            drow = conn.execute("SELECT frame_reference FROM detections WHERE id=?", (int(evidence_id),)).fetchone()
            if drow:
                frame_path = drow["frame_reference"]
    if not frame_path or not Path(frame_path).is_file():
        raise HTTPException(404, {"evidence_status": "unavailable",
                                  "detail": "Evidence frame not available for this id"})
    return FileResponse(frame_path, media_type="image/jpeg")


@app.post("/videos")
def upload_video(
    file: UploadFile = File(...),
    camera_id: str = Form(...),
    recording_start: str = Form(""),
    timezone: str = Form("America/Chicago"),
):
    suffix = Path(file.filename).suffix.lower()
    if suffix not in {".mp4", ".avi", ".mov"}:
        raise HTTPException(400, f"Unsupported format: {suffix or '(none)'}")
    video_id = uuid.uuid4().hex[:12]
    dest_dir = RECORDINGS / camera_id
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{video_id}{suffix}"
    with dest.open("wb") as out:
        shutil.copyfileobj(file.file, out)
    cap = cv2.VideoCapture(str(dest))
    if not cap.isOpened():
        raise HTTPException(400, "Unreadable video file")
    fps = cap.get(cv2.CAP_PROP_FPS) or 0
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0
    duration = frames / fps if fps else None
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    with connect() as conn:
        conn.execute(
            "INSERT INTO videos VALUES (?,?,?,?,?,?,?,?,?)",
            (
                video_id,
                camera_id,
                file.filename,
                str(dest),
                recording_start or None,
                timezone,
                duration,
                "queued",
                json.dumps({"processed_seconds": 0, "gaps": [], "width": width, "height": height}),
            ),
        )
    return {"id": video_id, "camera_id": camera_id, "filename": file.filename,
            "duration_seconds": duration, "analysis_status": "queued"}


@app.get("/videos/{video_id}")
def get_video(video_id: str):
    with connect() as conn:
        row = conn.execute("SELECT * FROM videos WHERE id=?", (video_id,)).fetchone()
        if not row:
            raise HTTPException(404, "Video not found")
        data = video_row(row)
        data["coverage"] = json.loads(data["coverage"])
        data["detection_count"] = conn.execute(
            "SELECT COUNT(*) FROM detections WHERE video_id=?", (video_id,)
        ).fetchone()[0]
        return data


@app.post("/videos/{video_id}/analyze")
def analyze_video(video_id: str):
    with connect() as conn:
        row = conn.execute("SELECT * FROM videos WHERE id=?", (video_id,)).fetchone()
        if not row:
            raise HTTPException(404, "Video not found")
        conn.execute("UPDATE videos SET analysis_status='running' WHERE id=?", (video_id,))
    model = get_model()
    cap = cv2.VideoCapture(row["stored_path"])
    src_fps = cap.get(cv2.CAP_PROP_FPS) or 30
    step = max(1, round(src_fps / SAMPLING_FPS))
    ev_dir = EVIDENCE / row["camera_id"] / video_id
    ev_dir.mkdir(parents=True, exist_ok=True)
    idx = 0
    sampled = 0
    detected = 0
    errors = []
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if idx % step == 0:
                t = idx / src_fps
                results = model(frame, conf=TEST_CONFIDENCE, verbose=False)
                for box in results[0].boxes:
                    cls = model.names[int(box.cls[0])]
                    conf = float(box.conf[0])
                    x1, y1, x2, y2 = (float(v) for v in box.xyxy[0])
                    frame_path = ev_dir / f"frame-{sampled:04d}.jpg"
                    cv2.imwrite(str(frame_path), frame)
                    with connect() as conn:
                        conn.execute(
                            "INSERT INTO detections "
                            "(video_id, timestamp_seconds, timestamp_utc, class_name,"
                            " confidence, bounding_box, frame_reference) VALUES (?,?,?,?,?,?,?)",
                            (video_id, t, None, cls, conf,
                             json.dumps([x1, y1, x2, y2]), str(frame_path)),
                        )
                    detected += 1
                sampled += 1
            idx += 1
    except Exception as exc:  # never report a failed job as complete
        errors.append(str(exc))
    finally:
        cap.release()
    status = "failed" if errors else "complete"
    coverage = {"processed_seconds": sampled / SAMPLING_FPS, "sampled_frames": sampled,
                "gaps": [], "errors": errors}
    with connect() as conn:
        conn.execute(
            "UPDATE videos SET analysis_status=?, coverage=? WHERE id=?",
            (status, json.dumps(coverage), video_id),
        )
    events = []
    if status == "complete":
        events = group_detections_into_events(video_id, row["camera_id"])
    return {"id": video_id, "analysis_status": status, "sampled_frames": sampled,
            "detections": detected, "events": len(events), "errors": errors}
