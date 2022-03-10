from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from peewee import DoesNotExist

from models.driver_model import Driver
from schemas.driver_no_id import driver_no_id_schema

driver_api = Blueprint('drivers', __name__, url_prefix='/drivers')


def driver_to_json(driver):
    return jsonify({'id': driver.get_id(), 'name': driver.name, 'car': driver.car})


@driver_api.route('', methods=['POST'])
@expects_json(driver_no_id_schema)
def create():
    driver = Driver.create_from_json(request.json)
    return driver_to_json(driver), 201


@driver_api.route('', methods=['GET'])
def get():
    try:
        driver = Driver.get_by_id(request.values["driverId"])
    except DoesNotExist as _:
        return "Driver id is not found", 404
    return driver_to_json(driver), 200


@driver_api.route('<driver_id>', methods=['DELETE'])
def delete(driver_id):
    try:
        driver = Driver.get_by_id(driver_id)
        driver.delete_instance()
    except DoesNotExist as _:
        return "Driver id is not found", 404
    return driver_to_json(driver), 200
