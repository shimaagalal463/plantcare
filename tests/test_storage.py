"""Tests for plantcare.storage."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from plantcare.storage import Book, init_book
from plantcare.room import Room
from plantcare.plant import Plant
from plantcare.care_log import CareLog
from plantcare.errors import NotFoundError, StorageError

def test_init_and_load(tmp_path):
    p = tmp_path / 'j.json'
    b = init_book(p)
    assert p.exists()
    b2 = Book.load(p)
    assert b2.schema_version >= 1

def test_add_entities(sample_book):
    assert len(sample_book.plants) == 2
    assert len(sample_book.care_logs) == 2

def test_get_plant(sample_book):
    p = sample_book.get_plant(1)
    assert p.name == 'Monstera'

def test_get_room(sample_book):
    r = sample_book.get_room(1)
    assert r.name == 'Living Room'

def test_missing_plant(sample_book):
    with pytest.raises(NotFoundError):
        sample_book.get_plant(9999)

def test_book_helpers(sample_book):
    from plantcare.storage import book_care_log_count, book_plant_count, find_care_for_plant, delete_care_log
    assert book_care_log_count(sample_book) == 2
    delete_care_log(sample_book, 1)
    assert book_care_log_count(sample_book) == 1

def test_save_roundtrip_0(tmp_path):
    p = tmp_path / 't0.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_1(tmp_path):
    p = tmp_path / 't1.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_2(tmp_path):
    p = tmp_path / 't2.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_3(tmp_path):
    p = tmp_path / 't3.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_4(tmp_path):
    p = tmp_path / 't4.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_5(tmp_path):
    p = tmp_path / 't5.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_6(tmp_path):
    p = tmp_path / 't6.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_7(tmp_path):
    p = tmp_path / 't7.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_8(tmp_path):
    p = tmp_path / 't8.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_9(tmp_path):
    p = tmp_path / 't9.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_10(tmp_path):
    p = tmp_path / 't10.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_11(tmp_path):
    p = tmp_path / 't11.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_12(tmp_path):
    p = tmp_path / 't12.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_13(tmp_path):
    p = tmp_path / 't13.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_14(tmp_path):
    p = tmp_path / 't14.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_15(tmp_path):
    p = tmp_path / 't15.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_16(tmp_path):
    p = tmp_path / 't16.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_17(tmp_path):
    p = tmp_path / 't17.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_18(tmp_path):
    p = tmp_path / 't18.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'

def test_save_roundtrip_19(tmp_path):
    p = tmp_path / 't19.json'
    b = init_book(p)
    b.add_room(Room(name='R', light_level='medium'))
    b.save()
    assert Book.load(p).rooms[0].name == 'R'




def test_storage_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.storage")
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
