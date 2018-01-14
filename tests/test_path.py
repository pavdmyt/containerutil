# -*- coding: utf-8 -*-

"""
tests.test_path
~~~~~~~~~~~~~~~

Tests for containerutil.path
"""

import containerutil as cutil


def test_exists(container):
    p = cutil.Path(container, "/home")
    assert p.exists()


def test_is_file(container):
    p = cutil.Path(container, "/home")
    assert not p.is_file()


def test_is_dir(container):
    p = cutil.Path(container, "/home")
    assert p.is_dir()
