"""Text reports."""
from __future__ import annotations

from typing import TYPE_CHECKING

from .care_log import care_log_summary
from .stats import action_counts, plant_care_counts

if TYPE_CHECKING:
    from .storage import Book


def room_report(book: "Book", room_id: int) -> str:
    room = book.get_room(room_id)
    plants = [p for p in book.plants if p.room_id == room_id]
    lines = ["Room: %s (%s light)" % (room.name, room.light_level), "Plants: %d" % len(plants)]
    for p in plants[:50]:
        logs = [c for c in book.care_logs if c.plant_id == p.id]
        lines.append("  - %s (%d care logs)" % (p.name, len(logs)))
    return "\n".join(lines)


def summary_report(book: "Book") -> str:
    lines = [
        "plantcare summary",
        "plants: %d" % len(book.plants),
        "rooms: %d" % len(book.rooms),
        "care_logs: %d" % len(book.care_logs),
        "schedules: %d" % len(book.schedules),
    ]
    top = action_counts(book)[:5]
    if top:
        lines.append("top actions:")
        for name, cnt in top:
            lines.append("  %s (%d)" % (name, cnt))
    return "\n".join(lines)


def year_report(book: "Book", year: int) -> str:
    logs = [c for c in book.care_logs if c.performed_at.startswith(str(year))]
    return "Year %d: %d care events for %d plants" % (
        year, len(logs), len({c.plant_id for c in logs}),
    )


# --- extended reports helpers ---

def reports_transform_0(value, scale=1):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_1(value, scale=2):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_2(value, scale=3):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_3(value, scale=4):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_4(value, scale=5):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_5(value, scale=6):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_6(value, scale=7):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_7(value, scale=8):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_8(value, scale=9):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_9(value, scale=10):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_10(value, scale=11):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def reports_transform_11(value, scale=12):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def soil_report(book):
    from .soil import count_by_moisture
    tallies = count_by_moisture(book.care_logs)
    lines = ["Soil moisture breakdown:"]
    for k, v in sorted(tallies.items(), key=lambda x: -x[1]):
        lines.append("  %s: %d" % (k, v))
    return "\n".join(lines)

