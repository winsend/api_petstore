import random
from datetime import datetime, UTC
from models.order import Order

class OrderFactory:
    
    @staticmethod
    def create(status: str = "placed") -> Order:
        return Order(
            petId = random.randint(1000, 9999),
            quantity = random.randint(1, 10),
            shipDate = datetime.now(UTC),
            status = status,
            complete = status == "delivered"
        )

    @staticmethod
    def create_dict(status: str = "placed", **kwargs) -> dict:
        order = OrderFactory.create(status=status)
        if kwargs:
            order = order.model_copy(update=kwargs)
        return order.model_dump(mode="json")   # Важно для datetime!