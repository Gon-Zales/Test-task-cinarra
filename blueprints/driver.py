from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from peewee import DoesNotExist

from models.driver_model import Driver
from schemas.driver_id import driver_id_schema
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
@expects_json(driver_id_schema)
def get():
    try:
        driver = Driver.get_by_id(request.json["driverId"])
    except DoesNotExist as ie:
        return "Driver id is not found", 404
    return driver_to_json(driver), 200


@driver_api.route('', methods=['DELETE'])
@expects_json(driver_id_schema)
def delete():
    try:
        driver_id = request.json["driverId"]
        driver = Driver.get_by_id(driver_id)
        deleted_id = driver.delete_instance()
        if driver_id != deleted_id:
            raise Exception("Wrong driver deleted")
    except DoesNotExist as ie:
        return "Driver id is not found", 404
    return driver_to_json(driver), 200
