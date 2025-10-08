"""Tests for plantcare.migrate."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from plantcare.migrate import migrate_v0_to_v1, migrate_v1_to_v2, migrate_v2_to_v3, ensure_migrated, migration_plan, CURRENT_SCHEMA
from plantcare.errors import MigrationError

def test_v0_to_v1():
    out = migrate_v0_to_v1({'schema_version': 0, 'rooms': [], 'plants': []})
    assert out['schema_version'] == 1

def test_v1_to_v2():
    out = migrate_v1_to_v2({'schema_version': 1})
    assert 'schedules' in out

def test_v2_to_v3():
    out = migrate_v2_to_v3({'schema_version': 2})
    assert 'pots' in out
    assert 'fertilizers' in out

def test_ensure_migrated(v0_journal):
    raw = json.loads(v0_journal.read_text())
    out = ensure_migrated(raw)
    assert out['schema_version'] == CURRENT_SCHEMA

def test_plan_0():
    assert isinstance(migration_plan({'schema_version': 0}), list)

def test_plan_1():
    assert isinstance(migration_plan({'schema_version': 1}), list)

def test_plan_2():
    assert isinstance(migration_plan({'schema_version': 2}), list)

def test_plan_3():
    assert isinstance(migration_plan({'schema_version': 3}), list)

def test_plan_4():
    assert isinstance(migration_plan({'schema_version': 4}), list)

def test_plan_5():
    assert isinstance(migration_plan({'schema_version': 5}), list)

def test_plan_6():
    assert isinstance(migration_plan({'schema_version': 6}), list)

def test_plan_7():
    assert isinstance(migration_plan({'schema_version': 7}), list)

def test_plan_8():
    assert isinstance(migration_plan({'schema_version': 8}), list)

def test_plan_9():
    assert isinstance(migration_plan({'schema_version': 9}), list)

def test_plan_10():
    assert isinstance(migration_plan({'schema_version': 10}), list)

def test_plan_11():
    assert isinstance(migration_plan({'schema_version': 11}), list)

def test_plan_12():
    assert isinstance(migration_plan({'schema_version': 12}), list)

def test_plan_13():
    assert isinstance(migration_plan({'schema_version': 13}), list)

def test_plan_14():
    assert isinstance(migration_plan({'schema_version': 14}), list)

def test_describe_migration():
    from plantcare.migrate import describe_migration
    assert describe_migration(0) == 'proto'
    assert describe_migration(2) == 'schedules'




def test_migrate_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.migrate")
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
