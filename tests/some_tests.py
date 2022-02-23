import pytest
from app import app


@pytest.fixture()
def app_test():
    app.config['TESTING'] = True
    yield app


@pytest.fixture()
def client(app_test):
    with app.app_context():
        with app.test_client() as client:
            yield client


def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'


def test_driver_create(client):
    response = client.post('/drivers', json={"name": "dsd", "car": "dasdas"})
    assert response.status_code == 201
