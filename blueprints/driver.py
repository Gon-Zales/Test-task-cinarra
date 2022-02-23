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


# TODO GET /drivers Найти водителя по id
#     get:
#       tags:
#       - drivers
#       summary: Найти водителя по id
#       parameters:
#       - name: driverId
#         in: query
#         description: ID Водителя
#         required: true
#         schema:
#           type: integer
#           format: int64
#       responses:
#         200:
#           description: successful operation
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
