import pytest

from app import app


@pytest.fixture()
def app_test():
    app.config['TESTING'] = True
    app.config['FLASK_ENV'] = "development"
    yield app


@pytest.fixture()
def client(app_test):
    with app.app_context():
        with app.test_client() as client:
            yield client

