from base64 import b64encode

import pytest

from revolut.app import create_app


@pytest.fixture(scope='module')
def app():
    """Flask Pytest uses it"""
    app = create_app(secret='secret')
    return app

@pytest.fixture(scope='module')
def auth():
    """The Basic Auth credentials for testing"""
    credentials = b64encode(bytes("admin:secret", 'ascii')).decode('ascii')
    data = {'Authorization': 'Basic ' + credentials}
    return data

@pytest.fixture(scope='module')
def client(app):
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
