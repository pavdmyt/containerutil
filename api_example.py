# -*- coding: utf-8 -*-

import docker
import containerutil


CONTAINER_NAME = 'my_container'


def main():
    client = docker.from_env()
    container = client.containers.get('alpine-test')

    dir_path = '/home'
    regular_file_path = '/etc/hosts'
    non_existent_path = '/foo/bar'
    symlink_path = '/etc/mtab'
    fifo_path = '/fifo1'

    path_list = [
        dir_path,
        regular_file_path,
        non_existent_path,
        symlink_path,
        fifo_path,
    ]
    container.exec_run('mkfifo ' + fifo_path)

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

        if p.is_fifo():
            print("{0} is a named pipe (FIFO)".format(path))


if __name__ == '__main__':
    main()
