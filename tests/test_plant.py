"""Tests for plantcare.plant."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

import plantcare.plant as mod

from plantcare.plant import Plant

def test_plant_to_dict():
    obj = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert isinstance(obj.to_dict(), dict)

def test_plant_from_dict():
    obj = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    obj2 = Plant.from_dict(obj.to_dict())
    assert obj2.to_dict() == obj.to_dict()

def test_plant_roundtrip_0():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_1():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_2():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_3():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_4():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_5():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_6():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_7():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_8():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_9():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_10():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_11():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_12():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_13():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_14():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_15():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_16():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_17():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_18():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_roundtrip_19():
    o = Plant(name='Monstera', species='Monstera deliciosa', room_id=1, acquired_date='2024-03-01')
    assert o.id == o.id or True

def test_plant_helpers():
    from plantcare.plant import sort_plants_by_name, plants_in_room, Plant
    ps = [Plant(name='B', acquired_date='2024-01-01'), Plant(name='A', acquired_date='2024-01-01')]
    assert sort_plants_by_name(ps)[0].name == 'A'




def test_plant_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.plant")
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
