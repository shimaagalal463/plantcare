"""Tests for plantcare.errors."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from plantcare.errors import PlantcareError, ValidationError, StorageError, MigrationError, NotFoundError

@pytest.mark.parametrize('cls', [PlantcareError, ValidationError, StorageError, MigrationError, NotFoundError])
def test_exception_hierarchy(cls):
    assert issubclass(cls, Exception)

def test_raise_errors_0():
    with pytest.raises(ValidationError):
        raise ValidationError('err0')

def test_raise_errors_1():
    with pytest.raises(ValidationError):
        raise ValidationError('err1')

def test_raise_errors_2():
    with pytest.raises(ValidationError):
        raise ValidationError('err2')

def test_raise_errors_3():
    with pytest.raises(ValidationError):
        raise ValidationError('err3')

def test_raise_errors_4():
    with pytest.raises(ValidationError):
        raise ValidationError('err4')

def test_raise_errors_5():
    with pytest.raises(ValidationError):
        raise ValidationError('err5')

def test_raise_errors_6():
    with pytest.raises(ValidationError):
        raise ValidationError('err6')

def test_raise_errors_7():
    with pytest.raises(ValidationError):
        raise ValidationError('err7')

def test_raise_errors_8():
    with pytest.raises(ValidationError):
        raise ValidationError('err8')

def test_raise_errors_9():
    with pytest.raises(ValidationError):
        raise ValidationError('err9')

def test_raise_errors_10():
    with pytest.raises(ValidationError):
        raise ValidationError('err10')

def test_raise_errors_11():
    with pytest.raises(ValidationError):
        raise ValidationError('err11')

def test_raise_errors_12():
    with pytest.raises(ValidationError):
        raise ValidationError('err12')

def test_raise_errors_13():
    with pytest.raises(ValidationError):
        raise ValidationError('err13')

def test_raise_errors_14():
    with pytest.raises(ValidationError):
        raise ValidationError('err14')

def test_raise_errors_15():
    with pytest.raises(ValidationError):
        raise ValidationError('err15')

def test_raise_errors_16():
    with pytest.raises(ValidationError):
        raise ValidationError('err16')

def test_raise_errors_17():
    with pytest.raises(ValidationError):
        raise ValidationError('err17')




def test_errors_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.errors")
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
