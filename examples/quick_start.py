#!/usr/bin/env python3
"""Smoke test — init a journal and add one plant care entry."""
import tempfile
from pathlib import Path

from plantcare.storage import Book, init_book
from plantcare.room import Room
from plantcare.plant import Plant
from plantcare.care_log import CareLog

def main():
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "demo.json"
        book = init_book(path)
        room = Room(name="Living Room", light_level="bright-indirect", humidity="medium")
        book.add_room(room)
        plant = Plant(name="Monstera", species="Monstera deliciosa", room_id=room.id, acquired_date="2024-03-01")
        book.add_plant(plant)
        book.add_care_log(CareLog(
            plant_id=plant.id, action="water", performed_at="2025-06-01T08:30:00",
            notes="top inch dry", soil_moisture="dry",
        ))
        book.save()
        print("saved %d care logs to %s" % (len(book.care_logs), path))

if __name__ == "__main__":
    main()
