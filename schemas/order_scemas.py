# TODO POST /orders Добавить новый заказ - тело заказа, без айди
#     OrderNoId:
#       type: object
#       properties:
#         client_id:
#           type: integer
#           format: int64
#         driver_id:
#           type: integer
#           format: int64
#         date_created:
#           type: string
#           format: date-time
#         status:
#           type: string
#           description: Order Status
#           enum:
#           - not_accepted
#           - in_progress
#           - done
#           - cancelled
#         address_from:
#           type: string
#         address_to:
#           type: string


# TODO PUT /orders/{orderId} Изменить заказ - всё тело заказа
#     Order:
#       type: object
#       properties:
#         id:
#           type: integer
#           format: int64
#         client_id:
#           type: integer
#           format: int64
#         driver_id:
#           type: integer
#           format: int64
#         date_created:
#           type: string
#           format: date-time
#         status:
#           type: string
#           description: Order Status
#           enum:
#           - not_accepted
#           - in_progress
#           - done
#           - cancelled
#         address_from:
#           type: string
#         address_to:
#           type: string
