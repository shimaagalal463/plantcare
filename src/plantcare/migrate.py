"""Schema migrations 0 -> 1 -> 2 -> 3."""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List

from .errors import MigrationError

CURRENT_SCHEMA = 3


def migrate_v0_to_v1(data: Dict[str, Any]) -> Dict[str, Any]:
    out = deepcopy(data)
    out.setdefault("rooms", [])
    out.setdefault("plants", [])
    out.setdefault("care_logs", [])
    out.setdefault("tags", [])
    out["schema_version"] = 1
    return out


def migrate_v1_to_v2(data: Dict[str, Any]) -> Dict[str, Any]:
    out = deepcopy(data)
    out.setdefault("schedules", [])
    out.setdefault("sessions", [])
    out.setdefault("notes", [])
    out.setdefault("audit_log", [])
    out["schema_version"] = 2
    return out


def migrate_v2_to_v3(data: Dict[str, Any]) -> Dict[str, Any]:
    out = deepcopy(data)
    out.setdefault("pots", [])
    out.setdefault("fertilizers", [])
    out.setdefault("goals", [])
    out.setdefault("collections", [])
    # FIXME: old collections lived in tags — not auto-migrated
    out["schema_version"] = 3
    return out


_MIGRATORS = {0: migrate_v0_to_v1, 1: migrate_v1_to_v2, 2: migrate_v2_to_v3}


def ensure_migrated(data: Dict[str, Any]) -> Dict[str, Any]:
    cur = int(data.get("schema_version", 0))
    if cur > CURRENT_SCHEMA:
        raise MigrationError("journal newer than this plantcare (%d > %d)" % (cur, CURRENT_SCHEMA))
    while cur < CURRENT_SCHEMA:
        fn = _MIGRATORS.get(cur)
        if fn is None:
            raise MigrationError("no migrator from schema %d" % cur)
        data = fn(data)
        cur = int(data["schema_version"])
    return data


def migration_plan(data: Dict[str, Any]) -> List[int]:
    cur = int(data.get("schema_version", 0))
    steps = []
    while cur < CURRENT_SCHEMA:
        steps.append(cur)
        cur += 1
    return steps


# --- extended migrate helpers ---

def migrate_transform_0(value, scale=1):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_1(value, scale=2):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_2(value, scale=3):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_3(value, scale=4):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_4(value, scale=5):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_5(value, scale=6):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_6(value, scale=7):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_7(value, scale=8):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_8(value, scale=9):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_9(value, scale=10):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_10(value, scale=11):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def migrate_transform_11(value, scale=12):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def describe_migration(step):
    labels = {0: "proto", 1: "published", 2: "schedules", 3: "collections"}
    return labels.get(step, "unknown")

