from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from peewee import DoesNotExist

from models.client_model import Client
from schemas.client_schemas import client_no_id_schema

client_api = Blueprint('clients', __name__, url_prefix='/clients')


def client_to_json(client):
    return jsonify({'id': client.get_id(), 'name': client.name, 'is_vip': client.is_vip})


@client_api.route('', methods=['POST'])
@expects_json(client_no_id_schema)
def create():
    client = Client.create_from_json(request.json)
    return client_to_json(client), 201


@client_api.route('', methods=['GET'])
def get():
    try:
        client = Client.get_by_id(request.args["clientId"])
    except DoesNotExist as _:
        return "client id is not found", 404
    return client_to_json(client), 200


@client_api.route('<client_id>', methods=['DELETE'])
def delete(client_id):
    try:
        client = Client.get_by_id(client_id)
        client.delete_instance()
    except DoesNotExist as _:
        return "Client id is not found", 404
    return client_to_json(client), 200
