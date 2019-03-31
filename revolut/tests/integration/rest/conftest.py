from base64 import b64encode

import psycopg2
import pytest
import sqlalchemy
import sqlalchemy_utils

from revolut.app import create_app
from revolut.rest.login import create_user


def pg_is_responsive(ip, docker_setup):
    try:
        conn = psycopg2.connect(
            "host={} user={} password={} dbname={} port=5433".format(
                ip,
                docker_setup['postgres']['user'],
                docker_setup['postgres']['password'],
                'postgres'
            )
        )
        conn.close()
        return True
    except psycopg2.OperationalError:
        return False


@pytest.fixture(scope='session')
def app(docker_ip, docker_services, docker_setup):
    """Flask Pytest uses it"""
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1,
        check=lambda: pg_is_responsive(docker_ip, docker_setup)
    )
    
    database_uri = "postgresql://{}:{}@{}:5433/{}".format(
        docker_setup['postgres']['user'],
        docker_setup['postgres']['password'],
        docker_setup['postgres']['host'],
        docker_setup['postgres']['dbname']
    )

    engine = sqlalchemy.create_engine(database_uri)
    sqlalchemy_utils.create_database(engine.url)

    app = create_app(secret='secret', database=database_uri)
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

