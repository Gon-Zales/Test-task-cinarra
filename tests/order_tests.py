from client_tests import stub as client_stub
from driver_tests import stub as driver_stub
from models.order_model import ORDER_STATUS, NOT_ACCEPTED, IN_PROGRESS, CANCELLED, DONE

STATUS_CHANGE = [
    (NOT_ACCEPTED, NOT_ACCEPTED, True),
    (NOT_ACCEPTED, IN_PROGRESS, True),
    (NOT_ACCEPTED, CANCELLED, True),
    (NOT_ACCEPTED, DONE, False),
    (IN_PROGRESS, NOT_ACCEPTED, False),
    (IN_PROGRESS, IN_PROGRESS, False),
    (IN_PROGRESS, CANCELLED, True),
    (IN_PROGRESS, DONE, True),
    (CANCELLED, NOT_ACCEPTED, False),
    (CANCELLED, IN_PROGRESS, False),
    (CANCELLED, CANCELLED, False),
    (CANCELLED, DONE, False),
    (DONE, NOT_ACCEPTED, False),
    (DONE, IN_PROGRESS, False),
    (DONE, CANCELLED, False),
    (DONE, DONE, False)
]


def get_stub(client):
    driver_id = client.post('/api/v1/drivers', json=driver_stub).json["id"]
    client_id = client.post('/api/v1/clients', json=client_stub).json["id"]
    return {
        "client_id": client_id,
        "driver_id": driver_id,
        "date_created": "2022-03-16T14:01:03",
        "status": NOT_ACCEPTED,
        "address_from": "dsd",
        "address_to": "dsd",
    }


def stub_w_id(client):
    stub = get_stub(client).copy()
    stub["id"] = client.post('/api/v1/orders', json=stub).json["id"]
    return stub


def compare_order(d1, d2, ignore_id):
    assert d1["client_id"] == d2["client_id"]
    assert d1["driver_id"] == d2["driver_id"]
    assert d1["date_created"] == d2["date_created"]
    assert d1["status"] == d2["status"]
    assert d1["address_from"] == d2["address_from"]
    assert d1["address_to"] == d2["address_to"]
    assert type(d1["id"]) is int
    if not ignore_id:
        assert d1["id"] == d2["id"]


def test_order_create(client):
    stub = get_stub(client)
    response = client.post('/api/v1/orders', json=stub)
    assert response.status_code == 201
    order = response.json
    compare_order(order, stub, True)

    stub = get_stub(client)
    for i in range(1, 3):
        stub["status"] = ORDER_STATUS[i]
        response = client.post('/api/v1/orders', json=stub)
        assert response.status_code == 400


def test_order_find(client):
    stub = get_stub(client)
    id_ = client.post('/api/v1/orders', json=stub).json["id"]
    stub["id"] = id_
    response = client.get('/api/v1/orders', query_string={"orderId": id_})
    assert response.status_code == 200
    order = response.json
    assert order["id"] == id_
    compare_order(order, stub, False)
    response = client.get('/api/v1/orders', query_string={"orderId": 2785})
    assert response.status_code == 404


def test_order_status_change(client):
    stub = get_stub(client)

    for old_status, new_status, is_valid in STATUS_CHANGE:
        stub["status"] = old_status
        order_id_ = client.post('/api/v1/orders/test', json=stub).json["id"]
        stub["status"] = new_status
        stub["id"] = order_id_
        response = client.put(f'/api/v1/orders/{order_id_}', json=stub)
        expected_result = 200 if is_valid else 400
        assert response.status_code == expected_result


def test_order_change(client):
    stub = stub_w_id(client)
    order_id = stub["id"]

    illegal_json = stub.copy()
    illegal_json["client_id"] = 1234
    response = client.put(f'/api/v1/orders/{order_id}', json=illegal_json)
    assert response.status_code == 400
    illegal_json = stub.copy()
    illegal_json["driver_id"] = 1234
    response = client.put(f'/api/v1/orders/{order_id}', json=illegal_json)
    assert response.status_code == 400

    stub["date_created"] = "2021-03-16T14:01:03"
    response = client.put(f'/api/v1/orders/{order_id}', json=stub)
    assert response.status_code == 200

    order = client.get('/api/v1/orders', query_string={"orderId": order_id}).json
    compare_order(order, stub, False)
