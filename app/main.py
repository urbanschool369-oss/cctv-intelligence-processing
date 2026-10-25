# Author: Shekar Kaki
"""CCTV Intelligence Processing MVP — Phase 1 API.

Frozen spec v0.1, Phase 1 scope only: upload a recording, extract
metadata, sample frames at 1 fps, run local YOLOv8s detection, store
timestamped detections in SQLite. No event grouping (Phase 2), no
summaries (Phase 3), no assistant (Phase 4), no UI (frontend choice
still TBD). No live CCTV, no IoT, no facial recognition.

Test-run parameter, NOT a frozen spec value: detection confidence
threshold 0.25 (the Ultralytics model default) is used for the Phase 1
test run only. The frozen spec requires thresholds to be set from
observed precision/recall; 0.25 is not approved as the product default.
"""
import json
import shutil
import uuid
from pathlib import Path

import cv2
from fastapi import FastAPI, File, Form, HTTPException, UploadFile

from .db import DB_PATH, connect, init_db

BASE = Path(__file__).resolve().parent.parent
RECORDINGS = BASE / "data" / "recordings"
EVIDENCE = BASE / "data" / "evidence"
MODEL_NAME = "yolov8s.pt"
SAMPLING_FPS = 1.0
TEST_CONFIDENCE = 0.25

app = FastAPI(title="CCTV Intelligence Processing — Phase 1")
init_db()
_model = None


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
    return {"status": "ok", "phase": 1, "model": MODEL_NAME, "sampling_fps": SAMPLING_FPS}


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
    return {"id": video_id, "analysis_status": status, "sampled_frames": sampled,
            "detections": detected, "errors": errors}
