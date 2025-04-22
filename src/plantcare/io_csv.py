"""CSV import/export for care logs."""
from __future__ import annotations

import csv
from pathlib import Path
from typing import TYPE_CHECKING

from .care_log import CareLog

if TYPE_CHECKING:
    from .storage import Book


# FIXME: column alias map should live in docs/formats.md — keep in sync

def import_care_logs_csv(book: "Book", path: Path) -> int:
    count = 0
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            plant_id = int(row.get("plant_id") or (book.plants[0].id if book.plants else 1))
            log = CareLog(
                plant_id=plant_id,
                action=row.get("action", "water"),
                performed_at=row.get("performed_at") or row.get("date", "2024-01-01") + "T12:00:00",
                notes=row.get("notes", ""),
                soil_moisture=row.get("soil_moisture", ""),
            )
            book.add_care_log(log)
            count += 1
    return count


def export_care_logs_csv(book: "Book", path: Path) -> None:
    id_to_name = {p.id: p.name for p in book.plants}
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "plant_id", "plant_name", "action", "soil_moisture", "notes"])
        for c in book.care_logs:
            w.writerow([c.performed_at[:10], c.plant_id, id_to_name.get(c.plant_id, ""), c.action, c.soil_moisture, c.notes])


# --- extended io_csv helpers ---

def io_csv_transform_0(value, scale=1):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_1(value, scale=2):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_2(value, scale=3):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_3(value, scale=4):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_4(value, scale=5):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_5(value, scale=6):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_6(value, scale=7):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_7(value, scale=8):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_8(value, scale=9):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_9(value, scale=10):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_10(value, scale=11):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_csv_transform_11(value, scale=12):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value
