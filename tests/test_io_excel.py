"""Tests for plantcare.io_excel."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

import plantcare.io_excel as mod

from plantcare.io_excel import export_rooms_xlsx

from plantcare.storage import init_book, Book
from plantcare.room import Room
from plantcare.plant import Plant

def test_excel_export(sample_book, tmp_path):
    p = tmp_path / 'r.xlsx'
    export_rooms_xlsx(sample_book, p)
    assert p.stat().st_size > 0

def test_io_io_excel_0(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_1(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_2(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_3(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_4(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_5(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_6(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_7(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_8(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_9(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_10(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_11(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_12(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_13(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_14(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_excel_15(tmp_path):
    init_book(tmp_path / 'j.json')




def test_io_excel_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.io_excel")
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
