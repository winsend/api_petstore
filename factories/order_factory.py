import random


class OrderFactory:

    @staticmethod
    def create_data_order(
        status: str = "placed"
    ) -> dict:

        return {
            "id": random.randint(100000, 999999),
            "petId": random.randint(1000, 9999),
            "quantity": random.randint(1, 10),
            "shipDate": "2026-06-01T10:24:23.859Z",
            "status": status,
            "complete": True
        }