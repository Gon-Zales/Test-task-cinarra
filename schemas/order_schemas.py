order_no_id_schema = {
    "type": "object",
    "properties": {
        "client_id": {"type": "integer"},
        "driver_id": {"type": "integer"},

        "date_created": {"type": "string"},
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

order_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "client_id": {"type": "integer"},
        "driver_id": {"type": "integer"},

        "date_created": {"type": "string"},
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
    "required": ["id", "client_id", "driver_id", "date_created", "status", "address_from", "address_to"]
}
