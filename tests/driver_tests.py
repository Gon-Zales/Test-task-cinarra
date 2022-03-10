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
driver_id = -89


def stub_w_id():
    res = stub.copy()
    res["id"] = driver_id
    return res


def compare_driver(d1, d2, ignore_id):
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
    compare_driver(driver, stub, True)
    global driver_id
    driver_id = driver["id"]


def test_driver_find(client):
    response = client.get('/drivers', query_string={"driverId": driver_id})
    assert response.status_code == 200
    driver = response.json
    assert driver["id"] == driver_id
    compare_driver(driver, stub_w_id(), False)
    response = client.get('/drivers', query_string={"driverId": 2785})
    assert response.status_code == 404


def test_driver_delete(client):
    driver = client.get('/drivers', query_string={"driverId": driver_id}).json
    response = client.delete(f'/drivers/{driver_id}')
    assert response.status_code == 200
    deleted = response.json
    assert deleted == driver
    response = client.delete(f'/drivers/{2785}')
    assert response.status_code == 404
