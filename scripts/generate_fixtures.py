#!/usr/bin/env python3
"""Generate large JSON fixtures for plantcare tests."""
import json
import random
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "tests" / "fixtures"
PLANTS = [
    ("Monstera deliciosa", "Monstera"), ("Epipremnum aureum", "Pothos"),
    ("Sansevieria trifasciata", "Snake plant"), ("Chlorophytum comosum", "Spider plant"),
    ("Ficus lyrata", "Fiddle leaf fig"),
]

def mega_journal(years=6, events_per_year=700):
    rng = random.Random(42)
    start = date(2019, 1, 1)
    rooms, plants, care_logs = [], [], []
    rooms.append({"id": 1, "name": "Living room", "light_level": "bright", "humidity": "normal", "notes": "", "tags": []})
    rooms.append({"id": 2, "name": "Bedroom", "light_level": "low", "humidity": "dry", "notes": "", "tags": []})
    plant_ids = {}
    for i, (sci, nick) in enumerate(PLANTS, start=1):
        plants.append({
            "id": i, "name": nick, "species": sci, "room_id": rng.choice([1, 2]),
            "acquired_date": "2019-03-01", "notes": "", "tags": [],
        })
        plant_ids[nick] = i
    log_id = 0
    actions = ["water", "fertilize", "prune", "mist", "repot"]
    for y in range(years):
        for month in range(1, 13):
            for _ in range(events_per_year // 12):
                log_id += 1
                nick = rng.choice(list(plant_ids.keys()))
                d = start + timedelta(days=rng.randint(0, 365 * years))
                care_logs.append({
                    "id": log_id, "plant_id": plant_ids[nick],
                    "action": rng.choice(actions),
                    "performed_at": d.isoformat() + "T09:30:00",
                    "notes": "", "soil_moisture": rng.choice(["dry", "moist", "wet", ""]),
                    "light_note": "", "tags": [],
                })
    return {
        "schema_version": 3,
        "plants": plants, "rooms": rooms, "care_logs": care_logs,
        "schedules": [], "pots": [], "fertilizers": [], "sessions": [], "notes": [],
        "goals": [], "tags": [], "collections": [], "audit_log": [],
    }


def main():
    FIX.mkdir(parents=True, exist_ok=True)
    data = mega_journal()
    (FIX / "megaplant.json").write_text(json.dumps(data), encoding="utf-8")
    for year in range(2019, 2026):
        subset = {k: v for k, v in data.items()}
        subset["care_logs"] = [o for o in data["care_logs"] if o["performed_at"].startswith(str(year))]
        (FIX / f"plantcare-{year}.json").write_text(json.dumps(subset), encoding="utf-8")
    print("wrote megaplant + year snapshots")

if __name__ == "__main__":
    main()
