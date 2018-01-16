# -*- coding: utf-8 -*-

import docker
import containerutil


CONTAINER_NAME = 'my_container'


def main():
    client = docker.from_env()
    container = client.containers.get('alpine-test')
    path_list = ['/home', '/etc/hosts', '/foo/bar', '/etc/mtab']

    for path in path_list:
        print("---\n* Checking {0}".format(path))
        p = containerutil.Path(container, path)

        if p.exists():
            print("{0} exists".format(path))
        else:
            print("{0}: no such file or directory".format(path))
            continue

        if p.is_file():
            print("{0} is file".format(path))

        if p.is_dir():
            print("{0} is a directory".format(path))

        if p.is_symlink():
            print("{0} is a symbolic link".format(path))


if __name__ == '__main__':
    main()
