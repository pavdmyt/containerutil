# -*- coding: utf-8 -*-

"""
tests.test_path
~~~~~~~~~~~~~~~

Tests for containerutil.path
"""

import pytest

import containerutil as cutil


test_cases = [
    # path; exists; is_dir; is_file

    # Empty (falls back to '/')
    ('', True, True, False),

    # Dirs
    ('/bin', True, True, False),
    ('/etc', True, True, False),
    ('/home', True, True, False),
    ('/lib', True, True, False),
    ('/media', True, True, False),
    ('/mnt', True, True, False),
    ('/proc', True, True, False),
    ('/root', True, True, False),
    ('/run', True, True, False),
    ('/sbin', True, True, False),
    ('/var', True, True, False),
    ('/usr', True, True, False),
    ('/usr/local', True, True, False),
    ('/usr/local/', True, True, False),
    ('/usr/local/bin', True, True, False),
    ('/usr/local/bin/', True, True, False),

    # Files
    ('/etc/fstab', True, False, True),
    ('/etc/hosts', True, False, True),
    ('/etc/passwd', True, False, True),
    ('/etc/resolv.conf', True, False, True),

    # Non-existent
    ('/foo', False, False, False),
    ('/foo/bar', False, False, False),
    ('/spam', False, False, False),
    ('/spam/eggs', False, False, False),
]


def id_func(param):
    path, _, isdir, isfile = param
    if isdir:
        return "{0!r}-{1}".format(path, "Directory")
    if isfile:
        return "{0!r}-{1}".format(path, "File")

    return repr(path)


@pytest.mark.parametrize('case', test_cases, ids=id_func)
def test_exists(case, container):
    path, expected, _, _ = case
    p = cutil.Path(container, path)
    assert p.exists() == expected


@pytest.mark.parametrize('case', test_cases, ids=id_func)
def test_is_file(case, container):
    path, _, _, expected = case
    p = cutil.Path(container, path)
    assert p.is_file() == expected


@pytest.mark.parametrize('case', test_cases, ids=id_func)
def test_is_dir(case, container):
    path, _, expected, _ = case
    p = cutil.Path(container, path)
    assert p.is_dir() == expected
