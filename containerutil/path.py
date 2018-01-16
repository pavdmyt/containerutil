# -*- coding: utf-8 -*-

"""
containerutil.path
~~~~~~~~~~~~~~~~~~

Container's filesystem path tools.
"""


class Path(object):
    _cmd_tmpl = '/bin/sh -c "test {0} {1} && echo true"'

    def __init__(self, container_obj, path):
        self._ctnr = container_obj
        self._path = path if path else '/'

    def exists(self):
        cmd = self._cmd_tmpl.format('-e', self._path)
        return self._checker(cmd)

    def is_file(self):
        cmd = self._cmd_tmpl.format('-f', self._path)
        return self._checker(cmd)

    def is_dir(self):
        cmd = self._cmd_tmpl.format('-d', self._path)
        return self._checker(cmd)

    def is_symlink(self):
        cmd = self._cmd_tmpl.format('-L', self._path)
        return self._checker(cmd)

    def is_fifo(self):
        cmd = self._cmd_tmpl.format('-p', self._path)
        return self._checker(cmd)

    def _checker(self, cmd):
        resp = self._ctnr.exec_run(cmd)
        if isinstance(resp, bytes):
            # Py3
            resp = resp.decode('utf-8')
        if "true" in resp:
            return True
        return False
