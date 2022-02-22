from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json

from models.driver_model import Driver
from schemas.driver_no_id import driver_no_id_schema


driver_api = Blueprint('drivers', __name__, url_prefix='/drivers')


@driver_api.route('', methods=['POST'])
@expects_json(driver_no_id_schema)
def create():
    driver = Driver.create_from_json(request.json)
    return jsonify({'id': driver.get_id(), 'name': driver.name, 'car': driver.car}), 201
