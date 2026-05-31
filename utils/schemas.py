# utils/schemas.py

PET_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "category": {"type": "object"},
        "name": {"type": "string"},
        "photoUrls": {"type": "array"},
        "tags": {"type": "array"},
        "status": {"type": "string", "enum": ["available", "pending", "sold"]}
    },
    "required": ["id", "name", "photoUrls", "status"]
}

ORDER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "petId": {"type": "integer"},
        "quantity": {"type": "integer"},
        "shipDate": {"type": "string"},
        "status": {"type": "string"},
        "complete": {"type": "boolean"}
    },
    "required": ["id", "petId", "quantity", "status", "complete"]
}

INVENTORY_SCHEMA = {
    "type": "object",
    "additionalProperties": {"type": "integer"}
}