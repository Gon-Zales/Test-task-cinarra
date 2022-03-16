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
    response = client.post('/api/v1/drivers', json=stub)
    assert response.status_code == 201
    driver = response.json
    compare_driver(driver, stub, True)
    global driver_id
    driver_id = driver["id"]


def test_driver_find(client):
    response = client.get('/api/v1/drivers', query_string={"driverId": driver_id})
    assert response.status_code == 200
    driver = response.json
    assert driver["id"] == driver_id
    compare_driver(driver, stub_w_id(), False)
    response = client.get('/api/v1/drivers', query_string={"driverId": 2785})
    assert response.status_code == 404


def test_driver_delete(client):
    driver = client.get('/api/v1/drivers', query_string={"driverId": driver_id}).json
    response = client.delete(f'/api/v1/drivers/{driver_id}')
    assert response.status_code == 200 and response.json == driver

    response = client.delete(f'/api/v1/drivers/{driver_id}')
    assert response.status_code == 404
