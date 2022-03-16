from datetime import datetime

from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from peewee import DoesNotExist

from models.order_model import Order, NOT_ACCEPTED, STATUS_CHANGE
from schemas.order_schema import order_schema
from schemas.order_no_id_schema import order_no_id_schema

order_api = Blueprint('orders', __name__, url_prefix='/orders')


def order_to_json(order: Order):
    return jsonify({
        'id': order.get_id(),
        'client_id': order.client_id.get_id(),
        'driver_id': order.driver_id.get_id(),
        "date_created": order.date_created.isoformat(),
        "status": order.status,
        "address_from": order.address_from,
        "address_to": order.address_to,
    })


@order_api.route('', methods=['POST'])
@expects_json(order_no_id_schema)
def create():
    if request.json["status"] != NOT_ACCEPTED:
        return "status on creation can only be 'not_accepted'", 400
    order = Order.create_from_json(request.json)
    return order_to_json(order), 201


@order_api.route('/test', methods=['POST'])
@expects_json(order_no_id_schema)
def create_any_status():
    from app import app
    if not app.testing:  # Probably should think for a minute in search of a more elegant solution
        return 90000
    order = Order.create_from_json(request.json)
    return order_to_json(order), 201


@order_api.route('', methods=['GET'])
def get():
    try:
        order = Order.get_by_id(request.values["orderId"])
    except DoesNotExist as _:
        return "order id is not found", 404
    return order_to_json(order), 200


def update_order(order, json):
    if json["status"] == NOT_ACCEPTED:
        order.client_id = json['client_id']
        order.driver_id = json['driver_id']
        order.date_created = datetime.fromisoformat(json['date_created'])
    else:
        order.status = json["status"]
    order.save()


@order_api.route('<order_id>', methods=['PUT'])
@expects_json(order_schema)
def change(order_id):
    try:
        order = Order.get_by_id(order_id)
    except DoesNotExist as _:
        return "order id is not found", 404
    try:
        new_status = request.json["status"]
        if (order.status, new_status) not in STATUS_CHANGE and order.status != new_status:
            return "invalid status change", 400
        update_order(order, request.json)
        return order_to_json(order), 200
    except Exception as e:
        return e.__str__(), 400
