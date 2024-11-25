"""JSON persistence — the Book."""
from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from .audit_log import AuditEntry, log_action
from .care_log import CareLog
from .errors import NotFoundError, StorageError
from .fertilizer import Fertilizer
from .goal import Goal
from .migrate import CURRENT_SCHEMA, ensure_migrated
from .note import Note
from .plant import Plant
from .pot import Pot
from .room import Room
from .schedule import WateringSchedule
from .session import Session


# HACK: id scan is fine until someone adds 10k plants — unlikely in my flat

def _next_id(items: List[Any]) -> int:
    if not items:
        return 1
    return max(getattr(x, "id", 0) for x in items) + 1


@dataclass
class Book:
    path: Path
    schema_version: int = CURRENT_SCHEMA
    plants: List[Plant] = field(default_factory=list)
    rooms: List[Room] = field(default_factory=list)
    care_logs: List[CareLog] = field(default_factory=list)
    schedules: List[WateringSchedule] = field(default_factory=list)
    pots: List[Pot] = field(default_factory=list)
    fertilizers: List[Fertilizer] = field(default_factory=list)
    sessions: List[Session] = field(default_factory=list)
    notes: List[Note] = field(default_factory=list)
    goals: List[Goal] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    collections: List[Dict[str, Any]] = field(default_factory=list)
    audit_log: List[AuditEntry] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "plants": [p.to_dict() for p in self.plants],
            "rooms": [r.to_dict() for r in self.rooms],
            "care_logs": [c.to_dict() for c in self.care_logs],
            "schedules": [s.to_dict() for s in self.schedules],
            "pots": [p.to_dict() for p in self.pots],
            "fertilizers": [f.to_dict() for f in self.fertilizers],
            "sessions": [s.to_dict() for s in self.sessions],
            "notes": [n.to_dict() for n in self.notes],
            "goals": [g.to_dict() for g in self.goals],
            "tags": list(self.tags),
            "collections": list(self.collections),
            "audit_log": [a.to_dict() for a in self.audit_log],
        }

    @classmethod
    def from_dict(cls, path: Path, data: Dict[str, Any]) -> "Book":
        book = cls(path=path)
        book.schema_version = int(data.get("schema_version", 0))
        book.plants = [Plant.from_dict(x) for x in data.get("plants", [])]
        book.rooms = [Room.from_dict(x) for x in data.get("rooms", [])]
        book.care_logs = [CareLog.from_dict(x) for x in data.get("care_logs", [])]
        book.schedules = [WateringSchedule.from_dict(x) for x in data.get("schedules", [])]
        book.pots = [Pot.from_dict(x) for x in data.get("pots", [])]
        book.fertilizers = [Fertilizer.from_dict(x) for x in data.get("fertilizers", [])]
        book.sessions = [Session.from_dict(x) for x in data.get("sessions", [])]
        book.notes = [Note.from_dict(x) for x in data.get("notes", [])]
        book.goals = [Goal.from_dict(x) for x in data.get("goals", [])]
        book.tags = list(data.get("tags", []))
        book.collections = list(data.get("collections", []))
        book.audit_log = [AuditEntry.from_dict(x) for x in data.get("audit_log", [])]
        return book

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
        fd, tmp = tempfile.mkstemp(dir=str(self.path.parent), suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                fh.write(payload)
                fh.flush()
                os.fsync(fh.fileno())
            os.replace(tmp, self.path)
        except OSError as exc:
            try:
                os.unlink(tmp)
            except OSError:
                pass
            raise StorageError("failed to write %s" % self.path) from exc
        log_action(self, "save", {"path": str(self.path)})

    @classmethod
    def load(cls, path: Path | str) -> "Book":
        p = Path(path)
        if not p.exists():
            raise StorageError("missing journal: %s" % p)
        try:
            raw = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise StorageError("invalid JSON") from exc
        data = ensure_migrated(raw)
        book = cls.from_dict(p, data)
        book.schema_version = CURRENT_SCHEMA
        return book

    def add_plant(self, plant: Plant) -> Plant:
        plant.id = _next_id(self.plants)
        self.plants.append(plant)
        log_action(self, "plant.add", {"id": plant.id})
        return plant

    def add_room(self, room: Room) -> Room:
        room.id = _next_id(self.rooms)
        self.rooms.append(room)
        log_action(self, "room.add", {"id": room.id})
        return room

    def add_care_log(self, log: CareLog) -> CareLog:
        log.id = _next_id(self.care_logs)
        self.care_logs.append(log)
        log_action(self, "care.add", {"id": log.id})
        return log

    def get_plant(self, plant_id: int) -> Plant:
        for p in self.plants:
            if p.id == plant_id:
                return p
        raise NotFoundError("plant %d not found" % plant_id)

    def get_room(self, room_id: int) -> Room:
        for r in self.rooms:
            if r.id == room_id:
                return r
        raise NotFoundError("room %d not found" % room_id)


def init_book(path: Path | str) -> Book:
    p = Path(path)
    book = Book(path=p)
    book.save()
    return book


# --- extended storage helpers ---

def storage_transform_0(value, scale=1):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_1(value, scale=2):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_2(value, scale=3):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_3(value, scale=4):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_4(value, scale=5):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_5(value, scale=6):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_6(value, scale=7):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_7(value, scale=8):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_8(value, scale=9):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_9(value, scale=10):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_10(value, scale=11):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_11(value, scale=12):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_12(value, scale=13):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_13(value, scale=14):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def storage_transform_14(value, scale=15):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def book_care_log_count(book):
    return len(book.care_logs)


def book_plant_count(book):
    return len(book.plants)


def find_care_for_plant(book, plant_id):
    return [c for c in book.care_logs if c.plant_id == plant_id]


def delete_care_log(book, log_id):
    book.care_logs = [c for c in book.care_logs if c.id != log_id]
    return book

