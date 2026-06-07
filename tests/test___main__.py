"""Tests for python -m plantcare."""
from plantcare.__main__ import main

def test_main_module_runs():
    assert main([]) == 0
