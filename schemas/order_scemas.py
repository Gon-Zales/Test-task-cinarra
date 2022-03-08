order_no_id_schema = {
    "type": "object",
    "properties": {
        "client_id": {"type": "integer"},
        "driver_id": {"type": "integer"},

        "date_created": {"type": "string($date-time)"},
        "status": {
            "description": "Order Status",
            "enum": [
                "not_accepted",
                "in_progress",
                "done",
                "cancelled"
            ], "default": "not_accepted"
        },
        "address_from": {"type": "string"},
        "address_to": {"type": "string"},
    },
    "required": ["client_id", "driver_id", "date_created", "status", "address_from", "address_to"]
}


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
