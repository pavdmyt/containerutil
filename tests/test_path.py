# -*- coding: utf-8 -*-

"""
tests.test_path
~~~~~~~~~~~~~~~

Tests for containerutil.path
"""

import pytest

import containerutil as cutil


class TC(object):
    """Test case."""

    def __init__(self, path, exists=False,
                 is_dir=False, is_file=False,
                 is_symlink=False, is_fifo=False):
        self.path = path
        self.exists = exists
        self.is_dir = is_dir
        self.is_file = is_file
        self.is_symlink = is_symlink
        self.is_fifo = is_fifo


test_cases = [
    # (path, exists, is_dir, is_file, is_symlink)

    # Empty (falls back to '/')
    TC('', True, True, False),

    # Dirs
    TC('/bin', True, True),
    TC('/etc', True, True),
    TC('/home', True, True),
    TC('/lib', True, True),
    TC('/media', True, True),
    TC('/mnt', True, True),
    TC('/proc', True, True),
    TC('/root', True, True),
    TC('/run', True, True),
    TC('/sbin', True, True),
    TC('/var', True, True),
    TC('/usr', True, True),
    TC('/usr/local', True, True),
    TC('/usr/local/', True, True),
    TC('/usr/local/bin', True, True),
    TC('/usr/local/bin/', True, True),

    # Files
    TC('/etc/fstab', True, is_file=True),
    TC('/etc/hosts', True, is_file=True),
    TC('/etc/passwd', True, is_file=True),
    TC('/etc/resolv.conf', True, is_file=True),

    # Symlinks
    TC('/etc/mtab', True, is_file=True, is_symlink=True),
    TC('/usr/bin/test', True, is_file=True, is_symlink=True),
    TC('/usr/bin/time', True, is_file=True, is_symlink=True),
    TC('/usr/bin/vi', True, is_file=True, is_symlink=True),
    TC('/usr/bin/wc', True, is_file=True, is_symlink=True),

    # Named pipes (FIFO)
    TC('/fifo1', True, is_fifo=True),
    TC('/fifo2', True, is_fifo=True),

    # Non-existent
    TC('/foo'),
    TC('/foo/bar'),
    TC('/spam'),
    TC('/spam/eggs'),
]


def id_func(case):
    if case.is_dir:
        return "{0!r}-{1}".format(case.path, "Directory")
    if case.is_file:
        return "{0!r}-{1}".format(case.path, "File")

    return repr(case.path)


@pytest.mark.parametrize('case', test_cases, ids=id_func)
def test_exists(case, container):
    p = cutil.Path(container, case.path)
    assert p.exists() == case.exists


@pytest.mark.parametrize('case', test_cases, ids=id_func)
def test_is_file(case, container):
    p = cutil.Path(container, case.path)
    assert p.is_file() == case.is_file


@pytest.mark.parametrize('case', test_cases, ids=id_func)
def test_is_dir(case, container):
    p = cutil.Path(container, case.path)
    assert p.is_dir() == case.is_dir


@pytest.mark.parametrize('case', test_cases, ids=id_func)
def test_is_symlink(case, container):
    p = cutil.Path(container, case.path)
    assert p.is_symlink() == case.is_symlink


@pytest.mark.parametrize('case', test_cases, ids=id_func)
def test_is_fifo(case, container):
    p = cutil.Path(container, case.path)
    assert p.is_fifo() == case.is_fifo
