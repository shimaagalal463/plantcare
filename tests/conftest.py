"""Shared pytest fixtures."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from plantcare.plant import Plant
from plantcare.room import Room
from plantcare.care_log import CareLog
from plantcare.schedule import WateringSchedule
from plantcare.storage import Book, init_book


@pytest.fixture
def tmp_journal(tmp_path):
    path = tmp_path / "journal.json"
    book = init_book(path)
    return book


@pytest.fixture
def sample_book(tmp_journal):
    book = tmp_journal
    room = Room(name="Living Room", light_level="bright-indirect", humidity="medium")
    book.add_room(room)
    p1 = Plant(name="Monstera", species="Monstera deliciosa", room_id=room.id, acquired_date="2024-03-01")
    p2 = Plant(name="Pothos", species="Epipremnum aureum", room_id=room.id, acquired_date="2024-06-15")
    book.add_plant(p1)
    book.add_plant(p2)
    book.add_care_log(CareLog(
        plant_id=p1.id, action="water", performed_at="2025-06-01T08:00:00",
        notes="top inch dry", soil_moisture="dry",
    ))
    book.add_care_log(CareLog(
        plant_id=p2.id, action="mist", performed_at="2025-06-01T09:15:00",
        notes="leaves dusty", light_note="indirect",
    ))
    book.schedules.append(WateringSchedule(plant_id=p1.id, interval_days=7, last_watered="2025-05-25"))
    book.save()
    return book


@pytest.fixture
def v0_journal(tmp_path):
    path = tmp_path / "old.json"
    data = {
        "schema_version": 0,
        "rooms": [{"id": 1, "name": "Legacy Room", "light_level": "medium"}],
        "care_logs": [],
        "plants": [],
    }
    path.write_text(json.dumps(data), encoding="utf-8")
    return path
