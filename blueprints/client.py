# TODO POST  /clients Занести в базу клиента
#   /clients:
#     post:
#       tags:
#       - clients
#       summary: Занести в базу клиента
#       requestBody:
#         description: Объект клиента для создания в базе
#         content:
#           application/json:
#             schema:
#               $ref: '#/components/schemas/ClientNoId'
#         required: true
#       responses:
#         201:
#           description: created!
#           content:
#             application/json:
#               schema:
#                 $ref: '#/components/schemas/Client'
#         400:
#           description: Неправильный запрос
#           content: {}


# TODO GET  /clients Найти клиента по ID
#     get:
#       tags:
#       - clients
#       summary: Найти клиента по ID
#       parameters:
#       - name: clientId
#         in: query
#         description: ID клиента
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
#                 $ref: '#/components/schemas/Client'
#         400:
#           description: Неправильный запрос
#           content: {}
#         404:
#           description: Объект в базе не найден
#           content: {}


# TODO DELETE  /clients/{clientId} Удалить клиента из базы
#   /clients/{clientId}:
#     delete:
#       tags:
#       - clients
#       summary: Удалить клиента из базы
#       parameters:
#       - name: clientId
#         in: path
#         description: ID Клиента
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
#                 $ref: '#/components/schemas/Client'
#         400:
#           description: Неправильный запрос
#           content: {}
#         404:
#           description: Объект в базе не найден
#           content: {}


