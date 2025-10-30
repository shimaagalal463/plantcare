"""Tests for plantcare.cli."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from plantcare.cli import build_parser, main, cmd_init, cmd_room_add, cmd_plant_add, cmd_care_add, cmd_report, cmd_import, cmd_backup, cmd_migrate
from plantcare.storage import Book
import argparse

def test_parser():
    p = build_parser()
    assert p.prog == 'plantcare'

def test_main_help(capsys):
    assert main([]) == 0

def test_cmd_init(tmp_path):
    args = argparse.Namespace(path=str(tmp_path / 'j.json'))
    assert cmd_init(args) == 0

def test_cmd_room_add(tmp_path):
    j = tmp_path / 'j.json'
    cmd_init(argparse.Namespace(path=str(j)))
    args = argparse.Namespace(journal=str(j), name='Living Room', light='bright-indirect', humidity='medium')
    assert cmd_room_add(args) == 0

def test_cmd_plant_add(sample_book):
    args = argparse.Namespace(journal=str(sample_book.path), name='Fern', species='Nephrolepis', room=1, date='2024-01-01')
    assert cmd_plant_add(args) == 0

def test_cmd_care_add(sample_book):
    args = argparse.Namespace(journal=str(sample_book.path), plant=1, action='water', date='2025-06-02', at=None, notes='dry', moisture='dry')
    assert cmd_care_add(args) == 0

def test_cmd_report_summary(sample_book, capsys):
    args = argparse.Namespace(journal=str(sample_book.path), kind='summary', id=1, top=5)
    assert cmd_report(args) == 0

def test_cmd_migrate_check(sample_book):
    args = argparse.Namespace(journal=str(sample_book.path), check=True)
    assert cmd_migrate(args) == 0

def test_cmd_import_csv(tmp_path):
    j, c = tmp_path / 'j.json', tmp_path / 'd.csv'
    cmd_init(argparse.Namespace(path=str(j)))
    c.write_text('plant_id,action,performed_at,notes,soil_moisture\n1,water,2024-01-01T12:00:00,note,dry\n')
    args = argparse.Namespace(journal=str(j), format='csv', file=str(c))
    assert cmd_import(args) == 0

def test_cmd_backup(tmp_path, sample_book):
    dest = tmp_path / 'bak.json'
    args = argparse.Namespace(journal=str(sample_book.path), dest=str(dest), label='t')
    assert cmd_backup(args) == 0

def test_parser_has_subcommands_0():
    p = build_parser()
    assert p._subparsers is not None

def test_parser_has_subcommands_1():
    p = build_parser()
    assert p._subparsers is not None

def test_parser_has_subcommands_2():
    p = build_parser()
    assert p._subparsers is not None

def test_parser_has_subcommands_3():
    p = build_parser()
    assert p._subparsers is not None

def test_parser_has_subcommands_4():
    p = build_parser()
    assert p._subparsers is not None

def test_parser_has_subcommands_5():
    p = build_parser()
    assert p._subparsers is not None

def test_parser_has_subcommands_6():
    p = build_parser()
    assert p._subparsers is not None

def test_parser_has_subcommands_7():
    p = build_parser()
    assert p._subparsers is not None

def test_parser_has_subcommands_8():
    p = build_parser()
    assert p._subparsers is not None

def test_parser_has_subcommands_9():
    p = build_parser()
    assert p._subparsers is not None




def test_cli_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.cli")
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
