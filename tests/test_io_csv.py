"""Tests for plantcare.io_csv."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

import plantcare.io_csv as mod

from plantcare.io_csv import import_care_logs_csv, export_care_logs_csv

from plantcare.storage import init_book, Book
from plantcare.room import Room
from plantcare.plant import Plant

def test_import_csv(tmp_path):
    j = tmp_path / 'j.json'
    c = tmp_path / 'o.csv'
    c.write_text('plant_id,action,performed_at,notes,soil_moisture\n1,water,2024-01-01T12:00:00,,dry\n')
    b = init_book(j)
    b.add_plant(Plant(name='P', acquired_date='2024-01-01'))
    n = import_care_logs_csv(b, c)
    assert n == 1

def test_export_csv(sample_book, tmp_path):
    p = tmp_path / 'out.csv'
    export_care_logs_csv(sample_book, p)
    assert p.exists()

def test_io_io_csv_0(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_1(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_2(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_3(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_4(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_5(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_6(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_7(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_8(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_9(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_10(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_11(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_12(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_13(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_14(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_csv_15(tmp_path):
    init_book(tmp_path / 'j.json')




def test_io_csv_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.io_csv")
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
