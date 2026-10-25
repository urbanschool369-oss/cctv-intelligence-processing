# Author: Shekar Kaki
"""SQLite storage for CCTV Intelligence Processing MVP, Phases 1-2.

Tables follow frozen spec v0.1 (spec/architecture.md, PRD section 8).
Phase 1 stores Video + Detection. Phase 2 adds Event (candidate
groupings only, never verified incidents).
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "cctv_intelligence.sqlite3"


def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with connect() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS videos (
                id TEXT PRIMARY KEY,
                camera_id TEXT NOT NULL,
                filename TEXT NOT NULL,
                stored_path TEXT NOT NULL,
                recording_start TEXT,
                timezone TEXT NOT NULL,
                duration_seconds REAL,
                analysis_status TEXT NOT NULL,
                coverage TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS detections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                video_id TEXT NOT NULL REFERENCES videos(id),
                timestamp_seconds REAL NOT NULL,
                timestamp_utc TEXT,
                class_name TEXT NOT NULL,
                confidence REAL NOT NULL,
                bounding_box TEXT NOT NULL,
                frame_reference TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS events (
                id TEXT PRIMARY KEY,
                video_id TEXT NOT NULL REFERENCES videos(id),
                camera_id TEXT NOT NULL,
                event_type TEXT NOT NULL,
                start_seconds REAL NOT NULL,
                end_seconds REAL NOT NULL,
                observation_count INTEGER NOT NULL,
                max_confidence REAL NOT NULL,
                evidence_reference TEXT,
                review_status TEXT NOT NULL
            );
            """
        )
