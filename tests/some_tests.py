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


stub = {"name": "dsd", "car": "Masdas"}


def compare_driver(d1, d2, ignore_id=True):
    assert d1["name"] == d2["name"]
    assert d1["car"] == d2["car"]
    if ignore_id:
        assert type(d1["id"]) is int
    else:
        assert d1["id"] == d2["id"]


def test_driver_create(client):
    response = client.post('/drivers', json=stub)
    assert response.status_code == 201
    driver = response.json
    # TODO write a constructor and override comparison to shorten such validations
    compare_driver(driver, stub)
    response = client.post('/drivers', json={"car": "dasdas"})
    assert response.status_code == 400
    response = client.post('/drivers', json={"name": "dsd"})
    assert response.status_code == 400
    response = client.post('/drivers', json={"name": "dsd", "car": 123})
    assert response.status_code == 400
    response = client.post('/drivers', json={"name": "dsd", "car": None})
    assert response.status_code == 400
    response = client.post('/drivers', json={"name": 123, "car": "dasdas"})
    assert response.status_code == 400
    response = client.post('/drivers', json={"name": None, "car": "dasdas"})
    assert response.status_code == 400


def test_driver_find(client):
    response = client.get('/drivers', json={"driverId": 1})
    assert response.status_code == 200
    driver = response.json
    assert driver["id"] == 1
    expected_result = stub.copy()
    expected_result["id"] = 1
    compare_driver(driver, stub)
    response = client.get('/drivers', json={"driverId": 2785})
    assert response.status_code == 404
    response = client.get('/drivers', json={"driverId": "2785"})
    assert response.status_code == 400

# TODO - 9 requests, each has to have at least two tests - to fail and to pass.
# TODO - Exhaust possible fail cases
