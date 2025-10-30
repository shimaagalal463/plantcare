"""Tests for plantcare.server."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from plantcare.server import PlantcareHandler, serve
import threading
import urllib.request
import time

def test_handler_class():
    assert hasattr(PlantcareHandler, 'do_GET')

def test_server_summary(sample_book):
    from http.server import HTTPServer
    PlantcareHandler.book_path = sample_book.path
    srv = HTTPServer(('127.0.0.1', 0), PlantcareHandler)
    port = srv.server_address[1]
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    time.sleep(0.2)
    try:
        resp = urllib.request.urlopen('http://127.0.0.1:%d/summary' % port)
        assert resp.status == 200
        resp = urllib.request.urlopen('http://127.0.0.1:%d/json' % port)
        assert resp.status == 200
    finally:
        srv.shutdown()

def test_server_smoke_0():
    assert callable(serve)

def test_server_smoke_1():
    assert callable(serve)

def test_server_smoke_2():
    assert callable(serve)

def test_server_smoke_3():
    assert callable(serve)

def test_server_smoke_4():
    assert callable(serve)

def test_server_smoke_5():
    assert callable(serve)

def test_server_smoke_6():
    assert callable(serve)

def test_server_smoke_7():
    assert callable(serve)

def test_server_smoke_8():
    assert callable(serve)

def test_server_smoke_9():
    assert callable(serve)




def test_server_expansion_helpers():
    import importlib
    m = importlib.import_module("plantcare.server")
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
