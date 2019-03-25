from base64 import b64encode

import pytest

from revolut.app import create_app
from revolut.rest.login import create_user


@pytest.fixture(scope='module')
def app():
    """Flask Pytest uses it"""
    app = create_app(secret='secret', database='sqlite:////tmp/test_revolut.db')
    app.config['SERVER_NAME'] = 'myapp.dev:5000'
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

@pytest.fixture(scope='module')
def client_with_db(app):
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    app.db.drop_all()
    app.db.create_all()
    create_user('admin', 'secret')

    yield testing_client  # this is where the testing happens!

    ctx.pop()

