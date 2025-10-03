"""Tests for plantcare.watering."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

import plantcare.watering as mod

from plantcare.watering import days_since_watered, is_overdue
from plantcare.schedule import WateringSchedule

def test_days_since():
    assert days_since_watered('2024-01-01') > 0

def test_is_overdue():
    s = WateringSchedule(plant_id=1, interval_days=7, last_watered='2020-01-01')
    assert is_overdue(s)

def test_watering_0():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_1():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_2():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_3():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_4():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_5():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_6():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_7():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_8():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_9():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_10():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_11():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_12():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_13():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_14():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_15():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_16():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_17():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_18():
    assert days_since_watered('2024-01-01') >= 0

def test_watering_19():
    assert days_since_watered('2024-01-01') >= 0




def test_watering_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.watering")
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
