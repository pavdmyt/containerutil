# -*- coding: utf-8 -*-

"""
tests.conftest
~~~~~~~~~~~~~~

Tests setup.
"""

import uuid

import docker
import pytest


@pytest.fixture(scope='session')
def image():
    return 'alpine:3.7'


@pytest.fixture(scope='session')
def dkr_client():
    return docker.from_env(version='auto')


@pytest.fixture(scope='session')
def session_id():
    return str(uuid.uuid4())


@pytest.fixture(scope='session')
def image_lst(dkr_client):
    images = [
        image.tags[0]
        for image in dkr_client.images.list()
        if image.tags
    ]
    return images


@pytest.fixture(scope='session')
def container(dkr_client, session_id, image, image_lst):
    # Get Image
    img_name, img_tag = image.split(':')
    if image not in image_lst:
        dkr_client.images.pull(img_name, tag=img_tag)

    # Run Container
    cmd = '/bin/sh -c "while true; do echo 1; sleep 1; done"'
    ctnr = dkr_client.containers.run(
        image=image,
        command=cmd,
        name='test-{0}-{1}'.format(img_name, session_id),
        detach=True,
    )

    # Create named pipes (FIFO)
    ctnr.exec_run('mkfifo /fifo1')
    ctnr.exec_run('mkfifo /fifo2')
    yield ctnr

    # Cleanup
    ctnr.kill()
    ctnr.remove()
