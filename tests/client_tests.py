stub = {"name": "dsd", "is_vip": True}
client_id = -89


def stub_w_id():
    res = stub.copy()
    res["id"] = client_id
    return res


def compare_client(d1, d2, ignore_id):
    assert d1["name"] == d2["name"]
    assert d1["is_vip"] == d2["is_vip"]
    if ignore_id:
        assert type(d1["id"]) is int
    else:
        assert d1["id"] == d2["id"]


def test_client_create(client):
    response = client.post('/clients', json=stub)
    assert response.status_code == 201
    client_json = response.json
    # TODO write a constructor and override comparison to shorten such validations
    compare_client(client_json, stub, True)
    global client_id
    client_id = client_json["id"]


def test_client_find(client):
    response = client.get('/clients', query_string={"clientId": client_id})
    assert response.status_code == 200
    client_json = response.json
    assert client_json["id"] == client_id
    compare_client(client_json, stub_w_id(), False)
    response = client.get('/clients', query_string={"clientId": 2785})
    assert response.status_code == 404


def test_client_delete(client):
    client_json = client.get('/clients', query_string={"clientId": client_id}).json
    response = client.delete('/clients/' + str(client_id))
    assert response.status_code == 200
    deleted = response.json
    assert deleted == client_json
    response = client.delete('/clients/' + str(client_id))
    assert response.status_code == 404
