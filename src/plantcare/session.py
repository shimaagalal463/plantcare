"""Care sessions (repotting afternoon, etc.)."""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional

from .parser import parse_datetime
from .validators import require_non_empty


@dataclass
class Session:
    name: str
    started_at: str
    room_id: Optional[int] = None
    ended_at: Optional[str] = None
    notes: str = ""
    id: int = 0

    def __post_init__(self):
        self.name = require_non_empty(self.name, "name")
        parse_datetime(self.started_at)
        if self.ended_at:
            parse_datetime(self.ended_at)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Session":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


# --- extended session helpers ---

def session_transform_0(value, scale=1):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_1(value, scale=2):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_2(value, scale=3):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_3(value, scale=4):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_4(value, scale=5):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_5(value, scale=6):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_6(value, scale=7):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_7(value, scale=8):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_8(value, scale=9):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_9(value, scale=10):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_10(value, scale=11):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def session_transform_11(value, scale=12):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value
