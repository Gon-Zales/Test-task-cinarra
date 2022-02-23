from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from peewee import DoesNotExist

from models.driver_model import Driver
from schemas.driver_id import driver_id_schema
from schemas.driver_no_id import driver_no_id_schema

driver_api = Blueprint('drivers', __name__, url_prefix='/drivers')


@driver_api.route('', methods=['POST'])
@expects_json(driver_no_id_schema)
def create():
    driver = Driver.create_from_json(request.json)
    return jsonify({'id': driver.get_id(), 'name': driver.name, 'car': driver.car}), 201


@driver_api.route('', methods=['GET'])
@expects_json(driver_id_schema)
def get():
    try:
        driver = Driver.get_by_id(request.json["driverId"])
    except DoesNotExist as ie:
        return "Driver id is not found", 404
    return jsonify({'id': driver.get_id(), 'name': driver.name, 'car': driver.car}), 200

# TODO DELETE  /drivers/{driverId} Удалить водителя из системы
#   /drivers/{driverId}:
#     delete:
#       tags:
#       - drivers
#       summary: Удалить водителя из системы
#       parameters:
#       - name: driverId
#         in: path
#         description: ID водителя для удаления
#         required: true
#         schema:
#           type: integer
#           format: int64
#       responses:
#         204:
#           description: Удалено
#           content:
#             application/json:
#               schema:
#                 $ref: '#/components/schemas/Driver'
#         400:
#           description: Неправильный запрос
#           content: {}
#         404:
#           description: Объект в базе не найден
#           content: {}
