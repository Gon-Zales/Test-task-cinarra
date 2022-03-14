from models.order_model import ORDER_STATUS, NOT_ACCEPTED
from client_tests import stub as client_stub
from driver_tests import stub as driver_stub

client_id = None
driver_id = None
order_id = -89


def get_stub():
    return {
        "client_id": client_id,
        "driver_id": driver_id,
        "date_created": "2022-03-13T13:45:50.536Z",
        "status": NOT_ACCEPTED,
        "address_from": "dsd",
        "address_to": "dsd",
    }


def stub_w_id():
    res = get_stub().copy()
    res["id"] = order_id
    return res


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
    global driver_id, client_id
    driver_id = client.post('/drivers', json=driver_stub).json["id"]
    client_id = client.post('/clients', json=client_stub).json["id"]
    response = client.post('/orders', json=get_stub())
    assert response.status_code == 201
    order = response.json
    compare_order(order, get_stub(), True)

    stub = get_stub()
    for i in range(1, 3):
        stub["status"] = ORDER_STATUS[i]
        response = client.post('/orders', json=stub)
        assert response.status_code == 400
    global order_id
    order_id = order["id"]


def test_order_find(client):
    response = client.get('/orders', query_string={"orderId": order_id})
    assert response.status_code == 200
    order = response.json
    assert order["id"] == order_id
    compare_order(order, stub_w_id(), False)
    response = client.get('/orders', query_string={"orderId": 2785})
    assert response.status_code == 404


def test_order_change(client):
    order_json = client.get('/orders', query_string={"orderId": order_id}).json
    global driver_id, client_id
    driver_id = client.post('/drivers', json=driver_stub).json["id"]
    client_id = client.post('/clients', json=client_stub).json["id"]
    stub = stub_w_id()

    stub["client_id"] = order_json["client_id"] = client_id
    stub["driver_id"] = order_json["driver_id"] = driver_id
    stub["date_created"] = order_json["date_created"] = "2021-03-13T13:45:50.536Z"
    response = client.put(f'/orders/{order_id}', json=order_json)
    assert response.status_code == 200

    for i in range(1, 3):
        stub["status"] = order_json["status"] = ORDER_STATUS[i]
        response = client.put(f'/orders/{order_id}', json=order_json)
        order = client.get('/orders', query_string={"orderId": order_id}).json
        assert response.status_code == 200 and order["status"]==ORDER_STATUS[i]

    order = client.get('/orders', query_string={"orderId": order_id}).json
    compare_order(order, stub, False)
