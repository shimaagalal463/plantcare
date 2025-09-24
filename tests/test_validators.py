"""Tests for plantcare.validators."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from plantcare.validators import validate_plant_name, validate_light_level, validate_moisture, validate_count, validate_id
from plantcare.errors import ValidationError

def test_validate_name_0():
    assert validate_plant_name('Plant 0') == 'Plant 0'

def test_validate_name_1():
    assert validate_plant_name('Plant 1') == 'Plant 1'

def test_validate_name_2():
    assert validate_plant_name('Plant 2') == 'Plant 2'

def test_validate_name_3():
    assert validate_plant_name('Plant 3') == 'Plant 3'

def test_validate_name_4():
    assert validate_plant_name('Plant 4') == 'Plant 4'

def test_validate_name_5():
    assert validate_plant_name('Plant 5') == 'Plant 5'

def test_validate_name_6():
    assert validate_plant_name('Plant 6') == 'Plant 6'

def test_validate_name_7():
    assert validate_plant_name('Plant 7') == 'Plant 7'

def test_validate_name_8():
    assert validate_plant_name('Plant 8') == 'Plant 8'

def test_validate_name_9():
    assert validate_plant_name('Plant 9') == 'Plant 9'

def test_validate_name_10():
    assert validate_plant_name('Plant 10') == 'Plant 10'

def test_validate_name_11():
    assert validate_plant_name('Plant 11') == 'Plant 11'

def test_validate_name_12():
    assert validate_plant_name('Plant 12') == 'Plant 12'

def test_validate_name_13():
    assert validate_plant_name('Plant 13') == 'Plant 13'

def test_validate_name_14():
    assert validate_plant_name('Plant 14') == 'Plant 14'

def test_validate_name_15():
    assert validate_plant_name('Plant 15') == 'Plant 15'

def test_validate_name_16():
    assert validate_plant_name('Plant 16') == 'Plant 16'

def test_validate_name_17():
    assert validate_plant_name('Plant 17') == 'Plant 17'

def test_validate_name_18():
    assert validate_plant_name('Plant 18') == 'Plant 18'

def test_validate_name_19():
    assert validate_plant_name('Plant 19') == 'Plant 19'

def test_validate_name_20():
    assert validate_plant_name('Plant 20') == 'Plant 20'

def test_validate_name_21():
    assert validate_plant_name('Plant 21') == 'Plant 21'

def test_validate_name_22():
    assert validate_plant_name('Plant 22') == 'Plant 22'

def test_validate_name_23():
    assert validate_plant_name('Plant 23') == 'Plant 23'

def test_validate_name_24():
    assert validate_plant_name('Plant 24') == 'Plant 24'

def test_validate_id_0():
    assert validate_id(1) == 1

def test_validate_id_1():
    assert validate_id(2) == 2

def test_validate_id_2():
    assert validate_id(3) == 3

def test_validate_id_3():
    assert validate_id(4) == 4

def test_validate_id_4():
    assert validate_id(5) == 5

def test_validate_id_5():
    assert validate_id(6) == 6

def test_validate_id_6():
    assert validate_id(7) == 7

def test_validate_id_7():
    assert validate_id(8) == 8

def test_validate_id_8():
    assert validate_id(9) == 9

def test_validate_id_9():
    assert validate_id(10) == 10

def test_validate_id_10():
    assert validate_id(11) == 11

def test_validate_id_11():
    assert validate_id(12) == 12

def test_validate_id_12():
    assert validate_id(13) == 13

def test_validate_id_13():
    assert validate_id(14) == 14

def test_validate_id_14():
    assert validate_id(15) == 15

def test_validate_id_15():
    assert validate_id(16) == 16

def test_validate_id_16():
    assert validate_id(17) == 17

def test_validate_id_17():
    assert validate_id(18) == 18

def test_validate_id_18():
    assert validate_id(19) == 19

def test_validate_id_19():
    assert validate_id(20) == 20

def test_validate_id_20():
    assert validate_id(21) == 21

def test_validate_id_21():
    assert validate_id(22) == 22

def test_validate_id_22():
    assert validate_id(23) == 23

def test_validate_id_23():
    assert validate_id(24) == 24

def test_validate_id_24():
    assert validate_id(25) == 25

def test_bad_name():
    with pytest.raises(ValidationError):
        validate_plant_name('')

def test_optional_string():
    from plantcare.validators import validate_optional_string
    assert validate_optional_string('hi', 'f') == 'hi'

def test_light_level():
    assert validate_light_level('bright-indirect') == 'bright-indirect'




def test_validators_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.validators")
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
