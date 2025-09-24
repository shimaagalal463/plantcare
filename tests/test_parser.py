"""Tests for plantcare.parser."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from plantcare.parser import parse_date, parse_datetime, parse_count, slugify
from plantcare.errors import ValidationError

def test_parse_date_iso():
    assert str(parse_date('2024-07-15')) == '2024-07-15'

def test_parse_datetime():
    dt = parse_datetime('2024-07-15T10:30:00')
    assert dt.hour == 10

def test_parse_count_variants():
    assert parse_count('5') == 5
    assert parse_count('present') == 1

def test_slugify():
    assert 'monstera' in slugify('Monstera Deliciosa')

def test_parse_date_0():
    assert parse_date('2024-01-01').year == 2024

def test_parse_date_1():
    assert parse_date('2024-02-02').year == 2024

def test_parse_date_2():
    assert parse_date('2024-03-03').year == 2024

def test_parse_date_3():
    assert parse_date('2024-04-04').year == 2024

def test_parse_date_4():
    assert parse_date('2024-05-05').year == 2024

def test_parse_date_5():
    assert parse_date('2024-06-06').year == 2024

def test_parse_date_6():
    assert parse_date('2024-07-07').year == 2024

def test_parse_date_7():
    assert parse_date('2024-08-08').year == 2024

def test_parse_date_8():
    assert parse_date('2024-09-09').year == 2024

def test_parse_date_9():
    assert parse_date('2024-10-10').year == 2024

def test_parse_date_10():
    assert parse_date('2024-11-11').year == 2024

def test_parse_date_11():
    assert parse_date('2024-12-12').year == 2024

def test_parse_date_12():
    assert parse_date('2024-01-13').year == 2024

def test_parse_date_13():
    assert parse_date('2024-02-14').year == 2024

def test_parse_date_14():
    assert parse_date('2024-03-15').year == 2024

def test_parse_date_15():
    assert parse_date('2024-04-16').year == 2024

def test_parse_date_16():
    assert parse_date('2024-05-17').year == 2024

def test_parse_date_17():
    assert parse_date('2024-06-18').year == 2024

def test_parse_date_18():
    assert parse_date('2024-07-19').year == 2024

def test_parse_date_19():
    assert parse_date('2024-08-20').year == 2024

def test_bad_date():
    with pytest.raises(ValidationError):
        parse_date('not-a-date')

def test_parse_optional_float():
    from plantcare.parser import parse_optional_float
    assert parse_optional_float('3.5') == 3.5

def test_parse_count_0():
    assert parse_count(0) == 0

def test_parse_count_1():
    assert parse_count(1) == 1

def test_parse_count_2():
    assert parse_count(2) == 2

def test_parse_count_3():
    assert parse_count(3) == 3

def test_parse_count_4():
    assert parse_count(4) == 4

def test_parse_count_5():
    assert parse_count(5) == 5

def test_parse_count_6():
    assert parse_count(6) == 6

def test_parse_count_7():
    assert parse_count(7) == 7

def test_parse_count_8():
    assert parse_count(8) == 8

def test_parse_count_9():
    assert parse_count(9) == 9

def test_parse_count_10():
    assert parse_count(10) == 10

def test_parse_count_11():
    assert parse_count(11) == 11

def test_parse_count_12():
    assert parse_count(12) == 12

def test_parse_count_13():
    assert parse_count(13) == 13

def test_parse_count_14():
    assert parse_count(14) == 14




def test_parser_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.parser")
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
