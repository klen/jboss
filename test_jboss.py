""" Tests for `jboss` module. """

import pytest
from jboss import APIClient


def test_jboss():
    client = APIClient()

    assert str(client.api.runtime['test:dev:1']) == 'GET runtime/test:dev:1'
    assert str(client.api.runtime['test:dev:1'].post) == 'POST runtime/test:dev:1'

    with pytest.raises(client.exception):
        client.api.unknown()
