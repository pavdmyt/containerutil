containerutil
=============

``containerutil.Path`` provides API similar to `pathlib.Path`_ for inspecting
`docker container`_ file system:

.. code:: python

    import docker
    import containerutil

    client = docker.from_env(version='auto')
    ctnr = client.containers.get('my-container')

    p = containerutil.Path(ctnr, '/foo/bar/path')

    p.exists()        # True if file exists (regardless of type)
    p.is_file()       # True if file exists and is a regular file
    p.is_symlink()    # True if file exists and is a symbolic link
    p.is_fifo()       # True if file is a named pipe (FIFO)


License
-------

MIT - Pavlo Dmytrenko


.. _pathlib.Path: https://docs.python.org/3/library/pathlib.html
.. _docker container: https://www.docker.com/what-container
