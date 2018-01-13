# -*- coding: utf-8 -*-


class Path(object):
    _cmd_tmpl = '/bin/sh -c "test {0} {1} && echo true"'

    def __init__(self, container_obj):
        self._ctnr = container_obj

    def exists(self, path):
        return self.isfile(path) or self.isdir(path)

    def isfile(self, path):
        cmd = self._cmd_tmpl.format('-f', path)
        return self._checker(cmd)

    def isdir(self, path):
        cmd = self._cmd_tmpl.format('-d', path)
        return self._checker(cmd)

    def _checker(self, cmd):
        resp = self._ctnr.exec_run(cmd)
        if isinstance(resp, bytes):
            # Py3
            resp = resp.decode('utf-8')
        if "true" in resp:
            return True
        return False
