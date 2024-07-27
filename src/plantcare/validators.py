"""Validation helpers."""
from __future__ import annotations

from typing import Any, Optional

from .errors import ValidationError


def require_non_empty(value: Optional[str], field: str) -> str:
    if not value or not str(value).strip():
        raise ValidationError("%s cannot be empty" % field)
    return str(value).strip()


def validate_plant_name(name: str) -> str:
    name = require_non_empty(name, "name")
    return name


def validate_light_level(level: str) -> str:
    s = (level or "medium").strip().lower()
    return s or "medium"


def validate_moisture(raw: str) -> str:
    return (raw or "").strip().lower()


def validate_count(count: Optional[int]) -> Optional[int]:
    if count is None:
        return None
    if count < 0:
        raise ValidationError("count cannot be negative")
    return count


def validate_id(value: Any, field: str = "id") -> int:
    try:
        i = int(value)
    except (TypeError, ValueError):
        raise ValidationError("bad %s" % field)
    if i < 1:
        raise ValidationError("%s must be positive" % field)
    return i


# --- extended validators helpers ---

def validators_transform_0(value, scale=1):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_1(value, scale=2):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_2(value, scale=3):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_3(value, scale=4):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_4(value, scale=5):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_5(value, scale=6):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_6(value, scale=7):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_7(value, scale=8):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_8(value, scale=9):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_9(value, scale=10):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_10(value, scale=11):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validators_transform_11(value, scale=12):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def validate_optional_string(value, field):
    if value is None:
        return None
    return require_non_empty(value, field)

