# -*- coding: utf-8 -*-

import docker
import containerutil


CONTAINER_NAME = 'my_container'


def main():
    client = docker.from_env()
    container = client.containers.get('cp_test')

    p = containerutil.Path(container)
    path_list = ['/home', '/etc/hosts', '/foo/bar']

    for path in path_list:
        print("---\n* Checking {0}".format(path))

        if p.exists(path):
            print("{0} exists".format(path))
        else:
            print("{0}: no such file or directory".format(path))
            continue

        if p.isfile(path):
            print("{0} is file".format(path))

        if p.isdir(path):
            print("{0} is a directory".format(path))


if __name__ == '__main__':
    main()
