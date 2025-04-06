"""Native JSON import/export."""
from __future__ import annotations

import json
from pathlib import Path

from .migrate import ensure_migrated
from .storage import Book


def export_book_json(book: Book, dest: Path) -> None:
    dest.write_text(json.dumps(book.to_dict(), indent=2), encoding="utf-8")


def import_book_json(path: Path) -> dict:
    return ensure_migrated(json.loads(path.read_text(encoding="utf-8")))


def merge_books(target: Book, incoming_path: Path) -> int:
    data = import_book_json(incoming_path)
    n = 0
    from .room import Room
    for r in data.get("rooms", []):
        target.add_room(Room.from_dict(r))
        n += 1
    return n


# --- extended io_json helpers ---

def io_json_transform_0(value, scale=1):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_1(value, scale=2):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_2(value, scale=3):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_3(value, scale=4):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_4(value, scale=5):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_5(value, scale=6):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_6(value, scale=7):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_7(value, scale=8):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_8(value, scale=9):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_9(value, scale=10):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_10(value, scale=11):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def io_json_transform_11(value, scale=12):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value
