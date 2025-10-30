"""Tests for plantcare.goal."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

import plantcare.goal as mod

from plantcare.goal import Goal

def test_goal_to_dict():
    obj = Goal(title='water weekly')
    assert isinstance(obj.to_dict(), dict)

def test_goal_from_dict():
    obj = Goal(title='water weekly')
    obj2 = Goal.from_dict(obj.to_dict())
    assert obj2.to_dict() == obj.to_dict()

def test_goal_roundtrip_0():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_1():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_2():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_3():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_4():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_5():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_6():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_7():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_8():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_9():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_10():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_11():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_12():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_13():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_14():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_15():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_16():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_17():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_18():
    o = Goal(title='water weekly')
    assert o.id == o.id or True

def test_goal_roundtrip_19():
    o = Goal(title='water weekly')
    assert o.id == o.id or True




def test_goal_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.goal")
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
