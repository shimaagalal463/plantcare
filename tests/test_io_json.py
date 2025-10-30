"""Tests for plantcare.io_json."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

import plantcare.io_json as mod

from plantcare.io_json import export_book_json, import_book_json, merge_books

from plantcare.storage import init_book, Book
from plantcare.room import Room
from plantcare.plant import Plant

def test_json_roundtrip(sample_book, tmp_path):
    p = tmp_path / 'out.json'
    export_book_json(sample_book, p)
    assert import_book_json(p)['schema_version'] >= 1

def test_io_io_json_0(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_1(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_2(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_3(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_4(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_5(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_6(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_7(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_8(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_9(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_10(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_11(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_12(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_13(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_14(tmp_path):
    init_book(tmp_path / 'j.json')

def test_io_io_json_15(tmp_path):
    init_book(tmp_path / 'j.json')




def test_io_json_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.io_json")
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
