client_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "is_vip": {"type": "boolean"},
        "name": {"type": "string"}
    },
    "required": ["id", "is_vip", "name"]
}
