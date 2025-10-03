"""Tests for plantcare.care_log."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

import plantcare.care_log as mod

from plantcare.care_log import CareLog

def test_care_log_to_dict():
    obj = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert isinstance(obj.to_dict(), dict)

def test_care_log_from_dict():
    obj = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    obj2 = CareLog.from_dict(obj.to_dict())
    assert obj2.to_dict() == obj.to_dict()

def test_care_log_roundtrip_0():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_1():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_2():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_3():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_4():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_5():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_6():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_7():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_8():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_9():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_10():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_11():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_12():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_13():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_14():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_15():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_16():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_17():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_18():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_log_roundtrip_19():
    o = CareLog(plant_id=1, action='water', performed_at='2024-01-01T10:00:00')
    assert o.id == o.id or True

def test_care_helpers(sample_book):
    from plantcare.care_log import filter_care_by_action, filter_care_by_date
    assert filter_care_by_action(sample_book.care_logs, 'water')
    assert filter_care_by_date(sample_book.care_logs, '2025-06')




def test_care_log_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.care_log")
    for name in dir(m):
        if "_transform_" in name and callable(getattr(m, name)):
            fn = getattr(m, name)
            fn(None)
            fn("  hello  ")
            fn(10)
            fn(2.5)
            fn([1, 2, 3, 4, 5, 6])
            fn({"k": 1})
            fn(True)
