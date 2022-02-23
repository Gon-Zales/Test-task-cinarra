# TODO POST  /orders Добавить новый заказ
#   /orders:
#     post:
#       tags:
#       - orders
#       summary: Добавить новый заказ
#       requestBody:
#         description: тело для нового заказа
#         content:
#           application/json:
#             schema:
#               $ref: '#/components/schemas/OrderNoId'
#         required: true
#       responses:
#         201:
#           description: created!
#           content:
#             application/json:
#               schema:
#                 $ref: '#/components/schemas/Order'
#         400:
#           description: плохой json
#           content: {}

# TODO GET  /orders Найти заказ
#     get:
#       tags:
#       - orders
#       summary: Найти заказ
#       description: возвращает один заказ
#       parameters:
#       - name: orderId
#         in: query
#         description: ID заказа
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
#                 $ref: '#/components/schemas/Order'
#         400:
#           description: Неправильный запрос
#           content: {}
#         404:
#           description: Объект в базе не найден
#           content: {}

# TODO PUT  /orders/{orderId}  Изменить заказ
#   /orders/{orderId}:
#     put:
#       tags:
#       - orders
#       summary: Изменить заказ
#       parameters:
#       - name: orderId
#         in: path
#         description: id заказа
#         required: true
#         schema:
#           type: integer
#           format: int64
#       requestBody:
#         description: Изменённый заказ
#         content:
#           application/json:
#             schema:
#               $ref: '#/components/schemas/OrderNoId'
#         required: true
#       responses:
#         200:
#           description: Изменено!
#           content:
#             application/json:
#               schema:
#                 $ref: '#/components/schemas/Order'
#         400:
#           description: Неправильный запрос
#           content: {}
#         404:
#           description: Объект в базе не найден
#           content: {}
