# data/test_data.py

valid_pet = {
    "id": 12345,
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "name": "Bob",
    "photoUrls": ["https://example.com/photo1.jpg"],
    "tags": [
        {
            "id": 1,
            "name": "friendly"
        }
    ],
    "status": "available"
}

updated_pet = {
    "id": 12345,
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "name": "Bob Updated",
    "photoUrls": ["https://example.com/photo2.jpg"],
    "tags": [
        {
            "id": 1,
            "name": "friendly"
        },
        {
            "id": 2,
            "name": "playful"
        }
    ],
    "status": "sold"
}

invalid_pet = {
    "id": -999,
    "name": "",
    "status": "unknown"
}