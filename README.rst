containerutil |Build Status| |Coverage| |pypi| |Versions| |Wheel|
=================================================================

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


Installation
------------

From `PyPI`_ using ``pip`` package manager:

.. code:: bash

    pip install --upgrade containerutil


Or install the latest sources from GitHub:

.. code:: bash

    pip install https://github.com/pavdmyt/containerutil/archive/master.zip


Development
-----------

Clone the repository:

.. code:: bash

    git clone https://github.com/pavdmyt/containerutil.git


Install dependencies:

.. code:: bash

    make install


Lint code:

.. code:: bash

    make lint


Run tests:

.. code:: bash

    make test


Contributing
------------

1. Fork it!
2. Create your feature branch: ``git checkout -b my-new-feature``
3. Commit your changes: ``git commit -m 'Add some feature'``
4. Push to the branch: ``git push origin my-new-feature``
5. Submit a pull request
6. Make sure tests are passing


License
-------

MIT - Pavlo Dmytrenko


.. _pathlib.Path: https://docs.python.org/3/library/pathlib.html
.. _docker container: https://www.docker.com/what-container
.. _PyPI: https://pypi.org/

.. |Build Status| image:: https://travis-ci.org/pavdmyt/containerutil.svg?branch=master
   :target: https://travis-ci.org/pavdmyt/containerutil
.. |Coverage| image:: https://coveralls.io/repos/github/pavdmyt/containerutil/badge.svg?branch=master
   :target: https://coveralls.io/github/pavdmyt/containerutil?branch=master
.. |pypi| image:: https://img.shields.io/pypi/v/containerutil.svg
   :target: https://pypi.org/project/containerutil/
.. |Versions| image:: https://img.shields.io/pypi/pyversions/containerutil.svg
   :target: https://pypi.org/project/containerutil/
.. |Wheel| image:: https://img.shields.io/pypi/wheel/containerutil.svg
   :target: https://pypi.org/project/containerutil/
